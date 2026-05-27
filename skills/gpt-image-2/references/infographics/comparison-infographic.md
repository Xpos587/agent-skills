# Comparison Infographic Template

This file is used for generating "binary / multi-way comparison" infographics:

- A vs B dual-column comparison (products / concepts / methods)
- Three-way comparison (e.g. three plans / three pricing tiers)
- Multi-dimensional review comparison (multiple products × multiple dimensions)
- Pros and cons / advantages and disadvantages / pros vs cons
- "Traditional approach vs new approach" science popularization figures
- Price tier comparison diagrams

Characteristics:

- Visually left-right / multi-column layout, strictly aligned
- Each column has a clear header (role / name / large image)
- Each row is a comparison dimension
- Uses checkmarks / crosses / colors / ratings to make clear distinctions
- At a glance you can tell "who wins"

## Scope

- Product vs product comparison diagrams
- Method / plan / school-of-thought comparison diagrams
- Pricing tier comparison diagrams
- Pros and cons / advantages and disadvantages comparison diagrams
- "Myth vs correct approach" science popularization

## When to use

- User mentions "comparison / vs / pk / pros and cons / dual-column / multi-column comparison / pricing tier"
- User wants "readers can tell at a glance which is more suitable for them"
- User wants a visual sense of "face-off / choice"

Do NOT use for:

- User wants "steps / process" → use `infographics/step-by-step-infographic.md`
- User wants "bento grid high-density information" → use `infographics/bento-grid-infographic.md`
- User wants "Slide single-page explanation" → use `slides-and-visual-docs/`
- User wants "pure engineering comparison table / configuration table" → use `academic-figures/qualitative-comparison-grid.md`

## Missing Information Priority Question Order

1. Number of comparison objects (2 / 3 / 4)
2. Name of each object
3. Number of comparison dimensions (recommend 4-7 dimensions, e.g.: price, performance, ease of use, scalability, ecosystem, learning curve)
4. Specific differences for each dimension under each object
5. Whether to have a clear "winner marker" (crown / TOP 1 label)
6. Color tone (neutral / warm / tech / black-white)
7. Aspect ratio (Xiaohongshu 3:4 / WeChat 16:9 / 1:1)

## Main Template: Dual-Column Comparison Infographic

Description

The entire image is divided into left and right columns, with the two compared objects as column headers (with logo / avatar / large image), below are 4-7 rows of comparison dimensions, each row uses icons + short text + colors / checkmarks-crosses to express differences, with a one-sentence conclusion at the bottom.

Prompt

