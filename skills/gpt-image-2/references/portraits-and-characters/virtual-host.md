# VTuber / Digital Host Character Template

This file is used to generate "virtual host / digital human / VTuber" type character visuals:

- VTuber profile cards
- Digital host main character images
- Live streaming character models
- Cross-dimensional brand ambassador characters

Features:

- 2D / 3D + semi-2D
- Strong character recognizability
- Usually includes name / debut info / tags
- Often paired with background effects and brand colors

## Scope

- VTuber avatars
- Digital human main characters
- Virtual host debut cards
- Cross-dimensional ambassador main images

## When to Use

- User mentions "VTuber / virtual host / digital human / virtual character"
- User wants visuals that are "non-real person" but with strong anthropomorphic feel

Do NOT use for:

- Real person professional headshots (use `professional-portrait.md`)
- Real person founder feature portraits (use `founder-portrait.md`)
- Character design sheets (use `character-sheet.md`)

## Missing Information Priority Question Order

1. Character name / theme
2. Style: Japanese anime / Korean / semi-realistic / cartoon 3D
3. Gender / age setting
4. Color theme
5. Debut info (first stream date / tags)
6. Whether background effects are needed

## Main Template: VTuber Debut Profile Card

📖 Description

Overall a 9:16 or 3:4 card, subject is the virtual host character, with name / debut time / tags / platform logos alongside.

📝 Prompt

```json
{
  "type": "VTuber Debut Profile Card",
  "goal": "Generate a visual that can serve as a VTuber debut day official profile card",
  "character": {
    "name": "{argument name=\"vtuber name\" default=\"Shirobai·Nona\"}",
    "style": "{argument name=\"art style\" default=\"Japanese anime + semi-realistic\"}",
    "gender": "{argument name=\"gender\" default=\"young girl\"}",
    "age_setting": "{argument name=\"age setting\" default=\"18 years old\"}",
    "appearance": "{argument name=\"appearance\" default=\"silver-white long hair, blue bi-colored eyes, snow fleece hat + gothic dress\"}",
    "pose": "{argument name=\"pose\" default=\"half-body front view, slightly tilted head smiling\"}"
  },
  "color_theme": {
    "main_color": "{argument name=\"main color\" default=\"ice blue + moon white\"}",
    "accent_color": "{argument name=\"accent\" default=\"light pink\"}"
  },
  "debut_info": {
    "debut_date": "{argument name=\"debut date\" default=\"2026.05.20\"}",
    "platform": "{argument name=\"platform\" default=\"YouTube · Bilibili\"}",
    "tags": "{argument name=\"tags\" default=\"#FirstStream #SnowFleece #VTuber\"}",
    "agency": "{argument name=\"agency\" default=\"NEX Live\"}"
  },
  "background": {
    "type": "{argument name=\"background\" default=\"winter snowfield + aurora\"}",
    "fx": "{argument name=\"fx\" default=\"falling snowflakes + cold light particles\"}"
  },
  "layout": {
    "character_position": "right half of frame",
    "info_block_position": "left side vertical arrangement",
    "logo_position": "bottom right agency logo"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "character as visual subject",
      "name and debut info clearly readable",
      "main color consistent with character color scheme",
      "agency logo no more than 5%"
    ],
    "avoid": [
      "character face blocked by info blocks",
      "background effects overpowering the character",
      "multiple font types",
      "real platform logos appearing (unless user-provided)"
    ]
  }
}
```

### Parameter Strategy

- Must ask: character name, style, color scheme, debut info
- Can default: background, effects, layout
- Can randomize: background details

### Auto-Complete Strategy

- Style auto-selected by theme (snow = ice blue; fire = red-orange; night = deep purple; spring = cherry pink)
- Outfit matched to style
- Debut info defaults to today + 30 days

## Variant 1: Stream Preview Thumbnail (Landscape)

📝 Prompt

```json
{
  "type": "VTuber Stream Preview Thumbnail",
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"16:9\"}",
  "character": {
    "pose": "{argument name=\"pose\" default=\"upper body + big expression\"}"
  },
  "title_overlay": {
    "main": "{argument name=\"stream title\" default=\"Tonight! First stream!\"}",
    "sub": "{argument name=\"stream sub\" default=\"See you at 21:00 / Snow Fleece\"}"
  },
  "constraints": {
    "must_feel": "streaming feel, inviting, screenshot-worthy"
  }
}
```

## Variant 2: Cross-Dimensional Ambassador Main Image

📝 Prompt

```json
{
  "type": "Cross-Dimensional Ambassador Main Image",
  "character": {
    "pose": "holding endorsed product, looking at camera"
  },
  "brand": {
    "name": "{argument name=\"brand\" default=\"AURORA Coffee\"}",
    "co_brand_visual": "brand logo + product in character's hands"
  },
  "constraints": {
    "must_feel": "endorsement feel, brand consistency, usable as official KV"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "VTuber Character Auto-Complete Template",
  "mode": "auto-fill",
  "rule": "User provides a theme (snow, night, sea, cherry blossoms), auto-generate name, color scheme, outfit, background, debut info",
  "constraints": {
    "must_feel": "ready for official release"
  }
}
```

## Things to Avoid

- Do not let the character's face be obscured by text
- Do not use real copyrighted character designs
- Do not cram > 5 lines of info on a single card
- Do not let background effects overpower the character
- Do not use > 3 font types