import PEqualNP.Library.L004
import PEqualNP.Library.L010
import PEqualNP.Library.L016
import PEqualNP.Library.L031

theorem PEqualNP.Outside.P_ne_NP_iff_SAT_not_mem_DTIME :
    PEqualNP.Library.P ≠ PEqualNP.Library.NP ↔
      ∀ k : ℕ, PEqualNP.Search.SAT ∉ PEqualNP.Library.DTIME (fun n : ℕ => n ^ k + k) := by
  have satTime := PEqualNP.Library.L004 PEqualNP.Search.SAT
  have complete := PEqualNP.Library.L031
  constructor
  · intro unequal k bounded
    have satInP := satTime.mpr ⟨k, bounded⟩
    apply unequal
    refine Set.Subset.antisymm PEqualNP.Library.L010 ?_
    intro L inNP
    exact PEqualNP.Library.L016 L PEqualNP.Search.SAT (complete.2 L inNP) satInP
  · intro outside equal
    have satInP : PEqualNP.Search.SAT ∈ PEqualNP.Library.P := equal.symm ▸ complete.1
    obtain ⟨k, bounded⟩ := satTime.mp satInP
    exact outside k bounded
