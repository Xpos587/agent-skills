# Multi-Condition / Multi-Condition Result Comparison Figure Template

This file is used for generating "multi-panel result comparison figures of the same research object under different conditions / groups / operating points":

- Experimental or simulation results under different temperatures / pressures / concentrations / ratios / times
- Parallel results of different treatment groups / control groups / process schemes
- Multi-panel (a)(b)(c)(d) paper result figures

Characteristics:

- 2x2 / 1x3 / 1x4 etc. uniform grid layout
- **All panels strictly unified**: same size, same color logic, same legend, same font hierarchy, same margins
- White background, low-saturation engineering colors, paper result figure style
- **When no real data is available, only qualitative expression is allowed; fabricating numerical values / contour lines / colorbar ranges is forbidden**

## Scope

- Engineering / physics / chemistry / energy / materials / environmental science multi-condition result comparisons
- Field map comparisons of combustion / flow field / temperature field / stress field / concentration field
- Experimental comparisons of different treatment groups / different doses / different time points
- Multi-panel visualization of the same metric under multiple conditions

## When to use

- User mentions "multi-condition / multi-condition / multi-condition / comparison under different X / panel (a)(b)(c)(d) / result comparison figure"
- User wants the visual "paper result figure, not marketing infographic"
- Comparing **the same type of results of the same object under different conditions**

Do NOT use for:

- User wants "comparison of different methods on the same samples" (rows=samples, columns=methods) → use `academic-figures/qualitative-comparison-grid.md`
- User wants "single publication-ready chart" (bar / line / scatter) → use `academic-figures/publication-chart.md`
- User wants "marketing / infographic-style binary comparison" → use `infographics/comparison-infographic.md`

## Missing Information Priority Question Order

1. What is being compared (same phenomenon / same metric)
2. Which conditions / operating points are being compared (recommend 2-6; more than 6 consider splitting into two figures)
3. What each panel displays (field map / line chart / bar chart / contour / micrograph) — **all panels must be the same type**
4. Whether real data is available (**critical**: determines qualitative vs. quantitative rendering)
5. Grid layout (2x2 / 1x3 / 1x4 / 2x3)
6. Label language (Chinese / English / bilingual)
7. Shared legend / shared colorbar (strongly recommended to share)

## Main Template: N-Panel Multi-Condition Comparison (Uniform Specification)

📖 Description

The entire figure is divided into N panels by a uniform grid, each panel showing the same type of result under different conditions. All panels share the colorbar / legend / font hierarchy / margins. Sub-figures are labeled (a)(b)(c)(d), labels brief and restrained. **Absolutely no panel may establish its own separate style.**

📝 Prompt

