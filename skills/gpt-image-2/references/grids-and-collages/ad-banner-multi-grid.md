# Cross-Industry Mixed Ad Banner Grid Template

This file is used to generate "a single image with N independent ad banners, each from a completely different industry / theme / style."

Typical uses:

- Ad / design agency capability demo board (showcase 4 different business directions at once)
- Public account / paid traffic material collection preview
- "What banners can AI make" self-demo
- Overseas Japanese / Korean SNS banner collage (travel / beauty / food / education mixed)
- Template library / asset collection hero image

Differences from existing `banner-grid-2x2.md`:

| Dimension | `banner-grid-2x2.md` (existing) | This template (new) |
|---|---|---|
| Theme unity | Same brand series, unified style | **Each cell has completely different industry / theme / palette** |
| Visual consistency | Shared brand colors and logo | Only shared grid + whitespace rhythm |
| Use case | Course / SNS ad set of four | Agency demo / collage asset set / multi-scene showcase |

## Scope

- 4 / 6 / 9 cell independent ad banner collage
- Multi-industry demo board (travel / beauty / food / education / finance / tech...)
- Multi-platform paid traffic material one-image preview
- Designer capability portfolio hero image

## When to use

- User mentions "four different industry banners / multi-theme ad group / make one each"
- User wants "one image covering N banners with completely different themes"
- User is making an agency proposal / template example image

Do NOT use for:

- Same brand 4 extended banners → use `grids-and-collages/banner-grid-2x2.md`
- One complete large banner → use `poster-and-campaigns/banner-hero.md`
- Style-mixed same-subject variations → use `grids-and-collages/mixed-style-multi-panel.md`
- Same business multi-day content (lookbook / schedule) → use `grids-and-collages/lookbook-grid.md`

## Missing Information Priority Question Order

1. Grid spec (2x2 / 2x3 / 3x3)
2. Theme / industry per cell (user provides list or lets you randomize)
3. Language (Japanese / Chinese / English / multi-language mix)
4. Whether readable real prices / discounts / copy needed
5. Whether each cell needs a "main character" or just product / text
6. Subject source: random generation / consistent model / user-provided reference

If user says "you decide": keep the language question, auto-generate 4 high-variance industries for the rest.

## Main Template: NxM Cross-Industry Ad Banner Demo Board

Description

Divide the canvas equally into NxM cells, each cell with independent composition, theme, and type size hierarchy, as if 4 finished banners were pasted into one image.

Prompt

