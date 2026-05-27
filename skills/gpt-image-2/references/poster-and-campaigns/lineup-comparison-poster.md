# Product Lineup / Model Comparison Infographic Poster Template

This file is used to generate "luxury catalog-style infographic posters featuring a single brand's full product line / full model range / full SKU lineup, arranged by tier / series / category in rows, with legend / icon key / spec chart."

Typical uses:

- Musical instrument brand full lineup poster (PRS / Fender / Gibson / Boss...)
- Automotive brand model lineage poster (Porsche / Audi / Ford...)
- Watch / lens / pen / premium hardware category series comparison
- Collector-grade poster / museum-grade brand tribute image
- Annual catalog or anniversary poster
- Dealership showroom wall hanging

Features (comparison with existing poster / infographic templates):

| Template | Use Case |
|---|---|
| `infographics/comparison-infographic.md` (existing) | A vs B / plan tier / misconception comparison (≤ 6 items) |
| `infographics/legend-heavy-infographic.md` (existing) | High-density educational / causal chain / evolution (not emphasizing product lineup) |
| **This template** (new) | **30+ SKUs displayed simultaneously, arranged in tier × series matrix with legends** |

**Core feature**: 30-50 product thumbnails simultaneously visible, using tier key + icon legend + tonal chart to let readers instantly understand "which model should I buy."

## Scope

- Single brand 30+ SKU lineup tribute poster
- Dealership showroom hanging poster / collector poster
- Annual catalog one-page overview
- Anniversary / memorial poster
- B2B pitch "how many SKUs we have" showcase

## When to Use

- User mentions "full lineup / full product lineage / full model range / collector poster / catalog one-page"
- Single brand product count ≥ 20
- User wants to emphasize "brand history / product line breadth / choice abundance"

Do NOT use:

- ≤ 6 product comparison → use `infographics/comparison-infographic.md`
- Single product multi-angle → use `product-visuals/exploded-view-poster.md`
- Single product premium studio image → use `product-visuals/premium-studio-product.md`
- Multi-brand mixed comparison → not applicable (this template emphasizes single brand)

## Missing Information Priority Questions

1. Brand name + category (PRS guitars / Porsche cars / Montblanc pens...)
2. Total SKU count (20-50 recommended, over 60 causes cell collapse)
3. Row grouping basis (tier level / series / era / price...)
4. Whether icon key / tonal key / spec key is needed (affects number of top legends)
5. Color scheme base (**dark luxury / white minimal / vintage sand gold**)
6. Aspect ratio (default 3:4 portrait)
7. Whether to include brand signature / seal / stamp decoration

## Main Template: Luxury Lineup Comparison Infographic Poster

📖 Description

Vertical poster with header (main title + subtitle + signature + dual seals) + 3 legend keys at top + 6-8 rows of product matrix in the middle (rows by tier), each row with tier label on the left and 6-7 product cards on the right.

📝 Prompt

