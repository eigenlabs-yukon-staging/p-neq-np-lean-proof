# Rung 3

The proof is in `lean/PEqualNP/Outside/P_ne_NP_iff_SAT_not_mem_DTIME.lean`.

The pinned reference proves SAT is NP-complete in `L031`. Instantiating
`L018` with SAT and that certificate gives SAT membership in P exactly when
P equals NP. Instantiating `L004` with SAT gives membership in P exactly
when some natural exponent supplies a bound of the form `n ^ k + k`.

If P and NP differ, a time-bound witness at any exponent would put SAT
in P and yield equality. Conversely, equality would put SAT in P and supply
one exponent, contradicting nonmembership at every exponent.

## Pinned declarations used by the script

The reference checkout was at `364123c9dcfa1899438ad3b87670bb55f7c3ddae`,
with Lean `v4.36.0` and Mathlib `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`.
The following are the types printed by Lean after importing the three
modules in that checkout. Here `Language Bool` is a set of Boolean lists.

```text
PEqualNP.Library.L004 : ∀ (L : Language Bool),
  L ∈ PEqualNP.Library.P ↔ ∃ k, L ∈ PEqualNP.Library.DTIME fun n => n ^ k + k
PEqualNP.Library.L018 : ∀ (L : Language Bool),
  PEqualNP.Library.NPComplete L → (L ∈ PEqualNP.Library.P ↔ PEqualNP.Library.P = PEqualNP.Library.NP)
PEqualNP.Library.L031 : PEqualNP.Library.NPComplete PEqualNP.Search.SAT
```

The source files are `lean/PEqualNP/Library/L004.lean`, `L018.lean`, and
`L031.lean` in that directory. Their SHA-256 digests, in the same order, are
```text
b6fc1da2e58da601159a5a2b713da7aeb035db58e17afbf1559e064be06dedfa  L004.lean
c4438d32cd56ab637c820712ede2675c59a8f545191c2dd686e1522b462d89b0  L018.lean
504151a610c292d35f58f80703e051d0701937661d7aa1890bbb19ed8aea5c3d  L031.lean
```

- **L004.** The forward proof keeps the Boolean decider and machine.
  It shows each `p : Polynomial ℕ` satisfies `p.eval n ≤ n ^ k + k`
  for every `n` and some natural `k`. Its induction uses `d + c`
  for the monomial `c * n ^ d` and `a + b + 2` for a sum with
  exponents `a` and `b`. For `n < 2` each power is at most one.
  For `n ≥ 2` the increased exponent absorbs the coefficient or the
  sum of powers. The reverse proof keeps the machine and uses the time
  polynomial `Polynomial.X ^ k + Polynomial.C k`, whose evaluation is
  exactly the bound. This equivalence covers all natural exponents.
- **L018.** The certificate is a pair of membership in NP and NP-hardness
  under the pinned polynomial-time many-one reductions. If its language
  belongs to P, compose each reduction from an NP language with the
  polynomial-time decider, using `L016`. With `L010` this gives both
  containments and hence equality. If P equals NP, rewrite the required
  P membership using equality and use the first component of the certificate.
- **L031.** The result specializes Cook–Levin to exactly
  `PEqualNP.Search.SAT`. In `SearchHelpers/TableauAssembly.lean`,
  `Tab.npComplete_SAT_of` combines SAT membership in NP from `L029`
  with the following reduction from any language in NP. Compile its
  verifier and map the input to an encoded CNF tableau with polynomial
  witness length and run time bounds. The three inputs supplied by
  `L031` are `Tab.accepts_of_sat` (a satisfying tableau gives an
  accepting bounded witness), `Tab.sat_of_accepts` (an accepting bounded
  witness yields a satisfying tableau), and `Tab.cpt_tableau_of` applied to
  `Tab.cpt_stepPart` (the map to the encoded tableau runs in polynomial
  time). The conclusion of the assembly is `NPComplete SAT`, so no
  substitution of a different SAT language or reduction notion is needed.

## Local Lean evidence

To reproduce the signature and axiom queries, load the following diagnostic
in the pinned reference with `lake env lean` from its `lean/` directory.

```lean
import PEqualNP.Library.L004
import PEqualNP.Library.L018
import PEqualNP.Library.L031

#check @PEqualNP.Library.L004
#check @PEqualNP.Library.L018
#check @PEqualNP.Library.L031
#print axioms PEqualNP.Library.L004
#print axioms PEqualNP.Library.L018
#print axioms PEqualNP.Library.L031
```

The three axiom queries each returned `[propext, Classical.choice, Quot.sound]`.
The exact candidate file, SHA-256
`5740981101a706e359a57ad219fd2771642e7320e2575e816273cba1c2b94f1b`,
was checked in the pinned reference using the rung-3 statement from
`checkers/ladder.json` as the statement file.

```text
node tools/check-lean.mjs lean/PEqualNP/Outside/P_ne_NP_iff_SAT_not_mem_DTIME.lean <statement-file> check
```

The local result was `ACCEPTED (check)` for
`PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME`, with 4,329 constants rechecked
and transitive axioms `[propext, Quot.sound, Classical.choice]`. The checker
reads the recorded proposition in its Mathlib and `PEqualNP.Defs` environment
before checking that the compiled theorem has that type. This is a local
reproduction of the reference check. The hosted static audit only examines
the submitted source and does not execute Lean.
