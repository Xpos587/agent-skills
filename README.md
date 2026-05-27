# Agent Skills

Cross-agent skill collection for AI-driven development. 67 skills for Claude Code, Codex CLI, OpenCode, Cursor, Gemini CLI, and any agent supporting the [Agent Skills](https://agentskills.io) standard.

## Installation

**Via Skills CLI** (cross-agent):

```bash
npx skills add xpos587/agent-skills
```

**Via Claude Code plugin:**

```bash
/plugin marketplace add xpos587/agent-skills
/plugin install agent-skills@agent-skills
```

**Via git submodule** (for project integration):

```bash
git submodule add https://github.com/xpos587/agent-skills.git .agents/shared-skills
```

## Skills

### Research & docs

| Skill | Description |
|-------|-------------|
| `brainstorming` | Explore intent, requirements, and design before creative work |
| `business-analyst` | Product discovery, stakeholder interviews, market research |
| `exploring-codebase` | Navigate unfamiliar code, trace call chains, understand architecture |
| `finding-datasets` | Find datasets for ML, data science, research |
| `finding-docs` | Look up library/framework/API documentation |
| `using-websearch` | Web search, article find, URL content extraction |
| `search-demand-research` | Validate startup ideas via search demand signals |
| `notebooklm` | Interact with Google NotebookLM programmatically |
| `pdf-official` | PDF processing with Python libraries |

### Engineering practices

| Skill | Description |
|-------|-------------|
| `systematic-debugging` | Structured debugging before proposing fixes |
| `verification-loop` | Build, types, lint, tests, security, diff review before PRs |
| `verification-before-completion` | Verify changes work before claiming done |
| `requesting-code-review` | Code review against requirements and standards |
| `executing-plans` | Execute implementation plans with review checkpoints |
| `writing-plans` | Plan implementation strategy before coding |
| `subagent-driven-development` | Execute plans with independent subagent tasks |
| `handoff` | Write/update handoff documents for session continuity |
| `finishing-a-development-branch` | Merge, PR, or cleanup decisions with provenance safety |

### Agent configuration

| Skill | Description |
|-------|-------------|
| `mcp-management` | Install and manage MCP servers across agents |
| `hooks-management` | Manage hooks and automation for coding agents |
| `settings-management` | Configure settings for Claude Code, Codex CLI, etc. |
| `subagents-management` | Create and manage subagents and skills |
| `skills-managing` | Find, install, update, review skills for AI coding agents |
| `plugins-management` | Create, publish, manage Claude Code plugins |
| `optimizing-claude-code` | Audit repos for Claude Code readiness |

### Frontend & design

| Skill | Description |
|-------|-------------|
| `frontend-patterns` | React, Next.js, state management, performance patterns |
| `frontend-design` | High-design-quality frontend interfaces |
| `shadcn` | Manage shadcn components and projects |
| `no-use-effect` | Enforce no-useEffect rule in React code |
| `hallmark` | Anti-AI-slop design for greenfield pages and redesigns |
| `impeccable` | Design, redesign, polish, and optimize frontend interfaces |
| `visual-art-direction` | Moodboards, responsive hero images, art direction |
| `landing-page-generator` | High-converting Next.js landing pages |
| `gsap-framer-scroll-animation` | GSAP ScrollTrigger and Framer Motion scroll animations |
| `color-expert` | Color science, OKLCH, palette generation, accessibility |
| `logo-creator` | Professional logos through iterative AI-assisted design |
| `gpt-image-2` | Image generation and editing |
| `searching-stock-images` | Search Pexels/Unsplash/Pixabay for stock photos |

### Backend & infra

| Skill | Description |
|-------|-------------|
| `api-design-principles` | REST and GraphQL API design |
| `async-python-patterns` | Python asyncio, concurrent programming |
| `python-testing-patterns` | pytest, fixtures, mocking, TDD |
| `polars` | Fast in-memory DataFrames with Polars |
| `writing-containerfiles` | Optimized Containerfiles (Podman/Docker) |
| `writing-github-actions` | GitHub Actions workflows |
| `configuring-prometheus` | Prometheus metric collection and monitoring |
| `cloudflare` | Cloudflare REST API operations |
| `vastai` | Vast.ai GPU instance management via CLI |
| `vastai-sdk` | Vast.ai Python SDK for GPU instances |
| `deployment-patterns` | CI/CD, Docker, health checks, rollback strategies |

### Mobile

| Skill | Description |
|-------|-------------|
| `android-development` | Kotlin, Jetpack Compose, Hilt, multi-module |
| `android-kotlin-compose` | Android apps with Material Design 3 |
| `android-clean-architecture` | Clean Architecture for Android/KMP |
| `android-native-dev` | Android native UI design and development |
| `android-bluetooth` | Android Bluetooth workflows |
| `android-media` | Android media capture and playback |
| `android-e2e-testing` | ADB-based Android testing |
| `camera1-to-camerax` | Migrate Camera1 to CameraX |
| `mobile-developer` | React Native, Flutter, native mobile |
| `r8-analyzer` | R8/ProGuard analysis for Android |
| `migrate-xml-views-to-jetpack-compose` | XML View to Compose migration |

### Tools & utilities

| Skill | Description |
|-------|-------------|
| `github` | GitHub operations via `gh` CLI |
| `docx` | Create, read, edit Word documents |
| `draw-io-diagram-generator` | Generate draw.io diagram files |
| `playwright-cli` | Browser automation and testing |
| `adb-device-testing` | Android device testing via ADB |
| `apktool` | Android APK unpacking and resource extraction |
| `ast-grep` | Structural code search with AST patterns |
| `editorconfig` | Generate .editorconfig files |
| `kdenlive` | Video editing via CLI |
| `telegram` | Telegram message operations |
| `niri-ipc` | Control Niri Wayland compositor |
| `ozon` | Search and analyze products on Ozon |
| `ip-russia` | Russian IP law guidance |
| `writing-human` | Humanize AI-generated Russian text |
| `copywriting` | Copywriting skill |
| `design-review` | Design review skill |
| `platform-design` | Platform design skill |
| `tool-design` | Design tools that agents can use effectively |

### OpenViking

| Skill | Description |
|-------|-------------|
| `openviking` | OpenViking context database |
| `ov-add-data` | Add data to OpenViking |
| `ov-search-context` | Search OpenViking context |
| `ov-server-operate` | Operate OpenViking server |
| `ov-this` | Preserve context across sessions |
| `install-openviking-memory` | Install OpenViking memory plugin |

## License

MIT