import PEqualNP.Library.L007
import PEqualNP.Library.Machines.FilterMap

theorem PEqualNP.Outside.P_subset_NP :
    PEqualNP.Library.P ⊆ PEqualNP.Library.NP := by
  intro L hP
  obtain ⟨decider, hdecider, htime⟩ := hP
  refine ⟨{pair | pair.1 ∈ L}, 0, ?_, ?_⟩
  · refine ⟨fun pair => decider pair.1, fun pair => hdecider pair.1, ?_⟩
    have hproject : PEqualNP.Library.ComputableInPolyTime PEqualNP.Library.encodePair
        (fun x : List Bool => x) (fun pair : List Bool × List Bool => pair.1) := by
      refine PEqualNP.Library.Machines.filterMap_polyTime _ _ _
        (Sum.elim some (fun _ => none)) ?_
      rintro ⟨input, witness⟩
      simp [PEqualNP.Library.encodePair, List.filterMap_append, List.filterMap_map]
    exact PEqualNP.Library.L007 _ _ _ _ _ _ _ _ _ _ _ hproject htime
  · intro input
    constructor
    · intro hinput
      exact ⟨[], by simp, hinput⟩
    · rintro ⟨witness, _, hwitness⟩
      exact hwitness
