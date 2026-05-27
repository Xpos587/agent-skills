# Pose / Action Reference Sheet N×N Template

This file is used to generate "the same character, in an N×N grid with different poses / actions / combat / dance poses" as a pure reference sheet / action dictionary.

Typical uses:

- Dance / hip-hop / combat pose choreography reference
- Character animator / manga artist pose lookup sheet
- Fitness / yoga / martial arts pose dictionary
- Fashion photo pose inspiration library
- Game character action reference sheet
- AI video / downstream generation pose control reference set

Features (distinguishing from existing portrait templates):

| Template | Focus |
|---|---|
| `character-sheet.md` (existing) | A character's "complete design" (turnaround + expressions + outfits + accessories) |
| `avatars-and-profile/character-grid-portrait.md` (existing) | n×n character grid (multi-profession / multi-era portraits) |
| **This template** (new) | **Same character N different poses / actions / dance poses pure action dictionary** |

**Core distinction**: This template does not change outfits, characters, or styles - only poses. The difference in each panel is entirely in body language.

## Scope

- 4×4 / 4×5 / 5×5 pose lookup sheet
- Dance / combat / fitness / fashion pose dictionary
- Animator / manga artist / coach reference
- AI pose control dataset source images

## When to Use

- User mentions "pose reference / pose sheet / action reference sheet / choreography / fitness / combat moves"
- Wants N different poses of the same character
- For use as teaching / reference / downstream generation input

Do NOT use for:

- Character complete design (turnaround + expressions + outfits) → use `character-sheet.md`
- Multi-profession / multi-era portraits → use `avatars-and-profile/character-grid-portrait.md`
- Manga storyboarding / narrative → use `storyboards-and-sequences/four-panel-comic.md`
- Real photography storyboards (with products / commercial ads) → use `storyboards-and-sequences/product-tvc-storyboard.md`

## Missing Information Priority Question Order

1. Pose count (default 16, common 9 / 12 / 16 / 20 / 25)
2. Character gender + body type + hairstyle + outfit (**must be fixed, shared across all panels**)
3. Render style (**photorealistic / grayscale 3D sculpture / anime lineart / minimalist flat**)
4. Pose theme (**hip-hop / combat / fashion / yoga / fitness / general movement**)
5. Whether each panel needs numbering / annotations / direction arrows
6. Background (default seamless white) + lighting (default soft studio)
7. Aspect ratio (default 1:1 contact sheet / 16:9 landscape)

## Main Template: 4×4 = 16-Panel Pose Reference Sheet (Photorealistic Style)

📖 Description

Clean studio contact sheet, no background, full body in frame, each panel's pose is independent but character / outfit / camera distance is strictly consistent.

📝 Prompt

