# Rung 1

The proof is in `lean/PEqualNP/Outside/P_subset_NP.lean`.

Start with a language `L` in P and a polynomial-time Boolean decider for
`L`. Use the relation on input-witness pairs that holds precisely when the
input is in `L`. The pair encoding lists the input with `Sum.inl` tags
followed by the witness with `Sum.inr` tags. Keep and untag the first group,
discard the other group, and apply the decider. Choose the zero polynomial
as the witness-length bound. A member uses the empty witness. A witness
for any input certifies membership because of how the relation was chosen.

## Pinned library facts

The two operations used in the machine construction have the following Lean
signatures in the pinned reference at `364123c9dcfa1899438ad3b87670bb55f7c3ddae`.

```text
PEqualNP.Library.L007 : ∀ (α β γ αΓ βΓ γΓ : Type) (ea : α → List αΓ) (eb : β → List βΓ) (ec : γ → List γΓ) (f : α → β)
  (g : β → γ),
  PEqualNP.Library.ComputableInPolyTime ea eb f →
    PEqualNP.Library.ComputableInPolyTime eb ec g → PEqualNP.Library.ComputableInPolyTime ea ec fun a => g (f a)
@PEqualNP.Library.Machines.filterMap_polyTime : ∀ {α β αΓ βΓ : Type} [Fintype αΓ] (ea : α → List αΓ) (eb : β → List βΓ)
  (f : α → β) (φ : αΓ → Option βΓ),
  (∀ (a : α), eb (f a) = List.filterMap φ (ea a)) → Nonempty (Turing.TM2ComputableInPolyTime ea eb f)
```

The filter-map machine scans its encoded input, applying a fixed map from
symbols to optional output symbols. A retained symbol contributes at most one
output symbol. This works for the finite tagged Boolean alphabet. In the
submitted proof its output is shown equal to the first component of the pair
by expanding the pair encoding and applying the filter-map list laws. The
composition theorem runs this machine, moves its output to the decider's
input stack, and runs the decider with a polynomial bound. These are the
only imported proof facts used in the machine construction.

The diagnostic queries `#print axioms PEqualNP.Library.L007` and
`#print axioms PEqualNP.Library.Machines.filterMap_polyTime` each returned
the three permitted axioms `propext`, `Classical.choice`, and `Quot.sound`.
The local reference checker using Lean `v4.36.0` and Mathlib
`fc4f59e577feb1a4956671bc04ac18aaaf8cd842` separately returned
`ACCEPTED (check)` for the exact rung-1 proposition. It rechecked 1,480
constants and reported the same three transitive axioms. The local checker
invocation was `node tools/check-lean.mjs lean/PEqualNP/Outside/P_subset_NP.lean
<statement-file> check`, with the proposition taken from the protected ladder.
