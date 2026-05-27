# Minimalist Mood Illustration Template

This file is used to generate "minimalist white space / strong mood" illustrations:

- Minimalist posters
- Literary mood images
- Brand mood images
- Article footer images
- Desktop / phone wallpapers

Features:

- Large white space
- Single subject or minimal elements
- One dominant color
- Strong mood / strong character
- Text (if any) is minimal

## Scope

- Literary mood images
- Minimalist posters
- Brand mood images
- Wallpaper / footer images

## When to Use

- User mentions "minimalist / white space / mood / a feeling / literary style"
- User wants visuals where "mood comes first", no narrative needed

Do NOT use for:

- Healing everyday scenes (use `healing-scene.md`)
- Concept epic scenes (use `concept-scene.md`)
- Picture book illustrations (use `picture-book-scene.md`)

## Missing Information Priority Question Order

1. A mood / a sentence
2. Subject (a person / a bird / a tree / abstract shape)
3. Dominant color
4. Whether text is needed
5. Aspect ratio

## Main Template: Minimalist White Space Mood Image

📖 Description

Overall large white space, small and offset subject, unified color tone, text (if any) only 1 sentence.

📝 Prompt

```json
{
  "type": "Minimalist White Space Mood Image",
  "goal": "Generate a minimalist illustration where mood comes first and white space is maximized",
  "mood": {
    "feeling": "{argument name=\"feeling\" default=\"quiet, solitude, late autumn\"}",
    "one_sentence": "{argument name=\"one sentence\" default=\"The wind stopped, and I finally paused for a moment.\"}"
  },
  "subject": {
    "description": "{argument name=\"main subject\" default=\"a solitary small tree in the distance\"}",
    "scale": "{argument name=\"subject scale\" default=\"occupies 10% of frame\"}",
    "position": "{argument name=\"subject position\" default=\"bottom right of frame\"}"
  },
  "background": {
    "type": "{argument name=\"background\" default=\"cream white mist + subtle paper texture\"}",
    "main_color": "{argument name=\"main color\" default=\"cream white + a touch of warm gray\"}"
  },
  "text_overlay": {
    "enabled": "{argument name=\"text enabled\" default=\"true\"}",
    "text": "{argument name=\"text\" default=\"The wind stopped, and I finally paused for a moment.\"}",
    "position": "{argument name=\"text position\" default=\"upper left of frame\"}",
    "font_style": "{argument name=\"font style\" default=\"thin serif\"}",
    "color": "dark gray"
  },
  "style": {
    "rendering": "minimalist illustration + subtle paper texture + soft grain",
    "lighting": "overall soft light, almost no dramatic lighting",
    "color_palette": "≤ 2 main colors"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "white space ≥ 70% of frame",
      "subject small but indispensable",
      "color tone strictly unified",
      "mood conveyed through color + white space, not decoration"
    ],
    "avoid": [
      "secondary elements stacking up",
      "more than 2 colors",
      "text longer than 1 sentence",
      "brand logos appearing"
    ]
  }
}
```

### Parameter Strategy

- Must ask: mood, subject
- Can default: background, color scheme, font
- Can randomize: small subject details

### Auto-Complete Strategy

- Mood → color scheme (solitude = cream white; night = deep blue; autumn = warm brown; spring = cherry pink)
- Subject auto-selected by mood (loneliness = a tree / a bird; calm = an ocean; longing = a receding silhouette)
- Text ≤ 18 characters

## Variant 1: Solid Color Minimalist Poster

📝 Prompt

```json
{
  "type": "Solid Color Minimalist Poster",
  "subject": {
    "description": "{argument name=\"subject\" default=\"a flying bird silhouette\"}",
    "scale": "5%"
  },
  "background": {
    "type": "solid color",
    "main_color": "{argument name=\"main color\" default=\"deep blue\"}"
  },
  "text_overlay": {
    "text": "{argument name=\"text\" default=\"freedom\"}",
    "font_style": "ultra-bold sans-serif"
  },
  "constraints": {
    "must_feel": "strong single statement, restrained, conceptual"
  }
}
```

## Variant 2: Abstract Shape Mood

📝 Prompt

```json
{
  "type": "Abstract Shape Mood Image",
  "subject": {
    "description": "{argument name=\"abstract\" default=\"two tangent circles\"}",
    "scale": "30%"
  },
  "constraints": {
    "must_feel": "conceptual, design-oriented, brand asset"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Minimalist Mood Image Auto-Complete Template",
  "mode": "auto-fill",
  "rule": "User provides a mood sentence or a single word, auto-decide subject, color scheme, text, aspect ratio",
  "constraints": {
    "must_feel": "can serve as wallpaper / footer image"
  }
}
```

## Things to Avoid

- Do not fill the frame
- Do not use > 2 main colors
- Do not let text exceed 18 characters
- Do not center the subject (minimalist usually uses offset placement)
- Do not use ornate fonts