# Mechanism / Pathway Diagram Template

This file is used for generating "academic mechanism diagrams / causal chains / transformation pathways / evolution mechanism figures":

- Mechanism / pathway analysis figures in paper body
- Reaction / transformation / degradation pathway diagrams
- Causal chain / multi-stage evolution diagrams
- Mechanism explanation slides for thesis defense presentations

Characteristics:

- Central object + multi-stage transformation pathway + result region
- Stage-based annotations (drying → pyrolysis → combustion → oxidation → emission, or similar causal sequences)
- White background + engineering-style low-saturation color palette (deep blue / slate blue / charcoal as primary, with ≤1 low-saturation warm accent for high-temperature/risk emphasis)
- Academic restraint style, **absolutely not marketing illustration or popular-science poster**

## Scope

- Combustion / chemical reaction / catalysis / degradation / aging / corrosion / attenuation mechanism schematics
- Biological / pharmaceutical / drug action / molecular interaction pathway diagrams (academic style, not popular-science illustration)
- Material phase transition / damage evolution / failure pathway
- Causal chain analysis / evolution pathway diagrams

## When to use

- User mentions "mechanism / mechanism / reaction pathway / transformation / evolution / causal / pathway / failure pathway"
- User wants the visual to be "mechanism figure in a paper, not popular-science illustration or marketing figure"
- User can already provide stage order or transformation relationships

Do NOT use for:

- User wants "method pipeline / system overview" → use `academic-figures/method-pipeline-overview.md`
- User wants "experimental apparatus / test system" → use `academic-figures/scientific-schematic.md`
- User wants "business process / decision diagram" → use `technical-diagrams/flowchart-decision.md`
- User wants "instructional steps, warm illustration feel" → use `infographics/step-by-step-infographic.md`

## Missing Information Priority Question Order

1. Mechanism / phenomenon general name (written in title or figure caption)
2. What is the central research object (particle / molecule / device / tissue / reaction system)
3. Stage order (recommend 3-6 stages; more than 6 consider grouping)
4. For each stage: stage name + brief description of the dominant process (phrase-style)
5. Whether there are branches / parallel paths / feedback loops
6. Whether to annotate high-temperature zones / risk zones / key reaction zones as local emphasis
7. Label language (Chinese / English / bilingual; paper figures usually English)
8. Aspect ratio (default horizontal 16:9; mechanism diagrams also commonly 4:3)

## Main Template: Central Object + Multi-stage Transformation + Result Region

📖 Description

The center is a simplified depiction of the research object (particle / molecular structure / device / reaction system), surrounded by "staged transformation pathways" expanding outward: from initial state through several intermediate mechanism stages to the final result region. All connections use academically restrained arrows, dramatic effects forbidden (no flames, no thick smoke, no glare).

📝 Prompt

