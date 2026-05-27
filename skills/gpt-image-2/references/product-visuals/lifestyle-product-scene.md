# Lifestyle Product Scene Image Template

This file is used to generate "product appearing in a real-life scene" visuals:

- Laptop on a desk workspace
- Drink on a seaside resort table
- Latte on a cafe table
- Skincare on a morning vanity
- Headphones on a dorm bed
- Gear in an outdoor camping scene

Emphasis:

- Product "being used / ready to use / just used" in the scene
- Real lifestyle atmosphere
- Natural or soft lighting primarily
- Appropriate props, but not overpowering

How it differs from `premium-studio-product.md`:

- Studio shot: pure atmosphere, pure product, dramatic lighting, no scene
- Lifestyle image: real scene, natural lighting, may include partial human (hand, back view)

How it differs from `product-card-overlay.md`:

- product-card-overlay: e-commerce detail page hero, must have UI card / copy overlay
- This template: pure photography scene image, no UI overlay required

## Scope

- Brand website hero
- Marketing banner main visual
- Instagram / Xiaohongshu / WeChat Moments cover
- Content-driven e-commerce assets
- Holiday promotion scene image
- Magazine-style lifestyle cover

## When to Use

- User mentions "scene image / lifestyle / lifestyle / real scene / magazine feel"
- User wants the product to look "like someone is using it"
- User wants the visual to feel natural, not overly commercial

Do NOT use:

- User wants e-commerce main image (use `white-background-product.md`)
- User wants exploded view (use `exploded-view-poster.md`)
- User wants packaging display (use `packaging-showcase.md`)
- User wants pure atmosphere ad-grade single product (use `premium-studio-product.md`)

## Missing Information Priority Questions

1. What the product specifically is
2. Scene: office desk / cafe / morning vanity / seaside / outdoors / kitchen / bedroom
3. Time: early morning, afternoon, dusk, night
4. Climate / lighting: natural light, warm light, overcast soft light, indoor lighting
5. Whether to include a person (partial / full body / back view)
6. Whether light copy is needed (slogan / hashtag)

## Main Template: Single Product + Real Scene

📖 Description

Product placed in a real-life scene, natural lighting primarily, may include partial human (hand / back view), few props to add lifestyle feel.

📝 Prompt

```json
{
  "type": "Lifestyle product scene image",
  "goal": "Generate a visual of a product appearing in a real-life scene, with authentic, restrained, high-quality atmosphere, usable as a brand main visual or social media cover",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"White pump serum bottle\"}",
    "visual_description": "{argument name=\"product visual\" default=\"Rounded shoulder bottle, frosted white, bottle printed 'DERMA CALM'\"}",
    "position": "{argument name=\"product position\" default=\"Center-right of frame\"}"
  },
  "scene": {
    "location": "{argument name=\"scene location\" default=\"Wooden vanity in morning sunlight\"}",
    "time_of_day": "{argument name=\"time of day\" default=\"Early morning\"}",
    "weather_or_mood": "{argument name=\"mood\" default=\"Fresh, soft, just-awakened feel\"}",
    "extra_props": [
      "{argument name=\"prop 1\" default=\"Clear water in a translucent glass\"}",
      "{argument name=\"prop 2\" default=\"Scattered white petals\"}",
      "{argument name=\"prop 3\" default=\"Folded off-white towel\"}"
    ]
  },
  "lighting": {
    "type": "{argument name=\"light type\" default=\"Natural light\"}",
    "direction": "{argument name=\"light direction\" default=\"Side light from left window\"}",
    "intensity": "{argument name=\"light intensity\" default=\"Soft\"}",
    "color_temp": "{argument name=\"color temperature\" default=\"Slightly warm\"}"
  },
  "human_presence": {
    "enabled": "{argument name=\"include human\" default=\"true\"}",
    "form": "{argument name=\"human form\" default=\"Partial, such as fingers lightly touching the bottle\"}",
    "rule": "If including a person, must feel natural and not posed; no full face visible"
  },
  "text_overlay": {
    "enabled": "{argument name=\"text enabled\" default=\"false\"}",
    "brand": "{argument name=\"brand name\" default=\"\"}",
    "headline": "{argument name=\"headline\" default=\"\"}"
  },
  "style": {
    "rendering": "Real photography feel + grain + low saturation, not like a hard ad shot",
    "depth": "Shallow depth of field, subject in sharp focus",
    "consistency": "Unified color tone, no jarring high-saturation elements"
  },
  "constraints": {
    "must_keep": [
      "Product is the visual focus",
      "Scene is realistic and believable",
      "Lighting direction is consistent",
      "Props match the product's color palette"
    ],
    "avoid": [
      "Scene looks like a 3D render",
      "Person's full face stealing attention",
      "Props overpowering the product",
      "Obvious e-commerce ad cards appearing"
    ]
  }
}
```

