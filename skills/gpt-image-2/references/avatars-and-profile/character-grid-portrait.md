# Character n×n Grid Portrait Template

This file is used for "a single image containing multiple versions of the same character (different expressions / different professions / different eras / different expressions)":

- 2×2 / 3×3 / 4×4 same person multi-profession / multi-scene
- Expression nine-grid (happy, angry, sad, joyful + more)
- Dynasty / mythological character series portraits
- Multiple style unified showcase
- Multi-character group portrait grid

Features:

- Single image divided into multiple panels
- Each panel is a different presentation of the same identity
- Grid lines / transparent separators
- Emphasis on "same person / same character" consistency

## Scope

- One person multi-profession grid
- Expression nine-grid
- Same character different eras / cultures
- Same character different styling collection

## When to Use

- User wants a single image showing multiple facets of a person
- User wants a "grid image" rather than a single image
- User wants multi-version comparison of the same identity

Do NOT use for:

- Expression / outfit design sheets (use `portraits-and-characters/character-sheet.md`)
- Single image style transfer (use `style-transfer-selfie.md`)
- Multiple different character collages (use `grids-and-collages/mixed-style-multi-panel.md`)

## Missing Information Priority Question Order

1. Subject identity (reference image / text description)
2. Grid specification (2×2 / 3×3 / 4×4)
3. Variation dimension per panel (profession / expression / era / style)
4. Specific content per panel (user list or we help list)
5. Style base (realistic / 3D cartoon / anime)
6. Aspect ratio

## Main Template: 2×2 Same Person Multi-Profession Grid

📖 Description

2×2 four panels, subject is the same person, each in a different profession / scene.

📝 Prompt

```json
{
  "type": "2x2 Same Person Multi-Profession Grid",
  "goal": "Generate a 2×2 grid image, subject is the same person, each panel presents a different professional identity and scene, usable as LinkedIn / self-introduction / creative avatar",
  "subject": {
    "description": "{argument name=\"subject description\" default=\"East Asian young male, short black hair, natural smile\"}",
    "consistency": "face shape, skin tone, and facial proportions must be strictly consistent across all four panels"
  },
  "style": "{argument name=\"art style\" default=\"high-resolution realistic portrait photography + natural light\"}",
  "layout": {
    "format": "2x2 grid",
    "panel_count": 4,
    "gap": "thin white separator lines",
    "panels": [
      {
        "position": "top-left",
        "scenario": "{argument name=\"panel 1\" default=\"Business professional: dark navy suit + white shirt + blue tie, gray textured background\"}"
      },
      {
        "position": "top-right",
        "scenario": "{argument name=\"panel 2\" default=\"Outdoor casual: dark blue T-shirt, blurred park background\"}"
      },
      {
        "position": "bottom-left",
        "scenario": "{argument name=\"panel 3\" default=\"Construction worker: yellow hard hat + orange reflective vest, blurred workshop background\"}"
      },
      {
        "position": "bottom-right",
        "scenario": "{argument name=\"panel 4\" default=\"Medical staff: white lab coat + light blue shirt, blurred lab background\"}"
      }
    ]
  },
  "constraints": {
    "must_keep": [
      "same person across four panels",
      "natural and unified lighting style per panel",
      "clothing highly matched with scene",
      "clear thin separator lines"
    ],
    "avoid": [
      "four panels looking like four different people",
      "obvious clothing-scene mismatches",
      "grid lines too thick breaking the visual",
      "style drift per panel"
    ]
  }
}
```

### Parameter Strategy

- Must ask: subject description, 4 variation dimensions
- Can default: style base, grid separator lines
- Can randomize: background details per panel

### Auto-Complete Strategy

- When user only provides the subject: auto-select 4 high-contrast professions / scenes (business + outdoor + blue-collar + medical is a classic combination)
- Default 2×2 grid
- Default realistic photography

## Variant 1: 3×3 Expression Nine-Grid (Same Character)

📝 Prompt

```json
{
  "type": "3x3 Same Character Expression Nine-Grid",
  "subject": {
    "description": "{argument name=\"character\" default=\"3D animation style, round-frame glasses, natural short hair\"}",
    "common_theme": "{argument name=\"framing concept\" default=\"peeking through torn white paper\"}"
  },
  "style": "{argument name=\"art style\" default=\"3D Pixar animation style\"}",
  "layout": {
    "format": "3x3 grid",
    "panel_count": 9,
    "panels": [
      {"expression": "blinking", "action": "adjusting glasses", "outfit": "green sweater"},
      {"expression": "smirk", "action": "pulling down sunglasses", "outfit": "red leather jacket"},
      {"expression": "thinking", "action": "finger on chin", "outfit": "yellow hoodie"},
      {"expression": "laughing", "action": "leaning on the hole edge", "outfit": "black-and-white striped shirt"},
      {"expression": "smiling", "action": "thumbs up", "outfit": "orange shirt"},
      {"expression": "calm", "action": "drinking boba tea", "outfit": "blue sweater"},
      {"expression": "happy", "action": "waving", "outfit": "purple vest + white shirt"},
      {"expression": "laughing eyes closed", "action": "arms crossed", "outfit": "pink cardigan"},
      {"expression": "goofy", "action": "poking cheek", "outfit": "teal sweater"}
    ]
  },
  "constraints": {
    "must_feel": "nine panels are the same character, only expression / action / outfit varies"
  }
}
```

## Variant 2: 3×3 Historical Dynasty Portrait Series

📝 Prompt

```json
{
  "type": "3x3 Dynasty Portrait Series",
  "subject": {
    "description": "{argument name=\"subject\" default=\"East Asian male, 30 years old, composed demeanor\"}",
    "common_theme": "same person in different dynasties"
  },
  "style": "high-resolution ink wash realistic",
  "layout": {
    "format": "3x3 grid",
    "panel_count": 9,
    "items": [
      "Han / Tang / Song / Yuan / Ming / Qing / Republican / Early PRC / Modern"
    ]
  },
  "constraints": {
    "must_feel": "nine panels are the same person, only attire, accessories, and background match the era"
  }
}
```

## Variant 3: 4×4 Same Character Style Collection

📝 Prompt

```json
{
  "type": "4x4 Same Character Style Collection",
  "subject": "{argument name=\"subject\" default=\"self based on reference image\"}",
  "layout": {
    "format": "4x4 grid",
    "panel_count": 16,
    "common_theme": "16 different styles of the same identity (cyberpunk / street / classical / Y2K / minimalist / oil painting / gothic / ...)"
  },
  "constraints": {
    "must_feel": "16 panels with high style contrast but identity remains consistent"
  }
}
```

## Variant 4: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Character Grid Portrait Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides subject + grid specification, auto-decide content per panel, style, composition",
  "constraints": {
    "must_feel": "ready to use as avatar collection / sticker pack / self-intro image"
  }
}
```

## Things to Avoid

- Do not let different panels look like different people (consistency is core)
- Do not make grid separator lines too thick
- Do not let style drift per panel (overall style should be unified)
- Do not exceed 4×4 (any more makes each panel too small)
- Do not scatter the grid theme across completely unrelated topics (maintain a consistent dimension)