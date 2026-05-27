# Large-Type Statement / Title-Safe Poster Template

This file is used for "posters where the giant text itself is the hero visual":

- Large-type statement (Hyper-Energetic Japanese Promo)
- Type-first poster
- Slogan / statement banner
- Extreme typography exercise
- Text-driven movie poster feel

Characteristics:

- The text itself is the subject (font size super-large occupying 50%+ of the frame)
- Usually 3-7 characters + 1-2 lines of small text
- Highly designed typography (handwritten / vintage print / noise / graffiti)
- Restrained background
- Emphasis on "message readable at a glance"

## Scope

- Slogan / statement posters
- Campaign / mega sale hero visuals
- Type-first banners

## When to use

- User mentions "large type / statement / hero text / type-first / text poster"
- User wants "one sentence is the hero image"
- User wants Japanese / extreme typography style

Do NOT use for:

- Posters with products → use `poster-and-campaigns/brand-poster.md`
- Editorial magazine covers → use `poster-and-campaigns/editorial-cover.md`
- Complex narratives → use `scenes-and-illustrations/concept-scene.md`

## Missing Information Priority Question Order

1. Main slogan (3-7 characters)
2. Sub-tagline / tagline
3. Style positioning (Japanese Showa / modern minimalist / vintage print / graffiti / noise)
4. Primary color 1-2
5. Whether to include small text annotations / logo
6. Aspect ratio

## Main Template: Japanese High-Energy Large-Type Poster

Description

One image, main subject is large slogan text itself + sub-tagline + small text + minimal graphic accents.

Prompt

```json
{
  "type": "Japanese high-energy large-type poster",
  "goal": "Generate a high-energy poster with giant text as the hero visual",
  "headline": {
    "text": "{argument name=\"headline\" default=\"FULL SPEED AHEAD\"}",
    "language": "{argument name=\"language\" default=\"Chinese / Japanese mixed\"}",
    "size": "occupying 60%+ of the frame",
    "alignment": "{argument name=\"alignment\" default=\"center\"}",
    "treatment": "{argument name=\"treatment\" default=\"noise overlay + halftone dots + offset stroke\"}"
  },
  "subheadline": {
    "text": "{argument name=\"subheadline\" default=\"GO ALL OUT 2026\"}",
    "size": "1/4 of headline",
    "position": "{argument name=\"sub position\" default=\"centered below headline\"}"
  },
  "small_text": {
    "items": [
      "{argument name=\"small text 1\" default=\"4.24-5.24 SPECIAL CAMPAIGN\"}",
      "{argument name=\"small text 2\" default=\"X COLLECTIVE\"}"
    ],
    "position": "bottom corners"
  },
  "design": {
    "primary_color": "{argument name=\"primary color\" default=\"#FF2C2C vermilion red\"}",
    "background_color": "{argument name=\"background\" default=\"#F4EEDC yellowish cream\"}",
    "decoration": "{argument name=\"decoration\" default=\"4-5 simple geometric shapes (circle / triangle / short bold arrow), deliberate whitespace\"}",
    "typography_family": "{argument name=\"font family\" default=\"modern Japanese sans + one handwritten accent\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "Slogan text must be readable at a glance",
      "Text occupies the absolute main subject of the frame",
      "Colors ≤ 3",
      "Fonts ≤ 2 families"
    ],
    "avoid": [
      "Slogan text too small, overwhelmed by decorations",
      "More than 6 decorative shapes",
      "More than 3 font types",
      "Typos in the slogan"
    ]
  }
}
```

### Parameter Strategy

- Must ask: slogan, sub-tagline, style, primary color
- Can default: layout, decorations, fonts
- Can randomize: specific decorative shapes

### Auto-Fill Strategy

- User gives slogan + style keyword → auto-decide text treatment + colors + decorations
- Default Japanese high-energy = noise + halftone + offset
- Default 3:4

## Variant 1: Minimal Swiss Typography Large-Type Poster

Prompt

```json
{
  "type": "minimal Swiss typography large-type poster",
  "headline": {
    "treatment": "no decorations + sans-serif + strict grid"
  },
  "design": {
    "primary_color": "pure black",
    "background_color": "pure white",
    "decoration": "none / only one thin horizontal line"
  },
  "constraints": {
    "must_feel": "Swiss graphic / Minimal"
  }
}
```

## Variant 2: Vintage Print Large-Type Poster

Prompt

```json
{
  "type": "vintage print large-type poster",
  "headline": {
    "treatment": "register shift + ink bleed + slight dirty feel"
  },
  "design": {
    "primary_color": "vintage red",
    "background_color": "aged cream paper",
    "decoration": "vintage print symbols"
  },
  "constraints": {
    "must_feel": "1960s letterpress"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "large-type poster auto-fill",
  "mode": "auto-fill",
  "rule": "User gives one slogan, auto-decide style + colors + text treatment + decorations",
  "constraints": {
    "must_feel": "printable + readable at a glance"
  }
}
```

## Things to Avoid

- Do not let slogan text be smaller than 40% of the frame
- Do not let decorations dominate the main subject
- Do not let the slogan have typos (most critical)
- Do not let fonts exceed 2 families
- Do not let background saturation overpower the main slogan
- Do not let small text exceed 3 lines
