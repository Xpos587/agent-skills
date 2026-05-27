# Manga Spread / Multi-Panel Page Template

This file is used for "multiple irregular panel narrative within a single page" manga visuals:

- Single page 5-7 panel manga
- Two-page spread (left and right pages connected)
- Psychological / suspense / combat / daily multi-panel
- Doujinshi manga / commercial manga
- Storyboard

Features:

- Irregular panels
- Large panel + small panel combinations
- Has reading order (usually top-right → bottom-left)
- Includes dialogue boxes + inner thoughts + narration
- Style more "comic book" than 4-panel gag

## Scope

- Single page multi-panel manga
- Two-page spreads
- Storyboards / layout drafts
- Doujinshi / commercial manga

## When to Use

- User mentions "manga panels / spread / multi-panel manga / storyboard"
- User wants more complex narrative, more dynamic rhythm
- User wants "comic book" quality

Do NOT use for:

- 4-panel gags (use `four-panel-comic.md`)
- Single image KV (use `anime-key-visual.md`)
- Character design sheets (use `portraits-and-characters/character-sheet.md`)

## Missing Information Priority Question Order

1. Story summary / what this page needs to tell
2. Panel count (5-9)
3. Main character description
4. Style: Japanese manga / Korean manhwa / American comics / doujinshi
5. Reading direction (Japanese right-to-left / American left-to-right)
6. Whether in color or pure black-and-white

## Main Template: Single Page Multi-Panel Manga

📖 Description

Overall one manga page, containing 5-7 irregular panels, unfolding a narrative following reading order.

📝 Prompt

```json
{
  "type": "Single Page Multi-Panel Manga",
  "goal": "Generate a complete single manga page with multiple panels, tight narrative rhythm",
  "story": {
    "summary": "{argument name=\"story summary\" default=\"protagonist receives a mysterious call, decides to go alone\"}",
    "main_character": "{argument name=\"main character\" default=\"young female detective, short hair, black trench coat\"}",
    "supporting": "{argument name=\"supporting\" default=\"none\"}"
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"Japanese black-and-white manga + screentone + strong shadows\"}",
    "tone": "{argument name=\"tone\" default=\"suspense + tension\"}",
    "color": "{argument name=\"color\" default=\"black-and-white + grayscale\"}"
  },
  "page_layout": {
    "panel_count": "{argument name=\"panel count\" default=\"6\"}",
    "reading_direction": "{argument name=\"reading direction\" default=\"Japanese: right to left, top to bottom\"}",
    "panels": [
      {
        "id": 1,
        "size": "large panel spanning upper half",
        "scene": "{argument name=\"panel 1\" default=\"protagonist side face close-up, phone to ear\"}",
        "text": "{argument name=\"text 1\" default=\"Narration: That call changed everything\"}"
      },
      {
        "id": 2,
        "size": "medium panel lower right",
        "scene": "{argument name=\"panel 2\" default=\"close-up of static from the phone receiver\"}",
        "text": "{argument name=\"text 2\" default=\"Caller: Tonight at ten, the usual place\"}"
      },
      {
        "id": 3,
        "size": "small panel lower left",
        "scene": "{argument name=\"panel 3\" default=\"protagonist eye close-up, pupils dilated\"}",
        "text": "{argument name=\"text 3\" default=\"Inner thought: It's him again\"}"
      },
      {
        "id": 4,
        "size": "medium panel right",
        "scene": "{argument name=\"panel 4\" default=\"protagonist putting on trench coat action panel\"}",
        "text": ""
      },
      {
        "id": 5,
        "size": "medium panel center",
        "scene": "{argument name=\"panel 5\" default=\"protagonist pushing open a door, rainy night street\"}",
        "text": ""
      },
      {
        "id": 6,
        "size": "large panel spanning lower half",
        "scene": "{argument name=\"panel 6\" default=\"protagonist's back receding, dim streetlights\"}",
        "text": "{argument name=\"text 6\" default=\"Narration: Is this keeping an appointment, or going to die\"}"
      }
    ]
  },
  "dialogue_design": {
    "balloon_style": "white background + black outline + pointed tail",
    "narration_box": "rectangle + gray background + black border",
    "thought_balloon": "cloud shape + dotted tail",
    "font_style": "sans-serif manga font"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "panel sizes have rhythm (large + small + large)",
      "reading order clear",
      "protagonist consistent across multiple panels",
      "dialogue boxes not blocking key character actions"
    ],
    "avoid": [
      "all panels the same size (monotonous rhythm)",
      "confusing reading order",
      "protagonist appearance drift",
      "sudden color shift (bright color suddenly appearing in black-and-white page)"
    ]
  }
}
```

### Parameter Strategy

- Must ask: story summary, panel count, main character
- Can default: style, reading direction, dialogue box style
- Can randomize: background details

### Auto-Complete Strategy

- When user only provides the story: auto-determine 5-7 panel rhythm
- Default Japanese black-and-white manga + screentone
- Default Japanese reading direction

## Variant 1: Two-Page Spread (Left and Right Pages)

📝 Prompt

```json
{
  "type": "Two-Page Spread Manga",
  "page_layout": {
    "panel_count": "8-12 (combined left and right pages)",
    "format": "horizontal spread, image divided into left and right pages"
  },
  "aspect_ratio": "16:11",
  "constraints": {
    "must_feel": "left and right pages connected, center gutter should not cut through key elements"
  }
}
```

## Variant 2: Color Commercial Manga Page

📝 Prompt

```json
{
  "type": "Color Commercial Manga Page",
  "style": {
    "color": "full color + flat fill + digital manga texture",
    "art_style": "American comics / Korean manhwa style"
  },
  "constraints": {
    "must_feel": "can serve as a commercial serialized manga page"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Manga Spread Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides a story segment, auto-split panels, layout, dialogue",
  "constraints": {
    "must_feel": "publisher editor can directly place into typesetting"
  }
}
```

## Things to Avoid

- Do not make all panels equal in size
- Do not make reading order hard to identify
- Do not let dialogue boxes cover faces / cover actions
- Do not suddenly introduce strong colors in a black-and-white manga page
- Do not let the protagonist look like different people across panels
- When doing spreads, do not place key elements exactly at the center binding line