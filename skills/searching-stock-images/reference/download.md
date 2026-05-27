# Download Reference

## Download Flow

1. **Validate URL**: must start with `https://` and match allowed domain:
   - `images.pexels.com`
   - `images.unsplash.com`, `plus.unsplash.com`
   - `pixabay.com`, `cdn.pixabay.com`
   - `img.freepik.com`
2. **Unsplash**: use `links.download` from search results (not `urls.raw`) — TOS compliance, triggers download count
3. **Destination**: default `./images/` in current project directory. Ask for confirmation if the directory doesn't exist before creating it
4. **Filename**: `<query-slug>-<provider>.<ext>`
   - Default extension: `.jpg`
   - Use `.png` for images with transparency
   - Use `.webp` for size optimization
   - Existing file → skip, inform user
5. **Download**:
   ```bash
   curl -sL --max-time 30 --fail -o "./images/FILENAME" "IMAGE_URL"
   ```
6. **Verify**: `ls -lh "./images/FILENAME"` — alert if > 10MB (user may want smaller resolution)
7. **Attribution**: always remind user:
   ```
   Photo by [Author](author_url) on [Provider]
   ```
   This is TOS-required. No exceptions, even for "placeholders."

## Attribution by Provider

| Provider | Format |
|----------|--------|
| Pexels | `Photo by [Author](photographer_url) on Pexels` |
| Unsplash | `Photo by [Author](user.links.html) on Unsplash` |
| Pixabay | `Photo by [Author](https://pixabay.com/users/USER-USER_ID/) on Pixabay` |
| Magnific | `Resource by [Author](https://www.freepik.com/author-slug) on Freepik` |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Unsplash download via `urls.raw` | Use `links.download` — TOS requires it |
| Missing attribution | Always include author + provider link |
| Overwriting existing file | Skip, inform user |
| Downloading > 10MB without warning | Alert user, suggest smaller resolution |
| Using HTTP URL | All URLs must be HTTPS |