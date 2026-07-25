from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.envelope_validator import load_envelope, validate_envelope  # noqa: E402


class ValidatorTests(unittest.TestCase):
    def valid(self) -> dict:
        return load_envelope(str(ROOT / "tests" / "fixtures" / "valid_envelope.json"))

    def assert_has_error(self, errors: list[str], field: str) -> None:
        self.assertTrue(
            any(error.startswith(f"{field}:") for error in errors),
            f"Expected an error for {field!r}, got: {errors}",
        )

    def test_valid_fixture_passes(self) -> None:
        self.assertEqual(validate_envelope(self.valid()), [])

    def test_required_fields(self) -> None:
        envelope = self.valid()
        del envelope["owner"]
        self.assert_has_error(validate_envelope(envelope), "owner")

    def test_task_id_type_and_format(self) -> None:
        envelope = self.valid()
        envelope["task_id"] = 123
        self.assert_has_error(validate_envelope(envelope), "task_id")

        envelope["task_id"] = "Bad ID"
        self.assert_has_error(validate_envelope(envelope), "task_id")

    def test_owner_and_objective_rules(self) -> None:
        envelope = self.valid()
        envelope["owner"] = "   "
        envelope["objective"] = "too short"
        errors = validate_envelope(envelope)
        self.assert_has_error(errors, "owner")
        self.assert_has_error(errors, "objective")

    def test_list_fields(self) -> None:
        envelope = self.valid()
        envelope["inputs"] = "data/file.txt"
        envelope["actions"] = []
        envelope["artifacts"] = ["output/result.md", 42]
        errors = validate_envelope(envelope)
        self.assert_has_error(errors, "inputs")
        self.assert_has_error(errors, "actions")
        self.assert_has_error(errors, "artifacts")

    def test_status_and_boolean_type(self) -> None:
        envelope = self.valid()
        envelope["status"] = "done"
        envelope["requires_human_approval"] = "false"
        errors = validate_envelope(envelope)
        self.assert_has_error(errors, "status")
        self.assert_has_error(errors, "requires_human_approval")

    def test_risky_actions_require_approval(self) -> None:
        envelope = self.valid()
        envelope["actions"] = ["read_text", "send_email"]
        envelope["requires_human_approval"] = False
        self.assert_has_error(validate_envelope(envelope), "requires_human_approval")

        envelope["requires_human_approval"] = True
        self.assertEqual(validate_envelope(envelope), [])

    def test_artifact_path_security(self) -> None:
        bad_paths = [
            "../secret.md",
            "/tmp/output.md",
            "reports/result.md",
            "output/result.exe",
            "output/a/../../secret.json",
        ]
        for bad_path in bad_paths:
            with self.subTest(path=bad_path):
                envelope = self.valid()
                envelope["artifacts"] = [bad_path]
                self.assert_has_error(validate_envelope(envelope), "artifacts")

    def test_candidate_envelope_is_repaired(self) -> None:
        candidate = load_envelope(str(ROOT / "candidate" / "task_envelope.json"))
        self.assertEqual(validate_envelope(candidate), [])
        self.assertIn("classify_feedback", candidate["actions"])
        self.assertFalse(candidate["requires_human_approval"])
        self.assertTrue(all(path.startswith("output/") for path in candidate["artifacts"]))

    def test_cli_exit_codes(self) -> None:
        valid_path = ROOT / "tests" / "fixtures" / "valid_envelope.json"
        result = subprocess.run(
            [sys.executable, str(ROOT / "src" / "envelope_validator.py"), str(valid_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("VALID", result.stdout)


if __name__ == "__main__":
    unittest.main()
