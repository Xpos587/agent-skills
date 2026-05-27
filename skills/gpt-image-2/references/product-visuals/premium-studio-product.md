# Premium Studio Product Image Template

This file is used to generate "top studio-grade commercial product images":

- Magazine ad-grade quality
- Dramatic lighting
- Unified color scheme
- Restrained props
- Product as the sole narrative protagonist

Suitable for:

- Perfume / high-end cosmetics
- Luxury watches / jewelry
- Spirits / wine
- Luxury accessories
- High-end 3C / audio-visual equipment
- Michelin restaurant main image

How it differs from `white-background-product.md`:

- White background image: e-commerce platform main image, emphasizing clean, accurate reproduction
- Studio image: ad-grade visual, emphasizing atmosphere, drama, brand tone

How it differs from `lifestyle-product-scene.md`:

- Studio image: pure product + pure atmosphere, no people, no life scenes
- Lifestyle image: product in a real usage scenario

## Scope

- High-end brand website hero image
- Magazine full-page ad
- Print campaign main visual
- Single product launch main image

## When to Use

- User mentions "studio / commercial ad / magazine / premium feel / cinematic / studio"
- User wants the product to look "expensive"
- User wants to move beyond white backgrounds but not into everyday scenes

Do NOT use:

- User wants e-commerce platform main image (use `white-background-product.md`)
- User wants product in a lifestyle scene (use `lifestyle-product-scene.md`)
- User wants to showcase packaging structure / gift box (use `packaging-showcase.md`)

## Missing Information Priority Questions

1. What the product specifically is + category
2. Brand positioning (high-end / minimalist / retro / dark / natural organic / futuristic)
3. Color scheme + main color + secondary color
4. Lighting atmosphere (soft / dramatic / cold / warm / overhead backlit)
5. Whether a few props are needed (same color family)
6. Whether main tagline / brand logo is needed

## Main Template: Single Product Premium Studio Visual

📖 Description

Product placed at center or golden ratio position, dark or same-color background, dramatic key light, minimal props, optional brand name + one tagline overlay.

📝 Prompt

```json
{
  "type": "Premium studio commercial product image",
  "goal": "Generate a studio visual directly usable as an ad-grade single-page main image, with the product as the sole narrative center, unified atmosphere, restrained color palette",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"Premium perfume glass bottle\"}",
    "visual_description": "{argument name=\"product visual\" default=\"Amber heavy glass bottle, gold metal cap, bottle printed with minimalist black brand name\"}",
    "position": "{argument name=\"product position\" default=\"Center-right of frame\"}",
    "scale": "{argument name=\"product scale\" default=\"Occupying 45% of frame\"}"
  },
  "background": {
    "type": "{argument name=\"background type\" default=\"Dark brown velvet fabric + same-tone environment\"}",
    "texture": "{argument name=\"background texture\" default=\"Fine velvet texture\"}",
    "color_tone": "{argument name=\"color tone\" default=\"Warm brown + gold\"}"
  },
  "lighting": {
    "key_light": "{argument name=\"key light\" default=\"Overhead 45° dramatic key light, clear sculpting\"}",
    "fill_light": "{argument name=\"fill light\" default=\"Right side weak soft light\"}",
    "rim_light": "{argument name=\"rim light\" default=\"Gold edge light from behind, outlining the bottle silhouette\"}",
    "mood": "{argument name=\"lighting mood\" default=\"Warm, luxurious, near-dusk feel\"}"
  },
  "props": {
    "enabled": "{argument name=\"props enabled\" default=\"true\"}",
    "items": [
      "{argument name=\"prop 1\" default=\"A few scattered dried rose petals\"}",
      "{argument name=\"prop 2\" default=\"Partial gold metallic reflection strip\"}"
    ],
    "rule": "Prop count ≤ 2, color must match the main color"
  },
  "text_overlay": {
    "enabled": "{argument name=\"text overlay enabled\" default=\"true\"}",
    "brand": "{argument name=\"brand name\" default=\"NUIT D'OR\"}",
    "headline": "{argument name=\"headline\" default=\"Night is another kind of light\"}",
    "position": "{argument name=\"text position\" default=\"Upper left half, sufficient whitespace\"}"
  },
  "style": {
    "rendering": "Top commercial photography + high dynamic range + fine grain, looks like a magazine full-page ad",
    "depth": "Shallow depth of field, background slightly blurred",
    "consistency": "Color palette strictly unified, no extra vivid colors"
  },
  "constraints": {
    "must_keep": [
      "Product as the absolute protagonist",
      "Unified lighting direction",
      "Unified color palette without clutter",
      "Copy does not obscure the product itself"
    ],
    "avoid": [
      "Props stealing the spotlight",
      "Lifestyle elements appearing (hands, tableware, models)",
      "Too many font types",
      "Background color too close to product, making outline invisible"
    ]
  }
}
```

### Parameter Strategy

- Required: product, brand positioning, main color
- Defaultable: props, copy position, lighting direction
- Random: specific prop items (generated reasonably within the main color range)

### Auto-fill Strategy

- Perfume / spirits default: dark tones + overhead key light
- Cosmetics default: soft cream tones + front soft light
- Jewelry default: dark background + strong rim light outlining
- Electronics default: deep space background + blue cold light
- Copy defaults to ≤ 8 characters, no long slogans

## Variant 1: Dark Luxury (Jewelry / Watches)

📝 Prompt

```json
{
  "type": "Dark luxury studio visual",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"Gold mechanical watch\"}",
    "visual_description": "{argument name=\"product visual\" default=\"Round gold case, brown crocodile leather strap, clear dial\"}"
  },
  "background": {
    "type": "Deep black plane + very weak reflection",
    "color_tone": "Near-black + localized gold"
  },
  "lighting": {
    "key_light": "Overhead spotlight",
    "rim_light": "Metallic edge light, emphasizing case silhouette"
  },
  "constraints": {
    "must_feel": "Rare, restrained, ceremonial"
  }
}
```

## Variant 2: Cool Electronics / Audio

📝 Prompt

```json
{
  "type": "Cool-toned electronics studio visual",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"Wireless smart speaker\"}",
    "visual_description": "{argument name=\"product visual\" default=\"Cylindrical deep space gray metal body, top touch ring with blue light\"}"
  },
  "background": {
    "type": "Deep space gray gradient",
    "color_tone": "Gray + cold blue"
  },
  "lighting": {
    "key_light": "Front soft light",
    "rim_light": "Blue backlight, creating tech feel"
  },
  "props": {
    "enabled": false
  },
  "constraints": {
    "must_feel": "Premium, restrained, futuristic"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Premium studio visual auto-fill template",
  "mode": "auto-fill",
  "rule": "Auto-select background tone, lighting direction, and copy length based on category, but keep the product as the sole narrative center",
  "constraints": {
    "must_feel": "Magazine ad grade"
  }
}
```

## Things to Avoid

- Do NOT include more than 2 props
- Do NOT show people or body parts (hands / lips / nails)
- Do NOT mix warm and cool tones (unless brand positioning explicitly allows it)
- Do NOT make product reflections so strong that brand text is unreadable
- Do NOT import white-background image style ("no atmosphere" does not equal premium)
- Do NOT make text larger than the brand's appropriate level of restraint (slogans should be few and short)