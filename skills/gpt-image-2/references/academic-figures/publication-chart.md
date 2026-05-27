# Publication-Ready Data Chart Template

This file is used for generating "standard data charts appearing in papers / reports":

- Bar chart / grouped bar chart (ablation experiments, method comparisons)
- Line chart / training curves (loss / accuracy over epochs)
- Scatter plot (performance-efficiency trade-off)
- Box plot / Violin plot (statistical distributions)
- Heatmap (confusion matrix / attention map / correlation matrix)

Characteristics:

- matplotlib / seaborn / R ggplot2 publication style
- Includes axes + labels + units + legend + error bars + significance markers
- Font size ≥ 10pt (ensures print readability)
- Restrained color palette (≤ 6 colors), grayscale-printable
- Grid lines very faint or absent

> ⚠️ Important disclaimer: **This template generates "visual representations of publication-grade charts", not real data visualizations**. GPT Image 2 cannot guarantee precise correspondence between coordinates and data.
>
> - If you need "to show what a paper chart looks like" / "make a cover / hero figure" → use this template
> - If you need "to generate publishable charts from real data" → use matplotlib / seaborn / ggplot2 / Plotly

## Scope

- Visual examples of paper method comparison charts
- Teaching slide "see this chart and understand" demonstration figures
- Blog / newsletter illustrations — "our method's performance on this chart"
- Investor deck "data mock"
- Demonstration and visualization teaching charts

## When to use

- User mentions "publication chart / matplotlib style / seaborn style / paper chart / bar chart / line chart / scatter / heatmap / confusion matrix"
- User wants "white background, restrained, grayscale-printable, like NeurIPS paper charts"
- User **clearly understands** this is a visual representation only, not relying on coordinate precision

Do NOT use for:

- User wants "real data visualization output" → recommend matplotlib / seaborn / Plotly
- User wants "KPI dashboard / data review" → use `infographics/kpi-dashboard-infographic.md`
- User wants "business PPT data page" → use `slides-and-visual-docs/visual-report-page.md`
- User wants "hand-drawn style infographic" → use `infographics/hand-drawn-infographic.md`

## Missing Information Priority Question Order

1. Chart type (bar / line / scatter / box / violin / heatmap / pie)
2. Topic ("our method's accuracy on ImageNet vs baselines")
3. X-axis and Y-axis names + units
4. Number of data series (single series / multi-series)
5. Whether there are error bars, significance markers *
6. Color tone (academic restraint / emphasis contrast / black-and-white monochrome)
7. Figure title + caption (paper figures generally have captions)

## Main Template: Publication-Ready Bar Chart (Default)

📖 Description

The entire figure is a standard academic bar chart: horizontal axis for methods / categories, vertical axis for metrics, comparing multiple methods, with error bars, significance *, and legend. Overall white background, sans-serif fonts, limited color palette.

📝 Prompt

