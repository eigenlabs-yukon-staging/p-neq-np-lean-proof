# Rung 3

The proof is in `lean/PEqualNP/Outside/P_ne_NP_iff_SAT_not_mem_DTIME.lean`.

The pinned reference proves SAT is NP-complete in `L031`. Instantiating
`L018` with SAT and that certificate gives SAT membership in P exactly when
P equals NP. Instantiating `L004` with SAT gives membership in P exactly
when some natural exponent supplies a bound of the form `n ^ k + k`.

If P and NP differ, a time-bound witness at any exponent would put SAT
in P and yield equality. Conversely, equality would put SAT in P and supply
one exponent, contradicting nonmembership at every exponent.
