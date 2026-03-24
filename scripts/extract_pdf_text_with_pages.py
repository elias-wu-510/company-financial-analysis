#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Dict

from pypdf import PdfReader


def normalize_text(text: str) -> str:
    text = text.replace('\u00a0', ' ')
    text = re.sub(r'\r\n?', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_pages(pdf_path: Path) -> List[Dict[str, str]]:
    reader = PdfReader(str(pdf_path))
    pages = []
    for idx, page in enumerate(reader.pages, start=1):
        try:
            raw = page.extract_text() or ''
        except Exception:
            raw = ''
        pages.append({"page": idx, "text": normalize_text(raw)})
    return pages


def write_text_output(pages: List[Dict[str, str]], out_path: Path) -> None:
    chunks = []
    for item in pages:
        chunks.append(f"=== PAGE {item['page']} ===\n{item['text']}\n")
    out_path.write_text('\n'.join(chunks).strip() + '\n', encoding='utf-8')


def write_json_output(pages: List[Dict[str, str]], out_path: Path) -> None:
    out_path.write_text(json.dumps(pages, ensure_ascii=False, indent=2), encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser(description='Extract PDF text with stable page markers.')
    parser.add_argument('pdf_path', help='Input PDF path')
    parser.add_argument('output', nargs='?', help='Optional output path')
    parser.add_argument('--json', action='store_true', help='Write JSON instead of plain text')
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path).expanduser().resolve()
    if not pdf_path.is_file():
        print(f'file not found: {pdf_path}', file=sys.stderr)
        return 2

    if args.output:
        out_path = Path(args.output).expanduser().resolve()
    else:
        out_path = pdf_path.with_suffix('.pages.json' if args.json else '.pages.txt')

    pages = extract_pages(pdf_path)
    if args.json:
        write_json_output(pages, out_path)
    else:
        write_text_output(pages, out_path)

    print(out_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
