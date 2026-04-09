#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path
from pypdf import PdfReader


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: extract_pdf_text.py <pdf-path> [output-txt]", file=sys.stderr)
        return 2
    pdf_path = Path(sys.argv[1]).expanduser().resolve()
    if not pdf_path.is_file():
        print(f"file not found: {pdf_path}", file=sys.stderr)
        return 2
    out_path = Path(sys.argv[2]).expanduser().resolve() if len(sys.argv) > 2 else pdf_path.with_suffix('.txt')
    reader = PdfReader(str(pdf_path))
    parts = []
    for page in reader.pages:
        try:
            parts.append(page.extract_text() or "")
        except Exception:
            parts.append("")
    out_path.write_text("\n\n".join(parts))
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
