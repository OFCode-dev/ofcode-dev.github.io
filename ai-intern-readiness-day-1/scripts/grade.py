from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_MARKERS = ("[DOLDUR]", "[BURAYA", "[YAZ]")


def check_submission_files() -> list[str]:
    errors: list[str] = []
    required = [
        ROOT / "submission" / "FINDINGS.md",
        ROOT / "submission" / "AI_USAGE.md",
        ROOT / "submission" / "LEARNING_NOTE.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing submission file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in PLACEHOLDER_MARKERS):
            errors.append(f"unfilled placeholder: {path.relative_to(ROOT)}")
        if len(text.strip()) < 180:
            errors.append(f"submission file is too short: {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    print("=== 1/2 Automated tests ===")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        check=False,
    )

    print("\n=== 2/2 Submission completeness ===")
    submission_errors = check_submission_files()
    if submission_errors:
        for error in submission_errors:
            print(f"FAIL: {error}")
    else:
        print("PASS: submission documents are complete")

    passed = result.returncode == 0 and not submission_errors
    print(f"\nFINAL RESULT: {'PASS' if passed else 'FAIL'}")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
