# Bilingual / Multi-Language Layout Visual Template

This file is used for "Chinese-English / Chinese-Japanese bilingual side-by-side layout" visuals:

- Chinese-English bilingual poster
- Chinese-Japanese bilingual science infographic
- Bilingual exhibition / cultural festival materials
- Cross-cultural brand hero visual
- Academic / cultural institution publication cover

Characteristics:

- Two languages placed side by side (not simple translation, but design language)
- Usually one language primary, one auxiliary / annotation
- Fonts strictly separated (Chinese uses Chinese fonts / English uses English fonts)
- Clear font size hierarchy
- Emphasis on whitespace and alignment

## Scope

- Chinese-English / Chinese-Japanese posters
- Cross-cultural brand materials
- Academic / cultural exhibition hero visuals

## When to use

- User mentions "Chinese-English / Chinese-Japanese / bilingual / bilingual"
- User wants cultural / academic / premium bilingual visuals

Do NOT use for:

- Single-language large-text poster → use `title-safe-poster.md`
- Pure product poster → use `poster-and-packaging/brand-poster.md`
- Magazine cover → use `poster-and-campaigns/editorial-cover.md`

## Missing Information Priority Question Order

1. Primary language + secondary language
2. Main tagline + sub-tagline (provide in both languages)
3. Theme / industry
4. Font style (serif / sans / serif / rounded)
5. Primary color 1-2
6. Aspect ratio

## Main Template: Chinese-English Bilingual Cultural Poster

Description

One image, Chinese primary, English secondary, establishing hierarchy through a strict layout system.

Prompt

```json
{
  "type": "Chinese-English bilingual cultural poster",
  "goal": "Generate a design-forward Chinese-English bilingual poster, usable as a cultural event / exhibition / brand hero visual",
  "languages": {
    "primary": "{argument name=\"primary language\" default=\"Chinese\"}",
    "secondary": "{argument name=\"secondary language\" default=\"English\"}"
  },
  "title_block": {
    "main_zh": "{argument name=\"main title zh\" default=\"The Orient Reimagined\"}",
    "main_en": "{argument name=\"main title en\" default=\"THE ORIENT REIMAGINED\"}",
    "subtitle_zh": "{argument name=\"subtitle zh\" default=\"Contemporary Eastern Aesthetic Exhibition\"}",
    "subtitle_en": "{argument name=\"subtitle en\" default=\"A Contemporary Eastern Aesthetic Exhibition\"}",
    "alignment": "{argument name=\"title alignment\" default=\"top-left aligned\"}",
    "hierarchy_rule": "Chinese largest → English medium → Chinese subtitle → English subtitle"
  },
  "meta": {
    "date": "{argument name=\"date\" default=\"2026.5.1 - 2026.5.31\"}",
    "venue": "{argument name=\"venue\" default=\"X Art Museum · Shanghai\"}",
    "presenter": "{argument name=\"presenter\" default=\"X CULTURAL FOUNDATION\"}"
  },
  "main_visual": {
    "description": "{argument name=\"main visual\" default=\"Eastern landscape + modern geometric cuts\"}",
    "position": "{argument name=\"main visual position\" default=\"lower right large area\"}"
  },
  "design": {
    "primary_color": "{argument name=\"primary color\" default=\"#A52A2A vermilion red\"}",
    "background_color": "{argument name=\"background\" default=\"#F4EEDC aged paper off-white\"}",
    "zh_font": "{argument name=\"zh font\" default=\"Song typeface / Kai typeface / modern serif\"}",
    "en_font": "{argument name=\"en font\" default=\"modern serif (Playfair / Cormorant)\"}",
    "grid": "{argument name=\"grid\" default=\"strict 12-column grid + thin guide lines (hidden in final output)\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "Chinese and English fonts strictly separated",
      "Clear hierarchy: title > subtitle > meta info",
      "Generous whitespace",
      "Color palette ≤ 3 colors"
    ],
    "avoid": [
      "Using the same font for Chinese and English (most common mistake)",
      "Translation errors (Chinese and English should be equivalent, not mistranslated)",
      "Font size difference between Chinese and English too large or too small",
      "Overstuffing elements"
    ]
  }
}
```

### Parameter Strategy

- Must ask: main tagline in Chinese and English, subtitle
- Can default: layout, fonts, colors, grid
- Can randomize: main visual details

### Auto-Fill Strategy

- User gives Chinese main tagline → auto-generate English translation + subtitle + meta info
- Font default: Chinese serif + English serif pairing
- Default 3:4

## Variant 1: Chinese-Japanese Bilingual Design

Prompt

```json
{
  "type": "Chinese-Japanese bilingual design",
  "languages": {
    "primary": "Japanese",
    "secondary": "Chinese"
  },
  "title_block": {
    "main_zh": "{argument name=\"zh\" default=\"Strolling Through Kyoto\"}",
    "main_en": "{argument name=\"jp\" default=\"Strolling Through Kyoto\"}"
  },
  "design": {
    "zh_font": "Gothic / Source Han Serif",
    "en_font": "Hiragino Mincho / Source Han Mincho (note: actually Japanese fonts)"
  },
  "constraints": {
    "must_feel": "Japanese magazine feel"
  }
}
```

## Variant 2: Science / Academic Style Bilingual

Prompt

```json
{
  "type": "science / academic style bilingual poster",
  "title_block": {
    "main_zh": "{argument name=\"main zh\" default=\"Photosynthesis\"}",
    "main_en": "{argument name=\"main en\" default=\"PHOTOSYNTHESIS\"}"
  },
  "main_visual": {
    "description": "schematic diagram + annotation lines"
  },
  "design": {
    "primary_color": "academic dark green",
    "background_color": "white"
  },
  "constraints": {
    "must_feel": "textbook insert + modern design"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "bilingual layout auto-fill",
  "mode": "auto-fill",
  "rule": "User gives main tagline (one language), auto-generate the other language + subtitle + meta info + design",
  "constraints": {
    "must_feel": "presentable at an art museum"
  }
}
```

## Things to Avoid

- Do not use the same font for Chinese and English
- Do not let Chinese-English translations misalign / mistranslate
- Do not make Chinese and English font sizes identical (should have primary-secondary hierarchy)
- Do not fill the image with both languages (leave whitespace)
- Do not mix more than 2 font families (1 Chinese + 1 English is the limit)
- Do not use Song typeface or Japanese fonts for English (wrong pairing)