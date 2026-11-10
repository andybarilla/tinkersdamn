# Social sharing cards

Editable `1200 × 630` source files for the site's Open Graph and social-preview images.

- `home.svg` → `src/assets/og-home.jpg`
- `covers.svg` → `src/assets/og-covers.jpg`
- `originals.svg` → `src/assets/og-originals.jpg`
- `courtney-live.jpg` is the cropped live portrait used by the first two cards.

After changing an SVG or linked image, regenerate the JPEGs from the repository root:

```bash
python design/social/render.py
```

The renderer embeds linked images before passing the SVG to ImageMagick. This avoids ImageMagick's restrictions on loading external files directly from SVGs.
