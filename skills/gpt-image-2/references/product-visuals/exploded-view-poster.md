# Product Exploded View Poster Template

This file is used to generate "a complete product vertically stacked and expanded into internal components + callout annotations + top promotional copy + bottom brand area" premium product poster.

Representative examples:

- VR headset exploded view
- Phone internal structure exploded diagram
- Smart speaker teardown diagram
- Wireless earbud exploded view
- High-end home appliance teardown diagram
- Camera / lens component expansion diagram
- Outdoor gear teardown diagram

## Scope

- High-end product launch main visual
- Detail page "tech highlights" single image
- Engineering aesthetics showcase
- Internal structure educational diagram
- Media-grade tech poster

## When to Use

- User mentions "exploded view / teardown diagram / internal structure / exploded view"
- User wants to showcase product engineering structure / modular design / technical details
- User wants a visual style leaning towards "hardcore engineering feel + commercial poster"

Do NOT use:

- User only wants white-background product image (use `white-background-product.md`)
- User only wants scene-based product image (use `lifestyle-product-scene.md`)
- User wants packaging display (use `packaging-showcase.md`)

## Missing Information Priority Questions

1. What the product is (specific model or category)
2. How many components you want to highlight (typically 6-9)
3. Brand name / main tagline / sub-tagline
4. Color scheme (soft gradient / pure black / aurora / deep space)
5. Whether bilingual callouts are needed (Chinese + English)
6. Callout layout: both sides distributed / top & bottom distributed / single side

## Main Template: Vertical Exploded View + Dual-Side Callouts

📖 Description

Main subject vertically stacked and expanded into multiple layers in the center of the frame, with callout labels distributed on both sides, product name + main tagline at top, closing copy + brand logo at bottom.

📝 Prompt

```json
{
  "type": "Product exploded view poster",
  "goal": "Generate a high-tech, engineering-aesthetic product poster with a vertical exploded view as the main subject and technical callouts on both sides, usable as a launch event main visual or detail page tech highlights image",
  "subject": "{argument name=\"product\" default=\"VR headset\"}",
  "style": {
    "rendering": "{argument name=\"render style\" default=\"Clean high-tech 3D render, studio lighting, glowing accents\"}",
    "background_color": "{argument name=\"background color\" default=\"Soft purple-blue gradient\"}",
    "lighting": "{argument name=\"lighting\" default=\"Studio overhead light + subtle rim light, faint glowing atmosphere between components\"}"
  },
  "header": {
    "logo": "{argument name=\"product brand mark\" default=\"∞ Meta Quest 3\"}",
    "subtitle": "{argument name=\"main catchphrase\" default=\"Reinventing reality with an entirely new structure.\"}"
  },
  "layout": {
    "centerpiece": "{argument name=\"centerpiece description\" default=\"Vertical stacked exploded view of a VR headset, showing 9 layers of different internal components from bottom to top: outer shell, camera sensors, main board with chip, Pancake lenses, internal frame, battery pack, side strap, top head strap, and facial interface pad\"}",
    "callout_layout": "{argument name=\"callout layout\" default=\"Evenly distributed on both sides\"}",
    "callout_labels": {
      "count": "{argument name=\"callout count\" default=\"8\"}",
      "left_side": [
        "{argument name=\"left callout 1\" default=\"Snapdragon® XR2 Gen 2\\nOutstanding processing performance for real-time immersive experiences.\"}",
        "{argument name=\"left callout 2\" default=\"Adjustable IPD mechanism\\nComfortable fit for a wide range of users.\"}",
        "{argument name=\"left callout 3\" default=\"Precision-engineered head strap\\nErgonomic design for comfort and stability.\"}"
      ],
      "right_side": [
        "{argument name=\"right callout 1\" default=\"Front panel\\nRefined design with optimized weight balance.\"}",
        "{argument name=\"right callout 2\" default=\"Tracking cameras\\nHigh-precision positional tracking and environmental sensing.\"}",
        "{argument name=\"right callout 3\" default=\"Pancake lenses\\nSlim design, wide field of view, and crisp image quality.\"}",
        "{argument name=\"right callout 4\" default=\"High-performance battery\\nOptimized power design for extended battery life.\"}",
        "{argument name=\"right callout 5\" default=\"Soft facial interface\\nEnsures comfort even during extended wear.\"}"
      ]
    },
    "footer": {
      "left_text_block": {
        "headline": "{argument name=\"bottom headline\" default=\"Experience born from structural evolution.\"}",
        "body": "{argument name=\"bottom body\" default=\"Every component embodies cutting-edge technology and meticulous design that supports immersive experiences. Meta Quest 3 builds the future from the inside out, delivering experiences beyond imagination.\"}"
      },
      "right_logo": "{argument name=\"footer brand logo\" default=\"∞ Meta\"}"
    }
  },
  "constraints": {
    "must_keep": [
      "Component layering is clear, with appropriate spacing between layers",
      "Callout leader lines point to the correct components",
      "Top logo and bottom brand area do not overlap with components",
      "Overall looks like a premium launch event poster"
    ],
    "avoid": [
      "Components spread too densely, making them hard to see",
      "Callout text too long causing messy line breaks",
      "Inconsistent lighting direction",
      "Components clipping or intersecting each other"
    ]
  }
}
```

