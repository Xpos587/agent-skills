# Paper Method Pipeline Overview Figure Template

This file is used for generating "that overview figure on the first page of a paper's method section":

- Top-conference paper method section opening figure (CVPR / NeurIPS / ICLR / ACL / SIGGRAPH etc.)
- System overview / pipeline figure
- Survey paper framework concept diagram
- Experimental apparatus / data flow overview
- Thesis defense method overview slides

Characteristics:

- Horizontal 3-6 stage blocks
- Clear directed data flow between each stage
- Each stage has: stage name + simplified illustration + input/output sub-labels
- Overall white / light gray background, black or dark gray main lines
- Publication fonts (Helvetica / Inter / Arial), restrained accent colors
- **Minimal, geometrically precise, grayscale-print readable**

## Scope

- Paper method overview / framework figure
- Survey paper pipeline overview
- System overview diagram ("our method has 4 steps: ...")
- Data flow / signal flow overview
- Experimental workflow overview

## When to use

- User mentions "paper / paper / method / pipeline / framework / overview / survey / top conference / arXiv"
- User wants the visual "minimal, white background, black lines, geometrically precise, like a CVPR paper overview figure"
- User has specific stage descriptions ready

Do NOT use for:

- User wants "neural network architecture diagram" (layer blocks + tensor shapes) → use `academic-figures/neural-network-architecture.md`
- User wants "concept / principle schematic" (high-degree-of-freedom scientific illustration) → use `academic-figures/scientific-schematic.md`
- User wants "step-by-step tutorial" (illustration feel, warm) → use `infographics/step-by-step-infographic.md`
- User wants "engineering system architecture diagram" (dark + semi-transparent blocks) → use `technical-diagrams/system-architecture.md`
- User wants "business flowchart" → use `technical-diagrams/flowchart-decision.md`

## Missing Information Priority Question Order

1. Method / system general name (written in figure title or caption)
2. Number of stages (recommend 3-6, more than 6 consider layering)
3. For each stage: name + main operation + input + output
4. Data modality (image / text / point cloud / audio / multimodal) — determines simplified illustrations within stages
5. Whether there are skip connections / feedback loops / multiple branches
6. Aspect ratio (horizontal 16:9 or 2:1, fits paper two-column format)
7. Whether English labels are needed (paper figures usually English)

## Main Template: Horizontal N-Stage Method Pipeline Figure

📖 Description

The entire figure flows horizontally: starting from the leftmost input, sequentially through 3-6 rectangular / rounded-rectangular stage blocks, each containing a simplified illustration + stage name + input/output sub-labels, connected by arrows, with output results on the far right. Overall restrained, strictly aligned, geometrically precise.

📝 Prompt

