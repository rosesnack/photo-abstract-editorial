#!/usr/bin/env python3
"""Join an original photo with an equally sized generated abstract panel."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Proportionally fit and pad an abstract panel to the original photo's "
            "displayed dimensions, then join both into a lossless PNG."
        )
    )
    parser.add_argument("original", type=Path, help="Path to the untouched source photo")
    parser.add_argument("panel", type=Path, help="Path to the generated abstract panel")
    parser.add_argument("output", type=Path, help="Output path; must end in .png")
    return parser.parse_args()


def open_displayed(path: Path) -> Image.Image:
    with Image.open(path) as image:
        return ImageOps.exif_transpose(image).convert("RGBA")


def fit_panel(panel: Image.Image, target_size: tuple[int, int]) -> Image.Image:
    if panel.size == target_size:
        return panel

    fitted = ImageOps.contain(panel, target_size, Image.Resampling.LANCZOS)
    corner = panel.getpixel((0, 0))
    background = corner if corner[3] == 255 else (243, 240, 232, 255)
    exact_panel = Image.new("RGBA", target_size, background)
    offset = (
        (target_size[0] - fitted.width) // 2,
        (target_size[1] - fitted.height) // 2,
    )
    exact_panel.alpha_composite(fitted, offset)
    return exact_panel


def compose(original_path: Path, panel_path: Path, output_path: Path) -> tuple[int, int]:
    if output_path.suffix.lower() != ".png":
        raise ValueError("Output must be PNG to avoid lossy recompression of the photo.")

    original = open_displayed(original_path)
    panel = open_displayed(panel_path)
    width, height = original.size
    panel = fit_panel(panel, original.size)

    if width > height:
        canvas = Image.new("RGBA", (width, height * 2))
        canvas.paste(original, (0, 0))
        canvas.paste(panel, (0, height))
        expected_size = (width, height * 2)
    else:
        canvas = Image.new("RGBA", (width * 2, height))
        canvas.paste(original, (0, 0))
        canvas.paste(panel, (width, 0))
        expected_size = (width * 2, height)

    if panel.size != original.size or canvas.size != expected_size:
        raise RuntimeError("Dimension validation failed before output.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, format="PNG", optimize=True)

    with Image.open(output_path) as saved:
        if saved.size != expected_size:
            raise RuntimeError(
                f"Saved output is {saved.width}x{saved.height}; expected "
                f"{expected_size[0]}x{expected_size[1]}."
            )

    return expected_size


def main() -> None:
    args = parse_args()
    width, height = compose(args.original, args.panel, args.output)
    print(f"Created {args.output} at {width}x{height} pixels.")


if __name__ == "__main__":
    main()
