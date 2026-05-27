# Multi-Method Qualitative Comparison Grid Template

This file is used for generating "paper qualitative results comparison grids":

- CV papers: multi-method segmentation / detection / generation result comparisons
- NLP papers: multi-method generated text comparisons (screenshot-style)
- 3D / reconstruction papers: multi-method reconstruction result comparisons
- Diffusion / image generation papers: different prompts × different methods grid
- Ablation study visual comparisons

Characteristics:

- Strict grid: rows = samples / inputs, columns = methods (including GT and Ours)
- Column header row has method names (with citations)
- Ours column usually has border / highlight
- Cell content is uniform (image / text snippet / heatmap)
- Thin gap between grid cells, overall white background
- Optional caption for explanation

## Scope

- Paper qualitative results section
- Ablation study visual comparisons
- Top conference supplementary large grid figures
- Survey paper method gallery
- Thesis defense comparison slides

## When to use

- User mentions "qualitative / comparison grid / comparison grid / methods comparison / ablation visual"
- User wants "standard paper comparison grid with rows=samples, columns=methods"

Do NOT use for:

- User wants "dual product consumer comparison" → use `infographics/comparison-infographic.md`
- User wants "multi-person avatar grid" → use `avatars-and-profile/character-grid-portrait.md`
- User wants "data chart" → use `academic-figures/publication-chart.md`
- User wants "video frame sequence" → use `storyboards-and-sequences/`

## Missing Information Priority Question Order

1. Number of rows (sample count, recommend 3-6 rows)
2. Number of columns (method count, recommend 3-6 columns, including Input/GT and Ours)
3. Method name for each column (including citation reference, e.g. "Method A [12]")
4. Cell content type (RGB image / mask / heatmap / text snippet / 3D render)
5. Whether to include row labels (left side labeled "Sample 1 / 2 / ..." or "Easy / Medium / Hard")
6. Whether to add red-box zoom-in at certain positions (focus area)
7. Whether to include caption annotation

## Main Template: Qualitative Comparison Grid (M rows × N cols)

📖 Description

The entire figure is a strict M×N grid: each row is a sample, each column is a method. Leftmost can have row labels, topmost row has column headers (method name + citation). Ours column has border highlight, red zoom-in boxes can be drawn inside certain cells.

📝 Prompt

