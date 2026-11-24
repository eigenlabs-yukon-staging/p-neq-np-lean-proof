"""Static audit of the submitted Lean files. Candidate-owned evidence, not a proof check.

Reads {"theorem": "<declared theorem name, or none>"} from stdin and prints one
JSON object: every submitted .lean file with its size, SHA-256, imports and any
forbidden token, and where the declared theorem is stated. It does not run Lean.
"""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path("/snapshot/files")
FORBIDDEN = re.compile(r"\b(sorry|admit|axiom|native_decide|unsafe|implemented_by|extern)\b")
IMPORT = re.compile(r"^\s*import\s+(\S+)", re.MULTILINE)
ALLOWED_IMPORT = re.compile(r"^(Mathlib|PEqualNP)(\.|$)")


def strip_comments(text):
    """Remove /- ... -/ blocks (nested) and -- line comments."""
    out, depth, i = [], 0, 0
    while i < len(text):
        if text.startswith("/-", i):
            depth += 1
            i += 2
        elif depth and text.startswith("-/", i):
            depth -= 1
            i += 2
        elif depth:
            i += 1
        elif text.startswith("--", i):
            while i < len(text) and text[i] != "\n":
                i += 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


declared = json.load(sys.stdin)["theorem"]
files, found = [], []
for path in sorted(ROOT.rglob("*.lean")):
    rel = path.relative_to(ROOT).as_posix()
    raw = path.read_bytes()
    code = strip_comments(raw.decode("utf-8", errors="replace"))
    imports = IMPORT.findall(code)
    files.append({
        "path": rel,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "imports": imports[:64],
        "imports_outside_mathlib_and_reference": [m for m in imports if not ALLOWED_IMPORT.match(m)][:16],
        "forbidden_tokens": sorted(set(FORBIDDEN.findall(code))),
    })
    if declared != "none":
        match = re.search(r"\btheorem\s+" + re.escape(declared) + r"\s*:(.*?):=", code, re.DOTALL)
        if match:
            found.append({"path": rel, "statement": " ".join(match.group(1).split())[:512]})

print(json.dumps({
    "declared_theorem": declared,
    "lean_file_count": len(files),
    "lean_files": files[:128],
    "declared_theorem_found": found[:8],
    "any_forbidden_token": any(f["forbidden_tokens"] for f in files),
    "any_import_outside_mathlib_and_reference": any(f["imports_outside_mathlib_and_reference"] for f in files),
    "ran_lean": False,
}, ensure_ascii=True, sort_keys=True))
