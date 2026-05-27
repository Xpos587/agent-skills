# Sticker Set Template

This file is used for "a single image containing N independent cuttable stickers":

- Fun animal stickers
- Character expression stickers
- Themed holiday stickers
- Industry / interest themed stickers
- iMessage / Telegram style sticker packs

Features:

- Multiple independent small elements in one image
- Each element has a transparent / white / outlined border
- Not connected to each other
- Can be printed as a whole sheet or individually cut
- Highly unified style

## Scope

- Sticker sets (4-12)
- Emoji collections
- Holiday gift box stickers
- Merchandise sticker cards

## When to Use

- User mentions "stickers / sticker set / emoji pack"
- User wants multiple independent small elements in one image
- User wants each element to be usable independently

Do NOT use for:

- Same character multi-expression nine-grid (use `character-grid-portrait.md`)
- Multi-version avatars (use `themed-3d-icon.md`)
- Multi-panel story collages (use `grids-and-collages/mixed-style-multi-panel.md`)

## Missing Information Priority Question Order

1. Theme (animals / food / characters / holiday / mood)
2. Sticker count (4 / 6 / 8 / 9 / 12)
3. Style: hand-drawn / 3D chibi / skeuomorphic / anime
4. Whether to include text labels
5. Color tone base
6. Whether white outlines are needed

## Main Template: Fun Animal Sticker Set (9 Stickers)

📖 Description

Overall 1:1 or 4:3 large image, light cream background, 9 independent stickers in a 3×3 arrangement, each with a white outline.

📝 Prompt

```json
{
  "type": "Sticker Set",
  "goal": "Generate a collection image containing N independent small stickers, each sticker can be cut out and used individually",
  "theme": "{argument name=\"theme\" default=\"fun animal everyday\"}",
  "style": {
    "rendering": "{argument name=\"art style\" default=\"3D chibi + soft light\"}",
    "color_palette": "{argument name=\"color palette\" default=\"warm orange + cream white + light green\"}"
  },
  "sticker_design": {
    "outline": "{argument name=\"outline\" default=\"3px white outline\"}",
    "shadow": "{argument name=\"shadow\" default=\"slight bottom drop shadow\"}",
    "with_label": "{argument name=\"with label\" default=\"true\"}",
    "label_style": "{argument name=\"label style\" default=\"rounded handwriting font, dark brown\"}"
  },
  "layout": {
    "background": "{argument name=\"background\" default=\"light cream + subtle paper texture\"}",
    "grid": "{argument name=\"grid\" default=\"3x3\"}",
    "spacing": "even spacing between stickers",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"1:1\"}"
  },
  "stickers": {
    "count": "{argument name=\"sticker count\" default=\"9\"}",
    "items": [
      "{argument name=\"sticker 1\" default=\"orange cat drinking coffee + label 'morning'\"}",
      "{argument name=\"sticker 2\" default=\"little shiba holding a balloon + label 'yay'\"}",
      "{argument name=\"sticker 3\" default=\"little bear yawning + label 'sleepy'\"}",
      "{argument name=\"sticker 4\" default=\"rabbit wearing sunglasses + label 'cool'\"}",
      "{argument name=\"sticker 5\" default=\"capybara holding flowers + label 'love'\"}",
      "{argument name=\"sticker 6\" default=\"little fox jumping + label 'go'\"}",
      "{argument name=\"sticker 7\" default=\"owl reading a book + label 'study'\"}",
      "{argument name=\"sticker 8\" default=\"hamster eating cake + label 'yum'\"}",
      "{argument name=\"sticker 9\" default=\"penguin waving + label 'hi'\"}"
    ]
  },
  "constraints": {
    "must_keep": [
      "each sticker independent, not connected to others",
      "overall style unified, no drift",
      "white outlines even",
      "label font consistent"
    ],
    "avoid": [
      "sticker size differences too large",
      "mixed styles (realistic + cartoon)",
      "label typos",
      "background overpowering stickers"
    ]
  }
}
```

### Parameter Strategy

- Must ask: theme, count
- Can default: style, outline, labels
- Can randomize: specific sticker designs

### Auto-Complete Strategy

- Default 9 stickers (3×3)
- Default white outlines + short labels
- Style auto-selected by theme (animals = chibi / food = 3D skeuomorphic / holiday = holiday colors)

## Variant 1: Holiday Sticker Set

📝 Prompt

```json
{
  "type": "Holiday Sticker Set",
  "theme": "{argument name=\"festival\" default=\"Christmas\"}",
  "style": {
    "color_palette": "Christmas red + Christmas green + gold"
  },
  "stickers": {
    "count": 6,
    "items": [
      "Christmas tree + 'Merry'",
      "Snowman + 'Joy'",
      "Gift box + 'Gift'",
      "Santa face + 'Ho Ho Ho'",
      "Reindeer + 'Rudolph'",
      "Snowflake + 'Cool'"
    ]
  },
  "constraints": {
    "must_feel": "holiday atmosphere, shareable, printable"
  }
}
```

## Variant 2: Mood Expression Stickers (No Text)

📝 Prompt

```json
{
  "type": "Mood Expression Stickers (No Text)",
  "sticker_design": {
    "with_label": false
  },
  "stickers": {
    "count": 12,
    "items": ["happy", "angry", "pouting", "speechless", "dying of laughter", "shocked", "sleepy", "hungry", "smitten", "cool", "awkward", "bye"]
  },
  "constraints": {
    "must_feel": "ready to use as emoji pack"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Sticker Set Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides theme, auto-decide count, style, color scheme, label content",
  "constraints": {
    "must_feel": "ready to print / upload to iMessage"
  }
}
```

## Things to Avoid

- Do not exceed 16 stickers (visual density too high)
- Do not let sticker size difference exceed 2x
- Do not mix realistic and chibi styles
- Do not use more than 1 label font type
- Do not let background show identifiable logos
- Do not overlap stickers with each other (must be independent)