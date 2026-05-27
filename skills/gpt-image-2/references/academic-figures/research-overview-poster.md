# Thesis Proposal / Defense / Presentation Research Overview Figure Template

This file is used for generating "research overview figures for thesis proposal opening slides / thesis presentation opening slides / group meeting guide pages":

- Research framework diagrams for master's/doctoral thesis proposal opening slides
- Overview figures for mid-term / final thesis defense opening slides
- Guide pages for group meeting / academic presentation PPT
- Research overview on lab homepage / project introduction pages

Characteristics:

- High-level, easy to read, suitable for single PPT slide display
- 5 core modules: Background / Objective / Research Module 1 / Research Module 2 / Expected Outcomes
- White background, low-saturation engineering colors, ≤3 main colors, **paper figure feel not business consulting pitch deck feel**
- Text distilled to short phrases, text walls forbidden

## Scope

- Thesis proposal / mid-term / defense opening slides (academic presentations)
- Group meeting guide pages / project presentations / Lab meeting cover
- Research framework diagrams in project proposal documents (academic style)
- Faculty personal homepage / Lab homepage "current research" sections

## When to use

- User mentions "thesis proposal / defense / overview figure / research framework / PPT opening / guide page / lab homepage"
- User wants the visual "academic defense PPT opening style, formal restrained engineering-style, not consulting pitch deck style"
- User can provide around 5 core modules

Do NOT use for:

- User wants "journal submission Graphical Abstract" → use `academic-figures/graphical-abstract.md`
- User wants "method pipeline" → use `academic-figures/method-pipeline-overview.md`
- User wants "business / investor pitch deck cover" → use `slides-and-visual-docs/visual-report-page.md`
- User wants "brand hero poster" → use `poster-and-campaigns/brand-poster.md`

## Missing Information Priority Question Order

1. Topic / research theme (written in title area)
2. Defense type (thesis proposal / mid-term / final / group meeting / project proposal) — determines tone and module composition
3. Names of 5 core modules (default: Background / Objective / Research Content 1 / Research Content 2 / Expected Outcomes)
4. Whether to include a core viewpoint / key question (strongly recommended; written below Background module)
5. Whether to include a simplified depiction of the research object (particle / device / process / system)
6. Label language (Chinese / English / bilingual; Chinese defenses usually Chinese-primary with English subtitles)
7. Aspect ratio (default 16:9 fits PPT; 4:3 fits older PPT templates)

## Main Template: Upper-Middle-Lower Three-Layer + Five-Module Research Overview

📖 Description

The entire figure is divided into three layers: "top theme + middle core modules + bottom result-orientation". The middle layer contains 4-5 research content modules, presenting a hierarchical, strictly aligned academic layout that **absolutely does not resemble a business pitch deck PPT**.

📝 Prompt

