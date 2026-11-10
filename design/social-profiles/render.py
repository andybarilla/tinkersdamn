#!/usr/bin/env python3
"""Render editable social-profile artwork into public/social."""

from __future__ import annotations

import base64
import mimetypes
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUT = ROOT / "public/social"
CARDS = {
    "avatar.svg": ("profile-avatar.png", "PNG32", None),
    "facebook-cover.svg": ("facebook-cover.jpg", None, "91"),
    "youtube-banner.svg": ("youtube-banner.jpg", None, "91"),
    "bluesky-banner.svg": ("bluesky-banner.jpg", None, "91"),
    "bandcamp-header.svg": ("bandcamp-header.jpg", None, "91"),
}
HREF_RE = re.compile(r'href="([^"#]+)"')


def embed_linked_images(svg_path: Path) -> str:
    svg = svg_path.read_text()

    def replace(match: re.Match[str]) -> str:
        href = match.group(1)
        if href.startswith(("data:", "http://", "https://")):
            return match.group(0)
        asset = (svg_path.parent / href).resolve()
        mime = mimetypes.guess_type(asset.name)[0] or "application/octet-stream"
        encoded = base64.b64encode(asset.read_bytes()).decode("ascii")
        return f'href="data:{mime};base64,{encoded}"'

    return HREF_RE.sub(replace, svg)


def main() -> None:
    magick = shutil.which("magick")
    if not magick:
        raise SystemExit("ImageMagick's `magick` command is required.")

    OUTPUT.mkdir(parents=True, exist_ok=True)

    for source_name, (output_name, png_format, quality) in CARDS.items():
        source = HERE / source_name
        output = OUTPUT / output_name
        embedded = embed_linked_images(source)

        with tempfile.NamedTemporaryFile(suffix=".svg", mode="w", delete=False) as temp:
            temp.write(embedded)
            temp_path = Path(temp.name)

        command = [magick, "-background", "none", str(temp_path)]
        if png_format:
            command.extend([png_format + ":" + str(output)])
        else:
            command.extend(["-quality", quality or "91", str(output)])

        try:
            subprocess.run(command, check=True)
        finally:
            temp_path.unlink(missing_ok=True)

        print(f"Rendered {source.relative_to(ROOT)} -> {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
