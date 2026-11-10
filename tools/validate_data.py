#!/usr/bin/env python3
"""Validate Check Desk CSV data files against data/schema/*.json.

Stdlib only. Comment lines (starting with #) in CSVs are ignored.
Empty values become null for optional schema fields; required fields must be present.

Usage (from repo root):
  python3 tools/validate_data.py
  python3 tools/validate_data.py data/providers/fees.csv data/locations/denver.csv
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "data" / "schema"

URI_LIKE = re.compile(r"^https?://[^\s]+$", re.I)
DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


def load_schema(name: str) -> dict:
    path = SCHEMA_DIR / name
    return json.loads(path.read_text(encoding="utf-8"))


def detect_schema(path: Path) -> str:
    name = path.name.lower()
    parts = [p.lower() for p in path.parts]
    if "fee" in name or "providers" in parts:
        return "fees.schema.json"
    if "location" in name or "locations" in parts:
        return "locations.schema.json"
    raise SystemExit(f"Cannot infer schema for {path}")


def empty_to_none(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    return value if value != "" else None


def coerce(value: str | None, prop: dict):
    types = prop.get("type", "string")
    if not isinstance(types, list):
        types = [types]
    value = empty_to_none(value)
    if value is None:
        if "null" in types:
            return None
        # missing / empty will fail required or type checks later
        return None
    if "boolean" in types and value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if "number" in types:
        try:
            return float(value) if ("." in value or "e" in value.lower()) else float(int(value))
        except ValueError:
            return value  # leave as string; type check will fail
    return value


def type_ok(value, types) -> bool:
    if not isinstance(types, list):
        types = [types]
    for t in types:
        if t == "null" and value is None:
            return True
        if t == "string" and isinstance(value, str):
            return True
        if t == "boolean" and isinstance(value, bool):
            return True
        if t == "number" and isinstance(value, (int, float)) and not isinstance(value, bool):
            return True
        if t == "integer" and isinstance(value, int) and not isinstance(value, bool):
            return True
        if t == "object" and isinstance(value, dict):
            return True
        if t == "array" and isinstance(value, list):
            return True
    return False


def validate_instance(obj: dict, schema: dict, rownum: int) -> list[str]:
    errors: list[str] = []
    prefix = f"row {rownum} ({obj.get('id') or '?'})"
    props = schema.get("properties", {})
    required = schema.get("required", [])
    additional = schema.get("additionalProperties", True)

    for key in required:
        if key not in obj or obj[key] is None or obj[key] == "":
            errors.append(f"{prefix}: missing required field '{key}'")

    if additional is False:
        for key in obj:
            if key not in props:
                errors.append(f"{prefix}: unexpected field '{key}'")

    for key, value in obj.items():
        if key not in props:
            continue
        prop = props[key]
        types = prop.get("type", "string")
        if not type_ok(value, types):
            errors.append(f"{prefix}: field '{key}' has type {type(value).__name__}, expected {types}")
            continue
        if value is None:
            enum = prop.get("enum")
            if enum is not None and None not in enum and value not in enum:
                errors.append(f"{prefix}: field '{key}' value {value!r} not in enum")
            continue
        if "enum" in prop and value not in prop["enum"]:
            errors.append(f"{prefix}: field '{key}' value {value!r} not in enum {prop['enum']}")
        if "const" in prop and value != prop["const"]:
            errors.append(f"{prefix}: field '{key}' value {value!r} != const {prop['const']!r}")
        if isinstance(value, str):
            if "minLength" in prop and len(value) < prop["minLength"]:
                errors.append(f"{prefix}: field '{key}' shorter than minLength {prop['minLength']}")
            if "pattern" in prop and re.search(prop["pattern"], value) is None:
                errors.append(f"{prefix}: field '{key}' value {value!r} does not match pattern {prop['pattern']}")
            if prop.get("format") == "uri":
                if not URI_LIKE.match(value):
                    errors.append(f"{prefix}: field '{key}' is not an http(s) URI: {value!r}")
                else:
                    parsed = urlparse(value)
                    if not parsed.netloc:
                        errors.append(f"{prefix}: field '{key}' URI missing host: {value!r}")
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            if "minimum" in prop and value < prop["minimum"]:
                errors.append(f"{prefix}: field '{key}' {value} below minimum {prop['minimum']}")
            if "maximum" in prop and value > prop["maximum"]:
                errors.append(f"{prefix}: field '{key}' {value} above maximum {prop['maximum']}")
    return errors


def read_csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    text = path.read_text(encoding="utf-8")
    lines = [ln for ln in text.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]
    reader = csv.DictReader(lines)
    if not reader.fieldnames:
        return [], []
    rows = []
    for raw in reader:
        rows.append({k: (v if v is not None else "") for k, v in raw.items() if k is not None})
    return list(reader.fieldnames), rows


def validate_file(path: Path) -> tuple[int, list[str]]:
    schema_name = detect_schema(path)
    schema = load_schema(schema_name)
    fieldnames, rows = read_csv_rows(path)
    errors: list[str] = []
    if not fieldnames:
        errors.append(f"{path}: no header row")
        return 0, errors
    props = schema.get("properties", {})
    objects = []
    for i, raw in enumerate(rows, start=2):  # header is line-ish; report 1-based data index + header
        obj = {}
        for key in fieldnames:
            if key not in props:
                obj[key] = empty_to_none(raw.get(key, ""))
                continue
            obj[key] = coerce(raw.get(key, ""), props[key])
        objects.append(obj)
        errors.extend(validate_instance(obj, schema, i))
    return len(objects), errors


def default_paths() -> list[Path]:
    found = []
    for p in [
        ROOT / "data" / "providers" / "fees.csv",
        ROOT / "data" / "locations" / "denver.csv",
    ]:
        if p.exists():
            found.append(p)
    return found


def main(argv: list[str]) -> int:
    paths = [Path(a) for a in argv] if argv else default_paths()
    if not paths:
        print("No CSV files to validate.", file=sys.stderr)
        return 2
    any_error = False
    for path in paths:
        if not path.exists():
            print(f"ERROR {path}: file not found")
            any_error = True
            continue
        count, errors = validate_file(path)
        rel = path if not path.is_absolute() else path
        try:
            rel = path.resolve().relative_to(ROOT)
        except Exception:
            rel = path
        print(f"{rel}: {count} data row(s)")
        for err in errors:
            print(f"  ERROR {err}")
            any_error = True
        if not errors:
            print("  OK")
    return 1 if any_error else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
