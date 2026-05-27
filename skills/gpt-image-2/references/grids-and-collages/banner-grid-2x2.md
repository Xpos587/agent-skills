# 2x2 Marketing Banner Grid Template

This file is used for "4 independent banners in one image, unified series design" visuals:

- Online education course series banners
- Training / enrollment banners
- Brand campaign multi-scene banners
- SNS / Moments ad set of four

Characteristics:

- 2x2 equal-size grid
- Each cell is an independent banner (with main title + visual + CTA)
- 4 banners share unified style but different content
- Each banner can be individually cropped for publishing

## Scope

- Education / training banner series
- Brand SNS ad sets
- Campaign multi-scene ads
- A/B test candidate drafts

## When to use

- User mentions "banner series / course banners / 4 ad pieces"
- User wants 4 banners with consistent style at once
- User needs SNS ad placement materials

Do NOT use for:

- One complete large banner → use `poster-and-campaigns/banner-hero.md`
- Multi-panel narrative → use `storyboards-and-sequences/four-panel-comic.md`
- Avatar grid → use `avatars-and-profile/character-grid-portrait.md`

## Missing Information Priority Question Order

1. Theme / business (education / e-commerce / brand campaign)
2. What each of the 4 banners promotes
3. Core character / prop for each banner
4. Brand colors / brand fonts
5. Whether logo / CTA needed
6. Aspect ratio (1:1 / 4:5 / 16:9 within each banner)

## Main Template: 2x2 Course / Education Banner Set

Description

One image with 2x2 independent banners, each promoting one course, sharing brand colors and logo area.

Prompt

```json
{
  "type": "2x2 course banner set",
  "goal": "Generate a set of 4 consistent-style course banners, individually croppable for SNS / public account header placement",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"Star Sea Academy\"}",
    "logo_position": "{argument name=\"logo position\" default=\"top-left corner of each banner\"}",
    "primary_color": "{argument name=\"primary color\" default=\"#FF6B35\"}",
    "secondary_color": "{argument name=\"secondary color\" default=\"#0F4C81\"}"
  },
  "layout": {
    "format": "2x2 grid",
    "panel_count": 4,
    "gap": "16px white divider",
    "panel_aspect_ratio": "{argument name=\"panel aspect\" default=\"4:5\"}",
    "overall_aspect_ratio": "1:1"
  },
  "panels": [
    {
      "position": "top-left",
      "course": "{argument name=\"course 1\" default=\"Kids Coding\"}",
      "headline": "{argument name=\"headline 1\" default=\"Scratch for 6-year-olds\"}",
      "visual": "{argument name=\"visual 1\" default=\"cartoon boy typing on keyboard at screen\"}",
      "cta": "{argument name=\"cta 1\" default=\"Try a Free Class\"}"
    },
    {
      "position": "top-right",
      "course": "{argument name=\"course 2\" default=\"Kids English\"}",
      "headline": "{argument name=\"headline 2\" default=\"Natural conversations with native teachers\"}",
      "visual": "{argument name=\"visual 2\" default=\"cartoon girl wearing headset speaking English\"}",
      "cta": "{argument name=\"cta 2\" default=\"Get a Trial Lesson\"}"
    },
    {
      "position": "bottom-left",
      "course": "{argument name=\"course 3\" default=\"Kids Math\"}",
      "headline": "{argument name=\"headline 3\" default=\"Thinking skills 1-on-1\"}",
      "visual": "{argument name=\"visual 3\" default=\"cartoon child working on whiteboard\"}",
      "cta": "{argument name=\"cta 3\" default=\"Get an Assessment\"}"
    },
    {
      "position": "bottom-right",
      "course": "{argument name=\"course 4\" default=\"Kids Art\"}",
      "headline": "{argument name=\"headline 4\" default=\"One artwork per week\"}",
      "visual": "{argument name=\"visual 4\" default=\"cartoon child painting\"}",
      "cta": "{argument name=\"cta 4\" default=\"Sign Up Online\"}"
    }
  ],
  "style": {
    "art_style": "{argument name=\"art style\" default=\"flat cartoon + rounded\"}",
    "typography": "Chinese rounded sans + English sans"
  },
  "constraints": {
    "must_keep": [
      "4 banners share the same brand colors and logo style",
      "Each banner works on its own",
      "Title ≤ 12 characters / line",
      "CTA button position consistent"
    ],
    "avoid": [
      "4 banners with style drift",
      "Headline font size varying too much",
      "CTA wording inconsistent",
      "Visual elements overstuffed"
    ]
  }
}
```

### Parameter Strategy

- Must ask: brand name, 4 promotional items
- Can default: brand colors, style, layout
- Can randomize: specific visual per banner

### Auto-Fill Strategy

- User gives brand + 4 products → auto-expand 4 headlines + visuals + CTAs
- Default 2x2 + 16px white dividers
- CTA wording auto-selected based on business type

## Variant 1: E-Commerce Product Banner Set

Prompt

```json
{
  "type": "e-commerce product banner set",
  "panels": [
    {"course": "new arrival", "headline": "limited first release", "cta": "buy now"},
    {"course": "best seller", "headline": "TOP 1 hit product", "cta": "view"},
    {"course": "repeat purchase", "headline": "return customer praise", "cta": "reorder discount"},
    {"course": "bundle", "headline": "buy 2 get 1 free", "cta": "order now"}
  ],
  "constraints": {
    "must_feel": "e-commerce feel + conversion-oriented"
  }
}
```

## Variant 2: Campaign Multi-Scene Banner Set

Prompt

```json
{
  "type": "campaign multi-scene banner set",
  "brand": {
    "name": "{argument name=\"event\" default=\"618 mega sale\"}"
  },
  "panels": [
    {"headline": "teaser"},
    {"headline": "flash sale"},
    {"headline": "top picks"},
    {"headline": "encore"}
  ],
  "constraints": {
    "must_feel": "unified campaign visual system"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "2x2 banner auto-fill",
  "mode": "auto-fill",
  "rule": "User gives brand + one-line business description, auto-decide 4 banner themes + design",
  "constraints": {
    "must_feel": "ready for ad placement"
  }
}
```

## Things to Avoid

- Do not let 4 banners have style drift
- Do not let headline font sizes / fonts be inconsistent
- Do not let CTA positions be inconsistent
- Do not let the logo appear in different positions
- Do not stuff > 5 elements in a single banner