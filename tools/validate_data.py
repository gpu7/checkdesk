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


WEEKDAY_HOUR_FIELDS = (
    "hours_mon",
    "hours_tue",
    "hours_wed",
    "hours_thu",
    "hours_fri",
)
WEEKEND_HOUR_FIELDS = ("hours_sat", "hours_sun")
HOURS_RANGE = re.compile(r"^(\d{1,2}):(\d{2})-(\d{1,2}):(\d{2})$")
MINUTES_1700 = 17 * 60
BANK_START = 9 * 60
BANK_END = 17 * 60


def parse_hours_value(value):
    """Parse a per-day hours cell.

    Returns:
      None — unpublished / empty
      ("closed",)
      ("range", start_minutes, end_minutes) — end may be 24*60; overnight if end <= start
      ("unparseable",) — present but not machine-readable
    """
    if value is None:
        return None
    if not isinstance(value, str):
        return ("unparseable",)
    text = value.strip()
    if text == "":
        return None
    if text.lower() == "closed":
        return ("closed",)
    match = HOURS_RANGE.match(text)
    if not match:
        return ("unparseable",)
    h1, m1, h2, m2 = (int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)))
    if h1 > 23 or m1 > 59:
        return ("unparseable",)
    start = h1 * 60 + m1
    if h2 == 24 and m2 == 0:
        end = 24 * 60
    elif h2 <= 23 and m2 <= 59:
        end = h2 * 60 + m2
    else:
        return ("unparseable",)
    return ("range", start, end)


def is_open_range(parsed) -> bool:
    return parsed is not None and parsed[0] == "range"


def range_open_after_1700(parsed) -> bool:
    """True if a machine-readable window is open after 17:00."""
    if not is_open_range(parsed):
        return False
    start, end = parsed[1], parsed[2]
    if end > start:
        return end > MINUTES_1700
    # Overnight or 24-hour window includes time after 17:00.
    return True


def range_outside_bank_hours(parsed) -> bool:
    """True if a weekday window is not fully contained in 09:00-17:00."""
    if not is_open_range(parsed):
        return False
    start, end = parsed[1], parsed[2]
    if end <= start:
        return True
    return start < BANK_START or end > BANK_END


def expected_open_day(obj: dict, field: str):
    parsed = parse_hours_value(obj.get(field))
    if parsed is None:
        return None
    if parsed[0] == "unparseable":
        return "skip"
    return is_open_range(parsed)


def expected_open_weekends(obj: dict):
    parsed = [parse_hours_value(obj.get(key)) for key in WEEKEND_HOUR_FIELDS]
    if any(is_open_range(item) for item in parsed):
        return True
    if any(item is not None and item[0] == "unparseable" for item in parsed):
        return "skip"
    if not any(item is not None for item in parsed):
        return None
    return False


def expected_open_after_1700_weekday(obj: dict):
    parsed = [parse_hours_value(obj.get(key)) for key in WEEKDAY_HOUR_FIELDS]
    if any(range_open_after_1700(item) for item in parsed):
        return True
    if any(item is not None and item[0] == "unparseable" for item in parsed):
        return "skip"
    if not any(item is not None for item in parsed):
        return None
    return False


def expected_after_hours(obj: dict):
    weekdays = [parse_hours_value(obj.get(key)) for key in WEEKDAY_HOUR_FIELDS]
    weekends = [parse_hours_value(obj.get(key)) for key in WEEKEND_HOUR_FIELDS]
    if any(is_open_range(item) for item in weekends):
        return True
    if any(range_outside_bank_hours(item) for item in weekdays):
        return True
    all_parsed = weekdays + weekends
    if any(item is not None and item[0] == "unparseable" for item in all_parsed):
        return "skip"
    if not any(item is not None for item in all_parsed):
        return None
    return False


def flag_consistency_error(prefix: str, field: str, actual, expected) -> str | None:
    if expected == "skip":
        return None
    if expected is None:
        if actual is not None:
            return (
                f"{prefix}: field '{field}' should be empty/null because the "
                f"relevant hours are not published, got {actual!r}"
            )
        return None
    if actual is not expected:
        return (
            f"{prefix}: field '{field}' is {actual!r}, but published hours imply {expected}"
        )
    return None


def validate_hours_flags(obj: dict, rownum: int) -> list[str]:
    """When per-day hours are machine-readable, flags must match them.

    Machine-readable values are empty (unpublished), 'closed', or 'HH:MM-HH:MM'
    (24:00 allowed as a closing time). Unparseable hours skip the check unless a
    parseable day already forces the flag to true.
    """
    hour_fields = WEEKDAY_HOUR_FIELDS + WEEKEND_HOUR_FIELDS
    if not any(key in obj for key in hour_fields):
        return []
    prefix = f"row {rownum} ({obj.get('id') or '?'})"
    expected = {
        "open_saturday": expected_open_day(obj, "hours_sat"),
        "open_sunday": expected_open_day(obj, "hours_sun"),
        "open_weekends": expected_open_weekends(obj),
        "open_after_1700_weekday": expected_open_after_1700_weekday(obj),
        "after_hours": expected_after_hours(obj),
    }
    errors: list[str] = []
    for field, exp in expected.items():
        err = flag_consistency_error(prefix, field, obj.get(field), exp)
        if err:
            errors.append(err)
    return errors


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
        if schema_name == "locations.schema.json":
            errors.extend(validate_hours_flags(obj, i))
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
