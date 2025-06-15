#!/usr/bin/env python3
import re
import sys
from datetime import datetime
from collections import defaultdict


def parse_schedule(lines):
    pattern = re.compile(r"^(\d{2}:\d{2})\s+(.+)$")
    fmt = "%H:%M"
    result = []
    for line in lines:
        raw = line.rstrip("\n")
        if not raw.strip():
            result.append(None)
            continue
        m = pattern.match(raw.strip())
        if not m:
            print("Warning: skipping unrecognized line:")
            continue
        t, label = m.groups()
        dt = datetime.strptime(t, fmt)
        result.append((dt, label))
    return result

def compute_report(parsed):
    timeline = []
    summary = defaultdict(int)
    # Extract only timestamped entries for duration calculations
    entries = [e for e in parsed if e is not None]

    for (idx, (t1, lbl1)) in enumerate(entries[:-1]):
        t2, _ = entries[idx + 1]
        if lbl1.lower().startswith("end"):
            continue
        dur = int((t2 - t1).total_seconds() / 60)
        summary[lbl1] += dur

    # Reconstruct timeline with blank lines intact
    it = iter(entries)
    next_idx = next(it, None)
    for item in parsed:
        if item is None:
            timeline.append("")  # blank line
        else:
            t, lbl = item
            if lbl.lower().startswith("end"):
                continue
            # Find corresponding next timestamp to show the range
            # Pop from entries list
            t2, _ = next_idx or (None, None)
            # Get next actual entry
            next_idx = next(it, None)
            # Format line
            timeline.append(f"{t.strftime('%H:%M')}-{next_idx[0].strftime('%H:%M')}  {lbl}")

    total = sum(summary.values()) or 1
    summary_lines = ["\n=== Summary ===",
                     f"Total time: {total} minutes\n"]
    for lbl, mins in sorted(summary.items(), key=lambda kv: kv[1], reverse=True):
        pct = mins * 100 / total
        summary_lines.append(f"{lbl}: {mins} min ({pct:.1f}%)")

    return timeline + summary_lines

def main():
    if len(sys.argv) < 2:
        print("Usage: python timelog.py <file>")
        sys.exit(1)

    fn = sys.argv[1]
    with open(fn, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    parsed = parse_schedule(lines)
    report = compute_report(parsed)
    out_fn = fn.rsplit(".", 1)[0] + "_report.txt"
    with open(out_fn, 'w', encoding='utf-8') as out:
        out.write("\n".join(report) + "\n")

if __name__ == "__main__":
    main()
