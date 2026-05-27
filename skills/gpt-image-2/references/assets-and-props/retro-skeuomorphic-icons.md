# Skeuomorphic / Retro Icon Set Template

This file is used for "icon sets / skeuomorphic / Y2K / retro" icon visuals:

- Skeuomorphic app icon sets
- Y2K style crystal icons
- Pixel / retro game icons
- Themed icon packs (life / work / travel)
- UI icon systems

Characteristics:

- Multiple icons with unified style
- Usually 6 / 8 / 12 / 16 icons
- Each icon in rounded square / circle
- Emphasis on material texture (glass / metal / skeuomorphic)
- Suitable as app icon packs / icon sets

## Scope

- App icon sets
- Themed icon packs
- UI icon systems
- Merchandise stickers / cards

## When to use

- User mentions "icons / icon set / skeuomorphic / skeuomorphic / Y2K / pixel icons"
- User wants a complete icon set

Do NOT use for:

- Single 3D icon avatar → use `avatars-and-profile/themed-3d-icon.md`
- Sticker sets → use `avatars-and-profile/sticker-set.md`
- General brand identity → use `branding-and-packaging/brand-identity-board.md`

## Missing Information Priority Question Order

1. Style (skeuomorphic / Y2K / pixel / Flat / Glass / Clay)
2. Icon theme (apps / work / life / travel)
3. Icon count (6 / 8 / 12 / 16)
4. Primary color 1-2
5. Shape base (rounded square / circle / freeform)
6. Whether to include text labels

## Main Template: Skeuomorphic App Icon Set

Description

One image containing N skeuomorphic icons with unified style, arranged in a grid.

Prompt

```json
{
  "type": "skeuomorphic app icon set",
  "goal": "Generate a set of unified-style icons, usable as an icon pack / theme pack",
  "theme": "{argument name=\"theme\" default=\"classic office apps\"}",
  "style": {
    "rendering": "{argument name=\"rendering\" default=\"skeuomorphic 3D + soft light + soft shadows\"}",
    "material": "{argument name=\"material\" default=\"glass texture + subtle reflection\"}",
    "color_palette": "{argument name=\"color palette\" default=\"off-white + warm orange + light blue + gray\"}",
    "shape_base": "{argument name=\"shape base\" default=\"rounded square (24% corner radius)\"}"
  },
  "layout": {
    "grid": "{argument name=\"grid\" default=\"4x3\"}",
    "icon_count": "{argument name=\"icon count\" default=\"12\"}",
    "spacing": "16px",
    "background": "{argument name=\"background\" default=\"beige paper texture\"}",
    "label_below": "{argument name=\"label below\" default=\"true\"}",
    "label_style": "thin gray sans-serif small text"
  },
  "icons": [
    {"id": 1, "concept": "{argument name=\"icon 1\" default=\"Mail - envelope + glow indicator\"}", "label": "Mail"},
    {"id": 2, "concept": "{argument name=\"icon 2\" default=\"Calendar - open page + red today marker\"}", "label": "Calendar"},
    {"id": 3, "concept": "{argument name=\"icon 3\" default=\"Notes - yellow sticky note + red bookmark\"}", "label": "Notes"},
    {"id": 4, "concept": "{argument name=\"icon 4\" default=\"Camera - vintage film camera\"}", "label": "Camera"},
    {"id": 5, "concept": "{argument name=\"icon 5\" default=\"Music - vinyl record\"}", "label": "Music"},
    {"id": 6, "concept": "{argument name=\"icon 6\" default=\"Maps - folded map + red pin\"}", "label": "Maps"},
    {"id": 7, "concept": "{argument name=\"icon 7\" default=\"Weather - sun + cloud\"}", "label": "Weather"},
    {"id": 8, "concept": "{argument name=\"icon 8\" default=\"Calculator - number keypad\"}", "label": "Calc"},
    {"id": 9, "concept": "{argument name=\"icon 9\" default=\"Clock - circular dial\"}", "label": "Clock"},
    {"id": 10, "concept": "{argument name=\"icon 10\" default=\"Settings - gear\"}", "label": "Settings"},
    {"id": 11, "concept": "{argument name=\"icon 11\" default=\"Health - heart pulse line\"}", "label": "Health"},
    {"id": 12, "concept": "{argument name=\"icon 12\" default=\"Wallet - brown leather wallet\"}", "label": "Wallet"}
  ],
  "constraints": {
    "must_keep": [
      "12 icons strictly unified style (same light source, same corner radius, same thickness)",
      "Color palette ≤ 6 colors",
      "Label font consistent",
      "Each icon individually recognizable"
    ],
    "avoid": [
      "Icon style drift (some skeuomorphic, some flat)",
      "More than 6 colors",
      "Too many details inside icons",
      "Label typos"
    ]
  }
}
```

### Parameter Strategy

- Must ask: theme, count, style
- Can default: layout, color palette, shape base
- Can randomize: specific design per icon

### Auto-Fill Strategy

- User gives theme + count → auto-expand each icon's specific appearance
- Default 4×3 = 12 icons
- Default skeuomorphic 3D + glass texture

## Variant 1: Y2K Crystal Icon Pack

Prompt

```json
{
  "type": "Y2K crystal icon pack",
  "style": {
    "material": "transparent crystal + refracted light",
    "color_palette": "high-saturation pink + blue-purple + silver"
  },
  "constraints": {
    "must_feel": "Y2K Aero style"
  }
}
```

## Variant 2: Pixel Retro Game Icons

Prompt

```json
{
  "type": "pixel retro game icons",
  "style": {
    "rendering": "16-bit pixel + sharp edges",
    "color_palette": "16-color retro game palette"
  },
  "constraints": {
    "must_feel": "FC / SNES era"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "icon pack auto-fill",
  "mode": "auto-fill",
  "rule": "User gives theme, auto-decide icon count, style, color palette, layout",
  "constraints": {
    "must_feel": "publishable as an icon pack"
  }
}
```

## Things to Avoid

- Do not let icon styles drift
- Do not let color palette exceed 6
- Do not let label fonts exceed 1 type
- Do not stuff > 3 elements inside a single icon
- Do not let grid sizes be inconsistent
- Do not let icons have insufficient contrast against background