```json
{
  "type": "pose reference sheet",
  "goal": "Generate a pure action reference sheet with N different poses of the same character, usable for choreography / animation / fitness / AI pose control reference",
  "subject": {
    "theme": "{argument name=\"pose theme\" default=\"hip-hop dance and combat-ready movement chart\"}",
    "character": {
      "count": 1,
      "gender_presentation": "{argument name=\"gender\" default=\"female\"}",
      "age_appearance": "{argument name=\"age\" default=\"young adult\"}",
      "body_type": "{argument name=\"body type\" default=\"fit athletic dancer\"}",
      "skin_tone": "{argument name=\"skin tone\" default=\"light tan\"}",
      "hair": {
        "color": "{argument name=\"hair color\" default=\"black\"}",
        "style": "{argument name=\"hair style\" default=\"high ponytail with loose strands\"}"
      },
      "outfit": {
        "count": 5,
        "items": [
          "{argument name=\"outfit top\" default=\"white sports bra or cropped athletic top\"}",
          "{argument name=\"outfit bottom\" default=\"baggy purple jogger pants\"}",
          "{argument name=\"outfit shoes\" default=\"white chunky sneakers\"}",
          "{argument name=\"outfit accessory 1\" default=\"purple wristbands or forearm bands on both arms\"}",
          "{argument name=\"outfit accessory 2\" default=\"small hoop earrings\"}"
        ]
      }
    }
  },
  "style": {
    "image_type": "{argument name=\"render style\" default=\"photorealistic studio pose sheet\"}",
    "lighting": "{argument name=\"lighting\" default=\"clean even studio lighting\"}",
    "background": "{argument name=\"background\" default=\"plain light gray to white seamless backdrop\"}",
    "camera": "{argument name=\"camera\" default=\"full-body framing, straight-on view, consistent distance\"}",
    "rendering": "{argument name=\"rendering\" default=\"sharp realistic anatomy, dynamic motion, slight shadow under feet\"}",
    "face": "{argument name=\"face treatment\" default=\"intentionally blurred or obscured\"}"
  },
  "layout": {
    "grid": {
      "rows": "{argument name=\"rows\" default=\"4\"}",
      "columns": "{argument name=\"columns\" default=\"4\"}",
      "count": "{argument name=\"panel count\" default=\"16\"}"
    },
    "numbering": {
      "count": "{argument name=\"panel count\" default=\"16\"}",
      "labels": ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"],
      "position": "top-left corner of each cell"
    },
    "cell_borders": "thin black divider lines between all panels",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"1:1\"}"
  },
  "poses": {
    "count": 16,
    "items": [
      { "label": "1", "description": "{argument name=\"pose 1\" default=\"wide low squat, knees bent outward, torso angled slightly left, both arms extended loosely in a defensive dance stance\"}" },
      { "label": "2", "description": "{argument name=\"pose 2\" default=\"deep side lunge to the left, left arm pointing straight left, right hand near the head, energetic directional pose\"}" },
      { "label": "3", "description": "{argument name=\"pose 3\" default=\"low crouch with one hand touching the floor, one knee bent under the body, opposite arm extended horizontally\"}" },
      { "label": "4", "description": "{argument name=\"pose 4\" default=\"upright one-leg balance, left knee lifted high, both arms spread outward for rhythm and balance\"}" },
      { "label": "5", "description": "{argument name=\"pose 5\" default=\"similar one-leg raised pose with the other leg supporting, arms stretched outward in a lighter dance variation\"}" },
      { "label": "6", "description": "{argument name=\"pose 6\" default=\"very wide grounded squat, torso pitched forward, one hand reaching toward the floor between the legs, other arm extended back\"}" },
      { "label": "7", "description": "{argument name=\"pose 7\" default=\"dramatic standing back arch, chest lifted upward, hips forward, both arms opened behind and to the sides\"}" },
      { "label": "8", "description": "{argument name=\"pose 8\" default=\"small jump or suspended squat, both feet off the floor, knees bent, arms spread wide symmetrically\"}" },
      { "label": "9", "description": "{argument name=\"pose 9\" default=\"floor-supported seated lean, one hand planted behind, one arm reaching diagonally upward, legs bent to one side\"}" },
      { "label": "10", "description": "{argument name=\"pose 10\" default=\"front-facing balance with one knee raised to hip height, one arm bent in guard position and the other extended sideways\"}" },
      { "label": "11", "description": "{argument name=\"pose 11\" default=\"deep lateral stance, feet far apart, knees bent, both hands raised open near shoulder level like a ready combat pose\"}" },
      { "label": "12", "description": "{argument name=\"pose 12\" default=\"low side lunge split, one hand planted on the floor, the other arm reaching vertically overhead, torso arched upward\"}" },
      { "label": "13", "description": "{argument name=\"pose 13\" default=\"standing backward lean with relaxed bent knees, chest up, arms hanging loosely behind in a groove pose\"}" },
      { "label": "14", "description": "{argument name=\"pose 14\" default=\"compact twisting crouch, weight low over bent legs, torso rotated, one arm pulled in and the other extended outward\"}" },
      { "label": "15", "description": "{argument name=\"pose 15\" default=\"very wide side lunge stretch, one hand to the floor near the front foot, opposite arm reaching diagonally overhead\"}" },
      { "label": "16", "description": "{argument name=\"pose 16\" default=\"one-leg lifted pose with knee high, one hand behind the head and the other arm extended forward, confident finishing stance\"}" }
    ]
  },
  "composition": "show the same person in all 16 panels with consistent outfit and scale, centered within each frame, designed like a movement library or choreography reference chart",
  "constraints": {
    "must_keep": [
      "Character across 16 panels is completely identical (face / body type / hairstyle / outfit / shoes)",
      "Full body in frame for each panel, camera distance consistent",
      "Each panel's pose must be recognizable and distinctly different",
      "Top-left numbering 1-16 clearly visible in each panel",
      "Body proportions correct (no limb distortion)"
    ],
    "avoid": [
      "All 16 poses are standing → must mix squat / lunge / floor / jump / arabesque",
      "Outfit / accessories changing across panels",
      "Full body cropped (head or feet cut off)",
      "Limb distortion / extra hands / extra feet",
      "Facial expressions drawing too much attention (focus should be on poses not expressions)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: pose count, character description (gender + body type + hairstyle + outfit), render style
- **Can default**: pose 1-16 specific descriptions (auto-generate diverse poses based on theme)
- **Can randomize**: face treatment, shadow direction

### Auto-Complete Strategy

- User only says "dance poses 16 panels" → use template default 16-pose combination (already mixed squat / lunge / floor / balance / jump / backbend)
- User provides theme (hip-hop / combat / fashion) → auto-adjust pose description style
- User provides reference character → fill all character fields with reference image details

## Variant 1: 4×4 Grayscale 3D Sculpture Style (with Direction Arrows)

Suitable for Korean dance choreography / combat move instruction, derived from Case 130 style.

📝 Prompt

```text
[STYLE]
monochromatic grayscale illustration, 3D rendered character, clean instructional reference sheet,
white background, comic-style cell grid layout, technical diagram aesthetic

