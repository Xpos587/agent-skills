# KPI Dashboard Infographic Template

This file is used for generating "KPI / dashboard / data review" infographics:

- Annual / quarterly / monthly data review diagrams
- Product key metrics overview
- Personal annual recap (how many books read / km run / movies watched)
- Team performance dashboards
- Company annual report key pages
- "What I did in X year" data visualization summary

Characteristics:

- Large numbers + progress bars + mini charts + icons
- Multiple independent "metric cards" combined
- Main metrics use extra-large font sizes
- Visually like an "information visualization dashboard", with a data feel

## Scope

- Annual / quarterly / monthly reviews
- Personal recaps / data summaries
- Product / business KPI overviews
- Company annual report key pages
- User wrapped (Spotify Wrapped style)

## When to use

- User mentions "KPI / dashboard / dashboard / annual recap / wrapped / data summary / review"
- User wants the visual "strong data feel, like a SaaS backend, like Wrapped"
- User has real numbers to display

Do NOT use for:

- User wants "bento grid diverse content" → use `infographics/bento-grid-infographic.md`
- User wants "serious publication-grade data charts" → use `academic-figures/publication-chart.md`
- User wants "business report slide" → use `slides-and-visual-docs/visual-report-page.md`
- User wants "brand identity system board" → use `branding-and-packaging/brand-identity-board.md`

## Missing Information Priority Question Order

1. Topic + time range (e.g. "2025 reading recap / Q3 business overview / monthly running data")
2. Main metrics (1-3 largest numbers, e.g. "read 47 books" "revenue 12M" "ran 612 km")
3. Secondary metrics (4-8, e.g. "most-read genre" "fastest single lap" "busiest month")
4. Whether to include trend charts / leaderboards / proportion charts (which data naturally suits visualization)
5. Color scheme (tech dark / warm summary / Spotify Wrapped gradient / minimalist white)
6. Aspect ratio (Xiaohongshu 3:4 / WeChat 16:9 / 1:1)

## Main Template: KPI Dashboard Infographic

Description

The entire image is divided into multiple metric cards, with "main metrics" (extra-large numbers) at the top, and secondary metric cards arranged below (numbers + progress rings / mini charts / leaderboards / trend lines), overall like a carefully designed data snapshot.

Prompt

