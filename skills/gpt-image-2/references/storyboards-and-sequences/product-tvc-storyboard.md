# Product TVC Commercial Storyboard Board Template

This file is used to generate "storyboards with a single product as the protagonist, across 9-12 commercial ad shots in realistic photography style", where each panel is a visual representation of a real camera shot.

Typical uses:

- Pre-shoot storyboard proposals for ad / TVC agencies
- E-commerce detail page "we can produce this quality of video" pre-visualization drafts
- Shot list references for video generation tools like Seedance / Sora / Runway
- Pre-client-approval video script visualization
- E-commerce "main image → TVC" one-image quick approval

Features (distinguishing from existing storyboard templates):

| Template | Nature | Style |
|---|---|---|
| `four-panel-comic.md` (existing) | 4-panel manga | Manga / gag / reversal |
| `manga-spread-page.md` (existing) | Manga spread panels | Japanese manga / irregular panels |
| `recipe-process-flowchart.md` (existing) | Process diagram | Recipe / tutorial illustration |
| **This template** (new) | **Real-shot storyboard** | **Commercial ad photography** |

**Core distinction**: This template's each panel is a "real photography / photorealistic render" finished frame, not manga panels or flowcharts, but the visual answer to "what will this 15-second ad look like when shot".

## Scope

- Pre-shoot TVC storyboards
- E-commerce detail page video shoot pre-visualization
- Client review ("what the finished product will roughly look like")
- Shot list references for video generation models (Sora / Seedance / Runway)
- Auto / beauty / food / electronics category 15-30 second ad storyboards

## When to Use

- User mentions "TVC / ad storyboard / storyboard / video script visualization"
- User already has a product, wants a visual proposal for "what the finished video looks like"
- Client wants to see "what each of the 9 / 12 shots will capture"

Do NOT use for:

- Manga / story 4-panels → use `four-panel-comic.md`
- Irregular manga spread → use `manga-spread-page.md`
- Recipe / tutorial process → use `recipe-process-flowchart.md`
- Single hero main image → use `product-visuals/premium-studio-product.md`
- Detail page all-in-one sales dashboard → use `product-visuals/ecommerce-marketing-board.md`

## Missing Information Priority Question Order

1. Product (must have a specific product / packaging / color / shape)
2. Video duration (15s / 30s / 60s) + aspect ratio (9:16 vertical / 16:9 horizontal / 1:1)
3. Total shot count (9 / 12 / 6)
4. Style (**cinematic / minimalist premium / warm lifestyle / cool tech / retro nostalgic**)
5. Whether "hands / actors" need to appear
6. Must-appear selling points (determines which shot is close-up and which is lifestyle)
7. Whether bilingual shot titles / timecodes are needed

## Main Template: 9-Panel Product TVC Commercial Storyboard Board

📖 Description

3×3 = 9 panels, each panel is an independent shot's finished visual representation, overall with header (program main title + duration + aspect ratio) + each panel's Chinese shot title + timecode + shooting notes.

📝 Prompt

