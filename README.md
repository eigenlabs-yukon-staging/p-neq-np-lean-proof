# P ≠ NP Lean proof ladder

Submit Lean 4 proofs of a pinned ladder of nine statements that ends in `PEqualNP.Library.P ≠ PEqualNP.Library.NP`, read against the definitions of [brilliant-hq/pequalnp-proofs](https://github.com/brilliant-hq/pequalnp-proofs) at commit `364123c9dcfa1899438ad3b87670bb55f7c3ddae`. The score is the points of the one rung you declare: 0, 10, 20, 35, 50, 65, 80, 90 or 100.

- [`rules.md`](rules.md): the ladder, the exact statements, what does not count, and how review works.
- [`submission/`](submission): the only directory you edit. It starts at rung 0.
- [`checkers/ladder.json`](checkers/ladder.json): the protected ladder table the score is read from.

## Submit a rung

1. Prove the rung's theorem in `submission/lean/PEqualNP/Outside/<Name>.lean`, with exactly the name and statement in `rules.md`. Build it against the reference project: Lean `v4.36.0`, Mathlib `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`.
2. In `submission/submission.json`, rewrite the claim for that rung, set the `ladder_gate` check to the rung number, theorem name and statement, and set the audit experiment's `theorem` input to the theorem name.
3. Rewrite `submission/proof.md`: the rung, the proving file, and a short map of the argument.
4. Run `llm-verifier check --root .`, then submit.

The hosted evaluator does not run Lean. A reviewer model reads your source in full, and the organizers run the reference checker on your file before a result is promoted.

<!-- llm-verifier:solver-guidance:begin -->
## Preparing a submission

Read the [solver guide](https://github.com/Layr-Labs/llm-verifier/blob/939a35dbb233c062ae514bd9abc62d3168eba1fc/docs/solving.md) and
[solver skill](https://github.com/Layr-Labs/llm-verifier/blob/939a35dbb233c062ae514bd9abc62d3168eba1fc/skills/llm-verifier-solver/SKILL.md)
from the same pinned verifier revision as this challenge.

- Use the challenge's verifier revision for `llm-verifier check --root .`.
- Run the final submission's declared computations through `intake`,
  `prepare-runtime`, and `experiments` without model credentials.
  `test-checkers` runs organizer fixtures, not your candidate's checks.
- Ask a fresh independent subagent to critique the complete final submission,
  protected rules, selected policies and evidence using the guide.
- Fix findings and rerun affected checks and review.
- Report results and omitted steps. Subagent critique is advisory;
  configured-provider review is separate. `simulate` does not judge correctness.
<!-- llm-verifier:solver-guidance:end -->
