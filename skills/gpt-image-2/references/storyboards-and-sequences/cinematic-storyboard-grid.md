# Cinematic Narrative Storyboard Contact Sheet Template

This file is used to generate "a continuous narrative / emotional / event sequence as the main thread, outputting 9-15 cinematic stills in an N×M grid" cinematic storyboard sheets.

Typical uses:

- Short film / concept film / pitch trailer visual proposals
- AI video generation (Sora / Runway / Pika) shot list references
- Manga / animation / game cinematic cut scene proposals
- Film investment deck concept visuals
- "What would this story look like when filmed" one-image answer
- sci-fi / combat / disaster / romance / suspense any genre

Features (distinguishing from existing storyboard templates):

| Template | Nature |
|---|---|
| `four-panel-comic.md` (existing) | 4-panel manga / gag / reversal |
| `manga-spread-page.md` (existing) | Manga spread (irregular panels) |
| `recipe-process-flowchart.md` (existing) | Process diagram (recipe / tutorial) |
| `product-tvc-storyboard.md` (new) | **Commercial TVC storyboard (product-centered)** |
| **This template** (new) | **Film / short film / concept film narrative storyboard** (event / emotion / story-centered) |

**Core distinction**: This template's each panel is a "cinematic-level cinematic still", not emphasizing product / commercial, but emphasizing "what happened in this second + how the camera captures it + what the emotion is".

## Scope

- Film / short film / animation cinematic storyboard sheets
- AI video shot lists
- Pitch trailer visual proposals
- Concept film storyboards (sci-fi / combat / disaster / romance / suspense)

## When to Use

- User mentions "film storyboard / cinematic storyboard / short film shot list / concept film shot list"
- Subject is event / emotion / story, not product / commercial ad
- Want "cinematic feel" not "manga feel" / "ad feel"

Do NOT use for:

- Commercial TVC storyboards (with product) → use `product-tvc-storyboard.md`
- Manga storyboards (with dialogue bubbles / inner thoughts) → use `four-panel-comic.md` / `manga-spread-page.md`
- Recipe / tutorial process → use `recipe-process-flowchart.md`
- Real photography process boards / gear dressing → use `process-photo-board.md`

## Missing Information Priority Question Order

1. Story / main thread (a paragraph: who + where + what happens + ending)
2. Genre (**sci-fi / disaster / combat / romance / suspense / western / film noir**)
3. Shot count (9 / 12 / 15) + grid (3×3 / 3×4 / 3×5 / 4×4)
4. Emotional arc (**beginning → rising → climax → falling / constant tension / constant calm then burst**)
5. Style (**photoreal / oil painting texture / anime film feel / black-and-white film / retro 70s**)
6. Color tone base (determines the color grading for the entire shot set)
7. Aspect ratio (per panel 16:9 / 21:9 cinematic widescreen; full sheet 1:1 contact sheet or 4:5 / 16:9)

## Main Template: 3×4 = 12-Shot Cinematic Storyboard Contact Sheet (Sci-Fi Case)

📖 Description

12 independent cinematic stills, continuous narrative of an event (e.g., spacecraft descending into a gas giant), each panel is a complete cinematic concept image, overall maintaining consistent mood / lighting / color scheme.

📝 Prompt