```json
{
  "type": "Academic multi-condition comparison figure",
  "goal": "Generate a multi-panel comparison figure suitable for direct inclusion in a paper results section, all panels strictly unified, white background, low-saturation engineering colors, grayscale-print readable",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"4:3\"}",
    "background": "pure white #FFFFFF",
    "outer_padding": "50px around the grid",
    "inter_panel_gap": "16-20px, identical horizontal and vertical",
    "render_quality": "vector-clean look, anti-aliased, sharp text"
  },
  "title_caption": {
    "figure_label": "{argument name=\"figure_label\" default=\"Figure X.\"}",
    "caption": "{argument name=\"caption\" default=\"Comparison of results under varying conditions.\"}",
    "position": "bottom-center, italic serif or compact sans-serif, smaller font size"
  },
  "grid_layout": {
    "rows": "{argument name=\"rows\" default=\"2\"}",
    "cols": "{argument name=\"cols\" default=\"2\"}",
    "panel_count": "{argument name=\"panel_count\" default=\"4\"}",
    "rule": "rows × cols == panel_count; all panels identical size; consistent vertical and horizontal alignment"
  },
  "panels": {
    "panel_type": "{argument name=\"panel_type\" default=\"contour-field\"}",
    "panel_type_options": "contour-field | line-chart | bar-chart | heatmap | micrograph | flow-field | bubble-chart",
    "rule": "ALL panels MUST share the same panel_type; never mix bar with line within the same comparison figure",
    "items": [
      {
        "id": "(a)",
        "condition_label": "{argument name=\"panel_a_label\" default=\"Condition A\"}",
        "condition_detail": "{argument name=\"panel_a_detail\" default=\"e.g. excess-air ratio λ = 1.0\"}"
      },
      {
        "id": "(b)",
        "condition_label": "{argument name=\"panel_b_label\" default=\"Condition B\"}",
        "condition_detail": "{argument name=\"panel_b_detail\" default=\"e.g. excess-air ratio λ = 1.2\"}"
      },
      {
        "id": "(c)",
        "condition_label": "{argument name=\"panel_c_label\" default=\"Condition C\"}",
        "condition_detail": "{argument name=\"panel_c_detail\" default=\"e.g. excess-air ratio λ = 1.4\"}"
      },
      {
        "id": "(d)",
        "condition_label": "{argument name=\"panel_d_label\" default=\"Condition D\"}",
        "condition_detail": "{argument name=\"panel_d_detail\" default=\"e.g. excess-air ratio λ = 1.6\"}"
      }
    ]
  },
  "panel_style": {
    "frame": "thin border 1px #1F2937 OR clean axis lines without outer frame, applied identically to all panels",
    "label_position": "(a) (b) (c) (d) at top-left of each panel, bold sans-serif, 11pt",
    "condition_label_position": "centered above each panel OR inside each panel top-right, identical position across all panels",
    "axis_labels": "shared if possible; if shown, identical font size, identical tick density across panels",
    "internal_titles": "AVOID per-panel decorative titles; rely on (a)(b)(c)(d) + condition label only"
  },
  "shared_legend": {
    "enabled": "{argument name=\"shared_legend_enabled\" default=\"true\"}",
    "position": "{argument name=\"shared_legend_position\" default=\"right-of-grid\"}",
    "rule": "single legend / colorbar shared across ALL panels; never give each panel its own legend with different range",
    "colorbar_range": "{argument name=\"colorbar_range\" default=\"qualitative-low-to-high\"}",
    "colorbar_range_rule": "if user provided a numerical range, use it; otherwise render as a qualitative gradient labeled 'low → high' with NO fabricated numerical ticks"
  },
  "color_logic": {
    "rule": "≤ 3 main colors total; if a sequential colormap is used, choose a perceptually uniform low-saturation engineering colormap (e.g. viridis-like, blue-to-orange, gray-to-deep-blue); apply the SAME colormap and SAME range to every panel",
    "must_print_grayscale_readable": true
  },
  "data_authenticity": {
    "user_provided_real_data": "{argument name=\"has_real_data\" default=\"false\"}",
    "rule_when_false": "render the panels as QUALITATIVE schematics: smooth gradient fields, generic shapes, no numerical tick labels on the colorbar, no specific values in axes; explicitly avoid the visual impression of a real dataset",
    "rule_when_true": "use the user-provided values; never extrapolate, interpolate, or invent additional values"
  },
  "constraints": {
    "must_keep": [
      "all panels identical size, identical aspect, identical position scheme",
      "shared color logic and shared legend across all panels",
      "white background, no gradient backdrop, no decorative pattern",
      "(a)(b)(c)(d) labels in identical position and identical style across all panels",
      "only sans-serif typography, identical font family across all panels",
      "the figure should look like it came from a results section of an engineering or science journal"
    ],
    "avoid": [
      "different colormap or different color range per panel",
      "different chart type per panel (e.g. mixing bar and line)",
      "decorative panel titles, hero panel that visually dominates the rest",
      "saturated brand colors, neon, vivid gradients",
      "3D effects, drop shadows, glossy fills, lens flare",
      "fabricated numerical tick values, fabricated colorbar ranges, fabricated isolines",
      "marketing-poster aesthetics, infographic-collage aesthetics",
      "watermarks, copyright stamps"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `panel_count`, `panel_type` (all panels same type), `has_real_data`
- **Can default**: `aspect_ratio`, `grid_layout` (2x2 is most common), `shared_legend_enabled` (true)
- **Can randomize**: each condition's `*_detail` wording (academic polish when user provides the control variable name)

### Auto-Fill Strategy

- User doesn't say whether real data exists → **must confirm first**: when `has_real_data` = false, render the entire figure qualitatively
- User provides different conditions but not specific values per panel → use placeholder phrases in condition_detail (e.g. `λ = X1`), **do not fabricate numbers**
- User provides panel count but row × col doesn't match → auto-select nearest square grid (2x2 / 2x3 / 3x3)
- User says "Chinese paper / defense" → switch labels to Chinese + fonts PingFang / Source Han Sans

## Variant 1: Horizontal 1xN (suitable for narrow panel comparisons)

```json
{
  "type": "Horizontal 1×N multi-condition comparison",
  "modify": {
    "layout": "rows = 1, cols = N (recommend N ≤ 4)",
    "use_case": "Panels containing narrow bar charts / narrow line charts, better suited for horizontal layout; or double-column paper layout requiring a single horizontal row"
  }
}
```

Suitable for: horizontal comparisons in single-column / double-column paper formats.

## Variant 2: Row-Column Dual-Factor Matrix (MxN)

```json
{
  "type": "Dual-factor matrix comparison",
  "modify": {
    "layout": "rows = M (different levels of one factor), cols = N (different levels of another factor)",
    "rule": "Top row shows column factor labels, leftmost column shows row factor labels; panel styling strictly unified within",
    "use_case": "When two independent variables need to be varied simultaneously (e.g. temperature × moisture content, or time × concentration)"
  }
}
```

Suitable for: two-factor experimental design result display, orthogonal experiment result visualization.

## Variant 3: Qualitative Field Map Rendering (No Real Data)

```json
{
  "type": "Qualitative field map multi-condition comparison",
  "modify": {
    "panel_type": "contour-field",
    "data_authenticity": {
      "user_provided_real_data": false,
      "rule": "render smooth qualitative gradient fields with NO numerical tick labels and NO specific isoline values; the colorbar shows 'low → high' as a qualitative scale only",
      "intent": "visually communicate 'higher temperature in panel (b)' without claiming any specific value"
    },
    "use_case": "For use at the defense / proposal stage when data is not yet available, to clarify research ideas first"
  }
}
```

Suitable for: illustrative result comparisons, methodology explanation phase.

## Things to Avoid

- Using different colormaps / different ranges per panel → directly destroys comparability
- Drawing contour lines / colorbar scales with specific values when no real data exists (**fabricating data is strictly forbidden**)
- Making one panel visually heavier than others ("main figure + auxiliary figure" structure is not allowed)
- Adding independent decorative titles to each panel
- Mixing different chart types (bar / line / contour) in the same comparison figure
- Using saturated brand colors or neon gradients
- Misapplying the "compare methods" logic (rows=samples × columns=methods) to this template (use `qualitative-comparison-grid.md` instead)
- Adding watermarks / journal logos / equipment brand labels