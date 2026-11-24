"""Static audit of the submitted Lean files. Candidate-owned evidence, not a proof check.

Reads {"theorem": "<declared theorem name, or none>"} from stdin and prints one
JSON object: every submitted .lean file with its size, SHA-256, imports and any
forbidden token, and where the declared theorem is stated. It authenticates the direct reference sources against the pinned Git commit.
It does not run Lean.
"""
import base64
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


PINNED = "364123c9dcfa1899438ad3b87670bb55f7c3ddae"


def git_object(records, oid, kind):
    record = records[oid]
    if record["type"] != kind:
        raise ValueError("unexpected Git object type")
    content = base64.b64decode(record["bytes"], validate=True)
    header = f"{kind} {len(content)}\0".encode("ascii")
    if hashlib.sha1(header + content).hexdigest() != oid:
        raise ValueError("Git object digest mismatch")
    return content


def tree_entry(tree, name):
    offset = 0
    result = None
    while offset < len(tree):
        end = tree.index(b"\0", offset)
        mode, raw_name = tree[offset:end].split(b" ", 1)
        digest = tree[end + 1:end + 21]
        if len(digest) != 20:
            raise ValueError("truncated Git tree entry")
        if raw_name == name:
            if result is not None:
                raise ValueError("duplicate Git tree entry")
            result = (mode, digest.hex())
        offset = end + 21
    if result is None:
        raise ValueError("Git tree entry missing")
    return result


def verify_sources(records, paths):
    header = git_object(records, PINNED, "commit").split(b"\n", 1)[0]
    key, root_oid = header.split(b" ", 1)
    if key != b"tree":
        raise ValueError("invalid Git commit tree header")
    findings = []
    for path in paths:
        tree_oid = root_oid.decode("ascii")
        segments = path.encode("ascii").split(b"/")
        for name in segments[:-1]:
            mode, tree_oid = tree_entry(git_object(records, tree_oid, "tree"), name)
            if mode != b"40000":
                raise ValueError("unexpected Git directory mode")
        mode, blob_oid = tree_entry(git_object(records, tree_oid, "tree"), segments[-1])
        if mode not in (b"100644", b"100755"):
            raise ValueError("unexpected Git source file mode")
        source = git_object(records, blob_oid, "blob")
        findings.append({
            "path": path,
            "blob_oid": blob_oid,
            "sha256": hashlib.sha256(source).hexdigest(),
            "source": source.decode("utf-8"),
        })
    return findings



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

object_fence = "```json git-objects\n"
proof = (ROOT / "proof.md").read_text(encoding="utf-8")
objects = json.loads(proof.split(object_fence, 1)[1].split("\n```", 1)[0])
import_paths = sorted({
    "lean/" + module.replace(".", "/") + ".lean"
    for file in files
    for module in file["imports"]
    if module.startswith("PEqualNP.")
})

print(json.dumps({
    "reference_commit": PINNED,
    "verified_reference_sources": verify_sources(objects, import_paths),
    "declared_theorem": declared,
    "lean_file_count": len(files),
    "lean_files": files[:128],
    "declared_theorem_found": found[:8],
    "any_forbidden_token": any(f["forbidden_tokens"] for f in files),
    "any_import_outside_mathlib_and_reference": any(f["imports_outside_mathlib_and_reference"] for f in files),
    "ran_lean": False,
}, ensure_ascii=True, sort_keys=True))
