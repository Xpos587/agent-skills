# Packaging Showcase Image Template

This file is used to generate visuals where "the product packaging itself" is the visual subject:

- Gift box packaging + contents
- Single product outer box + angle combination
- Product series packaging collection
- Limited edition gift box unboxing visual
- Set contents arranged outside the box

How it differs from `branding-and-packaging/` "brand packaging system" templates:

- This template: single product / single gift box as visual center, emphasis on "unboxing-ready" product image
- branding-and-packaging: leans towards "brand packaging design system" visuals, may include multiple SKUs, specification pages

How it differs from `white-background-product.md`:

- White background main image: the product itself alone
- Packaging showcase: box + opened contents (bottles / cards / manuals / accessories inside)

## Scope

- Gift box showcase
- Limited edition set promotional image
- Holiday promotion main image
- Beauty set / food gift pack / tech set
- Contents arrangement image
- Holiday gift box main image

## When to Use

- User mentions "gift box / set / packaging / unboxing image / gift box main image"
- User wants to show both the outer box and contents
- User wants to highlight the packaging design itself

Do NOT use:

- User only wants single product white-background main image (use `white-background-product.md`)
- User wants scene-based (use `lifestyle-product-scene.md`)
- User wants exploded view (use `exploded-view-poster.md`)

## Missing Information Priority Questions

1. Packaging type: paper box / tin box / wooden box / fabric bag / gift box / simple box
2. Contents: how many items, what each is
3. Brand name / series name
4. Style: premium minimalist / festive / light luxury retro / cute playful / Chinese heritage
5. Main color + secondary color
6. Whether to show opened state

## Main Template: Gift Box Opened + Contents Display

📖 Description

Main subject is an opened gift box with contents neatly arranged inside or beside the box, background is a matching color clean surface.

📝 Prompt

```json
{
  "type": "Gift box packaging showcase image",
  "goal": "Generate a gift box showcase image that combines product introduction with a sense of occasion, including outer box + contents + brand information layer",
  "package": {
    "type": "{argument name=\"package type\" default=\"Rigid paper gift box, lid open\"}",
    "shape": "{argument name=\"package shape\" default=\"Rectangular\"}",
    "exterior_color": "{argument name=\"exterior color\" default=\"Dark green + gold foil logo\"}",
    "interior_color": "{argument name=\"interior color\" default=\"Cream white velvet lining\"}",
    "logo": "{argument name=\"package logo\" default=\"Gold brand wordmark\"}",
    "ribbon": "{argument name=\"ribbon\" default=\"Dark green satin ribbon\"}"
  },
  "contents": {
    "count": "{argument name=\"content count\" default=\"4\"}",
    "items": [
      "{argument name=\"content item 1\" default=\"Main product glass bottle\"}",
      "{argument name=\"content item 2\" default=\"Small sachet samples x 2\"}",
      "{argument name=\"content item 3\" default=\"Brand card + usage instructions\"}",
      "{argument name=\"content item 4\" default=\"Metal spoon / accessory\"}"
    ],
    "arrangement": "{argument name=\"content arrangement\" default=\"Contents symmetrically placed inside the box, main product slightly forward and prominent\"}"
  },
  "scene": {
    "background_surface": "{argument name=\"background surface\" default=\"Cream white matte stone surface\"}",
    "background_color_tone": "{argument name=\"background tone\" default=\"Off-white + dark green accents\"}",
    "extra_decorations": [
      "{argument name=\"deco 1\" default=\"Scattered small plant leaves\"}",
      "{argument name=\"deco 2\" default=\"None\"}"
    ]
  },
  "lighting": {
    "key_light": "{argument name=\"key light\" default=\"45° overhead soft light\"}",
    "fill_light": "{argument name=\"fill light\" default=\"Even ambient fill\"}"
  },
  "text_overlay": {
    "enabled": "{argument name=\"text overlay enabled\" default=\"true\"}",
    "brand": "{argument name=\"brand name\" default=\"NORINE\"}",
    "headline": "{argument name=\"headline\" default=\"A gift for important days\"}",
    "subline": "{argument name=\"subline\" default=\"Limited Edition · 2026 Holiday\"}",
    "position": "Upper left or upper right, clean layout"
  },
  "style": {
    "rendering": "High-resolution commercial product photography, contents with realistic textures, packaging materials clearly identifiable",
    "consistency": "Color palette and materials consistent, image restrained and not cluttered"
  },
  "constraints": {
    "must_keep": [
      "Outer box recognizable + logo readable",
      "Contents clearly countable",
      "Box lid opening angle natural and not awkward",
      "Text position does not compete with the main subject"
    ],
    "avoid": [
      "Contents squeezed together hard to distinguish",
      "Box shape looking irregular",
      "Lighting washing out the gold foil logo completely",
      "Person / model / hands appearing in frame"
    ]
  }
}
```

