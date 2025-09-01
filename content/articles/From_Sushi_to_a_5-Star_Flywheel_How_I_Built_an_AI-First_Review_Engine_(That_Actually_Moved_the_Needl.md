---
title: "From Sushi to a 5-Star Flywheel: How I Built an AI-First Review Engine (That Actually Moved the Needle)"
content_type: "Article"
theme: "RevOps"
status: "scheduled"
publication_date: "2025-11-04T08:30:00.000-05:00"
notion_url: "https://www.notion.so/From-Sushi-to-a-5-Star-Flywheel-How-I-Built-an-AI-First-Review-Engine-That-Actually-Moved-the-Need-2616c059767380ce9629ecb26f611da3"
---

### **From Sushi to a 5-Star Flywheel: How I Built an AI-First Review Engine (That Actually Moved the Needle)**

### **The spark (at a sushi bar)**

Late one night I grabbed takeout from Mizu Sushi in Hyde Park. On the counter was an NFC “leave us a Google review” card. I tapped my phone, left a five-star review…and immediately thought: *How could we use this at the winery to increase (and improve) reviews?*

I saw three limitations in the typical “counter card” approach:

1. It only lives at POS—most guests never see or use it.

1. There’s no “sell”—no intentional request at the right moment.

1. There’s zero staff attribution—great hospitality is hard to quantify without it.

So I asked ChatGPT (this was GPT-3 era): *“Is there a no-code way to build an NFC/QR review system tied to associates, with 1–3★ going to a manager form and 4–5★ guiding guests to public review sites, all logged to Google Sheets for coaching and incentives?”*

Two weeks later, we had a working system.

---

### **The Version 1.0 build (no-code & nearly free)**

**Hardware & identity**

- Printed small batches of NFC cards (each associate gets 10) and added **unique QR codes** for people who don’t use NFC.

- The card says “Review Us” with **“Your Guide is ____”** (we add names via clear labels). People review *humans* more readily than brands; we saw names show up in public reviews far more often.

**Routing & data capture**

- **Landing page** (hosted on Firebase) with 1–5 stars. The associate ID is appended to the URL so attribution follows the session.

- If a guest selects **1–3★:** they’re sent to a **Jotform** styled to match. Name/email/phone + “what went wrong?” → logged to **Google Sheets** via Zapier; **email/SMS** notify managers instantly so we can fix things fast—often before guests leave.

- If a guest selects **4–5★:** they see links to **Google, Yelp, TripAdvisor**. We also log the positive rating + associate in Sheets (we don’t see the written review unless they post it publicly).

- **On-floor playbook:** Cards sit upright in small wooden holders. The close-out script:

**What happened**

- Before: ~**2–3 reviews/month**, avg **4.6★**.

- After: ~**15 reviews/month**, avg **5.0★** (settling at **4.8★** by July 2025).

- About **20%** of 4–5★ taps converted to public, written reviews—still a meaningful lift.

- Side benefit: faster service recovery (direct messages to managers) and **staff-level coaching** using the associate attribution.

**Cost:** peanuts. Mostly time.

---

### **What I’d build now (Version 2.0, fully coded)**

**Stack & data**

- **Next.js** app with auth (e.g., NextAuth) + **OAuth 2.0** to Google Business Profile API.

- **Database:** Postgres/**Supabase** (row-level security, auth, webhooks).

- **Jobs:** Vercel Cron or node-cron to pull new reviews hourly and store them.

- **Events:** On new review, fire a webhook → notify via email/SMS → generate an AI draft reply.

**UI & analytics**

- **React dashboard** with real-time tiles, time-series trends (Chart.js), and a “reply queue.”

- **Associate & table attribution** (ID in the URL/QR/NFC payload) → per-associate scorecards.

- Metrics: response rate & SLA, monthly rating trend, distribution by associate, review-to-club-join correlation, and time-to-response vs satisfaction.

**AI “magic sauce” (Claude)**

- Prompt template that:

- **One-click approve/post** or auto-post on simple five-star “thank you” cases.

- **Response library** that learns over time (reuse/modify top-performing replies).

**Governance & guardrails**

- Role-based permissions, audit trails, and configurable autopost rules.

- Opt-in staff incentives tied to **public** ratings and **response SLAs**, not just AOV/club conversion.

---

### **RevOps lessons that translate beyond tasting rooms**

- **Attribution ≠ surveillance.** We used it for coaching, not punishment. It’s the same principle as SDR dashboards that highlight talk tracks and next-best actions.

- **Funnel thinking wins.** Tap → star-select → public post is a funnel. Instrument each step and remove friction.

- **Service recovery is a revenue strategy.** Faster, better replies reduce churn and boost LTV.

- **Human-in-the-loop AI.** Draft with AI; approve with taste. This keeps tone on-brand.

- **Cheap experiments first.** The no-code MVP paid for itself quickly and de-risked the v2 build.

---

### **Steal this (simple) playbook**

1. **Give every associate 10 NFC/QR cards** with their name.

1. **Ask at the moment of delight.** Script the handoff.

1. **Attribute via URL params** (?associate=Russell.).

1. **Log everything** (rating, associate, timestamp) to your warehouse/Sheets.

1. **Notify & reply fast** (SLA target within 24h; sooner on weekends).

1. **Coach from the data** (celebrate wins; role-play recoveries).

1. **Level up to v2** when the MVP proves ROI.

---

### **Would I do it differently now?**

Absolutely. I’d ship the unified Next.js + Supabase app with AI-drafted replies, real-time charts, and clean governance. But I’m also a farmer at heart: *if it ain’t broke, don’t fix it.* This scrappy system still performs—and it taught us the habits and metrics we’ll carry into v2.

