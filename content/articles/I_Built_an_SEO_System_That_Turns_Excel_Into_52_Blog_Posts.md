---
title: "I Built an SEO System That Turns Excel Into 52 Blog Posts"
content_type: "Article"
theme: "Marketing"
status: "draft"
publication_date: "2026-01-06"
notion_url: "https://www.notion.so/I-Built-an-SEO-System-That-Turns-Excel-Into-52-Blog-Posts-2686c0597673802791a2fc60a745d050"
---

# I Built an SEO System That Turns Excel Into 52 Blog Posts—And It's Optimized for Both Google AND ChatGPT

**We were bleeding $30K/year on content that didn't rank. So I built a system that transforms Excel rows into SEO-optimized blog posts in 30 minutes instead of 8 hours. Here's the $0 blueprint.**

Last month, I discovered our blog posts weren't showing up in ChatGPT answers about Hudson Valley wineries. Our competitors were. That's when I realized: **Traditional SEO is only half the game now.**

So I built the **SEO Prompter**—a system that generates blog posts optimized for both Google rankings AND AI citations. It's already created 12 posts ranking on page one, with 3 appearing in Perplexity answers.

## The Dual SEO Problem That's Killing Your Traffic

Here's what most marketers miss: You need to rank in TWO places now:

1. **Google** (traditional SEO)

1. **AI Answers** (LLM SEO)

Your competition is already doing both. While you're optimizing meta descriptions, they're structuring content for Claude, ChatGPT, and Perplexity to cite.

**The real cost isn't just Google traffic—it's becoming invisible to AI-assisted buyers.**

## The System: Excel → Prompt → AI → Optimized Content

### The Architecture That Changes Everything

```plain text
Excel Row (2 minutes to fill comprehensively)
    ↓
Prompt Generator (auto-generates 5000+ word instructions)
    ↓
Claude Project (with your entire knowledge base)
    ↓
Human Review & Edit (15-20 minutes)
    ↓
Published Content (optimized for Google + AI)

```

### The Excel Setup (The Real Magic)

Here's what each row actually contains—17 columns of SEO intelligence:

**But wait—there's more.** The Excel also includes 5 photo columns:

- Photo URLs (hosted on Cloudinary/S3)

- Alt text for each image

- Captions

- Placement instructions

- SEO-optimized filenames

### Why This Comprehensiveness Matters

Each Excel cell feeds directly into the prompt generator, creating:

1. **Author Authority** (E-E-A-T signals)

1. **Strategic Linking**

1. **Visual SEO**

1. **Content Intelligence**

## The Knowledge Base: Your Unfair Advantage

Before any prompt runs, your entire business lives in Claude:

```plain text
knowledge_base/
├── website/
│   ├── all-pages-scraped.md
│   ├── navigation-structure.md
│   └── existing-content.md
├── products/
│   ├── complete-catalog.md (all 47 wines)
│   ├── tasting-notes.md
│   └── pricing-availability.md
├── brand/
│   ├── voice-guidelines.md
│   ├── messaging-framework.md
│   └── terminology-glossary.md
├── local/
│   ├── area-attractions.md
│   ├── restaurants-hotels.md
│   └── transportation-options.md
└── competitors/
    ├── their-content.md
    └── differentiation-points.md

```

**This means Claude never hallucinates facts about your business.** It knows your actual wines, real prices, true locations, genuine awards.

## The 30-Minute Workflow That Replaced 8-Hour Slogs

### What Actually Happens

1. **Fill Excel row** (2 min)

1. **Run prompt generator** (10 seconds)

1. **Execute in Claude Project** (2 min)

1. **Human Review & Polish** (15-20 min)

1. **Publish** (5 min)

**The human review is non-negotiable.** AI generates structure and content, but you ensure quality, accuracy, and working links.

## LLM SEO: The Secret Sauce

The prompter automatically structures content for AI consumption:

### 1. Question-First Architecture

```html
<h2>How do I get from NYC to Hudson Valley wineries?</h2>
<p><strong>Quick answer:</strong> Take Metro-North from Grand Central
to Poughkeepsie (90 min, $30), then Uber to wineries (15 min, $25).</p>

<h3>Detailed Transportation Options:</h3>
<ul>
  <li><strong>Train + Uber:</strong> $55 total, 2 hours door-to-door</li>
  <li><strong>Rental Car:</strong> $75/day, 90-minute drive</li>
  <li><strong>Wine Tour Bus:</strong> $149/person, includes tastings</li>
</ul>

```

### 2. Rich Schema Markup

```json
{
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How do I get from NYC to Hudson Valley wineries?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Take Metro-North from Grand Central..."
    }
  }]
}

```

### 3. Definition Boxes

```html
<div class="definition-box" itemscope itemtype="https://schema.org/DefinedTerm">
  <dt itemprop="name">Hudson Valley AVA</dt>
  <dd itemprop="description">American Viticultural Area established
  in 1982, spanning 3,800 square miles along the Hudson River...</dd>
</div>

```

