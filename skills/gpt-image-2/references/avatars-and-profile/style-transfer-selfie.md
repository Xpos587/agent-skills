# Stylized Selfie / Persona Transformation Template

This file is used for "based on a reference image (user selfie / public photo), transforming the person into a specific style" persona visuals:

- Cosplay selfie style
- Gothic / vintage film / street / graffiti style persona
- Idol photo / Polaroid style
- Outdoor activity scene photos (conventions, basketball court, cafe)
- Celebrity / character style transfer

Features:

- Must be based on a reference image (REFERENCE_0) preserving facial identity
- Only modify style / makeup / clothing / scene atmosphere
- Single image output (not a grid / not a sheet)
- Output feels like "another version of you"

## Scope

- Transform selfie into a character / style
- One-click cosplay any character
- Change makeup + clothing + scene atmosphere simultaneously

## When to Use

- User provides a selfie, wants to transform the style
- User describes themselves + desired style, wants us to generate
- User wants "my look but in X style"

Do NOT use for:

- Multi-version grid (use `character-grid-portrait.md`)
- Standard professional headshot (use `portraits-and-characters/professional-portrait.md`)
- Founder feature portrait (use `portraits-and-characters/founder-portrait.md`)
- VTuber / 2D character (use `portraits-and-characters/virtual-host.md`)

## Missing Information Priority Question Order

1. Is a reference image provided (REFERENCE_0)? If not, text description of the person is needed
2. Desired style theme (cosplay / gothic / film / street / idol / celebrity style)
3. Clothing / makeup / hairstyle change range
4. Scene background (keep original / new scene)
5. Aspect ratio

## Main Template: Style Transfer Selfie (Based on REFERENCE_0)

📖 Description

Preserve the reference image person's identity and basic pose, switching the overall style to the specified theme.

📝 Prompt

```text
Based on the person in REFERENCE_0, preserve their face shape, facial proportions, skin tone, and basic pose, and transform the overall style to {argument name="target style" default="trad goth style"}:
- Hair: {argument name="hair description" default="black short hair + heavy blunt bangs"}
- Makeup: {argument name="makeup description" default="dark smoky eye makeup + black matte lips"}
- Clothing: {argument name="outfit description" default="black leather top + silver cross necklace + layered accessories"}
- Accessories: {argument name="accessories" default="nose ring, 2 earrings, silver rings"}
- Scene: {argument name="scene description" default="keep original image background"}
- Lighting: {argument name="lighting" default="dramatic side light, high contrast"}

Output style: {argument name="rendering" default="high-resolution realistic photography"}, single portrait image.

Constraints:
- Do not modify the person's identity (face shape, facial proportions must be recognizable)
- Do not modify gender, age range, or ethnicity
- Makeup heavy but not fake, skin texture preserved
- Clothing style unified, no clashing mix
```

### Parameter Strategy

- Must ask: reference image, target style
- Can default: hairstyle, makeup, clothing, accessories
- Can randomize: background details, specific accessory designs

### Auto-Complete Strategy

- When user only provides a style keyword: auto-expand hairstyle + makeup + clothing + accessories four-piece set
- Without a reference image, request the user to provide one, or fall back to text description mode
- Default: keep original image background, unless the style strongly requires a scene change

## Variant 1: Cosplay Selfie (Convention / Role-Play)

📝 Prompt

```text
Based on the person in REFERENCE_0 (if no reference image, describe as {argument name="subject self description" default="East Asian young woman, natural smile"}), transform them into {argument name="character" default="Genshin Impact Raiden Shogun"} cosplay selfie,
Shooting scene: {argument name="event location" default=\"Shanghai anime convention\"};
Preserve the person's own facial features, making it clear "it's them cosplaying this character";
Render as smartphone selfie style + event atmosphere + natural light.
```

## Variant 2: Vintage Film / Vintage 35mm Flash Portrait

📝 Prompt

```text
Based on the person in REFERENCE_0, re-shoot them as a vintage 35mm flash film portrait:
- Hard shadows from direct flash
- Grainy film texture
- Colors leaning 1990s warm yellow
- Scene: {argument name="vintage scene" default="street pool hall"}
- Natural expression, not posed
Preserve the original image person's identity.
```

## Variant 3: Idol Photo / Polaroid Collection (Single Polaroid Format)

📝 Prompt

```text
Based on the person in REFERENCE_0, generate a Polaroid photo:
- Polaroid frame (white thick border, bottom white space for handwritten caption)
- Person centered in the frame
- Style: {argument name="polaroid mood" default="Japanese idol pure"}
- Handwritten line at the bottom: '{argument name="caption" default="2026.4.24 weekend"}'
- Overall grain + slight overexposure
```

## Variant 4: Auto-Complete Mode

📝 Prompt

```text
Based on the person in REFERENCE_0, transform them into the most suitable "high-end stylized persona" auto-decided:
- Auto-determine the style theme best suited for this person's presence
- Auto-expand hairstyle / makeup / clothing / scene / lighting
- Do not modify the person's identity features
- Output single image
```

## Things to Avoid

- Do not modify facial proportions (most common failure: face-swapping)
- Do not modify gender / ethnicity features
- Do not make makeup so heavy it becomes "fake filter skin"
- Do not swap the background to something disconnected from the theme
- Do not pretend to be based on a reference image when none is provided (fall back to text description mode)
- Do not use real copyrighted character names directly for cosplay (describe features rather than naming)