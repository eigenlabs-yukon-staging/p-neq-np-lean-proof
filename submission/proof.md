# Rung 3 • P versus NP and the fixed deterministic time classes

The theorem is `PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME`, in
`lean/PEqualNP/Outside/P_ne_NP_iff_SAT_not_mem_DTIME.lean`. The theorem concerns
the SAT language and the classes P, NP and DTIME in the pinned project.
The argument gives an equivalence and its only ladder claim is rung 3.

Suppose P differs from NP and SAT belongs to the fixed time class at
exponent k. Applying the reverse direction of L004 to that exponent and
membership puts SAT in P. L031 supplies a polynomial-time reduction to
SAT from each language in NP through the hardness component of
`NPComplete`. L016 composes the reduction and the SAT decision procedure,
putting each of those languages in P. The resulting inclusion NP ⊆ P
and L010's inclusion P ⊆ NP give equality, a contradiction.

In the reverse implication, assume SAT belongs to none of the fixed
time classes. If P equals NP, the membership component of L031 gives
SAT in P by transport along the class equality. The forward direction
of L004 gives an exponent with SAT in its fixed time class, contradicting
the hypothesis at that exponent.

## Direct reference imports

The code below is source context from the pinned
`brilliant-hq/pequalnp-proofs` commit
`364123c9dcfa1899438ad3b87670bb55f7c3ddae`. The Lean proof imports these
modules from the reference checkout. Each SHA-256 below is over the
original source bytes. The quoted code makes the contracts and their
implementations available to a reviewer alongside the submitted argument.

The reference L004 proves the polynomial bound by induction over
natural-coefficient polynomials. At lengths 0 and 1 every power is at
most 1 and the additive allowance covers sums and coefficients. For
length at least 2 the exponent can absorb the coefficient for a
monomial and can absorb the extra factor of two for polynomial addition.
In the converse it uses the polynomial X^k + C k, whose evaluation is
exactly the time bound. L031 applies the reference tableau assembly to
soundness, completeness, and polynomial-time construction for the
tableau from the compiled verifier.

### L004

Source SHA-256 `b6fc1da2e58da601159a5a2b713da7aeb035db58e17afbf1559e064be06dedfa`

```lean
import PEqualNP.Defs
import Mathlib.Tactic

/-- P is the union of DTIME(n^k + k). -/
theorem PEqualNP.Library.L004 : ∀ L : Language Bool, L ∈ PEqualNP.Library.P ↔
    ∃ k : ℕ, L ∈ PEqualNP.Library.DTIME (fun n : ℕ => n ^ k + k) := by
  intro L
  -- every polynomial with natural coefficients is below some n^k + k
  have bound : ∀ p : Polynomial ℕ, ∃ k : ℕ, ∀ n : ℕ, Polynomial.eval n p ≤ n ^ k + k := by
    intro p
    have small : ∀ (n e : ℕ), n < 2 → n ^ e ≤ 1 := fun n e hn => by
      have := Nat.pow_le_pow_left (show n ≤ 1 by omega) e
      rwa [Nat.one_pow] at this
    induction p using Polynomial.induction_on' with
    | add p q hp hq =>
      obtain ⟨a, ha⟩ := hp
      obtain ⟨b, hb⟩ := hq
      refine ⟨a + b + 2, fun n => ?_⟩
      rw [Polynomial.eval_add]
      have h1 := ha n
      have h2 := hb n
      rcases Nat.lt_or_ge n 2 with hn | hn
      · have e1 := small n a hn
        have e2 := small n b hn
        omega
      · have pa : n ^ a ≤ n ^ (a + b) := Nat.pow_le_pow_right (by omega) (by omega)
        have pb : n ^ b ≤ n ^ (a + b) := Nat.pow_le_pow_right (by omega) (by omega)
        have ps : n ^ (a + b + 1) = n ^ (a + b) * n := Nat.pow_succ ..
        have pt : n ^ (a + b + 1) ≤ n ^ (a + b + 2) := Nat.pow_le_pow_right (by omega) (by omega)
        have : 2 * n ^ (a + b) ≤ n ^ (a + b) * n := by
          rw [Nat.mul_comm]; exact Nat.mul_le_mul_left _ hn
        omega
    | monomial d c =>
      refine ⟨d + c, fun n => ?_⟩
      rw [Polynomial.eval_monomial]
      rcases Nat.lt_or_ge n 2 with hn | hn
      · have e1 := small n d hn
        calc c * n ^ d ≤ c * 1 := Nat.mul_le_mul_left _ e1
          _ ≤ n ^ (d + c) + (d + c) := by omega
      · have hc : c ≤ n ^ c := (Nat.lt_pow_self (by omega)).le
        calc c * n ^ d ≤ n ^ c * n ^ d := Nat.mul_le_mul_right _ hc
          _ = n ^ (d + c) := by rw [Nat.add_comm, Nat.pow_add]
          _ ≤ n ^ (d + c) + (d + c) := Nat.le_add_right _ _
  constructor
  · rintro ⟨f, hf, ⟨c⟩⟩
    obtain ⟨k, hk⟩ := bound c.time
    exact ⟨k, f, hf, c.toTM2ComputableInTime, hk⟩
  · rintro ⟨k, f, hf, c, hc⟩
    refine ⟨f, hf, ⟨⟨c.toTM2ComputableAux, Polynomial.X ^ k + Polynomial.C k, fun a => ?_⟩⟩⟩
    refine ⟨(c.outputsFun a).toEvalsTo, (c.outputsFun a).steps_le_m.trans ((hc _).trans ?_)⟩
    simp
```

