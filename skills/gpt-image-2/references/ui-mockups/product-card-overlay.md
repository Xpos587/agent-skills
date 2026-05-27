# Product Card Overlay Mockup Template

This file is used to generate "people / scene image as the base, with product cards / marketing UI elements overlaid" e-commerce mockups.

How it differs from `live-commerce-ui.md`:

- `live-commerce-ui.md`: simulates live stream platform interfaces, emphasizing chat area / gift area / platform UI
- This template: focuses on "product + model / product + scene + selling point card" product marketing visuals, closer to a landing page hero area or e-commerce detail page main image

## Scope

- E-commerce detail page main image mockup
- Landing page hero section
- WeChat Moments / official account image with product card
- Single-image ad: person + product card + selling point badge
- Model holding product + info card overlay

## When to Use

- User wants "one image that explains what the product is / selling points / price"
- User mentions "detail page main image / ad image / hero image / landing page mockup"
- User wants both a real person visual and an e-commerce information layer

Do NOT use:

- User wants a real live stream screenshot (use `live-commerce-ui.md`)
- User wants a pure white background product image (use `product-visuals/white-background-product.md`)

## Missing Information Priority Questions

1. What the product is (name + category)
2. Main subject source: real model photo, model description, abstract "no person" scene
3. Whether to show price / selling points / badges
4. Style: Japanese minimalist / tech / warm lifestyle / premium studio / street fashion
5. Dominant color palette
6. Copy language: Chinese / English / Japanese / bilingual

## Main Template: Person + Product Card + Selling Point Overlay

📖 Description

Generate an e-commerce landing page hero area visual, with a stable structure: left copy + center product + right model / scene.

📝 Prompt

```json
{
  "type": "E-commerce landing page hero product card overlay mockup",
  "goal": "Generate an image that can be directly used as an e-commerce detail page main visual or marketing landing page hero area, containing four elements: person, product, selling points, and pricing info",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"DERMA CALM\"}",
    "subtext": "{argument name=\"brand subtext\" default=\"For Sensitive Skin\"}"
  },
  "color_palette": {
    "base": "{argument name=\"base color\" default=\"White\"}",
    "primary": "{argument name=\"primary color\" default=\"Dark blue\"}",
    "accent": "{argument name=\"accent color\" default=\"Light blue\"}"
  },
  "layout": {
    "header": {
      "logo": "Left brand name + subtitle",
      "navigation_links": "{argument name=\"nav links\" default=\"ABOUT, PRODUCT, FEATURE, INGREDIENT, VOICE, Q&A\"}",
      "cta_buttons": "{argument name=\"cta buttons\" default=\"My Page, Buy Now\"}"
    },
    "hero": {
      "left_column": {
        "headline": "{argument name=\"main headline\" default=\"Gentle care that sensitive skin can use safely every day\"}",
        "subtext": "{argument name=\"sub headline\" default=\"Low irritation · Long-lasting moisture · Fragrance-free · Alcohol-free\"}",
        "buttons": ["Buy Now", "Learn More"]
      },
      "center_column": {
        "product": "{argument name=\"product description\" default=\"White pump bottle, bottle printed 'Moisture Barrier Serum'\"}",
        "props": [
          "Close-up of white emulsion-textured drops",
          "Circular 'Dermatologist Supervised' badge"
        ]
      },
      "right_column": {
        "subject": "{argument name=\"model description\" default=\"Young East Asian woman, translucent skin, fingers lightly touching cheek\"}",
        "background": "{argument name=\"background\" default=\"Blurred lab glassware background, bright and clean\"}"
      }
    },
    "bottom_features_panel": {
      "left_cards": {
        "count": "{argument name=\"left feature count\" default=\"3\"}",
        "items": [
          "{argument name=\"feature 1\" default=\"95% of users gave 5-star reviews\"}",
          "{argument name=\"feature 2\" default=\"Low-irritation formula, shield icon\"}",
          "{argument name=\"feature 3\" default=\"Droplet icon + Barrier repair\"}"
        ]
      },
      "right_badges": {
        "count": 3,
        "items": ["Fragrance-free", "Alcohol-free", "Sensitive skin tested"]
      },
      "footer": "Bottom small-text disclaimer"
    }
  },
  "style": {
    "rendering": "Clean, clinical feel, commercial-grade render, looks like a real landing page screenshot",
    "consistency": "Color palette strictly follows base / primary / accent three colors"
  },
  "constraints": {
    "must_keep": [
      "Three-column structure is clear",
      "Product as visual center",
      "Copy consistent with the product",
      "Badges cannot be larger than the logo"
    ],
    "avoid": [
      "Extremely crowded layout",
      "Model's pose looking unnatural",
      "Extra bright colors appearing in the palette"
    ]
  }
}
```

