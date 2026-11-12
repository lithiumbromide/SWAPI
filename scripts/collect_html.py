#!/usr/bin/env python3
"""Copy only HTML files from an extracted CHM tree while preserving paths."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from pipeline_common import clean_output


HTML_SUFFIXES = {".htm", ".html"}


def iter_html_files(root: Path):
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in HTML_SUFFIXES:
            yield path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=Path("extracted"), type=Path, help="Extracted CHM directory.")
    parser.add_argument("-o", "--output", default=Path("API_HTML"), type=Path, help="Output directory for HTML only.")
    parser.add_argument("--clean", action="store_true", help="Remove the output directory before copying.")
    args = parser.parse_args()

    input_root = args.input.resolve()
    output_root = args.output.resolve()

    if not input_root.is_dir():
        raise SystemExit(f"Input directory does not exist: {input_root}")

    if args.clean:
        clean_output(output_root, input_root)
    output_root.mkdir(parents=True, exist_ok=True)

    copied = 0
    for source in iter_html_files(input_root):
        relative = source.relative_to(input_root)
        target = output_root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied += 1

    print(f"copied: {copied}")
    print(f"output: {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