### 4. Structured Data Tables

```html
<table class="comparison-table">
  <thead>
    <tr>
      <th>Transport Method</th>
      <th>Cost</th>
      <th>Duration</th>
      <th>Pros</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Metro-North + Uber</td>
      <td>$55</td>
      <td>2 hours</td>
      <td>No driving, scenic ride</td>
    </tr>
  </tbody>
</table>

```

## Real Results: Traditional + LLM SEO Combined

### Month 1-2: Foundation

- Set up knowledge base (4 hours)

- Created Excel template (1 hour)

- Built prompt generator (2 days with Claude's help)

- Generated first 12 posts

### Month 2-3: Results

**Google Performance:**

- 8 posts ranking page 1

- "Wineries near NYC" moved from position 28 → 4

- Organic traffic up 34%

- Average position improved by 12.3 spots

**AI Visibility:**

- 3 posts cited in Perplexity

- 2 appearing in ChatGPT responses

- "Hudson Valley wine tours" — we're the primary source

- AI-driven traffic: 0 → 125 visits/month

**Business Impact:**

- Tasting room bookings up 23%

- Wine club signups from blog: 17 (worth $8,500 annually)

- Email list growth: +340 subscribers

- Content cost savings: $15,000

## The External Link Strategy That Actually Works

The prompter suggests 3-5 high-DA external links per post:

### Categories It Pulls From:

1. **Industry Publications** (DA 70+)

1. **Local/Tourism** (DA 60+)

1. **Educational** (DA 80+)

1. **News/Media** (DA 90+)

**Critical:** The system suggests links, but you verify:

- Link still works (404s kill SEO)

- Content is relevant and recent

- Site hasn't become spammy

- Anchor text is natural

## Your 30-Day Implementation Plan

### Days 1-7: Foundation

```bash
# Scrape your website
python scrape_site.py --url yoursite.com --output knowledge_base/

# Export your products/services
python export_products.py --platform shopify --format markdown

# Document brand voice
Create: brand_guidelines.md, tone_of_voice.md, terminology.md

```

### Days 8-14: Excel Setup

- Create content calendar with all 17 columns

- Plan 12 posts (3 months of weekly content)

- Identify pillar/supporting structure

- Research external link opportunities

### Days 15-21: System Build

```bash
# Install SEO Prompter
git clone https://github.com/yourusername/seo-prompter
pip install -r requirements.txt

# Configure for your business
cp config.example.yml config.yml
# Edit with your specifics

# Test prompt generation
python seo_prompter.py --row 1 --test

```

### Days 22-30: Production

- Generate 4 posts

- Review and edit each (15-20 min)

- Publish 2 per week

- Monitor initial performance

## The Investment vs. Return

### Costs:

- **Claude Pro:** $20/month

- **Your time:** 30 min/post editing

- **Initial setup:** 10 hours total

### Returns (Based on Our 3-Month Data):

- **Content savings:** $500/post × 12 = $6,000

- **Time savings:** 7.5 hours/post × 12 = 90 hours

- **Revenue increase:** $45,000 (attributed to blog traffic)

- **Email list value:** 340 subscribers × $25 = $8,500

**ROI: 242X in first quarter**

## Common Pitfalls to Avoid

1. **Skipping the knowledge base** — Generic content won't rank

1. **Not reviewing output** — AI makes mistakes, links break

1. **Ignoring LLM SEO** — Missing 50% of potential traffic

1. **Weak external linking** — Hurts authority signals

1. **Inconsistent publishing** — Momentum matters

## The Bottom Line

The SEO Prompter isn't about cutting corners. It's about amplifying expertise through systematic content generation that serves both traditional search and AI discovery.

**You still need:**

- Deep business knowledge

- Editorial judgment

- Quality standards

- Consistency

**But now you have:**

- 30-minute blog posts instead of 8-hour marathons

- Content optimized for Google AND AI

- Perfect technical SEO every time

- Scalable content production

Since implementing, we've transformed content from a cost center to a revenue driver. The same can work for any business with expertise to share and the discipline to edit AI output into excellence.

---

**P.S.** This article was generated in 31 minutes. Excel row filled → prompt generated → Claude created → I edited → you're reading. The system suggested Wine Spectator and Metro-North as external links, which I verified before including.

**P.P.S.** GitHub repo with complete system drops Monday. Includes Excel template with all 17 columns, prompt generator, and LLM SEO checklist. First 50 get a Loom video of me implementing it live.

**P.P.P.S.** No, this won't work on autopilot. Yes, you need to review every post. No, you don't need technical skills. Yes, this scales to any industry.

#SEO #LLMSEO #AIContent #MarketingAutomation #ContentStrategy #RevOps #DigitalMarketing #ContentMarketing #SmallBusiness #ExcelToSEO

---

**Want the complete Excel template with all 17 columns pre-configured? Comment "EXCEL" and I'll send you the .xlsx file that powers our entire content operation.**

