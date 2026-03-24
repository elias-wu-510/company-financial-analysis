#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

UNIT_RULES = [
    (re.compile(r'^百萬港元$', re.I), 'HK$ million'),
    (re.compile(r'^十億港元$', re.I), 'HK$ billion'),
    (re.compile(r'^港元$', re.I), 'HKD'),
    (re.compile(r'^hk\$\s?mn$', re.I), 'HK$ million'),
    (re.compile(r'^hk\$\s?million$', re.I), 'HK$ million'),
    (re.compile(r'^hk\$\s?bn$', re.I), 'HK$ billion'),
    (re.compile(r'^hk\$\s?billion$', re.I), 'HK$ billion'),
    (re.compile(r'^bn$', re.I), 'HK$ billion'),
    (re.compile(r'^mn$', re.I), 'HK$ million'),
]

PERIOD_RULES = [
    (re.compile(r'^2024\s*全年$'), 'FY2024'),
    (re.compile(r'^2025\s*全年$'), 'FY2025'),
    (re.compile(r'^2024\s*上半年$'), '1H2024'),
    (re.compile(r'^2025\s*上半年$'), '1H2025'),
    (re.compile(r'^fy\s*2024$', re.I), 'FY2024'),
    (re.compile(r'^fy\s*2025$', re.I), 'FY2025'),
    (re.compile(r'^(1h|h1)\s*2024$', re.I), '1H2024'),
    (re.compile(r'^(1h|h1)\s*2025$', re.I), '1H2025'),
]

LABEL_RULES = [
    (re.compile(r'^Revenue$', re.I), 'Revenue'),
    (re.compile(r'^營收$'), 'Revenue'),
    (re.compile(r'^收入$'), 'Revenue'),
    (re.compile(r'^EBITDA$', re.I), 'EBITDA'),
    (re.compile(r'^EBIT$', re.I), 'EBIT'),
    (re.compile(r'^Net debt to equity ratio$', re.I), 'Net debt-to-equity ratio'),
    (re.compile(r'^Net debt-to-equity ratio$', re.I), 'Net debt-to-equity ratio'),
    (re.compile(r'^淨負債權益比$'), 'Net debt-to-equity ratio'),
]


def normalize_value(value: str, rules: List[tuple[re.Pattern[str], str]]) -> str:
    text = value.strip()
    for pattern, replacement in rules:
        if pattern.match(text):
            return replacement
    return text


def normalize_item(item: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(item)
    if 'unit' in out and isinstance(out['unit'], str):
        out['unit'] = normalize_value(out['unit'], UNIT_RULES)
    if 'period' in out and isinstance(out['period'], str):
        out['period'] = normalize_value(out['period'], PERIOD_RULES)
    if 'label' in out and isinstance(out['label'], str):
        out['label'] = normalize_value(out['label'], LABEL_RULES)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description='Normalize units, period labels, and common chart labels.')
    parser.add_argument('input_json', help='JSON list of objects')
    parser.add_argument('-o', '--output', help='Optional output JSON path')
    args = parser.parse_args()

    path = Path(args.input_json).expanduser().resolve()
    if not path.is_file():
        print(f'file not found: {path}', file=sys.stderr)
        return 2

    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, list):
        print('input JSON must be a list of objects', file=sys.stderr)
        return 2

    output = [normalize_item(item if isinstance(item, dict) else {'value': item}) for item in data]
    payload = json.dumps(output, ensure_ascii=False, indent=2)
    if args.output:
        out = Path(args.output).expanduser().resolve()
        out.write_text(payload, encoding='utf-8')
        print(out)
    else:
        print(payload)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
