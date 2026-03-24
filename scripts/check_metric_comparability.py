#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

METRIC_GROUPS = {
    'revenue': ['revenue', '營收', '收入'],
    'ebitda': ['ebitda'],
    'ebit': ['ebit'],
    'net_profit': ['net profit', 'profit attributable', '淨利', '純利'],
    'balance_sheet_point_in_time': ['net debt', 'gross debt', 'cash balance', 'equity', 'net debt-to-equity', 'gearing'],
}

PERIOD_MARKERS = {
    'FY': ['fy', 'full year', '全年'],
    'H1': ['1h', 'h1', 'interim', '上半年'],
    'Quarter': ['q1', 'q2', 'q3', 'q4', 'quarter', '季度'],
}


def classify_metric(label: str) -> List[str]:
    lower = label.lower()
    hits = []
    for group, keywords in METRIC_GROUPS.items():
        if any(k in lower for k in keywords):
            hits.append(group)
    return hits


def classify_period(label: str) -> List[str]:
    lower = label.lower()
    hits = []
    for group, keywords in PERIOD_MARKERS.items():
        if any(k in lower for k in keywords):
            hits.append(group)
    return hits


def analyze_items(items: List[Dict[str, str]]) -> List[Dict[str, object]]:
    metric_hits = {}
    period_hits = {}
    for item in items:
        label = item.get('label', '')
        metric_hits[label] = classify_metric(label)
        period_hits[label] = classify_period(label)

    all_metric_groups = sorted({g for groups in metric_hits.values() for g in groups})
    all_period_groups = sorted({g for groups in period_hits.values() for g in groups})

    issues: List[Dict[str, object]] = []
    if len(all_metric_groups) > 1:
        issues.append({
            'severity': 'high',
            'issue': 'Mixed metric groups in one comparison frame',
            'metric_groups': all_metric_groups,
            'details': metric_hits,
            'suggestion': 'Split by metric level or add an explicit non-comparability warning.'
        })
    if len(all_period_groups) > 1:
        issues.append({
            'severity': 'high',
            'issue': 'Mixed period types in one comparison frame',
            'period_groups': all_period_groups,
            'details': period_hits,
            'suggestion': 'Keep FY, H1, and quarter views separate unless the chart is clearly explanatory only.'
        })
    if not issues:
        issues.append({
            'severity': 'info',
            'issue': 'No obvious mixed-metric or mixed-period issue detected from labels alone',
            'details': {'metrics': metric_hits, 'periods': period_hits},
            'suggestion': 'Still review the underlying data definitions before delivery.'
        })
    return issues


def load_items(path: Path) -> List[Dict[str, str]]:
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, list):
        raise ValueError('input JSON must be a list of objects with a label field')
    normalized = []
    for item in data:
        if isinstance(item, str):
            normalized.append({'label': item})
        elif isinstance(item, dict):
            normalized.append({'label': str(item.get('label', ''))})
        else:
            normalized.append({'label': str(item)})
    return normalized


def main() -> int:
    parser = argparse.ArgumentParser(description='Check chart/table label comparability.')
    parser.add_argument('input_json', help='JSON list of labels or objects with label fields')
    parser.add_argument('-o', '--output', help='Optional output JSON path')
    args = parser.parse_args()

    path = Path(args.input_json).expanduser().resolve()
    if not path.is_file():
        print(f'file not found: {path}', file=sys.stderr)
        return 2

    issues = analyze_items(load_items(path))
    payload = json.dumps(issues, ensure_ascii=False, indent=2)
    if args.output:
        out = Path(args.output).expanduser().resolve()
        out.write_text(payload, encoding='utf-8')
        print(out)
    else:
        print(payload)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
