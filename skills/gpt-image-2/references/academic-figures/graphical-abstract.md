# Graphical Abstract Template

This file is used for generating "journal submission Graphical Abstract / paper graphical abstract / submission cover figure":

- Graphical Abstract required by journal submissions
- Paper one-figure overview ("one figure explains main contributions")
- Research highlight figure for thesis defense / group meeting opening slides

Characteristics:

- Minimal, compact, 4-part core narrative (Problem → Method → Key Process → Result)
- Horizontal left→right or center-expanding layout
- White background, low-saturation engineering colors, ≤3 main colors, **like a high-quality journal graphical abstract, absolutely not a marketing poster**
- Text distilled to short phrases, paragraph-style explanations forbidden

## Scope

- Graphical Abstract for Elsevier / ACS / Wiley / Springer / IEEE journal submissions
- Research one-figure overview at top of arXiv / preprint README
- Paper supplementary or highlight figure
- Thesis defense / presentation "research highlights" page

## When to use

- User mentions "graphical abstract / graphical abstract / submission abstract figure / one figure explains / highlight figure"
- User wants the visual to be "journal cover-level abstract figure, concise restrained academic style"
- User can already explain in 1-2 sentences "what this paper does and what it found"

Do NOT use for:

- User wants "method pipeline overview" → use `academic-figures/method-pipeline-overview.md`
- User wants "thesis proposal / defense opening overview figure" → use `academic-figures/research-overview-poster.md`
- User wants "mechanism / pathway diagram" → use `academic-figures/mechanism-diagram.md`
- User wants "marketing / brand / magazine cover feel" → use `poster-and-campaigns/editorial-cover.md`

## Missing Information Priority Question Order

1. Research topic (one sentence; written in title or figure caption)
2. Target journal or target scenario (determines aspect ratio + primary color tone; different journals have different preferences)
3. 4 core elements: research problem / method or system / key process or mechanism / main result
4. Whether there is a simplified depiction of the "research object" (particle / molecule / device / process)
5. Label language (Chinese / English / bilingual; most journals require English)
6. Aspect ratio (default horizontal 16:9 / 2:1; some journals require square 1:1, confirm first)

## Main Template: Horizontal 4-Section Graphical Abstract

📖 Description

The entire figure flows horizontally: starting from the leftmost "Research Problem / Research Object", sequentially to "Method / System", "Key Process / Mechanism", "Main Result". The four areas are proportionally balanced, text distilled to short phrases, visual hierarchy clear, overall like a high-quality engineering journal abstract figure.

📝 Prompt

