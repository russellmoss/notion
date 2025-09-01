import os
import json
import requests
from datetime import datetime
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
NOTION_TOKEN = os.environ.get('NOTION_TOKEN')
DATABASE_ID = os.environ.get('NOTION_DATABASE_ID')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_TO = 'russell@mileaestatevineyard.com'
EMAIL_FROM = 'russell@mileaestatevineyard.com'

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

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
            print(f"Error processing block: {e}")
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
    else:
        return ''

def sync_notion_to_github():
    """Main sync function"""
    print("Starting Notion to GitHub sync...")
    
    # Get database items
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to query database: {response.text}")
    
    results = response.json()['results']
    
    changes = []
    
    # Process each item
    for item in results:
        # Get properties
        properties = item['properties']
        
        # Extract metadata
        title = get_property_value(properties.get('Title', properties.get('Name', {})))
        content_type = get_property_value(properties.get('Content Type', {}))
        theme = get_property_value(properties.get('Theme', {}))
        status = get_property_value(properties.get('Status', {}))
        pub_date = get_property_value(properties.get('Publication Date', {}))
        
        if not title:
            continue
            
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
        
        # Save markdown file
        md_path = f"{folder}/{filename}.md"
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
        old_content = ""
        if os.path.exists(md_path):
            with open(md_path, 'r', encoding='utf-8') as f:
                old_content = f.read()
        
        if old_content != full_content:
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(full_content)
            changes.append(f"Updated: {title}")
        
        # Save metadata JSON
        json_path = f"{folder}/{filename}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2)
    
    # Save root table
    table_data = []
    for item in results:
        properties = item['properties']
        table_data.append({
            'title': get_property_value(properties.get('Title', properties.get('Name', {}))),
            'content_type': get_property_value(properties.get('Content Type', {})),
            'theme': get_property_value(properties.get('Theme', {})),
            'status': get_property_value(properties.get('Status', {})),
            'publication_date': get_property_value(properties.get('Publication Date', {}))
        })
    
    with open('content_table.json', 'w', encoding='utf-8') as f:
        json.dump(table_data, f, indent=2)
    
    print(f"Sync complete! {len(changes)} items updated")
    
    return changes

def send_email(changes):
    """Send email notification"""
    if not changes:
        return
        
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = f'Notion Sync Complete - {len(changes)} items updated'
        
        body = "The following items were updated:\n\n"
        for change in changes:
            body += f"• {change}\n"
        
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
        if changes and EMAIL_PASSWORD:
            send_email(changes)
    except Exception as e:
        print(f"Sync failed: {e}")
        exit(1)
