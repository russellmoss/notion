---
title: "Note taking tool"
content_type: "Article"
theme: "RevOps, Leadership"
status: "Not started"
publication_date: ""
notion_url: "https://www.notion.so/Note-taking-tool-2756c059767380698c0bebf7d41f5b53"
---

# I Vibe-Coded a Brain Extension in 4 Hours and Now I Never Forget Anything

Last Tuesday I had three back-to-back calls. Important ones. The kind where decisions get made and budgets get approved and someone definitely said something critical that I should remember but won't.

By Thursday, it was all gone. Mental vapor. I knew we'd discussed pipeline metrics and something about Q1 planning but the specifics? The action items? The brilliant insight someone dropped at minute 47? Vanished into the cognitive ether where all meeting content goes to die.

So I did what any reasonable RevOps manager would do. I spent 4 hours building a system that turns me into a cyborg with perfect recall.

Not kidding. This thing is my external brain now.

## The Problem With Human Memory (It Sucks)

Here's what nobody admits: We're all pretending to remember things. Taking notes we'll never read again. Recording meetings we'll never replay. Creating "knowledge bases" that are really just graveyards for good ideas.

I tested myself last month. Tried to recall specifics from a "critical" meeting from two weeks prior. Could remember it was about conversion metrics. That's it. Not the actual metrics. Not the decisions. Not who was supposed to do what. Just... conversion metrics happened.

Meanwhile I'm managing revenue operations for a fintech, transitioning from running a winery, trying to keep seventeen different workstreams straight, and my brain is operating like a goldfish with ADHD. Something had to change.

## The System That Changed Everything

GitHub repo: https://github.com/russellmoss/-notes

Here's what I vibe-coded over one slightly manic Saturday afternoon fueled by cold brew and spite for my own forgetfulness:

**The Inputs:**

- Otter.ai recordings of every meeting (transcripts + AI summaries)

- MyScript Nebo for handwritten notes on my tablet (because typing in meetings makes you look like you're not paying attention even though you totally are)

- Random thoughts dictated to my phone while walking

- Screenshots, documents, whatever my brain might need later

**The Magic Middle Layer:**
A Next.js app that:

1. Monitors my Google Drive folders for new content

1. Processes everything through OpenAI to extract the actual important stuff

1. Structures it all into searchable, queryable data

1. Pushes everything to a Notion database with proper tagging, dates, action items, the works

**The Output:**
A living knowledge base I can query with natural language through Claude or GPT. "What did we decide about pricing models in January?" Boom. Full context, original transcript link, action items, who said what.

It's not just storage. It's active memory augmentation.

## Why MyScript + Otter Is the Power Combo Nobody's Talking About

Look. I have terrible handwriting. Like, doctor-prescription-level bad. But MyScript converts my chicken scratch to text at 90% accuracy. NINETY PERCENT. From my handwriting that looks like a spider fell in ink and had a seizure across the page.

So now I take notes on my tablet during meetings. Real notes. The kind where you draw arrows between ideas and underline important stuff three times and write "THIS!!!" in the margins. MyScript converts it all to text, maintains the structure, exports to a Google Doc.

Meanwhile Otter is recording everything. Getting every word, every pause, every "um, actually, wait, let me rethink that." The AI summary catches the big picture. The transcript catches the details.

Combine them? You get human insight (my notes) plus complete record (Otter) plus AI synthesis (GPT-4). It's like having a perfect assistant who attended every meeting, took perfect notes, and can recall everything instantly.

## The 4-Hour Build (Or: How I Learned to Stop Worrying and Love the Chaos)

Saturday, 2pm: Realized I'd forgotten an entire client meeting from Monday. Not just details. The ENTIRE MEETING. Knew it happened because it was on my calendar. No other evidence it existed.

2:15pm: Rage-opened VS Code.

2:30pm: Started building. No planning. No architecture diagrams. Just pure "this needs to exist" energy.

3:45pm: First version working. Ugly as sin but functional.

5:30pm: Cron jobs running. Notion database populating. Google Drive folders being monitored.

6:00pm: Tested with a week of old notes. Everything converted, structured, searchable.

6:15pm: Posted about it on LinkedIn while eating leftover Thai food. Peak productivity.

## What This Actually Means for RevOps (Everything)

In RevOps, context is currency. Knowing why we changed that lead scoring model in October matters when we're debugging conversion issues in March. Remembering the exact objection the CFO raised about tool consolidation shapes how you present the next proposal.

Before this system:

- "I think we discussed this already..." *frantically searches Slack for 20 minutes*

- "Wasn't there a decision about..." *nobody remembers*

- "Who was supposed to..." *checks seven different tools, finds nothing*

After this system:

- "In our January 15 standup at minute 23, Sarah proposed adjusting the SQL threshold from 20 to 30 points based on December's cohort analysis"

- "The CFO's exact concern was tool sprawl creating data silos, mentioned in three separate meetings"

- "Here are all five conversations where we discussed commission structure changes, with contradictions highlighted"

It's not about having a better memory. It's about having **accessible** memory. Queryable memory. Memory that works like your brain wishes it worked.

## The Part Where I Get Philosophical About Cognition and Tools

We're already cyborgs. Your phone is external memory. Google is external knowledge. Calculators are external computation. This just makes it explicit and actually useful.

The human brain is incredible at pattern recognition, creativity, and synthesis. It's terrible at storage and recall. So why are we pretending otherwise? Why are we wasting cognitive cycles trying to remember details when we could be using those cycles to actually think?

This isn't about replacing human intelligence. It's about amplifying it. Like how I used to optimize grape yields with soil sensors and weather data, now I'm optimizing cognitive yield with transcription and language models.

## The Unexpected Joy of Never Forgetting

Last week, a colleague mentioned something about "that idea you had about segmentation." I had no memory of this idea. None. Zero recollection of ever having thoughts about segmentation.

Queried my knowledge base: "segmentation idea Russell."

Found it. A casual comment I'd made three weeks ago during a standup about using engagement scoring for segment triggers instead of demographic data. Complete with implementation notes I'd scribbled during the discussion.

My colleague was impressed I "remembered" the details so clearly. I didn't correct them ;)

## Build Your Own or Stay Forgetful

The code's all there. Open source. No course to buy, no newsletter to subscribe to. Just clone the repo and go.

Will it work perfectly out of the box? No. You'll need to adjust it for your workflow, your tools, your brain. That's the point. This isn't a product. It's a framework for building your own cognitive exoskeleton.

Or keep pretending you'll remember everything from that important meeting. Keep taking notes you'll never review. Keep recording meetings you'll never replay.

Your choice.

But I'll tell you what. Since building this, I've recalled every action item, followed up on every commitment, and referenced specific conversations with scary accuracy. My team thinks I became a productivity god overnight.

Really, I just accepted that my brain needed a backup drive. And then I built one in an afternoon fueled by frustration and caffeine.

That's not cheating. That's evolution.

Now if you'll excuse me, I need to go query my knowledge base for "what was I supposed to be doing right now" because I definitely had something important but started writing this instead.

---

*Russell Moss is a RevOps Manager who believes the best fertilizer is the footsteps of the farmer, but sometimes you need to let the machines handle the memory so you can focus on the thinking. He spent 17+ years forgetting things in vineyards before forgetting things in fintech.*