```json
{
  "type": "product TVC storyboard board",
  "goal": "Generate a 9-panel storyboard image, each panel is a real camera shot visual representation for the product's commercial ad, usable as pre-shoot storyboard / client review / video generation reference",
  "input_mode": "{argument name=\"input mode\" default=\"text-only\"}",
  "reference_image_note": "If user provides product reference image, must keep product appearance completely identical (color / packaging / logo must not drift)",
  "header": {
    "title": "{argument name=\"header title\" default=\"Product TVC Storyboard Script\"}",
    "subtitle_meta": "{argument name=\"video duration\" default=\"15 seconds\"} / {argument name=\"aspect ratio\" default=\"9:16 vertical\"} / 9-grid",
    "product_name_subtitle": "{argument name=\"product name\" default=\"Blue Porcelain Ashtray\"}"
  },
  "layout": {
    "format": "{argument name=\"board orientation\" default=\"vertical 3:4 storyboard sheet\"}",
    "background": "{argument name=\"board background\" default=\"dark elegant gradient with subtle paper texture\"}",
    "grid": {
      "rows": 3,
      "columns": 3,
      "panel_count": 9,
      "panel_aspect_ratio": "{argument name=\"panel ratio\" default=\"9:16 (vertical TVC)\"}",
      "panel_borders": "thin light divider, generous gutter",
      "panel_label_position": "top-left number badge + scene title in Chinese; small timestamp top-right; small Chinese description below the image"
    }
  },
  "scenes": {
    "count": 9,
    "items": [
      { "id": 1, "title_zh": "{argument name=\"scene 1 title\" default=\"Environment Establishing\"}", "timestamp": "0-2s", "description": "environment-establishing wide shot with desk, books, window, and the product placed in context; soft morning light" },
      { "id": 2, "title_zh": "{argument name=\"scene 2 title\" default=\"Hero Reveal\"}", "timestamp": "2-3s", "description": "hero product medium shot on the table; warm rim light, shallow depth of field" },
      { "id": 3, "title_zh": "{argument name=\"scene 3 title\" default=\"Craftsmanship Close-up\"}", "timestamp": "3-5s", "description": "extreme close-up of the {argument name=\"signature detail\" default=\"blue floral craftsmanship pattern\"}" },
      { "id": 4, "title_zh": "{argument name=\"scene 4 title\" default=\"Usage Scene\"}", "timestamp": "5-7s", "description": "use case showing {argument name=\"use action\" default=\"a hand placing a cigarette into the ashtray with visible smoke\"}" },
      { "id": 5, "title_zh": "{argument name=\"scene 5 title\" default=\"Feature Display\"}", "timestamp": "7-8s", "description": "{argument name=\"function shot\" default=\"top-down capacity display showing multiple cigarette butts inside\"}" },
      { "id": 6, "title_zh": "{argument name=\"scene 6 title\" default=\"Cleaning & Care\"}", "timestamp": "8-10s", "description": "{argument name=\"care shot\" default=\"cleaning scene under running water in a sink with a hand holding the product\"}" },
      { "id": 7, "title_zh": "{argument name=\"scene 7 title\" default=\"Detail Quality\"}", "timestamp": "10-11s", "description": "{argument name=\"quality detail\" default=\"bottom-detail close-up showing the underside and anti-slip pads\"}" },
      { "id": 8, "title_zh": "{argument name=\"scene 8 title\" default=\"Mood Lifestyle\"}", "timestamp": "11-13s", "description": "{argument name=\"mood scene\" default=\"mood/lifestyle scene at night with the product on a desk, smoke rising, and ambient lamp light\"}" },
      { "id": 9, "title_zh": "{argument name=\"scene 9 title\" default=\"Brand Closing\"}", "timestamp": "13-15s", "description": "brand closing frame with the product as the hero plus Chinese marketing text '{argument name=\"closing tagline\" default=\"Craftsmanship Heritage, Refined Living\"}'" }
    ]
  },
  "global_style": {
    "rendering": "premium realistic commercial photography across all 9 panels",
    "consistency": "the product (color / shape / packaging / logo) stays IDENTICAL across all 9 panels",
    "lighting": "{argument name=\"lighting style\" default=\"warm premium lighting, shallow depth of field, refined lifestyle desktop environment\"}",
    "color_grading": "{argument name=\"color grading\" default=\"warm cinematic\"}",
    "panel_treatment": "each panel feels like a real ad still, not a sketch or wireframe"
  },
  "constraints": {
    "must_keep": [
      "9 shots numbered clearly, timecodes increasing without overlap (total = video duration)",
      "product appearance completely identical across 9 shots",
      "each panel must have Chinese shot title + timecode + description",
      "overall looks like a professional ad storyboard board, not 9 random images"
    ],
    "avoid": [
      "9 shots all same angle (must mix close-up / medium / wide / overhead / low angle)",
      "shot descriptions mismatched with product type (e.g. 'pouring powder into cup' shot for a phone)",
      "product changing color or appearance across shots",
      "timecode total inconsistent with video duration",
      "no closing shot (last panel must be brand closing)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: product name, video duration + aspect ratio, product reference image (if available)
- **Can default**: board background, closing tagline, lighting style
- **Can randomize**: scene 1-9 specific descriptions (apply template by product category)

### Auto-Complete Strategy

- User only says "make a 9-panel TVC storyboard for my product" + provides reference image → auto-apply 9-shot template by product category
- No specific shot content specified → use standard structure: "environment establishing → hero reveal → craftsmanship → usage → feature → cleaning/care → detail → mood → closing"
- No duration specified → default 15s 9 panels

## Variant 1: 12-Panel 30-Second Extended Version

📝 Prompt

```json
{
  "type": "12-panel 30s product TVC storyboard",
  "header": {
    "subtitle_meta": "30 seconds / {argument name=\"aspect ratio\" default=\"16:9 horizontal\"} / 12-grid"
  },
  "layout": { "rows": 3, "columns": 4, "panel_count": 12 },
  "scenes_extension": [
    "10) user testimonial / usage witness shot",
    "11) data / comparison / certification shot",
    "12) second brand closing + CTA"
  ],
  "use_case": "30s TVC / detail page long video / complete product story"
}
```

### When to Choose This Variant

- Video duration ≥ 30s
- Need "user witness + data comparison + CTA" for more complete sales flow
- Horizontal playback channels (YouTube / Bilibili / detail page banner video)

## Variant 2: 6-Panel Minimal Short Video Version (Suitable for 15s short-form platforms)

📝 Prompt

```json
{
  "type": "6-panel 15s vertical short video storyboard",
  "header": {
    "subtitle_meta": "15 seconds / 9:16 vertical / 6-grid"
  },
  "layout": { "rows": 2, "columns": 3, "panel_count": 6 },
  "scenes": [
    "1 hook / pain point opening",
    "2 product reveal",
    "3 one core selling point close-up",
    "4 usage moment",
    "5 effect / comparison",
    "6 brand + CTA"
  ],
  "use_case": "Douyin / Kuaishou / TikTok / Reels 15s short video"
}
```

### When to Choose This Variant

- Platform limit 15s or less
- Primarily going for "hook + selling point + conversion" fast-paced short video
- 6 shots = ~2.5s per shot average, direct and easy to understand

## Variant 3: Cinematic Narrative TVC (Premium Categories)

📝 Prompt

```json
{
  "type": "cinematic-narrative TVC storyboard",
  "header": {
    "subtitle_meta": "{argument name=\"video duration\" default=\"60 seconds\"} / 16:9 widescreen / 9-grid"
  },
  "scenes_replacement": [
    "1 protagonist entrance / situation introduction",
    "2 conflict / dilemma",
    "3 turning point / product reveal",
    "4 interaction / experience",
    "5 highlight moment",
    "6 emotional release",
    "7 group scene / resonance",
    "8 brand philosophy statement",
    "9 logo + slogan static frame"
  ],
  "style_override": {
    "lighting": "cinematic lighting, strong contrast, rich atmosphere",
    "color_grading": "retro / Tiffany / desert orange / black-and-white specific tone",
    "talent": "real actors + emotional facial expressions"
  }
}
```

### When to Choose This Variant

- Automotive / luxury / premium appliances / global brands
- Going for "story + emotion + philosophy" rather than "selling points + data"
- 60s+ extended brand film

## Things to Avoid

- 9 shots all product close-up → must have shot rhythm (wide / medium / close / extreme close / overhead / low angle)
- Product changing color / shape across shots → critical error, must emphasize "identical product"
- Shot descriptions mismatched with product category (e.g. "faucet rinse" shot for lipstick)
- Timecode total not equal to video total duration → client will immediately see this as unprofessional
- Missing brand closing shot (last panel must be logo + slogan / CTA)
- Drawing 9 panels in manga / illustration style → should be realistic photography feel
- Board missing header (title + duration + aspect ratio) → looks like 9 random images
- Leaving "argument" placeholders in the final prompt