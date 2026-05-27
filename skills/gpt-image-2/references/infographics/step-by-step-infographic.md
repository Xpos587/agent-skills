# Step-by-Step / Process Infographic Template

This file is used for generating "step-by-step / process / how-to / tutorial" style infographics:

- Recipe / baking step diagrams
- Operation tutorials / app usage flows
- Fitness movement breakdowns
- Makeup / skincare routines
- Travel / reimbursement / application processes
- Parenting / DIY operation steps

Characteristics:

- Each step has a clear number
- Each step is paired with a simple illustration / icon
- Guide arrows / connecting lines between steps
- Usually 3-7 steps, maximum 9 steps
- Style leans toward illustration feel, warm, easy to understand (**distinctly different from "engineering-precision flowcharts"**)

## Scope

- Recipe / operation / tutorial displays
- "Learn in X steps" type content
- DIY / handicraft / renovation steps
- Parenting / fitness / beauty steps
- User onboarding / beginner guides

## When to use

- User mentions "steps / process / how-to / tutorial / X steps / guide / recipe / makeup steps"
- User wants "readers can follow along step by step"
- User wants the visual "illustration feel, warm, easy to understand" (not engineering feel)

Do NOT use for:

- User wants "engineering-precision flowchart" (diamond decisions, Yes/No branches) → use `technical-diagrams/flowchart-decision.md`
- User wants "comic storyboard" → use `storyboards-and-sequences/recipe-process-flowchart.md`
- User wants "method pipeline paper figure" → use `academic-figures/method-pipeline-overview.md`
- User wants "bento grid high-density information" → use `infographics/bento-grid-infographic.md`

## Missing Information Priority Question Order

1. Topic + step count (e.g. "3 steps to make pasta / 5 steps to set up dev environment / 7 steps for daily skincare")
2. Specific content for each step (title + one or two sentences of explanation)
3. Color tone (warm food / fresh skincare / cartoon tutorial / chalkboard teaching)
4. Layout method (vertical waterfall / horizontal row / winding path / circular loop)
5. Whether to include cover / finished image (a "finished product image" at the beginning or a "finished product display" at the end)
6. Aspect ratio (Xiaohongshu 3:4 / WeChat 16:9 / 1:1)

## Main Template: Step-by-Step Tutorial Infographic

Description

The entire image is arranged with 3-7 numbered steps, each step containing: a number badge + step title + step illustration + brief text explanation, steps connected by arrows / connecting lines.

Prompt

