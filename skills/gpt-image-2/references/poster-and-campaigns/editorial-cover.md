# Magazine / Editorial Cover Template

This file is used to generate "magazine covers / editorial visuals / publication covers":

- Fashion magazine cover
- Industry journal cover
- Internal publication / report cover
- Independent media special edition cover
- Editorial feature main image

Features:

- Strong "publication feel"
- Main visual portrait / single object dominates
- Large headline + small section teasers
- Aspect ratio mostly portrait 3:4 / 4:5
- Space for publication name + issue number

## Scope

- Magazine / journal cover
- Industry report cover
- Independent media special edition cover
- Publication-style visual poster

## When to Use

- User mentions "magazine / cover / journal / cover / publication style"
- User wants the visual to have strong "editorial feel" rather than advertising poster feel

Do NOT use:

- General brand poster (use `brand-poster.md`)
- Banner (use `banner-hero.md`)
- Campaign KV (use `campaign-kv.md`)

## Missing Information Priority Questions

1. Publication name / issue number / publisher
2. Main title (cover large text)
3. Main visual (person / object / concept)
4. Sub-section / inside page teaser short lines (3-5)
5. Style: high fashion / cultural / financial / tech / retro
6. Aspect ratio

## Main Template: Magazine Cover (Portrait)

📖 Description

Portrait cover with main visual as portrait or single object, publication name + issue number at top left, main title as large text in horizontal or vertical arrangement, side teaser text in small font.

📝 Prompt

```json
{
  "type": "Magazine cover",
  "goal": "Generate a visual usable as a fashion / cultural / industry magazine cover with strong editorial feel",
  "publication": {
    "name": "{argument name=\"publication name\" default=\"NEUE\"}",
    "tagline": "{argument name=\"tagline\" default=\"Culture · Design · Future\"}",
    "issue": "{argument name=\"issue\" default=\"Issue 042 / 2026 April\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "main_visual": {
    "type": "{argument name=\"main visual type\" default=\"Portrait\"}",
    "description": "{argument name=\"main visual\" default=\"East Asian young woman frontal portrait, calm gaze, natural light\"}",
    "composition": "{argument name=\"composition\" default=\"Filling the frame, head centered slightly right\"}"
  },
  "title_block": {
    "main_title": "{argument name=\"main title\" default=\"Between Resets\"}",
    "main_title_style": "{argument name=\"title style\" default=\"Oversized bold serif, layered over main visual\"}",
    "kicker": "{argument name=\"kicker\" default=\"Interview\"}"
  },
  "side_teasers": {
    "count": "{argument name=\"teaser count\" default=\"4\"}",
    "items": [
      "{argument name=\"teaser 1\" default=\"Writing in the AI Age · Han Songluo vs ChatGPT\"}",
      "{argument name=\"teaser 2\" default=\"Architect's Journal · Slowly Building a House in Hangzhou\"}",
      "{argument name=\"teaser 3\" default=\"Special Feature · 30 at 30\"}",
      "{argument name=\"teaser 4\" default=\"Long Read · A Failed Startup\"}"
    ],
    "position": "{argument name=\"teaser position\" default=\"Bottom + left vertical\"}"
  },
  "color_palette": "{argument name=\"color palette\" default=\"Off-white + ink black + touch of brand orange\"}",
  "barcode": {
    "enabled": "{argument name=\"barcode enabled\" default=\"true\"}",
    "position": "Bottom right corner"
  },
  "constraints": {
    "must_keep": [
      "Main visual as absolute anchor",
      "Publication name clear and readable, not obscured",
      "Main title largest font size",
      "Section teasers not competing for attention"
    ],
    "avoid": [
      "Main visual and text competing for the same area",
      "More than 3 font types",
      "Extra colors in palette",
      "Advertising logos appearing"
    ]
  }
}
```

### Parameter Strategy

- Required: publication name, issue number, main title, main visual
- Defaultable: color palette, section teasers, barcode
- Random: small decorative elements

### Auto-fill Strategy

- Style auto-selected by publication type (fashion = high contrast + minimalist, financial = blue-gray + serif, cultural = warm beige + serif)
- Main title defaults to 6-12 characters
- Section teasers default to 3-4 items

## Variant 1: Single Object Cover (Product / Object)

📝 Prompt

```json
{
  "type": "Single object magazine cover",
  "main_visual": {
    "type": "object",
    "description": "{argument name=\"object\" default=\"A well-maintained vintage typewriter\"}"
  },
  "title_block": {
    "main_title": "{argument name=\"title\" default=\"The Soul of Tools\"}"
  },
  "constraints": {
    "must_feel": "Still life, restrained, literary feel"
  }
}
```

## Variant 2: Financial / Tech Journal Cover

📝 Prompt

```json
{
  "type": "Financial / tech journal cover",
  "main_visual": {
    "type": "concept",
    "description": "{argument name=\"concept\" default=\"Information flow abstract graphic + silhouette of main figure\"}"
  },
  "color_palette": "Deep blue + silver + touch of neon",
  "title_block": {
    "main_title": "{argument name=\"title\" default=\"AI Rewrites Business\"}"
  },
  "constraints": {
    "must_feel": "Cutting-edge, credible, industry flagship"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Magazine cover auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides publication type + theme, auto-generate publication name, issue number, main title, section teasers, style",
  "constraints": {
    "must_feel": "Ready for the newsstand"
  }
}
```

## Things to Avoid

- Do NOT let the publication name be obscured by the main visual
- Do NOT let the main title have insufficient color contrast against the main visual
- Do NOT exceed 5 section teaser items
- Do NOT use more than 3 font types
- Do NOT place the barcode in the center of the main visual
