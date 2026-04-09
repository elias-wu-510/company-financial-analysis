#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

PERIOD_PATTERNS = [
    (re.compile(r'\bFY\s*20\d{2}\b', re.I), 'FY'),
    (re.compile(r'\b20\d{2}\s*(annual report|annual results|full year)\b', re.I), 'FY'),
    (re.compile(r'\b(1H|H1|first half|interim)\s*20\d{2}\b', re.I), 'H1'),
    (re.compile(r'\b20\d{2}\s*(interim report|interim results|half[- ]year)\b', re.I), 'H1'),
    (re.compile(r'\bQ[1-4]\s*20\d{2}\b', re.I), 'Quarter'),
]

YEAR_PATTERN = re.compile(r'\b20\d{2}\b')
DISCLOSURE_DATE_PATTERN = re.compile(r'\b(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})\b')
CURRENCY_PATTERNS = [
    (re.compile(r'HK\$|Hong Kong dollars?|港元', re.I), 'HKD'),
    (re.compile(r'US\$|USD|US dollars?', re.I), 'USD'),
    (re.compile(r'RMB|CNY|人民幣', re.I), 'CNY'),
]
UNIT_PATTERNS = [
    (re.compile(r'百萬港元|HK\$\s?million|HK\$\s?mn', re.I), 'HK$ million'),
    (re.compile(r'十億港元|HK\$\s?billion|HK\$\s?bn|\bbn\b', re.I), 'HK$ billion'),
    (re.compile(r'人民幣百萬元|RMB\s?million', re.I), 'RMB million'),
]


def detect_period_type(text: str) -> Optional[str]:
    for pattern, label in PERIOD_PATTERNS:
        if pattern.search(text):
            return label
    return None


def detect_covered_period(text: str, path_name: str) -> Optional[str]:
    years = YEAR_PATTERN.findall(path_name + ' ' + text)
    years = sorted(set(years))
    period_type = detect_period_type(text + ' ' + path_name)
    if period_type == 'FY' and years:
        return f'FY{years[0]}'
    if period_type == 'H1' and years:
        return f'1H{years[0]}'
    if period_type == 'Quarter' and years:
        q_match = re.search(r'\b(Q[1-4])\s*(20\d{2})\b', text + ' ' + path_name, re.I)
        if q_match:
            return f"{q_match.group(1).upper()}{q_match.group(2)}"
        return f'Quarter {years[0]}'
    if len(years) == 1:
        return years[0]
    if len(years) >= 2:
        return f'{years[0]}-{years[-1]}'
    return None


def detect_disclosure_date(text: str, path_name: str) -> Optional[str]:
    m = DISCLOSURE_DATE_PATTERN.search(text) or DISCLOSURE_DATE_PATTERN.search(path_name)
    if not m:
        return None
    yyyy, mm, dd = m.groups()
    return f'{yyyy}-{int(mm):02d}-{int(dd):02d}'


def detect_currency(text: str) -> Optional[str]:
    for pattern, label in CURRENCY_PATTERNS:
        if pattern.search(text):
            return label
    return None


def detect_unit(text: str) -> Optional[str]:
    for pattern, label in UNIT_PATTERNS:
        if pattern.search(text):
            return label
    return None


def scan_file(path: Path, max_chars: int = 20000) -> Dict[str, Optional[str]]:
    content = path.read_text(encoding='utf-8', errors='ignore')[:max_chars]
    return {
        'document': path.name,
        'disclosure_date': detect_disclosure_date(content, path.name),
        'covered_period': detect_covered_period(content, path.name),
        'period_type': detect_period_type(content + ' ' + path.name),
        'currency': detect_currency(content),
        'unit': detect_unit(content),
        'path': str(path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description='Build a source-period map from text or HTML files.')
    parser.add_argument('inputs', nargs='+', help='Input files to scan')
    parser.add_argument('-o', '--output', help='Optional output JSON path')
    args = parser.parse_args()

    items: List[Dict[str, Optional[str]]] = []
    for raw in args.inputs:
        path = Path(raw).expanduser().resolve()
        if not path.is_file():
            print(f'skip missing file: {path}', file=sys.stderr)
            continue
        items.append(scan_file(path))

    payload = json.dumps(items, ensure_ascii=False, indent=2)
    if args.output:
        out = Path(args.output).expanduser().resolve()
        out.write_text(payload, encoding='utf-8')
        print(out)
    else:
        print(payload)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
