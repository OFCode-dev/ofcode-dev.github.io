from __future__ import annotations

import json
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    print("AI Intern Readiness - Environment Check")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    print(f"Repository: {ROOT}")

    failures: list[str] = []
    if sys.version_info < (3, 10):
        failures.append("Python 3.10 or newer is required.")

    required = [
        "README.md",
        "TASK.md",
        "docs/01_CONTRACT.md",
        "src/envelope_validator.py",
        "candidate/task_envelope.json",
        "tests/test_validator.py",
    ]
    for relative in required:
        if not (ROOT / relative).exists():
            failures.append(f"Missing file: {relative}")

    try:
        with (ROOT / "candidate" / "task_envelope.json").open(encoding="utf-8") as handle:
            json.load(handle)
        print("Candidate JSON syntax: OK")
    except Exception as exc:
        failures.append(f"Candidate JSON syntax error: {exc}")

    if failures:
        print("\nEnvironment check: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nEnvironment check: PASS")
    print("Next: run the unit tests described in README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
