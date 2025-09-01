---
title: "Run Your Wedding Venue Like a High-Performing Revenue Org"
content_type: "Article"
theme: "RevOps"
status: "draft"
publication_date: ""
notion_url: "https://www.notion.so/Run-Your-Wedding-Venue-Like-a-High-Performing-Revenue-Org-2616c059767380559b1be0db11a96e68"
---

# **Run Your Wedding Venue Like a High-Performing Revenue Or**

## 

**SLAs, Latency, Coverage & Expected Value (EV) in Google Looker Studio — with free data**

You can’t manage what you can’t measure. The same RevOps muscles that power B2B SaaS—**speed-to-first-response (SLA), stage conversion, stage latency, capacity coverage, and expected value (EV)**—work beautifully for a brick-and-mortar wedding venue.

**In this post, we’ll build an end-to-end Google Looker Studio dashboard (from a Salesforce-style CSV) that teaches you both *****how***** to use Looker Studio and *****how***** to think about wedding-venue data** so you can make the most informed decisions and strategies possible.

We’ll create: an **SLA impact** chart, a properly gated **stage-conversion** table, **latency** medians & P90, a **Month × Day-of-Week coverage heatmap** with a target slider, and an **EV vs Signed/Deposited** KPI strip with probability knobs.

You’ll see exactly what moves bookings, how to coach to the numbers, and how to plan capacity with confidence. (We’ll start with a CSV for learning; in production you can connect **directly to Salesforce** or route **Salesforce → warehouse → Looker Studio/Tableau**.)

**Live demo dashboard:** **https://lookerstudio.google.com/s/nRmeDByi1I4**

**Repo (data + README):** **https://github.com/russellmoss/linked-in-dashboard-data/blob/main/README.md**

---

### **What we’ll build (free & repeatable)**

From a Salesforce-style **CSV**, we’ll assemble an interactive Looker Studio report that shows:

- **SLA Impact** on booking rate

- **Stage-to-Stage Conversion** (properly gated)

- **Stage Latency** (Median & P90)

- **Capacity Coverage** (Month × Day-of-Week heatmap with a target slider)

- **EV vs Signed/Deposited** (KPI strip with probability sliders)

---

### **The venue funnel (mapped to RevOps)**

**Lead Created → First Email Sent → Call Booked → Call Held → Tour → Proposal Sent → Proposal Signed → Deposit → Wedding Date → Revenue Realized.**

It’s the same thinking as B2B: discovery → meeting → demo/tour → proposal → cl

---

### **Build notes (Looker Studio formulas we actually used)**

We worked directly from the CSV (see repo link) and created parsers, flags, buckets, and metrics.

### **1) Parse timestamps (once)**

```plain text
CreatedDate_dt      = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", CreatedDate)
First_Response_dt   = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", First_Response__c)
Call_Booked_dt      = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", Call_Booked__c)
Call_Held_dt        = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", Call_Held__c)
Tour_dt             = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", Tour_Date__c)
Proposal_Sent_dt    = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", Proposal_Sent__c)
Proposal_Signed_dt  = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", Proposal_Signed__c)
Deposit_dt          = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", Deposit_Date__c)
Wedding_dt          = PARSE_DATETIME("%Y-%m-%dT%H:%M:%SZ", Wedding_Date__c)
```

### **2) Stage flags (1/0) + SLA buckets**

```plain text
Booked_Flag     = CASE WHEN Proposal_Signed_dt IS NOT NULL THEN 1 ELSE 0 END
Deposited_Flag  = CASE WHEN Deposit_dt        IS NOT NULL THEN 1 ELSE 0 END
Called_Flag     = CASE WHEN Call_Held_dt      IS NOT NULL THEN 1 ELSE 0 END
Toured_Flag     = CASE WHEN Tour_dt           IS NOT NULL THEN 1 ELSE 0 END
Proposed_Flag   = CASE WHEN Proposal_Sent_dt  IS NOT NULL THEN 1 ELSE 0 END
```