```json
{
  "type": "Academic journal graphical abstract (Graphical Abstract)",
  "goal": "Generate a Graphical Abstract suitable for journal submission, minimal, white background, restrained engineering color palette, readable in seconds, absolutely no marketing poster feel",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"2:1\"}",
    "background": "pure white #FFFFFF",
    "outer_padding": "60px around the diagram",
    "render_quality": "vector-clean look, anti-aliased edges, sharp text, suitable for grayscale print"
  },
  "title_block": {
    "enabled": "{argument name=\"title_block_enabled\" default=\"false\"}",
    "title": "{argument name=\"title\" default=\"\"}",
    "rule": "most journals do not allow titles inside the graphical abstract; enable only when user explicitly requested a title"
  },
  "sections": [
    {
      "id": "P1",
      "role": "Problem",
      "label": "{argument name=\"problem_label\" default=\"Research Problem\"}",
      "summary": "{argument name=\"problem_summary\" default=\"a short phrase stating the gap, e.g. 'unstable combustion under variable moisture'\"}",
      "depiction": "{argument name=\"problem_depiction\" default=\"a minimal line-art sketch of the studied object or scenario\"}"
    },
    {
      "id": "P2",
      "role": "Method",
      "label": "{argument name=\"method_label\" default=\"Method\"}",
      "summary": "{argument name=\"method_summary\" default=\"a short phrase, e.g. 'thermogravimetric + kinetics analysis'\"}",
      "depiction": "{argument name=\"method_depiction\" default=\"a minimal schematic of the analytical or experimental setup\"}"
    },
    {
      "id": "P3",
      "role": "Process",
      "label": "{argument name=\"process_label\" default=\"Key Mechanism\"}",
      "summary": "{argument name=\"process_summary\" default=\"a short phrase, e.g. 'two-stage volatile combustion'\"}",
      "depiction": "{argument name=\"process_depiction\" default=\"a small mechanism strip with 2-3 sub-steps, line-art style\"}"
    },
    {
      "id": "P4",
      "role": "Result",
      "label": "{argument name=\"result_label\" default=\"Outcome\"}",
      "summary": "{argument name=\"result_summary\" default=\"a short phrase, e.g. 'optimized excess-air ratio reduces NOx by ~X%'\"}",
      "depiction": "{argument name=\"result_depiction\" default=\"a minimal qualitative chart sketch (no fabricated numbers) or a result icon (gauge / bar)\"}"
    }
  ],
  "section_block_style": {
    "shape": "implicit columns separated by generous whitespace, NOT four heavy rectangles in a row",
    "header_text": "section label in bold sans-serif, 12-13pt, top-aligned",
    "summary_text": "single phrase, 10pt regular, max 2 lines, no period",
    "depiction_size": "around 35-50% of column height, vertically centered"
  },
  "connectors": {
    "style": "thin arrows (1.2px) with simple triangle arrowheads, dark gray #334155, between adjacent sections only",
    "rule": "no crossing, no curved decorative arcs; arrows convey 'leads to' / 'analyzed by' relationships",
    "label_arrows": "false by default; only add label when the relationship is non-trivial"
  },
  "color_palette": {
    "rule": "≤ 3 main colors total, drawn from a low-saturation engineering set: deep blue #1E3A8A / slate blue #3B82F6 / charcoal #1F2937; allow ONE low-saturation accent (e.g. amber #F59E0B for a heat / risk highlight) only if the user signaled a thermal or risk emphasis",
    "must_print_grayscale_readable": true
  },
  "typography": {
    "language": "{argument name=\"language\" default=\"english\"}",
    "rule": "english → Inter / Helvetica / Arial; chinese → PingFang SC / Source Han Sans; bilingual → english as primary, chinese as smaller secondary line",
    "consistency": "all section headers identical size; all summaries identical size; never mix serif and sans-serif"
  },
  "constraints": {
    "must_keep": [
      "all four sections visually equal-weight, no section dominates",
      "white background, no gradient, no decorative pattern, no photographic background",
      "language matches the target journal (default english)",
      "summaries are short phrases, never full sentences with periods",
      "the figure must look like it could appear on an Elsevier / ACS / IEEE table of contents page",
      "every numerical claim must come from the user; if absent, render qualitatively"
    ],
    "avoid": [
      "marketing-poster aesthetics, brand campaign aesthetics, magazine cover aesthetics",
      "3D effects, drop shadows, gradients, glossy fills, lens flare, motion blur",
      "exaggerated flames, smoke, sparks (even when the topic is combustion)",
      "cartoon mascots, emoji, decorative icons, hand-drawn wobble",
      "stock-photo-style realistic backgrounds",
      "fabricated numbers, percentages, equations, or chart data not provided by the user",
      "saturated colors (no neon, no vivid), more than 3 main colors",
      "watermarks, copyright stamps, vendor logos"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: 4 `*_summary` (Problem / Method / Key Process / Result) at minimum a short phrase each
- **Can default**: `aspect_ratio` (2:1), `background` (white), `color_palette` (deep blue / slate blue / charcoal)
- **Can randomize**: each section's `*_depiction` specific rendering (infer when user provides object/method name; otherwise ask back)

### Auto-Fill Strategy

- User gives topic but not 4 sections → ask for 4 summaries, **fabricating research content is forbidden**
- User gives qualitative contribution but no numbers → use expressions like `qualitatively shows` / `consistently reduces` without numbers
- User gives numbers (e.g. "NOx reduced by 18%") → write `~18%` directly, do not fabricate other metrics
- User says "Chinese journal / Chinese abstract figure" → switch to Chinese + fonts PingFang / Source Han Sans

## Variant 1: Center-Expanding (Hub-and-spoke)

```json
{
  "type": "Center-expanding Graphical Abstract",
  "modify": {
    "layout": "Place a simplified depiction of the research object / core system at the center, radiating outward into 3-4 sectors, each representing a core element (problem, method, mechanism, or result)",
    "rule": "Sectors are visually equal-weight, separated by thin lines; central object occupies 30-40% of the canvas",
    "use_case": "Suitable for systems research, platform-type research, or multi-modal contributions that are difficult to narrate linearly"
  }
}
```

Suitable for: comprehensive research, systemic contributions (e.g. new platform, new framework).

## Variant 2: Square 1:1 (required by some journals)

```json
{
  "type": "Square Graphical Abstract",
  "modify": {
    "aspect_ratio": "1:1",
    "layout": "2×2 grid, top-left = problem / object, top-right = method, bottom-left = key process, bottom-right = result",
    "rule": "Four quadrants strictly equal size and aligned; uniform spacing between quadrants; arrows follow a Z-pattern P1 → P2 → P3 → P4",
    "use_case": "Some ACS / Wiley journals require a square Graphical Abstract"
  }
}
```

Suitable for: journals requiring square aspect ratio.

## Variant 3: Vertical (social media / preprint card)

```json
{
  "type": "Vertical Graphical Abstract",
  "modify": {
    "aspect_ratio": "3:4",
    "layout": "Top → bottom four sections: Problem → Method → Mechanism → Outcome",
    "rule": "Compact width, each section retains breathing space; suitable for mobile or Twitter / LinkedIn card previews",
    "use_case": "For social media promotion of preprints, Lab homepage highlight cards"
  }
}
```

Suitable for: research promotion beyond submissions, while maintaining academic restraint.

## Things to Avoid

- Drawing the Graphical Abstract as a "compressed full paper" — cramming in all method steps, all formulas, all results
- Using any form of gradient / glass texture / glow / 3D → immediately looks like a marketing figure
- Mixing Chinese and English labels arbitrarily (unless explicitly bilingual)
- Drawing bar charts / line charts with specific values when no real data exists (**fabricating data is strictly forbidden**; only qualitative display allowed)
- Using saturated brand colors or neon — journal abstract figures should maintain low-saturation engineering colors
- Drawing the research object as hyper-realistic 3D rendering (academic style needs simplified line drawings)
- Adding journal logos / watermarks / "submitted to ..." labels