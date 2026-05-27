# Chinese E-Commerce All-in-One Sales Board Template

This file is used to generate "a super-tall vertical image that packs e-commerce platform main image + detail page + selling points + usage steps + scenarios + packaging info + TVC storyboard all into a single image" composite sales visual.

Typical uses:

- Taobao / Tmall / JD detail page hero slot "one-image approval before listing"
- Douyin / Kuaishou e-commerce detail page vertical single image
- Franchise proposal / client review one-image overview
- Seller's "master template" for new product assets, later sliced into main images / detail pages / video scripts
- Cross-border e-commerce internal communication "one complete product marketing strategy"

Characteristics (compared to existing product-visuals templates):

| Template | Info Density | Function |
|---|---|---|
| `white-background-product.md` (existing) | Low | Single product multi-angle pure white background |
| `premium-studio-product.md` (existing) | Medium | Premium studio commercial shot |
| `lifestyle-product-scene.md` (existing) | Medium | Lifestyle scene |
| `packaging-showcase.md` (existing) | Medium | Gift box / packaging display |
| `exploded-view-poster.md` (existing) | High | Product exploded view + callout |
| **This template** (new) | **Very high** | **5-7 sales modules + TVC storyboard table all in one image** |

**Key distinction**: This template is NOT a "product visual poster", but a "detail page + main image + selling points + usage + scenarios + video script design master board".

## Scope

- Chinese e-commerce detail page full design master board
- New product launch one-image approval draft
- Seller "franchise + review + internal sharing" all-scenario use
- Food / beauty / daily goods / health categories (high info density categories)
- "Main image + detail page + video script" integrated proposal

## When to Use

- User mentions "detail page design / e-commerce main image + detail page together / one-image approval / full sales board"
- User wants a composite visual "including usage steps + scenarios + TVC storyboard"
- Chinese e-commerce food / beauty / maternity & baby / daily goods categories (naturally high info density)

Do NOT use:

- Single product white background main image → use `white-background-product.md`
- Premium commercial shot → use `premium-studio-product.md`
- TVC 9-panel storyboard only → use `storyboards-and-sequences/product-tvc-storyboard.md`
- Overseas e-commerce single image (low info density) → use `product-card-overlay.md` or `banner-hero.md`

## Missing Information Priority Questions

1. Product category + brand + product name (required, the soul of the board)
2. Packaging appearance (box color / font / logo / contents)
3. Color scheme (dark luxury food / light refreshing beauty / warm maternity & baby / cool tech)
4. Core selling points that must appear (4-6 items, determines mid-section feature panel content)
5. Usage method / brewing steps (determines HOW TO MAKE area)
6. Application scenarios (breakfast / office / gym / before bed, pick 4)
7. Whether bottom TVC storyboard table is needed (default yes)

## Main Template: 5+1 Module E-Commerce All-in-One Sales Board

📖 Description

Vertical super-long canvas, divided into top / middle / bottom + bottom storyboard table four zones, containing 5 sales modules + 1 TVC storyboard strip.

📝 Prompt

