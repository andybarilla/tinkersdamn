# Social profile artwork

Editable source files for the band's current social profiles and channel headers.

| File | Output | Size | Intended use |
| --- | --- | --- | --- |
| `avatar.svg` | `public/social/profile-avatar.png` | 1080 × 1080 | Facebook, Instagram, YouTube, Bluesky, and Bandcamp avatar |
| `facebook-cover.svg` | `public/social/facebook-cover.jpg` | 1640 × 624 | Facebook Page cover, with important content kept away from the profile-photo overlay |
| `youtube-banner.svg` | `public/social/youtube-banner.jpg` | 2560 × 1440 | YouTube channel banner; critical content stays inside the centered 1546 × 423 safe area |
| `bluesky-banner.svg` | `public/social/bluesky-banner.jpg` | 1500 × 500 | Bluesky profile banner |
| `bandcamp-header.svg` | `public/social/bandcamp-header.jpg` | 975 × 180 | Bandcamp artist header |

Regenerate everything from the repository root:

```bash
python design/social-profiles/render.py
```

The outputs are available from the deployed site under `/social/`, which also makes them easy to download without digging through the repository.
