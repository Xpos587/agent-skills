# Interpretation Framework

6-layer analysis for search demand signals. Each layer answers a specific CustDev question.

## 1. Demand Signal

**Question**: Are people searching for this pain/problem?

**What to look for**:
- Wordstat: `totalCount` per mask. Absolute numbers matter less than presence/absence and relative comparison across masks
- Trends: Interest score (0-100). Score > 10 for a niche topic = meaningful signal

**Interpretation**:
- Confirmed: Multiple masks show consistent search volume
- Partial: Some masks show volume, others don't
- Not confirmed: No masks show meaningful volume
- Insufficient data: Volume too low for reliable analysis

**Red flag**: 0 queries for a product name doesn't mean 0 demand. It means the category doesn't exist in search yet. Search by pain, not by solution name.

## 2. Client Language

**Question**: What words/phrases do people use to describe the problem?

**What to look for**:
- Wordstat: `topRequests` and `associations` — exact phrases people type
- Trends: `related_queries.rising` and `related_queries.top` — how searchers frame the topic

**Interpretation**:
- Extract surprising/b non-obvious terms — these are insights interviews might miss
- Group terms by intent: pain statements, solution-seeking, comparison, informational
- Use discovered language in positioning, landing pages, ad copy

**Output**: List of top 10-20 phrases grouped by intent, with non-obvious findings highlighted.

## 3. Seasonality

**Question**: Does demand have peaks/troughs?

**What to look for**:
- Wordstat: `dynamics` monthly data — exact monthly counts
- Trends: `interest_over_time.timeline_data` — relative interest over months

**Interpretation**:
- Clear seasonal pattern → confirms hypothesis timing (e.g., "sports training" peaks in fall/winter)
- Flat demand → year-round opportunity
- Declining trend → market shrinking, validate carefully
- Rising trend → market growing, favorable signal

**Output**: Identify peak months, trough months, and trend direction (rising/stable/declining).

## 4. Geography

**Question**: Where do people search for this?

**What to look for**:
- Wordstat: `regions` data with absolute counts and `affinityIndex`
- Trends: `interest_by_region` with relative scores (0-100)

**Interpretation**:
- Geo concentration → validates or refines SAM estimates
- Unexpected geo patterns → may reveal new markets or disprove assumptions
- Compare `affinityIndex` (Wordstat) — high affinity in small region = disproportionately interested population

**Output**: Top 5-10 regions by volume and top 5 by affinity index.

## 5. Search Competitors

**Question**: What existing solutions are people already finding?

**What to look for**:
- Wordstat: `associations` — what else people search alongside the mask
- Trends: `related_topics` — topics searched by the same users

**Interpretation**:
- Named competitors in search → market exists, but you're not alone
- Generic tool names → people solving the problem with workarounds
- No competitor names → either no market or market doesn't search for solutions (validate via interviews)

**Output**: List of discovered competitor/tool names with type (direct competitor / workaround / adjacent solution).

## 6. Breakout/Growth

**Question**: Is demand growing?

**What to look for**:
- Trends: `formatted_value: "Breakout"` (5000%+ growth) or `"+N%"` in related queries
- Wordstat: Compare current month dynamics vs. same month previous year if data available

**Interpretation**:
- Breakout keywords → emerging need, first-mover opportunity
- High growth (+100%+) → validated and growing market
- Moderate growth (+50-99%) → stable growth
- Flat or declining → saturated or shrinking

**Output**: List of breakout and high-growth terms with growth percentages.