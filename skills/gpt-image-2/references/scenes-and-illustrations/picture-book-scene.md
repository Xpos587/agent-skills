# Picture Book / Children's Book Scene Illustration Template

This file is used to generate "picture book / children's book / children's content" style illustrations:

- Picture book interior pages / covers
- Children's content social media header images
- Picture book style merchandise
- Educational content illustrations
- Holiday cards

Features:

- Soft watercolor / crayon / collage style
- Chibi cute characters
- Warm colors
- Clear, easy-to-understand information
- Story-like quality

## Scope

- Picture book interior pages / covers
- Educational content illustrations
- Children's holiday cards
- Children's brand illustrations

## When to Use

- User mentions "picture book / children's book / children's / crayon style / watercolor picture book style"
- User wants warm, childlike, story-like feel

Do NOT use for:

- Healing everyday scenes (use `healing-scene.md`)
- Concept epic scenes (use `concept-scene.md`)
- Minimalist mood (use `minimalist-mood-scene.md`)

## Missing Information Priority Question Order

1. Story / theme
2. Main character (child / animal)
3. Scene
4. Style: watercolor / crayon / collage / anime children's style
5. Whether to include text
6. Aspect ratio

## Main Template: Picture Book Interior Page Illustration

📖 Description

Overall a picture book illustration page, main character is chibi cute, scene has soft light, optionally includes 1 line of story text.

📝 Prompt

```json
{
  "type": "Picture Book Interior Page Illustration",
  "goal": "Generate a warm illustration that can be directly used as a picture book interior page",
  "story": {
    "theme": "{argument name=\"story theme\" default=\"Little Bear's first adventure in the forest\"}",
    "scene": "{argument name=\"scene\" default=\"forest path in the morning mist\"}",
    "moment": "{argument name=\"story moment\" default=\"Little Bear looks up and sees the first ray of sunlight through the leaves\"}"
  },
  "main_character": {
    "description": "{argument name=\"main character\" default=\"round little bear, carrying a small cloth bag\"}",
    "expression": "{argument name=\"expression\" default=\"curious + smiling\"}",
    "pose": "{argument name=\"pose\" default=\"looking up\"}"
  },
  "secondary_characters": {
    "items": [
      "{argument name=\"secondary 1\" default=\"a little bird flying by\"}",
      "{argument name=\"secondary 2\" default=\"a rabbit peeking out\"}"
    ]
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"watercolor picture book style + soft outlines\"}",
    "color_palette": "{argument name=\"color palette\" default=\"warm orange + soft green + cream white\"}",
    "rendering": "grainy paper texture + soft watercolor + simple lines"
  },
  "text_overlay": {
    "enabled": "{argument name=\"text enabled\" default=\"true\"}",
    "text": "{argument name=\"text\" default=\"Little Bear looked up, and the world suddenly felt very big.\"}",
    "position": "{argument name=\"text position\" default=\"bottom center of frame\"}",
    "font_style": "rounded handwriting font"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"4:3\"}",
  "constraints": {
    "must_keep": [
      "main character as visual center",
      "overall color palette warm and healing",
      "reasonable white space for text and image",
      "secondary characters do not upstage the main character"
    ],
    "avoid": [
      "adult-level complex expressions",
      "overly cold color tones",
      "overly realistic scene rendering",
      "brand logos appearing"
    ]
  }
}
```

### Parameter Strategy

- Must ask: main character, scene, text
- Can default: style, color scheme, font
- Can randomize: secondary character specifics

### Auto-Complete Strategy

- Main character chibi-cute priority (animals > children)
- Default style is watercolor picture book
- Text ≤ 25 characters
- Default aspect ratio 4:3 or 3:4

## Variant 1: Holiday Card

📝 Prompt

```json
{
  "type": "Holiday Children's Card",
  "story": {
    "theme": "{argument name=\"festival\" default=\"Christmas\"}",
    "scene": "snowy night cabin"
  },
  "main_character": {
    "description": "little fox wearing a red hat"
  },
  "text_overlay": {
    "text": "Merry Christmas",
    "position": "top"
  },
  "constraints": {
    "must_feel": "holiday atmosphere, warm, shareable"
  }
}
```

## Variant 2: Educational Illustration

📝 Prompt

```json
{
  "type": "Children's Educational Illustration",
  "story": {
    "theme": "{argument name=\"concept\" default=\"correct brushing order\"}",
    "scene": "bathroom"
  },
  "main_character": {
    "description": "child holding a toothbrush"
  },
  "text_overlay": {
    "enabled": true,
    "text": "1. Rinse → 2. Upper teeth → 3. Lower teeth → 4. Rinse"
  },
  "constraints": {
    "must_feel": "easy to understand, educational, friendly"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Picture Book Illustration Auto-Complete Template",
  "mode": "auto-fill",
  "rule": "User provides a theme, auto-decide main character, scene, style, text",
  "constraints": {
    "must_feel": "printable as a picture book"
  }
}
```

## Things to Avoid

- Do not make character facial features realistic
- Do not make scenes too dark
- Do not let text exceed 25 characters
- Do not use > 3 font types
- Do not include concepts only adults would understand