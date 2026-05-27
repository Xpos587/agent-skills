# E-Commerce Livestream / Social Live UI Mockup Template

This file is used to generate "portrait image + live stream platform overlay UI" complex visual results.

Suitable for:

- E-commerce live stream interface
- Social media live stream screenshot
- Streamer selling mockup
- Chat bubble + gift popup + product card live stream UI composite image

## Usage Rules

The key point of this template is not to fix a single streamer, but to break the image into a stable structure, allowing the user to:

- Specify a real person photo
- Specify a celebrity name
- Specify a character description
- Fully randomly generate a streamer persona

Similarly, product cards, chat messages, background brands, and gift content can all be:

- User-specified
- Using default values
- Randomly generated within reasonable bounds

## Missing Information Priority Questions

When the user only says "make an e-commerce live stream UI mockup", ask in priority order:

1. Streamer source: real person photo / celebrity name / character description / random generation
2. Product info: what's being sold
3. Platform style: more like Douyin / Xiaohongshu / Taobao Live / generic live stream mockup
4. Language: Chinese interface or English interface

If the user doesn't want to answer each item, you can explicitly offer an "auto-fill mode":

- You randomly fill in secondary information
- Keep only the user-specified core parts

## Template 1: Generic E-Commerce Live Stream UI Mockup

📖 Description

Generate a realistic social media live stream interface overlaid on a portrait, with customizable chat messages, gift popups, and a product purchase card.

📝 Prompt

```json
{
  "type": "E-commerce live stream UI mockup",
  "goal": "Generate a highly realistic live commerce screenshot-style visual, with the streamer portrait as the main subject, overlaid with complete live stream UI elements, suitable for social sharing, concept mockups, or commerce visual presentations",
  "subject": {
    "source_mode": "{argument name=\"host source mode\" default=\"celebrity-name\"}",
    "reference_photo": "{argument name=\"host reference photo\" default=\"none\"}",
    "celebrity_name": "{argument name=\"host name\" default=\"Elon Musk\"}",
    "description": "{argument name=\"host portrait description\" default=\"Smiling, half-body portrait, wearing a black T-shirt with white tech graphics\"}",
    "pose": "{argument name=\"host pose\" default=\"Facing the camera, leaning slightly forward, as if talking in a live stream\"}",
    "expression": "{argument name=\"host expression\" default=\"Relaxed, confident, engaging\"}"
  },
  "scene": {
    "background_style": "{argument name=\"background style\" default=\"Tech company launch event backstage + live stream set\"}",
    "left_background": "Left side showing a screen with '{argument name=\"left background logo\" default=\"SPACEX\"}' text",
    "right_background": "Right side showing a red '{argument name=\"right background logo\" default=\"Tesla T logo\"}' and a dark car",
    "lighting": "{argument name=\"lighting\" default=\"Bright, commercial feel, studio-level key lighting, while maintaining the live stream screenshot feel\"}"
  },
  "ui_overlay": {
    "platform_style": "{argument name=\"platform style\" default=\"Generic Chinese live commerce platform UI\"}",
    "top_header": {
      "host_info": "Avatar, name '{argument name=\"host name\" default=\"Elon Musk\"}', subtitle '55.6K likes this session', red 'Follow' button",
      "rank_badge": "Gold icon with 'Ranked #1 on platform'",
      "viewer_stats": "3 top viewer avatars, showing '12.3w', '8.6w', '5.7w', total '687K', 'X' close button",
      "right_links": "'More streams >', 'Gift Hall 0/24' (with blue 'Classic' label)"
    },
    "mid_left_gifts": {
      "count": 2,
      "items": [
        "Avatar 'Tech enthusiast', 'Sent hearts', heart icon x 1314",
        "Avatar 'Star voyager', 'Sent rocket', rocket icon x 666"
      ]
    },
    "bottom_left_chat": {
      "system_message": "Level 37 badge 'Cosmic Wanderer joined the stream'",
      "message_count": 7,
      "messages": [
        "LittleRocket: Musk! The future is bright! 🚀",
        "future: When is Tesla Model 2 coming out?",
        "StarryDreamer: Can SpaceX reach Mars this year?",
        "AIExplorer: How's Neuralink progressing?",
        "CoolNetizen: Hey Boss!",
        "Mars: First time in your stream, so excited!",
        "User123: Tell us about AI, will it replace humans?"
      ]
    },
    "bottom_right_product_card": {
      "hot_tag": "Orange 'Hot seller x 1888'",
      "image": "{argument name=\"product image subject\" default=\"Tesla Cybertruck\"}",
      "title": "{argument name=\"product name\" default=\"Tesla Cybertruck Electric Pickup\"}",
      "price": "{argument name=\"product price\" default=\"¥ 1,618,000\"}",
      "button": "Red 'Grab' button",
      "floating_animation": "Semi-transparent hearts floating upward along the right edge"
    },
    "bottom_bar": {
      "input_field": "'Say something...'",
      "icons": ["Smiley", "Three dots", "Shopping cart", "Gift box", "Share"]
    }
  },
  "style": {
    "visual_target": "Realistic live stream screenshot mockup, not a pure UI design draft or a pure photography poster, but a natural fusion of real streamer portrait and platform overlay UI",
    "rendering": "Real portrait photography + platform overlay UI + commercial advertising-level clarity",
    "color_tone": "Tech feel, commercial feel, platform live stream atmosphere coexisting",
    "composition": "Portrait live stream screenshot composition, person occupying visual center, UI clearly readable, product card in bottom right, chat area in bottom left"
  },
  "constraints": {
    "must_keep": [
      "Streamer is the visual center",
      "Live stream UI layers are clearly separated",
      "Product card, chat area, and gift area must all appear",
      "Overall looks like a real live stream screenshot, not a simple collage"
    ],
    "avoid": [
      "UI text completely unreadable",
      "Interface overly crowded",
      "Distorted facial features",
      "Product card perspective errors",
      "Chat box blending into the background"
    ]
  }
}
```