```json
{
  "type": "Dual-column comparison infographic",
  "goal": "Generate a comparison diagram that lets readers tell at a glance which is more suitable for them",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"3:4 portrait\"}",
    "background": "{argument name=\"background\" default=\"warm off-white #F8F6F2\"}",
    "split_line": "{argument name=\"split_line\" default=\"A thin divider line in the center / or an interlocking VS symbol\"}"
  },
  "header": {
    "main_title": "{argument name=\"main_title\" default=\"React vs Vue: Which to Choose? 2026 Practical Comparison\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"7 dimensions to help you decide\"}"
  },
  "columns": [
    {
      "id": "left",
      "name": "{argument name=\"left_name\" default=\"React\"}",
      "color_theme": "{argument name=\"left_color\" default=\"cyan #61DAFB + dark gray\"}",
      "header_visual": "{argument name=\"left_visual\" default=\"React logo (large size + light background card)\"}",
      "tagline": "{argument name=\"left_tagline\" default=\"Flexible, strong ecosystem, large community\"}"
    },
    {
      "id": "right",
      "name": "{argument name=\"right_name\" default=\"Vue\"}",
      "color_theme": "{argument name=\"right_color\" default=\"emerald #41B883 + dark gray\"}",
      "header_visual": "{argument name=\"right_visual\" default=\"Vue logo (large size + light background card)\"}",
      "tagline": "{argument name=\"right_tagline\" default=\"Easy to pick up, great docs, more conventions\"}"
    }
  ],
  "comparison_rows": {
    "count": "{argument name=\"row_count\" default=\"7\"}",
    "structure": "Each row: left side dimension icon + dimension name (center) → left column performance + right column performance, using color blocks / checkmarks-crosses / 1-5 star ratings on the right side",
    "items": [
      "Learning Curve",
      "Speed to Productivity",
      "Ecosystem Maturity",
      "Job Market",
      "Performance",
      "TypeScript Experience",
      "Suitable Project Types"
    ],
    "marker_style": "{argument name=\"marker_style\" default=\"5-star rating + color contrast\"}",
    "highlight_winner_per_row": true
  },
  "footer": {
    "verdict": "{argument name=\"verdict\" default=\"Depends on team preference: choose Vue for quick onboarding, React for long-term ecosystem\"}",
    "winner_badge": {
      "enabled": "{argument name=\"winner_badge_enabled\" default=\"false\"}",
      "label": "{argument name=\"winner_badge_label\" default=\"Editor's Choice\"}",
      "position": "left | right"
    }
  },
  "constraints": {
    "must_keep": [
      "Left and right column widths symmetrical",
      "Each row height aligned",
      "Dimension name centered (belongs to the 'center pillar'), each side shows its own performance",
      "Colors should not make one side obviously overpower the other (unless explicit winner)",
      "Fonts consistent",
      "Data / ratings have visual markers, not pure text"
    ],
    "avoid": [
      "Left and right column sizes asymmetrical",
      "Dimension rows without icons",
      "Color conflicts making it hard to tell which side is which",
      "Only 1-2 comparison dimensions (information density too low)",
      "More than 10 comparison dimensions (each row becomes too cramped)",
      "Conclusion too subjective (best to summarize objectively in one sentence)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `left_name`, `right_name`, `row_count` (or specific dimension list)
- **Can default**: `background`, `marker_style` (5-star), `color_theme` (based on brand colors / defaults)
- **Can randomize**: dimension icon specific rendering, whether `split_line` is a thin line or VS symbol

### Auto-Fill Strategy

- User only provides two objects (e.g. "React vs Vue"): auto-infer 7 common comparison dimensions
- User only provides topic (e.g. "compare React and Vue"): fill in names, taglines, color themes (using brand colors)
- User doesn't mention winner: default no winner badge, conclusion is neutral
- User says "I want a clear face-off feel" → add VS symbol + winner badge + more contrasting colors

## Variant 1: Three-Column Comparison (Pricing Tiers / Three Plans)

```json
{
  "type": "Three-column pricing tier comparison infographic",
  "columns_count": 3,
  "column_examples": ["Free", "Pro", "Enterprise"],
  "rule": "Middle column slightly wider + background slightly brighter + 'Most Popular' corner tag, rows = feature dimensions + checkmarks / crosses + quantitative metrics"
}
```

Suitable for: SaaS pricing pages, plan comparisons, membership tier comparisons.

## Variant 2: Myth vs Correct Approach (Science Popularization)

```json
{
  "type": "Myth vs Correct approach dual-column comparison",
  "left_column": {
    "label": "❌ Common Myths",
    "color": "muted red / gray",
    "items": "3-5 common misconceptions"
  },
  "right_column": {
    "label": "✅ Correct Practices",
    "color": "muted green / fresh",
    "items": "3-5 correct statements + brief explanations"
  },
  "vibe": "education / science popularization / health / parenting"
}
```

Suitable for: health science popularization, parenting myths, consumer pitfall avoidance, fitness myths.

## Variant 3: Multi-Product × Multi-Dimension Review Matrix (Horizontal)

```json
{
  "type": "Multi-column horizontal review matrix",
  "layout": "Top row = multiple products (4-6), left column = review dimensions (5-8 rows), cells = ratings / checkmarks-crosses / brief text",
  "highlight_rule": "Highest score in each row highlighted with color + champion count tallied at the bottom of each column",
  "vibe": "media review diagrams, consumer reports"
}
```

Suitable for: camera reviews, laptop reviews, app roundups, SUV comparisons.

## Things to Avoid

- Dual-column width asymmetry (visual bias → appears unfair)
- Inconsistent row heights → comparison items don't align
- No dimension icons → hard to distinguish between rows
- Identical colors → loses left-right differentiation
- Overly strong color contrast (bright red on one side, bright green on the other) → looks like an emotional verdict
- Only 1/0 rating expressions → no gradation (recommend 1-5 stars / dots / progress bars)
- No conclusion footer → readers don't know which you're recommending
- Making the comparison figure into a pure text table → loses infographic's "readable at a glance" quality