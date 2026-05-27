# Short Video Cover / Stream Thumbnail UI Template

This file is used to generate "short video cover + UI element" mockups, such as:

- Douyin / Kuaishou / Bilibili / Xiaohongshu video covers
- YouTube / Twitch thumbnails
- VTuber / streamer stream covers
- Self-media show covers
- Social platform short video covers

Features:

- Large subject, large text, high information hierarchy
- Must have a visual "click trigger"
- Strong text overlay on person / main subject image

How it differs from `live-commerce-ui.md`:

- Live stream UI: simulates the entire live stream interface (chat / gifts / products)
- This template: just the cover layer, focus on eye-catching title + main visual

## Scope

- Short video platform cover image
- YouTube / Bilibili / Twitch thumbnails
- Show main visual
- Live stream preview image
- Course / knowledge video cover

## When to Use

- User mentions "cover / thumbnail / short video cover / video first frame"
- User wants to generate a high-click-through-rate visual
- User provides show name / title / streamer / topic

Do NOT use:

- User wants a real live stream screenshot (use `live-commerce-ui.md`)
- User wants a social feed detail page (use `social-interface-mockup.md`)

## Missing Information Priority Questions

1. Platform: Douyin / Kuaishou / Xiaohongshu / Bilibili / YouTube / Twitch
2. Content type: knowledge & science / lifestyle vlog / gaming / live stream preview / commercial ad / cute content
3. Main title copy
4. Main subject (real person / cartoon / object / abstract main visual)
5. Style: high-contrast striking / soft & cute / calm minimalist / dark & mysterious
6. Whether subtitle, bullets, and badges are needed

## Main Template: Knowledge-Category High-Contrast Short Video Cover

📖 Description

Simulates a "explainer / analysis video cover that clearly explains one topic", with the subject shifted right, large title text on the left, with subtitle and bullet points.

📝 Prompt

```json
{
  "type": "Short video knowledge cover mockup",
  "goal": "Generate a high-click-through-rate video cover image, including main title, subtitle, main visual, and platform-style small badges",
  "platform": "{argument name=\"platform\" default=\"Generic short video cover\"}",
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"16:9\"}",
  "background": {
    "color_palette": "{argument name=\"color palette\" default=\"Deep blue gradient + highlight yellow\"}",
    "texture": "{argument name=\"texture\" default=\"Subtle noise + soft glow\"}"
  },
  "main_visual": {
    "subject": "{argument name=\"main subject\" default=\"A middle-aged man looking at the camera and pointing to the title on the left\"}",
    "position": "{argument name=\"subject position\" default=\"Right 1/3 of the frame\"}",
    "expression": "{argument name=\"expression\" default=\"Authoritative, slightly surprised\"}"
  },
  "title_block": {
    "main_title": "{argument name=\"main title\" default=\"ChatGPT Uses 99% of People Don't Know About\"}",
    "title_style": "{argument name=\"title style\" default=\"White background black text bold sans-serif + partially highlighted yellow outline\"}",
    "sub_title": "{argument name=\"sub title\" default=\"One trick to 10x your efficiency\"}",
    "bullet_points": {
      "count": "{argument name=\"bullet count\" default=\"3\"}",
      "items": [
        "{argument name=\"bullet 1\" default=\"Auto-organize meeting notes\"}",
        "{argument name=\"bullet 2\" default=\"Batch generate PPT outlines\"}",
        "{argument name=\"bullet 3\" default=\"One-click email template writing\"}"
      ]
    }
  },
  "platform_marks": {
    "logo_or_handle": "{argument name=\"creator handle\" default=\"@EfficiencyNerd\"}",
    "duration_label": "{argument name=\"duration\" default=\"06:24\"}"
  },
  "style": {
    "rendering": "Cover image must look like a real video cover, not a generic poster",
    "contrast": "Title must be readable from 1 meter away",
    "consistency": "Overall style consistent, no style conflicts"
  },
  "constraints": {
    "must_keep": [
      "Main title has the highest visual weight",
      "Main visual and title do not block each other",
      "Color contrast is sufficiently high"
    ],
    "avoid": [
      "Title too long causing messy line breaks",
      "Subject's expression too exaggerated to look cheap",
      "Too many small texts in the corners"
    ]
  }
}
```