### Parameter Strategy

- Required: product, component count, main tagline
- Defaultable: background color, lighting, callout template copy
- Random: secondary technical description wording, bottom paragraph copy

### Auto-fill Strategy

When the user only provides a "product name":

- Auto-infer 6-9 common components
- Callout copy uses "technical name + one-sentence value description" format
- Main tagline uses "With... reinvent..." or "Born from structural evolution" style closing statements
- Bottom brand area defaults to same as top logo

## Variant 1: Phone / Tablet Exploded Diagram

📝 Prompt

```json
{
  "type": "Smart device exploded view poster",
  "subject": "{argument name=\"product\" default=\"Flagship smartphone\"}",
  "style": {
    "rendering": "Deep space black background + minimalist metallic reflections",
    "background_color": "{argument name=\"background color\" default=\"Near-black deep space gray\"}"
  },
  "header": {
    "logo": "{argument name=\"product mark\" default=\"NEX Pro\"}",
    "subtitle": "{argument name=\"catchphrase\" default=\"See every layer, understand every detail\"}"
  },
  "layout": {
    "centerpiece": "Phone internals vertically exploded from bottom to top in 8 layers: metal frame, main board (with SoC), screen assembly, camera module, vibration unit, battery, speaker, glass back cover",
    "callout_labels": {
      "count": 8,
      "items_template": "Component name + one-sentence tech highlight"
    }
  },
  "constraints": {
    "must_feel": "Engineering aesthetics + flagship launch feel"
  }
}
```

## Variant 2: Wearable / Audio Exploded Diagram

📝 Prompt

```json
{
  "type": "Wearable product exploded view poster",
  "subject": "{argument name=\"product\" default=\"Wireless noise-cancelling headphones\"}",
  "style": {
    "rendering": "Minimalist white background + soft shadows + localized metallic reflections",
    "background_color": "{argument name=\"background color\" default=\"Off-white gradient\"}"
  },
  "header": {
    "logo": "{argument name=\"product mark\" default=\"AURA Pro\"}",
    "subtitle": "{argument name=\"catchphrase\" default=\"Silence from the inside out\"}"
  },
  "layout": {
    "centerpiece": "Ear cup side exploded into 6 layers: outer shell, microphone array, noise-cancellation chip board, driver unit, acoustic sponge, memory foam ear pad",
    "callout_labels": {
      "count": 6
    }
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Exploded view poster auto-fill template",
  "mode": "auto-fill",
  "rule": "After the user provides a product name, auto-determine layer count (6-9 layers), callout count, main tagline, bottom paragraph, and brand logo, but must maintain four essentials: clear components, callouts aligned to components, top main tagline, bottom brand",
  "constraints": {
    "must_feel": "Premium launch event main visual"
  }
}
```

## Things to Avoid

- Do NOT have too many component layers (over 10 layers will look crowded)
- Do NOT let callout leader lines cross over other components
- Do NOT write callout text as marketing slogans — should be "component + technology + value" three-part format
- Do NOT have the top logo and bottom brand logo be inconsistent
- Do NOT add irrelevant decorative elements to the background (rings, patterns, brush strokes)
- Do NOT have conflicting lighting directions (overhead light + reversed shadow immediately breaks the illusion)