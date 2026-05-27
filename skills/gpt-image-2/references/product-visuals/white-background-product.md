# White-Background E-Commerce Main Image Template

This file is used to generate the most common "e-commerce pure white background product image":

- Single product white background
- Multi-angle white background
- White background + light shadow
- White background + minimal copy

Suitable for:

- Platform main image (Taobao / JD / Amazon / Douyin e-commerce first image)
- Product SKU card
- Detail page first screen static image
- App icon-style product anchor image

## Scope

- Single product image
- Multi-angle composite image
- Minimal copy main image
- Generic e-commerce main image

## When to Use

- User mentions "white background image / main image / product image / platform main image / SKU card"
- User wants to use directly on e-commerce platforms, no scene atmosphere needed
- User wants to highlight the product itself, no decorations

Do NOT use:

- User wants product in a lifestyle scene (use `lifestyle-product-scene.md`)
- User wants studio-grade atmosphere and texture (use `premium-studio-product.md`)
- User wants to showcase packaging appearance (use `packaging-showcase.md`)

## Missing Information Priority Questions

1. What the product specifically is (name + key visual features)
2. Single product or multi-angle
3. Whether text is needed (brand name / selling point / price)
4. Whether badges are needed (new / limited / discount)
5. Whether subtle shadow and reflection are needed

## Main Template: Minimal White Background Single Product

📖 Description

Pure white background, product centered, soft reflection / floor shadow, optional brand name and single selling point overlay.

📝 Prompt

```json
{
  "type": "White background e-commerce main image",
  "goal": "Generate a white background product image directly usable for e-commerce platform main image slot, with the product as the absolute visual center",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"White pump serum bottle\"}",
    "visual_description": "{argument name=\"product visual description\" default=\"Rounded shoulder bottle, frosted white body, metallic silver pump head, clean label on front\"}",
    "label_text": "{argument name=\"label text\" default=\"DERMA CALM Moisture Serum 30ml\"}",
    "angle": "{argument name=\"shot angle\" default=\"Front 3/4 view\"}",
    "scale": "{argument name=\"product scale\" default=\"Occupying 60% of frame\"}"
  },
  "background": {
    "type": "{argument name=\"background type\" default=\"Pure white\"}",
    "shadow": "{argument name=\"shadow\" default=\"Subtle bottom soft shadow\"}",
    "reflection": "{argument name=\"reflection\" default=\"None\"}"
  },
  "lighting": {
    "key_light": "{argument name=\"key light\" default=\"Front soft light\"}",
    "fill_light": "{argument name=\"fill light\" default=\"Even soft light from both sides\"}"
  },
  "text_overlay": {
    "enabled": "{argument name=\"text overlay enabled\" default=\"false\"}",
    "brand": "{argument name=\"overlay brand\" default=\"\"}",
    "selling_point": "{argument name=\"overlay selling point\" default=\"\"}"
  },
  "style": {
    "rendering": "High-resolution commercial photography + clean post-processing, no scene elements at all",
    "consistency": "True-to-life color reproduction, true-to-life texture reproduction"
  },
  "constraints": {
    "must_keep": [
      "Pure white background",
      "Product as the sole visual center",
      "Label text must be clearly readable"
    ],
    "avoid": [
      "Any decorative props appearing",
      "Color patches on the background",
      "Strong reflections interfering with the product itself",
      "Heavy outline on product edges"
    ]
  }
}
```

### Parameter Strategy

- Required: product name, key visual features, label text
- Defaultable: shooting angle, shadow style, lighting setup
- Random: frame occupancy ratio (floating within reasonable range)

### Auto-fill Strategy

- When no specific angle is given: skincare / beverages / electronics default to front 3/4, shoes default to 45° side view, bags default to front straight-on
- When no label text is given, do NOT fabricate a brand — leave it empty
- When no badges are specified, do NOT add any by default

## Variant 1: Multi-Angle White Background Composite

📝 Prompt

```json
{
  "type": "Multi-angle white background composite image",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"Wireless earbuds\"}",
    "angles_count": "{argument name=\"angle count\" default=\"3\"}",
    "angles": [
      "{argument name=\"angle 1\" default=\"Front: charging case closed\"}",
      "{argument name=\"angle 2\" default=\"Open case + earbuds exposed\"}",
      "{argument name=\"angle 3\" default=\"Single earbud close-up\"}"
    ],
    "arrangement": "{argument name=\"arrangement\" default=\"Horizontally evenly spaced\"}"
  },
  "background": {
    "type": "Pure white",
    "shadow": "Subtle shadow"
  },
  "constraints": {
    "must_feel": "Composite looks like it was shot in the same session, consistent lighting"
  }
}
```

## Variant 2: White Background + Minimal Marketing Overlay

Suitable for simple main images that need "brand + single selling point + price" overlaid on white background.

📝 Prompt

```json
{
  "type": "White background minimal marketing main image",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"Sports water bottle\"}"
  },
  "background": "Pure white",
  "text_overlay": {
    "enabled": true,
    "brand": "{argument name=\"brand\" default=\"AQUA GO\"}",
    "selling_point": "{argument name=\"selling point\" default=\"24-hour insulation\"}",
    "price": "{argument name=\"price\" default=\"¥ 89\"}",
    "badge": "{argument name=\"badge\" default=\"New arrival\"}",
    "layout": "Brand top left, selling point top right, price bottom right, badge bottom left"
  },
  "constraints": {
    "must_feel": "Like an e-commerce platform SKU main image",
    "avoid": "Confused information hierarchy"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "White background main image auto-fill template",
  "mode": "auto-fill",
  "rule": "User only provides product name, auto-determine angle, shadow, and frame occupancy, but strictly maintain pure white background",
  "constraints": {
    "must_feel": "Ready to list on e-commerce platforms directly"
  }
}
```

## Things to Avoid

- Background must not show gray edges, gradients, or textures
- Do NOT automatically add flowers, stones, fabrics, or other props for aesthetics
- Do NOT have shadow direction contradict lighting direction
- Do NOT make the product occupy less than 40% of frame, it will look sparse
- Do NOT fabricate a non-existent brand name for the label (unless explicitly allowed)
- Do NOT add stylized font text on a white background image (unless `text_overlay` is explicitly enabled)