[LAYOUT]
4x4 grid layout, 16 panels total, each panel separated by thin black border lines,
numbered cells from 1 to 16, consistent panel size

[CHARACTER]
{argument name="character" default="young female dancer, athletic build, ponytail hairstyle, crop top and baggy pants, sneakers"}, same character in all panels

[PANEL STRUCTURE - per cell]
top-left: bold number badge + {argument name="title" default="Korean title text"}
center: full-body character pose illustration
bottom-left: {argument name="description" default="Korean description text (3-4 lines)"}
overlay: directional arrows indicating movement direction

[ARROWS / MOTION INDICATORS]
curved arrows, straight arrows, circular rotation indicators,
placed around the character to show movement flow and direction

[RENDERING STYLE]
high detail 3D sculpt style, soft studio lighting, subtle shadows,
no color, grayscale shading, clean linework, game concept art quality

[NEGATIVE]
no background scenery, no color tones, no extra characters,
no cluttered backgrounds
```

### When to Choose This Variant

- Want an "instructional manual feel"
- Need explicit direction arrows
- Grayscale 3D sculpture feel (not photorealistic)

## Variant 2: 5×5 = 25-Panel Large Action Dictionary

📝 Prompt

```json
{
  "type": "expanded pose reference sheet 25-panel",
  "layout": { "rows": 5, "columns": 5, "count": 25 },
  "must_keep": ["detail per panel will be smaller, but poses still recognizable", "suitable for contact sheet / 16:10 landscape"],
  "use_case": "animator / choreographer / pose AI dataset"
}
```

### When to Choose This Variant

- Need more pose samples
- Accept reduced detail per panel
- Suitable as dataset / library

## Variant 3: 3×3 = 9-Panel Refined Hero Pose Collection (Higher Detail Per Panel)

📝 Prompt

```json
{
  "type": "hero pose collection 9-panel",
  "layout": { "rows": 3, "columns": 3, "count": 9 },
  "rendering_quality_per_panel": "increase detail since fewer panels",
  "use_case": "fashion photo pose inspiration / model reference / poster hero pose library"
}
```

### When to Choose This Variant

- For fashion / model shoot pose inspiration
- Each panel needs higher finish quality
- Not pursuing pose quantity

## Things to Avoid

- Character outfit drift across 16 panels → critical error
- All 16 poses are standing or all squat → lack of movement diversity
- Missing or out-of-order numbering
- Full body cropped (head / feet)
- Extra hands / extra feet / joint distortion
- Adding abstract backgrounds to realistic poses (keep seamless solid color)
- Facial expressions drawing too much attention (use blurred face / neutral treatment)
- Directly using the template's default "hip-hop" pose combination for a "yoga" theme (replace pose 1-16 descriptions)
- Letting the model freely generate N poses (must explicitly list each panel's pose description)