### Parameter Strategy

- Required: packaging type, contents composition, brand name, main color
- Defaultable: ribbon, lining color, decorations
- Random: small decorative items (within the color palette)

### Auto-fill Strategy

- Beauty gift box default: cream lining + gold logo + glass bottle as main product
- Holiday food gift box default: wooden box or kraft paper + red ribbon + multiple small sachet contents
- Tech gift box default: black rigid box + gray foam lining + main device + accessories
- Slogan defaults to "Limited Edition / Holiday / Anniversary" closing phrase

## Variant 1: Festive Gift Box

📝 Prompt

```json
{
  "type": "Festive gift box showcase image",
  "package": {
    "type": "Rigid paper gift box, lid open",
    "exterior_color": "{argument name=\"exterior color\" default=\"Chinese red + gold foil\"}",
    "interior_color": "Gold velvet lining",
    "ribbon": "Gold bow"
  },
  "contents": {
    "items": [
      "{argument name=\"content 1\" default=\"Red gift bags x 2\"}",
      "{argument name=\"content 2\" default=\"Main gift (food / tea / craft item)\"}",
      "{argument name=\"content 3\" default=\"Greeting card\"}"
    ]
  },
  "scene": {
    "background_surface": "Gold glossy or deep red velvet",
    "extra_decorations": ["Scattered gold particles", "Plum blossom branch accents"]
  },
  "constraints": {
    "must_feel": "Festive gravitas, Eastern celebration"
  }
}
```

## Variant 2: Minimalist Light Luxury Gift Box

📝 Prompt

```json
{
  "type": "Minimalist light luxury gift box showcase image",
  "package": {
    "type": "Matte rigid paper gift box",
    "exterior_color": "Cream + thin gray line",
    "interior_color": "Dark gray velvet",
    "logo": "Debossed brand wordmark + tiny gold foil"
  },
  "contents": {
    "items": [
      "{argument name=\"content 1\" default=\"Main glass bottle\"}",
      "{argument name=\"content 2\" default=\"Accessory / instruction card\"}"
    ]
  },
  "scene": {
    "background_surface": "Warm gray matte stone slab",
    "extra_decorations": []
  },
  "constraints": {
    "must_feel": "Restrained, dignified"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Packaging showcase image auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides category and brand only. Auto-determine packaging type, contents combination, color scheme, and decorations, but must maintain packaging as the visual center",
  "constraints": {
    "must_feel": "Can be directly used as brand website or e-commerce page hero"
  }
}
```

## Things to Avoid

- More than 6 content items starts to look cluttered; recommend 3-5 items
- Do NOT put all contents back inside the box; at least 1 item should be half-out or forward
- Do NOT use highly reflective metal surfaces as background (makes gold foil logo unreadable)
- Do NOT put other brand logos in the image besides the product brand
- Do NOT make the gift box look like a "shipping box being opened" — that cheap feel
- Do NOT use overly saturated colored backgrounds that distort the box's true colors