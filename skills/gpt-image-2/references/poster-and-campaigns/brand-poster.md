# Brand Main Poster Template

This file is used to generate "a single main poster that represents a brand's expression at a given stage":

- New product launch main poster
- Quarterly campaign main image
- Brand upgrade main image
- Festival / holiday event main poster
- Company anniversary main image

Features:

- One strong slogan
- Clear visual center
- Brand colors strictly unified
- Suitable for landscape / portrait / square multi-format versions

## Scope

- Single brand main poster
- Large-scale campaign key visual
- Festival / anniversary / milestone main image

## When to Use

- User mentions "brand poster / key visual / KV / event main image / slogan poster"
- User wants one image that can represent the brand

Do NOT use:

- Series key visual (use `campaign-kv.md`)
- Web banner (use `banner-hero.md`)
- Magazine cover (use `editorial-cover.md`)

## Missing Information Priority Questions

1. Brand name + industry
2. Theme / slogan
3. Visual tone: futuristic / retro / minimalist / Chinese heritage / street
4. Whether there is a person / product / scene
5. Aspect ratio: portrait / landscape / square
6. Color palette

## Main Template: Single Brand Main Poster

📖 Description

A single poster with the main visual centered or occupying a large proportion, slogan clear, brand logo in the corner, suitable as a single-image distribution main image.

📝 Prompt

```json
{
  "type": "Brand main poster",
  "goal": "Generate a brand main poster that can be directly used as a launch event main image, campaign key visual, or social media hero image",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"AURORA\"}",
    "industry": "{argument name=\"industry\" default=\"Consumer Electronics\"}"
  },
  "visual_tone": {
    "aesthetic": "{argument name=\"aesthetic\" default=\"Minimalist futuristic\"}",
    "color_palette": "{argument name=\"color palette\" default=\"Deep blue + silver white + violet highlights\"}",
    "lighting": "{argument name=\"lighting\" default=\"Cool rim light + soft center light\"}"
  },
  "centerpiece": {
    "type": "{argument name=\"centerpiece type\" default=\"Product\"}",
    "description": "{argument name=\"centerpiece description\" default=\"Next-gen flagship earbuds, floating at the center of the frame, with a subtle glow at the 1/3 mark\"}",
    "scale": "{argument name=\"scale\" default=\"Occupying 50% of frame\"}"
  },
  "slogan": {
    "main": "{argument name=\"main slogan\" default=\"Hear Everything That Was Never Heard\"}",
    "sub": "{argument name=\"sub slogan\" default=\"AURORA Pro · Next-Gen Active Noise Cancellation\"}"
  },
  "logo_placement": {
    "position": "{argument name=\"logo position\" default=\"Bottom right corner\"}",
    "size": "Moderate, not competing with main visual"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4 portrait\"}",
  "constraints": {
    "must_keep": [
      "Main visual as visual anchor",
      "Slogan no more than 12 characters",
      "Brand logo must appear and be readable",
      "Color palette strictly consistent"
    ],
    "avoid": [
      "Information density too high",
      "Additional brand elements appearing",
      "More than 2 font types",
      "Background color blending with main visual"
    ]
  }
}
```

### Parameter Strategy

- Required: brand, slogan, main visual type, aspect ratio
- Defaultable: color palette, lighting, logo position
- Random: background texture details

### Auto-fill Strategy

- User provides brand + industry → auto-select tone (consumer electronics = futuristic, Chinese heritage = warm tones, retail = warm gray)
- Slogan defaults to 8-12 characters
- Logo defaults to bottom right corner

## Variant 1: Person + Product Dual Subject

📝 Prompt

```json
{
  "type": "Person + product dual-subject poster",
  "centerpiece": {
    "type": "human + product",
    "human": "{argument name=\"human\" default=\"East Asian young woman, natural smile\"}",
    "product": "{argument name=\"product\" default=\"White serum bottle\"}",
    "composition": "Person on right, product at left 1/3"
  },
  "constraints": {
    "must_feel": "Trust, quality, clear brand persona"
  }
}
```

## Variant 2: Pure Text Main Poster

📝 Prompt

```json
{
  "type": "Pure text brand main poster",
  "slogan": {
    "main": "{argument name=\"slogan\" default=\"We Want to Win, But More Importantly, Bring Our Partners Along\"}"
  },
  "visual_tone": {
    "aesthetic": "Minimalist, generous whitespace, typography as visual"
  },
  "constraints": {
    "must_feel": "Attitude, values, sense of belief"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Brand main poster auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides brand and milestone, auto-select tone, color palette, slogan, main visual",
  "constraints": {
    "must_feel": "Ready for public distribution"
  }
}
```

## Things to Avoid

- Do NOT let the slogan exceed 12 characters
- Do NOT let the logo compete with the main visual
- Do NOT place multiple products in one poster
- Do NOT use more than 3 font types
- Do NOT let the background contain recognizable third-party brands
