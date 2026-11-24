# P ≠ NP Lean proof ladder

Participants submit Lean 4 proofs of a pinned ladder of statements that ends in `P ≠ NP`, each read against the definitions of the reference project `brilliant-hq/pequalnp-proofs`.

## Problem and model

Every statement is read against the reference project at one pinned state:

- Repository: `https://github.com/brilliant-hq/pequalnp-proofs`, commit `364123c9dcfa1899438ad3b87670bb55f7c3ddae`.
- Lean toolchain: `leanprover/lean4:v4.36.0`. Mathlib: commit `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`.
- Definitions: `PEqualNP.Library.P`, `PEqualNP.Library.NP` and `PEqualNP.Library.DTIME` in `lean/PEqualNP/Defs/Base.lean`, and `PEqualNP.Search.SAT` in `lean/PEqualNP/Defs/Search.lean`. Machines are Mathlib's `Turing.FinTM2`; inputs are binary strings; NP is defined by polynomial-time verifiers with polynomially bounded witnesses.

The final target is

```lean
theorem PEqualNP.Outside.P_ne_NP : PEqualNP.Library.P ≠ PEqualNP.Library.NP := by
  ...
```

The ladder has nine rungs. Each rung above 0 is one theorem with a fixed name and a fixed statement:

| Rung | Points | Theorem name | Exact statement |
|---:|---:|---|---|
| 0 | 0 | none | none: no checked Lean progress is claimed |
| 1 | 10 | `PEqualNP.Outside.P_subset_NP` | `PEqualNP.Library.P ⊆ PEqualNP.Library.NP` |
| 2 | 20 | `PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_P` | `PEqualNP.Library.P ≠ PEqualNP.Library.NP ↔ PEqualNP.Search.SAT ∉ PEqualNP.Library.P` |
| 3 | 35 | `PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME` | `PEqualNP.Library.P ≠ PEqualNP.Library.NP ↔ ∀ k : ℕ, PEqualNP.Search.SAT ∉ PEqualNP.Library.DTIME (fun n : ℕ => n ^ k + k)` |
| 4 | 50 | `PEqualNP.Outside.SAT_not_mem_DTIME_1` | `PEqualNP.Search.SAT ∉ PEqualNP.Library.DTIME (fun n : ℕ => n ^ 1 + 1)` |
| 5 | 65 | `PEqualNP.Outside.SAT_not_mem_DTIME_2` | `PEqualNP.Search.SAT ∉ PEqualNP.Library.DTIME (fun n : ℕ => n ^ 2 + 2)` |
| 6 | 80 | `PEqualNP.Outside.SAT_not_mem_DTIME_3` | `PEqualNP.Search.SAT ∉ PEqualNP.Library.DTIME (fun n : ℕ => n ^ 3 + 3)` |
| 7 | 90 | `PEqualNP.Outside.SAT_not_mem_P` | `PEqualNP.Search.SAT ∉ PEqualNP.Library.P` |
| 8 | 100 | `PEqualNP.Outside.P_ne_NP` | `PEqualNP.Library.P ≠ PEqualNP.Library.NP` |

Rungs 1 to 3 restate the target: containment, then the target as a statement about one language, then as a countable family of fixed-polynomial lower bounds. Rungs 4 to 6 are the first three members of that family. Rung 7 is the whole family and rung 8 is the target itself.

A rung is reached when the submission contains one Lean file, `lean/PEqualNP/Outside/<last part of the theorem name>.lean`, that meets the reference checker's requirements:

1. It builds with the pinned toolchain and the pinned Mathlib.
2. It contains no `sorry` and no `admit`, anywhere under the theorem.
3. The theorem's transitive axioms are only `propext`, `Classical.choice` and `Quot.sound`. An added `axiom`, `native_decide`, `unsafe`, `implemented_by` or `extern` is refused.
4. It declares the theorem with exactly the name and exactly the statement in the table, read against Mathlib and `PEqualNP/Defs` and against nothing the file declares. A notation, instance, coercion or local definition in the file must not change what the statement means.
5. It imports only Mathlib and modules of the reference project at the pinned commit. Helpers go above the theorem inside a namespace named after the theorem.

## Score

The score is `proof_ladder_points`, an integer from 0 to 100. Higher is better.

A submission declares exactly one rung. The score is the points of that rung in the table. It is computed by the protected checker `ladder_gate` from the declared rung, theorem name and statement; the reviewer does not choose the number. Points are not added across rungs and there is no partial credit inside a rung.

A submission whose declared rung is not established is invalid and receives no score. It is not moved down to a lower rung. Declare the rung you can prove.

## What does not count

- A proof read against definitions other than the pinned ones, including a local copy of `P`, `NP`, `DTIME`, `SAT`, machines, encodings or polynomial bounds, whatever it is named.
- A theorem with a different name, a weaker statement, extra hypotheses, or a statement that only matches after a notation or coercion declared in the file.
- A file that contains `sorry`, `admit`, an added `axiom`, `native_decide`, `unsafe`, `implemented_by` or `extern`.
- A proof that depends on a helper that is not in the submission and not in the reference project at the pinned commit.
- A prose argument, a paper, a link, a build transcript or terminal output with no Lean source behind it. These are context, never evidence that a rung is reached.
- A relativized, oracle, circuit, average-case or other model result offered in place of the stated theorem.
- A result for a toolchain, Mathlib or reference commit other than the pinned ones.

## Submission and review

Submit only files under `submission/`:

- `submission.json`: the claim, the `ladder_gate` check with the declared rung, theorem name and statement, and the static audit experiment.
- `proof.md`: which rung is claimed, the file that proves it, and a short map of the argument.
- `lean_audit.py`: the static audit experiment. It lists the submitted Lean files with their sizes, hashes, imports and forbidden tokens, and reports where the declared theorem appears.
- `lean/PEqualNP/Outside/<Name>.lean`: the Lean proof, for any rung above 0.

Every submission must declare a rung; unscored partial results are not accepted. Limits: 128 files, 262,144 bytes per file, 1,048,576 bytes in total.

Review has three stages. First, the protected checker `ladder_gate` compares the declared theorem name and statement with the table and reports the rung's points; without a pass there is no score. Second, an LLM reviewer reads every submitted file and the audit output and decides whether the claim is established exactly as written. Third, results are promoted by hand: before a result above rung 0 is promoted, the organizers run the reference checker (`node tools/check-lean.mjs <file> <statement> check`) on the submitted file at the pinned commit and promote only on `ACCEPTED (check)`.

The hosted evaluator runs in a sandbox with no network and no Lean toolchain, so it does not run Lean's kernel. The reviewer's judgment is an assessment of the submitted source, not a formal certificate; the reference checker run at promotion is the formal check.
