"""Task envelope validator.

This file intentionally contains missing and incorrect logic.
Complete it according to docs/01_CONTRACT.md.
Only Python's standard library is required.
"""

from __future__ import annotations

import json
import re
from pathlib import PurePosixPath
from typing import Any

REQUIRED_FIELDS = {
    "task_id",
    "owner",
    "objective",
    "inputs",
    "actions",
    "artifacts",
    "status",
    "requires_human_approval",
}

ALLOWED_STATUSES = {"planned", "in_progress", "blocked"}
HUMAN_APPROVAL_ACTIONS = {
    "send_email",
    "delete_file",
    "publish_content",
    "modify_customer_record",
    "execute_payment",
}
ALLOWED_ARTIFACT_EXTENSIONS = {".json", ".md", ".csv"}
TASK_ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load_envelope(path: str) -> dict[str, Any]:
    """Load a JSON envelope from disk."""
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("envelope: top-level JSON value must be an object")
    return data


def validate_required_fields(envelope: dict[str, Any]) -> list[str]:
    """Return errors for missing required fields."""
    # TODO: implement according to the contract.
    return []


def validate_scalar_fields(envelope: dict[str, Any]) -> list[str]:
    """Validate task_id, owner, objective, status and approval flag."""
    errors: list[str] = []

    # Intentionally incomplete: only one field is partially checked.
    task_id = envelope.get("task_id")
    if isinstance(task_id, str) and not task_id:
        errors.append("task_id: must not be empty")

    # TODO: validate all scalar fields according to the contract.
    return errors


def validate_list_fields(envelope: dict[str, Any]) -> list[str]:
    """Validate inputs, actions and artifacts as non-empty string lists."""
    # TODO: implement according to the contract.
    return []


def validate_risk_policy(envelope: dict[str, Any]) -> list[str]:
    """Require human approval for risky actions."""
    errors: list[str] = []
    actions = envelope.get("actions", [])

    # BUG: This condition is reversed and does not handle wrong action types.
    if isinstance(actions, list) and set(actions) & HUMAN_APPROVAL_ACTIONS:
        if envelope.get("requires_human_approval") is True:
            errors.append(
                "requires_human_approval: must be false for actions in this task"
            )

    return errors


def validate_artifact_paths(envelope: dict[str, Any]) -> list[str]:
    """Validate safe output artifact paths."""
    # TODO: implement using PurePosixPath if useful.
    _ = PurePosixPath
    return []


def validate_envelope(envelope: dict[str, Any]) -> list[str]:
    """Return every validation error without stopping at the first one."""
    errors: list[str] = []
    errors.extend(validate_required_fields(envelope))
    errors.extend(validate_scalar_fields(envelope))
    errors.extend(validate_list_fields(envelope))
    errors.extend(validate_risk_policy(envelope))
    errors.extend(validate_artifact_paths(envelope))
    return errors


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate a task envelope JSON file")
    parser.add_argument("path", help="Path to the JSON envelope")
    args = parser.parse_args()

    try:
        envelope = load_envelope(args.path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"INVALID\n- {exc}")
        return 2

    errors = validate_envelope(envelope)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
