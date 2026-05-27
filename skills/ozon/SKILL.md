---
name: ozon
description: >
  Use this skill when the user wants to search for products on Ozon (ozon.ru),
  analyze product listings, check for scams, validate technical specifications,
  or find the best deal on online marketplaces. Trigger on requests like:
  "найди ноутбук", "проверь этот товар", "сравни цены на мониторы",
  "is this a scam", "check this product", or any shopping/marketplace query
  involving Ozon or Russian e-commerce platforms.
---

# Ozon — Product Search & Scam Detection

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Authentication](#authentication)
- [Scripts](#scripts)
- [Workflow](#workflow)
- [AI Analysis Guidelines](#ai-analysis-guidelines)
- [Decision Tree](#decision-tree)
- [Review Output Format](#review-output-format)
- [Report Format](#report-format)
- [Quick Reference](#quick-reference)

## Overview

Search Ozon for products, analyze listings for scams, validate specs, recommend best options.

1. **Search** → collect product cards
2. **Analyze** → deep-dive each product (specs, reviews, seller)
3. **Validate** → check scam patterns and spec inconsistencies
4. **Report** → ranked list with trust scores and red flags

## Prerequisites

Dependencies are declared inline via PEP 723 `# /// script` blocks — `uv run` resolves them on first execution. No manual install needed.

Browser: **Camoufox** (anti-detect Firefox via Playwright API). Downloads its own Firefox binary on first run.

## Authentication (Required First Step)

Ozon blocks anonymous/bot browsers with captcha. **Authenticate before first use:**

```bash
uv run scripts/ozon_login.py
```

Opens Camoufox browser at Ozon login page. Log in manually, close window. Profile (cookies, localStorage, session) saved to `~/.config/ozon-shopper/profile/` and reused by all scripts.

**Session expired?** Run `ozon_login.py` again.

## Scripts

All scripts live in `scripts/` and accept `--help` for usage.

| Script | Purpose | Key Args |
|--------|---------|----------|
| `ozon_login.py` | Open browser for manual login | — |
| `ozon_search.py` | Search Ozon, collect product cards | `--query`, `--max-results`, `--output` |
| `ozon_product_page.py` | Parse full product details | `--url`, `--output` |
| `ozon_reviews.py` | Extract reviews via entrypoint API (text, rating, photos, videos) | `--url`, `--max-reviews`, `--output` |
| `ozon_seller.py` | Get seller information | `--url`, `--output` |
| `helpers/reporter.py` | Generate Markdown report from JSON data | `--input`, `--output` |
| `full_analysis.py` | End-to-end analysis (product + reviews + seller + report) in one session | `--urls`, `--query`, `--max-results`, `--max-reviews`, `--output-dir`, `--report` |

## Known Limitations

- **Product variants**: Ozon groups reviews by product variant (color, storage). `ozon_reviews.py` returns reviews for the specific variant in the URL. If a variant has no reviews, `total_extracted` will be 0 even though other variants may have reviews (shown in `summary.total_on_page`).
- **Seller name**: When seller link text is empty, name is extracted from URL slug — may not match the display name exactly. Seller rating/age from seller page is more reliable.
- **Product score**: The overall product rating (e.g., 4.9/5) is now extracted from `webSingleProductScore` widget via DOM.
- **Rating distribution**: Per-star breakdown (5★: N, 4★: N, ...) is extracted by intercepting the browser's composer API response when the reviews section is scrolled into view. The `summary.rating_distribution` field includes `total`, `total_score`, and `distribution` (per-star counts).

## Workflow

### Step 1: Search

```bash
uv run scripts/ozon_search.py --query "ноутбук ASUS" --max-results 10 --output results.json
```

### Step 2: Analyze Each Product

For each product from search results, run three analyses in parallel:

```bash
uv run scripts/ozon_product_page.py --url "https://www.ozon.ru/product/..." --output product.json
uv run scripts/ozon_reviews.py --url "https://www.ozon.ru/product/..." --max-reviews 30 --output reviews.json
uv run scripts/ozon_seller.py --url "https://www.ozon.ru/product/..." --output seller.json
```

### Step 3: Validate Against Scam Patterns

Read `references/scam_patterns.md` and `references/specs_rules.md`, analyze each product against these checklists.

**Key validation checks:**
- Price anomaly (too low for the category/specs)
- Seller trust (rating, age on platform, number of products)
- Review authenticity (bot patterns, review velocity, rating distribution)
- Spec consistency (claimed specs vs realistic pricing)
- Brand verification (official vs third-party seller)

### Step 4: Generate Report

```bash
uv run scripts/helpers/reporter.py --input results/ --output report.md
```

### One-Step: Full Analysis

Run all steps above in one command (single browser session):

```bash
uv run scripts/full_analysis.py --urls "https://www.ozon.ru/product/..." --output-dir results/ --report report.md
uv run scripts/full_analysis.py --query "ноутбук ASUS" --max-results 5
```

## AI Analysis Guidelines

When analyzing products, follow these principles from `references/scam_patterns.md`:

### Red Flags (immediate disqualification)
- Price 40%+ below market average for identical specs
- Seller account less than 3 months old with high-value electronics
- All reviews posted within 48 hours
- Vague specs (e.g., "Intel i7" without model number)
- Stock photos instead of real product images
- Rating distribution anomaly: >95% are 5-star with 10+ total reviews (indicates fake reviews)

### Yellow Flags (investigate further)
- Price 20-40% below market average
- Mixed review sentiment despite high rating
- Seller has few products but many sales
- Specifications that look "too good to be true" for the price
- Rating distribution skewed: >85% are 5-star with moderate review count

### Trust Signals (positive indicators)
- Official brand store on Ozon
- Consistent review timeline spanning months
- Detailed, specific reviews with photos
- Seller responds to negative reviews professionally
- Specs match manufacturer's official page

## Decision Tree

```
User query → Is it a search or a specific URL?
├── Search → Run ozon_search.py → Collect results
│   └── For each result → Run product + reviews + seller analysis
│       └── Validate → Generate ranked report
│
└── Specific URL → Run product + reviews + seller analysis
    └── Validate → Generate single product analysis
```

## Review Output Format

`ozon_reviews.py` returns JSON with this structure:

```json
{
  "total_extracted": 3,
  "summary": {
    "total": 3,
    "avg_rating": 5.0,
    "positive_pct": 100.0,
    "total_on_page": 47,
    "rating_distribution": {
      "total": 47,
      "total_score": 4.9,
      "distribution": {"5": 43, "4": 3, "3": 0, "2": 1, "1": 0}
    },
    "product_score": 4.9
  },
  "reviews": [
    {
      "id": "uuid",
      "author": "Имя Ф.",
      "rating": 5,
      "date": "2026-01-17",
      "text": "Full review text...",
      "positive": "Достоинства",
      "negative": "Недостатки",
      "useful_count": 20,
      "useless_count": 0,
      "comments_count": 6,
      "photos": [{"url": "...", "uuid": "..."}],
      "videos": [{"url": "...", "preview": "...", "duration": "00:41"}]
    }
  ]
}
```

**Key fields for scam analysis:**
- `text` + `positive`/`negative` — review substance for authenticity checks
- `photos`/`videos` — real product photos indicate genuine purchases
- `date` — review timeline for velocity/bot pattern detection
- `author` — check for repetitive author names
- `total_on_page` vs `total_extracted` — variant may have few reviews while product has many

## Report Format

```markdown
## Результаты поиска: "[query]"

### 1. [Product Name] — [Price]₽ ✅/⚠️/🔴 [Verdict]
- **Продавец**: [Name] (рейтинг [X], [Y] месяцев на Ozon)
- **Отзывы**: [N] отзывов, [X]% положительных
- **Характеристики**: [Key specs]
- **Оценка доверия**: [X]/10
- **Красные флаги**: [list or "Нет"]
```

## Quick Reference

| Task | Command |
|------|---------|
| Login | `uv run scripts/ozon_login.py` |
| Search Ozon | `uv run scripts/ozon_search.py --query "..."` |
| Check product | `uv run scripts/ozon_product_page.py --url "..."` |
| Read reviews | `uv run scripts/ozon_reviews.py --url "..."` |
| Check seller | `uv run scripts/ozon_seller.py --url "..."` |
| Generate report | `uv run scripts/helpers/reporter.py --input results/` |
| **Full analysis** | `uv run scripts/full_analysis.py --urls "..." ` or `--query "..."` |
| Help on any script | `uv run scripts/ozon_search.py --help` |