### L010

Source SHA-256 `991d393baad64e2bea3c0eb51841732de91ee2433ac5599c2a91181102fcb2ef`

```lean
import PEqualNP.Library.L007
import PEqualNP.Library.Machines.FilterMap

/-- P is contained in NP: the verifier ignores the witness. It keeps the first component of the
pair and runs the decider on it; the empty witness always works. -/
theorem PEqualNP.Library.L010 : PEqualNP.Library.P ⊆ PEqualNP.Library.NP := by
  rintro L ⟨f, hf, hc⟩
  refine ⟨{p | p.1 ∈ L}, 0, ⟨fun p => f p.1, fun p => hf p.1, ?_⟩, fun x => ?_⟩
  · refine PEqualNP.Library.L007 _ _ _ _ _ _ _ _ _ (fun p : List Bool × List Bool => p.1) f ?_ hc
    refine PEqualNP.Library.Machines.filterMap_polyTime _ _ _
      (fun s : Bool ⊕ Bool => Sum.elim some (fun _ => none) s) ?_
    rintro ⟨x, w⟩
    simp [PEqualNP.Library.encodePair, List.filterMap_append, List.filterMap_map]
  · exact ⟨fun h => ⟨[], by simp, h⟩, fun ⟨_, _, h⟩ => h⟩
```

### L016

Source SHA-256 `790378d8fc0e82ebc464dffeeb78f1ba8ef051d5ee09f00592f862b70c316fd9`

```lean
import PEqualNP.Library.L007

/-- P is closed under polynomial-time reductions: run the reduction, then the decider. -/
theorem PEqualNP.Library.L016 : ∀ L₁ L₂ : Language Bool,
    PEqualNP.Library.PolyTimeReducible L₁ L₂ → L₂ ∈ PEqualNP.Library.P →
    L₁ ∈ PEqualNP.Library.P :=
  fun _ _ ⟨f, hf, hf'⟩ ⟨g, hg, hg'⟩ =>
    ⟨fun x => g (f x), fun x => (hf' x).trans (hg (f x)),
      PEqualNP.Library.L007 _ _ _ _ _ _ _ _ _ f g hf hg'⟩
```

### L031

Source SHA-256 `504151a610c292d35f58f80703e051d0701937661d7aa1890bbb19ed8aea5c3d`

```lean
import PEqualNP.Library.SearchHelpers.TableauSound
import PEqualNP.Library.SearchHelpers.TableauComplete
import PEqualNP.Library.SearchHelpers.TableauStepCPT
import PEqualNP.Library.SearchHelpers.TableauEdgeCPT
import PEqualNP.Library.SearchHelpers.TableauAssembly

/-- SAT is NP-complete (Cook 1971, Levin 1973). SAT is in NP (L-lib-029). For hardness, an NP
verifier compiles to a micro-instruction code; the input is mapped to the encoding of the tableau
formula of that code, which is satisfiable exactly when some witness makes the code accept, and
whose encoding is written in polynomial time. -/
theorem PEqualNP.Library.L031 : PEqualNP.Library.NPComplete PEqualNP.Search.SAT :=
  PEqualNP.Library.SearchHelpers.Tab.npComplete_SAT_of
    (fun c zs m T hz h => PEqualNP.Library.SearchHelpers.Tab.accepts_of_sat c zs m T hz h)
    (fun c zs m T hz w hw h => PEqualNP.Library.SearchHelpers.Tab.sat_of_accepts c zs m T hz w hw h)
    (fun c p q => PEqualNP.Library.SearchHelpers.Tab.cpt_tableau_of c p q
      (PEqualNP.Library.SearchHelpers.Tab.cpt_stepPart c p q))
```
