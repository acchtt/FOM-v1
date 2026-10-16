#!/usr/bin/env python3
"""Validate FOM Football C consistency receipts. Standard library only."""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys

SCHEMA = pathlib.Path(__file__).resolve().parents[1] / "schemas" / "fom-receipt-v1.schema.json"

STAGE_AUTHORITY_PATHS = {
    "intake": "models/football/stages_v4/SWEEP.md",
    "rank": "models/football/stages_v4/RANK.md",
    "reconciliation": "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
    "audit": "models/football/prompts/04_WORK_POST_SLATE_AUDIT.md",
}
DECISION_AUTHORITY_PATHS = {
    "prematch": "models/football/prompts/02_NORMAL_CHAT_XI_ODDS.md",
    "live": "models/football/prompts/03_NORMAL_CHAT_LIVE.md",
}


def check(value, rule, path="$"):
    errors = []
    kind = rule.get("type")
    types = {
        "object": lambda v: isinstance(v, dict),
        "array": lambda v: isinstance(v, list),
        "string": lambda v: isinstance(v, str),
        "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
        "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
        "boolean": lambda v: isinstance(v, bool),
    }
    if kind and not types[kind](value):
        return [f"{path}: expected {kind}"]
    if "const" in rule and value != rule["const"]:
        errors.append(f"{path}: expected {rule['const']!r}")
    if "enum" in rule and value not in rule["enum"]:
        errors.append(f"{path}: invalid value {value!r}")
    if kind == "string":
        if len(value) < rule.get("minLength", 0):
            errors.append(f"{path}: empty/short string")
        if "pattern" in rule and not re.search(rule["pattern"], value):
            errors.append(f"{path}: pattern mismatch")
        if rule.get("format") == "date-time":
            try:
                parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
                if parsed.tzinfo is None or parsed.utcoffset() is None:
                    raise ValueError("timezone required")
            except ValueError:
                errors.append(f"{path}: invalid offset-aware ISO timestamp")
    if kind in ("integer", "number") and "minimum" in rule and value < rule["minimum"]:
        errors.append(f"{path}: below minimum")
    if kind == "array":
        for i, item in enumerate(value):
            errors.extend(check(item, rule.get("items", {}), f"{path}[{i}]"))
    if kind == "object" or (
        kind is None and isinstance(value, dict)
        and ("required" in rule or "properties" in rule)
    ):
        for field in rule.get("required", []):
            if field not in value:
                errors.append(f"{path}.{field}: missing")
        for field, item in value.items():
            if field in rule.get("properties", {}):
                errors.extend(check(item, rule["properties"][field], f"{path}.{field}"))
            elif rule.get("additionalProperties") is False:
                errors.append(f"{path}.{field}: unexpected field")
        for key, deps in rule.get("dependentRequired", {}).items():
            if key in value:
                for dep in deps:
                    if dep not in value:
                        errors.append(f"{path}.{dep}: required by {key}")
    for condition in rule.get("allOf", []):
        branch = (
            condition.get("then")
            if matches(value, condition.get("if", {}))
            else condition.get("else")
        )
        if branch:
            errors.extend(check(value, branch, path))
    return errors


def matches(value, rule):
    """Minimal structural evaluation for the schema's if/then guards."""
    if not isinstance(value, dict):
        return False
    if any(k not in value for k in rule.get("required", [])):
        return False
    for key, sub in rule.get("properties", {}).items():
        if key in value:
            if "const" in sub and value[key] != sub["const"]:
                return False
            if "properties" in sub and not matches(value[key], sub):
                return False
    return True


def _expected_authority_path(receipt):
    stage = receipt.get("stage")
    if stage == "decision":
        context = receipt.get("context", {})
        if isinstance(context, dict):
            return DECISION_AUTHORITY_PATHS.get(context.get("phase"))
        return None
    return STAGE_AUTHORITY_PATHS.get(stage)


def _unique(values):
    return isinstance(values, list) and len(values) == len(set(values))


