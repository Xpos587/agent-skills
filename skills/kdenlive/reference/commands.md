# Command Reference

## Global Flags

| Flag | Purpose |
|------|---------|
| `--json` | Machine-readable JSON output (always use for agents) |
| `--project PATH` | Path to `.kdenlive-cli.json` project file |

## Project

| Command | Key Flags | Notes |
|---------|-----------|-------|
| `project new` | `-n` name, `-p` profile, `-o` output, `--width`/`--height`/`--fps-num`/`--fps-den` | `-p` sets preset profile, custom via `--width`/`--height`/`--fps-*` |
| `project profiles` | — | Lists all available video profiles |
| `project save` | — | Persist in-memory state to file |
| `project info` | — | Human-readable project summary |
| `project json` | — | Raw project JSON |
| `project open` | — | Open existing project file |

### Video Profiles

hd1080p30, hd1080p25, hd1080p24, hd1080p60, hd720p30, hd720p25, hd720p60, 4k30, 4k60, sd_ntsc, sd_pal

## Bin (Media)

| Command | Key Flags | Notes |
|---------|-----------|-------|
| `bin import SOURCE` | `-n` name, `-d` duration (sec), `--type` video/audio/image/color/title | **Always set `-d`** — defaults to 0.0 |
| `bin list` | — | Lists all bin clips |
| `bin get CLIP_ID` | — | Detailed clip info |
| `bin remove CLIP_ID` | — | Remove from bin |

## Timeline

| Command | Key Flags | Notes |
|---------|-----------|-------|
| `timeline add-track` | `-n` name, `--type` video/audio, `--mute`/`--hide`/`--locked` | Returns integer track ID |
| `timeline remove-track TRACK_ID` | — | Remove track |
| `timeline add-clip TRACK_ID CLIP_ID` | `-p` position (sec), `--in`/`--out` (sec) | TRACK_ID = int, CLIP_ID = "clip0" |
| `timeline remove-clip TRACK_ID CLIP_INDEX` | — | CLIP_INDEX = position in track |
| `timeline trim TRACK_ID CLIP_INDEX` | `--in`/`--out` (sec) | Trim in/out points |
| `timeline split TRACK_ID CLIP_INDEX SPLIT_AT` | — | Split at time offset (seconds) |
| `timeline move TRACK_ID CLIP_INDEX` | — | Move clip to new position |
| `timeline list` | — | List all tracks with clips |

## Filter

| Command | Key Flags | Notes |
|---------|-----------|-------|
| `filter add TRACK_ID CLIP_INDEX FILTER_NAME` | `-p key=value` | Add filter to clip |
| `filter remove TRACK_ID CLIP_INDEX FILTER_INDEX` | — | Remove filter |
| `filter set TRACK_ID CLIP_INDEX FILTER_INDEX` | `-p key=value` | Set filter parameter |
| `filter list TRACK_ID CLIP_INDEX` | — | List filters on clip |
| `filter available` | `-c` category | List all available filters |

### Available Filters

| Filter | Category | Key Params |
|--------|----------|------------|
| brightness | color | level (float, default 1.0) |
| contrast | color | level (float, default 1.0) |
| saturation | color | saturation (float, default 1.0) |
| blur | effect | hblur (int), vblur (int) |
| fade_in_video | transition | duration (float, default 1.0) |
| fade_out_video | transition | duration (float, default 1.0) |
| fade_in_audio | transition | duration (float, default 1.0) |
| fade_out_audio | transition | duration (float, default 1.0) |
| volume | audio | gain (float, default 1.0) |
| crop | effect | — |
| rotate | effect | — |
| speed | effect | — |
| chroma_key | effect | — |

## Transition

| Command | Key Flags | Notes |
|---------|-----------|-------|
| `transition add TYPE TRACK_A TRACK_B` | `-p` position (sec), `-d` duration (sec), `--param key=value` | Between two tracks |
| `transition remove INDEX` | — | Remove transition |
| `transition set INDEX` | `--param key=value` | Set parameter |
| `transition list` | — | List all transitions |

Common transition types: dissolve, wipe

## Guide

| Command | Key Flags | Notes |
|---------|-----------|-------|
| `guide add POSITION` | `--label` text | Position in seconds |
| `guide remove INDEX` | — | Remove guide |
| `guide list` | — | List all guides |

## Export

| Command | Key Flags | Notes |
|---------|-----------|-------|
| `export xml` | `-o` output path | Generate Kdenlive/MLT XML |
| `export presets` | — | List render presets |

### Render Presets

| Preset | Description | Codec | Extension |
|--------|-------------|-------|-----------|
| h264_hq | H.264 High Quality | libx264 + aac | mp4 |
| h264_fast | H.264 Fast/Draft | libx264 + aac | mp4 |
| h265_hq | H.265/HEVC HQ | libx265 + aac | mp4 |
| webm_vp9 | WebM VP9 | libvpx-vp9 + libvorbis | webm |
| prores | Apple ProRes 422 | prores_ks + pcm_s16le | mov |
| lossless | FFV1 Lossless | ffv1 + flac | mkv |
| gif | Animated GIF | gif + none | gif |
| audio_only | Audio Only (WAV) | none + pcm_s16le | wav |

## Session

| Command | Key Flags | Notes |
|---------|-----------|-------|
| `session undo` | — | Undo last operation (up to 50 levels) |
| `session redo` | — | Redo last undone operation |
| `session history` | — | Show undo history |
| `session status` | — | Show session state |
