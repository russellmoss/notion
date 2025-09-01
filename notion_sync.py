import os
import json
import requests
from datetime import datetime
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Configuration
NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
DATABASE_ID = os.environ.get('NOTION_DATABASE_ID')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_TO = 'russell@mileaestatevineyard.com'
EMAIL_FROM = 'russell@mileaestatevineyard.com'

# Format database ID with hyphens if needed
def format_database_id(db_id):
    """Format database ID to include hyphens"""
    # Remove any existing hyphens
    clean_id = db_id.replace('-', '')
    
    # Add hyphens in the correct positions for UUID v4
    if len(clean_id) == 32:
        return f"{clean_id[:8]}-{clean_id[8:12]}-{clean_id[12:16]}-{clean_id[16:20]}-{clean_id[20:]}"
    return db_id

DATABASE_ID = format_database_id(DATABASE_ID)
print(f"Using database ID: {DATABASE_ID}")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def test_connection():
    """Test if we can access the database"""
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to access database: {response.text}")
        return False
    
    print(f"Successfully connected to database: {response.json().get('title', [{}])[0].get('plain_text', 'Untitled')}")
    return True

def clean_filename(title):
    """Clean title for use as filename"""
    if not title:
        return "untitled"
    # Remove special characters
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    # Replace spaces with underscores
    title = title.replace(' ', '_')
    # Limit length
    return title[:100]

def get_page_content(page_id):
    """Get full content of a Notion page"""
    url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    
    all_blocks = []
    has_more = True
    start_cursor = None
    
    while has_more:
        payload = {"page_size": 100}
        if start_cursor:
            payload["start_cursor"] = start_cursor
            
        response = requests.get(url, headers=headers, params=payload)
        data = response.json()
        
        if 'results' in data:
            all_blocks.extend(data['results'])
        
        has_more = data.get('has_more', False)
        start_cursor = data.get('next_cursor')
    
    return all_blocks

def blocks_to_markdown(blocks):
    """Convert Notion blocks to markdown"""
    markdown = []
    
    for block in blocks:
        block_type = block['type']
        
        try:
            if block_type == 'paragraph':
                text = get_text_from_block(block['paragraph'])
                markdown.append(text + '\n')
                
            elif block_type == 'heading_1':
                text = get_text_from_block(block['heading_1'])
                markdown.append(f"# {text}\n")
                
            elif block_type == 'heading_2':
                text = get_text_from_block(block['heading_2'])
                markdown.append(f"## {text}\n")
                
            elif block_type == 'heading_3':
                text = get_text_from_block(block['heading_3'])
                markdown.append(f"### {text}\n")
                
            elif block_type == 'bulleted_list_item':
                text = get_text_from_block(block['bulleted_list_item'])
                markdown.append(f"- {text}\n")
                
            elif block_type == 'numbered_list_item':
                text = get_text_from_block(block['numbered_list_item'])
                markdown.append(f"1. {text}\n")
                
            elif block_type == 'code':
                text = get_text_from_block(block['code'])
                language = block['code'].get('language', '')
                markdown.append(f"```{language}\n{text}\n```\n")
                
            elif block_type == 'quote':
                text = get_text_from_block(block['quote'])
                markdown.append(f"> {text}\n")
                
            elif block_type == 'divider':
                markdown.append("---\n")
                
            elif block_type == 'toggle':
                text = get_text_from_block(block['toggle'])
                markdown.append(f"<details>\n<summary>{text}</summary>\n\n")
                if block['has_children']:
                    children = get_page_content(block['id'])
                    child_markdown = blocks_to_markdown(children)
                    markdown.append(child_markdown)
                markdown.append("</details>\n")
                
            elif block_type == 'callout':
                text = get_text_from_block(block['callout'])
                icon = block['callout'].get('icon', {}).get('emoji', '💡')
                markdown.append(f"> {icon} **Note**: {text}\n")
                
        except Exception as e:
            print(f"Error processing block type {block_type}: {e}")
            continue
    
    return '\n'.join(markdown)

