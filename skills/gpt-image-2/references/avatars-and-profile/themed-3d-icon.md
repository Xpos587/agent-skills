# Themed 3D Icon Avatar Template

This file is used for "3D cartoon / chibi icon-level" avatar visuals:

- Kawaii 3D character icons
- Minecraft-style skin renders
- Skeuomorphic 3D avatars
- App icon-style avatars
- Merchandise stickers / merchandise small characters

Features:

- 3D rendered feel
- Chibi, cute, strong theme feel
- Single image / single character
- Rounded square / circular composition
- Suitable for social platform avatars / app icons

## Scope

- Rounded square / circular avatars
- App icons
- Merchandise small character images
- Cartoon version of "me"

## When to Use

- User wants a 3D cartoon version of a character or themselves
- User wants a Pixar / Kawaii / chibi character avatar
- User wants the character as an icon-level presence for their IP

Do NOT use for:

- Realistic style selfies (use `style-transfer-selfie.md`)
- Multi-version grid (use `character-grid-portrait.md`)
- Character complete design sheets (use `portraits-and-characters/character-sheet.md`)

## Missing Information Priority Question Order

1. Theme (cat / character / self / hobby)
2. Style base (Kawaii chibi / Pixar realistic cartoon / Minecraft pixel 3D / skeuomorphic 3D)
3. Color scheme / main color
4. Accessories / props (glasses / hat / item in hand)
5. Composition: bust / full body / head only
6. Output format: circular / rounded square / transparent background

## Main Template: Kawaii 3D Character Icon

📖 Description

Overall a 1:1 avatar image, subject is a chibi 3D character, rounded square composition, solid color background.

📝 Prompt

```json
{
  "type": "Kawaii 3D Character Icon",
  "goal": "Generate a 3D chibi character image that can serve as a social platform avatar / app icon / merchandise small character",
  "character": {
    "subject": "{argument name=\"character subject\" default=\"round orange shiba inu\"}",
    "personality": "{argument name=\"personality\" default=\"happy, clever\"}",
    "expression": "{argument name=\"expression\" default=\"smile + open mouth with tongue out\"}",
    "pose": "{argument name=\"pose\" default=\"front-facing bust, looking at camera\"}",
    "outfit_or_accessory": [
      "{argument name=\"item 1\" default=\"small red bow tie\"}",
      "{argument name=\"item 2\" default=\"tiny bell\"}"
    ]
  },
  "style": {
    "rendering": "{argument name=\"rendering\" default=\"3D Pixar style + slight toon shading\"}",
    "color_palette": "{argument name=\"color palette\" default=\"warm orange + cream white\"}",
    "lighting": "{argument name=\"lighting\" default=\"soft light + slight backlight\"}"
  },
  "background": {
    "type": "{argument name=\"background\" default=\"cream yellow solid + very faint halo\"}"
  },
  "format": {
    "shape": "{argument name=\"shape\" default=\"rounded square\"}",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"1:1\"}",
    "composition_safety": "subject has 10% margin, avoid being cropped"
  },
  "constraints": {
    "must_keep": [
      "overall chibi and cute",
      "subject clearly centered",
      "color scheme ≤ 3 colors",
      "details restrained (do not cram too many elements)"
    ],
    "avoid": [
      "realistic style mixing in",
      "colors saturated to the point of being harsh",
      "background interfering with subject",
      "accessories blocking character face"
    ]
  }
}
```

### Parameter Strategy

- Must ask: character theme, expression
- Can default: style, color scheme, background, format
- Can randomize: specific accessory designs

### Auto-Complete Strategy

- When user provides a subject (shiba / cat / self / hobby): auto-select chibi style + warm colors + rounded square
- Default 1-2 accessories
- Default 1:1 aspect ratio

## Variant 1: Minecraft-Style Skin Render

📝 Prompt

```json
{
  "type": "Minecraft-Style Personalized Skin Render",
  "character": {
    "subject": "{argument name=\"character\" default=\"minecraft character stylized after the reference image person\"}",
    "outfit": "{argument name=\"outfit\" default=\"blue T-shirt + jeans + red backpack\"}"
  },
  "style": {
    "rendering": "Minecraft voxel 3D style, blocky body, pixel textures",
    "color_palette": "Minecraft standard 16-color palette"
  },
  "background": {
    "type": "Minecraft grass block scene"
  },
  "constraints": {
    "must_feel": "recognizable as Minecraft style and looks like them"
  }
}
```

## Variant 2: Skeuomorphic 3D App Icon

📝 Prompt

```json
{
  "type": "Skeuomorphic 3D App Icon-Style Avatar",
  "character": {
    "subject": "{argument name=\"theme\" default=\"photography enthusiast\"}",
    "metaphor_object": "{argument name=\"object\" default=\"3D camera + slight reflection\"}"
  },
  "style": {
    "rendering": "skeuomorphic 3D + soft light + thick shadows",
    "color_palette": "Apple Big Sur style"
  },
  "background": {
    "type": "rounded square light gray gradient"
  },
  "constraints": {
    "must_feel": "like a real clickable app icon"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "3D Icon Avatar Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides a theme (interest / personality / preference) and auto-decide character image, style, color scheme, format",
  "constraints": {
    "must_feel": "ready to swap as avatar"
  }
}
```

## Things to Avoid

- Do not make the 3D character look "half-real half-fake" (either chibi or skeuomorphic, not neither)
- Do not let the background be so flashy it overpowers the subject
- Do not let the avatar contain readable English labels / text
- Do not let accessories block the face
- Do not cram > 2 characters in a single icon