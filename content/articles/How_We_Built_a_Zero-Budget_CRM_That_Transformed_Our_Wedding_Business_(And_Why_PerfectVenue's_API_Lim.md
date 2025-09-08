---
title: "How We Built a Zero-Budget CRM That Transformed Our Wedding Business (And Why PerfectVenue's API Limitations Made It Better)"
content_type: "Article"
theme: "Sales, Marketing, RevOps"
status: "draft"
publication_date: "2026-02-11"
notion_url: "https://www.notion.so/How-We-Built-a-Zero-Budget-CRM-That-Transformed-Our-Wedding-Business-And-Why-PerfectVenue-s-API-Lim-2686c0597673804fb6def7f74e85233f"
---

# How We Built a Zero-Budget CRM That Transformed Our Wedding Business (And Why PerfectVenue's API Limitations Made It Better)

**Sometimes constraints breed the most creative solutions.**

Six months ago, I faced a classic hospitality tech problem: our wedding venue needed a CRM that actually understood how weddings work, but enterprise solutions cost $50K+ annually and still required extensive customization. PerfectVenue, our booking platform, offered no API access for automation. Our leads were scattered across emails, spreadsheets, and sticky notes.

So I did what any wine-industry-turned-RevOps professional would do: **I built our own system using Google Sheets, AI, and a healthy dose of systems thinking.**

Today, that "makeshift" CRM handles 200+ wedding leads monthly, automates 80% of our follow-ups, and increased our tour booking rate by 47%. Here's how we did it – and why the constraints actually made it better.

## The Architecture: When Google Sheets Becomes a Power Tool

At its core, our CRM is a Google Sheet on steroids. But calling it just a spreadsheet is like calling a Formula 1 car just a vehicle.

**The backend runs on Google Apps Script that:**

- Monitors lead progression through 6 distinct stages (Hot → Hot-Manual → Warm-no call → Warm-no tour → Cold → Closed)

- Triggers Zapier webhooks for automated nurture sequences

- Creates real-time alerts for time-sensitive actions

- Protects array formulas from accidental overwrites (columns AF-AJ for the spreadsheet nerds)

- Deduplicates and merges lead data automatically

**The frontend is a custom web dashboard that:**

- Provides instant visibility into pipeline health

- Shows dismissible alerts for hot leads and stale opportunities

- Integrates OpenAI for natural language queries ("Show me all leads who haven't been contacted in 7 days")

- Tracks conversion metrics at each stage of our funnel

## The PerfectVenue Problem That Became Our Superpower

Here's where it gets interesting. PerfectVenue (now part of Tripleseat) doesn't offer API access to its users. Most would see this as a dealbreaker. We saw it as an opportunity to get creative.

**Our solution: An email parser powered by Claude AI.**

Twice daily (9am and 4pm), a Google Script:

1. Scans our inbox for WeddingPro inquiries forwarded by PerfectVenue

1. Sends the email content to Claude with this prompt: *"Extract guest name, email, phone, event date, guest count, and message. Determine if this needs manual response (specific questions) or automated flow (general inquiry)."*

1. Generates a summary email with pre-filled CRM entry links

1. Categorizes leads as "Hot" (automated sequence) or "Hot-Manual" (needs personalized response)

The 5-minute overlaps between sweeps ensure zero leads fall through the cracks. Duplicate detection prevents double-processing. The system has processed 1,000+ inquiries with 99.7% accuracy.

## The Nurture Sequences That Actually Convert

This is where domain expertise meets automation. Different lead types trigger different sequences:

**"Hot" leads (general inquiries) receive:**

- Immediate lookbook PDF (showcasing real weddings, not stock photos)

- Personalized text within 4 hours from our events manager

- Email series highlighting different wedding styles we've hosted

- Social proof (testimonials) on days 3, 7, and 14

- Calendly link with dynamic availability

**"Hot-Manual" leads (specific questions) get:**

- Manual response within 2 hours addressing their specific concerns

- Custom pricing if they asked about budgets

- Availability confirmation for their date

- Followed by the standard nurture sequence

**"Warm-no call" leads trigger:**

- SMS asking about their planning timeline

- Email with virtual tour video

- Limited-time booking incentive (expires in 72 hours)

- Final "we'd love to host you" message before moving to Cold

**The results speak volumes:**

- Hot → Tour conversion: 34% (industry average: 15-20%)

- Tour → Booking conversion: 52% (industry average: 30-35%)

- Average response time: 12 minutes (industry average: 48 hours)

- Email engagement rate: 67% (industry average: 20-25%)

## The AI Integration That Changes Everything

We integrated OpenAI directly into the dashboard. Our events manager can now ask questions like:

- "Which leads from Instagram haven't had a tour yet?"

- "Show me everyone who mentioned 'micro wedding' in the last month"

- "What's our conversion rate for Saturday vs Sunday weddings?"

The AI understands our specific business context – it knows that "Tour Scheduled" is different from "Tour Completed," that "Hot-Manual" means personalized attention, that proposal-to-deposit timing affects cash flow.

This isn't just about querying data. It's about making data accessible to people who think in stories and relationships, not SQL and spreadsheets.

## Why This Matters Beyond Wine Country

I've managed vineyards in New Zealand, run wineries in the Hudson Valley, and now optimize revenue operations for fintech. The pattern is always the same: **Whether you're optimizing grape yields or SaaS conversion rates, the approach remains constant – data, systems thinking, and scalable solutions.**

But here's what I've learned: The best systems aren't built by consultants or vendors. They're built by people who live the problems daily and have just enough technical knowledge to be dangerous.

**The investment:**

- Time: 2 weeks of evenings and weekends

- Cost: $0 (using free tiers of everything)

- Technical expertise required: Basic JavaScript and a willingness to prompt AI

**The return:**

- 47% increase in tour booking rate

- 80% reduction in manual follow-up time

- 25% increase in average booking value (better lead qualification)

- 100% visibility into pipeline health

## The Leadership Lesson Hidden in the Code

Building this system taught me something crucial about modern leadership: **Your job isn't to have all the answers. It's to create systems that surface the right questions at the right time.**

Every morning, our events manager opens the dashboard and immediately sees:

- Who needs a follow-up call

- Which hot leads clicked but didn't book

- What stage each lead is in

- Exactly what action to take next

She doesn't need to remember. She doesn't need to check multiple systems. She just needs to execute on clear, prioritized actions.

This is what I mean by creating a culture of joy and belonging through systems. When your team spends time building relationships instead of managing spreadsheets, when they can see their impact in real-time, when the system celebrates their wins automatically – that's when work becomes meaningful.

## Your Playbook to Build This Tomorrow

**For the wine/hospitality folks who think this is too technical:**

1. Start with your existing spreadsheet

1. Use Claude/ChatGPT to write the code (copy my prompts)

1. Build one automation at a time

1. Test with 10 leads before scaling

**For the RevOps professionals stuck with inflexible systems:**

1. Stop waiting for IT approval

1. Build a proof of concept with free tools

1. Show results, then ask for resources

1. Remember: Perfect is the enemy of good enough

**The prompts that built this:**

- "Create Google Apps Script that monitors a sheet for leads older than 24 hours without follow-up"

- "Build a webhook trigger that sends data to Zapier when lead stage changes"

- "Parse this email to extract wedding inquiry details and categorize as hot or manual response needed"

## The Bottom Line

We're running a modern wedding venue with a CRM built on Google Sheets, powered by AI, and held together by creative workarounds. It shouldn't work this well. But it does – because it was built by someone who's stood in a tasting room at 9pm entering contacts, who's watched great leads go cold because of slow follow-up, who understands that in hospitality, speed and personalization aren't nice-to-haves – they're everything.

The future isn't about choosing between high-tech and high-touch. It's about using technology to be more human, not less. It's about building systems that give your team superpowers, not replace them.

**Whether you're pouring wine or shipping code, the principle remains: Build systems that scale relationships, not just transactions.**

---

*Currently building revenue operations at Savvy Wealth while applying vineyard management principles to SaaS metrics. Previously: General Manager at Milea Estate Vineyard, where every wedding is a harvest and every system is a trellis.*

What data-driven hospitality challenge are you solving with unexpected tools? Let's connect and share war stories.

#RevOps #HospitalityTech #WeddingIndustry #Innovation #AI #Leadership #WineIndustry #Automation #CRM #SystemsThinking

