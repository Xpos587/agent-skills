# Concept / Epic Scene Illustration Template

This file is used to generate "cinematic epic scenes / concept art / epic illustrations":

- Game concept art
- Movie key art
- Novel / IP main visuals
- Trailer poster scenes
- World-building introduction scenes

Features:

- Large scenes / sweeping perspectives
- Intense atmosphere
- High visual information density
- Dramatic lighting
- Suitable for large-format display

## Scope

- Game / animation / movie concept art
- Novel / IP main visuals
- Trailer posters
- World-building main images

## When to Use

- User mentions "concept art / key art / epic scene / cinematic / epic"
- User wants a single image that tells an entire world's story

Do NOT use for:

- Cozy everyday scenes (use `healing-scene.md`)
- Picture book style (use `picture-book-scene.md`)
- Minimalist mood (use `minimalist-mood-scene.md`)

## Missing Information Priority Question Order

1. World-building theme (cyberpunk / Eastern fantasy / post-apocalyptic / space / wuxia)
2. Subject (character + distant view / giant creature / city)
3. Time / weather / atmosphere
4. Color scheme + lighting tone
5. Aspect ratio (landscape 21:9 / 16:9 / vertical 9:16)
6. Whether a title text area is needed

## Main Template: Cinematic Concept Epic Scene

📖 Description

Overall wide-format image, foreground character + midground narrative + background sweeping perspective, dramatic lighting, title area reserved.

📝 Prompt

```json
{
  "type": "Cinematic Concept Epic Scene",
  "goal": "Generate a concept epic scene that can serve as game key art / movie key art / IP world-building main visual",
  "world": {
    "theme": "{argument name=\"world theme\" default=\"cyberpunk Eastern metropolis\"}",
    "tone": "{argument name=\"world tone\" default=\"neon + rainy night + high-density architecture\"}"
  },
  "composition": {
    "foreground": "{argument name=\"foreground\" default=\"female protagonist back view holding umbrella\"}",
    "midground": "{argument name=\"midground\" default=\"wet street + neon signs + reflections\"}",
    "background": "{argument name=\"background\" default=\"towering skyscrapers + holographic ads\"}",
    "perspective": "{argument name=\"perspective\" default=\"low angle looking up\"}"
  },
  "lighting": {
    "key_light": "{argument name=\"key light\" default=\"neon pink + neon blue alternating\"}",
    "fill_light": "{argument name=\"fill light\" default=\"wet ground reflections\"}",
    "atmosphere": "{argument name=\"atmosphere\" default=\"moist air + rain + light particles\"}"
  },
  "color_palette": "{argument name=\"color palette\" default=\"neon pink + electric blue + deep black\"}",
  "title_safe_area": "{argument name=\"title area\" default=\"top 1/4 of frame reserved for title\"}",
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"21:9\"}",
  "style": {
    "rendering": "cinematic concept art + digital painting + high detail"
  },
  "constraints": {
    "must_keep": [
      "foreground, midground, background layers clearly separated",
      "lighting direction consistent",
      "color palette strictly unified",
      "foreground character silhouette clear"
    ],
    "avoid": [
      "foreground and background blending together",
      "excessive detail filling the frame",
      "real brand logo signs appearing",
      "sudden color tone shifts"
    ]
  }
}
```

### Parameter Strategy

- Must ask: world-building, composition layers, aspect ratio
- Can default: lighting, color scheme, style
- Can randomize: background detail specifics

### Auto-Complete Strategy

- Theme auto-selects color scheme (cyber = neon / wuxia = ink wash / post-apocalyptic = scorched earth brown / space = deep purple)
- Default 21:9 landscape
- Auto-reserve title area

## Variant 1: Vertical IP Main Visual

📝 Prompt

```json
{
  "type": "Vertical IP Main Visual",
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"9:16\"}",
  "composition": {
    "foreground": "protagonist full body centered",
    "midground": "halo + companion silhouettes",
    "background": "core building representing the world"
  },
  "constraints": {
    "must_feel": "poster feel, heroic, launch main image"
  }
}
```

## Variant 2: Natural Wonder Epic Scene

📝 Prompt

```json
{
  "type": "Natural Wonder Epic Scene",
  "world": {
    "theme": "{argument name=\"natural theme\" default=\"polar ice floes + giant whale\"}",
    "tone": "solitude, grandeur, solemnity"
  },
  "composition": {
    "foreground": "tiny human figure",
    "background": "gigantic natural subject"
  },
  "constraints": {
    "must_feel": "insignificant vs grand"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Concept Epic Scene Auto-Complete Template",
  "mode": "auto-fill",
  "rule": "User provides a world-building sentence, auto-decide composition, lighting, color scheme, aspect ratio",
  "constraints": {
    "must_feel": "can serve as large screen / launch KV"
  }
}
```

## Things to Avoid

- Do not let foreground and background blend into the same color
- Do not let lighting sources be inconsistent
- Do not cram too many minor details
- Do not make characters larger than buildings (breaks world scale)
- Do not use > 4 main colors