```json
{
  "type": "Academic research overview figure (research overview / framework figure for thesis defense)",
  "goal": "Generate a research overview figure suitable for direct inclusion in a thesis proposal / defense PPT opening slide, formal and restrained, white background, engineering color palette, clearly paper-figure feel, absolutely no business pitch feel",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "pure white #FFFFFF",
    "outer_padding": "60px around the diagram",
    "render_quality": "vector-clean look, anti-aliased edges, sharp text"
  },
  "title_block": {
    "main_title": "{argument name=\"main_title\" default=\"Research Overview\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"e.g. thesis topic in one short phrase\"}",
    "occasion_label": "{argument name=\"occasion_label\" default=\"Thesis Proposal Defense\"}",
    "position": "top-center, main_title in bold sans-serif 18-22pt, subtitle in regular 12-14pt below, occasion_label in italic gray 10pt at top-right"
  },
  "background_section": {
    "label": "{argument name=\"background_label\" default=\"Background & Problem\"}",
    "summary": "{argument name=\"background_summary\" default=\"a short phrase stating why this matters and what gap exists\"}",
    "key_question": "{argument name=\"key_question\" default=\"a single research question, expressed as one sentence ≤ 18 words\"}",
    "position": "upper-middle band, full width, visually anchored as 'context'"
  },
  "objective_section": {
    "label": "{argument name=\"objective_label\" default=\"Objective\"}",
    "summary": "{argument name=\"objective_summary\" default=\"a short phrase stating the research goal\"}",
    "position": "directly below background, narrower than background, centered"
  },
  "research_modules": {
    "count": "{argument name=\"module_count\" default=\"3\"}",
    "items": [
      {
        "id": "RM1",
        "name": "{argument name=\"module_1_name\" default=\"Characterization\"}",
        "summary": "{argument name=\"module_1_summary\" default=\"a short phrase stating what is studied / measured\"}",
        "method_hint": "{argument name=\"module_1_method\" default=\"thermogravimetric analysis\"}"
      },
      {
        "id": "RM2",
        "name": "{argument name=\"module_2_name\" default=\"Modeling\"}",
        "summary": "{argument name=\"module_2_summary\" default=\"a short phrase stating the modeling / simulation focus\"}",
        "method_hint": "{argument name=\"module_2_method\" default=\"CFD combustion model\"}"
      },
      {
        "id": "RM3",
        "name": "{argument name=\"module_3_name\" default=\"Optimization\"}",
        "summary": "{argument name=\"module_3_summary\" default=\"a short phrase stating optimization or application focus\"}",
        "method_hint": "{argument name=\"module_3_method\" default=\"parameter sweep + emission analysis\"}"
      }
    ],
    "layout": "horizontal row of equal-width modules in the central band, all modules identical size and identical style"
  },
  "expected_outcome_section": {
    "label": "{argument name=\"outcome_label\" default=\"Expected Outcomes\"}",
    "items": "{argument name=\"outcome_items\" default=\"3-4 short phrases listing deliverables, e.g. 'kinetics database', 'optimized operating window', 'engineering recommendations'\"}",
    "position": "bottom band, full width, visually distinct from research_modules but stylistically consistent"
  },
  "module_block_style": {
    "shape": "rounded rectangle (corner radius ~8px) OR stage label + thin underline",
    "size_per_module": "all modules identical size, vertically aligned",
    "fill": "very light tint (e.g. #F1F5F9, #ECFEFF) — at most 2 different tints; modules of the same role share the same tint",
    "border": "1.2px solid #334155",
    "title_text": "module name in bold sans-serif (PingFang SC / Source Han Sans for CJK; Inter / Helvetica / Arial for english), 13-14pt",
    "summary_text": "single phrase, 10-11pt regular, 1-2 lines max, no period",
    "method_hint_text": "italic gray 9-10pt, below summary"
  },
  "connectors": {
    "style": "thin arrows (1.2px) with simple triangle arrowheads, dark gray #334155",
    "rule": "vertical flow background → objective → modules → outcomes; modules are horizontally parallel (no inter-module arrows unless logically required)",
    "decoration": "none; no curved arcs, no dashed unless explicitly indicating a feedback loop"
  },
  "color_palette": {
    "rule": "≤ 3 main colors total, drawn from a low-saturation engineering set: deep blue #1E3A8A / slate blue #3B82F6 / charcoal #1F2937; allow ONE low-saturation accent (e.g. amber #F59E0B) for the outcome band only if user signaled emphasis",
    "must_print_grayscale_readable": true
  },
  "typography": {
    "language": "{argument name=\"language\" default=\"chinese\"}",
    "rule": "chinese → PingFang SC / Source Han Sans; english → Inter / Helvetica / Arial; bilingual → primary line larger, secondary line smaller and gray",
    "consistency": "all module titles identical size; all summaries identical size; never mix serif and sans-serif"
  },
  "constraints": {
    "must_keep": [
      "all research modules identical size, vertically aligned, equal weight",
      "white background, no gradient, no decorative pattern",
      "language and font consistent across the entire figure",
      "summaries are short phrases, never full paragraphs",
      "the figure must look like the cover slide of an academic defense, not a corporate roadmap or pitch deck",
      "color palette ≤ 3 main colors, must remain readable in grayscale print"
    ],
    "avoid": [
      "consulting / pitch-deck aesthetics, brand campaign aesthetics",
      "decorative icons, emoji, mascots, hand-drawn wobble",
      "3D rendering, glossy fills, lens flare, drop shadow blocks",
      "stock-photo backgrounds, photographic hero images",
      "fabricated quantitative claims (no '+30% efficiency', '150 samples' unless user provided them)",
      "saturated brand colors, neon, vivid gradients",
      "dense text walls; no module summary should exceed 2 lines",
      "watermarks, copyright stamps, university / lab logos unless explicitly requested"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `main_title`, names of 5 core modules (Background / Objective / Research Content 1-N / Expected Outcomes)
- **Can default**: `aspect_ratio` (16:9), `background` (white), `color_palette` (deep blue / slate blue / charcoal)
- **Can randomize**: `method_hint` wording (academic polish when user provides method name); `occasion_label` (thesis proposal / mid-term / final / group meeting)

### Auto-Fill Strategy

- User provides topic but no modules → ask for 3-4 research modules, **fabricating research content is forbidden**
- User provides `key_question` exceeding 18 words → proactively suggest condensing or splitting into 2 sub-questions
- User doesn't provide expected outcomes → use placeholder phrases (e.g. "deliverable 1: ...") and mark for user to fill in
- User says "Chinese defense / Chinese PPT" → `language` defaults to Chinese, main title in Chinese + English subtitle (smaller size + gray)

## Variant 1: Center Theme + Surrounding Modules (Radial)

```json
{
  "type": "Center theme + surrounding modules research overview",
  "modify": {
    "layout": "Place a simplified depiction of the research theme / research object at the center; arrange 4 research modules around it in a ring or four quadrants; leave a results band at the bottom",
    "rule": "Central object occupies 25-30% of the canvas; surrounding modules equal in size, equal spacing, strictly aligned",
    "use_case": "Suitable for systems-type / platform-type projects, where research modules are parallel rather than sequentially dependent"
  }
}
```

Suitable for: platform-type projects, comprehensive topics, research overviews with multiple parallel research directions.

## Variant 2: Left-Right Dual-Column (Left = Research Content, Right = Roadmap / Timeline)

```json
{
  "type": "Left-right dual-column research overview",
  "modify": {
    "layout": "Left column = research content modules (3-4 vertically stacked); right column = timeline / roadmap / milestones (minimal gantt-style)",
    "rule": "Left-right column width ratio approximately 3:2; right column timeline uses thin lines + node circles, with month or semester labels next to nodes",
    "use_case": "Thesis proposals requiring a clear 'what to do + when to do it' project plan"
  }
}
```

Suitable for: thesis proposals, project proposal documents requiring progress plans.

## Variant 3: Minimal Version (Research Modules Only, No Timeline / No Outcome Band)

```json
{
  "type": "Minimal research overview",
  "modify": {
    "layout": "Remove expected_outcome_section and timeline; keep only title + background/key_question + 3-4 research modules",
    "use_case": "Group meeting guide pages or lab meeting covers, only needing to quickly highlight 'what will be discussed today'"
  }
}
```

Suitable for: group meetings / Lab meetings / course presentations.

## Things to Avoid

- Drawing the research overview as a business consulting pitch deck style (dark background + large color blocks + brand colors) → immediately "non-academic"
- Using emoji / business icons / cartoon illustrations to decorate research modules
- Writing research modules as complete paragraphs, each exceeding 2 lines → visually cluttered
- Fabricating specific percentages / data metrics in "Expected Outcomes" (**fabricating data is strictly forbidden**)
- Making one research module visibly larger than others (should be equal weight)
- Using saturated / gradient / glass texture decorative backgrounds
- Forcing school / lab logos or watermarks (unless user explicitly requests)
- Cramming a detailed method pipeline figure (should use `method-pipeline-overview.md`) into the overview