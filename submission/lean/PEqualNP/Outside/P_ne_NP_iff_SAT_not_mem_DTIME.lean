import PEqualNP.Library.L002
import PEqualNP.Library.L003
import PEqualNP.Library.L010
import PEqualNP.Library.L016
import PEqualNP.Library.L029
import PEqualNP.Library.L031
import PEqualNP.Library.Helpers.OutputLength

namespace PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME

private theorem monomialBound (p : Polynomial ℕ) :
    ∃ k : ℕ, ∀ n : ℕ, p.eval n ≤ n ^ k + k := by
  obtain ⟨a, d, h⟩ := PEqualNP.Library.Helpers.poly_le_monomial p
  let k := d + a + p.eval 0 + p.eval 1
  refine ⟨k, fun n => ?_⟩
  rcases Nat.lt_or_ge n 2 with hsmall | hlarge
  · have hz : n = 0 ∨ n = 1 := by omega
    apply Nat.le_trans _ (Nat.le_add_left _ _)
    rcases hz with rfl | rfl <;> dsimp [k] <;> omega
  · have ha : a ≤ n ^ a := (Nat.lt_pow_self (by omega : 1 < n)).le
    calc
      p.eval n ≤ a * n ^ d := h n (by omega)
      _ ≤ n ^ a * n ^ d := Nat.mul_le_mul_right _ ha
      _ = n ^ (a + d) := (pow_add _ _ _).symm
      _ ≤ n ^ k := Nat.pow_le_pow_right (by omega) (by dsimp [k]; omega)
      _ ≤ n ^ k + k := Nat.le_add_right _ _

end PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME

theorem PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME :
    PEqualNP.Library.P ≠ PEqualNP.Library.NP ↔
      ∀ k : ℕ, PEqualNP.Search.SAT ∉ PEqualNP.Library.DTIME (fun n : ℕ => n ^ k + k) := by
  constructor
  · intro hne k htime
    have hp : PEqualNP.Search.SAT ∈ PEqualNP.Library.P := by
      apply (PEqualNP.Library.L003 _).mpr
      refine ⟨Polynomial.X ^ k + Polynomial.C k, ?_⟩
      simpa using htime
    apply hne
    apply Set.Subset.antisymm PEqualNP.Library.L010
    intro L hL
    exact PEqualNP.Library.L016 L PEqualNP.Search.SAT (PEqualNP.Library.L031.2 L hL) hp
  · intro hno heq
    have hp : PEqualNP.Search.SAT ∈ PEqualNP.Library.P := by
      rw [heq]
      exact PEqualNP.Library.L029
    obtain ⟨p, hp⟩ := (PEqualNP.Library.L003 _).mp hp
    obtain ⟨k, hbound⟩ := PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME.monomialBound p
    exact hno k (PEqualNP.Library.L002 _ _ hbound hp)
