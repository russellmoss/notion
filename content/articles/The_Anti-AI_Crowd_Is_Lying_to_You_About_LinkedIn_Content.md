---
title: "The Anti-AI Crowd Is Lying to You About LinkedIn Content"
content_type: "Article"
theme: "Marketing"
status: "draft"
publication_date: "2026-02-26"
notion_url: "https://www.notion.so/The-Anti-AI-Crowd-Is-Lying-to-You-About-LinkedIn-Content-26a6c059767380409ee2cea8a3e9285a"
---

# The Anti-AI Crowd Is Lying to You About LinkedIn Content

## The Reality Check Nobody Wants to Admit

Let's drop the pretense: 90% of LinkedIn content is AI-generated. The other 10% is either poetry or lies.

We're all busy professionals running complex businesses, managing teams, hitting revenue targets. If you're spending 4 hours crafting the perfect LinkedIn post, you're either unemployed or terrible at time management. That's 4 hours not spent on your actual job, not spent with your family, not spent building something that matters.

But here's the thing most people get wrong: Using AI doesn't mean sacrificing authenticity. It means being smart about systems and scale—the same principles I apply whether I'm optimizing grape yields or SaaS conversion rates.

I built a content creation system that takes me from idea to published post in under 15 minutes. Not because I'm lazy. Because I'm efficient. And because I'd rather spend my Saturday mornings with my kids than wordsmithing a post about pipeline velocity.

## The Problem With Every Other AI Content Tool

I tried Taplio. I tried Buffer's AI. I tried ChatGPT raw.

They all produce the same vanilla, corporate-speak garbage that reads like it was written by a committee of MBAs who've never actually worked in the trenches. "Leverage synergies to optimize stakeholder value through data-driven insights."

Kill me now.

These tools don't know that I once had to fire a customer mid-wedding because they were berating my staff. They don't know I built a spin-to-win app that increased tasting room revenue 25%. They don't know I've managed vineyards in Bhutan and taught at Cornell.

Generic AI tools produce generic content. And generic content is worse than no content.

## My System: Notion → GitHub → Claude

Here's what I actually built:

### Step 1: The Source of Truth (Notion)

Everything starts in Notion. Every article, every micropost, every half-baked idea at 2 AM. Why? Because Notion is where I think, not where I publish.

My database tracks:

- Content type (article vs. micropost)

- Theme (RevOps, Sales, Leadership, Marketing)

- Status (idea → draft → scheduled → published)

- Publication date

- Engagement metrics (added post-publication)

This isn't just organization—it's pattern recognition. After 50+ posts, I can see what resonates, what tanks, and what themes I'm neglecting.

### Step 2: The Bridge (Python Script)

Here's where it gets interesting. I wrote a Python script that:

1. **Pulls from Notion API** - Grabs all content and metadata

1. **Converts to Markdown** - Preserves formatting, handles all block types

1. **Organizes by Type** - Articles go to `/content/articles/`, microposts to `/content/micro-posts/`

1. **Tracks Changes** - Only updates what's actually changed (incremental sync)

1. **Creates Indexes** - Generates both JSON (for programmatic access) and CSV (for analysis)

1. **Emails Summaries** - Sends notifications only when there are actual changes

The script runs automatically via GitHub Actions. No manual intervention. No "oh shit, I forgot to backup my content."

Key feature: It's not just backing up—it's creating a searchable, version-controlled knowledge base of everything I've ever written. Git gives me diffs, history, branches. I can see how my thinking evolved over time.

### Step 3: The Brain (Claude Project)

This is where the magic happens. I created a Claude Project with:

**The Repository**: My entire GitHub content library loaded as knowledge
**The Context**: My background, experience, writing samples
**The Instructions**: Specific guidelines about my voice, themes, and goals

The instructions are critical. They tell Claude:

- I managed vineyards and wineries for 17+ years

- I'm now in RevOps at a fintech

- I connect wine experiences to business principles

- I use data and concrete examples, not fluff

- I care about building cultures of joy and belonging

- I write like I talk—direct, sometimes provocative, always authentic

When I want to create content, I don't start from scratch. I ask Claude to:

1. Analyze what I've already published

1. Identify gaps in my content calendar

1. Interview me about recent experiences

1. Generate drafts that sound like me, not like GenericLinkedInGuy™

## The Quality Control Layer

Here's what the "AI will replace writers" crowd doesn't understand: AI hallucinates. Constantly.

About 10-20% of what Claude generates is pure fiction. Made-up metrics. Imaginary case studies. Events that never happened. Last week it claimed I increased wine club conversion by 73.4%. The actual number was 50%. Still impressive, but accuracy matters.

So I authenticate everything:

- Verify every metric against my actual dashboards

- Check that examples actually happened

- Ensure technical details are correct

- Adjust tone if it's too aggressive or too soft

This takes 5-10 minutes per piece. Not 4 hours.

## The Results

Since implementing this system:

- Publishing frequency: Up 300%

- Engagement rate: Up 45%

- Time per post: Down 85%

- Weekend hours reclaimed: 100%

But more importantly:

- My content still sounds like me

- My experiences are real

- My insights are earned

- My time is protected

## Why This Matters

The wine industry is dying because it refuses to embrace modern tools and thinking. Winemakers spending 6 months on label design while their tasting rooms convert at 3%.

Don't make the same mistake with your content strategy.

You're not a writer. You're a revenue leader, a founder, an operator. Your value isn't in crafting perfect prose—it's in sharing hard-won insights that help others avoid your mistakes.

Build a system that captures your voice, preserves your authenticity, and respects your time. Or keep spending your Saturdays writing posts that three people will read.

Your choice.

## The Code

Want the actual Python script? The Claude instructions? The Notion template?

I'm not selling a course. I'm not launching a newsletter. If you actually want to build this, message me. I'll send you the GitHub repo.

Because the best way to build a culture of joy and innovation isn't hoarding knowledge—it's sharing what works.

Just like I learned in the vineyard: The best fertilizer is the footsteps of the farmer. But sometimes, you need to let the machines handle the repetitive work so you can focus on what actually needs your expertise.

That's not cheating. That's scaling.

---

*Russell Moss is a RevOps Manager at Savvy Wealth who spent 17+ years optimizing grape yields before optimizing revenue operations. He believes every business problem is fundamentally the same: data, systems, and human motivation.*

