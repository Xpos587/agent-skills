# Bento Grid / Modular Infographic Template

This file is used for generating "bento grid / Bento grid / high-density modular" infographics:

- Xiaohongshu "high-density information mega-image" (pitfall guides / complete guides / multi-dimensional reviews)
- WeChat official account / Notion-style knowledge cards
- Product feature overview diagrams
- Multi-dimensional reviews / multi-SKU comparison one-page flow
- Year-end summaries / quarterly review dashboards

Characteristics:

- Composed of 6-9 rectangular modules of varying sizes (like Apple iOS widget layout)
- Each module independently carries one information unit (a data set / a screenshot / a key point)
- Large modules serve as visual anchors, small modules supplement details
- Unified rounded corners within modules, restrained whitespace, high information density
- Unified color scheme overall, using color blocks to distinguish module functions

## Scope

- High-density knowledge / tips / guide diagrams
- Multi-module product introduction diagrams
- Multi-dimensional review diagrams
- Annual / quarterly review diagrams
- Notion / dashboard-style visuals

## When to use

- User mentions "bento / bento grid / widget / modular / high-density info mega-image / one-page flow / dense diagram / Notion style"
- User wants "one image to explain multiple dimensions clearly"
- User wants the visual to look like Apple Newsroom / iOS widget / Notion dashboard

Do NOT use for:

- User wants a single-subject infographic → use `infographics/legend-heavy-infographic.md`
- User wants hand-drawn / notebook style → use `infographics/hand-drawn-infographic.md`
- User wants step-by-step process → use `infographics/step-by-step-infographic.md`
- User wants technical architecture diagram → use `technical-diagrams/system-architecture.md`

## Missing Information Priority Question Order

1. Topic (expressible in one sentence, e.g. "8 best domestic cameras worth buying in 2026")
2. Module count (6 / 8 / 9, recommend 8)
3. Main title + subtitle
4. Color tone (minimalist black-white / Morandi / Apple light gray / dark tech / warm)
5. Aspect ratio (Xiaohongshu 3:4 / WeChat 16:9 / 1:1)
6. Whether a "recommended / TOP 1" especially prominent large module is needed

## Main Template: Bento Grid High-Density Infographic

Description

One image divided into 6-9 rounded rectangular modules of varying sizes, overall resembling an iOS widget screen layout, each module carrying an independent information unit.

Prompt

