# Cosmetics / Skincare Packaging Template

This file is used for "cosmetics / skincare bottle, box, and set" packaging design visuals:

- Single skincare bottle packaging design
- Cosmetics series set packaging
- Gift box packaging
- Beauty e-commerce hero image (with packaging)

Characteristics:

- Emphasis on bottle form + label + material
- Emphasis on material texture (glass / frosted / metal cap)
- Usually includes brand name + product name + volume
- Restrained colors, premium feel
- Single bottle or series display

## Scope

- Skincare / cosmetics packaging design
- Beauty gift boxes
- Beauty e-commerce hero images

## When to use

- User mentions "skincare / cosmetics / packaging design / bottle"
- User wants product packaging visuals

Do NOT use for:

- Food / beverage labels → use `beverage-label-design.md`
- Gift box photography → use `product-visuals/packaging-showcase.md`
- Single product white-background image → use `product-visuals/white-background-product.md`

## Missing Information Priority Question Order

1. Brand name + style positioning (luxury / minimalist / artistic / Y2K)
2. Product type (serum / cream / cleanser / perfume)
3. Bottle material (glass / frosted glass / PETG / ceramic)
4. Primary color 1-2
5. Single product / set
6. Volume

## Main Template: Single Skincare Serum Packaging Design

Description

One image, main subject is a skincare serum bottle + outer box, background is a clean scene.

Prompt

```json
{
  "type": "skincare serum single bottle packaging design",
  "goal": "Generate a cosmetics packaging visual usable as product launch hero / packaging proposal / e-commerce main image",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"LUMEN\"}",
    "positioning": "{argument name=\"positioning\" default=\"scientific skincare + minimalist\"}"
  },
  "product": {
    "name": "{argument name=\"product name\" default=\"Photon Repair Serum\"}",
    "subtitle": "{argument name=\"product subtitle\" default=\"PHOTON REPAIR SERUM\"}",
    "volume": "{argument name=\"volume\" default=\"30ml\"}",
    "form": "{argument name=\"bottle form\" default=\"cylindrical glass bottle + dropper\"}",
    "key_ingredient": "{argument name=\"ingredient\" default=\"5% Niacinamide\"}"
  },
  "design": {
    "bottle_material": "{argument name=\"bottle material\" default=\"frosted transparent glass\"}",
    "label_material": "{argument name=\"label material\" default=\"matte adhesive + hot silver text\"}",
    "primary_color": "{argument name=\"primary color\" default=\"#0F4C81 deep blue\"}",
    "accent_color": "{argument name=\"accent color\" default=\"matte silver\"}",
    "typography": "{argument name=\"typography\" default=\"modern sans + small Chinese text\"}"
  },
  "outer_box": {
    "enabled": "{argument name=\"outer box\" default=\"true\"}",
    "shape": "{argument name=\"box shape\" default=\"cube rigid paper box\"}",
    "finish": "{argument name=\"box finish\" default=\"matte paper + hot silver logo\"}"
  },
  "scene": {
    "background": "{argument name=\"background\" default=\"off-white silk + soft light\"}",
    "props": "{argument name=\"props\" default=\"transparent acrylic board + a few water droplets\"}",
    "lighting": "{argument name=\"lighting\" default=\"premium soft light + overhead key light\"}"
  },
  "format": {
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"4:5\"}",
    "composition": "bottle body center-right + outer box behind"
  },
  "constraints": {
    "must_keep": [
      "Bottle material texture realistic (glass should have reflections and refractions)",
      "Label text clearly readable",
      "Overall palette ≤ 3 colors",
      "Premium feel, restrained"
    ],
    "avoid": [
      "Label fonts > 2 types",
      "Background too bright overpowering the product",
      "Bottle proportions distorted",
      "Appearing cheap plastic feel (unless intentional)"
    ]
  }
}
```

### Parameter Strategy

- Must ask: brand name, product type, bottle form
- Can default: material, colors, outer box, scene
- Can randomize: prop details

### Auto-Fill Strategy

- User gives brand positioning + product type → auto-expand bottle / label / colors / scene
- Luxury = black-gold / minimalist = white-blue / artistic = beige-wood / Y2K = high-saturation
- Default 4:5 portrait

## Variant 1: Cosmetics Series Set

Prompt

```json
{
  "type": "cosmetics series set",
  "product": {
    "form": "5-piece set (cleanser + toner + serum + cream + sunscreen)"
  },
  "design": {
    "consistency_rule": "5-piece packaging strictly unified system: same bottle proportions + same fonts + same color palette"
  },
  "scene": {
    "composition": "5 pieces arranged by height + centered"
  },
  "constraints": {
    "must_feel": "set-level + series recognition"
  }
}
```

## Variant 2: Gift Box Packaging

Prompt

```json
{
  "type": "cosmetics gift box",
  "outer_box": {
    "enabled": true,
    "shape": "flat rectangular gift box (half-open)",
    "finish": "velvet wrap + hot gold logo + ribbon"
  },
  "scene": {
    "background": "dark background + spotlight"
  },
  "constraints": {
    "must_feel": "holiday / gift-level"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "cosmetics packaging auto-fill",
  "mode": "auto-fill",
  "rule": "User gives brand + product type + style positioning, auto-decide bottle / label / outer box / scene",
  "constraints": {
    "must_feel": "ready for product launch event"
  }
}
```

## Things to Avoid

- Do not let product name + volume font size differ too much
- Do not let label fonts exceed 2 types
- Do not distort bottle proportions
- Do not let background be too bright overpowering the product
- Do not place the brand logo in an inconspicuous position
- Do not let "luxury positioning" products appear with cheap materials