### Parameter Strategy

- Required: main title, main subject, platform, style
- Defaultable: subtitle, badges, small text labels
- Random: order and specific wording of bullet points, but strongly related to the topic

### Auto-fill Strategy

- When main title is empty, do NOT fabricate one — must ask
- When subtitle is missing, auto-fill with a "number + verb" sentence pattern
- Bullet points must be ≤ 4
- Default subject expression: "authoritative + slightly surprised"

## Variant 1: Cute-Style VTuber / Streamer Preview Cover

📝 Prompt

```json
{
  "type": "VTuber / Streamer preview cover",
  "style": "anime, high-contrast cute pink scheme, sparkles, hearts, stars decorations",
  "character": {
    "description": "{argument name=\"character description\" default=\"Brown-haired twin-bun anime girl, amber eyes, gentle smile\"}",
    "outfit": "{argument name=\"outfit\" default=\"Pink kimono + white maid apron, cherry blossom hair ornament\"}",
    "pose": "{argument name=\"pose\" default=\"Holding a flower-decorated pink microphone\"}"
  },
  "layout": {
    "background": "{argument name=\"background\" default=\"Pink gradient + sparkles + hearts + ribbons\"}",
    "text_sections": [
      {
        "type": "Top ribbon",
        "text": "{argument name=\"top ribbon\" default=\"Streaming tonight, let's chat~\"}"
      },
      {
        "type": "Main title",
        "text": "{argument name=\"main title\" default=\"Casual Talk Stream\"}",
        "decorations": "3 large peach illustrations around it"
      },
      {
        "type": "Middle ribbon",
        "text": "{argument name=\"middle ribbon\" default=\"Want to spend happy time with everyone ♡\"}"
      },
      {
        "type": "Bottom points",
        "items": [
          "Beginner friendly",
          "Gift recycling",
          "ROMO"
        ]
      },
      {
        "type": "Bottom speech bubble",
        "text": "Comments very welcome ♪ Let's chat a lot"
      }
    ]
  },
  "constraints": {
    "must_feel": "Like a real streamer preview cover, not fan art illustration"
  }
}
```

## Variant 2: Unboxing / Review Video Cover

📝 Prompt

```json
{
  "type": "Unboxing review video cover",
  "platform": "{argument name=\"platform\" default=\"YouTube\"}",
  "aspect_ratio": "16:9",
  "main_visual": {
    "subject": "{argument name=\"main product\" default=\"An unopened tech product packaging box\"}",
    "host": "{argument name=\"host description\" default=\"Half-body of the host on the left side of the frame, exaggerated surprised expression\"}",
    "extras": ["Glowing lines circling the box", "Partially torn packaging creating suspense"]
  },
  "title_block": {
    "main_title": "{argument name=\"main title\" default=\"World First! I Tore It Open\"}",
    "sub_title": "{argument name=\"sub title\" default=\"Is it really worth the price?\"}",
    "label_badge": "{argument name=\"badge\" default=\"Exclusive\"}"
  },
  "constraints": {
    "must_feel": "Strong click trigger + strong curiosity"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Short video cover auto-fill template",
  "mode": "auto-fill",
  "rule": "When user only provides a topic, auto-fill main title, subtitle, main subject, style, and color scheme, but must maintain the three cover essentials: main title, main visual, and strong contrast",
  "constraints": {
    "must_feel": "Like a real eye-catching cover on a video platform"
  }
}
```

## Things to Avoid

- Do NOT let the title fill the entire frame (must leave room for the main visual)
- Do NOT make the title color too close to the background, must have high contrast
- Do NOT squeeze more than 2 lines of subtitle on a single cover
- Do NOT have the subject's face largely obscured by title text
- Do NOT mix UI elements from multiple platforms (e.g., YouTube red play button + Douyin watermark)
- Do NOT pile emoji expressions on a "knowledge & science" cover