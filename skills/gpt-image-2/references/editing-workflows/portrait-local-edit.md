# Portrait Local Edit Workflow Template

This file is for the editing task of "making localized modifications to a portrait image":

- Modifying hairstyle / hair color
- Modifying clothing color / style
- Modifying glasses / accessories
- Modifying makeup
- Modifying expression (mild)

Features:

- Must preserve the person's identity (face shape / facial proportions)
- Only localized modifications
- Paired with masks when necessary
- Does not modify the scene

## Scope

- Portrait local modifications
- Clothing / accessory modifications
- Makeup modifications
- Hairstyle / hair color modifications

## When to Use

- User provides a portrait image + wants to modify a specific area
- User wants to preserve the feeling of "it's the same person"

Do NOT use for:

- Replacing the entire background (use `background-replacement.md`)
- Replacing with a different object / item (use `local-object-replacement.md`)
- Removing something (use `object-removal.md`)

## Missing Information Priority Question Order

1. Which area to modify (hairstyle / clothing / makeup / accessories)
2. Description of the desired modification
3. Whether a mask is provided
4. Whether to preserve expression / pose
5. Whether to adjust lighting

## Main Template: Hairstyle / Hair Color Modification

📖 Description

Preserve the person's identity and composition, only modify hairstyle / hair color.

📝 Prompt

```text
Based on REFERENCE_0, preserve the person's face shape, facial proportions, skin tone, expression, pose, clothing, and background, and only modify the hairstyle / hair color to:
{argument name="new hair description" default="shoulder-length straight hair + natural black + slight wave"}.
The shadows, reflections, and hairline of the new hairstyle must be consistent with the original image's lighting direction;
Do not modify the person's identity features (eye shape, mouth shape, nose, ears);
Do not modify the background.
```

### Parameter Strategy

- Must ask: area to modify, new appearance
- Can default: preserve identity, preserve background, preserve lighting
- Can randomize: hair strand details

### Auto-Complete Strategy

- Default: preserve person's identity
- Default: preserve composition and lighting
- Default: only make localized modifications, do not touch other areas

## Variant 1: Clothing Modification

📝 Prompt

```text
Based on REFERENCE_0, preserve the person's face, hairstyle, pose, expression, and background, and only modify the clothing to:
{argument name="new outfit description" default="beige long-sleeve shirt + khaki blazer"};
The folds and shadows of the new clothing must be consistent with the original image's lighting direction;
Do not modify the person's identity features;
Do not modify the background.
```

## Variant 2: Makeup Modification

📝 Prompt

```text
Based on REFERENCE_0, preserve the person's identity and composition, and only modify the makeup to:
{argument name="new makeup description" default="matte nude lips + brown-toned eye shadow + natural blush"};
Preserve skin tone, skin texture details, and facial feature shapes;
Do not make the makeup look overly heavy or mismatched with the skin tone;
Do not modify the background.
```

## Variant 3: Accessory Modification / Addition

📝 Prompt

```text
Based on REFERENCE_0, preserve the person's identity and composition, and add / modify accessories to:
{argument name="accessory description" default="a pair of thin metal round-frame glasses"};
The angle and shadows of the accessories must be consistent with the original image's lighting direction;
Do not modify other body parts;
Do not modify the background.
```

## Variant 4: Auto-Complete Mode

📝 Prompt

```text
Based on REFERENCE_0, make a light style upgrade to the person (hairstyle / makeup / clothing — any one), auto-determining the most inconsistent area and fixing it;
Keep the person's identity unchanged;
Keep the background unchanged.
```

## Things to Avoid

- Do not modify facial features to the point of face-swapping
- Do not let the modified area's lighting direction be inconsistent with the original image
- Do not incidentally modify background and skin tone
- Do not make makeup so heavy it looks like "fake filter skin"
- Without a mask, inform the user that results may have slight variation
- Do not modify gender / ethnicity features unless the user explicitly requests