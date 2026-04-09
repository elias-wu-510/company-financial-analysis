#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import List, Dict, Any

TEXT_RE = re.compile(r'<text[^>]*x="([^"]+)"[^>]*y="([^"]+)"[^>]*>(.*?)</text>', re.S)
RECT_RE = re.compile(r'<rect[^>]*x="([^"]+)"[^>]*y="([^"]+)"[^>]*width="([^"]+)"[^>]*height="([^"]+)"[^>]*fill="([^"]+)"[^>]*/?>', re.S)
NUM_RE = re.compile(r'(-?\d+(?:\.\d+)?)%')
TAG_RE = re.compile(r'<[^>]+>')


def strip_tags(text: str) -> str:
    return TAG_RE.sub('', text).strip()


def f(v: str) -> float:
    return float(v)


def extract_svg_blocks(html: str) -> List[str]:
    blocks = []
    start = 0
    while True:
        i = html.find('<svg', start)
        if i == -1:
            break
        j = html.find('</svg>', i)
        if j == -1:
            break
        blocks.append(html[i:j+6])
        start = j + 6
    return blocks


def parse_texts(svg: str) -> List[Dict[str, Any]]:
    out = []
    for x, y, t in TEXT_RE.findall(svg):
        out.append({'x': f(x), 'y': f(y), 'text': strip_tags(t)})
    return out


def parse_rects(svg: str) -> List[Dict[str, Any]]:
    out = []
    for x, y, w, h, fill in RECT_RE.findall(svg):
        out.append({'x': f(x), 'y': f(y), 'width': f(w), 'height': f(h), 'fill': fill})
    return out


def find_value_texts(texts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    vals = []
    for t in texts:
        m = NUM_RE.fullmatch(t['text'])
        if m:
            vals.append({**t, 'value': float(m.group(1))})
    return vals


def nearest_rect(value_text: Dict[str, Any], rects: List[Dict[str, Any]]) -> Dict[str, Any] | None:
    candidates = []
    tx, ty = value_text['x'], value_text['y']
    for r in rects:
        if abs((r['x'] + r['width']/2) - tx) <= 28:
            # text is typically above the bar
            vertical_gap = abs(r['y'] - ty)
            candidates.append((vertical_gap, r))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    return candidates[0][1]


def scan_svg(svg: str, idx: int) -> Dict[str, Any]:
    texts = parse_texts(svg)
    rects = [r for r in parse_rects(svg) if r['width'] >= 20 and r['height'] >= 2]
    value_texts = find_value_texts(texts)
    pairs = []
    for vt in value_texts:
        nr = nearest_rect(vt, rects)
        if nr:
            pairs.append({'label': vt['text'], 'value': vt['value'], 'rect_height': nr['height'], 'rect_y': nr['y'], 'x': nr['x']})

    warnings = []
    # compare all pairs: higher value should have >= height when same chart implies bar comparison
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            a, b = pairs[i], pairs[j]
            if math.isclose(a['value'], b['value'], rel_tol=1e-6):
                continue
            if a['value'] > b['value'] and a['rect_height'] + 0.5 < b['rect_height']:
                warnings.append({
                    'severity': 'high',
                    'issue': 'Higher numeric value rendered with shorter bar',
                    'a': a,
                    'b': b,
                })
            if b['value'] > a['value'] and b['rect_height'] + 0.5 < a['rect_height']:
                warnings.append({
                    'severity': 'high',
                    'issue': 'Higher numeric value rendered with shorter bar',
                    'a': b,
                    'b': a,
                })

    return {
        'svg_index': idx,
        'value_bar_pairs': pairs,
        'warnings': warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description='Simple chart sanity scan for HTML/SVG bar charts.')
    parser.add_argument('html_file', help='HTML file containing SVG charts')
    parser.add_argument('-o', '--output', help='Optional output JSON path')
    args = parser.parse_args()

    path = Path(args.html_file).expanduser().resolve()
    if not path.is_file():
        print(f'file not found: {path}', file=sys.stderr)
        return 2

    html = path.read_text(encoding='utf-8', errors='ignore')
    svgs = extract_svg_blocks(html)
    results = [scan_svg(svg, i+1) for i, svg in enumerate(svgs)]
    payload = {'file': str(path), 'charts': results}
    data = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.output:
        out = Path(args.output).expanduser().resolve()
        out.write_text(data, encoding='utf-8')
        print(out)
    else:
        print(data)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