def get_text_from_block(block_data):
    """Extract text from block rich text array"""
    if 'rich_text' not in block_data:
        return ''
    
    text_parts = []
    for text_obj in block_data['rich_text']:
        if text_obj['type'] == 'text':
            text = text_obj['text']['content']
            
            # Apply formatting
            annotations = text_obj.get('annotations', {})
            if annotations.get('bold'):
                text = f"**{text}**"
            if annotations.get('italic'):
                text = f"*{text}*"
            if annotations.get('code'):
                text = f"`{text}`"
            if annotations.get('strikethrough'):
                text = f"~~{text}~~"
                
            text_parts.append(text)
    
    return ''.join(text_parts)

def get_property_value(property_data):
    """Extract value from Notion property"""
    if not property_data:
        return ''
        
    prop_type = property_data['type']
    
    if prop_type == 'title':
        return ''.join([t['plain_text'] for t in property_data['title']])
    elif prop_type == 'rich_text':
        return ''.join([t['plain_text'] for t in property_data['rich_text']])
    elif prop_type == 'select':
        return property_data['select']['name'] if property_data['select'] else ''
    elif prop_type == 'multi_select':
        return ', '.join([s['name'] for s in property_data['multi_select']])
    elif prop_type == 'date':
        return property_data['date']['start'] if property_data['date'] else ''
    elif prop_type == 'status':
        return property_data['status']['name'] if property_data['status'] else ''
    elif prop_type == 'url':
        return property_data['url'] if property_data['url'] else ''
    else:
        return ''

