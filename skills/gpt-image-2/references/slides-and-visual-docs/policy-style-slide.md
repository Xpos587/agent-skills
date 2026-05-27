# Policy / Government-Style Explanatory Slide Template

This file is used to generate "government announcement / policy interpretation / public outreach" style visual pages:

- Government policy interpretation
- Industry white paper one-page summary
- Public service information
- Regulatory change notice
- Notice / announcement main visual

Features:

- Rigorous and restrained
- Large main title, official feel
- Clear information blocks
- Stable color scheme (deep blue / deep red / deep green + beige)
- Appropriate decoration but not loud

## Scope

- Policy interpretation diagram
- Government announcement main image
- Industry white paper summary image
- Regulatory change notice diagram
- Public outreach poster-style Slide

## When to Use

- User mentions "policy interpretation / government announcement / white paper / public outreach / rigorous explanation"
- User wants the visual to look "authoritative, serious, not entertaining"

Do NOT use:

- User wants an explainer course slide (use `dense-explainer-slides.md`)
- User wants a business report (use `visual-report-page.md`)
- User wants a science education diagram (use `educational-diagram-slide.md`)

## Missing Information Priority Questions

1. Topic (policy name / announcement name / regulation name)
2. Issuing body / publishing institution
3. Core content sections (3-5)
4. Key numbers or dates
5. Color scheme: government red / government blue / government green / neutral gray
6. Whether QR code / contact information is needed

## Main Template: Policy Interpretation Single-Page Slide

📖 Description

Overall page: top official logo / institution name + main title + subtitle; middle multiple explanatory blocks + data highlights; bottom source / QR code / release date.

📝 Prompt

```json
{
  "type": "Policy interpretation single-page Slide",
  "goal": "Generate a rigorous, authoritative visual page usable for government announcements / policy interpretation",
  "style": {
    "color_palette": "{argument name=\"color palette\" default=\"Government red + off-white + dark gray\"}",
    "tone": "{argument name=\"visual tone\" default=\"Rigorous, restrained, official\"}",
    "typography": "{argument name=\"typography\" default=\"Source Song large title + Source Han Sans body text\"}"
  },
  "header": {
    "agency_name": "{argument name=\"agency name\" default=\"National Bureau of X\"}",
    "agency_logo": "{argument name=\"agency logo\" default=\"National emblem / institution crest\"}",
    "main_title": "{argument name=\"main title\" default=\"Guiding Opinions on Promoting High-Quality Development of X Industry\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"Key Points of Policy Interpretation\"}",
    "release_date": "{argument name=\"release date\" default=\"April 24, 2026\"}"
  },
  "sections": {
    "count": "{argument name=\"section count\" default=\"5\"}",
    "items": [
      "{argument name=\"section 1\" default=\"Policy Background\"}",
      "{argument name=\"section 2\" default=\"Key Objectives\"}",
      "{argument name=\"section 3\" default=\"Priority Tasks\"}",
      "{argument name=\"section 4\" default=\"Safeguard Measures\"}",
      "{argument name=\"section 5\" default=\"Implementation Timeline\"}"
    ],
    "section_block_style": "Number + title + 2-3 line explanation, optionally with small icons"
  },
  "highlight_numbers": {
    "enabled": "{argument name=\"highlight numbers enabled\" default=\"true\"}",
    "items": [
      "{argument name=\"key number 1\" default=\"5 Priority Tasks\"}",
      "{argument name=\"key number 2\" default=\"3-Year Implementation Cycle\"}",
      "{argument name=\"key number 3\" default=\"Covering 28 Fields\"}"
    ]
  },
  "footer": {
    "source": "{argument name=\"source\" default=\"Source: Full text of official document link\"}",
    "qr_code": "{argument name=\"qr code\" default=\"Bottom-right QR code: View the original policy text\"}"
  },
  "constraints": {
    "must_keep": [
      "Main title is the largest font size",
      "Institution logo and name must appear and be readable",
      "Color palette restrained ≤ 3 colors",
      "Data highlight area visually prominent but not excessive"
    ],
    "avoid": [
      "Entertaining fonts appearing",
      "Overly cartoonish illustrations",
      "Brand advertising elements appearing",
      "Overly saturated colors"
    ]
  }
}
```

### Parameter Strategy

- Required: policy name, institution, sections
- Defaultable: color palette, typography scheme, bottom information
- Random: decorative small icons

### Auto-fill Strategy

- Default sections follow the "Background / Objectives / Tasks / Safeguards / Timeline" five-part structure
- Default color palette: government red + off-white + dark gray
- Default institution style left generic to avoid impersonating real institutions

## Variant 1: Public Outreach Poster-Style Slide

📝 Prompt

```json
{
  "type": "Public outreach poster-style Slide",
  "header": {
    "main_title": "{argument name=\"main title\" default=\"Citywide Waste Sorting · Starts with Me\"}",
    "subtitle": "Authoritative guide + Action guide"
  },
  "centerpiece": {
    "description": "{argument name=\"centerpiece\" default=\"Four types of waste bins + simple sorting icons\"}"
  },
  "sections": {
    "items": [
      "Recyclables",
      "Kitchen waste",
      "Hazardous waste",
      "Other waste"
    ]
  },
  "constraints": {
    "must_feel": "Public service, clear, easy to understand"
  }
}
```

## Variant 2: White Paper Summary Slide

📝 Prompt

```json
{
  "type": "Industry white paper summary Slide",
  "header": {
    "main_title": "{argument name=\"report name\" default=\"2026 X Industry Development White Paper\"}"
  },
  "sections": {
    "items": ["Market Overview", "Trend Insights", "Key Data", "Future Outlook"]
  },
  "highlight_numbers": {
    "enabled": true,
    "items": ["Market size 1.2 trillion", "Compound growth 18%", "Active enterprises 4500+"]
  },
  "constraints": {
    "must_feel": "Professional, usable as public release material"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Policy-style Slide auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides topic, auto-select institution style, section splitting, color palette",
  "constraints": {
    "must_feel": "Authoritative, restrained, distributable"
  }
}
```

## Things to Avoid

- Do NOT impersonate any real institution logo
- Do NOT use entertaining fonts (brush script, cartoon fonts except in special circumstances)
- Do NOT let illustrations distract from the content
- Do NOT exceed 3 main colors
- Do NOT make body text line spacing so tight it becomes unreadable
- Do NOT add too many marketing cards on a policy-style Slide