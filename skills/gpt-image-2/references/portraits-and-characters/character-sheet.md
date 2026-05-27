# Character Sheet / Turnaround Template

This file is used to generate visuals for "a character's complete design page / turnaround / expression set / accessory set":

- Animation / game character design
- IP mascot design
- Manga protagonist design
- Fan character design
- Brand mascot design

Features:

- Multiple views / multiple poses on a single page
- Annotated color schemes / outfit details / key dimensions
- Grid-based layout
- Similar to animation studio design sheets

## Scope

- Character turnaround (front / side / back)
- Expression nine-grid
- Outfit variants
- Props / weapon collection

## When to Use

- User mentions "character design / turnaround / design sheet / expression set / character sheet"
- User wants a single image that shows a character's complete design package

Do NOT use for:

- Single character portrait (use `professional-portrait.md` / `founder-portrait.md`)
- VTuber profile card (use `virtual-host.md`)

## Missing Information Priority Question Order

1. Character name / concept
2. Style: anime / 3D cartoon / realistic / pixel
3. Gender / age / race
4. Outfit style
5. Sheet type: turnaround / expression set / outfit variants / comprehensive
6. Whether to include annotations and color palette

## Main Template: Character Comprehensive Design Sheet

📖 Description

A single 4:3 or 3:4 large image containing turnaround (front / side / back), expression nine-grid, outfit and accessory close-ups, and color palette.

📝 Prompt

```json
{
  "type": "Character Comprehensive Design Sheet",
  "goal": "Generate a character comprehensive design sheet that can be directly used for animation / game / IP production approval",
  "character": {
    "name": "{argument name=\"character name\" default=\"Shirobai·Nona\"}",
    "concept": "{argument name=\"character concept\" default=\"Winter Watcher, lonely yet resolute\"}",
    "art_style": "{argument name=\"art style\" default=\"anime + semi-realistic\"}",
    "gender": "{argument name=\"gender\" default=\"young girl\"}",
    "age_setting": "{argument name=\"age setting\" default=\"18 years old\"}"
  },
  "sections": {
    "three_view": {
      "enabled": "{argument name=\"three view enabled\" default=\"true\"}",
      "items": ["front full body", "side full body", "back full body"],
      "annotations": ["hair color", "eye color", "outfit layers", "accessories"]
    },
    "expression_grid": {
      "enabled": "{argument name=\"expression grid enabled\" default=\"true\"}",
      "count": "{argument name=\"expression count\" default=\"9\"}",
      "items": ["smile", "laugh", "shy", "angry", "pout", "surprised", "serious", "confused", "sleeping"]
    },
    "outfit_variants": {
      "enabled": "{argument name=\"outfit variants enabled\" default=\"true\"}",
      "count": "{argument name=\"outfit count\" default=\"3\"}",
      "items": [
        "{argument name=\"outfit 1\" default=\"daily gothic dress\"}",
        "{argument name=\"outfit 2\" default=\"combat gear: silver-white armor\"}",
        "{argument name=\"outfit 3\" default=\"casual: sweater + long skirt\"}"
      ]
    },
    "props_and_weapons": {
      "enabled": "{argument name=\"props enabled\" default=\"true\"}",
      "items": ["{argument name=\"prop 1\" default=\"ice crystal staff\"}", "{argument name=\"prop 2\" default=\"snow fleece pendant\"}"]
    },
    "color_palette": {
      "enabled": "{argument name=\"palette enabled\" default=\"true\"}",
      "main": "{argument name=\"palette main\" default=\"ice blue / moon white / silver gray\"}",
      "accent": "{argument name=\"palette accent\" default=\"light pink\"}"
    }
  },
  "layout": {
    "background": "{argument name=\"background\" default=\"cream-white grid background, clean like a design sheet\"}",
    "grid": "entire sheet divided by thin lines, each area has title + annotations"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"4:3\"}",
  "constraints": {
    "must_keep": [
      "turnaround proportions strictly consistent",
      "expressions on the same face shape, only expressions change",
      "outfit variants retain the same facial appearance",
      "color palette matches the character's actual colors"
    ],
    "avoid": [
      "turnaround views look like three different people",
      "duplicate expressions in the nine-grid",
      "annotation lines crossing each other",
      "background overpowering the character"
    ]
  }
}
```

### Parameter Strategy

- Must ask: character name, style, gender, concept
- Can default: sheet type combination, background, layout
- Can randomize: expression types, accessory designs

### Auto-Complete Strategy

- Style auto-selected by IP type (young girl anime / male realistic / mascot 3D)
- Default includes turnaround + expression nine-grid + color palette
- No weapons unless specified

## Variant 1: Pure Expression Nine-Grid

📝 Prompt

```json
{
  "type": "Character Expression Nine-Grid Sheet",
  "sections": {
    "three_view": { "enabled": false },
    "expression_grid": { "enabled": true, "count": 9 },
    "outfit_variants": { "enabled": false }
  },
  "constraints": {
    "must_feel": "can be used as sticker pack / streaming emote assets"
  }
}
```

## Variant 2: Outfit Variant Collection

📝 Prompt

```json
{
  "type": "Character Outfit Variant Collection Sheet",
  "sections": {
    "three_view": { "enabled": false },
    "expression_grid": { "enabled": false },
    "outfit_variants": { "enabled": true, "count": 5 }
  },
  "constraints": {
    "must_feel": "can be used as outfit planning draft"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Character Design Auto-Complete Template",
  "mode": "auto-fill",
  "rule": "User provides a concept sentence, auto-generate full design (views, expressions, outfits, colors)",
  "constraints": {
    "must_feel": "ready for production approval"
  }
}
```

## Things to Avoid

- Do not make turnaround proportions inconsistent (most common error)
- Do not have duplicate expressions in the nine-grid
- Do not add complex scene backgrounds to design sheets
- Do not let annotations cover the character's body
- Do not use real copyrighted characters as references