```json
{
  "type": "KPI Dashboard Infographic",
  "goal": "Present a set of numbers in a 'data visualization dashboard' format, letting readers perceive data scale and distribution at a glance",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"3:4 portrait\"}",
    "background": "{argument name=\"background\" default=\"deep ink #0F172A gradient to #1E293B (dark mode)\"}",
    "alt_background_light": "warm cream #F8F5EE (if user prefers light mode)"
  },
  "header": {
    "main_title": "{argument name=\"main_title\" default=\"2025 Reading Recap\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"Full year finished / reading / abandoned overview\"}",
    "period": "{argument name=\"period\" default=\"2025.01 - 2025.12\"}"
  },
  "palette": {
    "primary_text": "{argument name=\"primary_text\" default=\"#F1F5F9\"}",
    "accent_main": "{argument name=\"accent_main\" default=\"cyan #22D3EE\"}",
    "accent_secondary": "{argument name=\"accent_secondary\" default=\"violet #A78BFA\"}",
    "accent_alert": "{argument name=\"accent_alert\" default=\"rose #FB7185\"}",
    "rule": "Limit to 4 main colors, accent used for 'highlighting key numbers'"
  },
  "hero_metrics": {
    "count": "{argument name=\"hero_count\" default=\"3\"}",
    "rule": "1-3 'main metric' cards at the top, each with an extra-large number + short label + year-over-year change arrow",
    "examples": [
      { "value": "47", "label": "Books Finished", "delta": "↑ +12 vs 2024" },
      { "value": "23,140", "label": "Total Pages", "delta": "↑ +28%" },
      { "value": "8.2", "label": "Avg Rating", "delta": "↓ -0.1" }
    ]
  },
  "sub_metrics": {
    "count": "{argument name=\"sub_count\" default=\"6\"}",
    "card_types_to_use": [
      "progress_ring  — ring progress chart, center number + label (suitable for 'goal completion 78%')",
      "bar_mini       — mini horizontal bar, multi-entity ranking (suitable for 'TOP 5 most-read genres')",
      "trend_line     — mini line chart, trend over time (suitable for 'monthly reading count trend')",
      "donut_split    — proportion pie chart, 2-4 segments (suitable for 'e-book vs print book ratio')",
      "big_number_card — single large number + label (suitable for 'fastest book finished: 3 days')",
      "ranked_list    — numbered list, 3-5 items (suitable for 'TOP 3 highest-rated books')"
    ],
    "rule": "Each card has: card title (small) + main visual (chart) + brief data note (≤1 line)",
    "examples": [
      { "type": "ranked_list", "title": "TOP 3 Highest Rated", "items": ["\"...\" 9.5", "\"...\" 9.3", "\"...\" 9.1"] },
      { "type": "donut_split", "title": "Print vs Digital", "values": "60% / 40%" },
      { "type": "trend_line", "title": "Monthly Reading Count", "delta": "Peak: August 7 books" },
      { "type": "progress_ring", "title": "Annual Goal", "value": "94% (47/50)" },
      { "type": "bar_mini", "title": "TOP 5 Genres", "items": "Sci-pop / Fiction / History / Business / Philosophy" },
      { "type": "big_number_card", "title": "Fastest Book Finished", "value": "3 days" }
    ]
  },
  "layout": {
    "structure": "Top hero_metrics row → middle sub_metrics grid (2 cols × 3 rows or 3 cols × 2 rows) → bottom footer bar",
    "card_styling": "rounded corners 16-24px, semi-transparent dark fill + 1px light border, ample padding, clear text hierarchy"
  },
  "footer": {
    "tagline": "{argument name=\"footer_tagline\" default=\"Keep going next year\"}",
    "credit": "{argument name=\"credit\" default=\"@your_handle · made with gpt-image-2\"}"
  },
  "constraints": {
    "must_keep": [
      "Numbers must be real and readable (large font size, high contrast)",
      "Each card has 'data visualization', not pure text",
      "Color correspondence clear: accent_main for key numbers, alert only for negative / anomalies",
      "Fixed gap between cards, unified corner radius",
      "At least 1 card uses trend_line or progress_ring (with 'change' feel)"
    ],
    "avoid": [
      "Numbers too small to read clearly",
      "Cards containing only text (loses dashboard feel)",
      "More than 5 colors (looks like a rainbow not a dashboard)",
      "Chart precision faking real data (e.g. fabricating exact coordinates) → mark as illustrative",
      "Turning the dashboard into a pure table",
      "Using Comic Sans / handwritten fonts (data feel lost)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `hero_metrics` (at least 1 main metric with specific number + label), `sub_metrics` count, color preference (dark / light)
- **Can default**: `aspect_ratio` (3:4), `palette` (cyan + violet dark), card rounded corners / spacing
- **Can randomize**: which chart type each sub-card uses (if user doesn't specify)

### Auto-Fill Strategy

- User only provides topic and a few numbers → auto-fill reasonable card type combinations, ensuring at least 1 trend, 1 ranked_list, 1 progress_ring
- User says "Spotify Wrapped style" → switch to vivid gradient background (pink-purple-orange), bolder typography
- User says "annual report serious edition" → switch to light background + mono palette, Inter font, remove emoji
- User says "personal recap" → add footer credit, warm accent, can add cute emoji

## Variant 1: Spotify Wrapped Style

```json
{
  "type": "Wrapped-style KPI dashboard",
  "modify": {
    "background": "vivid gradient (magenta-purple → blue-purple → orange)",
    "typography": "extreme bold display font, slogan-style",
    "hero_metrics": "extra-large numbers spanning full width, only 1 main metric per page",
    "vibe": "like a music player year-end summary, with rhythm and strong emotion"
  }
}
```

Suitable for: annual personal summaries, brand wrapped events, social platform year-end figures.

## Variant 2: Business / Corporate Dashboard Serious Edition

```json
{
  "type": "Business KPI dashboard infographic",
  "modify": {
    "background": "pure white #FFFFFF or very light gray #F8FAFC",
    "palette": "primary text dark gray #0F172A, accent single deep blue #1E40AF",
    "typography": "Inter / Sohne, extremely restrained",
    "vibe": "investor deck / annual report / quarterly report"
  }
}
```

Suitable for: company annual reports, quarterly business reviews, investor briefings.

## Variant 3: Vintage / Newspaper Style Data Review

```json
{
  "type": "Vintage newspaper-style KPI infographic",
  "modify": {
    "background": "warm aged paper",
    "palette": "black + red + beige three-color",
    "typography": "serif title (Playfair / Bodoni) + monospace numbers",
    "vibe": "like The Economist / Wall Street Journal data feature page"
  }
}
```

Suitable for: media annual data features, vintage-style content, serious-reader audiences.

## Things to Avoid

- All data is text → loses dashboard visualization purpose
- No gap between cards → loses sense of independence
- More than 5 main colors → looks like a rainbow board not a dashboard
- Using Comic Sans or handwritten-style fonts → data credibility drops to zero
- Pretending precision (fabricating exact X-axis Y-axis scale values) → misleading
- Cards with empty information (just one big number + one label) → excessive whitespace
- No hero metric (every card the same size) → loses visual focal point