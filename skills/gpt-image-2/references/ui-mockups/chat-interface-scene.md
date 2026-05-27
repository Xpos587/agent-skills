# Chat Interface / Conversation Bubble Scene Template

This file is used to generate "chat App interface + conversation bubbles + character avatars" mockups, suitable for:

- WeChat / iMessage / WhatsApp / Discord style chat screenshots
- Conversation-style sticker packs
- "Fake chat" scripts between characters
- Customer service conversation mockups
- Counseling / teaching scenario conversation demos
- AI assistant conversation interface demos

How it differs from `live-commerce-ui.md`:

- Live stream UI: focuses on the person's image, with UI overlaid on top
- Chat interface: focuses on chat bubbles + avatars, the image IS the conversation flow within the App

## Scope

- One-on-one chat screenshot mockup
- Group chat screenshot mockup
- AI-human conversation flow screenshot
- Two-character / multi-character interactive script
- Story-driven screenshot (e.g., "two people's conversation advancing a plot")

## When to Use

- User mentions "chat screenshot / conversation mockup / WeChat chat / iMessage / group chat mockup"
- User wants two or more characters to "have a conversation"
- User wants to generate a conversation flow with sticker-like qualities
- User wants to generate an AI assistant / customer service conversation demo

Do NOT use:

- User wants a social media platform post (use `social-interface-mockup.md`)
- User wants a live stream interface (use `live-commerce-ui.md`)

## Missing Information Priority Questions

1. Platform style: iMessage, WeChat, WhatsApp, Discord, generic IM, AI assistant
2. Color mode: light / dark
3. Conversation characters: how many people, who each one is
4. Conversation topic: specific scenario (argument / confession / business / roleplay / AI Q&A)
5. Whether rich media is needed: emojis, stickers, transfer cards, voice messages
6. Whether I can auto-fill the conversation content

## Main Template: Two-Person Chat Screenshot

📖 Description

Simulate a chat page between two people in an IM App, including top header, scrollable conversation flow, and bottom input bar.

📝 Prompt

```json
{
  "type": "Mobile two-person chat screenshot mockup",
  "goal": "Generate a highly realistic chat screenshot for content creation, script demos, or character conversation visuals",
  "platform": {
    "name": "{argument name=\"platform\" default=\"iMessage\"}",
    "color_mode": "{argument name=\"color mode\" default=\"light\"}",
    "language": "{argument name=\"interface language\" default=\"Chinese\"}"
  },
  "header": {
    "status_bar": "Top status bar, time '{argument name=\"status time\" default=\"21:42\"}', signal, Wi-Fi, battery",
    "navigation": {
      "back": "Back arrow",
      "contact_avatar": "{argument name=\"contact avatar\" default=\"Contact avatar\"}",
      "contact_name": "{argument name=\"contact name\" default=\"Lin Shen\"}",
      "online_status": "{argument name=\"online status\" default=\"Online\"}",
      "right_actions": ["Voice call icon", "Video call icon"]
    }
  },
  "conversation": {
    "self_alignment": "right",
    "other_alignment": "left",
    "message_count": "{argument name=\"message count\" default=\"8\"}",
    "messages": [
      {
        "role": "other",
        "type": "text",
        "text": "{argument name=\"msg 1\" default=\"Hey there? I've been thinking about that thing\"}",
        "timestamp": "21:38"
      },
      {
        "role": "self",
        "type": "text",
        "text": "{argument name=\"msg 2\" default=\"I'm here, go ahead\"}",
        "timestamp": "21:39"
      },
      {
        "role": "other",
        "type": "text",
        "text": "{argument name=\"msg 3\" default=\"I've decided to submit the proposal tomorrow\"}",
        "timestamp": "21:39"
      },
      {
        "role": "self",
        "type": "voice",
        "duration": "00:08",
        "timestamp": "21:40"
      },
      {
        "role": "other",
        "type": "sticker",
        "description": "Cute cat OK sticker",
        "timestamp": "21:40"
      },
      {
        "role": "self",
        "type": "image",
        "description": "Whiteboard with mind map drawn on it",
        "timestamp": "21:41"
      },
      {
        "role": "other",
        "type": "text",
        "text": "{argument name=\"msg 7\" default=\"I agree with this direction, see you tomorrow at 9\"}",
        "timestamp": "21:41"
      },
      {
        "role": "self",
        "type": "text",
        "text": "{argument name=\"msg 8\" default=\"Sounds good, coffee's on me tomorrow morning\"}",
        "timestamp": "21:42"
      }
    ]
  },
  "footer": {
    "input_bar": {
      "left_icons": ["Camera", "Photo", "Voice"],
      "placeholder": "{argument name=\"input placeholder\" default=\"Type a message\"}",
      "right_icons": ["Emoji", "+"]
    },
    "home_indicator": "Bottom home indicator bar"
  },
  "style": {
    "rendering": "High-fidelity mobile chat interface screenshot, portrait ratio, looks like a real phone screenshot",
    "consistency": "Bubble colors, avatar positions, and timestamp styles strictly follow the platform style"
  },
  "constraints": {
    "must_keep": [
      "Bubble left/right alignment matches the sender",
      "Timestamps progress logically, no out-of-order messages",
      "Text clearly readable",
      "Avatars match nicknames"
    ],
    "avoid": [
      "Bubble background and text color contrast too low",
      "Time display not logically consistent within a single day",
      "Image and voice message misalignment"
    ]
  }
}
```