## Template 2: Brand Founder Live Stream Selling Mockup

📖 Description

Suitable for "brand founder / tech entrepreneur / celebrity principal" appearing on camera for a high-credibility live commerce scenario.

📝 Prompt

```json
{
  "type": "Brand founder live commerce mockup",
  "subject": {
    "identity": "{argument name=\"host identity\" default=\"Tech company founder\"}",
    "name": "{argument name=\"host name\" default=\"Elon Musk\"}",
    "description": "{argument name=\"host portrait description\" default=\"High-credibility real-person half-body portrait, slight smile, as if explaining product highlights\"}"
  },
  "product": {
    "name": "{argument name=\"product name\" default=\"Flagship smart electric vehicle\"}",
    "category": "{argument name=\"product category\" default=\"Tech hardware\"}",
    "price": "{argument name=\"product price\" default=\"¥ 399,999\"}",
    "selling_points": [
      "{argument name=\"selling point 1\" default=\"Autonomous driving assistance\"}",
      "{argument name=\"selling point 2\" default=\"Minimalist smart cabin\"}",
      "{argument name=\"selling point 3\" default=\"Long range\"}"
    ]
  },
  "ui": {
    "product_card": "High-credibility commerce card, showing main image, title, price, strong buy button",
    "chat_style": "Viewers asking about price, release date, and features",
    "gift_style": "Tech circle / fan-oriented gift messages"
  },
  "constraints": {
    "goal": "Make the entire image look like the brand founder is genuinely live streaming, not a simple concept poster"
  }
}
```

## Template 3: Random Streamer + Random Product Auto-fill Mode

📖 Description

For when the user just says "make me a live commerce interface image" without specifying a person or product.

📝 Prompt

```json
{
  "type": "Live commerce auto-fill template",
  "mode": "auto-fill",
  "subject": {
    "host_generation_mode": "random-but-plausible",
    "description": "Auto-generate a streamer persona suitable for on-camera presence, with clear character traits, professional feel, and camera presence"
  },
  "product": {
    "generation_mode": "random-but-coherent",
    "rule": "Auto-generate products consistent with the streamer's persona and setting, avoid obviously mismatched combinations"
  },
  "ui": {
    "chat_messages": "Auto-generate product-related messages that sound like real live stream viewers",
    "gift_messages": "Auto-generate a small number of gift popups to enhance the live atmosphere",
    "product_card": "Auto-generate reasonable product name, price, and hot-seller tag"
  },
  "constraints": {
    "must_feel": [
      "Real",
      "Clear platform feel",
      "Rich information but not cluttered",
      "Suitable as a case study mockup"
    ]
  }
}
```

## How to Generate Variants from This Template

### Variant 1: User Provides a Photo

- Change `subject.source_mode` to `reference-photo`
- Use the user's image as the main subject reference
- Keep other UI fields in the template structure

### Variant 2: User Provides a Celebrity Name

- Use `celebrity-name`
- Keep the description field as a supplementary visual description

### Variant 3: User Provides a Character Description Only

- Use `text-description`
- Make the `description` field in the template the dominant field

### Variant 4: User Provides Nothing

- Use `auto-fill`
- Only ask a few essential questions for core fields
- Remaining fields can be randomly filled