### Parameter Strategy

- Required: product, scene, whether to include person
- Defaultable: time, lighting, props
- Random: specific prop items (generated reasonably within the color palette and scene)

### Auto-fill Strategy

- Skincare default: morning vanity + natural side light + towel, petals, glass
- Beverage default: outdoor or tabletop + natural light + ice cubes, lemon slices
- Electronics default: office desk + indoor natural light + notebook, coffee cup
- Outdoor gear default: dusk natural light + mountains / seaside + simple background elements

## Variant 1: Beverage Outdoor Scene

📝 Prompt

```json
{
  "type": "Beverage outdoor lifestyle scene image",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"Golden sparkling beverage aluminum can\"}"
  },
  "scene": {
    "location": "Seaside wooden table",
    "time_of_day": "Sunny afternoon",
    "extra_props": [
      "Tall glass + lemon garnish",
      "Nearby water-droplet-covered can",
      "Distant blurred beach and sky"
    ]
  },
  "lighting": {
    "type": "Natural light",
    "direction": "Overhead + flash fill",
    "intensity": "Bright"
  },
  "human_presence": {
    "enabled": true,
    "form": "Distant woman's back facing the sea"
  },
  "text_overlay": {
    "enabled": true,
    "headline": "{argument name=\"headline\" default=\"Summer, the one sip you need\"}"
  },
  "constraints": {
    "must_feel": "Vacation, refreshing, freedom"
  }
}
```

## Variant 2: Office Desk Electronics Scene

📝 Prompt

```json
{
  "type": "Desktop electronics lifestyle scene image",
  "subject": {
    "product_name": "{argument name=\"product name\" default=\"Wireless earbud charging case\"}"
  },
  "scene": {
    "location": "Minimalist Scandinavian-style desk",
    "time_of_day": "Morning",
    "extra_props": [
      "Laptop half-open",
      "Coffee cup",
      "Small plant",
      "Open notebook"
    ]
  },
  "lighting": {
    "type": "Indoor natural light + overhead soft light",
    "direction": "Front-left",
    "intensity": "Bright and even"
  },
  "human_presence": {
    "enabled": true,
    "form": "Partial fingers resting naturally on the desk"
  },
  "constraints": {
    "must_feel": "Professional, focused, clean"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Lifestyle scene image auto-fill template",
  "mode": "auto-fill",
  "rule": "When user only provides a product name, auto-determine the most suitable scene, time, lighting, and human presence approach, but must maintain the product as the visual focus",
  "constraints": {
    "must_feel": "Magazine-quality, believable, not exaggerated"
  }
}
```

## Things to Avoid

- Do NOT make the person's full face the protagonist
- Do NOT stuff more than 4-5 props
- Do NOT mix "studio overhead light + indoor natural light" lighting
- Do NOT make the saturation too high, it becomes a hard ad shot
- Do NOT overlay e-commerce style "price + discount" cards on a lifestyle image (that's product-card-overlay's job)
- Do NOT have background elements that create brand conflicts (e.g., an Apple computer at a competitor's launch event)