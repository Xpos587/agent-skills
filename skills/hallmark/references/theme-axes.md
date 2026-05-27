# Theme axes — diversification reference

Loaded when comparing theme distances for the diversification rule. Use this instead of `tokens.css` — it's smaller and structured for comparison.

Three axes per theme. Two consecutive Hallmark outputs must differ on **at least one** axis.

## Axes

- **Paper band** — `dark` (L < 30 %) / `mid` (30–85 %) / `light` (> 85 %)
- **Display style** — `italic-serif` / `roman-serif` / `geometric-sans` / `mono` / `display-condensed-italic` / `display-heavy` / `system-native` / `risograph-bold`
- **Accent hue** — `warm` (10–60°) / `cool` (200–300°) / `neutral` (no chromatic accent) / `chromatic-other` (green / sage / phosphor / etc.)

## The 22 themes

| Theme | Paper band | Display style | Accent hue |
|---|---|---|---|
| Specimen | light | italic-serif | warm |
| Atelier | light | italic-serif | warm |
| Brutal | light | display-heavy | warm |
| Salon | light | roman-serif | warm |
| Newsprint | light | roman-serif | warm |
| Linen | light | roman-serif | cool |
| Studio | light | italic-serif | chromatic-other (green) |
| Manifesto | dark | display-heavy | warm |
| Terminal | dark | mono | chromatic-other (phosphor) |
| Midnight | dark | geometric-sans | cool |
| Almanac | light | system-native | cool |
| Garden | light | italic-serif | chromatic-other (sage) |
| Quiet | light | system-native | neutral |
| Riso | light | risograph-bold | cool |
| Sport | light | display-condensed-italic | warm |
| Bloom | light | geometric-sans | warm |
| Coral | light | geometric-sans | warm |
| Violet | light | geometric-sans | cool |
| Aurora | dark | geometric-sans | cool |
| Halo | dark | geometric-sans | chromatic-other (amber) |
| Plume | light | geometric-sans | warm |
| Editorial | light | roman-serif | warm |

## Genre clusters

The catalog rotation is scoped to genre:

- **Atmospheric** → Bloom / Midnight / Terminal
- **Modern-minimal** → Quiet
- **Playful** → Plume
- **Editorial** → Specimen / Atelier / Brutal / Salon / Newsprint / Linen / Studio / Manifesto / Almanac / Garden / Riso / Sport / Coral / Violet / Aurora / Halo / Editorial

## Diversification check

When comparing two themes, count matching axes. If ≥2 of 3 match, the pair is **too close** — pick a more distant theme.

Examples:
- Specimen (light / italic-serif / warm) vs Studio (light / italic-serif / chromatic-other) → 2 matches (paper + display) → **acceptable** (differs on accent)
- Specimen vs Salon (light / roman-serif / warm) → 2 matches (paper + accent) → **too close** — pick a different theme