def sync_notion_to_github():
    """Main sync function"""
    print("Starting Notion to GitHub sync...")
    
    # Test connection first
    if not test_connection():
        raise Exception("Cannot connect to Notion database. Please check your token and database ID.")
    
    # Get database items
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to query database: {response.text}")
    
    results = response.json()['results']
    print(f"Found {len(results)} items in database")
    
    # Track different types of changes
    new_items = []
    updated_items = []
    deleted_items = []
    
    # Track all current files
    current_files = set()
    
    # Process each item
    for item in results:
        # Get properties
        properties = item['properties']
        
        # Extract metadata - try different possible property names
        title = (get_property_value(properties.get('Title', {})) or 
                get_property_value(properties.get('Name', {})) or
                get_property_value(properties.get('title', {})) or
                'Untitled')
                
        content_type = get_property_value(properties.get('Content Type', {}))
        theme = get_property_value(properties.get('Theme', {}))
        status = get_property_value(properties.get('Status', {}))
        pub_date = get_property_value(properties.get('Publication Date', {}))
        
        print(f"Processing: {title}")
        
        # Get page content
        page_content = get_page_content(item['id'])
        markdown_content = blocks_to_markdown(page_content)
        
        # Create metadata
        metadata = {
            'title': title,
            'content_type': content_type,
            'theme': theme,
            'status': status,
            'publication_date': pub_date,
            'notion_url': item['url'],
            'last_edited': item['last_edited_time']
        }
        
        # Determine folder
        if content_type and 'article' in content_type.lower():
            folder = 'content/articles'
        elif content_type and 'micro' in content_type.lower():
            folder = 'content/micro-posts'
        else:
            folder = 'content'
        
        # Create filename
        filename = clean_filename(title)
        
        # Track current files
        md_path = f"{folder}/{filename}.md"
        json_path = f"{folder}/{filename}.json"
        current_files.add(md_path)
        current_files.add(json_path)
        
        # Save markdown file
        os.makedirs(folder, exist_ok=True)
        
        # Add front matter
        full_content = f"""---
title: "{title}"
content_type: "{content_type}"
theme: "{theme}"
status: "{status}"
publication_date: "{pub_date}"
notion_url: "{item['url']}"
---

{markdown_content}
"""
        
        # Check if content changed
        if os.path.exists(md_path):
            with open(md_path, 'r', encoding='utf-8') as f:
                old_content = f.read()
            if old_content != full_content:
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(full_content)
                updated_items.append(title)
        else:
            # New file
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
            new_items.append(title)
        
        # Save metadata JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
    
    # Check for deleted files - FIXED: Only check actual content folders, not root
    for folder in ['content/articles', 'content/micro-posts']:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                file_path = f"{folder}/{file}"
                # Only process files, not directories
                if os.path.isfile(file_path) and file_path not in current_files and not file.startswith('.'):
                    # File exists in repo but not in Notion anymore
                    os.remove(file_path)
                    deleted_items.append(file.replace('.md', '').replace('.json', '').replace('_', ' '))
    
    # Remove duplicates from deleted items
    deleted_items = list(set(deleted_items))
    
    # Save root table as JSON
    table_data = []
    for item in results:
        properties = item['properties']
        table_data.append({
            'title': (get_property_value(properties.get('Title', {})) or 
                     get_property_value(properties.get('Name', {})) or
                     'Untitled'),
            'content_type': get_property_value(properties.get('Content Type', {})),
            'theme': get_property_value(properties.get('Theme', {})),
            'status': get_property_value(properties.get('Status', {})),
            'publication_date': get_property_value(properties.get('Publication Date', {}))
        })
    
    with open('content_table.json', 'w', encoding='utf-8') as f:
        json.dump(table_data, f, indent=2)
    
    # Save root table as CSV (matching Notion export format)
    csv_data = []
    for item in results:
        properties = item['properties']
        
        # Extract all properties matching your Notion database
        title = (get_property_value(properties.get('Title', {})) or 
                get_property_value(properties.get('Name', {})) or
                'Untitled')
        
        csv_data.append({
            'Publication Date': get_property_value(properties.get('Publication Date', {})),
            'Title': title,
            'Content Type': get_property_value(properties.get('Content Type', {})),
            'Theme': get_property_value(properties.get('Theme', {})),
            'Platform link': get_property_value(properties.get('Platform link', {})),
            'Assets': get_property_value(properties.get('Assets', {})),
            'CTA / Hashtags': get_property_value(properties.get('CTA / Hashtags', {})),
            'Status': get_property_value(properties.get('Status', {}))
        })
    
    # Sort by publication date (newest first) to match your Notion view
    csv_data.sort(key=lambda x: x['Publication Date'] if x['Publication Date'] else '', reverse=True)
    
    # Write CSV file with UTF-8 BOM for Excel compatibility
    with open('Content_Library.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
        fieldnames = ['Publication Date', 'Title', 'Content Type', 'Theme', 
                     'Platform link', 'Assets', 'CTA / Hashtags', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in csv_data:
            writer.writerow(row)
    
    print("Saved Content_Library.csv to root")
    
    # Print summary
    total_changes = len(new_items) + len(updated_items) + len(deleted_items)
    if total_changes > 0:
        print(f"Sync complete! Changes detected:")
        if new_items:
            print(f"  - {len(new_items)} new items")
        if updated_items:
            print(f"  - {len(updated_items)} updated items")
        if deleted_items:
            print(f"  - {len(deleted_items)} deleted items")
    else:
        print("Sync complete! No changes detected.")
    
    return {
        'new': new_items,
        'updated': updated_items,
        'deleted': deleted_items
    }

def send_email(changes):
    """Send email notification only if there are changes"""
    # Only send if there are actual changes
    if not any([changes['new'], changes['updated'], changes['deleted']]):
        print("No changes detected, skipping email notification")
        return
        
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        
        # Create subject with change summary
        total = len(changes['new']) + len(changes['updated']) + len(changes['deleted'])
        msg['Subject'] = f'Notion Sync: {total} changes detected'
        
        # Build email body
        body = "Notion to GitHub sync completed with the following changes:\n\n"
        
        if changes['new']:
            body += f"📄 NEW ITEMS ({len(changes['new'])}):\n"
            for item in changes['new']:
                body += f"  • {item}\n"
            body += "\n"
        
        if changes['updated']:
            body += f"✏️ UPDATED ITEMS ({len(changes['updated'])}):\n"
            for item in changes['updated']:
                body += f"  • {item}\n"
            body += "\n"
        
        if changes['deleted']:
            body += f"🗑️ DELETED ITEMS ({len(changes['deleted'])}):\n"
            for item in changes['deleted']:
                body += f"  • {item}\n"
            body += "\n"
        
        body += f"\nView changes: https://github.com/russellmoss/notion/commits/main"
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Gmail SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print("Email notification sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    try:
        changes = sync_notion_to_github()
        if EMAIL_PASSWORD:
            send_email(changes)
    except Exception as e:
        print(f"Sync failed: {e}")
        exit(1)
