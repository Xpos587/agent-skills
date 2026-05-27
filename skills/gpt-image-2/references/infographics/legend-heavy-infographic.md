# High Legend-Density Infographic Template

This file is used for generating "high legend / high annotation / high information density" science popularization / educational / explanatory infographics:

- Medical causal chain infographics
- Process flow infographics
- Historical / cultural explanation infographics
- Equipment / species anatomy diagrams
- Complex system structure diagrams

Characteristics:

- Central main subject (human body / equipment / concept diagram)
- Surrounding numbered information blocks
- Each block composed of "number + title + icon + sub-items"
- Bilingual Chinese-English / multi-language parallel
- Extremely high information volume but rigorous layout

## Scope

- Medical science popularization diagrams
- Fashion / design process flow diagrams
- Evolution / evolutionary / historical timeline diagrams
- Equipment anatomy diagrams
- Cross-disciplinary system diagrams

## When to use

- User mentions "causal chain / evolution diagram / system diagram / anatomy diagram / process diagram / infographic"
- User wants one image to explain an entire system
- User wants bilingual Chinese-English

Do NOT use for:

- User wants "explanatory Slides" → use `slides-and-visual-docs/dense-explainer-slides.md`
- User wants maps → use maps series
- User wants speech pages → use `policy-style-slide.md`

## Missing Information Priority Question Order

1. Topic (disease / process / concept)
2. Main title + English subtitle
3. Number of sections (recommend 8-14)
4. Central main visual
5. Color scheme (medical red-blue / natural green / tech blue / beige scholarly)
6. Whether bilingual

## Main Template: High-Density Causal Chain Infographic

Description

A transparent / semi-sectioned central subject surrounded by 8-14 numbered information blocks, each composed of a small icon + title + sub-items, with a concluding sentence at the bottom.

Prompt

```json
{
  "type": "High-density causal chain infographic poster",
  "goal": "Generate a high-finish science popularization / educational / explanatory infographic, usable as a single-page PDF main image, social media long-image header, hospital / school promotional image",
  "style": {
    "aesthetic": "{argument name=\"aesthetic\" default=\"highly detailed anatomy / engineering diagram style + clean structured layout + scientific diagram feel\"}",
    "color_palette": "{argument name=\"color palette\" default=\"medical red, medical blue, beige, anatomical flesh\"}",
    "language": "{argument name=\"language\" default=\"bilingual Chinese + English\"}"
  },
  "header": {
    "main_title_cn": "{argument name=\"main title cn\" default=\"The Causal Chain of Diabetes\"}",
    "main_title_en": "{argument name=\"main title en\" default=\"THE CAUSAL CHAIN OF DIABETES\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"From insulin failure, to high blood sugar, to whole-body damage\"}"
  },
  "centerpiece": {
    "description": "{argument name=\"centerpiece description\" default=\"Transparent human body, showing circulatory system and internal organs\"}",
    "highlight": "{argument name=\"highlight color\" default=\"Red highlight path\"}"
  },
  "sections": {
    "count": "{argument name=\"section count\" default=\"14\"}",
    "items": [
      "01 Glucose Enters the Body",
      "02 Pancreas and Insulin",
      "03 Normal Insulin Action",
      "04 Insulin Resistance: Type 2 Pathway Begins",
      "05 Liver Continues Releasing Glucose",
      "06 Beta Cell Failure: Compensation to Collapse",
      "07 Type 1 Diabetes Branch",
      "08 High Blood Sugar and Blood Chemistry",
      "09 High Blood Sugar Causes Tissue Damage",
      "10 Acute Metabolic Consequences",
      "11 Microvascular Complications",
      "12 Macrovascular Complications",
      "13 Long-term Organ System Cost",
      "14 Regulatory System Failure"
    ]
  },
  "section_block_style": {
    "components": ["Number", "Chinese title", "English title", "1-3 icons", "Short description ≤ 2 lines"],
    "alignment": "Radiating around the central subject or in two side columns"
  },
  "footer": {
    "core_message": "{argument name=\"core message\" default=\"Diabetes is not a single event — it is the long-term accumulation of metabolic imbalance\"}",
    "core_message_en": "{argument name=\"core message en\" default=\"Diabetes is not a single event — it is the accumulation of metabolic imbalance.\"}"
  },
  "constraints": {
    "must_keep": [
      "Central subject as visual anchor",
      "Section numbering continuous",
      "Chinese and English appear simultaneously, but not at the same font size",
      "Legend / annotation lines do not cross"
    ],
    "avoid": [
      "Information block sizes inconsistent",
      "Icons overly decorative",
      "Chinese and English line breaks inconsistent",
      "Overall too bright / too dark affecting readability"
    ]
  }
}
```

### Parameter Strategy

- Must ask: topic, main title, section count, central subject
- Can default: color scheme, English titles, bottom concluding sentence
- Can randomize: section icon specific rendering

### Auto-Fill Strategy

- User only provides topic → auto-decide 8-14 sections, and auto-generate English titles
- Central subject auto-selected based on topic (medicine → human body; process → equipment cross-section; evolution → timeline; history → protagonist silhouette)
- Color scheme auto-selected by topic default colors

## Variant 1: Eastern Manuscript Style Infographic

Prompt

```json
{
  "type": "Eastern manuscript style infographic",
  "header": {
    "main_title": "{argument name=\"main title\" default=\"Confucianism, Buddhism, Daoism · Fundamental Differences\"}"
  },
  "style": {
    "aesthetic": "Ancient manuscript + ink wash lines + low-saturation digital watercolor",
    "color_palette": "sage green, pale gold, off-white",
    "background": "Aged beige parchment + worn corners"
  },
  "centerpiece": {
    "description": "A vertical egg-shaped layered structure in the center, from top to bottom: Buddhism, Daoism, Confucianism"
  },
  "sections": {
    "items": ["Buddhism / Self and Self", "Daoism / Self and All Things", "Confucianism / Self and Others"]
  },
  "constraints": {
    "must_feel": "classical, restrained, research-like"
  }
}
```

## Variant 2: Evolution Timeline Infographic

Prompt

```json
{
  "type": "Evolution timeline infographic",
  "header": {
    "main_title": "{argument name=\"main title\" default=\"Human Evolution\"}"
  },
  "centerpiece": {
    "description": "A winding stone staircase with 25 numbered steps, each step showing a biological form",
    "highlight": "End with a glowing cosmic silhouette with a question mark"
  },
  "sections": {
    "items": [
      "L0 Single-cell Life",
      "L1 Multicellular Organisms",
      "L2 Animal Kingdom",
      "L3 Chordates",
      "L4 Land Revolution",
      "L5 Mammalia",
      "L6 Hominidae Evolution",
      "L7 Homo Sapiens Era"
    ]
  },
  "extras": ["Top-right 'gained / lost function' legend", "Bottom 'key evolution milestones' timeline"],
  "constraints": {
    "must_feel": "strong knowledge feel, visually stunning"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "High-density infographic auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides topic and field, auto-decide sections, central subject, color scheme, English translations",
  "constraints": {
    "must_feel": "publication-grade"
  }
}
```

## Things to Avoid

- Section count < 6 feels sparse, > 16 feels too dense
- Do not make Chinese and English titles the same font size
- Do not pile all sections on one side, must surround the center
- Do not let lines cross causing reading confusion
- Do not make the infographic into a pure text poster (must have icons + main subject)
- Do not let overall colors exceed 4 main colors