```json
{
  "type": "{argument name=\"grid spec\" default=\"2x2\"} grid of independent advertisement banners",
  "goal": "Generate a high-density ad demo board where each cell is an independently croppable finished banner, for showcasing visual capabilities across different industries",
  "language": "{argument name=\"language\" default=\"Japanese\"}",
  "layout": {
    "structure": "{argument name=\"panel count\" default=\"4\"} equal quadrants",
    "gutter": "{argument name=\"gutter\" default=\"6px white divider\"}",
    "overall_aspect_ratio": "{argument name=\"overall ratio\" default=\"1:1\"}",
    "panel_aspect_ratio": "{argument name=\"panel ratio\" default=\"1:1\"}",
    "quadrants": [
      {
        "position": "top-left",
        "theme": "{argument name=\"theme 1\" default=\"Travel\"}",
        "subject": "{argument name=\"subject 1\" default=\"A couple holding hands on a white sand beach with turquoise ocean and bright blue sky\"}",
        "elements": ["{argument name=\"deco 1\" default=\"red hibiscus flower in bottom-left corner\"}"],
        "text_labels": [
          "{argument name=\"text 1a\" default=\"This year, set yourself free.\"}",
          "{argument name=\"text 1b\" default=\"Okinawa Trip\"}",
          "{argument name=\"text 1c\" default=\"3-day healing journey\"}",
          "{argument name=\"text 1d\" default=\"Flight + Hotel\"}",
          "{argument name=\"price 1\" default=\"39,800 yen~\"}",
          "{argument name=\"text 1e\" default=\"Stunning views, gourmet food, experiences all fulfilled!\"}"
        ],
        "icons": { "count": 3, "descriptions": ["airplane", "hotel building", "car"] },
        "color_palette": "{argument name=\"palette 1\" default=\"sky blue, turquoise, sand cream, accent red\"}"
      },
      {
        "position": "top-right",
        "theme": "{argument name=\"theme 2\" default=\"Skincare\"}",
        "subject": "{argument name=\"subject 2\" default=\"Close-up of a young woman with dewy glowing skin, eyes closed\"}",
        "elements": [
          "{argument name=\"deco 2a\" default=\"soft pink gradient background\"}",
          "{argument name=\"deco 2b\" default=\"dynamic water splash effects\"}",
          "{argument name=\"product 2\" default=\"pink cosmetic jar labeled 'LUMIERE Brightening Gel'\"}"
        ],
        "text_labels": [
          "Say goodbye to pores and dullness!",
          "Full of translucency",
          "To glowing dewy skin",
          "New sensation skincare",
          "{argument name=\"discount 2\" default=\"First-time limited 78% OFF\"}",
          "{argument name=\"price 2\" default=\"1,980 yen\"}"
        ],
        "badges": { "count": 3, "style": "gold circular", "labels": ["Pore Care", "High Moisture", "Firmness & Glow"] },
        "color_palette": "blush pink, ivory, soft gold accent"
      },
      {
        "position": "bottom-left",
        "theme": "{argument name=\"theme 3\" default=\"Gourmet Food\"}",
        "subject": "{argument name=\"subject 3\" default=\"Thick medium-rare steak sizzling on a dark grill plate\"}",
        "elements": ["garlic chips", "rosemary sprig", "dark background with smoke and glowing embers"],
        "text_labels": [
          "Melt-in-your-mouth delicious!",
          "{argument name=\"food 3\" default=\"Kuroge Wagyu\"}",
          "Luxury Steak",
          "Limited Time / Special Price",
          "{argument name=\"original price 3\" default=\"Regular price 8,980 yen\"}",
          "{argument name=\"sale price 3\" default=\"4,980 yen\"}"
        ],
        "badges": { "count": 1, "style": "red circular", "labels": ["A4 A5 Grade"] },
        "color_palette": "deep brown, charcoal black, amber, accent crimson"
      },
      {
        "position": "bottom-right",
        "theme": "{argument name=\"theme 4\" default=\"Online Education\"}",
        "subject": "{argument name=\"subject 4\" default=\"Young man in blue shirt studying at desk, writing in notebook beside open laptop\"}",
        "elements": ["bright indoor lighting", "minimal desk environment"],
        "text_labels": [
          "In your spare moments",
          "{argument name=\"goal 4\" default=\"Pass in the shortest time!\"}",
          "Online Certification Course",
          "Complete on your phone",
          "Efficient learning makes the difference!",
          "{argument name=\"discount 4\" default=\"Only now! 20% OFF tuition\"}"
        ],
        "badges": { "count": 1, "style": "blue circular", "labels": ["100,000 students surpassed!"] },
        "icons": { "count": 2, "descriptions": ["smartphone", "open book"] },
        "color_palette": "sky blue, white, energetic yellow accent"
      }
    ]
  },
  "global_style": {
    "rendering": "real ad-grade composition per panel; each panel must look like a finished standalone banner",
    "typography": "bold sans-serif headline + smaller subhead per panel; multi-weight hierarchy",
    "layering": "subject photo + clear text overlay + small badge / icon ornaments",
    "lighting": "panel-appropriate (sunny travel, dewy beauty, smoky food, bright office)"
  },
  "constraints": {
    "must_keep": [
      "Each cell looks like an independently croppable finished banner (not a simple collage)",
      "Type size hierarchy is clear within each cell (headline ≫ subhead ≫ price/CTA)",
      "Cells do not spill into each other"
    ],
    "avoid": [
      "All cells reuse the same palette / same model",
      "Text blurry and unreadable",
      "Unbalanced whitespace ratio per cell",
      "Forcing all logos / brands to be the same brand"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: grid spec, language, each theme (or confirm random)
- **Can default**: text_labels (auto-fill copy based on theme), color_palette (recommend based on theme)
- **Can randomize**: subject description, price numbers, badge copy

### Auto-Fill Strategy

- User only says "make 4 banners for different industries" → default travel / beauty / food / education combo (validated by Case 90)
- User provides industry list but no copy → auto-write headline / price / badge based on industry semantics
- User specifies language → all panels must use the same language (unless explicitly saying "mixed language")

## Variant 1: 3x3 Nine-Cell Industry Panorama Demo Board

Prompt

```json
{
  "type": "3x3 grid of advertisement banners across 9 industries",
  "language": "{argument name=\"language\" default=\"Japanese\"}",
  "layout": {
    "structure": "9 equal cells",
    "industries": [
      "Travel", "Skincare", "Gourmet Food",
      "Online Education", "Fashion", "Finance",
      "Mobile Game", "Real Estate", "Healthcare"
    ]
  },
  "per_cell_required_elements": [
    "industry-appropriate hero subject",
    "1 large headline",
    "1 sub-line",
    "1 price or CTA strip",
    "1 small badge or icon row"
  ],
  "global_style": {
    "rendering": "uniform crisp print quality across all 9 cells",
    "color_diversity": "must use 9 visibly different palettes so cells don't blend",
    "negative_space": "each cell ~12% padding"
  }
}
```

### When to choose this variant

- User says "make 9 banners for completely different industries"
- Designer is making a universal template demo page
- Want to post directly to Behance / Dribbble portfolio cover

## Variant 2: Mobile Vertical 2x4 Paid Traffic Material Set

Prompt

```json
{
  "type": "2x4 vertical mobile ad placement preview",
  "panel_aspect_ratio": "9:16",
  "overall_aspect_ratio": "9:16 collage of 8 mini portrait banners",
  "use_case": "Pinterest / TikTok / Reels / Moments feed ad effect preview",
  "per_cell_required_elements": [
    "vertical hero photo or illustration",
    "top-aligned headline",
    "bottom-aligned CTA pill",
    "small brand watermark"
  ],
  "constraints": {
    "must_keep": [
      "Vertical composition safe zones (leave 12% at top / bottom for platform UI)",
      "8 panels have clearly different industries"
    ]
  }
}
```

### When to choose this variant

- User is making paid traffic material demo
- Making mobile ad effect preview image
- Showing client "same campaign with multiple industry angles"

## Things to Avoid

- Forcing 4 cells to use the same model (becomes a lookbook instead of multi-industry demo)
- All panels sharing the same palette → loses the visual tension of "cross-industry"
- Copy too long causing hierarchy collapse within a panel (headline should be readable within 1/3-1/2 of the panel height)
- Writing "argument" from the template into the final prompt (do parameter substitution first or keep default)
- When mixing languages, not specifying which panel uses which language → model will confuse everything
- Panel count exceeding 9 → per-cell detail will collapse in a single image, better to split into two images