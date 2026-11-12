from __future__ import annotations

import os
import shutil
import stat
import sys
from pathlib import Path

if sys.version_info < (3, 10):
    raise SystemExit(f"Python 3.10+ is required, found {sys.version.split()[0]}. Use the project venv described in README.md.")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def make_writable_and_retry(function, path, _error) -> None:
    os.chmod(path, stat.S_IWRITE)
    function(path)


def clean_output(output_root: Path, input_root: Path) -> None:
    protected = (input_root, Path.cwd().resolve())
    if output_root.parent == output_root or any(path.is_relative_to(output_root) for path in protected):
        raise SystemExit(f"Refusing to clean {output_root}: it is a filesystem root or contains the input or current directory.")
    if not output_root.exists():
        return
    handler = {"onexc" if sys.version_info >= (3, 12) else "onerror": make_writable_and_retry}
    try:
        shutil.rmtree(output_root, **handler)
    except OSError as error:
        raise SystemExit(f"Could not delete {output_root}: {error}. Close programs that hold files in it (OneDrive sync, editors, Explorer previews) and retry.") from error