```json
{
  "type": "Step-by-step tutorial infographic",
  "goal": "Generate a tutorial diagram with strong illustration feel, warm and easy to understand, that readers can follow step by step",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"3:4 portrait\"}",
    "background": "{argument name=\"background\" default=\"warm cream #FAF6EE with slight paper texture\"}"
  },
  "header": {
    "main_title": "{argument name=\"main_title\" default=\"5 Steps to Make Japanese Omurice\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"Beginner-friendly · 20 minutes\"}",
    "optional_finished_image": "{argument name=\"finished_image\" default=\"A 'finished product small image' in the top-right corner + decorative border\"}"
  },
  "palette": {
    "primary": "{argument name=\"primary\" default=\"warm orange #E89F71\"}",
    "secondary": "{argument name=\"secondary\" default=\"sage green #9FB89E\"}",
    "neutral": "{argument name=\"neutral\" default=\"deep brown #4A3A2E\"}",
    "rule": "Limit to 3-4 main colors, illustration style consistent across steps"
  },
  "layout": {
    "style": "{argument name=\"layout_style\" default=\"vertical-zigzag\"}",
    "options_explained": {
      "vertical-stack": "Pure vertical waterfall, one step per row",
      "vertical-zigzag": "Z-shaped serpentine, odd/even steps alternate left and right",
      "horizontal-row": "Horizontal 3-5 steps side by side",
      "circular": "Distributed on a ring (suitable for cyclic types)",
      "winding-path": "Winding path, steps distributed along the path (suitable for cooking / travel)"
    }
  },
  "steps": {
    "count": "{argument name=\"step_count\" default=\"5\"}",
    "structure_per_step": [
      "Large number badge (circle / rounded square, unified color, number font large and bold)",
      "Step title (4-8 characters, bold)",
      "Illustration icon / small scene (hand-drawn feel, single object or action illustrative)",
      "1-2 lines of explanation text"
    ],
    "items_example": [
      "01 Prepare Ingredients: 3 eggs, 1 bowl of rice, 1/4 onion, diced ham",
      "02 Saute Onions: Melt butter in pan, saute onions until translucent",
      "03 Mix in Rice: Add rice and ham, season and stir-fry",
      "04 Make Egg Wrap: Beat eggs in another pan, make a half-cooked egg sheet",
      "05 Wrap and Plate: Place fried rice on egg sheet, fold into boat shape, squeeze ketchup"
    ]
  },
  "connectors": {
    "style": "{argument name=\"connector_style\" default=\"hand-drawn curved arrows\"}",
    "rule": "Visual guidance required between steps: arrows / dashed lines / footprints / ingredient splash elements all acceptable"
  },
  "footer": {
    "tip": "{argument name=\"tip\" default=\"Tip: Ketchup can be swapped for Korean chili sauce for a more savory flavor\"}",
    "credit": "{argument name=\"credit\" default=\"@your_handle\"}"
  },
  "constraints": {
    "must_keep": [
      "Illustration style consistent across steps (hand-drawn / flat / cartoon — pick one, don't mix)",
      "Number badge design completely consistent (color, font size, shape)",
      "Visual connections between steps clear",
      "Text no more than two lines per step",
      "Illustration sizes consistent or graded by importance"
    ],
    "avoid": [
      "Engineering diagram style (right angles, drab palette, diamond decision boxes)",
      "Different illustration styles for each step",
      "Step count < 3 (too short for a tutorial) or > 9 (too long to read)",
      "No numbering / inconsistent numbering style",
      "Step explanation exceeding 3 lines (becomes long text)",
      "Using Helvetica and other cold-feel fonts (recommend hand-lettered / rounded / friendly fonts)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `step_count`, each step's title (i.e. actual content of `items_example`)
- **Can default**: `background`, `palette` (select by topic — food uses warm orange, skincare uses macaron, tech tutorials use mint), `layout_style` (default vertical-zigzag), `connector_style`
- **Can randomize**: each step's illustration specific rendering, whether connector is arrow or dashed line, decorations (splashes / sparkles / small labels)

### Auto-Fill Strategy

- User only provides topic (e.g. "5 steps to make pasta"): auto-fill 5 specific step contents, auto-select warm food palette, auto-add finished product small image
- User says "Xiaohongshu style" → add hand-drawn decorations + macaron color palette
- User says "beauty / skincare" → switch palette to dusty pink + cream
- User says "fitness" → switch palette to mint + coral, illustrations use figure action poses
- User says "DIY / handicraft" → add tool emoji / materials list
- User says "tech tutorial" → switch palette to mint + slate, illustrations use screenshot frames

## Variant 1: Horizontal 3-5 Step Process

```json
{
  "type": "Horizontal step-by-step tutorial infographic",
  "modify": {
    "aspect_ratio": "16:9 landscape",
    "layout_style": "horizontal-row",
    "step_count": "3-5",
    "rule": "Each step equal width side by side, connected by bold arrows, number above and explanation below each step"
  }
}
```

Suitable for: web hero sections, PPT single pages, product onboarding pages.

## Variant 2: Winding Path Process

```json
{
  "type": "Winding path step-by-step tutorial infographic",
  "modify": {
    "layout_style": "winding-path",
    "background": "Illustration-style map base (grass / kitchen / city street)",
    "rule": "Steps distributed along a winding path, with footprints / ingredients / tools drawn on the path, each step on a small card by the roadside",
    "vibe": "travel journal, cooking adventure, children's tutorial"
  }
}
```

Suitable for: children's tutorials, travel planning, story-driven step displays.

## Variant 3: Circular Loop Steps

```json
{
  "type": "Circular loop step infographic",
  "modify": {
    "layout_style": "circular",
    "step_count": "4-8",
    "rule": "Steps arranged on a large ring, clockwise, arrows along the ring, center holds theme text + summary",
    "vibe": "PDCA / seasonal cycle / lifecycle / monthly routine"
  }
}
```

Suitable for: PDCA cycles, monthly plan cycles, fitness routines, seasonal cycles.

## Things to Avoid

- Too many steps (>9) or too few (<3)
- Mixed illustration styles across steps (one step hand-drawn, another flat)
- Number badge design different for each step
- No visual connections (steps look like scattered cards)
- Using engineering flowchart diamond decisions / right-angle arrows → loses illustration warmth
- Using Helvetica / Arial cold-feel fonts
- Step explanations exceeding 3 lines → becomes long text, loses infographic quality
- Making a "flowchart" using this template (for flowcharts use `technical-diagrams/flowchart-decision.md`)