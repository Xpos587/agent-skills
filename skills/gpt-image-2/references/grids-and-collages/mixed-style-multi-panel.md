# Multi-Style Mixed Multi-Panel Collage Template

This file is used for "multiple panels in one image, each panel has a different style but unified theme":

- 5 / 6 cell mixed style collage
- Cross-style IP visual poster
- "Same subject in different timelines" collage
- "One-line evolution history" collage
- Social media fun poster

Characteristics:

- Multiple different style panels coexist
- Each panel has a completely different style (realistic + anime + pixel + oil painting)
- Theme or subject remains consistent
- Strong visual impact, fun
- Usually with small labels inside panels

## Scope

- Cross-style art collage
- One character / theme in multiple style renditions
- Viral posters
- IP history / timeline collage

## When to use

- User mentions "multi-style / cross-style / style mixing / multiple art styles"
- User wants visual impact + fun
- User wants the same theme rendered in different styles

Do NOT use for:

- Style-unified banner sets → use `banner-grid-2x2.md`
- Style-unified lookbook → use `lookbook-grid.md`
- Style-unified 4-panel comic → use `storyboards-and-sequences/four-panel-comic.md`

## Missing Information Priority Question Order

1. Theme / subject (must be clear, as it anchors all styles)
2. Panel count (4 / 5 / 6)
3. Style per panel (realistic / anime / oil painting / pixel / 3D / crayon / ...)
4. Whether to include style labels
5. Aspect ratio

## Main Template: 5-Cell Mixed Style Collage (Same Subject, Different Styles)

Description

One image, 5 cells of different shapes, each cell with a completely different style but consistent subject, with a small style label at the bottom of each cell.

Prompt

```json
{
  "type": "5-cell mixed style collage",
  "goal": "Generate a multi-style collage image with consistent subject, 5 cells each rendered in a different art style",
  "subject": {
    "description": "{argument name=\"subject description\" default=\"a cat wearing sunglasses\"}",
    "consistency_rule": "same subject across all 5 cells, only art style changes"
  },
  "layout": {
    "format": "{argument name=\"layout\" default=\"center large + four corner small\"}",
    "panel_count": 5,
    "label_position": "bottom of each cell",
    "label_design": "thin black text + white background"
  },
  "panels": [
    {
      "position": "center",
      "style": "{argument name=\"panel 1 style\" default=\"high-resolution realistic photography\"}",
      "label": "{argument name=\"panel 1 label\" default=\"PHOTO\"}"
    },
    {
      "position": "top-left",
      "style": "{argument name=\"panel 2 style\" default=\"Japanese anime thick painting\"}",
      "label": "{argument name=\"panel 2 label\" default=\"ANIME\"}"
    },
    {
      "position": "top-right",
      "style": "{argument name=\"panel 3 style\" default=\"classical oil painting + gold frame feel\"}",
      "label": "{argument name=\"panel 3 label\" default=\"OIL\"}"
    },
    {
      "position": "bottom-left",
      "style": "{argument name=\"panel 4 style\" default=\"16-bit pixel\"}",
      "label": "{argument name=\"panel 4 label\" default=\"PIXEL\"}"
    },
    {
      "position": "bottom-right",
      "style": "{argument name=\"panel 5 style\" default=\"chibi 3D Pixar style\"}",
      "label": "{argument name=\"panel 5 label\" default=\"3D\"}"
    }
  ],
  "global_constraints": {
    "background": "{argument name=\"background\" default=\"beige paper texture\"}",
    "spacing": "12px white separator"
  },
  "constraints": {
    "must_keep": [
      "Subject highly consistent across 5 cells (recognizable as the same entity / person at a glance)",
      "Clear style difference per cell",
      "Label fonts unified",
      "Overall layout balanced"
    ],
    "avoid": [
      "Subject looking like a different species / different person across cells",
      "Labels obscuring the subject",
      "Different backgrounds causing collage to feel fragmented",
      "Cell sizes with no discernible pattern"
    ]
  }
}
```

### Parameter Strategy

- Must ask: subject, 5 styles
- Can default: layout, labels, background
- Can randomize: details per cell

### Auto-Fill Strategy

- User gives subject → auto-select 5 high-contrast styles (realistic + anime + oil painting + pixel + 3D is the classic combo)
- Default center large + four corner small
- Default small label at bottom of each cell

## Variant 1: 6-Cell "Evolution History" Collage

Prompt

```json
{
  "type": "6-cell evolution history collage",
  "subject": {
    "description": "{argument name=\"subject\" default=\"a car\"}",
    "common_theme": "6-era evolution of the same theme"
  },
  "panels": [
    {"label": "1900s", "style": "vintage black and white film"},
    {"label": "1950s", "style": "vintage color poster"},
    {"label": "1980s", "style": "neo-vaporwave"},
    {"label": "2000s", "style": "digital photography"},
    {"label": "2020s", "style": "modern realistic"},
    {"label": "2050s", "style": "cyberpunk concept art"}
  ],
  "constraints": {
    "must_feel": "sense of time + sense of evolution"
  }
}
```

## Variant 2: 4-Cell "If They Lived in Different Countries"

Prompt

```json
{
  "type": "4-cell international imagination collage",
  "subject": {
    "description": "{argument name=\"subject\" default=\"a coffee shop owner\"}",
    "common_theme": "visual expression of the same identity in different national cultures"
  },
  "panels": [
    {"label": "JAPAN", "style": "Japanese kissaten + warm wood"},
    {"label": "ITALY", "style": "Italian corner cafe + mosaic floor"},
    {"label": "ETHIOPIA", "style": "traditional coffee ceremony + red fabrics"},
    {"label": "USA", "style": "industrial coffee shop + black metal"}
  ],
  "constraints": {
    "must_feel": "cultural feel + same identity"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "mixed style collage auto-fill",
  "mode": "auto-fill",
  "rule": "User gives subject + collage axis (style / era / culture), auto-decide 5 panels",
  "constraints": {
    "must_feel": "virally fun"
  }
}
```

## Things to Avoid

- Do not let panels exceed 6 (visual fragmentation)
- Do not let the subject lose recognizability across cells
- Do not let style contrasts be subtle (looks like the same cell repeated)
- Do not let background colors clash (unify with one base color anchor)
- Do not stuff > 1 line of labels