```json
{
  "type": "Chinese e-commerce product marketing board",
  "goal": "Generate a composite sales board simultaneously containing main image / detail page / selling points / usage steps / scenarios / portability / TVC storyboard, usable as detail page master / franchise draft / seller internal asset",
  "product": {
    "category": "{argument name=\"product category\" default=\"instant grain powder drink\"}",
    "brand": "{argument name=\"brand\" default=\"Wugu Mofang\"}",
    "name": "{argument name=\"product name\" default=\"Walnut Sesame Black Bean Powder\"}",
    "packaging": "{argument name=\"packaging description\" default=\"matte black retail box with gold Chinese typography and a large swirling bowl graphic on the front, plus individual black sachets inside\"}",
    "net_weight": "{argument name=\"net weight\" default=\"320g (32g x 10 sachets)\"}"
  },
  "style": {
    "overall": "{argument name=\"overall style\" default=\"premium dark food advertising layout\"}",
    "color_palette": ["black", "deep brown", "warm gold", "beige", "walnut brown"],
    "lighting": "dramatic studio lighting with glossy highlights and warm rim light",
    "mood": "{argument name=\"mood\" default=\"luxurious, nourishing, healthy, appetizing\"}"
  },
  "layout": {
    "format": "single tall composite board divided into 5 major sections plus a bottom storyboard table",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"portrait, approximately 9:16\"}",
    "grid": "top area split into left main image and right detail page; middle area split into preparation guide and feature panel; lower area split into lifestyle scenarios and sachet carry section; bottom is a full-width tabular storyboard",
    "sections": [
      {
        "title": "Main image",
        "position": "top-left",
        "count": 8,
        "labels": [
          "{argument name=\"brand\" default=\"Wugu Mofang\"}",
          "{argument name=\"product name\" default=\"Walnut Sesame Black Bean Powder\"}",
          "32g x 10 sachets, individually packaged",
          "{argument name=\"main keyword 1\" default=\"Five Black Grains\"}",
          "{argument name=\"main keyword 2\" default=\"Rich & Mellow\"}",
          "{argument name=\"main keyword 3\" default=\"Individual Sachets\"}",
          "{argument name=\"main keyword 4\" default=\"Instant Brew\"}",
          "product box and drink cup hero composition"
        ]
      },
      {
        "title": "Details page",
        "position": "top-right",
        "count": 5,
        "labels": ["{argument name=\"ingredient 1\" default=\"Black Sesame\"}", "{argument name=\"ingredient 2\" default=\"Black Bean\"}", "{argument name=\"ingredient 3\" default=\"Black Rice\"}", "{argument name=\"ingredient 4\" default=\"Walnut\"}", "{argument name=\"ingredient 5\" default=\"Grain Powder\"}"]
      },
      {
        "title": "{argument name=\"feature title\" default=\"Rich & Smooth, Delicious Taste\"}",
        "position": "mid-right",
        "count": 4,
        "labels": [
          "{argument name=\"feature 1\" default=\"Instant Brew, Nutritious & Delicious\"}",
          "{argument name=\"feature 2\" default=\"Fine Powder\"}",
          "{argument name=\"feature 3\" default=\"Rich & Smooth\"}",
          "{argument name=\"feature 4\" default=\"Nutritious Meal Replacement\"}"
        ]
      },
      {
        "title": "{argument name=\"how to title\" default=\"Brewing Instructions HOW TO MAKE\"}",
        "position": "mid-left lower",
        "count": 3,
        "labels": [
          "{argument name=\"step 1\" default=\"1. Pour in one sachet (32g)\"}",
          "{argument name=\"step 2\" default=\"2. Add 200ml hot water or milk\"}",
          "{argument name=\"step 3\" default=\"3. Stir evenly and enjoy\"}"
        ]
      },
      {
        "title": "{argument name=\"scenario title\" default=\"A Good Cup of Grains, Easy Living\"}",
        "position": "lower-left",
        "count": 4,
        "labels": [
          "{argument name=\"scenario 1\" default=\"Energizing Breakfast\"}",
          "{argument name=\"scenario 2\" default=\"Office Afternoon Tea\"}",
          "{argument name=\"scenario 3\" default=\"Fitness Meal Replacement\"}",
          "{argument name=\"scenario 4\" default=\"Bedtime Warm Drink\"}"
        ]
      },
      {
        "title": "{argument name=\"convenience title\" default=\"Individual Sachets, Carry Anywhere\"}",
        "position": "lower-right",
        "count": 3,
        "labels": ["Individual sachets, portable & hygienic", "Locks in freshness, moisture & oxidation proof", "1 sachet = 1 cup, precise portioning"]
      },
      {
        "title": "Video Promo Ad / TVC Video Prompts + Storyboard",
        "position": "bottom full width",
        "count": 7,
        "labels": [
          "Shot 1: Opening - Product showcase",
          "Shot 2: Ingredient close-up",
          "Shot 3: Pouring powder into cup",
          "Shot 4: Brewing and stirring",
          "Shot 5: Drinking scene",
          "Shot 6: Product selling points",
          "Shot 7: Closing tagline"
        ]
      }
    ]
  },
  "scene_elements": {
    "ingredients": [
      { "name": "{argument name=\"ingredient 1\" default=\"black sesame\"}", "form": "small black seeds in a round bowl" },
      { "name": "{argument name=\"ingredient 2\" default=\"black beans\"}", "form": "glossy whole beans in a round bowl" },
      { "name": "{argument name=\"ingredient 3\" default=\"black rice\"}", "form": "dark long grains in a round bowl" },
      { "name": "{argument name=\"ingredient 4\" default=\"walnuts\"}", "form": "walnut halves in a round bowl" },
      { "name": "{argument name=\"ingredient 5\" default=\"grain powder\"}", "form": "light beige powder in a round bowl" }
    ],
    "serving": {
      "drink": "{argument name=\"drink description\" default=\"thick gray-brown sesame walnut bean beverage with smooth surface swirl\"}",
      "cup": "transparent glass cup with handle",
      "utensil": "metal spoon stirring or resting inside drink"
    },
    "supporting_props": ["walnuts on table", "scattered black beans", "grain stalks or wheat stems", "dark tabletop", "ingredient bowls", "open package showing 5 visible sachets"]
  },
  "text_treatment": {
    "headline_font": "bold elegant Chinese display type in metallic gold",
    "body_font": "clean sans serif Chinese with occasional English subtitles",
    "accent": "thin gold divider lines and circular ingredient frames"
  },
  "camera_and_composition": {
    "product_shots": "front-facing hero box, angled sachet display box, close-up beverage macro",
    "food_photography": "high-detail commercial food styling, shallow depth of field, crisp texture emphasis"
  },
  "quality": "ultra-detailed commercial design mockup, polished e-commerce key visual plus details page plus ad storyboard, 4K",
  "constraints": {
    "must_keep": [
      "5 sales modules + 1 TVC storyboard strip must all appear and be identifiable",
      "Each module has its own sub-heading + numbering or icons",
      "Packaging / product appearance is consistent across different modules",
      "Chinese copy hierarchy is clear in main title / subtitle / selling points"
    ],
    "avoid": [
      "Drawing the detail page area as pure text (must have ingredient images / icons)",
      "No visual boundaries between the 5 modules",
      "Drawing the TVC storyboard strip as a text list instead of thumbnails + annotations",
      "Stacking all copy onto the main image area so it no longer looks like a main image",
      "Ingredients / product changing packaging color in different areas"
    ]
  }
}
```