```json
{
  "type": "luxury vintage lineup comparison infographic poster",
  "goal": "Generate a luxury catalog-style brand full product line comparison poster with 30+ SKUs displayed simultaneously, with tier / icon / style legends",
  "subject": "{argument name=\"subject description\" default=\"a highly detailed, vertically oriented PRS electric guitar lineup chart designed like a premium museum poster or collector's reference board\"}",
  "style": {
    "overall": "{argument name=\"overall style\" default=\"ornate, dark, glossy, high-contrast, gold-foil typography, elegant wood-and-metal textures, symmetrical grid layout, premium catalog aesthetic, subtle vintage patina, ultra sharp graphic design\"}"
  },
  "branding": {
    "main_headline": "{argument name=\"main headline\" default=\"THE LEGENDARY LINEAGE OF PRS GUITARS\"}",
    "subheadline": "{argument name=\"subheadline\" default=\"EVERY ICON. EVERY LINE. ONE HERITAGE.\"}",
    "signature": "{argument name=\"signature\" default=\"Paul Reed Smith\"}",
    "left_seal": "{argument name=\"left seal\" default=\"PAUL REED SMITH GUITARS\"}",
    "right_seal": "{argument name=\"right seal\" default=\"MADE IN MARYLAND U.S.A.\"}"
  },
  "palette": {
    "background": "{argument name=\"background palette\" default=\"black and deep charcoal with dark figured wood accents\"}",
    "primary": "{argument name=\"primary color\" default=\"antique gold\"}",
    "secondary": "{argument name=\"secondary color\" default=\"cream\"}",
    "accent_colors": ["deep green", "teal", "royal blue", "purple", "gold", "burgundy"]
  },
  "layout": {
    "format": "{argument name=\"format\" default=\"single-page vertical poster\"}",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4 portrait\"}",
    "header": {
      "position": "top",
      "elements": [
        "large central title",
        "small tagline below",
        "script signature",
        "2 circular emblems in upper left and upper right",
        "{argument name=\"legend count\" default=\"3\"} horizontal legend boxes under the title"
      ]
    },
    "sections": [
      {
        "title": "{argument name=\"key 1 title\" default=\"PRESTIGE TIER KEY\"}",
        "position": "upper left below title",
        "count": 6,
        "labels": ["{argument name=\"tier 1\" default=\"SE\"}", "{argument name=\"tier 2\" default=\"S2\"}", "{argument name=\"tier 3\" default=\"CE\"}", "{argument name=\"tier 4\" default=\"CORE\"}", "{argument name=\"tier 5\" default=\"WOOD LIBRARY\"}", "{argument name=\"tier 6\" default=\"PRIVATE STOCK\"}"]
      },
      {
        "title": "{argument name=\"key 2 title\" default=\"PICKUP ICON KEY\"}",
        "position": "upper center-right below title",
        "count": 7,
        "labels": ["HH", "HSH", "P-90", "SOAP", "58/15", "TCI", "Bass"]
      },
      {
        "title": "{argument name=\"key 3 title\" default=\"TONAL CHARACTER KEY\"}",
        "position": "upper right below title",
        "count": 7,
        "labels": ["Warm / Vintage", "Balanced / All-around", "Bright / Articulate", "High Gain / Modern", "Blues / Classic Rock", "Metal / Progressive", "Funk / Soul / Clean"]
      },
      {
        "title": "{argument name=\"row 1 label\" default=\"CORE\"}",
        "position": "first main row left label",
        "count": 7,
        "labels": ["{argument name=\"row 1 model 1\" default=\"Custom 24\"}", "McCarty 594", "DGT (David Grissom)", "Custom 22", "Hollowbody II", "SC 594", "row category panel"]
      },
      {
        "title": "{argument name=\"row 2 label\" default=\"S2\"}",
        "position": "second main row left label",
        "count": 6,
        "labels": ["S2 Custom 24", "S2 McCarty 594", "S2 Standard 24", "S2 Vela", "S2 Singlecut", "S2 Mira"]
      },
      {
        "title": "{argument name=\"row 3 label\" default=\"SE\"}",
        "position": "third main row left label",
        "count": 6,
        "labels": ["SE Custom 24", "SE Standard 24", "SE Paul's Guitar", "SE Santana", "SE Hollowbody II", "SE Mark Holcomb"]
      },
      {
        "title": "{argument name=\"row 4 label\" default=\"CE\"}",
        "position": "fourth main row left label",
        "count": 6,
        "labels": ["CE 24", "CE 22", "CE 24 Semi-Hollow", "CE 24 Floyd", "CE 24 Satin", "CE Bass"]
      },
      {
        "title": "{argument name=\"row 5 label\" default=\"BOLT-ON SERIES\"}",
        "position": "fifth main row left label",
        "count": 6,
        "labels": ["NF 53", "Silver Sky", "NF 3", "NF 53 Satin", "DGT Bolt-On", "Studio"]
      },
      {
        "title": "{argument name=\"row 6 label\" default=\"PRIVATE STOCK\"}",
        "position": "sixth main row left label",
        "count": 6,
        "labels": ["Dragon I", "Frostbite", "#4004", "The Tree of Life", "#8731", "PS DGT"]
      }
    ],
    "footer": {
      "position": "bottom",
      "elements": ["small badge at lower left", "centered company line", "right-side script signature"]
    }
  },
  "content_grid": {
    "total_models_shown": "{argument name=\"total model count\" default=\"37\"}",
    "card_design": "{argument name=\"card design\" default=\"each product card contains a guitar render, model name, year, small pickup icons, a short descriptive blurb, and origin/wood specs at the bottom\"}",
    "row_side_panels": 6
  },
  "visual_details": {
    "products": "{argument name=\"product description\" default=\"front-facing electric guitars with varied body shapes and highly polished figured maple tops, metallic and transparent finishes, some solid colors, some natural wood\"}",
    "typography": "all caps serif headlines, small serif body text, script signature accents",
    "borders": "thin decorative gold rules around every panel and the full poster",
    "lighting": "studio-lit products against dark panel backgrounds",
    "render_quality": "clean infographic precision with realistic product renders"
  },
  "camera": "straight-on flat poster view, no perspective distortion, centered composition",
  "quality": "ultra detailed, print-ready, high-resolution editorial infographic, luxury brand poster",
  "constraints": {
    "must_keep": [
      "30+ product thumbnails must be readable with unified orientation (same view angle)",
      "Tier row left labels clear",
      "Top 3 keys (tier / pickup / tonal) must correspond to small icons on product cards",
      "Signature / seals / main title / subtitle must all appear",
      "Overall consistent dark + gold / sand-white color scheme"
    ],
    "avoid": [
      "Product orientation inconsistent (one front-facing, one 45°, one low angle)",
      "Labels misaligned causing rows to not look like a catalog",
      "30+ products squeezed into 1:1 square → must be vertical 3:4 or longer",
      "Colors exceeding 4 main + 6 accent colors",
      "Product names misspelled (lineup poster core is product names, must be correct)"
    ]
  }
}
```

