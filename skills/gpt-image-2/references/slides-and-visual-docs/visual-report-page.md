# Business Visual Report Page Template

This file is used to generate "business report / investment analysis / growth review / OKR overview" style visual single pages:

- Business consulting firm style
- Investment bank / research report
- Company annual report overview
- Investor briefing
- OKR quarterly summary

Features:

- Data-driven
- Table + chart + illustration mix
- Rigorous layout
- One page can clearly convey a business judgment

## Scope

- Single-page KPI overview
- Investor briefing cover
- Report executive summary page
- Quarterly business review page

## When to Use

- User mentions "report / review / investor briefing / KPI / OKR / executive summary"
- User needs data visualization + business judgment style

Do NOT use:

- User wants a government announcement (use `policy-style-slide.md`)
- User wants an explainer course slide (use `dense-explainer-slides.md`)
- User wants a science education diagram (use `educational-diagram-slide.md`)

## Missing Information Priority Questions

1. Report topic (business / quarter / project / company)
2. Key data (3-5 items)
3. Key judgment (one-sentence conclusion)
4. Whether a timeline / trend chart is needed
5. Color scheme: business blue / black-gold / warm gray
6. Whether English / Chinese-English bilingual

## Main Template: Business Report Executive Summary Page

📖 Description

Top: title + reporting period + logo; middle: key data cards + trend mini-chart + one-sentence judgment; bottom: source / notes.

📝 Prompt

```json
{
  "type": "Business report executive summary page",
  "goal": "Generate an executive summary visual single page usable as investor briefing, quarterly report cover, or internal OKR review",
  "style": {
    "color_palette": "{argument name=\"color palette\" default=\"Business blue + gray + white\"}",
    "tone": "{argument name=\"visual tone\" default=\"Rational, restrained, trustworthy\"}",
    "typography": "{argument name=\"typography\" default=\"Sans-serif modern font + bold numbers\"}"
  },
  "header": {
    "company_or_team": "{argument name=\"team name\" default=\"NEX Inc.\"}",
    "report_period": "{argument name=\"period\" default=\"2026 Q1\"}",
    "main_title": "{argument name=\"main title\" default=\"Quarterly Business Review · Executive Summary\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"3 Key Metrics + 1 Core Judgment\"}"
  },
  "kpi_cards": {
    "count": "{argument name=\"kpi count\" default=\"4\"}",
    "items": [
      {
        "label": "{argument name=\"kpi 1 label\" default=\"Revenue\"}",
        "value": "{argument name=\"kpi 1 value\" default=\"¥ 1.24B\"}",
        "change": "{argument name=\"kpi 1 change\" default=\"+18% YoY\"}"
      },
      {
        "label": "{argument name=\"kpi 2 label\" default=\"Active Users\"}",
        "value": "{argument name=\"kpi 2 value\" default=\"38.2M\"}",
        "change": "{argument name=\"kpi 2 change\" default=\"+22% YoY\"}"
      },
      {
        "label": "{argument name=\"kpi 3 label\" default=\"Gross Margin\"}",
        "value": "{argument name=\"kpi 3 value\" default=\"62.1%\"}",
        "change": "{argument name=\"kpi 3 change\" default=\"+3.4 pp\"}"
      },
      {
        "label": "{argument name=\"kpi 4 label\" default=\"NPS\"}",
        "value": "{argument name=\"kpi 4 value\" default=\"62\"}",
        "change": "{argument name=\"kpi 4 change\" default=\"+8\"}"
      }
    ]
  },
  "trend_chart": {
    "enabled": "{argument name=\"trend chart enabled\" default=\"true\"}",
    "type": "{argument name=\"chart type\" default=\"Line + area\"}",
    "metric": "{argument name=\"chart metric\" default=\"Quarterly revenue\"}",
    "x_axis": "Q1-Q4",
    "y_axis": "¥ billions"
  },
  "core_judgment": {
    "headline": "{argument name=\"core judgment\" default=\"Core growth comes from the AI product line; more R&D resources should be invested in Q2\"}"
  },
  "footer": {
    "source": "{argument name=\"source\" default=\"Data source: Internal finance system\"}",
    "confidentiality": "{argument name=\"confidentiality\" default=\"Internal document · For discussion only\"}"
  },
  "constraints": {
    "must_keep": [
      "Numbers must be largest and most prominent",
      "Trend chart consistent with KPI data",
      "Core judgment only one sentence",
      "Color palette minimal ≤ 3 colors"
    ],
    "avoid": [
      "Data too densely stacked",
      "Decorative illustrations appearing",
      "Multiple font types",
      "Background too dark making numbers hard to read"
    ]
  }
}
```

### Parameter Strategy

- Required: reporting period, topic, key data
- Defaultable: color palette, fonts, confidentiality label
- Random: small decorative elements

### Auto-fill Strategy

- When user only provides a topic: auto-generate 4 common KPIs (revenue / users / gross margin / NPS)
- Default color palette: business blue
- Default core judgment uses "because X, therefore Y" sentence pattern

## Variant 1: Investor Pitch Cover

📝 Prompt

```json
{
  "type": "Investor pitch cover single page",
  "header": {
    "main_title": "{argument name=\"company\" default=\"NEX Inc.\"}",
    "subtitle": "{argument name=\"tagline\" default=\"Redefining AI Workflows\"}"
  },
  "kpi_cards": {
    "items": [
      "ARR ¥ 120M",
      "Growth 240% YoY",
      "Customers 4500+"
    ]
  },
  "core_judgment": {
    "headline": "This is the optimal funding window"
  },
  "constraints": {
    "must_feel": "Sharp, confident, futuristic"
  }
}
```

## Variant 2: Annual Report Overview Page

📝 Prompt

```json
{
  "type": "Company annual report overview page",
  "header": {
    "main_title": "{argument name=\"year\" default=\"2025 Annual Report\"}",
    "subtitle": "Full-year key achievements + Next year outlook"
  },
  "sections": {
    "items": ["Full-year KPIs", "Key Milestones", "Team Growth", "Next Year Plan"]
  },
  "constraints": {
    "must_feel": "Restrained, with gravitas"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Business report page auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides business direction + reporting period, auto-generate KPIs / trends / core judgment",
  "constraints": {
    "must_feel": "Can be sent to investors / executives"
  }
}
```

## Things to Avoid

- Do NOT stuff more than 6 KPIs on an executive summary page
- Do NOT let the trend chart contradict the KPIs
- Do NOT use flashy fonts
- Do NOT make the core judgment more than 2 sentences
- Do NOT make the background color too dark, it makes numbers hard to read