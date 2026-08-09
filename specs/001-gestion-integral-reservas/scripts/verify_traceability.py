#!/usr/bin/env python3
"""Verify traceability for the "Gestión de profesionales" (bundle BW, backend) feature.

Two independent checks, both against files in this feature directory:

1. Coverage: every AC-ID (FR-BW-ID) listed in tasks.md's "## Coverage Audit" table
   has at least one associated task.
2. Traceability: every task row in traceability.md has a non-empty commit SHA
   (only enforced with --require-sha, since the SHA column is legitimately
   empty until the FINAL task runs).

Usage:
    python3 verify_traceability.py                # run both checks, report only
    python3 verify_traceability.py --require-sha   # also fail if any SHA is empty
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

FEATURE_DIR = Path(__file__).resolve().parent.parent
TASKS_FILE = FEATURE_DIR / "tasks.md"
TRACEABILITY_FILE = FEATURE_DIR / "traceability.md"

AC_ID_RE = re.compile(r"FR-BW-\d{3}")
TASK_ID_RE = re.compile(r"T\d{3}")
SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")


def parse_coverage_audit(tasks_text: str) -> dict[str, list[str]]:
    """Extract the Coverage Audit table: AC-ID -> [task IDs]."""
    marker = "## Coverage Audit"
    if marker not in tasks_text:
        raise ValueError(f"tasks.md has no '{marker}' section")
    section = tasks_text.split(marker, 1)[1]
    section = section.split("\n---", 1)[0]

    mapping: dict[str, list[str]] = {}
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|") or not AC_ID_RE.match(line.lstrip("| ")):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 3:
            continue
        ac_id = cols[0]
        if not AC_ID_RE.fullmatch(ac_id):
            continue
        task_ids = TASK_ID_RE.findall(cols[2])
        mapping[ac_id] = task_ids
    return mapping


def parse_traceability_rows(trace_text: str) -> dict[str, str]:
    """Extract Tnnn -> SHA from traceability.md's table rows."""
    shas: dict[str, str] = {}
    for line in trace_text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 4:
            continue
        task_id = cols[0]
        if not TASK_ID_RE.fullmatch(task_id):
            continue
        shas[task_id] = cols[3]
    return shas


def all_task_ids(tasks_text: str) -> list[str]:
    """Every Tnnn that appears as a checklist item ID in tasks.md, in order."""
    ids: list[str] = []
    for line in tasks_text.splitlines():
        m = re.match(r"^- \[[ xX]\] (T\d{3})\b", line)
        if m and m.group(1) not in ids:
            ids.append(m.group(1))
    return ids


def check_coverage(tasks_text: str) -> tuple[bool, list[str]]:
    coverage = parse_coverage_audit(tasks_text)
    problems = []
    for ac_id, task_ids in coverage.items():
        if not task_ids:
            problems.append(f"AC-ID {ac_id} has zero associated tasks (orphan)")
    ok = not problems
    print(f"[coverage] {len(coverage)} AC-ID(s) checked: "
          f"{'PASS' if ok else 'FAIL'}")
    for ac_id, task_ids in coverage.items():
        print(f"  {ac_id}: {', '.join(task_ids) if task_ids else '(none)'}")
    return ok, problems


def check_traceability(tasks_text: str, require_sha: bool) -> tuple[bool, list[str]]:
    if not TRACEABILITY_FILE.exists():
        msg = f"{TRACEABILITY_FILE} does not exist"
        print(f"[traceability] FAIL: {msg}")
        return False, [msg]

    trace_text = TRACEABILITY_FILE.read_text(encoding="utf-8")
    shas = parse_traceability_rows(trace_text)
    expected_ids = all_task_ids(tasks_text)

    problems = []
    for task_id in expected_ids:
        if task_id not in shas:
            problems.append(f"{task_id} has no row in traceability.md")
            continue
        sha = shas[task_id]
        if require_sha and (not sha or not SHA_RE.match(sha)):
            problems.append(f"{task_id} has no valid commit SHA recorded (got: {sha!r})")

    ok = not problems
    filled = sum(1 for t in expected_ids if SHA_RE.match(shas.get(t, "")))
    print(f"[traceability] {len(expected_ids)} task(s) expected, "
          f"{filled} with a recorded SHA: {'PASS' if ok else 'FAIL' if require_sha else 'INCOMPLETE (not required yet)'}")
    return ok, problems


def main() -> int:
    require_sha = "--require-sha" in sys.argv

    if not TASKS_FILE.exists():
        print(f"ERROR: {TASKS_FILE} does not exist", file=sys.stderr)
        return 1
    tasks_text = TASKS_FILE.read_text(encoding="utf-8")

    coverage_ok, coverage_problems = check_coverage(tasks_text)
    traceability_ok, traceability_problems = check_traceability(tasks_text, require_sha)

    problems = coverage_problems + (traceability_problems if require_sha else [])
    if problems:
        print("\nProblems found:")
        for p in problems:
            print(f"  - {p}")
        return 1

    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
