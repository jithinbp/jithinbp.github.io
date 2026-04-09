#!/usr/bin/env python3
"""
Strip YAML front matter from markdown files in this directory.

Usage:
  python3 remove_front_matter.py --dry-run
  python3 remove_front_matter.py --apply
"""

from __future__ import annotations

import argparse
from pathlib import Path


def strip_front_matter(text: str) -> str:
    # Front matter must start at top of file with --- line
    if not text.startswith("---\n"):
        return text

    lines = text.splitlines(keepends=True)
    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx == -1:
        return text

    # Remove front matter and optional immediate blank lines
    content = "".join(lines[end_idx + 1 :])
    return content.lstrip("\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Remove YAML front matter from .md files in static/md.")
    parser.add_argument("--apply", action="store_true", help="Write changes to files.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change.")
    args = parser.parse_args()

    if not args.apply and not args.dry_run:
        parser.error("Specify one mode: --dry-run or --apply")

    base = Path(__file__).resolve().parent
    md_files = sorted(p for p in base.glob("*.md") if p.name != "README.md")

    changed = 0
    for path in md_files:
        original = path.read_text(encoding="utf-8")
        stripped = strip_front_matter(original)
        if stripped != original:
            changed += 1
            print(f"{'Would update' if args.dry_run else 'Updated'}: {path.name}")
            if args.apply:
                path.write_text(stripped, encoding="utf-8")

    if changed == 0:
        print("No files needed changes.")
    else:
        print(f"Done. {changed} file(s) {'would be' if args.dry_run else 'were'} updated.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

