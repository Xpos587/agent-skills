# Lookbook / 9-Grid Infographic Template

This file is used for "N-cell themed list in one image":

- 7-day outfit lookbook
- 9-grid self-care checklist
- Weekly recipe lookbook
- Monthly plan 9-grid
- Themed list image (10 bests, 7-day habits)

Characteristics:

- Multi-cell list (7 / 9 / 12)
- Each cell independently readable
- Usually with numbering / dates / labels
- No strong narrative, emphasis on list display
- Top main title + bottom brief summary

## Scope

- Outfit lookbook
- Recipe weekly calendar
- Habit tracking cards
- TOP N list visuals

## When to use

- User mentions "7-day / 9-grid / monthly / lookbook / TOP N"
- User wants one image to list a complete checklist

Do NOT use for:

- Marketing banner sets → use `banner-grid-2x2.md`
- Relationship diagrams → use `storyboards-and-sequences/character-relationship-diagram.md`
- Expression 9-grid → use `avatars-and-profile/character-grid-portrait.md`

## Missing Information Priority Question Order

1. Theme (outfits / recipes / habits / TOP)
2. Cell count (7 / 9 / 12)
3. Content per cell
4. Whether to include numbering / dates / labels
5. Style: photography / illustration / minimalist
6. Aspect ratio

## Main Template: 7-Day Outfit Lookbook

Description

One image with a top title, main body of 7 outfit cells, each showing a full-body outfit, and a bottom brief style summary.

Prompt

```json
{
  "type": "7-day outfit lookbook",
  "goal": "Generate a 7-day outfit infographic for posting on Xiaohongshu / Instagram",
  "title_block": {
    "main_title": "{argument name=\"main title\" default=\"What to Wear This Week\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"7 days · 7 outfits\"}",
    "position": "top center"
  },
  "subject": {
    "model": "{argument name=\"model description\" default=\"East Asian young woman, natural smile\"}",
    "consistency": "must be the same person across all 7 cells"
  },
  "layout": {
    "format": "{argument name=\"layout\" default=\"top 4 + bottom 3 staggered\"}",
    "panel_count": 7,
    "panel_design": {
      "label_top": "{argument name=\"label format\" default=\"DAY 1 / MON\"}",
      "outfit_caption": "1-line style description"
    }
  },
  "outfits": [
    {"day": 1, "label": "MON", "style": "{argument name=\"day 1\" default=\"commuter white shirt + beige trousers\"}"},
    {"day": 2, "label": "TUE", "style": "{argument name=\"day 2\" default=\"knit cardigan + jeans\"}"},
    {"day": 3, "label": "WED", "style": "{argument name=\"day 3\" default=\"dress + flats\"}"},
    {"day": 4, "label": "THU", "style": "{argument name=\"day 4\" default=\"sports hoodie + short skirt\"}"},
    {"day": 5, "label": "FRI", "style": "{argument name=\"day 5\" default=\"leather jacket + black straight pants\"}"},
    {"day": 6, "label": "SAT", "style": "{argument name=\"day 6\" default=\"linen shirt + wide-leg pants\"}"},
    {"day": 7, "label": "SUN", "style": "{argument name=\"day 7\" default=\"hoodie + athletic shorts\"}"}
  ],
  "style": {
    "art_style": "{argument name=\"art style\" default=\"Japanese magazine fashion photography + beige background\"}",
    "color_palette": "{argument name=\"color palette\" default=\"beige + earth tones + black\"}"
  },
  "footer": {
    "summary": "{argument name=\"summary\" default=\"workday commute + weekend relaxed\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "Same person across all 7 cells",
      "Outfit styles follow weekly rhythm",
      "Color palette strictly unified",
      "Label fonts consistent"
    ],
    "avoid": [
      "7 cells looking like different people",
      "High-saturation neon colors in palette",
      "Outfit style drifting to completely mismatched",
      "More than 2 font types"
    ]
  }
}
```

### Parameter Strategy

- Must ask: theme, model description, 7 outfits
- Can default: layout, style, color palette
- Can randomize: background details

### Auto-Fill Strategy

- User gives "style keyword" (minimalist / retro / street) → auto-expand 7 outfit sets
- Default 7 cells + staggered layout
- Default Japanese magazine photography style

## Variant 1: 9-Grid Self-Care Checklist

Prompt

```json
{
  "type": "9-grid self-care checklist",
  "title_block": {
    "main_title": "{argument name=\"main title\" default=\"9 daily self-care habits\"}"
  },
  "layout": {
    "format": "3x3 grid",
    "panel_count": 9
  },
  "outfits": [
    {"label": "1", "style": "8 glasses of water"},
    {"label": "2", "style": "10 min stretch"},
    {"label": "3", "style": "15 min sunlight"},
    {"label": "4", "style": "deep breathing"},
    {"label": "5", "style": "note 3 gratitudes"},
    {"label": "6", "style": "listen to a favorite song"},
    {"label": "7", "style": "call family"},
    {"label": "8", "style": "10 pages of reading"},
    {"label": "9", "style": "bedtime by 11pm"}
  ],
  "style": {
    "art_style": "minimalist illustration + soft colors"
  },
  "constraints": {
    "must_feel": "usable as a habit-tracking poster"
  }
}
```

## Variant 2: TOP 12 List Image

Prompt

```json
{
  "type": "TOP 12 list image",
  "title_block": {
    "main_title": "{argument name=\"main title\" default=\"12 best books to read in 2026\"}"
  },
  "layout": {
    "format": "3x4 grid",
    "panel_count": 12
  },
  "constraints": {
    "must_feel": "recommendation feel + shareable"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "Lookbook / list auto-fill",
  "mode": "auto-fill",
  "rule": "User gives theme, auto-decide cell count, content, style",
  "constraints": {
    "must_feel": "postable to Xiaohongshu"
  }
}
```

## Things to Avoid

- Do not let cell count exceed 16
- Do not let cell size difference > 2x (unless main image rules are consistent)
- Do not let background colors disconnect from the theme
- Do not use multiple title font sizes / font types
- Do not have multiple different models in one lookbook (maintain identity consistency)