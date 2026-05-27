# Workflows

## Full Video Assembly

```
project new → bin import (x clips) → timeline add-track (x tracks) → timeline add-clip (x placements) → filter add → transition add → guide add → export xml
```

### Step-by-Step

```bash
# 1. Create project
cli-anything-kdenlive --json project new -n "MyVideo" -p hd1080p30 -o /abs/path/project.json

# 2. Import clips to bin
cli-anything-kdenlive --json --project /abs/path/project.json bin import /abs/path/interview.mp4 -n "Interview" -d 120
cli-anything-kdenlive --json --project /abs/path/project.json bin import /abs/path/broll.mp4 -n "B-Roll" -d 45
cli-anything-kdenlive --json --project /abs/path/project.json bin import /abs/path/music.mp3 -n "BGM" -d 180 --type audio

# 3. Add tracks
cli-anything-kdenlive --json --project /abs/path/project.json timeline add-track -n "V1" --type video
cli-anything-kdenlive --json --project /abs/path/project.json timeline add-track -n "A1" --type audio

# 4. Place clips
cli-anything-kdenlive --json --project /abs/path/project.json timeline add-clip 0 clip0 -p 0 --out 30
cli-anything-kdenlive --json --project /abs/path/project.json timeline add-clip 0 clip1 -p 30 --out 45
cli-anything-kdenlive --json --project /abs/path/project.json timeline add-clip 1 clip2 -p 0 --out 60

# 5. Filters
cli-anything-kdenlive --json --project /abs/path/project.json filter add 0 0 fade_in_video -p duration=1.5
cli-anything-kdenlive --json --project /abs/path/project.json filter add 0 1 fade_out_video -p duration=1.0

# 6. Transition
cli-anything-kdenlive --json --project /abs/path/project.json transition add dissolve 0 0 -p 28 -d 2.0

# 7. Guides
cli-anything-kdenlive --json --project /abs/path/project.json guide add 30.0 --label "Scene 2"

# 8. Export to Kdenlive XML
cli-anything-kdenlive --json --project /abs/path/project.json export xml -o /abs/path/output.kdenlive
```

## Clip Trimming

```bash
cli-anything-kdenlive --json --project /abs/path/project.json timeline trim 0 0 --in 10 --out 30
```

## Clip Splitting

```bash
cli-anything-kdenlive --json --project /abs/path/project.json timeline split 0 0 15.0
```

## Undo/Redo

```bash
# Check history
cli-anything-kdenlive --json --project /abs/path/project.json session history

# Undo last operation
cli-anything-kdenlive --json --project /abs/path/project.json session undo

# Redo
cli-anything-kdenlive --json --project /abs/path/project.json session redo
```

## Read-Only Commands (no project needed)

```bash
cli-anything-kdenlive --json project profiles          # List profiles
cli-anything-kdenlive --json filter available          # 13 filters with params
cli-anything-kdenlive --json filter available -c color # Filter by category
cli-anything-kdenlive --json export presets             # 8 render presets
```

## Rendering (via melt)

```bash
melt output.kdenlive -consumer avformat:output.mp4 vcodec=libx264 acodec=aac
```

Or open `output.kdenlive` in Kdenlive GUI and render from there.

## Project JSON Structure (for direct editing)

```json
{
  "version": "1.0",
  "name": "MyVideo",
  "profile": {
    "name": "hd1080p30", "width": 1920, "height": 1080,
    "fps_num": 30, "fps_den": 1, "progressive": true,
    "dar_num": 16, "dar_den": 9
  },
  "bin": [
    {"id": "clip0", "name": "Interview", "source": "/abs/path/video.mp4", "duration": 120.0, "type": "video"}
  ],
  "tracks": [
    {"id": 0, "name": "V1", "type": "video", "mute": false, "hide": false, "locked": false, "clips": [
      {"clip_id": "clip0", "in": 0.0, "out": 30.0, "position": 0.0, "filters": [
        {"name": "fade_in_video", "params": {"duration": 1.5}, "enabled": true}
      ]}
    ]}
  ],
  "transitions": [],
  "guides": [
    {"id": 0, "position": 30.0, "label": "Scene 2", "type": "default", "comment": ""}
  ],
  "metadata": {}
}
```
