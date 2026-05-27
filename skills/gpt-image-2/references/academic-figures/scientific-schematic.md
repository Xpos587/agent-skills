# Scientific Concept / Principle Schematic Template

This file is used for generating "scientific concept / principle / experimental apparatus" schematics:

- Physics / chemistry / biology experimental apparatus diagrams
- Algorithm / math concept schematics (e.g. attention mechanism, manifold, coordinate systems)
- Mechanism / pathway / process schematics (cell pathways, chemical reactions)
- Textbook-style principle diagrams
- "How our field roughly works" concept figures in Nature / Science reviews

Characteristics:

- **Extremely high freedom**: every scientific schematic looks different, unlike pipeline / network diagrams that can be grid-structured
- Minimal white / light gray background
- Geometrically precise: scale bars / coordinate axes / angle alignment
- Simplified but not cartoon style (scientific rigor)
- Annotation lines + numbering + formulas
- Publication fonts (Helvetica / Inter / Computer Modern for math formulas)

> Design judgment: **This type of figure has extremely high freedom and rich variation; forcing JSON would constrain composition**. This template uses a **"structured natural language prompt + key parameters + examples" hybrid format**, controlling constraints without locking down composition.

## Scope

- Experimental apparatus schematics (optics / mechanics / fluid dynamics / chemical reactors)
- Biological mechanism / pathway / anatomy schematics
- Algorithm / math concept visualization (attention / convex set / manifold / coordinate transforms)
- Physical process schematics (waves / fields / particle trajectories)
- "Big picture" concept figures in review papers

## When to use

- User mentions "schematic / illustration / schematic / principle diagram / experimental apparatus / mechanism diagram / Nature style / textbook style"
- User wants "free composition, white background, geometrically precise, with academic feel"
- User's content is a **single concept / single apparatus / single mechanism** rather than a **pipeline / network / multi-method**

Do NOT use for:

- User wants "method pipeline" (multi-stage flow) → use `academic-figures/method-pipeline-overview.md`
- User wants "neural network architecture" → use `academic-figures/neural-network-architecture.md`
- User wants "data chart" → use `academic-figures/publication-chart.md`
- User wants "hand-drawn cartoon schematic" → use `infographics/hand-drawn-infographic.md`
- User wants "children's science" → use `scenes-and-illustrations/picture-book-scene.md`

## Missing Information Priority Question Order

1. What concept / apparatus / mechanism to explain? (one-sentence definition)
2. What is the main subject? (that core entity in the center — molecule / cell / lens / reactor / matrix / ...)
3. Supporting elements? (annotation lines / formulas / coordinate axes / parameters)
4. Style preference (Nature review style / textbook style / top-conference paper serious style / BioRender friendly style)
5. Whether math formula annotations are needed? Which ones?
6. Whether Chinese or English (default English)
7. Aspect ratio (papers commonly use 1:1, 4:3, 16:9)

## Main Template: Scientific Concept / Principle Schematic (Structured Natural Language)

📖 Description

The entire figure centers around one central concept / apparatus / mechanism, composed of minimal geometric elements + annotation lines + formulas + concise accent colors, achieving publication-grade clarity and rigor.

📝 Prompt (Structured Natural Language Template)

```
A scientific schematic illustration in the style of {argument name="reference_style" default="a Nature / Science methods figure"}.

CORE CONCEPT
The figure illustrates: {argument name="core_concept" default="how cross-attention works between a query sequence and a key/value sequence"}.

CENTRAL SUBJECT
The visual centerpiece is {argument name="central_subject" default="a 2D matrix grid representing query × key dot products, with arrows feeding in queries from the left and keys from the top"}.

SUPPORTING ELEMENTS
{argument name="supporting_elements" default="(1) a softmax curve diagram on the right showing how raw scores become attention weights; (2) a small inset showing the resulting weighted sum producing the output"}.

Each supporting element is positioned with deliberate spacing and connected to the central subject by thin labeled arrows or leader lines.

ANNOTATIONS
- Use leader lines (thin black, no arrowheads or tiny arrowheads) to label specific parts of the central subject.
- Each label is in {argument name="label_font" default="11pt sans-serif (Helvetica / Inter / Arial)"}.
- {argument name="annotation_count" default="4-6"} labels total — do NOT overcrowd.
- Use lowercase italic letters (a, b, c) for sub-figure labels in the top-left of each panel.

EQUATIONS
{argument name="equations_list" default="Show one or two key equations near the relevant region. Use Computer Modern / serif math font, italic variables. Example: Attn(Q,K,V) = softmax(QK^T / √d_k) V"}

Equations should be small but readable, placed adjacent to the part of the figure they explain (not floating in the corner).

COLOR PALETTE
- Limit total to {argument name="color_count" default="3-4"} muted, academic colors:
  - {argument name="primary_color" default="deep blue #1E3A8A"} — for the central subject
  - {argument name="secondary_color" default="warm orange #D97706"} — for the highlighted / contrasting flow
  - {argument name="neutral_color" default="medium gray #475569"} — for annotation lines and supporting structures
  - white background, near-white shading for sub-regions
- The figure must remain readable when printed in grayscale: rely on shape and labels, not color alone.

LAYOUT
- {argument name="layout_style" default="single-panel, central subject occupies ~60% of the canvas, supporting elements arranged around it"}.
- Generous whitespace (~25% of canvas), rigorous alignment to an invisible grid.
- Aspect ratio: {argument name="aspect_ratio" default="4:3"}.

STYLE ENFORCEMENT
- Crisp vector-clean lines (no anti-aliasing artifacts, no jitter)
- All shapes are geometrically precise (perfect circles, exact angles)
- All text typeset, NEVER hand-drawn lettering
- Background pure white #FFFFFF or very light gray
- NO 3D extrusion, NO drop shadow, NO gradient fill, NO glossy highlight
- NO cartoon characters, NO emoji, NO decorative ornaments
- Should look like it was generated with TikZ / Inkscape / Adobe Illustrator for a peer-reviewed publication

CAPTION (optional, drawn below figure)
{argument name="caption_text" default="Figure 2. Illustration of the cross-attention mechanism. Queries (Q) attend to keys (K) via scaled dot-product, producing attention weights that aggregate values (V)."}
```

