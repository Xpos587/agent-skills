# Real Photography Process Board / Gear Dressing / Operation Process Board Template

This file is used to generate "real-person / character-level cinematic realistic multi-step operation process boards". Common scenarios:

- Gear dressing / armor assembly / uniform changing process
- Craft operation / makeup / experiment / workshop steps
- Training / martial arts / fitness movement breakdown
- Equipment maintenance / PC building / device startup process
- Character cosplay / prop wearing process
- Any "step 1 → step N, each step a real-shot cinematic image + number + description" visual manual

Features (distinguishing from existing/new templates):

| Template | Nature |
|---|---|
| `recipe-process-flowchart.md` (existing) | Recipe process (hand-drawn / illustration style) |
| `pose-reference-sheet.md` (new) | Pose dictionary (same character N isolated actions, no narrative order) |
| `cinematic-storyboard-grid.md` (new) | Film storyboard (continuous narrative, events/emotion) |
| `product-tvc-storyboard.md` (new) | Commercial TVC storyboard (product-centered) |
| **This template** (new) | **Real-person/character cinematic process board** (step-centered + order + equipment state changes) |

**Core distinction**: This template's each sub-image is a "real-person/cinematic real-shot still of the same character at different steps", emphasizing **equipment state / operation posture changes from step 1 to N**, accompanied by step numbers + step titles + step descriptions.

## Scope

- Gear dressing process (armor / tactical gear / cosplay)
- Craft operation process (coffee brewing / makeup / experiment)
- Training breakdown (martial arts / fitness / dance technique breakdown)
- Device startup / maintenance / PC building process
- Ceremony / dressing etiquette process

## When to Use

- User mentions "gear / dressing / process board / step board / operation breakdown / process board"
- Subject is **the same real character** or **the same object** undergoing **ordered state changes**
- Want **real-shot / cinematic realistic quality** (not hand-drawn/lineart)
- Each step needs image + step number + step description text

Do NOT use for:

- Recipe / tutorial lineart process → use `recipe-process-flowchart.md`
- Pose dictionary / action dictionary (no order) → use `pose-reference-sheet.md`
- Film narrative storyboard (narrative over steps) → use `cinematic-storyboard-grid.md`
- Commercial ad TVC (product-centered) → use `product-tvc-storyboard.md`

## Missing Information Priority Question Order

1. Process theme (what process? gear / makeup / operation / training)
2. Character description (gender / age / hairstyle / clothing / key identifying features)
3. Step count (recommended 4 / 6 / 8 / 9) + grid (2×3 / 3×2 / 3×3 / 2×4)
4. Each step's title + brief description (equipment state / action description)
5. Style (**cinematic real-shot / tokusatsu / fashion editorial / workshop documentary / tutorial screenshot**)
6. Language (title / description text language: Japanese / Chinese / English)
7. Environment (workshop / makeup room / gym / lab / outdoor)
8. Aspect ratio (landscape 16:9 display board / vertical 4:5 manual / 1:1 social media)

## Main Template: 3×2 = 6-Step Real Person Cinematic Gear Dressing Process Board (Tokusatsu Case)

📖 Description

Landscape 16:9 large image, 2 rows 3 columns totaling 6 panels. Top title banner + 6 panel step images (each with red numbered badge + step Japanese title + step description) + bottom slogan banner. Each panel is the same character in a cinematic still, equipment state progressively building step by step.

📝 Prompt

