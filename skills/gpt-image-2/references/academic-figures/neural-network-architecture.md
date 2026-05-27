# Neural Network Architecture Diagram Template

This file is used for generating "that kind of neural network architecture diagram in papers":

- Transformer / Encoder-Decoder architecture diagrams
- U-Net / FPN / multi-scale network architectures
- GAN / Diffusion / VAE architectures
- Attention mechanism schematics
- Custom model architecture diagrams

Characteristics:

- Multiple layer blocks arranged along data flow direction (horizontal or vertical)
- Each layer block has: layer name + tensor shape annotation (H × W × C)
- Skip connections / residual / attention connections clearly drawn
- Color-coded different layer types (Conv / Attention / FC / Norm)
- Publication-grade, white background, restrained

## Scope

- Model architecture figures in papers
- Survey paper frameworks
- Thesis defense model introduction slides
- Teaching slides for network schematics

## When to use

- User mentions "network architecture / neural network architecture / model architecture / Transformer / U-Net / GAN / Diffusion / VAE"
- User wants "clear layer hierarchy, standard tensor shapes, skip connections at a glance"
- User wants the visual "paper style, white background, color-coded layer types"

Do NOT use for:

- User wants "method pipeline overview" (multi-stage business flow) → use `academic-figures/method-pipeline-overview.md`
- User wants "system architecture diagram" (frontend + backend + DB) → use `technical-diagrams/system-architecture.md`
- User wants "data flow / ER diagram" → use `technical-diagrams/er-diagram.md`
- User wants "concept schematic / attention visualization" (high freedom) → use `academic-figures/scientific-schematic.md`

## Missing Information Priority Question Order

1. Model type (Encoder-Decoder / U-Net / Transformer / GAN / Diffusion / custom)
2. Backbone network layer count / per-layer type (e.g. "6-layer Transformer encoder + 6-layer decoder + 8-head attention")
3. Tensor shapes (input resolution / channel count / sequence length)
4. Whether there are skip connections / residual / cross-attention
5. Whether there are multi-task / multi-head outputs
6. Whether Chinese labels are needed (paper figures usually English)
7. Aspect ratio (horizontal 16:9 / 2:1, fits paper two-column format)

## Main Template: Transformer / Encoder-Decoder Architecture Diagram

📖 Description

The entire figure flows horizontally: left input embedding → multi-layer encoder blocks → cross-attention → multi-layer decoder blocks → right output head. Each layer block is annotated with layer type and tensor shape, skip connections shown with curved dashed lines.

📝 Prompt