```json
{
  "type": "cinematic storyboard contact sheet",
  "goal": "Generate a 12-shot storyboard sheet, each shot is a complete cinematic still, the entire set tells one continuous narrative",
  "subject": {
    "primary": "{argument name=\"primary subject\" default=\"a small futuristic spacecraft descending into a massive gas giant storm system\"}",
    "secondary": "{argument name=\"secondary subject\" default=\"an enormous leviathan-like silhouette hidden within the clouds\"}",
    "mood": "{argument name=\"mood\" default=\"oppressive, catastrophic, awe-struck, high tension, cosmic dread\"}",
    "style": "{argument name=\"cinematic style\" default=\"photorealistic cinematic concept art with dark sci-fi realism, volumetric storm clouds, strong contrast, amber and black palette with occasional cold blue lightning\"}",
    "aspect_ratio_per_panel": "{argument name=\"per-panel ratio\" default=\"16:9\"}"
  },
  "vehicle_or_actor": {
    "design": "{argument name=\"hero design\" default=\"compact armored deep-atmosphere ship with 3 bright rear engines, angular industrial hull, worn metallic panels\"}",
    "scale": "{argument name=\"scale relation\" default=\"tiny compared to the planet and creature\"}"
  },
  "layout": {
    "grid": {
      "rows": "{argument name=\"rows\" default=\"3\"}",
      "columns": "{argument name=\"columns\" default=\"4\"}",
      "count": "{argument name=\"panel count\" default=\"12\"}"
    },
    "sheet_aspect_ratio": "{argument name=\"sheet ratio\" default=\"16:9 contact sheet\"}",
    "panel_borders": "thin white dividers, generous gutter",
    "sections": [
      { "position": "row 1 col 1", "description": "{argument name=\"shot 1\" default=\"wide exterior shot of the ship entering the upper atmosphere of a colossal gas giant at extreme speed, glowing clouds streaked with fire and friction around the vessel, curved planetary horizon visible\"}" },
      { "position": "row 1 col 2", "description": "{argument name=\"shot 2\" default=\"cockpit POV, dark interior filled with red and cyan holographic instruments, forward visibility collapsing into turbulent storm layers and electrical haze\"}" },
      { "position": "row 1 col 3", "description": "{argument name=\"shot 3\" default=\"exterior mid-wide shot of the ship diving into a gigantic rotating cloud funnel, surrounded by violent spiraling storm structure\"}" },
      { "position": "row 1 col 4", "description": "{argument name=\"shot 4\" default=\"extreme close exterior of the ship hull as bright lightning strikes dangerously close, white electric energy crawling across the metal surface\"}" },
      { "position": "row 2 col 1", "description": "{argument name=\"shot 5\" default=\"dashboard warning screen in red, showing a critical systems failure interface with 4 warning lines and 1 large percentage readout: WARNING / ENGINES COMPROMISED / THRUST FLUCTUATION / GRAVITY SPIKE DETECTED / DESCENT RATE -453%\"}" },
      { "position": "row 2 col 2", "description": "{argument name=\"shot 6\" default=\"rear three-quarter exterior of the ship fighting turbulence inside dense storm clouds, engines burning hard while the craft barely holds course\"}" },
      { "position": "row 2 col 3", "description": "{argument name=\"shot 7\" default=\"massive circular disturbance forming in the clouds like an eye or maw, entire storm systems displaced by something huge moving beneath\"}" },
      { "position": "row 2 col 4", "description": "{argument name=\"shot 8\" default=\"second cockpit view with radar-like navigation display and red alert text, pilot making a blind evasive maneuver through lightning-filled darkness\"}" },
      { "position": "row 3 col 1", "description": "{argument name=\"shot 9\" default=\"first reveal of the colossal creature shape rising near the ship, black organic surface and immense curved anatomy emerging from darkness, ship tiny at lower left\"}" },
      { "position": "row 3 col 2", "description": "{argument name=\"shot 10\" default=\"spiral descent shot, ship caught inside a vortex tunnel of clouds, spinning downward with engines flaring as it struggles to recover\"}" },
      { "position": "row 3 col 3", "description": "{argument name=\"shot 11\" default=\"sudden breakthrough into a calm void, minimal composition, ship flying in eerie silence through dark open space with soft mist and no visible storm around it\"}" },
      { "position": "row 3 col 4", "description": "{argument name=\"shot 12\" default=\"final reveal, gigantic leviathan fully emerging behind or beside the ship in cleared space, backlit by a pale circular storm opening, enormous open maw-like silhouette dwarfing the craft\"}" }
    ],
    "continuity": "all 12 panels depict one continuous narrative sequence with consistent hero design, color grading, and mood arc"
  },
  "lighting": {
    "primary": "{argument name=\"primary light\" default=\"glowing amber storm light\"}",
    "secondary": "{argument name=\"secondary light\" default=\"red cockpit interface glow\"}",
    "accents": "{argument name=\"accent light\" default=\"blue-white lightning and engine exhaust\"}"
  },
  "environment": {
    "location": "{argument name=\"location\" default=\"inside the upper and middle storm layers of a gigantic gas giant\"}",
    "weather": "{argument name=\"weather\" default=\"violent turbulence, electrical storms, vortex funnels, cloud walls, pressure chaos\"}",
    "threat": "{argument name=\"threat / tension\" default=\"no safe zone, repeated near-failure, unknown colossal presence driving the storm\"}"
  },
  "constraints": {
    "must_keep": [
      "12 panels must present one continuous narrative (not 12 random images)",
      "hero (ship / character) appearance consistent across all panels",
      "overall color grading / mood unified",
      "shot rhythm mixed (wide / medium / close-up / POV / low angle / high angle)",
      "at least 1 reveal / climax shot (e.g. the last panel)"
    ],
    "avoid": [
      "12 panels all same shot type (e.g. all close-ups)",
      "hero appearance drift",
      "overall color grading inconsistent (one panel warm light, another cold light with no reason)",
      "shot descriptions disconnected from the main story thread",
      "drawing storyboards as manga / adding dialogue bubbles (this is cinematic stills, not manga)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: primary subject, mood, cinematic style, 12-shot brief descriptions
- **Can default**: lighting, environment, aspect ratio
- **Can randomize**: specific angle per shot (auto-generate wide/POV/CU mix based on main thread)

### Auto-Complete Strategy

- User provides a one-sentence story outline → auto-split into 12 shots (following "entry → mid → escalation → climax → reveal" structure)
- No mood specified → auto-select by genre (sci-fi=oppressive; romance=warm; combat=tense; suspense=cold)
- No shot type specified per panel → auto-mix 4 wide / 4 medium / 2 CU / 2 POV

## Variant 1: 3×3 = 9-Shot Short Film Rhythm (Suitable for 1-2 Minute Short Films)

📝 Prompt

```json
{
  "type": "9-shot short film storyboard",
  "layout": { "rows": 3, "columns": 3, "count": 9 },
  "narrative_arc": ["1 establish", "2-3 inciting", "4-5 escalation", "6 turn", "7-8 climax", "9 resolve / cliffhanger"],
  "use_case": "1-2 minute short film / concept film / TikTok long video"
}
```

### When to Choose This Variant

- Shorter story / tighter pacing
- Don't need 12 shots
- Suitable for short film / short video proposals

## Variant 2: 4×4 = 16-Shot Large-Scale Scenes (Suitable for Combat / Disaster / Long Sequences)

📝 Prompt

```json
{
  "type": "16-shot epic sequence storyboard",
  "layout": { "rows": 4, "columns": 4, "count": 16 },
  "narrative_arc_extended": [
    "1-2 setup",
    "3-5 build",
    "6-8 first wave",
    "9 mid-climax",
    "10-12 second wave",
    "13-14 final climax",
    "15-16 aftermath"
  ],
  "use_case": "large-scale combat / disaster film / epic sequence"
}
```

### When to Choose This Variant

- Need more shots for complex narrative
- Epic / combat / disaster genre
- Accept reduced detail per panel

## Variant 3: Black-and-White Film / Retro Film Grain Texture

📝 Prompt

```json
{
  "type": "black-and-white noir storyboard contact sheet",
  "style_override": {
    "rendering": "high-contrast black and white film still, deep shadows, grain texture, 1940s noir cinematography",
    "lighting": "venetian blind shadows, hard side light, smoke",
    "framing": "tight closeups, dutch angles, low POV"
  },
  "use_case": "suspense / film noir / retro crime genre"
}
```

### When to Choose This Variant

- Black-and-white / noir genre
- Want retro film grain texture
- Emphasize light/shadow / geometric composition

## Things to Avoid

- Story disconnect between 12 panels (must be continuous narrative)
- Hero appearance drift
- Color grading inconsistency (one panel warm, another cold)
- All same shot type (must mix wide / medium / close / POV / low/high angle)
- Drawing storyboards as manga / adding dialogue bubbles
- Inserting ad products into cinematic storyboards (use `product-tvc-storyboard.md`)
- Last panel not a reveal / climax / cliffhanger (cinematic storyboards need a clear ending shot)
- Letting the model freely generate 12 shots (must explicitly list each shot description to ensure narrative coherence)