```json
{
  "type": "{argument name=\"theme type\" default=\"Japanese sci-fi armor dressing-process infographic\"}",
  "goal": "Generate a cinematic real-shot process board with the same character as protagonist, progressively showing equipment/operation changes step by step",
  "style": "{argument name=\"overall style\" default=\"cinematic live-action tokusatsu-inspired promotional board, realistic industrial lighting, polished metal surfaces, sharp photographic detail\"}",
  "theme": "{argument name=\"process theme\" default=\"manual pre-battle suit-up sequence for a female hero in a red, silver, black, and blue protector suit\"}",
  "subject": {
    "character": {
      "gender": "{argument name=\"gender\" default=\"female\"}",
      "age": "{argument name=\"age\" default=\"young adult\"}",
      "identity": "{argument name=\"identity\" default=\"helmetless heroine during assembly, face intentionally obscured or anonymized in every unhelmeted panel\"}",
      "hair": "{argument name=\"hair\" default=\"dark brown to black hair tied in a high ponytail with bangs\"}",
      "undersuit": "{argument name=\"undersuit\" default=\"glossy black skintight inner suit with silver chest panel and white neck ring\"}",
      "armor_or_outfit": "{argument name=\"armor description\" default=\"retro-futuristic protector armor with red shoulder and arm plates, silver breastplate and torso plating, circular blue chest core, red waist unit, white gloves, red forearm guards with yellow stripe accents\"}",
      "helmet_or_headpiece": "{argument name=\"helmet description\" default=\"round red-and-silver helmet with black visor\"}"
    },
    "environment": {
      "location": "{argument name=\"location\" default=\"high-tech industrial hangar or armor bay\"}",
      "background_elements": "{argument name=\"background elements\" default=\"metal framework, robotic equipment, tool benches, armor racks, computer monitors, workshop lighting, bay corridor marked BAY-07 in final panel\"}"
    }
  },
  "layout": {
    "header": {
      "count": 2,
      "labels": [
        "{argument name=\"header title\" default=\"Soldat Manual Suit-Up Process\"}",
        "{argument name=\"header subtitle\" default=\"Manual donning of the exclusive protector suit 'Soldat' before battle. Each unit is securely attached and the system is activated.\"}"
      ],
      "design": "wide black-to-red gradient banner across top, large bold white headline text, diagonal red accent stripe"
    },
    "sections": [
      {
        "step_id": 1,
        "title": "{argument name=\"step 1 title\" default=\"1 Inner Suit Check\"}",
        "position": "top-left",
        "labels": ["{argument name=\"step 1 caption\" default=\"Check sensors and connectors on each part. Final body condition confirmation before combat.\"}"],
        "image": "{argument name=\"step 1 image\" default=\"three-quarter view of the heroine in only the black glossy inner suit, looking down while checking or tightening a wrist connector\"}"
      },
      {
        "step_id": 2,
        "title": "{argument name=\"step 2 title\" default=\"2 Chest & Shoulder Armor Attachment\"}",
        "position": "top-center",
        "labels": ["{argument name=\"step 2 caption\" default=\"Attach chest unit and shoulder protectors. Connect and lock the fasteners.\"}"],
        "image": "{argument name=\"step 2 image\" default=\"mid shot with chest armor and red shoulder plates installed, heroine fastening the front torso area with both hands\"}"
      },
      {
        "step_id": 3,
        "title": "{argument name=\"step 3 title\" default=\"3 Waist Unit & Belt Securing\"}",
        "position": "top-right",
        "labels": ["{argument name=\"step 3 caption\" default=\"Attach waist unit and confirm all locks. Check mobility of moving parts.\"}"],
        "image": "{argument name=\"step 3 image\" default=\"mid shot with torso armor completed, heroine tightening or checking the waist belt and side locks\"}"
      },
      {
        "step_id": 4,
        "title": "{argument name=\"step 4 title\" default=\"4 Helmet Preparation\"}",
        "position": "bottom-left",
        "labels": ["{argument name=\"step 4 caption\" default=\"Check helmet visor and internal systems. Confirm headset synchronization.\"}"],
        "image": "{argument name=\"step 4 image\" default=\"heroine holding the red helmet in both hands at chest height, showing the glossy black visor\"}"
      },
      {
        "step_id": 5,
        "title": "{argument name=\"step 5 title\" default=\"5 Helmet Donning & System Activation\"}",
        "position": "bottom-center",
        "labels": ["{argument name=\"step 5 caption\" default=\"Don the helmet and lock the top connector. Full body system activates, chest core glows.\"}"],
        "image": "{argument name=\"step 5 image\" default=\"heroine placing the helmet onto her head with both hands; blue chest core glowing brightly\"}"
      },
      {
        "step_id": 6,
        "title": "{argument name=\"step 6 title\" default=\"6 Suit-Up Complete\"}",
        "position": "bottom-right",
        "labels": ["{argument name=\"step 6 caption\" default=\"Final check of all systems. Enter combat mode. Soldat, ready for deployment!\"}"],
        "image": "{argument name=\"step 6 image\" default=\"full-body frontal hero pose in a futuristic corridor, fully suited with helmet on, arms relaxed at sides\"}"
      }
    ],
    "footer": {
      "count": 1,
      "labels": ["{argument name=\"footer slogan\" default=\"Each piece of equipment protects life and draws out power. Soldat's battle begins here.\"}"],
      "design": "dark red cinematic footer strip with centered white slogan"
    },
    "grid": {
      "rows": 2,
      "columns": 3,
      "panel_count": 6,
      "panel_borders": "thin white dividers",
      "number_badges": "red square badges with white numerals 1-6 placed at the corner of each panel"
    }
  },
  "text_rendering": {
    "language": "{argument name=\"language\" default=\"Japanese\"}",
    "font": "{argument name=\"font style\" default=\"bold sans-serif headline with smaller sans-serif body text\"}",
    "colors": "{argument name=\"text color scheme\" default=\"white text on black, red, and white info bars; red numbered squares with white numerals\"}"
  },
  "composition": "{argument name=\"composition\" default=\"16:9 wide infographic board, six equal photo panels arranged in a 3-by-2 grid, each panel captioned below with a red numbered box from 1 to 6\"}",
  "lighting": "{argument name=\"lighting\" default=\"moody workshop lighting with metallic reflections and red accent lights, realistic shadows, cinematic sci-fi atmosphere\"}",
  "constraints": {
    "must_keep": [
      "Same character (appearance / body type / undersuit) consistent across all panels",
      "Equipment state explicitly progressive in each step (what was put on → what was added next)",
      "Each panel has clear numbering + step title + brief description",
      "Title language, font, and color scheme remain unified",
      "Overall 16:9 display board layout neatly aligned",
      "Lighting / color grading / environment texture consistent"
    ],
    "avoid": [
      "Character face / hairstyle / body type drifting across panels",
      "Equipment state non-progressive (step 4 more fully armored than step 5)",
      "Missing numbering / titles / descriptions",
      "Making the process board into a pose dictionary (no narrative connection between panels)",
      "Making the process board into manga / adding dialogue bubbles",
      "Environment / lighting / filter style inconsistent across panels"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: theme (what process), character (character description), 6 step titles + captions + images (progressive), language
- **Can default**: style, environment, composition, lighting, grid
- **Can randomize**: footer slogan, background detail (unless user specified)

### Auto-Complete Strategy

- User says "want a 6-step gear dressing process" → auto-split 6 steps by "inner layer → upper body → lower body → head preparation → head on → full body complete"
- User says "coffee brewing 6 steps" → auto-split by "grind → weigh → heat water → bloom → pour → serve"
- User says "makeup 6 steps" → auto-split by "primer → concealer → eye makeup → blush → lip color → setting"
- No language specified → default to user's conversation language

## Variant 1: 3×3 = 9-Step Vertical Manual (4:5 / 9:16)

📝 Prompt

```json
{
  "type": "9-step process manual board, vertical poster",
  "layout": { "rows": 3, "columns": 3, "panel_count": 9, "aspect_ratio": "4:5 or 9:16 vertical" },
  "use_case": "more detailed step manual / Xiaohongshu / social media vertical visual / tutorial cover"
}
```

### When to Choose This Variant

- More than 6 steps (e.g., detailed 9-step tutorial)
- Need vertical format (social media / mobile reading)
- Tutorial-style content

## Variant 2: 2×4 = 8-Step Landscape (Suitable for Training Breakdown / Martial Arts Moves)

📝 Prompt

```json
{
  "type": "8-step technical breakdown board, horizontal banner",
  "layout": { "rows": 2, "columns": 4, "panel_count": 8, "aspect_ratio": "16:9 ultra-wide" },
  "use_case": "martial arts move breakdown / fitness movement breakdown / dance technique / gymnastics"
}
```

### When to Choose This Variant

- Horizontal narrative more natural (left → right one move at a time)
- Step count is 8
- Need wider display width

## Variant 3: 4-Step Minimal Process (Suitable for Simple Equipment / Beginner Tutorials)

📝 Prompt

```json
{
  "type": "4-step minimal process board",
  "layout": { "rows": 2, "columns": 2, "panel_count": 4, "aspect_ratio": "1:1" },
  "use_case": "minimal beginner tutorial / simple equipment / 4-step short process"
}
```

### When to Choose This Variant

- Process has only 4 steps
- 1:1 suitable for Instagram / Xiaohongshu cover
- Want clean and concise

## Variant 4: Photography Fashion Editorial Quality (Non-Tokusatsu Style)

📝 Prompt

```json
{
  "type": "fashion editorial multi-step lookbook board",
  "style_override": {
    "rendering": "high-end fashion photography, soft beauty light, magazine editorial spread",
    "lighting": "softbox key light + rim light, clean shadow",
    "background": "seamless studio backdrop or minimal location"
  },
  "use_case": "outfit coordination steps / makeup tutorial / fashion lookbook"
}
```

### When to Choose This Variant

- Need fashion editorial beauty
- Theme is clothing / makeup / beauty
- No need for sci-fi / industrial feel

## Things to Avoid

- Character appearance drifting across panels (**must emphasize character consistency**)
- Equipment state non-progressive (must explicitly stack step by step)
- Missing numbering / titles / descriptions
- Making the process board into a pose dictionary (use `pose-reference-sheet.md`)
- Making the process board into manga / adding dialogue bubbles
- Environment / lighting / filter style inconsistent across panels
- Letting the model freely generate steps (must explicitly list each step's title + description + camera description)
- Generating real person lookalike photos without face blurring / obfuscation (**observe identity privacy constraints**)