```json
{
  "type": "Publication-Ready Bar Chart",
  "goal": "Generate a visual representation of a bar chart for a paper / report, white background, restrained, professional, grayscale-print readable",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"4:3\"}",
    "background": "white #FFFFFF",
    "outer_padding": "60px"
  },
  "title": {
    "text": "{argument name=\"title\" default=\"Accuracy on ImageNet-1K\"}",
    "position": "top-center, sans-serif bold 13pt",
    "subtitle": "{argument name=\"subtitle\" default=\"\"}"
  },
  "axes": {
    "x_axis": {
      "label": "{argument name=\"x_label\" default=\"Method\"}",
      "categories": [
        "{argument name=\"cat1\" default=\"ResNet-50\"}",
        "{argument name=\"cat2\" default=\"ViT-B\"}",
        "{argument name=\"cat3\" default=\"Swin-B\"}",
        "{argument name=\"cat4\" default=\"ConvNeXt-B\"}",
        "{argument name=\"cat5\" default=\"Ours\"}"
      ],
      "tick_label_rotation": "0deg or 30deg if labels are long"
    },
    "y_axis": {
      "label": "{argument name=\"y_label\" default=\"Top-1 Accuracy (%)\"}",
      "range": "{argument name=\"y_range\" default=\"75 to 86\"}",
      "tick_format": "decimal or percent",
      "gridlines": "very faint horizontal gridlines (light gray dashed, low opacity)"
    }
  },
  "bars": {
    "style": "vertical bars, ~30-40% width of category slot, gap between bars",
    "color_rule": {
      "default": "use a single muted color for all baselines (e.g. slate blue #64748B), highlight 'Ours' bar in accent color (e.g. orange #D97706 or red #DC2626)",
      "alternative": "if comparing methods grouped by family, use 2-3 muted colors to encode family"
    },
    "value_labels": {
      "enabled": "{argument name=\"value_labels_enabled\" default=\"true\"}",
      "rule": "show numeric value above each bar, sans-serif 9pt bold, e.g. '82.3'"
    }
  },
  "error_bars": {
    "enabled": "{argument name=\"error_bars_enabled\" default=\"true\"}",
    "style": "thin black T-bar at top of each bar, ±std or ±95% CI",
    "annotation": "mention what the error represents in caption (e.g. 'error bars show ±1 std over 5 runs')"
  },
  "significance_markers": {
    "enabled": "{argument name=\"significance_enabled\" default=\"false\"}",
    "rule": "if true, draw thin horizontal brackets between compared bars, with * / ** / *** annotation above (p<0.05 / p<0.01 / p<0.001)"
  },
  "legend": {
    "enabled": "{argument name=\"legend_enabled\" default=\"false\"}",
    "rule": "only show legend if multiple colors / groups used; place top-right inside or outside the plot area",
    "items": ["Baselines", "Ours"]
  },
  "caption": {
    "enabled": "{argument name=\"caption_enabled\" default=\"true\"}",
    "label": "{argument name=\"figure_label\" default=\"Figure 3.\"}",
    "text": "{argument name=\"caption_text\" default=\"Top-1 accuracy on ImageNet-1K. Our method outperforms all baselines while using fewer parameters. Error bars show ±1 std over 5 runs.\"}",
    "style": "below the chart, italic serif or compact sans-serif, justified, smaller font"
  },
  "constraints": {
    "must_keep": [
      "white background, no gradient, no pattern fills",
      "sans-serif fonts only (Helvetica / Inter / Arial); axis tick labels ≥ 9pt, axis labels ≥ 11pt, title ≥ 13pt",
      "color palette ≤ 6 colors, must remain readable in grayscale",
      "all axes have labels and units",
      "no 3D bar effects, no perspective tilt",
      "if multiple bars per category, group them with consistent spacing",
      "Ours bar is visually distinguishable (color or annotation)"
    ],
    "avoid": [
      "rainbow colors / saturated palette",
      "3D extruded bars / pie charts (3D distorts perception)",
      "missing axis labels or units",
      "unreadable tick labels (too small or rotated awkwardly)",
      "decorative background images / textures",
      "emoji / cartoon icons inside or around bars",
      "value labels overlapping bars or each other",
      "random / irrelevant accent colors",
      "fake precision: don't render bar heights to imply real numbers — keep it clearly illustrative"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: chart type (if not bar), `title`, `x_label` / `y_label` / units, `categories`
- **Can default**: `aspect_ratio` (4:3), `background` (white), `error_bars_enabled` (true), `value_labels_enabled` (true), `legend_enabled` (false for single series)
- **Can randomize**: bar width, tick count, gridline density (within reasonable range)

### Auto-Fill Strategy

- User says "I have 5 methods' accuracy comparison" → auto-use default 5 categories, highlight last as Ours
- User doesn't specify y_range → infer (based on value range ± 5%)
- User doesn't mention error → default error_bars enabled (standard paper practice)
- User doesn't mention significance → default disabled (unless it's a statistics paper)
- User says "not bar" → switch to corresponding variant

## Variant 1: Line Chart (Training Curves / Time Series)

```json
{
  "type": "Publication-Ready Line Chart",
  "modify": {
    "x_axis_typical": "epoch / step / time / iteration",
    "y_axis_typical": "loss / accuracy / metric",
    "lines_count": "1-5 series, each a different muted color",
    "line_style": "solid 1.5px main line + optional shaded area (semi-transparent same color) for std band",
    "markers": "optional small markers at sparse intervals (circles / triangles), not on every point",
    "legend": "always enabled for multi-series, top-right or below",
    "rule_extra": "axes can be log-scale if data spans orders of magnitude (label as 'log scale')"
  }
}
```

Suitable for: training curves, time series trends, ablation over hyperparameters, scaling laws.

## Variant 2: Scatter Plot (Trade-off Diagram)

```json
{
  "type": "Publication-Ready Scatter Plot",
  "modify": {
    "typical_use": "performance vs efficiency trade-off (e.g. accuracy vs FLOPs / latency / params)",
    "x_axis_typical": "compute / params / latency (often log scale)",
    "y_axis_typical": "accuracy / metric",
    "point_style": "filled circles, size encodes a third dimension (e.g. model size), color encodes a category (e.g. method family)",
    "label_each_point": "small text label next to each point with method name (no leader lines unless crowded)",
    "ours_emphasis": "Our method points are larger and use accent color + black border",
    "frontier_line": "optional: draw a Pareto frontier curve to show 'we push the frontier'"
  }
}
```

Suitable for: performance-efficiency trade-offs, parameters vs accuracy, Pareto frontier.

## Variant 3: Heatmap (Confusion Matrix / Attention Map / Correlation)

```json
{
  "type": "Publication-Ready Heatmap",
  "modify": {
    "grid": "N × N (default 5×5 to 10×10)",
    "color_map": "sequential — viridis / Blues / Reds / grayscale; diverging (e.g. correlation matrix) — RdBu_r red-blue bidirectional",
    "cell_annotation": "show numeric value inside each cell in monospace, color flips for readability on dark cells",
    "axes_label": "row labels = ground truth, column labels = predicted (confusion matrix scenario)",
    "colorbar": "right side vertical colorbar with label and ticks",
    "rule_extra": "always include colorbar; never use rainbow colormap for sequential data (jet has been deprecated by academia)"
  }
}
```

Suitable for: confusion matrices, attention weight visualization, correlation matrices, ablation grids.

## Variant 4: Box Plot / Violin Plot (Statistical Distribution)

```json
{
  "type": "Publication-Ready Box / Violin Plot",
  "modify": {
    "typical_use": "compare distributions across methods / conditions / groups",
    "elements": "box (Q1, median, Q3) + whiskers (1.5 IQR) + outlier dots; violin shape overlaid to show density",
    "median_line_emphasis": "median line thick solid, color distinguishes group",
    "annotation": "can overlay swarm / strip plot to show each data point",
    "rule_extra": "if using violin, still draw box inside the violin; do not use pure violin (loses median information)"
  }
}
```

Suitable for: experiment repetition result distributions, cross-dataset / cross-user / cross-condition distribution comparisons.

## Things to Avoid

- Using 3D bars / 3D pies → seriously unprofessional
- Using rainbow / jet colormap for continuous values (abandoned by academia)
- Missing units / missing axis labels
- Value labels too small to read
- No caption or caption doesn't explain error bars
- Combining 4-5 unrelated charts into one figure (should use multi-panel figure template, each sub-figure independent)
- Pretending precision (implying real data when it's illustrative)
- Using fancy fonts (Comic Sans / handwritten)
- Adding watermarks / decorative backgrounds
- Missing legend (multi-series must have one)
- Multiple series with identical colors
- Missing Ours highlight (paper figures usually need reviewers to spot yours at a glance)