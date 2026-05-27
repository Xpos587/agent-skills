# Mascot Brand Kit Template

This file is used for "multi-panel brand identity / merchandise visual document centered on a mascot":

- Mascot multi-angle + expressions + application scenarios
- Mascot merchandise catalog
- Brand IP complete introduction page
- Cartoon persona brand identity document

Characteristics:

- One large image, multiple sections
- Main section: mascot three-view + hero image
- Secondary sections: expressions + colors + merchandise
- Style emphasizes "friendly + cute + consistent"
- Usually includes IP name + personality description

## Scope

- Mascot brand identity kit
- IP merchandise catalog
- Cartoon persona introduction page
- Marketing campaign IP package

## When to use

- User mentions "mascot / mascot / IP character / cartoon spokesperson"
- User wants "complete IP kit" rather than a single image

Do NOT use for:

- Single character design sheet → use `portraits-and-characters/character-sheet.md`
- General brand identity → use `brand-identity-board.md`
- Single anime KV → use `storyboards-and-sequences/anime-key-visual.md`

## Missing Information Priority Question Order

1. Brand / IP name + one-line personality description
2. Mascot main form (animal / human / anthropomorphic / food)
3. Colors 1-2
4. Whether expression pack / merchandise / costumes needed
5. Render style (2D cartoon / 3D chibi / Pixar realistic cartoon)
6. Aspect ratio

## Main Template: Mascot Brand Identity Kit

Description

One large image, divided into hero image section + three-view section + expression section + application section.

Prompt

```json
{
  "type": "mascot brand identity kit",
  "goal": "Generate a multi-panel visual document usable as a mascot brand kit / merchandise introduction page",
  "ip": {
    "name": "{argument name=\"ip name\" default=\"AURORA Little Light\"}",
    "tagline": "{argument name=\"tagline\" default=\"accompanying you through every night\"}",
    "personality": "{argument name=\"personality\" default=\"gentle, curious, loves to glow\"}",
    "brand_owner": "{argument name=\"brand owner\" default=\"AURORA home lighting\"}"
  },
  "mascot": {
    "form": "{argument name=\"mascot form\" default=\"small semi-transparent lightbulb sprite, round and chubby, with a glowing tail\"}",
    "color_palette": "{argument name=\"color palette\" default=\"warm gold + off-white + light blue\"}",
    "rendering": "{argument name=\"rendering\" default=\"3D Pixar style + chibi\"}"
  },
  "regions": {
    "hero": {
      "position": "{argument name=\"hero position\" default=\"upper left large area\"}",
      "content": "mascot hero image + name + one-line personality description",
      "background": "solid color + soft glow"
    },
    "three_view": {
      "position": "{argument name=\"three view position\" default=\"upper right\"}",
      "content": "front / side / back three-view",
      "label": "FRONT / SIDE / BACK"
    },
    "expressions": {
      "position": "{argument name=\"expression position\" default=\"lower left\"}",
      "count": "{argument name=\"expression count\" default=\"6\"}",
      "items": ["happy", "curious", "sleepy", "surprised", "shy", "slightly angry"]
    },
    "applications": {
      "position": "{argument name=\"app position\" default=\"lower right\"}",
      "items": [
        "{argument name=\"app 1\" default=\"product packaging box corner\"}",
        "{argument name=\"app 2\" default=\"app splash screen\"}",
        "{argument name=\"app 3\" default=\"merchandise stickers\"}",
        "{argument name=\"app 4\" default=\"short video intro mascot animation still frame\"}"
      ]
    }
  },
  "style": {
    "background": "{argument name=\"background\" default=\"beige paper texture + thin gray guide lines\"}",
    "typography": "rounded sans + one handwritten accent line"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "Mascot appearance consistent across all sections",
      "Three-view proportions strictly unified",
      "Expressions clearly identifiable",
      "Application scenarios match the brand"
    ],
    "avoid": [
      "Mascot art style drifting across sections",
      "Expressions exaggerated to the point of distortion",
      "Colors with strong contrast undermining IP tone",
      "Application mockup style conflicts"
    ]
  }
}
```

### Parameter Strategy

- Must ask: IP name, form, personality, main color
- Can default: layout, expressions, application scenarios
- Can randomize: merchandise details

### Auto-Fill Strategy

- User gives one line "I want a cute spokesperson for X industry" → auto-decide form + personality + colors + 6 expressions + 4 applications
- Default 3D chibi rendering
- Default 4-section layout

## Variant 1: Mascot Merchandise Catalog (Focus on Products)

Prompt

```json
{
  "type": "mascot merchandise catalog",
  "regions": {
    "hero": {"content": "mascot + IP name"},
    "three_view": null,
    "expressions": null,
    "applications": {
      "items": [
        "T-shirt", "mug", "phone case", "sticker pack", "keychain", "plush toy", "tote bag", "phone stand"
      ]
    }
  },
  "constraints": {
    "must_feel": "e-commerce product catalog feel"
  }
}
```

## Variant 2: Minimal Mascot Introduction Page (Hero + Personality Only)

Prompt

```json
{
  "type": "minimal mascot introduction page",
  "regions": {
    "hero": {"content": "mascot + name + personality"},
    "three_view": null,
    "expressions": {"count": 4},
    "applications": null
  },
  "constraints": {
    "must_feel": "clean, easy to read"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "Mascot brand kit auto-fill",
  "mode": "auto-fill",
  "rule": "User gives brand + industry + personality keywords, auto-decide mascot form + expressions + applications",
  "constraints": {
    "must_feel": "publishable as merchandise / PR image"
  }
}
```

## Things to Avoid

- Do not let the mascot have inconsistent proportions across sections
- Do not let expressions be so exaggerated they look like a different character
- Do not add too many other design elements on application mockups
- Do not let colors exceed 4 main colors
- Do not omit IP name + personality description
