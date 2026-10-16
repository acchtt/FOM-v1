#!/usr/bin/env python3
"""Validate FOM v1 receipts. Python standard library only; no network/API."""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys

SCHEMA = pathlib.Path(__file__).resolve().parents[1] / "schemas" / "fom-receipt-v1.schema.json"


def check(value, rule, path="$"):
    errors = []
    kind = rule.get("type")
    types = {"object": lambda v: isinstance(v, dict),
             "array": lambda v: isinstance(v, list),
             "string": lambda v: isinstance(v, str),
             "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
             "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
             "boolean": lambda v: isinstance(v, bool)}
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
    if kind == "object":
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
        branch = condition.get("then") if matches(value, condition.get("if", {})) else condition.get("else")
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


def validate(receipt, schema):
    errors = []
    if not isinstance(receipt, dict):
        return ["$: receipt must be a JSON object"]
    versions = {v["properties"]["schema_version"]["const"]: v for v in schema["oneOf"]}
    rule = versions.get(receipt.get("schema_version"))
    if not rule:
        return ["$.schema_version: unknown FOM receipt version"]
    errors.extend(check(receipt, rule))
    if receipt.get("schema_version") == "fom-rank-v1":
        assessed = receipt.get("assessed", [])
        if isinstance(assessed, list):
            rows = [r for r in assessed if isinstance(r, dict) and "match_id" in r and "state" in r]
            ids = [r["match_id"] for r in rows]
            if len(ids) != len(set(ids)):
                errors.append("$.assessed: duplicate match_id")
            partitions = {"FOM_FOCUS": "focus_board", "FOM_WATCH": "watch", "FOM_DROP": "drop"}
            for state, field in partitions.items():
                actual = receipt.get(field, [])
                expected = {r["match_id"] for r in rows if r["state"] == state}
                if isinstance(actual, list) and (len(actual) != len(set(actual)) or set(actual) != expected):
                    errors.append(f"$.{field}: must contain exactly the matching assessed IDs")
    if receipt.get("schema_version") == "fom-sweep-v1":
        window = receipt.get("requested_window", {})
        if isinstance(window, dict):
            try:
                start = dt.datetime.fromisoformat(window["start"].replace("Z", "+00:00"))
                end = dt.datetime.fromisoformat(window["end"].replace("Z", "+00:00"))
                if start >= end:
                    errors.append("$.requested_window: start must precede end")
            except (KeyError, ValueError, TypeError):
                pass  # Base schema already reports invalid timestamps.
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipts", nargs="+", type=pathlib.Path)
    args = parser.parse_args()
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    failed = False
    for path in args.receipts:
        try:
            obj = json.loads(path.read_text(encoding="utf-8"))
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
    return int(failed)


if __name__ == "__main__":
    sys.exit(main())
