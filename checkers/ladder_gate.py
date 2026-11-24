"""Organizer-owned ladder gate for the P != NP Lean proof ladder.

Reads one declared rung from stdin and compares it with the protected ladder
table. It passes only when the declared theorem name and Lean statement are
exactly the ones pinned for that rung, and then reports that rung's points.

It never sees the submitted files and never runs Lean: a pass binds the score
to the ladder table, it does not establish that the theorem is proved.
"""
import json
from pathlib import Path
import sys

# Fixed protected path, never a path supplied by the requester.
LADDER = json.loads(Path("/snapshot/files/checkers/ladder.json").read_text(encoding="utf-8"))
RUNGS = {entry["rung"]: entry for entry in LADDER["rungs"]}


def normalise(text):
    """Collapse every run of white space to one space and trim the ends."""
    return " ".join(text.split())


inputs = json.load(sys.stdin)
rung = inputs["rung"]
entry = RUNGS.get(rung)
if entry is None:
    result = {"passed": False, "rung": 0, "proof_ladder_points": 0,
              "message": "unknown rung"}
else:
    name_ok = normalise(inputs["theorem"]) == entry["theorem"]
    statement_ok = normalise(inputs["statement"]) == normalise(entry["statement"])
    passed = name_ok and statement_ok
    if passed:
        message = "declared theorem and statement match the pinned rung"
    elif not name_ok:
        message = "theorem name differs from the pinned name for this rung"
    else:
        message = "statement differs from the pinned statement for this rung"
    result = {"passed": passed, "rung": rung,
              "proof_ladder_points": entry["points"] if passed else 0,
              "message": message}
print(json.dumps(result, ensure_ascii=True))