### Parameter Strategy

- **Required**: brand name, product category, 6 tier names + product name list per row
- **Defaultable**: overall style (auto by category), palette, aspect ratio
- **Random**: description blurb (auto by product), spec text on cards

### Auto-fill Strategy

- User provides "PRS guitar full lineup" → use template default 6 rows × 6-7 SKU structure
- User provides "car brand" + a few models → auto-arrange by "sedan / SUV / sports / EV" rows
- Legend count not specified → default 3 (tier / core spec / character)

## Variant 1: Light Minimal Edition (suitable for tech / design brands)

📝 Prompt

```json
{
  "type": "minimal lineup comparison poster, light edition",
  "style_override": {
    "overall": "clean white / light gray background, thin sans-serif typography, no gold foil, no ornate borders, only thin hairlines",
    "palette": "off-white background, soft gray dividers, single accent color from brand (e.g. orange / blue / green)"
  },
  "use_case": "Apple / Tesla / Bose / design-driven brands"
}
```

### When to choose this variant

- Tech / design brands (not suited for luxury gold foil)
- Want minimalist / modern feel
- Single accent with strong contrast

## Variant 2: Horizontal Timeline Lineage Edition (rows by era)

📝 Prompt

```json
{
  "type": "horizontal lineup chronology poster",
  "format_override": "horizontal poster, 16:9 or 21:9",
  "row_grouping_by": "decade (1950s / 60s / 70s / 80s / 90s / 2000s / 2010s / 2020s)",
  "use_case": "Brand anniversary poster / evolution history"
}
```

### When to choose this variant

- Brand anniversary / history poster
- Want to emphasize "timeline + evolution" rather than "tier + selection"
- Horizontal display (exhibition / showroom wall)

## Variant 3: 3-Tier Comparison Table (suitable for fewer SKUs / entry-flagship comparison)

📝 Prompt

```json
{
  "type": "3-tier lineup comparison table poster",
  "row_count": 3,
  "rows": ["BASIC / Entry", "PRO / Advanced", "ULTRA / Flagship"],
  "columns_per_row": 4,
  "extra_columns": ["spec table per tier with checkmarks / dashes"],
  "use_case": "New product launch / price segment comparison / B2C buying guide"
}
```

### When to choose this variant

- SKU count ≤ 12
- User needs "performance comparison" more than "lineup panorama"
- Suitable for website / landing page / sales collateral

## Things to Avoid

- 30+ SKUs squeezed into 1:1 square → must be vertical long or horizontal wide format
- Product direction / view angle inconsistent → catalog feel immediately collapses
- Tier label using same font size as body text → rows cannot be quickly identified
- Legend keys not matching icons on product thumbnails (legend becomes useless)
- Uneven spacing between product thumbnails → visual clutter
- Product names misspelled (catalog poster core information)
- Color palette ≥ 6 main colors (should be limited to 1 main background + 1 main text color + 1 accent + at most 6 row accent colors)
- Keeping "PRS Guitars" from the template when your brand is not PRS → must replace brand name and all product names
