# Web Banner / Hero Template

This file is used to generate "website top hero area / app banner / ad creative" visuals:

- Website homepage hero
- Landing page banner
- App top campaign banner
- Email marketing banner
- Feed ad creative

Features:

- Horizontal ratio (16:9 / 21:9 / 3:1)
- One strong claim
- CTA area reserved
- Safe whitespace (avoid cropping key elements)

## Scope

- Web hero
- Landing page hero
- App banner
- Email banner
- Ad creative

## When to Use

- User mentions "banner / hero / landing page main image / top image"
- User needs horizontal composition + CTA area

Do NOT use:

- Portrait / square main poster (use `brand-poster.md`)
- Series KV (use `campaign-kv.md`)
- Magazine cover (use `editorial-cover.md`)

## Missing Information Priority Questions

1. Use case (web hero / app banner / email)
2. Theme / claim
3. Main visual
4. CTA copy + color
5. Brand color
6. Aspect ratio

## Main Template: Web Hero Banner

📖 Description

Overall horizontal composition, left side with title + subtitle + CTA, right side with main visual, bottom safe whitespace.

📝 Prompt

```json
{
  "type": "Web hero banner",
  "goal": "Generate a horizontal banner directly usable as a product website / marketing landing page hero area main image",
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"16:9\"}",
  "layout": {
    "left_column": {
      "headline": "{argument name=\"headline\" default=\"Redefine Your Work Rhythm\"}",
      "subhead": "{argument name=\"subhead\" default=\"AURORA Pro · Let AI Handle 80% of the Grind\"}",
      "cta": {
        "text": "{argument name=\"cta text\" default=\"Free Trial\"}",
        "color": "{argument name=\"cta color\" default=\"Brand primary color\"}",
        "secondary": "{argument name=\"secondary cta\" default=\"Learn More\"}"
      }
    },
    "right_column": {
      "centerpiece": "{argument name=\"hero visual\" default=\"Product screenshot + slight 3D perspective + highlight\"}",
      "scale": "{argument name=\"hero scale\" default=\"Occupying 80% of right side\"}"
    }
  },
  "background": {
    "type": "{argument name=\"background type\" default=\"Light gradient\"}",
    "decoration": "{argument name=\"decoration\" default=\"Subtle noise + faint geometric shapes\"}"
  },
  "brand": {
    "logo_position": "Top left corner",
    "navigation_hint": "{argument name=\"nav hint\" default=\"Top navigation bar already exists, banner should not draw it\"}"
  },
  "safe_area": {
    "rule": "Bottom 10% + right 5% whitespace, avoid cropping",
    "mobile_consideration": "{argument name=\"mobile aware\" default=\"true\"}"
  },
  "constraints": {
    "must_keep": [
      "Headline is the largest font size",
      "CTA must look clickable (clear button shape)",
      "Main visual on right side not exceeding safe area",
      "Color palette strictly unified"
    ],
    "avoid": [
      "Headline overlapping main visual",
      "CTA color contrast too low against background",
      "Information density too high",
      "Main visual spanning entire frame with no space for claim"
    ]
  }
}
```

### Parameter Strategy

- Required: headline, CTA, main visual, aspect ratio
- Defaultable: background, subtitle, safe area
- Random: decorative geometric shapes

### Auto-fill Strategy

- When user provides product name: auto-generate 1 headline + 1 subtitle + 1 CTA
- CTA defaults to brand primary color button + gray secondary button
- Main visual auto-selected by industry (SaaS = screenshot, consumer = product, service = person)

## Variant 1: Full-Image Background + Floating Copy Layer

📝 Prompt

```json
{
  "type": "Full-screen background hero",
  "background": {
    "type": "Full-image background",
    "description": "{argument name=\"background image\" default=\"Morning workspace, soft light\"}"
  },
  "layout": {
    "left_column": {
      "headline": "{argument name=\"headline\" default=\"AI Gives You 30 Extra Minutes Every Morning\"}",
      "cta": "Try Now"
    }
  },
  "constraints": {
    "must_feel": "Atmospheric, lifestyle, brand spirit"
  }
}
```

## Variant 2: Long Horizontal Strip Banner (21:9 / 3:1)

📝 Prompt

```json
{
  "type": "Ultra-wide strip banner",
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"21:9\"}",
  "layout": {
    "left_column": { "headline": "20% Off for 7 Days Only" },
    "right_column": { "centerpiece": "Countdown number + product thumbnail" }
  },
  "constraints": {
    "must_feel": "Promotional, urgency, strong CTA"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Banner / hero auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides product + theme + aspect ratio, auto-generate headline / CTA / main visual / safe area",
  "constraints": {
    "must_feel": "Ready to go live on web / app"
  }
}
```

## Things to Avoid

- Do NOT let the headline and main visual obscure each other
- Do NOT let CTA color contrast be below 4.5:1 against the background
- Do NOT pack more than 3 lines of body text on a banner
- Do NOT ignore safe whitespace (mobile cropping will cause problems)
- Do NOT turn a horizontal banner composition into a pure image (must have a claim)