### Parameter Strategy

- Required: product name, brand name, model direction, main color
- Defaultable: navigation copy, button copy, badge copy
- Random: bottom small-text disclaimer, specific wording of selling points

### Auto-fill Strategy

- If no brand is given, generate a concise English brand name + Chinese subtitle
- If no model direction is given, default to target user profile (skincare → young woman / men's skincare → young man / tech → urban young adult)
- Must have 3 selling points, no duplicates, no empty platitudes

## Variant 1: Dark Tech Product Landing Page

📝 Prompt

```json
{
  "type": "Dark tech brand landing page hero mockup",
  "theme": "{argument name=\"theme\" default=\"Men's skincare / Digital hardware\"}",
  "color_palette": ["Deep navy blue", "White", "Blue gradient"],
  "header": {
    "logo": "{argument name=\"brand name\" default=\"NEX SKIN\"}",
    "navigation": ["HOME", "PRODUCT", "ABOUT", "FEATURE", "FAQ"],
    "cta_button": "Get Started >"
  },
  "hero": {
    "left_column": {
      "headline": "{argument name=\"main headline\" default=\"Freshness starts with daily care\"}",
      "sub_headline": "Men's skin deserves simplicity",
      "feature_highlights": [
        "Oil control: Regulates sebum",
        "Moisturizing: Long-lasting hydration",
        "All-in-one: Toner + Serum + Lotion"
      ]
    },
    "center_image": {
      "subject": "{argument name=\"model\" default=\"Clean-cut young Asian man\"}",
      "pose": "Hand on chin in thought"
    },
    "right_column": {
      "product_shot": "{argument name=\"product\" default=\"Tall slim dark blue bottle with water droplets\"}"
    }
  },
  "bottom_stats_bar": {
    "items": [
      "Cumulative sales 1.2M bottles",
      "Satisfaction rate 92.1%",
      "Repurchase rate 85.3%"
    ]
  },
  "constraints": {
    "must_feel": "Masculine, professional, trustworthy"
  }
}
```

## Variant 2: Four-Panel Person + Product Card Collection

Suitable for covering multiple demographics / scenarios in one image.

📝 Prompt

```json
{
  "type": "Four-panel person-product card collection mockup",
  "layout": "2x2 grid, each panel with independent person + independent product card",
  "quadrants": [
    {
      "position": "Top left",
      "industry": "Skincare",
      "subject": "Asian woman lightly touching cheek",
      "product": "White pump bottle",
      "headline": "{argument name=\"q1 headline\" default=\"Awaken Your Skin\"}"
    },
    {
      "position": "Top right",
      "industry": "Food & Beverage",
      "subject": "Close-up of Bolognese pasta",
      "product": "Restaurant logo + limited edition label",
      "headline": "{argument name=\"q2 headline\" default=\"This Bowl Is an Event\"}"
    },
    {
      "position": "Bottom left",
      "industry": "Travel",
      "subject": "Backpacker facing mountain lake",
      "product": "Travel brand + discount banner",
      "headline": "{argument name=\"q3 headline\" default=\"Set Out, Be Free\"}"
    },
    {
      "position": "Bottom right",
      "industry": "SaaS App",
      "subject": "Phone showing task management App interface",
      "product": "App brand + 7-day free trial",
      "headline": "{argument name=\"q4 headline\" default=\"Make Task Management Simpler\"}"
    }
  ],
  "constraints": {
    "must_feel": "Like the same brand matrix or same ad campaign production"
  }
}
```

## Variant 3: Auto-fill Mode

For when the user just says "make an e-commerce landing page main image."

📝 Prompt

```json
{
  "type": "Landing page product card overlay auto-fill template",
  "mode": "auto-fill",
  "rule": "Based on the main template, auto-fill brand name, copy, and model direction, but keep all four elements: brand, person, product, and selling points present",
  "constraints": {
    "must_feel": "Real e-commerce ad image",
    "avoid": "Looks like a PPT slide"
  }
}
```

## Things to Avoid

- Do NOT make the model's expression overly exaggerated or fake-smiling (immediately destroys credibility)
- Keep selling point badges to ≤ 3-4, more becomes ad noise
- Copy color must not be too close to the background image, otherwise unreadable
- Product must have clear main lighting in the frame, cannot be blurred along with the model
- Do NOT have Chinese + English + Japanese all occupying equal size; there must be a dominant language