```json
{
  "type": "Academic mechanism schematic (mechanism / pathway figure)",
  "goal": "Generate a mechanism schematic suitable for direct inclusion in an engineering or natural science paper, emphasizing clear causal pathways, academic restraint, and grayscale print readability",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "pure white #FFFFFF",
    "outer_padding": "60px around the diagram",
    "render_quality": "vector-clean look, anti-aliased edges, sharp text"
  },
  "title_caption": {
    "figure_label": "{argument name=\"figure_label\" default=\"Figure X.\"}",
    "caption": "{argument name=\"caption\" default=\"Schematic of the proposed mechanism.\"}",
    "position": "bottom-center, italic serif or compact sans-serif, smaller font size"
  },
  "central_object": {
    "label": "{argument name=\"object_label\" default=\"Biomass particle\"}",
    "depiction": "{argument name=\"object_depiction\" default=\"a simplified cross-sectional sketch of a porous biomass particle, line-art style, no photo realism\"}",
    "position": "horizontally centered, occupying roughly 25-35% of canvas width",
    "style": "thin line-art / engineering schematic, no 3D, no shading, no hyperreal texture"
  },
  "stages": {
    "count": "{argument name=\"stage_count\" default=\"5\"}",
    "items": [
      {
        "id": "M1",
        "name": "{argument name=\"stage_1_name\" default=\"Drying\"}",
        "summary": "{argument name=\"stage_1_summary\" default=\"moisture evaporation under heating\"}",
        "highlight": "{argument name=\"stage_1_highlight\" default=\"none\"}"
      },
      {
        "id": "M2",
        "name": "{argument name=\"stage_2_name\" default=\"Pyrolysis\"}",
        "summary": "{argument name=\"stage_2_summary\" default=\"thermal decomposition releasing volatiles\"}",
        "highlight": "{argument name=\"stage_2_highlight\" default=\"reaction zone\"}"
      },
      {
        "id": "M3",
        "name": "{argument name=\"stage_3_name\" default=\"Volatile Combustion\"}",
        "summary": "{argument name=\"stage_3_summary\" default=\"gas-phase combustion of released volatiles\"}",
        "highlight": "{argument name=\"stage_3_highlight\" default=\"high-temperature region\"}"
      },
      {
        "id": "M4",
        "name": "{argument name=\"stage_4_name\" default=\"Char Oxidation\"}",
        "summary": "{argument name=\"stage_4_summary\" default=\"surface oxidation of the remaining char\"}",
        "highlight": "{argument name=\"stage_4_highlight\" default=\"none\"}"
      },
      {
        "id": "M5",
        "name": "{argument name=\"stage_5_name\" default=\"Emission Formation\"}",
        "summary": "{argument name=\"stage_5_summary\" default=\"formation of NOx, CO, particulate matter\"}",
        "highlight": "{argument name=\"stage_5_highlight\" default=\"emission risk region\"}"
      }
    ]
  },
  "result_region": {
    "enabled": "{argument name=\"result_region_enabled\" default=\"true\"}",
    "label": "{argument name=\"result_region_label\" default=\"Outcome\"}",
    "items": "{argument name=\"result_region_items\" default=\"temperature distribution, combustion efficiency, emission characteristics\"}",
    "position": "rightmost block or bottom-right region, visually separated from stages but stylistically consistent"
  },
  "stage_block_style": {
    "shape": "rounded rectangle (corner radius ~6px) OR stage label + leader line directly attached to the central object",
    "size_per_stage": "consistent across all stages",
    "fill": "very light tint (e.g. #F1F5F9, #ECFEFF) — at most 2 different tints; use a low-saturation warm tint (e.g. #FEF3C7) only for stages whose 'highlight' is non-none",
    "border": "1.2px solid dark gray #334155",
    "title_text": "stage name in bold sans-serif (Helvetica / Inter / Arial / PingFang / Source Han Sans for CJK), 11-12pt",
    "summary_text": "single phrase, 9-10pt regular, no full sentence, no period"
  },
  "connectors": {
    "style": "thin arrows (1.2px) with simple triangle arrowheads, dark gray #334155",
    "rule": "connect stages in causal / temporal order, no crossing, no decorative curves; only label arrows when carrying a named quantity (e.g. 'heat flux', 'O2', 'volatiles')",
    "feedback_loop": {
      "enabled": "{argument name=\"feedback_loop\" default=\"false\"}",
      "rule": "if true, add one curved dashed arrow looping back, labeled e.g. 'self-propagating heat'"
    }
  },
  "highlight_strategy": {
    "rule": "for stages whose 'highlight' is non-none, apply ONLY a subtle low-saturation tint background (e.g. #FEF3C7 for high-temperature; #FEE2E2 for emission risk). NEVER use flames, smoke, glow, lens flare, or 3D heat-map effects",
    "max_highlighted_stages": 2
  },
  "constraints": {
    "must_keep": [
      "central object visually anchors the figure; stages radiate or flow outward in a stable reading order",
      "white background, no gradient, no decorative pattern",
      "color palette ≤ 3 main colors, must remain readable in grayscale print",
      "only sans-serif typography, no script / handwritten / display fonts",
      "stage labels are short phrases, never full sentences",
      "the figure must look like it came from a journal article, not a popular-science illustration",
      "all arrows aligned, no crossings unless the mechanism genuinely requires it"
    ],
    "avoid": [
      "exaggerated flames, smoke, sparks, glow, lens flare, motion blur",
      "3D rendering, metallic highlights, glossy fills",
      "cartoon mascots, emoji, decorative icons, hand-drawn wobble",
      "photo-realistic photography of equipment, products, or scenery",
      "marketing poster aesthetics, magazine cover aesthetics",
      "fabricated numbers, equations, or chemical formulas not provided by the user",
      "saturated brand-style colors (no neon, no vivid)",
      "watermarks, copyright stamps, vendor logos"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `object_label` / `object_depiction`, stage names, stage order
- **Can default**: `aspect_ratio` (16:9), `background` (white), `figure_label` / `caption`, color tints
- **Can randomize**: each stage's `summary` wording (academic polish when user provides gist), whether `highlight` is enabled (default none when not specified)

### Auto-Fill Strategy

- User provides phenomenon name + stage count but no per-stage details → ask back, **fabricating non-existent physical / chemical processes is forbidden**
- User provides stage names but no summaries → fill with academic phrases (keep ≤6 words)
- User doesn't mention feedback loops → default `feedback_loop: false`
- User says "Chinese paper / defense" → switch labels to Chinese + fonts PingFang / Source Han Sans

## Variant 1: Left → Center → Right Three-Section Causal Chain

```json
{
  "type": "Three-section causal chain mechanism diagram",
  "modify": {
    "layout": "Left = initial conditions / triggering factors; Center = multi-stage transformation mechanism; Right = final results / characterization",
    "rule": "Thicker spacing between the three sections (visual grouping), but maintain consistent strokes and fonts; left and right sections condensed to ≤4 items each",
    "use_case": "Mechanism diagrams requiring clear distinction of 'cause → process → result', e.g. 'biomass combustion → multi-stage reactions → emissions and char residue'"
  }
}
```

Suitable for: combustion / reaction engineering, degradation and aging, damage evolution, clinical causal pathways (academic style).

## Variant 2: Cyclic / Self-Exciting Mechanism

```json
{
  "type": "Cyclic self-exciting mechanism diagram",
  "modify": {
    "layout": "Stages arranged in a ring, arrows follow the ring clockwise; the cyclic driving force or key intermediate product is written in the center",
    "annotation": "Select 1-2 arrows on the ring and add dashed style labels 'positive feedback' / 'self-propagating'",
    "use_case": "Positive feedback mechanisms, autocatalytic reactions, chronic degradation cycles"
  }
}
```

Suitable for: autocatalysis, chain reactions, thermal runaway, chronic inflammation pathways.

## Variant 3: Multi-Branch Competing Pathways

```json
{
  "type": "Multi-branch competing pathways diagram",
  "modify": {
    "layout": "The central object branches outward into 2-3 parallel pathways, each representing a competing mechanism; each pathway connects to a different result region at the end",
    "annotation": "At the start of each pathway, label the controlling condition (temperature / O2 partial pressure / pH, etc.)",
    "use_case": "Mechanism diagrams that need to express 'the same precursor follows different mechanisms under different conditions'"
  }
}
```

Suitable for: pathway-selective reactions, phase separation, dominant reaction mechanisms at different temperature ranges.

## Things to Avoid

- Using rendered flames / thick smoke / explosions / glare to "look professional" → immediately degenerates into marketing illustration
- Stage blocks of inconsistent sizes, chaotic font sizes, mixing serif + sans-serif
- Using emoji or cartoon icons as stage illustrations
- Using saturated / neon / gradient backgrounds instead of restrained engineering colors
- Inserting non-existent chemical equations, physical constants, temperature values into the figure (**fabricating data is strictly forbidden**)
- Drawing the mechanism diagram as a complete equipment cross-section (should use `scientific-schematic.md`)
- Mixing comparison / multi-condition results (should use `multi-condition-comparison.md`) into the mechanism diagram