# 4-Panel Comic Template

This file is used for "4-panel comic / satirical comic / gag comic" visuals:

- Reversal 4-panel gags
- Satirical product ad comics
- Short story 4-panels
- Social media 4-panel comics
- Food / mood 4-panels

Features:

- 4 equal-sized panels (2×2 or 1×4)
- Each panel is an independent scene but the story is connected
- Setup / development / twist / punchline rhythm
- Usually includes dialogue bubbles / inner thoughts
- Unified style

## Scope

- Social media 4-panel comics
- Satirical ad 4-panels
- Reversal gags
- Mood diary comics

## When to Use

- User mentions "4-panel / four-panel comic / gag comic / satirical comic"
- User wants to tell a short story with rhythm
- User wants a reversal / punchline

Do NOT use for:

- Multi-panel spread manga (use `manga-spread-page.md`)
- Non-narrative icon collages (use `grids-and-collages/banner-grid-2x2.md`)
- Single image KV (use `anime-key-visual.md`)

## Missing Information Priority Question Order

1. Theme / story core
2. Main character description
3. What each of the 4 panels depicts (setup, development, twist, punchline)
4. Style (hand-drawn Japanese manga / minimalist lineart / American cartoon / Chinese manhua)
5. Whether there are dialogue bubbles
6. Aspect ratio (1:1 / 4:3 / 9:16)

## Main Template: 2×2 Reversal 4-Panel Comic

📖 Description

Overall a single image, divided into 2×2 four panels, telling a short story with rhythm and a reversal following setup / development / twist / punchline.

📝 Prompt

```json
{
  "type": "2x2 Reversal 4-Panel Comic",
  "goal": "Generate a 2×2 four-panel comic telling a short story with rhythm and a reversal",
  "story": {
    "theme": "{argument name=\"theme\" default=\"person on a diet and midnight fried chicken\"}",
    "structure": "setup / development / twist / punchline",
    "main_character": "{argument name=\"main character\" default=\"short-haired girl, wearing pajamas\"}"
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"Japanese manga lineart + flat light coloring\"}",
    "consistency": "main character across 4 panels must be the same person, art style unified",
    "color_palette": "{argument name=\"color palette\" default=\"cream white + warm orange + gray\"}"
  },
  "panels": {
    "format": "2x2 grid",
    "items": [
      {
        "position": "top-left",
        "label": "Setup",
        "scene": "{argument name=\"panel 1\" default=\"main character standing on a scale, frowning\"}",
        "dialogue": "{argument name=\"dialogue 1\" default=\"Starting my diet tonight!\"}"
      },
      {
        "position": "top-right",
        "label": "Development",
        "scene": "{argument name=\"panel 2\" default=\"main character firmly drinking a glass of water\"}",
        "dialogue": "{argument name=\"dialogue 2\" default=\"Water is pretty filling\"}"
      },
      {
        "position": "bottom-left",
        "label": "Twist",
        "scene": "{argument name=\"panel 3\" default=\"late at night, main character secretly opening a food delivery app\"}",
        "dialogue": "{argument name=\"dialogue 3\" default=\"...just one order of fried chicken\"}"
      },
      {
        "position": "bottom-right",
        "label": "Punchline",
        "scene": "{argument name=\"panel 4\" default=\"main character hugging a bucket of fried chicken, teary-eyed\"}",
        "dialogue": "{argument name=\"dialogue 4\" default=\"Starting tomorrow\"}"
      }
    ]
  },
  "dialogue_design": {
    "balloon_style": "{argument name=\"balloon style\" default=\"white rounded bubbles, black outline\"}",
    "font_style": "{argument name=\"font style\" default=\"rounded handwriting font\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"1:1\"}",
  "constraints": {
    "must_keep": [
      "same main character across 4 panels",
      "story rhythm clear (setup / development / twist / punchline)",
      "dialogue bubbles not covering faces",
      "art style unified, no drift"
    ],
    "avoid": [
      "story going flat with no reversal",
      "dialogue exceeding 12 characters",
      "panel sizes inconsistent",
      "multiple font types"
    ]
  }
}
```

### Parameter Strategy

- Must ask: theme, main character, 4-panel plot
- Can default: style, color scheme, bubble style
- Can randomize: specific dialogue wording

### Auto-Complete Strategy

- When user only provides a theme: auto-expand setup-development-twist-punchline 4-panel plot + 4 lines of dialogue
- Default main character auto-selected to fit the theme
- Default 2×2

## Variant 1: Satirical Product Ad 4-Panel

📝 Prompt

```json
{
  "type": "Satirical Product Ad 4-Panel",
  "story": {
    "theme": "{argument name=\"product satire theme\" default=\"Tech company PPT vs actual product\"}"
  },
  "panels": {
    "format": "2x2 grid",
    "items": [
      {"label": "How it looks on the PPT", "scene": "futuristic product + user mesmerized"},
      {"label": "Launch demo", "scene": "engineer's hands shaking"},
      {"label": "Actual delivery", "scene": "product box with only a charger inside"},
      {"label": "Customer service reply", "scene": "'Will be in the next version'"}
    ]
  },
  "constraints": {
    "must_feel": "satirical + gag + instantly understandable"
  }
}
```

## Variant 2: 1×4 Horizontal Strip (Suitable for Twitter / X Long Posts)

📝 Prompt

```json
{
  "type": "1x4 Horizontal Strip Comic",
  "panels": {
    "format": "1x4 horizontal strip",
    "items": [
      {"label": "1", "scene": "..."},
      {"label": "2", "scene": "..."},
      {"label": "3", "scene": "..."},
      {"label": "4", "scene": "..."}
    ]
  },
  "aspect_ratio": "16:9",
  "constraints": {
    "must_feel": "horizontal reading, 4 panels forming one continuous action"
  }
}
```

## Variant 3: Food / Mood Diary 4-Panel

📝 Prompt

```json
{
  "type": "Mood 4-Panel Diary Comic",
  "story": {
    "theme": "{argument name=\"daily theme\" default=\"Monday morning me\"}"
  },
  "style": {
    "art_style": "minimalist lineart + minimal color blocks"
  },
  "constraints": {
    "must_feel": "relatable, everyday, resonant"
  }
}
```

## Variant 4: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "4-Panel Comic Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides theme, auto-expand setup-development-twist-punchline 4 panels + main character + dialogue",
  "constraints": {
    "must_feel": "ready to post on social media"
  }
}
```

## Things to Avoid

- Do not have 4 panels without reversal / without rhythm
- Do not let dialogue exceed 12 characters per panel
- Do not let art style drift per panel
- Do not make 4 panels unequal in size (unless deliberately designed)
- Do not let bubbles cover faces