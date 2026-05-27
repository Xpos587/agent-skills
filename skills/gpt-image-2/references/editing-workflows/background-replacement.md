# Background Replacement Workflow Template

This file is for the editing task of "replacing an image's background with a new background", corresponding to the `scripts/edit.js` script.

Suitable scenarios:

- Product image background replacement (white background → lifestyle scene / studio / outdoor)
- Portrait background replacement (cluttered → clean studio)
- Old photo background renovation
- Cross-category asset background style unification

## Scope

- Single-subject background replacement
- Subject unchanged / only background changes
- Subject edges clear / identifiable

## When to Use

- User provides original image (REFERENCE_0) + a sentence like "change to XX background"
- User wants the subject to stay put and only change the background
- User wants multiple images with unified backgrounds

Do NOT use for:

- The subject itself needs modification (use `local-object-replacement.md`)
- Only removing something (use `object-removal.md`)
- The product itself needs retouching (use `product-retouching.md`)

## Missing Information Priority Question Order

1. Original image description / what is the subject
2. New background: scene / color tone / lighting
3. Whether to preserve the original image's lighting direction
4. Whether to regenerate shadows / reflections
5. Output aspect ratio (keep original / adjust)

## Main Template: Product Image Background Replacement

📖 Description

Input a subject image, output with the subject preserved and the background replaced with the specified scene.

📝 Prompt

```text
Based on REFERENCE_0, preserve the shape, proportions, labels, and materials of {argument name="subject" default="the white pump bottle in the center of the frame"}, and only replace the background with {argument name="new background" default="wooden vanity table in early morning sunlight, soft light streaming in from the left window, distant view slightly blurred, background elements include a glass of water, a few white petals, a folded beige towel"}.
Regenerate shadows and reflections consistent with the new background, making the subject look naturally present in the new scene.
Do not modify the subject's own color, text, shape, or materials.
Render style: {argument name="render style" default="high-resolution commercial photography, realistic grain, shallow depth of field, subject sharp, background naturally blurred"}.
Output aspect ratio: {argument name="aspect ratio" default="keep original aspect ratio"}.
```

### Parameter Strategy

- Must ask: original image subject, new background description
- Can default: render style, aspect ratio
- Can randomize: small background detail props

### Auto-Complete Strategy

- Industry auto-selects background: cosmetics → vanity table; food → dining table; electronics → minimalist office desk
- Default keep original aspect ratio
- Default regenerate shadows

## Variant 1: Portrait Background Replacement with Studio Backdrop

📝 Prompt

```text
Based on REFERENCE_0, preserve the pose, expression, clothing, and facial features of {argument name="subject" default="the person in the frame"}, and only replace the background with {argument name="studio backdrop" default="neutral gray backdrop paper"}.
Regenerate soft light shadows consistent with the new background; do not change the person's appearance, skin tone, or clothing color.
Render style: {argument name="render style" default="studio portrait photography, soft light, natural skin texture"}.
```

## Variant 2: Product Image Outdoor Scene Replacement

📝 Prompt

```text
Based on REFERENCE_0, preserve {argument name="subject" default="the product in the center of the frame"}, and replace the background with {argument name="outdoor scene" default="wooden boardwalk by the sea, warm dusk light, distant waves blurred"}.
Preserve all product labels and material details; regenerate shadows for the product consistent with the outdoor lighting direction.
Do not let product colors shift too much from the lighting (preserve brand colors).
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```text
Based on REFERENCE_0, preserve the subject; auto-select the most suitable one of "clean studio / natural scene / minimalist interior" three background options and replace it.
Keep the original aspect ratio; regenerate natural shadows for the subject.
```

## Things to Avoid

- Do not modify the subject itself (unless user allows)
- Do not let lighting direction be inconsistent with the subject's original lighting
- Do not let background elements be too many and distracting
- Do not leave obvious masking artifacts on the subject's edges
- Do not modify text / labels on the subject