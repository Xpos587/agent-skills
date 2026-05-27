# Local Object Replacement Workflow Template

This file is for the editing task of "replacing one object in an image with another object":

- Replacing a coffee cup in the image with a thermos
- Replacing a T-shirt on a person with a hoodie
- Replacing a car logo with another brand
- Replacing a pet cat with a dog
- Replacing an object in the background with something else

Features:

- Most of the subject preserved
- Only localized precise replacement
- Surrounding lighting / shadows need to adapt
- Optionally paired with a mask

## Scope

- Single object replacement
- Multiple object replacement
- Precise replacement with a mask

## When to Use

- User provides original image (REFERENCE_0) + wants to replace something
- User wants everything except the replaced object to stay unchanged

Do NOT use for:

- Replacing the entire background (use `background-replacement.md`)
- Only removing something (use `object-removal.md`)
- Product / portrait retouching (use `product-retouching.md` / `portrait-local-edit.md`)

## Missing Information Priority Question Order

1. The object in the original image to be replaced
2. What to replace it with
3. Whether a mask is provided
4. Whether shadows / reflections need to be regenerated after replacement
5. Whether to preserve the replaced object's size / position

## Main Template: Single Object Replacement

📖 Description

Precisely replace one object, keeping the rest of the image as much as possible.

📝 Prompt

```text
Based on REFERENCE_0, replace {argument name="original object" default="the white ceramic coffee cup on the table"} with {argument name="replacement object" default="same-sized stainless steel thermos, matte silver, with simple brand text 'AURORA' on the body"}.
Preserve the position, lighting, shadows, and composition of all other elements in the original image; only modify the replaced object itself.
Regenerate shadows, reflections, and materials for the new object consistent with the original image's lighting direction.
Do not change other people, table, or background.
```

### Parameter Strategy

- Must ask: original object, replacement object
- Can default: whether shadows need regeneration
- Can randomize: secondary details of the replacement object

### Auto-Complete Strategy

- Default preserve original object's size and position
- Default regenerate shadows
- When user doesn't specify material, choose by reasonable analogy

## Variant 1: Precise Replacement with Mask

📝 Prompt

```text
Based on REFERENCE_0, use REFERENCE_1 (mask) to mark the area to be replaced, and precisely replace {argument name="object to replace" default="the person's white T-shirt"} with {argument name="new object" default="dark blue long-sleeve hoodie with 'AURORA' text on the chest"}.
Only modify the masked area; the area outside the mask must be preserved pixel-perfectly;
Generate folds and shadows for the new clothing consistent with the original image's lighting;
Keep the person's body shape and pose completely unchanged.
```

## Variant 2: Batch Object Replacement

📝 Prompt

```text
Based on REFERENCE_0, replace all {argument name="original objects" default="wooden chairs"} in the frame with {argument name="replacement objects" default="beige plastic chairs"}.
Keep each chair's position, angle, and placement unchanged;
Generate shadows for the new chairs consistent with the original image's lighting direction;
Do not modify the tables, walls, light fixtures, or people.
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```text
Based on REFERENCE_0, replace {argument name="object" default="the main foreground object"} in the original image with a more modern visual style version of the same function, auto-deciding material and color scheme while keeping position and size consistent.
```

## Things to Avoid

- Do not change the original object's position / proportions after replacement (unless user allows)
- Do not let the replacement object's lighting direction be inconsistent with the original image
- Do not incidentally modify other unrelated elements
- Do not let the replacement object's material look "pasted on"
- Without a mask, do not pretend precision is perfect (note that edges may have slight variation)