```json
{
  "type": "Bento grid high-density modular infographic",
  "goal": "Generate a multi-module infographic that looks like Apple newsroom / iOS widget / Notion dashboard, explaining multiple dimensions in one image",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"3:4 portrait\"}",
    "background": "{argument name=\"background\" default=\"warm off-white #F5F2EC\"}",
    "global_corner_radius": "{argument name=\"global_corner_radius\" default=\"24px\"}",
    "module_gap": "{argument name=\"module_gap\" default=\"16px\"}"
  },
  "header": {
    "main_title": "{argument name=\"main_title\" default=\"8 Best Domestic Cameras Worth Buying in 2026\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"Full-frame / APS-C / Video-oriented / Retro cameras all-in-one guide\"}",
    "title_position": "top-left, large bold sans-serif"
  },
  "palette": {
    "primary": "{argument name=\"primary\" default=\"deep ink #1A1A1A\"}",
    "accent": "{argument name=\"accent\" default=\"vermilion #E94B3C\"}",
    "module_tints": [
      "soft sand #EBE3D5",
      "muted sage #C7D3C0",
      "dusty blue #B4C5D6",
      "warm peach #F2D4C4"
    ],
    "rule": "module backgrounds rotate among the tints; primary used for text; accent used at most twice"
  },
  "layout": {
    "style": "{argument name=\"layout_style\" default=\"asymmetric bento\"}",
    "module_count": "{argument name=\"module_count\" default=\"8\"}",
    "grid": "irregular: 1 hero module (large, 2x2 footprint) + 4-7 supporting modules of mixed 1x1 / 1x2 / 2x1 sizes",
    "alignment": "all modules share the same corner radius and gap; module edges align to an invisible grid"
  },
  "modules": [
    {
      "id": "M1-hero",
      "size": "large (2x2)",
      "role": "TOP 1 / Top Recommendation",
      "content": "Cover-grade showcase: large image + recommendation reason + ★★★★★ rating + brief spec"
    },
    {
      "id": "M2",
      "size": "medium (1x2)",
      "role": "Comparison Dimension 1",
      "content": "e.g. 'Weight Comparison': bar chart + number labels + highlight the winner item"
    },
    {
      "id": "M3",
      "size": "small (1x1)",
      "role": "Key Number",
      "content": "One extra-large number + brief description, e.g. '8 units' 'From ¥4,999'"
    },
    {
      "id": "M4",
      "size": "small (1x1)",
      "role": "Icon Explanation",
      "content": "A set of 4-6 simple icons + ultra-short labels (e.g. 'Use Cases')"
    },
    {
      "id": "M5",
      "size": "medium (2x1)",
      "role": "Ranking / List",
      "content": "TOP 3 text list, with large 1/2/3 number badges in front"
    },
    {
      "id": "M6",
      "size": "small (1x1)",
      "role": "Quote / Selling Point",
      "content": "One golden quote / KOL quote + quotation mark decoration"
    },
    {
      "id": "M7",
      "size": "medium (1x2)",
      "role": "Detail Showcase",
      "content": "Product close-up detail + 1-2 callout labels"
    },
    {
      "id": "M8",
      "size": "small (1x1)",
      "role": "Footer / Tip",
      "content": "'Swipe to next page →' / QR code / source attribution"
    }
  ],
  "module_internal_style": {
    "padding": "16-24px inside each module",
    "typography": "sans-serif (Inter / Helvetica Neue / Source Han Sans); module title in bold, body smaller",
    "rule": "each module is self-contained and could stand alone",
    "imagery": "small product photos / icons / micro-charts; never let a module become pure text"
  },
  "constraints": {
    "must_keep": [
      "All modules share unified corner radius",
      "Fixed gap between modules",
      "Each module has its own micro-title",
      "At least 1 module contains visualized data (chart / large number)",
      "Total image uses no more than 5 main colors"
    ],
    "avoid": [
      "All modules the same size (becomes a grid table)",
      "Modules touching with no whitespace",
      "Information density too low within modules (becomes empty widget)",
      "Module borders using thick outlines (>2px)",
      "Using gradients / glass textures to blur bento's minimalist feel"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `main_title`, `module_count`
- **Can default**: `aspect_ratio` (3:4), `palette` (warm off-white + vermilion accent), `global_corner_radius`, `module_gap`
- **Can randomize**: `module_tints` specific order, each module's specific content (auto-infer from topic if user doesn't specify)

### Auto-Fill Strategy

- User only provides topic → auto-decide 8 modules, infer module roles (TOP 1 / key number / icon / ranking / selling point / detail / footer)
- User says "Xiaohongshu style" → palette warm off-white + warm accent, aspect 3:4
- User says "tech / digital style" → palette dark gray + neon accent, aspect 1:1 or 3:4
- User says "finance / serious" → palette mono + single dark accent, aspect 16:9

## Variant 1: iOS Widget Screen Style

```json
{
  "modify": {
    "background": "iOS system wallpaper gradient (deep blue-purple → black)",
    "module_backgrounds": "frosted glass + light border",
    "module_corner_radius": "32px (more rounded)",
    "typography": "SF Pro Display + SF Symbols style icons",
    "vibe": "like a screenshot of an iPhone home screen with all widgets filled with information"
  }
}
```

Suitable for: tech / app recommendations / product introductions.

## Variant 2: Notion Dashboard Style

```json
{
  "modify": {
    "background": "pure white #FFFFFF",
    "module_backgrounds": "very light gray #F7F6F3 + 1px light gray border",
    "module_corner_radius": "8px (square-ish)",
    "module_padding": "larger",
    "typography": "Inter / Sohne, ultra-light weight dominant",
    "vibe": "minimalist, understated, like a Notion page screenshot"
  }
}
```

Suitable for: knowledge management, productivity, SaaS tool introductions.

## Variant 3: High-Density Xiaohongshu "Pitfall Guide" Style

```json
{
  "modify": {
    "module_count": "9-12",
    "background": "warm cream + grainy paper texture",
    "module_tints": ["mint", "peach", "lavender", "lemon"],
    "accent": "tomato red used for '⚠️ Pitfall' labels",
    "typography": "slightly rounder / handwritten font for friendliness",
    "vibe": "information packed, more vibrant colors, with emoji / labels"
  }
}
```

Suitable for: Xiaohongshu pitfall guides, beginner guides, must-see lists.

## Things to Avoid

- All modules the same size → becomes a grid table, loses bento's "visual hierarchy"
- Modules without micro-titles → loses "independent information unit" semantics
- All text modules across the entire image → loses visual impact
- No whitespace or inconsistent whitespace between modules → visually noisy
- More than 5 main colors → overall feel collapses
- Forcing a hero module as decoration but with empty content → wastes visual weight
- Module borders >2px → looks like a spreadsheet not bento