import PEqualNP.Library.L004
import PEqualNP.Library.L018
import PEqualNP.Library.L031

theorem PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME :
    PEqualNP.Library.P ≠ PEqualNP.Library.NP ↔
      ∀ k : ℕ, PEqualNP.Search.SAT ∉ PEqualNP.Library.DTIME (fun n : ℕ => n ^ k + k) := by
  have satInP := PEqualNP.Library.L018 PEqualNP.Search.SAT PEqualNP.Library.L031
  have satTime := PEqualNP.Library.L004 PEqualNP.Search.SAT
  constructor
  · intro hne k hk
    exact hne (satInP.mp (satTime.mpr ⟨k, hk⟩))
  · intro hall heq
    obtain ⟨k, hk⟩ := satTime.mp (satInP.mpr heq)
    exact hall k hk
