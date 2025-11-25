from __future__ import annotations
from typing import List, Dict, Any

from .models import RouteSnapshot


def snapshots_to_dicts(routes: List[RouteSnapshot]) -> List[Dict[str, Any]]:
    return [r.to_dict() for r in routes]


def format_table(routes: List[RouteSnapshot]) -> str:
    if not routes:
        return "(no routes)"

    dicts = [r.to_dict() for r in routes]
    columns = ["device", "channel", "tower_id", "latency_ms", "signal_quality", "g_layer", "frequency"]

    col_widths = {col: len(col) for col in columns}

    for row in dicts:
        for col in columns:
            col_widths[col] = max(col_widths[col], len(str(row[col])))

    def fmt_row(row_vals) -> str:
        return " ".join(
            str(row_vals[c]).ljust(col_widths[c])
            for c in columns
        )

    header = fmt_row({c: c for c in columns})
    sep = " ".join("-" * col_widths[c] for c in columns)
    lines = [header, sep]

    for row in dicts:
        lines.append(fmt_row(row))

    return "\n".join(lines)
