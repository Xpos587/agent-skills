# Social Media Interface Mockup Template

This file is used to generate "highly realistic mockups of social media App interfaces + content", such as Weibo / Twitter(X) / Xiaohongshu / Threads / Instagram post pages, feed detail pages, and comment sections.

It is NOT for making real screenshots, but rather for:

- Concept product visuals
- "Fake accounts" for characters / historical figures / virtual IPs on social media
- Marketing demos
- Content creative showcases

## Scope

- Single post detail page (tweet / post)
- Comment section mockup
- Social media profile header
- Dark / light mode UI simulation
- Multi-image grid / multi-image card mockup

## When to Use

- User mentions "social media mockup / tweet mockup / Weibo mockup / Twitter mockup / Moments mockup / Xiaohongshu mockup"
- User wants a celebrity / character / virtual identity to "post something on a platform"
- User wants to generate operational assets that blend UI + content, not real screenshots

Do NOT use this template when:

- User only wants a person avatar
- User wants a real feature screenshot
- User wants a live commerce interface (use `live-commerce-ui.md`)

## Missing Information Priority Questions

When the user only says "make a social media mockup", ask in this order, combining where possible:

1. Platform style: Twitter/X, Xiaohongshu, Weibo, Threads, Instagram, generic social App
2. Color mode: dark or light
3. Account subject: real person / celebrity / fictional character / historical figure / brand account
4. Post content: core copy
5. Whether images are needed, and the image topic
6. Whether I can auto-fill interaction data (likes, retweets, comment text)

If the user says "you fill it in for me", only ask platform style + subject identity + post topic, and auto-fill the rest.

## Main Template: Single Social Post Detail Page

📖 Description

Simulate a "social media post detail page" screenshot mockup, including:

- Top status bar and navigation
- Post author info (avatar / display name / handle / verification badge)
- Post body text and optional hashtags
- Multi-image card (optional)
- Interaction stats and action bar
- Bottom reply bar and bottom tab bar

📝 Prompt

```json
{
  "type": "Mobile social media post detail page mockup",
  "goal": "Generate a highly realistic social media post detail page screenshot for content mockups or concept demos",
  "platform": {
    "name": "{argument name=\"platform\" default=\"Twitter / X\"}",
    "color_mode": "{argument name=\"color mode\" default=\"dark\"}",
    "language": "{argument name=\"interface language\" default=\"Chinese\"}"
  },
  "header": {
    "status_bar": "Top status bar, showing time '{argument name=\"status time\" default=\"19:28\"}', signal, Wi-Fi, battery icons",
    "navigation": "Back arrow + title '{argument name=\"page title\" default=\"Post\"}'"
  },
  "post": {
    "author": {
      "avatar": "{argument name=\"avatar description\" default=\"Half-body portrait of a Chinese emperor in red robes and black hat\"}",
      "display_name": "{argument name=\"display name\" default=\"Zhu Yuanzhang\"}",
      "verified_badge": true,
      "handle": "{argument name=\"handle\" default=\"@Emperor_Ming\"}",
      "extra_badges": "{argument name=\"author extra badges\" default=\"Royal Certification\"}"
    },
    "content": {
      "text": "{argument name=\"post text\" default=\"Ascending the throne today, beginning the Hongwu Era. May we build the Great Ming together with all my ministers!\"}",
      "hashtags": "{argument name=\"hashtags\" default=\"#HongwuYear1 #CoronationCeremony #GreatMingDynasty\"}",
      "media_grid": {
        "count": "{argument name=\"image count\" default=\"3\"}",
        "images": [
          "{argument name=\"image 1\" default=\"Emperor seated on a golden dragon throne, front view\"}",
          "{argument name=\"image 2\" default=\"Wide shot of thousands bowing in the palace courtyard\"}",
          "{argument name=\"image 3\" default=\"Emperor on horseback leading troops forward\"}"
        ]
      }
    },
    "metadata": {
      "timestamp": "{argument name=\"timestamp\" default=\"1:36 PM · January 23, 1368\"}",
      "engagement": "{argument name=\"engagement stats\" default=\"5,432 Reposts · 8,765 Quotes · 20.1K Likes · 102.3K Views\"}"
    },
    "actions": "Bottom row of action icons: Reply, Repost, Like (red heart with count '1'), Share, Upload"
  },
  "comments_preview": {
    "show": "{argument name=\"show top comment\" default=\"true\"}",
    "top_comment": {
      "avatar": "Random generic user avatar",
      "name": "{argument name=\"top commenter\" default=\"Red Turban Veteran Zhang\"}",
      "text": "{argument name=\"top comment text\" default=\"Your Majesty is wise! May the Great Ming last forever!\"}"
    }
  },
  "footer": {
    "reply_bar": {
      "avatar": "Small avatar of the currently logged-in user",
      "placeholder": "{argument name=\"reply placeholder\" default=\"Reply to Zhu Yuanzhang...\"}"
    },
    "navigation_bar": "Bottom tabs: Home, Search, Notifications (with red dot '1'), Messages"
  },
  "style": {
    "rendering": "High-fidelity mobile UI screenshot, roughly 1:2 portrait ratio, looks like a real phone screenshot",
    "consistency": "Overall color scheme strictly follows the platform's official style"
  },
  "constraints": {
    "must_keep": [
      "Platform UI element hierarchy is clear",
      "Avatar, display name, verification badge, and handle must all be correctly rendered",
      "Body text must be clearly readable"
    ],
    "avoid": [
      "Looks like an image collage rather than real UI",
      "Wrong proportions making it look like a desktop web page",
      "Avatar not matching the display name"
    ]
  }
}
```

