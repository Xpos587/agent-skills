# Object Removal Workflow Template

This file is for the editing task of "removing something from an image, keeping the rest of the frame":

- Removing passersby / onlookers
- Removing watermarks / logos (only in non-copyright contexts)
- Removing extra props
- Removing utility lines / cables
- Removing blemishes from the image

Features:

- No new object needed to replace
- Removed area needs natural fill
- Optionally paired with a mask
- Must not affect the main subject

## Scope

- Single object removal
- Multiple object removal
- Large area removal (utility lines / cables)
- Local blemish removal

## When to Use

- User provides original image (REFERENCE_0) + wants to remove something
- User wants a cleaner image

Do NOT use for:

- Replacing with a new object (use `local-object-replacement.md`)
- Replacing the entire background (use `background-replacement.md`)

## Missing Information Priority Question Order

1. The object to remove
2. Whether a mask is provided
3. What the removed area should be filled with (background continuation / clean solid color)
4. Whether shadows / reflections are affected

## Main Template: Single Object Removal

📖 Description

Precisely remove one object, filling the original area with surrounding environment naturally.

📝 Prompt

```text
Based on REFERENCE_0, remove {argument name="object to remove" default="the passerby in the background"} from the frame.
Fill the removed area using the surrounding environment ({argument name="fill description" default="street ground, wall, and distant buildings"}) to create a natural continuation, making it look as if it never existed;
Preserve the main subject, lighting direction, shadows, and image composition;
Do not modify other people, objects, or text.
```

### Parameter Strategy

- Must ask: object to remove, fill type
- Can default: preserve main subject
- Can randomize: fill-in details

### Auto-Complete Strategy

- Default: infer fill from surrounding environment
- Default: preserve all shadow directions

## Variant 1: Removal with Mask

📝 Prompt

```text
Based on REFERENCE_0, use REFERENCE_1 (mask) to mark the area to be removed, and naturally replace the content in that area with a continuation of the surrounding environment;
Only modify the masked area; preserve the area outside the mask pixel-perfectly;
Do not let the filled area show visible seams or texture jumps.
```

## Variant 2: Batch Removal (e.g., Utility Lines / Onlookers)

📝 Prompt

```text
Based on REFERENCE_0, remove all {argument name="objects to remove" default="utility lines in the sky / passersby on the street"} from the frame.
Fill the removed areas with the corresponding background (sky / ground / buildings) naturally;
Preserve the main subject, lighting, shadows, and composition.
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```text
Based on REFERENCE_0, automatically identify clutter that interferes with reading the main subject and remove it (e.g., passersby, utility lines, bottles, water stains);
Preserve the main subject and composition; fill the background naturally.
```

## Things to Avoid

- Do not remove the main subject along with the clutter
- Do not modify the lighting direction (shadows must also be preserved after removal)
- Do not let the filled area appear "blurry / repeating texture"
- Without a mask, inform the user that results may have slight variation
- Do not remove copyrighted logos / watermarks (unless the user is the legal owner)