def validate(receipt, schema):
    if not isinstance(receipt, dict):
        return ["$: receipt must be a JSON object"]

    versions = {
        v["properties"]["schema_version"]["const"]: v
        for v in schema["oneOf"]
    }
    rule = versions.get(receipt.get("schema_version"))
    if not rule:
        return ["$.schema_version: unknown FOM Football C receipt version"]

    errors = check(receipt, rule)

    authority = receipt.get("football_c_authority")
    if isinstance(authority, dict):
        expected_path = _expected_authority_path(receipt)
        if expected_path and authority.get("stage_authority_path") != expected_path:
            errors.append(
                "$.football_c_authority.stage_authority_path: "
                f"expected {expected_path!r} for this stage"
            )

    version = receipt.get("schema_version")

    if version == "fom-c-intake-v1":
        window = receipt.get("requested_window", {})
        if isinstance(window, dict):
            try:
                start = dt.datetime.fromisoformat(window["start"].replace("Z", "+00:00"))
                end = dt.datetime.fromisoformat(window["end"].replace("Z", "+00:00"))
                if start >= end:
                    errors.append("$.requested_window: start must precede end")
            except (KeyError, ValueError, TypeError):
                pass

        buckets = [
            receipt.get("eligible_match_ids", []),
            receipt.get("pending_match_ids", []),
            receipt.get("excluded_match_ids", []),
        ]
        if all(isinstance(x, list) for x in buckets):
            flattened = [item for bucket in buckets for item in bucket]
            if len(flattened) != len(set(flattened)):
                errors.append(
                    "$: intake match IDs must not appear in more than one bucket"
                )

    if version == "fom-c-rank-v1":
        assessed = receipt.get("assessed", [])
        if isinstance(assessed, list):
            rows = [
                r for r in assessed
                if isinstance(r, dict)
                and "match_id" in r
                and "c_board_state" in r
            ]
            ids = [r["match_id"] for r in rows]
            if len(ids) != len(set(ids)):
                errors.append("$.assessed: duplicate match_id")

            expected_focus = {
                r["match_id"] for r in rows if r["c_board_state"] == "FOCUS"
            }
            actual = receipt.get("official_board", [])
            if isinstance(actual, list):
                if not _unique(actual) or set(actual) != expected_focus:
                    errors.append(
                        "$.official_board: must contain exactly all C-FOCUS assessed IDs"
                    )

    if version == "fom-c-reconciliation-v1":
        if (
            receipt.get("primary_issue_class") == "C_MODEL_MISS"
            and receipt.get("rule_application_consistent") is not True
        ):
            errors.append(
                "$.rule_application_consistent: C_MODEL_MISS requires consistent "
                "application of the pinned Football C rules"
            )
        if receipt.get("prospective_evidence_only") is not True:
            errors.append(
                "$.prospective_evidence_only: reconciliation must be prospective"
            )

    return errors


def validate_bundle(receipts):
    """Cross-receipt invariants for receipts supplied together."""
    errors = []
    by_run_id = {
        r.get("run_id"): r
        for r in receipts
        if isinstance(r, dict) and isinstance(r.get("run_id"), str)
    }
    by_workflow = {}
    for receipt in receipts:
        if not isinstance(receipt, dict):
            continue
        workflow_id = receipt.get("workflow_id")
        if isinstance(workflow_id, str):
            by_workflow.setdefault(workflow_id, []).append(receipt)

    for workflow_id, group in by_workflow.items():
        shas = {
            r.get("football_c_authority", {}).get("commit_sha")
            for r in group
            if isinstance(r.get("football_c_authority"), dict)
        }
        shas.discard(None)
        if len(shas) > 1:
            errors.append(
                f"{workflow_id}: mixed Football C authority SHAs are forbidden"
            )

    ref_fields = {
        "fom-c-rank-v1": "intake_receipt_ref",
        "fom-c-decision-v1": "rank_receipt_ref",
        "fom-c-reconciliation-v1": "frozen_receipt_ref",
    }
    for receipt in receipts:
        if not isinstance(receipt, dict):
            continue
        ref_field = ref_fields.get(receipt.get("schema_version"))
        if not ref_field:
            continue
        ref = receipt.get(ref_field)
        upstream = by_run_id.get(ref)
        if not upstream:
            continue
        if upstream.get("workflow_id") != receipt.get("workflow_id"):
            errors.append(
                f"{receipt.get('run_id')}: {ref_field} crosses workflow_id"
            )
        upstream_sha = upstream.get("football_c_authority", {}).get("commit_sha")
        current_sha = receipt.get("football_c_authority", {}).get("commit_sha")
        if upstream_sha and current_sha and upstream_sha != current_sha:
            errors.append(
                f"{receipt.get('run_id')}: {ref_field} uses different C authority"
            )

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipts", nargs="+", type=pathlib.Path)
    args = parser.parse_args()

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    failed = False
    loaded = []

    for path in args.receipts:
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
            loaded.append(obj)
            errors = validate(obj, schema)
        except (OSError, ValueError) as exc:
            errors = [f"cannot read JSON: {exc}"]

        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path}")

    bundle_errors = validate_bundle(loaded)
    if bundle_errors:
        failed = True
        print("FAIL BUNDLE")
        for error in bundle_errors:
            print(f"  - {error}")

    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