### Parameter Strategy

- Required: platform, color mode, account subject, post copy
- Defaultable: status bar time, bottom tab bar copy, action bar icons
- Random: interaction stats numbers, top comment text, secondary hashtags

### Auto-fill Strategy

When the user says "fill it in for me":

- Default time to afternoon hours
- Estimate views and likes based on post content popularity (niche content in K, trending in W)
- Comments should use authentic community voice, not generic template phrases
- Hashtags should stay relevant to the post topic, don't stuff unrelated trending keywords

## Variant 1: Light Mode + Xiaohongshu Style

📝 Prompt

```json
{
  "type": "Xiaohongshu-style image-and-text post detail page mockup",
  "platform": {
    "name": "Xiaohongshu",
    "color_mode": "light",
    "language": "Chinese"
  },
  "header": "Top with search bar + avatar + follow button",
  "post": {
    "author": {
      "display_name": "{argument name=\"display name\" default=\"Xiao Man Maya\"}",
      "tag": "{argument name=\"author tag\" default=\"Outfit | Shop Explorer\"}"
    },
    "title": "{argument name=\"post title\" default=\"Shanghai Weekend City Walk Route Share\"}",
    "cover_image": "{argument name=\"cover image\" default=\"Young woman walking sideways on the street\"}",
    "swipeable_images_count": 4,
    "body_text": "{argument name=\"body text\" default=\"Anfu Road → Wukang Road → Wuyuan Road, total 3 km...\"}",
    "tags": ["#WeekendPhotoOp", "#City Walk", "#WhereToGoInShanghaiOnWeekends"]
  },
  "interaction_bar": "Like, Bookmark, Comment, Share, all with numbers",
  "comments_preview": {
    "count": 3,
    "messages": [
      "I want the detailed guide!",
      "I've done this route too, super photogenic",
      "Outfit link please 🔗"
    ]
  },
  "constraints": {
    "must_feel": "Like a real Xiaohongshu image-and-text note, not a poster"
  }
}
```

## Variant 2: Brand Account Official Announcement

Suitable for brand, app, or corporate account style.

📝 Prompt

```json
{
  "type": "Brand official account announcement mockup",
  "platform": {
    "name": "{argument name=\"platform\" default=\"Twitter / X\"}",
    "color_mode": "{argument name=\"color mode\" default=\"light\"}"
  },
  "post": {
    "author": {
      "display_name": "{argument name=\"brand name\" default=\"Anthropic\"}",
      "verified_badge": "official-gold",
      "handle": "{argument name=\"handle\" default=\"@AnthropicAI\"}"
    },
    "content": {
      "text": "{argument name=\"announcement text\" default=\"Today we're introducing Claude Opus 4.7 — our most capable model yet for coding and complex reasoning.\"}",
      "media_grid": {
        "count": 1,
        "images": ["Product launch main visual with large text '{argument name=\"product name\" default=\"Claude Opus 4.7\"}'"]
      }
    },
    "metadata": {
      "engagement": "High interaction volume, e.g., '12K Reposts / 36K Quotes / 158K Likes / 2.3M Views'"
    }
  },
  "constraints": {
    "must_feel": "Like an official account formal announcement",
    "avoid": "Obviously personal or colloquial wording"
  }
}
```

## Variant 3: Auto-fill Mode

For when the user just says "make me a social media mockup."

📝 Prompt

```json
{
  "type": "Social post mockup auto-fill template",
  "mode": "auto-fill",
  "platform_generation": "If user doesn't specify, default to Twitter / X, dark mode, Chinese interface",
  "author_generation": "Randomly generate a plausible but inoffensive account subject",
  "content_generation": "Center around a specific and vivid topic, not broad and empty",
  "media_generation": "Default 1-3 images, closely related to the body text",
  "constraints": {
    "must_feel": "Real, human, credible"
  }
}
```

## Things to Avoid

- Do NOT make UI elements just text stacks — must have avatars, buttons, and icons as the three essentials
- Do NOT mash up social media styles to the point of being unrecognizable as any platform
- Do NOT make the body text longer than a screenshot would normally display, or it will be severely truncated
- Do NOT generate overly personal or emotional language in a "brand official account"
- Do NOT generate a main color that obviously conflicts with the platform's official colors (e.g., pure Xiaohongshu red appearing on X)