# Product Retouching Workflow Template

This file is for the editing task of "retouching a product based on the original image":

- Improving product image quality/texture
- Fixing blemishes / scratches
- Adjusting gloss / reflections
- Sharpening labels / text
- Regenerating shadows / reflections

Features:

- Subject (product) preserved
- Focus is "quality upgrade" not "replacement"
- Does not forcibly change the background
- Does not modify product form or text

## Scope

- Product image quality upgrade
- Blemish repair
- Lighting redo
- Label / text sharpening

## When to Use

- User provides original image (REFERENCE_0) + wants the product to look more premium
- User wants to preserve the scene and only upgrade quality

Do NOT use for:

- Replacing the entire background (use `background-replacement.md`)
- Replacing the product with a different product (use `local-object-replacement.md`)
- Regenerating a white-background main image from scratch (use `product-visuals/white-background-product.md` to redraw)

## Missing Information Priority Question Order

1. Original product description
2. Which aspect to enhance (texture / gloss / label / shadows)
3. Whether to remove blemishes
4. Whether to preserve the background
5. Whether to output a before/after comparison

## Main Template: Product Quality Upgrade

📖 Description

Preserve the original image's product and scene, only upgrade the product's quality (more translucent / more glossy / labels sharper / more premium).

📝 Prompt

```text
Based on REFERENCE_0, preserve the shape, proportions, label content, and scene background of {argument name="product" default="the white pump bottle"} in the frame, and perform a quality upgrade on the product itself:
- Enhance the texture of {argument name="enhancement focus" default="bottle gloss and subtle reflections"};
- Fix {argument name="defect to fix" default="light scratches and spots on the bottle"};
- Make {argument name="label sharpening" default="the text and logo on the front label"} sharper and clearer;
- Keep shadows and reflections consistent with the original image's direction, but more refined;
- Do not modify the product color, text, or material type;
- Do not replace the background.
Render style: {argument name="render style" default="premium commercial product photography + magazine-level post-processing"}.
```

### Parameter Strategy

- Must ask: which aspect to enhance
- Can default: preserve background, preserve text, preserve colors
- Can randomize: shadow softness

### Auto-Complete Strategy

- Default: enhance gloss + fix blemishes + sharpen labels
- When intensity is not specified, treat as "restrained upgrade"
- Do not touch brand colors

## Variant 1: Label / Text Sharpening

📝 Prompt

```text
Based on REFERENCE_0, only sharpen and clarify the text on the product label in the frame:
- Preserve all text content, letter spacing, and font;
- Do not modify other parts of the bottle;
- Do not modify the background.
```

## Variant 2: Shadow / Reflection Regeneration

📝 Prompt

```text
Based on REFERENCE_0, preserve the product itself, and regenerate more refined {argument name="shadow type" default="soft bottom shadow + subtle reflection"}:
- Shadow direction consistent with the original image's lighting;
- Reflection intensity restrained, not distracting;
- Do not modify the product itself;
- Do not modify the background.
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```text
Based on REFERENCE_0, perform an overall quality upgrade on the product, auto-determining upgrade priorities (gloss / label / shadow / edges);
Preserve the product's original identity, overall elevation by one tier.
```

## Things to Avoid

- Do not modify the product's text (especially brand names)
- Do not let gloss upgrades turn into a "plastic" look
- Do not regenerate the background (unless the user allows)
- Do not let shadow direction drift
- Do not make exaggerated color adjustments to the product