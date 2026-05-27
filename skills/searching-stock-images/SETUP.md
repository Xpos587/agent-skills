# Stock Images — Setup Guide

## Method 1: Environment Variables (Recommended)

Add to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
export PEXELS_API_KEY="your_pexels_key"
export UNSPLASH_ACCESS_KEY="your_unsplash_key"
export PIXABAY_API_KEY="your_pixabay_key"
export MAGNIFIC_API_KEY="your_magnific_key"
```

Restart your shell or `source` the file. Keys are never written to disk in plaintext.

## Method 2: Config File

Run this command to create the secure config file:

```bash
mkdir -p ~/.config/stock-images && cat > ~/.config/stock-images/keys.json << 'KEYS'
{
  "pexels": "YOUR_PEXELS_KEY",
  "unsplash": "YOUR_UNSPLASH_KEY",
  "pixabay": "YOUR_PIXABAY_KEY",
  "magnific": "YOUR_MAGNIFIC_KEY"
}
KEYS
chmod 600 ~/.config/stock-images/keys.json
```

Replace the placeholder values with your actual keys. Remove any providers you don't have.

## Get API Keys (all free)

1. **Pexels**: https://www.pexels.com/api/
2. **Unsplash**: https://unsplash.com/developers
3. **Pixabay**: https://pixabay.com/api/docs/
4. **Magnific (Freepik)**: https://docs.magnific.com/authentication

## Verify Setup

ENV vars:

```bash
for v in PEXELS_API_KEY UNSPLASH_ACCESS_KEY PIXABAY_API_KEY MAGNIFIC_API_KEY; do printenv "$v" >/dev/null 2>&1 && echo "$v: set"; done
```

Config file:

```bash
test -f ~/.config/stock-images/keys.json && ls -la ~/.config/stock-images/keys.json
```

Permissions should be `-rw-------`. Validate JSON without printing keys:

```bash
jq empty ~/.config/stock-images/keys.json && echo "Config JSON is valid"
```
