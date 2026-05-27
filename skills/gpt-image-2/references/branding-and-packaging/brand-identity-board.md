# Brand Identity System Board Template

This file is used for "one image showing a complete brand identity system" visuals:

- Brand logo + fonts + colors + application scenarios
- VI summary single page
- Brand proposal board
- Brand guideline cover
- Designer case study single page

Characteristics:

- One large image divided into multiple sections
- Logo applications + color palette + font specifications + physical mockups
- Emphasis on "system feel + professionalism"
- Usually with grid + labels
- Calm, not overly decorated

## Scope

- Brand identity system board (VI summary)
- Brand proposal board
- Designer portfolio single page

## When to use

- User mentions "VI / brand identity / brand system / brand board / brand guideline cover"
- User wants one image showing the full brand set

Do NOT use for:

- Mascot brand kit → use `mascot-brand-kit.md`
- Single poster → use `poster-and-campaigns/brand-poster.md`
- Packaging mockup single image → use `cosmetic-packaging.md`

## Missing Information Priority Question Order

1. Brand name + one-line positioning
2. Industry / audience
3. Logo main form (wordmark / graphic / combination)
4. Primary color 1-2
5. Font preference (serif / sans-serif / handwritten)
6. Whether packaging / business card / poster mockups needed

## Main Template: Brand Identity System Board

Description

One large image, divided into logo area + color area + typography area + application mockup area.

Prompt

```json
{
  "type": "brand identity system board",
  "goal": "Generate a brand identity single page usable as VI summary / brand board",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"AURORA\"}",
    "tagline": "{argument name=\"tagline\" default=\"Light makes life soft\"}",
    "industry": "{argument name=\"industry\" default=\"home lighting\"}",
    "personality": "{argument name=\"personality\" default=\"gentle, modern, restrained\"}"
  },
  "regions": {
    "logo": {
      "position": "{argument name=\"logo position\" default=\"upper left large area\"}",
      "primary_logo": "{argument name=\"primary logo\" default=\"AURORA wordmark + circular halo graphic\"}",
      "secondary_logos": ["black and white single color version", "graphic version (no text)", "vertical layout version"],
      "background_test": "dark background / light background each shown once"
    },
    "color_palette": {
      "position": "{argument name=\"color position\" default=\"upper right\"}",
      "primary": [
        "{argument name=\"primary color 1\" default=\"#0F4C81 navy blue\"}",
        "{argument name=\"primary color 2\" default=\"#FFD166 warm gold\"}"
      ],
      "secondary": [
        "{argument name=\"secondary color 1\" default=\"#F4F1EA off-white\"}",
        "{argument name=\"secondary color 2\" default=\"#222 dark gray\"}"
      ],
      "swatch_design": "color block + HEX + Chinese name"
    },
    "typography": {
      "position": "{argument name=\"type position\" default=\"lower left\"}",
      "headline_font": "{argument name=\"headline font\" default=\"modern serif (e.g. Playfair Display)\"}",
      "body_font": "{argument name=\"body font\" default=\"Chinese rounded sans + English sans\"}",
      "demo_block": "Aa Bb Cc 1234 + one Chinese line + one English line"
    },
    "applications": {
      "position": "{argument name=\"app position\" default=\"lower right\"}",
      "mockups": [
        "{argument name=\"mockup 1\" default=\"business card front and back\"}",
        "{argument name=\"mockup 2\" default=\"product packaging box\"}",
        "{argument name=\"mockup 3\" default=\"app icon + splash screen\"}"
      ]
    }
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"modern minimalist brand board, beige background + subtle paper texture\"}",
    "grid": "thin gray guide lines"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "4 section boundaries clear",
      "Logo area always in leading position",
      "Color palette ≤ 6 colors + HEX readable",
      "Application mockup styles unified"
    ],
    "avoid": [
      "Too many elements leaving no breathing room per section",
      "More than 2 font families",
      "More than 6 colors",
      "Missing HEX codes"
    ]
  }
}
```

### Parameter Strategy

- Must ask: brand name, industry, primary colors, positioning
- Can default: layout, font recommendations, application mockups
- Can randomize: mockup physical details

### Auto-Fill Strategy

- User gives brand name + industry + one personality keyword → auto-expand logo + colors + fonts + 3 mockups
- Default "modern minimalist" style
- Default portrait 3:4

## Variant 1: Ultra-Minimal Brand Board (Logo + Colors Only)

Prompt

```json
{
  "type": "minimal brand board",
  "regions": {
    "logo": {"primary_logo": "wordmark + minimal graphic", "background_test": "white + pure black backgrounds"},
    "color_palette": {"primary": ["#000", "#FFF", "#FFD166"]},
    "typography": {"demo_block": "Aa Bb"},
    "applications": null
  },
  "constraints": {
    "must_feel": "Swiss graphic / Japanese minimal"
  }
}
```

## Variant 2: High-Density Brand Board (with tone of voice, icon system)

Prompt

```json
{
  "type": "high-density brand board",
  "regions": {
    "logo": {"primary_logo": "..."},
    "color_palette": {"primary": ["..."], "secondary": ["..."]},
    "typography": {"demo_block": "..."},
    "applications": {"mockups": ["business card", "packaging", "poster", "app icon", "website hero"]}
  },
  "extras": {
    "icon_system": "12 unified style icon grid",
    "tone_of_voice": "3 brand voice example sentences"
  },
  "constraints": {
    "must_feel": "complete printable brand book cover"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "Brand board auto-fill",
  "mode": "auto-fill",
  "rule": "User gives brand name + industry + one personality description, auto-decide logo / colors / fonts / application mockups",
  "constraints": {
    "must_feel": "usable as client proposal cover page"
  }
}
```

## Things to Avoid

- Do not let the logo area be squeezed to an inconspicuous position
- Do not let colors exceed 6
- Do not let fonts exceed 2 families
- Do not let mockups be so flashy they undermine professionalism
- Do not omit HEX annotations
- Do not let the background have strong textures
