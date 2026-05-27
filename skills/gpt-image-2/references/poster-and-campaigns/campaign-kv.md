# Campaign Key Visual Template

This file is used to generate "a campaign key visual set" emphasizing "extensible, reusable, serializable":

- Quarterly campaign key visual
- Festival / holiday campaign main image
- Cross-platform unified visual delivery
- Co-branded campaign main image

Features:

- Main visual emphasizes "extensibility" to banner / story / short video cover
- Composed of 1 anchor visual + 1 layout system
- Emphasizes campaign claim
- Color palette strictly unified

## Scope

- New campaign key visual system
- Festival / Double 11 / mega sale campaign
- Co-branded campaign

## When to Use

- User mentions "campaign / mega sale / quarterly event / KV / series key visual"
- User wants the visual to extend into banner / story / poster formats

Do NOT use:

- Single brand poster (use `brand-poster.md`)
- Web hero (use `banner-hero.md`)

## Missing Information Priority Questions

1. Campaign theme
2. Campaign time window
3. Campaign claim (slogan / proposition line)
4. Brand color + campaign-specific color
5. Main visual center (person / product / conceptual graphic)
6. Whether derivative layouts need to be shown

## Main Template: Campaign Key Visual + Derivatives

📖 Description

Main image is the anchor visual, with campaign claim at the center, and derivative layouts (1:1, 9:16, 16:9) shown as small previews below.

📝 Prompt

```json
{
  "type": "Campaign Key Visual system",
  "goal": "Generate a visual system image that serves as the campaign main image and displays its derivative versions",
  "campaign": {
    "name": "{argument name=\"campaign name\" default=\"AURORA Spring Drop 2026\"}",
    "claim": "{argument name=\"campaign claim\" default=\"New Sounds of Spring, Hear Every Heartbeat\"}",
    "duration": "{argument name=\"duration\" default=\"2026.4.20 - 2026.5.15\"}"
  },
  "visual_system": {
    "color_palette": "{argument name=\"color palette\" default=\"Cherry pink + misty blue + off-white\"}",
    "anchor_visual": {
      "description": "{argument name=\"anchor visual\" default=\"Young woman wearing new wireless earbuds, background of falling cherry blossom petals\"}",
      "composition": "Person at left 1/3 of frame, enough whitespace for claim"
    },
    "graphic_motif": "{argument name=\"motif\" default=\"Repeating small cherry blossom mark + dot rhythm accents\"}"
  },
  "claim_typography": {
    "font_style": "{argument name=\"font style\" default=\"Modern serif + smooth details\"}",
    "color": "Dark gray + cherry pink accent"
  },
  "derivative_layouts": {
    "enabled": "{argument name=\"derivatives enabled\" default=\"true\"}",
    "items": [
      "1:1 Social hero image",
      "9:16 Short video cover",
      "16:9 Banner"
    ],
    "rule": "Three derivative layouts displayed in a row below the main image"
  },
  "logo_placement": {
    "position": "Bottom right corner"
  },
  "constraints": {
    "must_keep": [
      "Anchor visual and derivative layouts maintain visual consistency",
      "Claim text readable at all aspect ratios",
      "Color palette strictly unified",
      "Brand logo appears in all versions"
    ],
    "avoid": [
      "Derivative layout style drift",
      "Claim unreadable at small sizes",
      "Extra colors appearing in palette",
      "Anchor visual subject extending beyond frame"
    ]
  }
}
```

### Parameter Strategy

- Required: campaign name, claim, color palette, anchor visual
- Defaultable: derivative layout list, logo position, typography
- Random: motif decoration specific forms

### Auto-fill Strategy

- User provides theme + occasion (spring / summer / Double 11 / Christmas) → auto-select color palette and motif
- Claim defaults to 12-18 characters
- Derivative layouts default to 3 aspect ratios

## Variant 1: Co-branded Campaign

📝 Prompt

```json
{
  "type": "Co-branded campaign key visual",
  "campaign": {
    "name": "{argument name=\"co-brand campaign\" default=\"AURORA × MUJI Limited\"}",
    "claim": "{argument name=\"claim\" default=\"Sounds of Everyday, Quiet Power\"}"
  },
  "visual_system": {
    "color_palette": "Gray-white + warm beige + touch of brand color",
    "anchor_visual": {
      "description": "Both brands' products side by side + everyday scene"
    }
  },
  "constraints": {
    "must_feel": "Restrained, shared context, neither brand overpowering the other"
  }
}
```

## Variant 2: Pure Graphic Campaign

📝 Prompt

```json
{
  "type": "Pure graphic campaign key visual",
  "visual_system": {
    "anchor_visual": {
      "description": "{argument name=\"motif\" default=\"Geometric shape evolved from brand logotype\"}"
    },
    "graphic_motif": "{argument name=\"pattern\" default=\"Repeating grid + rhythm dots\"}"
  },
  "constraints": {
    "must_feel": "Strong concept, abstract, belonging to brand assets"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Campaign KV auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides campaign theme + timing, auto-decide claim, color palette, anchor, derivatives",
  "constraints": {
    "must_feel": "Ready to enter the media delivery system"
  }
}
```

## Things to Avoid

- Do NOT let derivative layouts diverge in style from the main image
- Do NOT let the claim overlap the main subject (whitespace must be preserved)
- Do NOT use more than 2 font families in one KV system
- Do NOT make all aspect ratios the same composition (each must be genuinely re-composed)
- Do NOT let the motif overpower the main subject