```json
{
  "type": "Neural network architecture diagram",
  "goal": "Generate a publication-grade network architecture diagram: clear layer hierarchy, tensor shape annotations, distinct skip connections, grayscale-print readable",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "white #FFFFFF",
    "outer_padding": "60px"
  },
  "model_meta": {
    "name": "{argument name=\"model_name\" default=\"Our Transformer\"}",
    "input_spec": "{argument name=\"input_spec\" default=\"Input Image: 224×224×3\"}",
    "output_spec": "{argument name=\"output_spec\" default=\"Class Logits: 1000\"}"
  },
  "layer_groups": {
    "rule": "use color-coded blocks per layer type — keep palette ≤ 5 muted academic colors",
    "color_legend": [
      { "type": "Embedding / PatchEmbed", "fill": "#E0E7FF", "border": "#6366F1" },
      { "type": "Self-Attention", "fill": "#FEE2E2", "border": "#DC2626" },
      { "type": "Cross-Attention", "fill": "#FEF3C7", "border": "#D97706" },
      { "type": "Feed Forward / MLP", "fill": "#D1FAE5", "border": "#059669" },
      { "type": "Norm / Residual", "fill": "#F3F4F6", "border": "#6B7280" }
    ]
  },
  "layers": {
    "count": "{argument name=\"layer_count\" default=\"8\"}",
    "items": [
      { "id": "L1", "type": "Embedding / PatchEmbed", "name": "Patch Embed", "shape": "196×768" },
      { "id": "L2", "type": "Norm / Residual", "name": "LayerNorm", "shape": "196×768" },
      { "id": "L3", "type": "Self-Attention", "name": "Multi-head Self-Attn (×8)", "shape": "196×768", "annotation": "× N=6 (encoder)" },
      { "id": "L4", "type": "Feed Forward / MLP", "name": "FFN", "shape": "196×768" },
      { "id": "L5", "type": "Cross-Attention", "name": "Cross-Attn", "shape": "K×768" },
      { "id": "L6", "type": "Self-Attention", "name": "Decoder Self-Attn", "shape": "K×768", "annotation": "× N=6 (decoder)" },
      { "id": "L7", "type": "Feed Forward / MLP", "name": "FFN", "shape": "K×768" },
      { "id": "L8", "type": "Norm / Residual", "name": "Output Head (Linear)", "shape": "K×C" }
    ]
  },
  "block_style": {
    "shape": "rounded rectangle (corner radius 4-6px)",
    "size_rule": "blocks of same layer type share identical width and height; visually grouped",
    "border": "1.2px solid (use the type's border color)",
    "fill": "use the type's fill color (very light tint)",
    "label_text": "layer name on first line (sans-serif bold 10-11pt) + tensor shape on second line (monospace italic 9pt)",
    "annotation_text": "if 'annotation' present (e.g. '× N=6'), draw it as a curly brace with label on the right side of the repeated block"
  },
  "connections": {
    "main_flow": {
      "style": "thin black solid arrows (1.2px), horizontal left → right",
      "arrowhead": "small filled triangle"
    },
    "residual": {
      "enabled": "{argument name=\"residual_enabled\" default=\"true\"}",
      "style": "curved dashed arrow arcing above the main flow, label '+' near join",
      "rule": "draw residual from input of attention block to its output"
    },
    "cross_attention": {
      "enabled": "{argument name=\"cross_attention_enabled\" default=\"true\"}",
      "style": "horizontal arrow from encoder side feeding into decoder cross-attn, label 'K, V'",
      "rule": "encoder output is shown as K, V input to decoder cross-attn"
    }
  },
  "extras": {
    "show_param_count": {
      "enabled": "{argument name=\"show_params\" default=\"false\"}",
      "rule": "if true, add parameter count below each major group (e.g. '85M params')"
    },
    "highlight_novelty": {
      "enabled": "{argument name=\"highlight_novelty\" default=\"true\"}",
      "rule": "if true, surround the user's contributed module with a thicker dashed orange border + label 'Ours' / 'Novel'"
    }
  },
  "constraints": {
    "must_keep": [
      "tensor shapes are accurate and labeled in monospace font",
      "color encodes layer type consistently across the figure",
      "all layers of the same type have identical block size",
      "white background, no gradient, no decoration",
      "all labels in English by default (or all Chinese if explicitly requested), no mixing",
      "must remain readable when printed in grayscale (rely on shape and label, not color alone)",
      "novel contribution (if any) is clearly marked"
    ],
    "avoid": [
      "3D extruded blocks, drop shadows, glossy fills",
      "rainbow palette (>5 colors)",
      "cartoon icons, emoji",
      "freeform 'art-style' blobs instead of crisp rectangles",
      "tensor shapes typeset in proportional font",
      "arrows crossing through blocks",
      "missing tensor shape labels (the figure is then useless for paper review)",
      "unlabeled cross-attention (must say K, V)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `layer_count`, each layer's `type` and `shape`
- **Can default**: `aspect_ratio` (16:9), `background` (white), `color_legend` (default 5-category palette), `block_style`
- **Can randomize**: precise font size / padding per block row, annotation placement

### Auto-Fill Strategy

- User says "I use Transformer" but gives no details → ask for key parameters (layers, heads, hidden dimension, sequence length); do not fabricate model scale
- User says "U-Net" → auto-use contracting + expansive dual-arm layout variant (see Variant 1)
- User doesn't mention residual → default `residual_enabled: true` (vast majority of modern networks have it)
- User doesn't mention novelty → default `highlight_novelty: true` (paper figures generally mark their contribution)
- User doesn't mention parameter count → default `show_params: false` (unless user mentions model scale comparison)

## Variant 1: U-Net / FPN Dual-Arm Architecture

```json
{
  "type": "U-Net / FPN dual-arm architecture diagram",
  "modify": {
    "layout": "U-shape: left arm downsampling (contracting path) + central bottleneck + right arm upsampling (expansive path), with horizontal skip connections between each level",
    "annotation": "Skip connections shown with horizontal dashed arrows, feature maps shown with progressively narrowing / widening rectangles to indicate spatial dimension changes"
  }
}
```

Suitable for: U-Net, FPN, HRNet, all encoder-decoder segmentation networks.

## Variant 2: GAN / Diffusion Dual-Network Adversarial / Multi-Step Inference

```json
{
  "type": "GAN / Diffusion architecture diagram",
  "modify": {
    "layout_gan": "Generator on top (noise → image) + Discriminator below (image → real/fake), sharing the generated image as D's input in the middle",
    "layout_diffusion": "Horizontal timestep sequence t=T → t=0, each timestep is the same U-Net instance, labeled with 't' embedding conditioning"
  }
}
```

Suitable for: GAN family, diffusion models, score-based models.

## Variant 3: Multi-Task / Multi-Head Output

```json
{
  "type": "Multi-task / multi-head output architecture diagram",
  "modify": {
    "layout": "Shared backbone in center → branches right into 2-4 task heads (e.g. classification head / regression head / segmentation head)",
    "annotation": "Each head labeled with its corresponding loss function and weight λ"
  }
}
```

Suitable for: multi-task learning, detection + segmentation, auxiliary supervision.

## Things to Avoid

- Missing or randomly written tensor shapes → core information of paper figure is gone
- Using gradients / 3D cube stacking → looks like PPT not a paper
- Colors ≥ 6 → loses layer type semantics
- Missing residual / cross-attention annotations (if the architecture has them) → misleads readers
- Using Comic Sans / handwritten fonts
- Skip connection arrows crossing through layer blocks
- Inconsistent block sizes for the same layer type
- Mixing Chinese and English labels
- Drawing "training loss" into the architecture diagram (should be a separate training figure or explained in caption)
- Cramming specific hyperparameter tables into the architecture figure (should go in a table, not the figure)