```plain text
Response_Bucket =
CASE
  WHEN Response_Minutes__c <= 15  THEN "0–15m"
  WHEN Response_Minutes__c <= 60  THEN "16–60m"
  WHEN Response_Minutes__c <= 180 THEN "61–180m"
  WHEN Response_Minutes__c <= 720 THEN "181–720m"
  ELSE ">12h"
END
```

### **3) Latency (days) — we used direct percentiles on day counts**

```plain text
Call_to_Tour_Days        = DATETIME_DIFF(Tour_dt,            Call_Held_dt,       DAY)
Tour_to_Proposal_Days    = DATETIME_DIFF(Proposal_Sent_dt,   Tour_dt,            DAY)
Sign_to_Deposit_Days     = DATETIME_DIFF(Deposit_dt,         Proposal_Signed_dt, DAY)
```

**Medians & P90s (chart metrics):**

```plain text
Median_Call_to_Tour   = PERCENTILE(Call_to_Tour_Days, 50)
Median_Tour_to_Prop   = PERCENTILE(Tour_to_Proposal_Days, 50)
Median_Sign_to_Dep    = PERCENTILE(Sign_to_Deposit_Days, 50)

P90_Call_to_Tour      = PERCENTILE(Call_to_Tour_Days, 90)
P90_Tour_to_Prop      = PERCENTILE(Tour_to_Proposal_Days, 90)
P90_Sign_to_Dep       = PERCENTILE(Sign_to_Deposit_Days, 90)
```

### **4) Calendar coverage (Month × DOW) + target slider**

```plain text
Wedding_Month_Label = FORMAT_DATETIME("%Y-%m", Wedding_dt)
Wedding_DOW         = FORMAT_DATETIME("%a",    Wedding_dt)   -- Sun..Sat
Wedding_DOW_Order =
CASE Wedding_DOW
  WHEN 'Sun' THEN 1 WHEN 'Mon' THEN 2 WHEN 'Tue' THEN 3
  WHEN 'Wed' THEN 4 WHEN 'Thu' THEN 5 WHEN 'Fri' THEN 6 WHEN 'Sat' THEN 7
END
Wedding_Date_Key    = SUBSTR(IFNULL(CONCAT('', Wedding_dt), ''), 1, 10)
```

**Parameter:** Target_Per_DOW (Range 1–10; Step 1; Default 4)

```plain text
Coverage_Ratio  = COUNT_DISTINCT(Wedding_Date_Key) / Target_Per_DOW
Coverage_Capped =
CASE WHEN (COUNT_DISTINCT(Wedding_Date_Key) / Target_Per_DOW) > 1.5 THEN 1.5
     ELSE (COUNT_DISTINCT(Wedding_Date_Key) / Target_Per_DOW) END
```

### **5) Expected Value (EV) for unsigned pipeline + YTD actuals**

**Parameters:** Tour_Prob (0–1), Proposal_Prob (0–1)

```plain text
Stage_Weighted_EV =
CASE
  WHEN Proposal_Signed_Flag = 1 THEN 0
  WHEN Proposed_Flag        = 1 THEN Amount * Proposal_Prob
  WHEN Toured_Flag          = 1 THEN Amount * Tour_Prob
  ELSE 0
END
```

```plain text
Signed_Value   = SUM(CASE WHEN Proposal_Signed_dt IS NOT NULL THEN Amount            ELSE 0 END)
Deposits_Value = SUM(CASE WHEN Deposit_dt         IS NOT NULL THEN Deposit_Amount__c ELSE 0 END)
```

### 

### **A) SLA Impact — Booking Rate by Response Speed (Created Date lens)**

- **Bar chart:** Response_Bucket × AVG(Booked_Flag) → Percent

- **Filters:** Lead Source · Event Space · Owner; **Date = CreatedDate_dt** [**Screenshot: SLA Impact bar with filter controls visible**] [**AI image idea: stopwatch overlaying an inbox**]

**Takeaway:** Faster responses (0–15m / 16–60m) out-convert slower buckets.

---

### **B) Stage-to-Stage Conversion (one-row table; properly gated)**

Each % is **among those who reached the prior stage** (no double-counting). Examples:

