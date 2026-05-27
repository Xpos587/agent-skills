# Anime Key Visual Single Image Template

This file is used for "a single image that represents an entire work" anime main visuals:

- Anime KV / main visuals
- Light novel covers
- Doujinshi covers
- Anime posters
- Game card main images (without UI)

Features:

- A single image gathering multiple characters or one character + strong atmosphere
- Dramatic composition and lighting
- Anime / semi-realistic style
- Usually vertical 3:4 / 4:5
- Title space reserved

## Scope

- Anime main visuals
- Light novel / doujinshi covers
- IP posters
- Game card art

## When to Use

- User mentions "anime KV / anime main visual / light novel cover / IP poster"
- User wants a single image that tells the entire world's story
- User wants anime-style high-finish large image

Do NOT use for:

- Multi-panel narrative (use `manga-spread-page.md`)
- 4-panel comics (use `four-panel-comic.md`)
- Real person feature portraits (use `portraits-and-characters/founder-portrait.md`)
- Cinematic concept epic scenes (use `scenes-and-illustrations/concept-scene.md`)

## Missing Information Priority Question Order

1. Work / theme
2. Main character design (count + relationship)
3. World-building / era / atmosphere
4. Style: modern anime / 90s anime / semi-realistic
5. Whether title space is needed
6. Aspect ratio

## Main Template: Anime Key Visual Single Image

📖 Description

Overall a large image, containing main character + scene atmosphere + title space, strong narrative feel.

📝 Prompt

```json
{
  "type": "Anime Key Visual",
  "goal": "Generate a single image that can serve as an anime / light novel / IP main visual",
  "ip": {
    "title": "{argument name=\"ip title\" default=\"Frost White Fantasia\"}",
    "tagline": "{argument name=\"tagline\" default=\"This snow has been falling for a thousand years\"}"
  },
  "characters": {
    "count": "{argument name=\"character count\" default=\"3\"}",
    "items": [
      "{argument name=\"character 1\" default=\"female protagonist, silver-white long hair, blue eyes, snow-white dress\"}",
      "{argument name=\"character 2\" default=\"swordsman companion, black hair, battle armor\"}",
      "{argument name=\"character 3\" default=\"small animal companion, snow-white fox\"}"
    ],
    "composition_relationship": "{argument name=\"composition\" default=\"protagonist centered, companions flanking left and right, animal at feet\"}"
  },
  "world": {
    "scene": "{argument name=\"scene\" default=\"frozen city, distant castle, falling snow\"}",
    "lighting": "{argument name=\"lighting\" default=\"cold blue key light + warm gold rim light\"}",
    "atmosphere": "{argument name=\"atmosphere\" default=\"epic, solitude, resolute\"}"
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"modern anime + semi-realistic + impasto background\"}",
    "color_palette": "{argument name=\"color palette\" default=\"ice blue + moon white + warm gold\"}"
  },
  "title_block": {
    "enabled": "{argument name=\"title block enabled\" default=\"true\"}",
    "main_title": "{argument name=\"main title\" default=\"Frost White Fantasia\"}",
    "sub_title": "{argument name=\"sub title\" default=\"FROZEN FANTASIA\"}",
    "position": "{argument name=\"title position\" default=\"top center of frame\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "protagonist as absolute visual center",
      "lighting direction consistent",
      "color palette strictly unified",
      "title and protagonist do not overlap"
    ],
    "avoid": [
      "too many characters making faces too small to identify",
      "background too bright overwhelming characters",
      "extra bright colors appearing in the palette",
      "too many font types for title"
    ]
  }
}
```

### Parameter Strategy

- Must ask: work name, main characters, world-building
- Can default: style, color scheme, title space
- Can randomize: background details

### Auto-Complete Strategy

- Default 1-3 main characters
- World-building → auto-determine color scheme (cold world = blue-white / post-apocalyptic = scorched earth brown / school = warm orange)
- Default vertical 3:4

## Variant 1: Single Character + Extremely Strong Atmosphere KV

📝 Prompt

```json
{
  "type": "Single Character + Strong Atmosphere KV",
  "characters": {
    "count": 1,
    "items": ["{argument name=\"character\" default=\"long-haired girl, backlit\"}"]
  },
  "world": {
    "atmosphere": "solitude + mysterious"
  },
  "constraints": {
    "must_feel": "movie poster feel"
  }
}
```

## Variant 2: Group KV (5+ Characters)

📝 Prompt

```json
{
  "type": "Group KV",
  "characters": {
    "count": 6,
    "composition_relationship": "pyramid composition: protagonist at top + supporting characters surrounding"
  },
  "constraints": {
    "must_feel": "team feel, epic, can serve as anime premiere main image"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Anime KV Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides a work concept sentence, auto-decide main characters, composition, world-building, title",
  "constraints": {
    "must_feel": "ready for premiere launch"
  }
}
```

## Things to Avoid

- Do not exceed 7 characters (face recognition will fail)
- Do not let lighting directions be inconsistent
- Do not let the title cover the protagonist's face
- Do not use > 4 main colors
- Do not let background detail exceed character detail