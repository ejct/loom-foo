#!/usr/bin/env python3
"""Small deterministic checker for actual text edits (not a grammar evaluator).

Usage:
  python scripts/check_invariants.py --case tests/sample.json --output-file /tmp/result.txt

A case JSON object must contain source (str); optional exact protected_fragments,
expected_contains, forbidden_contains, unchanged (bool), and exact_output (str).
The checker compares literal Unicode strings and counts; it does not parse Markdown,
run an LLM, certify normative correctness, or provide automatic integration.
"""
import argparse
import json
import pathlib
import sys


def check(case: dict, output: str) -> list[str]:
    errors: list[str] = []
    source = case.get("source")
    if not isinstance(source, str):
        return ["case.source must be text"]
    if not isinstance(output, str):
        return ["output must be text"]
    if case.get("unchanged", False) and output != source:
        errors.append("source changed despite unchanged=true")
    if "exact_output" in case and output != case["exact_output"]:
        errors.append("output does not match exact_output")
    for item in case.get("protected_fragments", []):
        if not isinstance(item, str) or not item:
            errors.append("invalid protected fragment")
        elif source.count(item) != output.count(item):
            errors.append(f"protected literal count changed: {item!r}")
    for item in case.get("expected_contains", []):
        if item not in output:
            errors.append(f"required literal missing: {item!r}")
    for item in case.get("forbidden_contains", []):
        if item in output:
            errors.append(f"forbidden literal found: {item!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, help="JSON case with source and constraints")
    parser.add_argument("--output-file", required=True, help="UTF-8 file with actual output")
    args = parser.parse_args()
    case = json.loads(pathlib.Path(args.case).read_text(encoding="utf-8"))
    result = pathlib.Path(args.output_file).read_text(encoding="utf-8")
    errors = check(case, result)
    if errors:
        print("FAIL: " + " | ".join(errors))
        return 1
    print("PASS: literal constraints only; no language-quality or runtime claim")
    return 0


if __name__ == "__main__":
    sys.exit(main())