```plain text
Call Held → Tour:
SUM(CASE WHEN Called_Flag=1 AND Toured_Flag=1 THEN 1 ELSE 0 END)
/ NULLIF(SUM(Called_Flag),0)

Tour → Proposal:
SUM(CASE WHEN Toured_Flag=1 AND Proposed_Flag=1 THEN 1 ELSE 0 END)
/ NULLIF(SUM(Toured_Flag),0)

Proposal → Signed:
SUM(CASE WHEN Proposed_Flag=1 AND Booked_Flag=1 THEN 1 ELSE 0 END)
/ NULLIF(SUM(Proposed_Flag),0)
```

*Format as %; hide row numbers; use a constant dimension like “All Inquiries.”*

**Takeaway:** See exactly where you leak (e.g., tours not getting proposals).

---

### **C) Stage Latency — Medians & P90 (Created Date lens)**

- **Bar:** Median_Call_to_Tour, Median_Tour_to_Prop, Median_Sign_to_Dep

- **Small table beneath:** the three P90s

**Takeaway:** Medians show typical speed; **P90** highlights long-tail delays to fix.

---

### **D) Booked Dates (Month × Day-of-Week) (Wedding Date lens)**

- **Pivot (counts):** Rows = Wedding_Month_Label; Columns = Wedding_DOW_Order then Wedding_DOW; Metric = COUNT_DISTINCT(Wedding_Date_Key)

- **Sort:** columns by order Asc; **exclude null** column if it appears

**Takeaway:** Scan seasonality and weekday demand at a glance.

---

### **E) Coverage Heatmap — Booked ÷ Target per Weekday (Wedding Date lens)**

- **Duplicate** the pivot; swap metric → Coverage_Capped

- **Conditional format:** 0.0 (red) → 1.0 (yellow) → 1.5 (green)

- **Control:** slider bound to Target_Per_DOW (label: *Target slots per day of the week*)

**Takeaway:** <1.0× under target; ~1.0× on pace; >1.0× above target.

---

### **F) EV vs Signed & Deposited — What-If + YTD Actuals**

- **Scorecard 1:** SUM(Stage_Weighted_EV) (currency) — page lens = CreatedDate_dt

- **Scorecard 2:** Signed_Value (date dim = Proposal_Signed_dt) — **YTD**

- **Scorecard 3:** Deposits_Value (date dim = Deposit_dt) — **YTD**

- **Controls:** sliders bound to Tour_Prob & Proposal_Prob

**Takeaway:** EV bubbles the biggest **unsigned** dollars (tours/proposals) so you can focus effort.

---

### **Why this is “RevOps thinking” for venues**

- **Speed wins:** Coach to 15/60-minute response SLAs.

- **Latency drags:** Automate tour scheduling; escalate when delays creep toward P90.

- **Capacity clarity:** Month×DOW + target slider (e.g., **4 Saturdays/mo**) shows if you’re on pace.

- **Prioritization:** EV + a “Top unsigned by EV” table tells sales where to work first.

---

### **Getting the data in (CSV today; direct or via warehouse tomorrow)**

**This tutorial uses a CSV export** (see repo), but in production you can:

1. **Connect Salesforce → BI directly** (native connectors to Looker Studio/Tableau). *Fast setup; good for smaller teams. Watch API limits & schema changes.*

1. **Go Salesforce → Warehouse → BI** Fivetran/Airbyte/Meltano → **BigQuery/Snowflake/Redshift** → Looker Studio/Tableau. *Pros: snapshots, joins (marketing/finance), governance, reliability.*

Either path works—just keep **one timestamp per stage**, a **first response timestamp**, and **Amount/Deposit** fields. Then drop in the formulas above.

**Repo (data + README):** **https://github.com/russellmoss/linked-in-dashboard-data/blob/main/README.md**

---

### **Wrap**

Running a wedding venue like a modern revenue org isn’t about jargon—it’s about **instrumentation** and **habits**. Measure what matters, coach to it, and the calendar fills itself.

**Live demo (Looker Studio):** **https://lookerstudio.google.com/s/nRmeDByi1I4** **Repo (data + README):** **https://github.com/russellmoss/linked-in-dashboard-data/blob/main/README.md**