```json
{
  "type": "Qualitative Comparison Grid (paper-grade multi-method multi-sample comparison grid)",
  "goal": "Generate a grid comparison figure suitable for direct inclusion in a paper qualitative results section, strictly aligned, clear column headers, Ours highlighted, grayscale-print readable",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"4:3\"}",
    "background": "white #FFFFFF",
    "outer_padding": "40px"
  },
  "grid": {
    "rows": "{argument name=\"rows\" default=\"4\"}",
    "cols": "{argument name=\"cols\" default=\"5\"}",
    "cell_size_rule": "all cells identical size; gap between cells 4-6px",
    "cell_aspect": "{argument name=\"cell_aspect\" default=\"square\"}"
  },
  "headers": {
    "column_headers": {
      "enabled": true,
      "items": [
        { "id": "C1", "label": "{argument name=\"col1_name\" default=\"Input\"}" },
        { "id": "C2", "label": "{argument name=\"col2_name\" default=\"Method A [12]\"}" },
        { "id": "C3", "label": "{argument name=\"col3_name\" default=\"Method B [34]\"}" },
        { "id": "C4", "label": "{argument name=\"col4_name\" default=\"Method C [56]\"}" },
        { "id": "C5", "label": "{argument name=\"col5_name\" default=\"Ours\"}", "highlight": true }
      ],
      "style": "centered above each column, sans-serif bold 11pt, citations in smaller superscript or in [brackets]"
    },
    "row_labels": {
      "enabled": "{argument name=\"row_labels_enabled\" default=\"true\"}",
      "items": [
        "{argument name=\"row1_label\" default=\"Sample 1\"}",
        "{argument name=\"row2_label\" default=\"Sample 2\"}",
        "{argument name=\"row3_label\" default=\"Sample 3\"}",
        "{argument name=\"row4_label\" default=\"Sample 4\"}"
      ],
      "style": "rotated 90° on the left margin OR placed above each row in italic 10pt"
    }
  },
  "cell_content": {
    "type": "{argument name=\"content_type\" default=\"rgb_image\"}",
    "options_explained": {
      "rgb_image": "natural images / photos",
      "segmentation_mask": "color-coded mask overlays",
      "heatmap": "viridis / jet style heatmap",
      "depth_map": "grayscale or turbo colormap",
      "text_snippet": "rendered text block in a code-like box",
      "3d_render": "rendered 3D mesh from a fixed viewpoint",
      "side_by_side": "two halves: input | result"
    },
    "consistency_rule": "all cells in the same row should depict the SAME underlying sample so the comparison is fair"
  },
  "highlights": {
    "ours_column": {
      "enabled": true,
      "style": "thicker border 1.5px in deep red / accent color (e.g. #DC2626) around each Ours cell"
    },
    "zoom_in_boxes": {
      "enabled": "{argument name=\"zoom_in_enabled\" default=\"false\"}",
      "rule": "if true, draw small red rectangles inside cells highlighting interesting regions; same red box appears at the same coordinate across the row to make comparison fair",
      "callout_style": "optional zoomed crop placed below the row, connected by thin lines"
    }
  },
  "caption": {
    "enabled": "{argument name=\"caption_enabled\" default=\"true\"}",
    "label": "{argument name=\"figure_label\" default=\"Figure 4.\"}",
    "text": "{argument name=\"caption_text\" default=\"Qualitative comparison with state-of-the-art methods. Our method (last column) preserves fine details and reduces artifacts.\"}",
    "style": "below the grid, italic serif or compact sans-serif, justified, smaller font"
  },
  "constraints": {
    "must_keep": [
      "all cells identical size and tightly aligned",
      "white or near-white background, no gradient",
      "column headers clearly above each column with citation",
      "Ours column visually distinguished (border / shaded header)",
      "row content depicts the same sample across all methods",
      "if zoom-in boxes used, position is identical across the row",
      "labels in English by default, no mixing with Chinese unless requested",
      "must remain interpretable in grayscale print"
    ],
    "avoid": [
      "different cell sizes between rows / columns",
      "random colors as cell backgrounds (cells are content, not decoration)",
      "missing citations on baseline methods",
      "ours column hidden or unmarked",
      "rotated cells / tilted layouts (must be axis-aligned)",
      "decorative emoji / cartoon icons inside cells",
      "varying content type per row (e.g. one row mask, next row RGB) without explicit row label",
      "more than 6 cols (becomes unreadable in two-column paper format)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `rows`, `cols`, method name per column (with citation), `content_type`
- **Can default**: `aspect_ratio` (4:3), `row_labels_enabled` (true), `caption_enabled` (true)
- **Can randomize**: inter-column gap exact pixels, font size (within reasonable range)

### Auto-Fill Strategy

- User says "I have 4 methods + ours" → auto-add Input column (becoming 5 columns: Input / M1 / M2 / M3 / M4 / Ours, total 6 columns)
- User doesn't provide row labels → default to "Sample 1, 2, 3, ..." or ask whether to label difficulty levels
- User doesn't provide citations → prompt "consider adding [n] citation placeholders" rather than fabricating them
- User says "ablation study" → change column names to ablation variants like "w/o A", "w/o B", "Full"
- User says "need zoom-in" → enable `zoom_in_enabled` and prompt for region coordinates

## Variant 1: Pure Text NLP Qualitative Comparison

```json
{
  "type": "NLP qualitative comparison grid",
  "modify": {
    "content_type": "text_snippet",
    "cell_aspect": "tall rectangle (e.g. 2:3 portrait)",
    "cell_styling": "monospace font in cell, black text on white, with key tokens highlighted in colored boxes",
    "row_labels": "input prompt / question displayed at the leftmost of each row",
    "use_case": "Compare outputs from multiple LLMs / translation / summarization"
  }
}
```

Suitable for: NLP paper generation result comparisons, machine translation quality comparisons.

## Variant 2: Segmentation Mask Multi-Column Comparison (with Color Overlay)

```json
{
  "type": "Segmentation mask comparison grid",
  "modify": {
    "content_type": "segmentation_mask",
    "cell_styling": "RGB image base + semi-transparent mask overlay; consistent color per class; GT column and Ours column easy to compare",
    "extras": "Quantitative metric labels (e.g. 'mIoU: 0.78') can be added in small text below cells",
    "color_legend": "Small legend at bottom-right of figure: color → class name"
  }
}
```

Suitable for: semantic segmentation, instance segmentation, medical image segmentation papers.

## Variant 3: Diffusion / Generative Model Prompt × Method Matrix

```json
{
  "type": "Generation prompt × method matrix",
  "modify": {
    "rows": "different text prompts (left labels show prompt text)",
    "cols": "different generation methods or different sampling steps",
    "cell_content": "generated images, all from same prompt across the row",
    "extras": "Small labels like '↑ +0.3 CLIP score' can be added on the Ours column"
  }
}
```

Suitable for: diffusion models, text-to-image generation, image editing method comparisons.

## Things to Avoid

- Inconsistent cell sizes → completely loses comparison meaning
- Missing citations → peer reviewers will deduct points
- Ours column unmarked → readers don't know which is yours
- Inconsistent samples across the same row (first column shows cat, second shows dog) → comparison invalid
- Adding gradients / shadows / excessive rounding → doesn't look like a paper
- Using emoji or cartoon decorations → seriously unprofessional
- More than 6 columns → unreadable in two-column paper layout
- No caption → readers don't know what this figure is trying to say
- Zoom-in boxes at inconsistent positions across different cells → unfair comparison