### Parameter Strategy

- **Required**: product brand + name, packaging description, 5 ingredient / component / selling point keywords
- **Defaultable**: style overall (auto by category), scenario / step / feature copy (auto template by category)
- **Random**: supporting props details, TVC 7-shot specific copy

### Auto-fill Strategy

- User only says "make an XX e-commerce detail page all-in-one" → default by food / beauty / maternity & baby auto-select dark / light / warm color scheme
- If 5 ingredients not specified → auto-list by product category (e.g., milk powder → 5 milk sources; skincare → 5 active ingredients; fitness meal replacement → 5 grains)
- If TVC shots not specified → use the template's 7-shot standard structure

## Variant 1: Light & Refreshing Beauty / Skincare Board (style swap)

📝 Prompt

```json
{
  "type": "Chinese e-commerce skincare product marketing board",
  "style_override": {
    "overall": "clean light premium beauty layout",
    "color_palette": ["off-white", "soft beige", "rose gold", "pastel pink", "champagne"],
    "lighting": "bright airy soft daylight with subtle highlights",
    "mood": "fresh, clean, hydrating, premium"
  },
  "section_replacements": {
    "ingredients_section": "5 active ingredient icons (Hyaluronic Acid / Niacinamide / Ceramide / Retinol / VC)",
    "feature_section": "4 efficacy claims (Moisturizing / Brightening / Anti-wrinkle / Repairing)",
    "scenario_section": "4 use moments (Morning / Commuting / Pre-makeup / Night Repair)",
    "how_to_section": "3-step routine (Cleansing → Apply → Massage)"
  }
}
```

### When to choose this variant

- Beauty / skincare / personal care category
- Client wants "Japanese refreshing / Korean healing" style
- No need for the "dark + gold" luxury feel of food categories

## Variant 2: Maternity & Baby / Children / Warm Color Scheme

📝 Prompt

```json
{
  "type": "Chinese e-commerce baby/child product marketing board",
  "style_override": {
    "overall": "warm friendly child-safe layout with rounded corners and soft illustrations",
    "color_palette": ["cream", "soft yellow", "baby blue", "pastel pink", "wood brown"],
    "lighting": "warm natural daylight, gentle shadows",
    "mood": "safe, gentle, healthy, trustworthy"
  },
  "extra_section": {
    "title": "Mom's Peace of Mind / Safety Certifications",
    "elements": ["EU Certified", "No additives", "0 preservatives", "Baby safe"]
  }
}
```

### When to choose this variant

- Maternity & baby / children / pregnancy product categories
- Must emphasize "safety / certifications / no additives"
- Warm colors + rounded visuals

## Variant 3: 3C / Digital / Tools Category (less text + more tech specs)

📝 Prompt

```json
{
  "type": "Chinese e-commerce 3C / digital product marketing board",
  "style_override": {
    "overall": "tech minimal dark layout with neon accents",
    "color_palette": ["matte black", "graphite", "cyan", "white"],
    "mood": "high-tech, precise, professional"
  },
  "section_replacements": {
    "ingredients_section": "spec table (CPU / RAM / Battery / Connectivity / Weight)",
    "feature_section": "4 tech feature pills with icons",
    "scenario_section": "4 user scenarios (Office / Business Travel / Creative / Gaming)",
    "how_to_section": "skip; replace with 6 product angle close-ups"
  }
}
```

### When to choose this variant

- Digital / tools / electronics products
- Client wants "less emotion + more specs + strong tech feel"

## Things to Avoid

- Squeezing all 5+1 modules into a 1:1 square image → must use 9:16 / 3:4 long image to fit everything
- Filling the main image area with text → the main image IS the main image, text belongs in the selling points area
- No visual boundaries between modules (lines / color blocks / whitespace) → the whole image becomes an unreadable blob
- Drawing the TVC storyboard strip as a pure text list → must have 7 thumbnail images + numbering + titles
- Packaging / product changing color / font across different modules → consistency is the lifeblood of this type of board
- Color palette ≥ 6 main colors → must keep to 3-4 main colors + 1 accent
- Fonts ≥ 4 types across the whole image → title + body + 1 handwritten accent is sufficient
- Letting the model "come up with 5 ingredients" when your product actually has specific ingredients → must explicitly list them in the prompt