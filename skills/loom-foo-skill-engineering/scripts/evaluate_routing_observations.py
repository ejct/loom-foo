#!/usr/bin/env python3
"""Offline host-routing observation comparator; does not invoke or authenticate a host."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

def evaluate(cases: list[dict], observations: list[dict]) -> dict:
    cases_by_id = {x["id"]: x for x in cases}
    obs_by_id = {x["case_id"]: x for x in observations}
    if len(cases_by_id) != len(cases) or len(obs_by_id) != len(observations) or set(obs_by_id) - set(cases_by_id):
        raise ValueError("duplicate case id or observation of unknown fixture")
    rows = []
    for case in cases:
        obs = obs_by_id.get(case["id"])
        trusted_form = (obs is not None and obs.get("origin") == "HOST_TRACE"
                        and isinstance(obs.get("trace_ref"), str) and bool(obs["trace_ref"].strip()))
        if not trusted_form:
            routing, delivery = "NOT_CONFIRMED", "NOT_CONFIRMED"
        elif obs.get("selected_owner") != case["expected_owner"]:
            routing, delivery = "FAIL", "NOT_APPLICABLE"
        else:
            routing = "PASS"
            delivery = ("NOT_APPLICABLE" if case["expected_owner"] == "none" else
                        "PASS" if obs.get("root_read_observed") is True else "NOT_CONFIRMED")
        rows.append({"case_id": case["id"], "expected_owner": case["expected_owner"],
                     "routing": routing, "root_delivery": delivery,
                     "trace_ref": obs.get("trace_ref") if trusted_form else None})
    status = ("ROUTING_FAIL" if any(x["routing"] == "FAIL" for x in rows) else
              "INCOMPLETE_NOT_CONFIRMED" if any("NOT_CONFIRMED" in (x["routing"], x["root_delivery"]) for x in rows)
              else "OBSERVED_WITHIN_SCOPE")
    return {"status": status, "cases": rows, "claimed_trace_provenance_not_authenticated": True}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observations", type=Path, required=True)
    parser.add_argument("--cases", type=Path, required=True, help="Frozen expected-owner fixture JSON array")
    args = parser.parse_args()
    try:
        result = evaluate(json.loads(args.cases.read_text(encoding="utf8")),
                          json.loads(args.observations.read_text(encoding="utf8")))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if result["status"] == "ROUTING_FAIL" else 2 if result["status"] != "OBSERVED_WITHIN_SCOPE" else 0

if __name__ == "__main__":
    raise SystemExit(main())