### Parameter Strategy

- **Must ask**: `core_concept`, `central_subject` at minimum one sentence description
- **Can default**: `reference_style` (Nature methods style), `color_count` (3-4), color trio (deep blue + orange + gray), `label_font`, `aspect_ratio`
- **Can randomize**: annotation placement angles, leader line routing (should avoid key content), whether equations are enabled

### Auto-Fill Strategy

- User says "I want to draw an attention mechanism schematic" but no details → auto-use default for cross-attention schematic, ask if self-attention needs a separate figure
- User says "optical double-slit interference experiment" → central_subject = double-slit barrier + screen + incident light, supporting = interference fringe small figure + formula d sinθ = mλ
- User says "cell receptor signaling pathway" → use BioRender friendly style: rounded cell membrane + receptor + ligand + internal signaling chain
- User doesn't provide reference_style: guess by field — CV/ML use "top-conference paper style"; biology use "BioRender / Nature methods style"; physics use "textbook + formula style"
- User says "no English, all Chinese" → switch label_font to Source Han Sans / Song typeface + formulas keep LaTeX math font

## Variant 1: Experimental Apparatus Schematic (Optics / Chemistry)

```
Modify the main template:

CENTRAL SUBJECT
A precise schematic of an experimental apparatus, drawn in side view (orthographic projection).

LAYOUT
- Equipment components arranged from left to right along the optical / fluid path:
  light source / reactant inlet → first optical / chemical element → second element → ... → detector / outlet
- Components shown as simplified geometric primitives:
  - Lasers / lamps: small box with arrows indicating beam direction
  - Lenses: standard biconvex / planoconvex symbol (two arcs)
  - Mirrors: thin angled lines with hatching on the back
  - Reactors: round-bottom flask outline
  - Detectors: rectangular box with diagonal corner stripes
- Beam / fluid path drawn as a thin colored line (e.g. red for light, blue for fluid)

ANNOTATIONS
- Each component labeled with its role and (if relevant) a parameter (e.g. f = 50mm, λ = 532nm)
- Arrows show direction of light / flow

VIBE
Like a JOSA / Optics Letters experimental setup figure, or like a chemistry textbook reaction apparatus.
```

Suitable for: optical experiments, chemical reaction apparatus, fluid / mechanical apparatus, semiconductor manufacturing process schematics.

## Variant 2: Biological / Medical Mechanism Schematic (BioRender Style)

```
Modify the main template:

CENTRAL SUBJECT
A simplified biological structure (cell membrane / cell / tissue / organ / molecule).

STYLE
- BioRender-friendly: rounded organic shapes, slightly stylized but anatomically reasonable
- Color-coded biology palette: warm membrane (peach / coral), cool nucleus / organelles (blue / purple), bright signaling molecules (yellow / green)
- 3D suggestion via subtle shading (single-direction soft shading, no harsh highlights)

ANNOTATIONS
- Each structure labeled with its biological name (italic Latin / standard nomenclature)
- Signaling pathways drawn as arrows with mechanism keywords ("phosphorylation", "binding", "translocation")
- If multi-step, number each step and provide a brief side caption

VIBE
Like a Cell / Nature review pathway figure, balanced between scientific accuracy and visual approachability.
```

Suitable for: molecular biology pathways, cellular mechanisms, anatomy schematics, drug action mechanisms.

## Variant 3: Math / Algorithm Concept Visualization

```
Modify the main template:

CENTRAL SUBJECT
A mathematical / algorithmic concept rendered as geometry:
- vectors as arrows, matrices as grids, functions as curves, manifolds as surfaces
- coordinate systems with labeled axes (x, y, z), origin marked

STYLE
- Clean TikZ / Asymptote aesthetic
- Heavy use of LaTeX-rendered equations integrated into the figure
- Greek letters and mathematical symbols throughout
- Sparingly use color — usually 2 colors (black + one accent) to highlight what's being discussed

ANNOTATIONS
- Equation snippets next to relevant geometry
- Brief textual descriptions on the side ("optimal transport plan minimizes ...")
- Sub-figure labels (a), (b), (c) for multi-panel concept figures

VIBE
Like a figure from "Convex Optimization" by Boyd, or from a SIGGRAPH technical paper.
```

Suitable for: optimization theory, geometry / topology, probability distributions, signal processing, computer graphics mathematical foundations.

## Things to Avoid

- Cartoonized, exaggerated elements → loses scientific rigor
- Gradients / glass textures / drop shadows → looks like PPT not a paper
- More than 4 colors / high saturation / neon colors
- Formulas in non-math fonts (must use italic variables + serif math font)
- Mixed Chinese and English (unless explicitly bilingual)
- Decorative background textures / patterns
- Annotation lines crossing through the main subject / labels colliding
- Using emoji as biological / chemical element icons
- Multiple unrelated concepts crammed into one figure (should split)
- Blurry or low-resolution (paper figures must be vector-grade clarity)
- Freehand "sketch feel" → use `infographics/hand-drawn-infographic.md` instead; this template must be geometrically precise