```json
{
  "type": "Academic paper method pipeline overview figure",
  "goal": "Generate a pipeline overview figure suitable for direct inclusion on the first page of a top-conference paper method section, minimal, white background, geometrically precise, publication-grade readability",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "pure white #FFFFFF or very light gray #FAFAFA",
    "outer_padding": "60px around the diagram",
    "render_quality": "vector-clean look, anti-aliased edges, sharp text"
  },
  "title_caption": {
    "figure_label": "{argument name=\"figure_label\" default=\"Figure 1.\"}",
    "caption": "{argument name=\"caption\" default=\"Overview of our proposed pipeline.\"}",
    "position": "bottom-center, italic serif or compact sans-serif, smaller font size"
  },
  "input": {
    "label": "{argument name=\"input_label\" default=\"Input Image\"}",
    "thumbnail": "{argument name=\"input_thumbnail\" default=\"a small representative thumbnail (e.g. an RGB image, a text snippet, a point cloud)\"}",
    "position": "leftmost, vertically centered"
  },
  "stages": {
    "count": "{argument name=\"stage_count\" default=\"4\"}",
    "items": [
      {
        "id": "S1",
        "name": "{argument name=\"stage_1_name\" default=\"Feature Extractor\"}",
        "icon_or_glyph": "{argument name=\"stage_1_glyph\" default=\"a stack of 3 small horizontal bars representing CNN feature maps\"}",
        "sub_label": "{argument name=\"stage_1_sub\" default=\"ResNet-50\"}"
      },
      {
        "id": "S2",
        "name": "{argument name=\"stage_2_name\" default=\"Multi-scale Encoder\"}",
        "icon_or_glyph": "{argument name=\"stage_2_glyph\" default=\"a small triangle / pyramid representing multi-scale\"}",
        "sub_label": "{argument name=\"stage_2_sub\" default=\"FPN-style\"}"
      },
      {
        "id": "S3",
        "name": "{argument name=\"stage_3_name\" default=\"Cross-attention Decoder\"}",
        "icon_or_glyph": "{argument name=\"stage_3_glyph\" default=\"two interleaved arrows representing cross-attention\"}",
        "sub_label": "{argument name=\"stage_3_sub\" default=\"Transformer\"}"
      },
      {
        "id": "S4",
        "name": "{argument name=\"stage_4_name\" default=\"Prediction Head\"}",
        "icon_or_glyph": "{argument name=\"stage_4_glyph\" default=\"a small grid representing dense prediction\"}",
        "sub_label": "{argument name=\"stage_4_sub\" default=\"MLP × 2\"}"
      }
    ]
  },
  "output": {
    "label": "{argument name=\"output_label\" default=\"Predicted Mask\"}",
    "thumbnail": "{argument name=\"output_thumbnail\" default=\"a small representative output (e.g. a segmentation mask, a 3D model, a generated image)\"}",
    "position": "rightmost, vertically centered"
  },
  "stage_block_style": {
    "shape": "rounded rectangle (corner radius ~6px)",
    "size_per_stage": "around 120px wide × 80px tall, all stages identical size",
    "fill": "very light tint (e.g. #F1F5F9, #ECFEFF, #FEF9C3) — at most 2 different tints used to group stages by category",
    "border": "1.2px solid dark gray #334155",
    "title_text": "stage name in bold sans-serif (Helvetica / Inter / Arial), 11-12pt, top-center inside block",
    "icon_position": "centered inside block, takes ~50% of block height",
    "sub_label_text": "sub-label in italic gray, below stage name"
  },
  "connectors": {
    "style": "thin black arrows (1.2px) with simple triangle arrowheads",
    "rule": "horizontal flow left → right; small label above arrow only when carrying intermediate data type (e.g. 'feature map H/4 × W/4 × 256')",
    "skip_connections": {
      "enabled": "{argument name=\"skip_connections\" default=\"false\"}",
      "rule": "if true, draw curved arrows that arc above the main flow with dashed style, label them 'skip' / 'residual'"
    }
  },
  "extras": {
    "loss_branch": {
      "enabled": "{argument name=\"loss_branch_enabled\" default=\"false\"}",
      "label": "{argument name=\"loss_branch_label\" default=\"L = L_cls + λ L_reg\"}",
      "rule": "if enabled, draw a small dashed branch from output back to a 'Loss' box, formula in italic"
    },
    "color_legend": {
      "enabled": "{argument name=\"color_legend_enabled\" default=\"false\"}",
      "rule": "if multiple stage tints are used, add a tiny legend bottom-right explaining each color group"
    }
  },
  "constraints": {
    "must_keep": [
      "all stage blocks identical size and vertically aligned",
      "white or near-white background, no gradient, no decoration",
      "only sans-serif typography, no script / handwritten / display fonts",
      "color palette ≤ 4 colors total, must remain readable in grayscale print",
      "input thumbnail and output thumbnail same size, both have a thin border",
      "arrows must not overlap stage blocks; labels must not collide with arrows",
      "use English labels by default unless user requested otherwise",
      "the figure should look like it came directly from a CVPR / NeurIPS PDF"
    ],
    "avoid": [
      "3D effects, drop shadows, gradients, glossy fills",
      "cartoon icons, emoji, hand-drawn wobble",
      "saturated colors (no neon, no vivid)",
      "Helvetica + serif mixed in same diagram",
      "decorative background patterns / textures",
      "illustrative photo backgrounds inside stage blocks",
      "stage blocks of unequal size or unaligned baselines",
      "Chinese mixed with English labels unless explicitly bilingual"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `stage_count`, name of each stage
- **Can default**: `aspect_ratio` (16:9), `background` (white), `figure_label` / `caption`, stage block size / colors
- **Can randomize**: each stage's `icon_or_glyph` specific rendering (infer when user doesn't specify)

### Auto-Fill Strategy

- User provides method name and "I have 4 stages" but doesn't say what each stage is → ask back (cannot fabricate algorithm details)
- User provides stage name but no sub_label → leave empty or auto-infer (fill in typical options like "ResNet-50" when inferable)
- User doesn't mention skip connections → default `skip_connections: false`
- User doesn't mention loss → default `loss_branch: false` (only add when user explicitly wants a training pipeline)
- User says "Chinese paper" / "defense" → switch labels to Chinese + fonts PingFang / Source Han Sans

## Variant 1: Dual-Row Multi-Branch Pipeline

```json
{
  "type": "Dual-row multi-branch pipeline diagram",
  "modify": {
    "layout": "Upper and lower rows of stages flowing in parallel; merging at a fusion block in the center",
    "use_case": "Multi-modal fusion methods (e.g. visual + text, or RGB + depth)",
    "rule": "Upper row processes one modality, lower row processes another, merging at a central fusion block before output"
  }
}
```

Suitable for: multimodal, dual-stream networks, teacher-student methods.

## Variant 2: Training + Inference Dual Pipeline Comparison

```json
{
  "type": "Training vs Inference comparison pipeline diagram",
  "modify": {
    "layout": "Two rows: upper row 'Training Phase' (with loss, ground truth input, gradient backflow), lower row 'Inference Phase' (forward-only, lightweight)",
    "annotation": "Left side uses large braces labeled 'Training' / 'Inference'",
    "use_case": "Methods that need to clearly distinguish training and inference flows"
  }
}
```

Suitable for: knowledge distillation, self-supervised pre-training, semi-supervised methods.

## Variant 3: Iterative / Recurrent Pipeline

```json
{
  "type": "Iterative / recurrent pipeline diagram",
  "modify": {
    "layout": "Stages arranged horizontally, but the last stage has a curved arrow looping back to the second stage, forming a cycle",
    "annotation": "Label the cycle arrow with 'iterate × N' or 'until convergence'",
    "use_case": "Iterative optimization, diffusion denoising, diffusion model timestep flow"
  }
}
```

Suitable for: diffusion models, iterative refinement methods, energy-based models.

## Variant 4: Engineering Research Roadmap (Left / Center / Right Three-Section)

```json
{
  "type": "Engineering research roadmap",
  "modify": {
    "layout": "Left / Center / Right three-section: left = research object and background (simplified line-art depiction), center = multi-step analysis path (4-7 academic modules), right = output and results orientation (3-4 phrased conclusion directions)",
    "rule": "Three-section width ratio approximately 2:5:2; left and right sides use academic phrases + simplified line-art, no commercial icons / realistic rendering / dramatic flame and smoke effects; center analysis path modules are uniform in size, strictly aligned, with concise connection relationships",
    "tone": "Closer to a fusion of high-quality Graphical Abstract and method roadmap, not an office flowchart or commercial poster",
    "stage_naming_examples_for_engineering": [
      "fuel / material characterization",
      "kinetics / thermodynamics analysis",
      "experimental setup OR numerical model",
      "boundary / operating condition design",
      "process simulation or experiment",
      "field / behavior evaluation",
      "emission / performance analysis"
    ],
    "color_palette": "deep blue / slate blue / charcoal as main; one low-saturation amber accent for high-temperature or risk modules ONLY when user signaled it; ≤ 3 main colors total",
    "data_authenticity": "if no real data is provided, do NOT invent equations, kinetic constants, temperature values, emission factors, or chart numbers; render module summaries as qualitative phrases only",
    "use_case": "Energy and power, combustion, thermal engineering, environmental engineering, materials, chemical engineering research roadmaps and high-quality Graphical Abstract fusion needs; CS/CV/ML types should use the main template"
  }
}
```

Suitable for: energy and power, combustion, thermal engineering, environmental engineering, chemical engineering, materials — research roadmaps and high-quality Graphical Abstract fusion needs; CS/CV/ML types should use the main template.

## Things to Avoid

- Using gradients / drop shadows / glass textures → immediately "PPT style" instead of paper style
- Stage blocks of unequal size / misaligned heights
- Using emoji / cartoon icons as stage glyphs
- Using Comic Sans / handwritten fonts as title fonts
- More than 4 colors or oversaturated
- Input/output thumbnails with visibly different resolutions
- Arrows crossing through stage blocks or labels colliding
- Mixing Chinese and English labels (unless explicitly bilingual)
- Drawing "comparison methods" on the same pipeline (should use `qualitative-comparison-grid.md`)
- Cramming network layer details (convolution kernel size, activation functions) into the pipeline figure (this belongs in `neural-network-architecture.md`)