### Parameter Strategy

- Required: platform, both parties' identities, conversation topic
- Defaultable: status bar time, bottom input bar icons, online status
- Random: a few atmospheric messages (stickers, emojis, emoji), but must not overshadow the main conversation

### Auto-fill Strategy

When the user says "help me write a conversation":

- Keep it within 6-10 messages
- Content must have a beginning, middle, and end — not just "mm-hmm, okay"
- Keep each message within reasonable IM length (≤ 35 chars optimal)
- Timestamps must be continuous and logical

## Variant 1: Group Chat Mockup

📝 Prompt

```json
{
  "type": "Group chat mockup",
  "platform": {
    "name": "{argument name=\"platform\" default=\"WeChat\"}",
    "color_mode": "light"
  },
  "group": {
    "name": "{argument name=\"group name\" default=\"Product Team Daily\"}",
    "member_count": "{argument name=\"member count\" default=\"12\"}"
  },
  "conversation": {
    "messages": [
      {"role": "member", "name": "Lily", "text": "Is the requirements review at 4 today?"},
      {"role": "member", "name": "Chen", "text": "Yes, Meeting Room A"},
      {"role": "self", "text": "I've updated the doc in the group"},
      {"role": "system", "text": "A message was recalled"},
      {"role": "member", "name": "PM Wang", "text": "@all Please arrive 5 minutes early"}
    ]
  },
  "constraints": {
    "must_feel": "Like a real work group chat"
  }
}
```

## Variant 2: AI Assistant Conversation Interface

Suitable for: AI product feature demo screenshots, promotional images, teaching materials.

📝 Prompt

```json
{
  "type": "AI assistant conversation interface mockup",
  "platform": {
    "name": "{argument name=\"product name\" default=\"Generic AI Assistant\"}",
    "color_mode": "{argument name=\"color mode\" default=\"light\"}"
  },
  "header": {
    "title": "{argument name=\"chat title\" default=\"New Conversation\"}",
    "model_label": "{argument name=\"model label\" default=\"Claude Opus 4.7\"}",
    "right_actions": ["New conversation", "History"]
  },
  "conversation": {
    "messages": [
      {
        "role": "user",
        "text": "{argument name=\"user question\" default=\"Help me organize the following meeting notes into action items\"}"
      },
      {
        "role": "assistant",
        "type": "structured",
        "content": [
          "1. Action item one: Owner / Deadline",
          "2. Action item two: Owner / Deadline",
          "3. Action item three: Owner / Deadline"
        ]
      },
      {
        "role": "user",
        "text": "{argument name=\"follow up\" default=\"Now generate an email to send to the team\"}"
      },
      {
        "role": "assistant",
        "type": "code-block",
        "language": "markdown",
        "preview": "Email body preview, opening greeting, structured key points in the middle, signature at the end"
      }
    ]
  },
  "footer": {
    "input_bar": {
      "placeholder": "{argument name=\"input placeholder\" default=\"Ask something...\"}",
      "right_button": "Send"
    },
    "tools_row": ["Upload file", "Web", "Code", "Image"]
  },
  "constraints": {
    "must_feel": "Like a real AI product screenshot, not a pure design mockup"
  }
}
```

## Variant 3: Auto-fill Mode

For when the user just says "make a chat screenshot."

📝 Prompt

```json
{
  "type": "Chat interface auto-fill template",
  "mode": "auto-fill",
  "platform_default": "iMessage light mode",
  "scene_generation": "Default to a slice-of-life conversation, don't force a dramatic plot",
  "rule": "If the user doesn't specify the parties' identities, default to a casual conversation between two friends",
  "constraints": {
    "must_feel": "Natural, like a real phone screenshot"
  }
}
```

## Things to Avoid

- Do NOT align all messages on one side — sender and receiver must be distinguished
- Do NOT place the user's own avatar on the self-message side (except for some platform exceptions)
- Do NOT mix UI elements from two different platforms (e.g., iMessage blue bubbles + WeChat bottom bar)
- Do NOT have timestamps that go backwards or are inconsistent between messages
- Do NOT add personal emotional expressions in "customer service / AI assistant" scenarios
- Do NOT make all messages plain text — interleave images / stickers / voice messages for realism