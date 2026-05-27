---
name: search-demand-research
description: Use when validating startup ideas, CustDev hypotheses, or product-market fit through search demand signals. Triggers on "is there demand for X", "validate hypothesis", "market size via search", "search volume for pain point", "what words people use for X problem", "seasonality check", "competitor discovery through search", "CustDev validation", "demand research", "ищут ли X", "спрос на X", "валидация гипотезы"
---

# Search Demand Research

Validate CustDev hypotheses through search data. Input: problem/hypothesis. Output: is there demand, how people describe the pain, seasonality, geo, search competitors.

**Not** an SEO tool. **Not** a semantic collector for ad campaigns. Search data supplements CustDev — it doesn't replace interviews. Never project revenue, conversion rates, or market size from search volume.

## When to Use

- Validating "is there demand for X" hypotheses
- Discovering how people describe a problem (client language)
- Checking seasonality/geo of demand
- Finding search competitors and existing alternatives
- Startup validation, product-market fit research

## When NOT to Use

- Semantic collection for Yandex.Direct → `yandex-performance-ops`
- SEO keyword research → `google-trends-api`, `seo-keyword-research`
- Auto-classification of keywords
- WTP estimation (search data can't measure willingness to pay)
- Revenue/conversion funnel projection from search volume

## B2B Rule

For B2B hypotheses, search data is **secondary** — interviews and industry channels are primary. B2B buyers rarely search for solutions; they ask peers. Low or zero search volume does not invalidate a B2B hypothesis.

## Platform Selection

| Target market | Primary | Secondary |
|---|---|---|
| Russia/CIS | Wordstat | Trends |
| Global | Trends | Wordstat (if CIS layer needed) |
| Both markets | Both in parallel | — |

## Workflow

```
Hypothesis → Masks → Collect → Interpret → Report
```

### Step 1. Formulate Research Masks

Convert hypothesis into 3-5 search masks:

| Mask type | Example | Signal |
|---|---|---|
| Pain | "how to improve X" | Demand for solution |
| Product | "X analysis tool" | Existing alternatives |
| Competitor | "X vs Y" | Search competition |
| Parent | "child progress X" | B2 segment |
| Root | "X" (single word) | Overall landscape |

**Limit: 3-5 masks per hypothesis.** This is research, not full semantic collection.

### Step 2. Collect

Masks file format: `mask<TAB>intent` (intent: pain/product/competitor/parent/root).

```bash
# Wordstat — single query or masks file
python3 <skill-dir>/scripts/research_wordstat.py --query "how to improve X" \
  --dynamics --regions-data --output-dir research/wordstat
python3 <skill-dir>/scripts/research_wordstat.py --masks-file masks.tsv \
  --dynamics --regions-data --output-dir research/wordstat

# Google Trends — full research
python3 <skill-dir>/scripts/research_trends.py --query "X training tool" \
  --full --output-dir research/trends

# Token check
python3 <skill-dir>/scripts/research_wordstat.py --token-check
python3 <skill-dir>/scripts/research_trends.py --token-check
```

### Step 3. Interpret (6 Layers)

See [references/interpretation_framework.md](references/interpretation_framework.md).

1. **Demand signal** — are people searching for the pain?
2. **Client language** — what words/phrases do they use?
3. **Seasonality** — peaks/dips confirming or contradicting hypotheses
4. **Geography** — where demand concentrates (validates SAM)
5. **Search competitors** — existing solutions people already find
6. **Breakout/growth** — is demand rising?

**Core rule: 0 queries ≠ 0 market.** No search signal means the category may not exist in search, not that the market doesn't exist.

### Step 4. Limitations

See [references/limitations.md](references/limitations.md).

| Limitation | Consequence |
|---|---|
| Product without category = 0 queries | Doesn't mean no demand |
| Informational queries ≠ purchase intent | Can't measure WTP |
| B2B barely searches | Director doesn't google "analytics for school" |
| Narrow niche = noise | Queries in tens, not thousands |
| Trends = relative numbers | 0-100 scale, not absolute volume |
| Google ≠ whole market | Yandex, social, native search miss |

**Interpretation rule**: Search data is one validation source. Positive signal = confirmation, not proof. Absent signal = no data, not disproof.

### Step 5. Report

Auto-detect language from hypothesis. Structure:

```
# [Language-specific title]

## Hypothesis
## Methodology (platform, masks, period, geo)
## Signals (demand, language, seasonality, geo, competitors, trend)
## Limitations
## Verdict (confirmed / partial / not confirmed / insufficient data)
```

## Scripts & Tokens

| Script | Purpose |
|---|---|
| `scripts/research_wordstat.py` | Wordstat research collector (`YANDEX_WORDSTAT_TOKEN`) |
| `scripts/research_trends.py` | Google Trends via SerpApi (`SERPAPI_KEY`) |
| `scripts/research_common.py` | Cache, utilities, masks file parsing |

Tokens: Wordstat → oauth.yandex.ru, SerpApi → serpapi.com (free: 250/mo). Scripts: `--help` for details.

## Wordstat Operators

See [references/wordstat_operators.md](references/wordstat_operators.md).

## Common Mistakes

| Mistake | Fix |
|---|---|
| Summing totalCount across masks as "market size" | Each mask = separate signal. Never sum |
| Projecting revenue/conversion funnel from search volume | Search volume = directional signal only. No revenue, CTR, or conversion math |
| Concluding "no market" from 0 queries | 0 = no search signal. Go to CustDev interviews |
| Using search as primary validation for B2B | B2B buyers don't google solutions. Interviews first, search supplementary |
| Using full-depth 2000 rows for CustDev | 200 rows is enough. Full-depth is for ad campaigns |
| Searching by product name that doesn't exist | Search by pain/problem, not solution name |
| Treating Trends numbers as absolute | 0-100 = relative interest. Compare across queries only |
| Ignoring seasonality | Peak/trough may explain "low demand" in off-season |
| Using SEO metrics (keyword difficulty, CTR, bid estimates) | Not an SEO tool. Use search data for demand signals only |