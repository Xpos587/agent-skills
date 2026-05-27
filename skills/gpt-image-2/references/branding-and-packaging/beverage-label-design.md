# Beverage / Food Label Design Template

This file is used for "beverage bottle / food can / condiment bottle label + packaging design" visuals:

- Beverage bottle label design
- Food can label
- Condiment bottle label
- Chinese / Japanese / Western various styles
- Product photography + label design hybrid

Characteristics:

- Emphasis on label information (brand name + product name + volume + nutrition facts)
- Label fonts / layout are refined
- Usually includes illustrations / graphic elements
- Packaging combined with environmental photography
- Emphasis on product tone (healthy / luxury / retro / Chinese national trend)

## Scope

- Beverage / food label design
- Condiment packaging
- Chinese national trend / retro style beverages

## When to use

- User mentions "beverage / food / label design / canned / bottled"
- User wants complete "packaging + label" design

Do NOT use for:

- Cosmetics packaging → use `cosmetic-packaging.md`
- Gift box photography → use `product-visuals/packaging-showcase.md`
- General brand board → use `brand-identity-board.md`

## Missing Information Priority Question Order

1. Brand name + category (tea / coffee / juice / condiment)
2. Style tone (Chinese national trend / Japanese / Western modern / retro)
3. Bottle / can form
4. Primary color 1-2
5. Whether illustrations / graphics needed
6. Whether nutrition facts / warning labels needed

## Main Template: Chinese National Trend Beverage Label Design

Description

One image, main subject is a beverage bottle + label design, background is an Eastern-style scene.

Prompt

```json
{
  "type": "Chinese national trend beverage bottle label design",
  "goal": "Generate a beverage bottle + label visual usable as product launch / e-commerce hero image",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"Dongfeng Tea\"}",
    "positioning": "{argument name=\"positioning\" default=\"Chinese national trend + modern\"}",
    "product_name": "{argument name=\"product name\" default=\"Morning Oolong\"}",
    "product_subtitle": "{argument name=\"product subtitle\" default=\"OOLONG MORNING\"}",
    "volume": "{argument name=\"volume\" default=\"330ml\"}"
  },
  "bottle": {
    "form": "{argument name=\"bottle form\" default=\"short stocky glass bottle + metal cap\"}",
    "material": "{argument name=\"material\" default=\"transparent glass + tea liquid visible\"}"
  },
  "label_design": {
    "style": "{argument name=\"label style\" default=\"ink wash + fine brush painting + negative space\"}",
    "primary_color": "{argument name=\"primary color\" default=\"ink green + gold\"}",
    "background_color": "{argument name=\"label bg\" default=\"off-white\"}",
    "illustration": "{argument name=\"illustration\" default=\"fine brush tea mountain + distant peaks\"}",
    "typography": "{argument name=\"typography\" default=\"title Song typeface + English sans\"}",
    "info_strip_bottom": "nutrition facts + volume + ingredient list (small text)"
  },
  "scene": {
    "background": "{argument name=\"background\" default=\"bamboo mat + tea bowl + a green leaf\"}",
    "lighting": "{argument name=\"lighting\" default=\"natural soft light\"}"
  },
  "format": {
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"4:5\"}",
    "composition": "bottle centered + slightly tilted + label clearly facing camera"
  },
  "constraints": {
    "must_keep": [
      "Label style unified (do not mix ink wash + American comics)",
      "Label fonts ≤ 2 types",
      "Nutrition facts / ingredient list in small text readable but not overwhelming",
      "Bottle material realistic"
    ],
    "avoid": [
      "Label design overstuffed",
      "Illustration style conflicting with text style",
      "Background color too bright overpowering illustration",
      "Typos"
    ]
  }
}
```

### Parameter Strategy

- Must ask: brand name, category, style
- Can default: bottle, label, scene
- Can randomize: prop details

### Auto-Fill Strategy

- User gives "Chinese national trend / Japanese / Western modern / retro" style → auto-decide label illustration + palette + fonts
- Default 4:5 portrait
- Default includes small-text nutrition facts

## Variant 1: Japanese Craft-Style Condiment Bottle

Prompt

```json
{
  "type": "Japanese craft-style condiment bottle",
  "brand": {
    "product_name": "{argument name=\"product\" default=\"Round Soybean Soy Sauce\"}"
  },
  "bottle": {
    "form": "vintage short bottle + wooden stopper"
  },
  "label_design": {
    "style": "Japanese craft + hand-drawn calligraphy + beige washi paper",
    "primary_color": "deep brown + vermillion seal"
  },
  "scene": {
    "background": "raw wood table + bamboo basket"
  },
  "constraints": {
    "must_feel": "traditional craft feel"
  }
}
```

## Variant 2: Western Modern Juice

Prompt

```json
{
  "type": "Western modern juice bottle",
  "brand": {
    "product_name": "COLD-PRESS ORANGE",
    "volume": "350ml"
  },
  "bottle": {
    "form": "tall slim transparent PET bottle"
  },
  "label_design": {
    "style": "modern minimal + large text color block + clear nutrition facts",
    "primary_color": "bright orange + white"
  },
  "scene": {
    "background": "white acrylic surface + halved orange"
  },
  "constraints": {
    "must_feel": "healthy + modern + supermarket-friendly"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "beverage / food label auto-fill",
  "mode": "auto-fill",
  "rule": "User gives brand + category + style, auto-decide bottle / label / illustration / scene",
  "constraints": {
    "must_feel": "ready to send to print shop"
  }
}
```

## Things to Avoid

- Do not mix styles (Chinese national trend + American comics in same frame)
- Do not let label fonts exceed 2 types
- Do not omit nutrition facts / ingredient list (unless it is a mockup)
- Do not distort bottle proportions
- Do not let illustration overwhelm to the point where the brand name is unrecognizable
- Do not let background colors be so saturated they overpower the product