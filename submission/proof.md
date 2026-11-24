# Rung 3

The proof is in `lean/PEqualNP/Outside/P_ne_NP_iff_SAT_not_mem_DTIME.lean`.
It reads the fixed proposition against the P, NP, DTIME and SAT definitions
in the reference at `364123c9dcfa1899438ad3b87670bb55f7c3ddae`.

Suppose SAT has a decision procedure for one of the displayed bounds. The
time polynomial `Polynomial.X ^ k + Polynomial.C k` evaluates to that
bound at every input length. By `L003`, the procedure puts SAT in P. By the
hardness component of `L031`, every NP language reduces to SAT under the
pinned polynomial-time many-one reductions. Applying `L016` to that
reduction and the SAT decider puts each such language in P. Have the
opposite containment by `L010`, giving P = NP.

Conversely, if P = NP, `L029` puts SAT in P by rewriting. By `L003` that
supplies a polynomial time bound `p`. The local helper `monomialBound`
then supplies a fixed bound. It uses a monomial upper bound
`p.eval n ≤ a * n ^ d` for `1 ≤ n` and takes
`k = d + a + p.eval 0 + p.eval 1`. At inputs of length zero or one, the
additive term alone covers the polynomial. At any other length, `a ≤ n ^ a`
and `a + d ≤ k`. Thus `p.eval n ≤ n ^ k + k` at every length, so
monotonicity `L002` puts SAT in the fixed-bound class. If membership was
excluded at every exponent, this gives a contradiction.

## Evidence for direct imports

The following signatures and axiom reports are from `#check @...` and
`#print axioms ...` after importing the seven modules in the pinned
checkout with Lean `v4.36.0` and Mathlib `fc4f59e577feb1a4956671bc04ac18aaaf8cd842`.

```text
PEqualNP.Library.L002 : ∀ (t t' : ℕ → ℕ), (∀ (n : ℕ), t n ≤ t' n) → PEqualNP.Library.DTIME t ⊆ PEqualNP.Library.DTIME t'
PEqualNP.Library.L003 : ∀ (L : Language Bool),
  L ∈ PEqualNP.Library.P ↔ ∃ p, L ∈ PEqualNP.Library.DTIME fun n => Polynomial.eval n p
PEqualNP.Library.L010 : PEqualNP.Library.P ⊆ PEqualNP.Library.NP
PEqualNP.Library.L016 : ∀ (L₁ L₂ : Language Bool),
  PEqualNP.Library.PolyTimeReducible L₁ L₂ → L₂ ∈ PEqualNP.Library.P → L₁ ∈ PEqualNP.Library.P
PEqualNP.Library.L029 : PEqualNP.Search.SAT ∈ PEqualNP.Library.NP
PEqualNP.Library.L031 : PEqualNP.Library.NPComplete PEqualNP.Search.SAT
PEqualNP.Library.Helpers.poly_le_monomial : ∀ (p : Polynomial ℕ),
  ∃ a d, ∀ (m : ℕ), 1 ≤ m → Polynomial.eval m p ≤ a * m ^ d
'PEqualNP.Library.L002' depends on axioms: [propext, Classical.choice, Quot.sound]
'PEqualNP.Library.L003' depends on axioms: [propext, Classical.choice, Quot.sound]
'PEqualNP.Library.L010' depends on axioms: [propext, Classical.choice, Quot.sound]
'PEqualNP.Library.L016' depends on axioms: [propext, Classical.choice, Quot.sound]
'PEqualNP.Library.L029' depends on axioms: [propext, Classical.choice, Quot.sound]
'PEqualNP.Library.L031' depends on axioms: [propext, Classical.choice, Quot.sound]
'PEqualNP.Library.Helpers.poly_le_monomial' depends on axioms: [propext, Classical.choice, Quot.sound]
```

`L029` constructs a polynomial-time SAT verifier. Its decision function
checks an encoding of the formula and bounded witness. The same result
supplies the membership half of `L031`. Its hardness half reduces an
arbitrary verifier to an encoded CNF computation tableau. The tableau
is satisfiable exactly when the compiled verifier accepts with a bounded
witness, and the reduction computes the encoded tableau in polynomial
time. This is Cook–Levin for the SAT predicate used in the goal.

The audit validates the Git object evidence below by hashing the raw
commit object, following its root tree to each imported source path,
and checking the hash of every tree and blob it uses. The expected
commit is the reference commit specified in the protected rules. The
audit reports the verified source texts, including their theorem bodies,
so examination of the direct imports can use their pinned bytes. This
checks those sources' identities. Lean elaboration and verification of
transitive axioms were done locally in the pinned reference.

## Lean reference result

The exact candidate and ladder statement were checked with this command
from the pinned reference checkout, using the matching Mathlib cache.

```text
node tools/check-lean.mjs lean/PEqualNP/Outside/P_ne_NP_iff_SAT_not_mem_DTIME.lean <statement-file> check
```

The statement file contained the exact rung 3 proposition from
`checkers/ladder.json`. The reference returned `ACCEPTED (check)` for
the theorem and rechecked 4,344 constants, reporting `propext`,
`Quot.sound`, and `Classical.choice` as its transitive axioms.

The checked Lean file SHA-256 is `9484e47a621fe42afd19b23a257fe51f2bc234f757c8f821d88c288261dbdd04`.

## Git object evidence

The object bodies below include unchanged source files copied from
brilliant-hq/pequalnp-proofs, distributed under the Apache License 2.0.
The dates and authorship in the raw commit apply to that repository.

```json git-objects
{
  "05cc995beb7c21c3b72d0eeb1b594bd3be6c962b": {
    "bytes": "aW1wb3J0IFBFcXVhbE5QLkxpYnJhcnkuTDAwNwppbXBvcnQgUEVxdWFsTlAuTGlicmFyeS5NYWNoaW5lcy5GaWx0ZXJNYXAKCi8tLSBQIGlzIGNvbnRhaW5lZCBpbiBOUDogdGhlIHZlcmlmaWVyIGlnbm9yZXMgdGhlIHdpdG5lc3MuIEl0IGtlZXBzIHRoZSBmaXJzdCBjb21wb25lbnQgb2YgdGhlCnBhaXIgYW5kIHJ1bnMgdGhlIGRlY2lkZXIgb24gaXQ7IHRoZSBlbXB0eSB3aXRuZXNzIGFsd2F5cyB3b3Jrcy4gLS8KdGhlb3JlbSBQRXF1YWxOUC5MaWJyYXJ5LkwwMTAgOiBQRXF1YWxOUC5MaWJyYXJ5LlAg4oqGIFBFcXVhbE5QLkxpYnJhcnkuTlAgOj0gYnkKICByaW50cm8gTCDin6hmLCBoZiwgaGPin6kKICByZWZpbmUg4p+oe3AgfCBwLjEg4oiIIEx9LCAwLCDin6hmdW4gcCA9PiBmIHAuMSwgZnVuIHAgPT4gaGYgcC4xLCA/X+KfqSwgZnVuIHggPT4gP1/in6kKICDCtyByZWZpbmUgUEVxdWFsTlAuTGlicmFyeS5MMDA3IF8gXyBfIF8gXyBfIF8gXyBfIChmdW4gcCA6IExpc3QgQm9vbCDDlyBMaXN0IEJvb2wgPT4gcC4xKSBmID9fIGhjCiAgICByZWZpbmUgUEVxdWFsTlAuTGlicmFyeS5NYWNoaW5lcy5maWx0ZXJNYXBfcG9seVRpbWUgXyBfIF8KICAgICAgKGZ1biBzIDogQm9vbCDiipUgQm9vbCA9PiBTdW0uZWxpbSBzb21lIChmdW4gXyA9PiBub25lKSBzKSA/XwogICAgcmludHJvIOKfqHgsIHfin6kKICAgIHNpbXAgW1BFcXVhbE5QLkxpYnJhcnkuZW5jb2RlUGFpciwgTGlzdC5maWx0ZXJNYXBfYXBwZW5kLCBMaXN0LmZpbHRlck1hcF9tYXBdCiAgwrcgZXhhY3Qg4p+oZnVuIGggPT4g4p+oW10sIGJ5IHNpbXAsIGjin6ksIGZ1biDin6hfLCBfLCBo4p+pID0+IGjin6kK",
    "type": "blob"
  },
  "364123c9dcfa1899438ad3b87670bb55f7c3ddae": {
    "bytes": "dHJlZSBkMGI3NTMzNDEwZmNiNTg5YzY3OWIxZjQ0Y2MyNDM0OTVjYmQ1YzY2CnBhcmVudCAxYTllY2ZmOTk1Y2I3NDU5ZjNkZGYyOTFiZWQwNzg4N2E0ODc2NzA5CmF1dGhvciBrLXNhbmRodSA8MjM1MTA4OTAray1zYW5kaHVAdXNlcnMubm9yZXBseS5naXRodWIuY29tPiAxNzk1NTAzNTM2IC0wNTAwCmNvbW1pdHRlciBHaXRIdWIgPG5vcmVwbHlAZ2l0aHViLmNvbT4gMTc5NTUwMzUzNiArMDIwMApncGdzaWcgLS0tLS1CRUdJTiBQR1AgU0lHTkFUVVJFLS0tLS0KIAogd3NGY0JBQUJDQUFRQlFKckJUV3dDUkMxYVE3dXU1VWhsQUFBOVo0UUFEL1N3VVBZWklyZTFuQm9MQVRJZzBKbwogRHQyc0dKUy9GUmcyY3pZTGxRVGRFMjJqREk3OGlIZFdxN040b2t6WkJ6OHdZaGwrYnl3Z1Jmbnlkcm9GZENYWAogaCt0VlIzamEyWW9VcjFFNWFhNUxLQ1NkVGxVazdkS1owSStZd0owVVRHYXJ6N0x3Z3p4dmtYWGFuazVLRGhjVwogN2Z4M2UxWHBRajhqL3MvRXJwcE5UTEU3VFE2NGEzdDZqbGpYOHBzRWlTcTVSbXN2ZStzdTFHUmxWNytsNllrKwogQ1ZyRFlZTFJrelBiQ3c1TndreUUwVXV4eDk4c0dFSkhDZ2h5YVJXcUxBMDdUUlJHeXpHb01rM2swZzJmNXRtcQogRlNVYUw5ZlRXMTVqbjFiUUMxeS95bEkwdnZ2QWp0U29sRW9EOC9SZ1A1L1hPY202c3ZYZ3lsME8wTDFOM1ZKdwogMVd1VEk1eHlVUEorenlTWlJDZjJwaUs1NHp3RThEUDc3RlNoTDE4WGw4dkVYRzI1QkZ2UUVkZjh4eGg1d080QgogWUFNdWp5UFJ0RlVJbmlJaXNsdE1CQzA1M1dJeDlGV3RLRGFPZWppTWdvQ3RWSWttNjNHcEJVQkVmK25id3BqeAogMDgrMlZDd2VIVXZZaWY2d3EyaElTZE9Nd1d4THZSZTJLSjRlOHFEVzYvTWJ3dzZtUEZLM2pBZklNT2xBQnpTNQogamJ2RmVLOHc1S0lkZXZ3bzMrK21CUzhQQjF3ZkJacE8vRnlLK0ljSWxWQ2R5MlhYc2pPb2FNajZhUk1ZdGNzZQogVTdEck9QZkhtbEFyOTVyZ21MUmh0bEpUWHBZUEwzZWF5TE1xWCtud0p5UHNqUXAydDkzYTlRZWRNRkdjQXpMRgogODViaDhBK2J0ZU0yeXRLSUFlNU8KID1SaXg2CiAtLS0tLUVORCBQR1AgU0lHTkFUVVJFLS0tLS0KIAoKUmVkdWNlIEwtbWV0YS0xNzQ5OiBzcGxpdCBQRygyLDMpIG5lc3RlZC1BTkQgY29yZSBpbnRvIGRlZ2VuZXJhdGUgZ2F0ZXMsIDEgbmVzdGVkIHBhaXIsIGFuZCAyKyBwYWlycyAoIzQwNTIp",
    "type": "commit"
  },
  "756573e98bf8fa5395739f527274d306cde8ddf5": {
    "bytes": "aW1wb3J0IFBFcXVhbE5QLkRlZnMKCi8tLSBEVElNRSBpcyBtb25vdG9uZSBpbiB0aGUgdGltZSBib3VuZC4gLS8KdGhlb3JlbSBQRXF1YWxOUC5MaWJyYXJ5LkwwMDIgOiDiiIAgdCB0JyA6IOKElSDihpIg4oSVLCAo4oiAIG4gOiDihJUsIHQgbiDiiaQgdCcgbikg4oaSCiAgICBQRXF1YWxOUC5MaWJyYXJ5LkRUSU1FIHQg4oqGIFBFcXVhbE5QLkxpYnJhcnkuRFRJTUUgdCcgOj0gYnkKICByaW50cm8gdCB0JyBoIEwg4p+oZiwgaGYsIGMsIGhj4p+pCiAgZXhhY3Qg4p+oZiwgaGYsIGMsIGZ1biBuID0+IChoYyBuKS50cmFucyAoaCBuKeKfqQo=",
    "type": "blob"
  },
  "7af05ade6b01dcc13774539fce4aff2cfb3d39b7": {
    "bytes": "MTAwNjQ0IENoZWNrTGVtbWEubGVhbgCsVvSsDU3QYOGlMqFaAfj04AR9xzEwMDY0NCBQRXF1YWxOUC5sZWFuAMt+EdRRDNX+bly6R47H4P1hH+4RNDAwMDAgUEVxdWFsTlAA8Z0VLNw3dmo2ykD2lLjwO9z48BQxMDA2NDQgbGFrZS1tYW5pZmVzdC5qc29uABWH/upuiZhr7nEjQVnsCNobk0m+MTAwNjQ0IGxha2VmaWxlLnRvbWwATQRIBO4ArfCLNtP0fcRinPs9X8UxMDA2NDQgbGVhbi10b29sY2hhaW4AAPhINZsc2vfBLNa3rMW0NkdS4VQ=",
    "type": "tree"
  },
  "83a76a561a6b58741496f59fe36c27283d1cffbd": {
    "bytes": "aW1wb3J0IFBFcXVhbE5QLkxpYnJhcnkuU2VhcmNoSGVscGVycy5TYXRWZXJpZmllckNQVAoKLy0tIFNBVCBpcyBpbiBOUC4gLS8KdGhlb3JlbSBQRXF1YWxOUC5MaWJyYXJ5LkwwMjkgOiBQRXF1YWxOUC5TZWFyY2guU0FUIOKIiCBQRXF1YWxOUC5MaWJyYXJ5Lk5QIDo9CiAgUEVxdWFsTlAuTGlicmFyeS5TZWFyY2hIZWxwZXJzLlNhdFYuU0FUX2luX05QX29mIFBFcXVhbE5QLkxpYnJhcnkuU2VhcmNoSGVscGVycy5TYXRWLmNwdF9TVgo=",
    "type": "blob"
  },
  "8ae5b9145c4c9763d726626ecfc09a058a84751e": {
    "bytes": "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",
    "type": "tree"
  },
  "8cef0786a928d3c8a28ab86b8b08918b844a5a54": {
    "bytes": "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",
    "type": "tree"
  },
  "8e179aebef27be2b29a8988c320da55f54c77694": {
    "bytes": "aW1wb3J0IFBFcXVhbE5QLkxpYnJhcnkuTWFjaGluZXMuUnVuCmltcG9ydCBNYXRobGliLkFuYWx5c2lzLlNwZWNpZmljTGltaXRzLk5vcm1lZAoKLy0hCiMgVGhlIG91dHB1dCBvZiBhIHBvbHlub21pYWwtdGltZSBmdW5jdGlvbiBpcyBwb2x5bm9taWFsbHkgbG9uZwoKSGVscGVyIG1vZHVsZSAocHJvb2ZzIG9ubHksIG5vIHN0YXRlbWVudCBtYXkgdXNlIGl0KS4gQSBzdGFjayBncm93cyBieSBhIGJvdW5kZWQgbnVtYmVyIG9mCnN5bWJvbHMgcGVyIHN0ZXAsIHNvIHRoZSBvdXRwdXQgb2YgYSBwb2x5bm9taWFsLXRpbWUgZnVuY3Rpb24gb24gc3RyaW5ncyBpcyBhdCBtb3N0IGEgbW9ub21pYWwKaW4gdGhlIGlucHV0IGxlbmd0aC4gQXBwbGllZCB0byB0aGUgYmluYXJ5IGVuY29kaW5nIG9mIENORiBmb3JtdWxhczogYSBmb3JtdWxhIG5hbWluZyB0aGUKdmFyaWFibGUgYDIgXiBuYCBoYXMgYSBzaG9ydCBjb2RlLCBzbyBubyBwb2x5bm9taWFsLXRpbWUgZnVuY3Rpb24gY2FuIG91dHB1dCBhbiBhc3NpZ25tZW50IGFzCmEgbGlzdCBpbmRleGVkIGJ5IHZhcmlhYmxlIG51bWJlci4KLS8KCm5hbWVzcGFjZSBQRXF1YWxOUC5MaWJyYXJ5LkhlbHBlcnMKb3BlbiBUdXJpbmcgUEVxdWFsTlAuTGlicmFyeSBQRXF1YWxOUC5MaWJyYXJ5Lk1hY2hpbmVzCgovLS0gQSBwb2x5bm9taWFsIHdpdGggbmF0dXJhbCBjb2VmZmljaWVudHMgaXMgYmVsb3cgYSBtb25vbWlhbCBmcm9tIDEgb24uIC0vCnRoZW9yZW0gcG9seV9sZV9tb25vbWlhbCAocCA6IFBvbHlub21pYWwg4oSVKSA6IOKIgyBhIGQgOiDihJUsIOKIgCBtIDog4oSVLCAxIOKJpCBtIOKGkiBwLmV2YWwgbSDiiaQgYSAqIG0gXiBkIDo9IGJ5CiAgaW5kdWN0aW9uIHAgdXNpbmcgUG9seW5vbWlhbC5pbmR1Y3Rpb25fb24nIHdpdGgKICB8IGFkZCBwIHEgaHAgaHEgPT4KICAgIG9idGFpbiDin6hhLCBkLCBo4p+pIDo9IGhwCiAgICBvYnRhaW4g4p+oYiwgZSwgaCfin6kgOj0gaHEKICAgIHJlZmluZSDin6hhICsgYiwgZCArIGUsIGZ1biBtIGhtID0+ID9f4p+pCiAgICBydyBbUG9seW5vbWlhbC5ldmFsX2FkZCwgTmF0LmFkZF9tdWxdCiAgICBoYXZlIGgxIDogbSBeIGQg4omkIG0gXiAoZCArIGUpIDo9IE5hdC5wb3dfbGVfcG93X3JpZ2h0IGhtIChieSBvbWVnYSkKICAgIGhhdmUgaDIgOiBtIF4gZSDiiaQgbSBeIChkICsgZSkgOj0gTmF0LnBvd19sZV9wb3dfcmlnaHQgaG0gKGJ5IG9tZWdhKQogICAgZXhhY3QgYWRkX2xlX2FkZCAoKGggbSBobSkudHJhbnMgKE5hdC5tdWxfbGVfbXVsX2xlZnQgXyBoMSkpCiAgICAgICgoaCcgbSBobSkudHJhbnMgKE5hdC5tdWxfbGVfbXVsX2xlZnQgXyBoMikpCiAgfCBtb25vbWlhbCBkIGMgPT4gZXhhY3Qg4p+oYywgZCwgZnVuIG0gXyA9PiBieSBydyBbUG9seW5vbWlhbC5ldmFsX21vbm9taWFsXeKfqQoKLy0tIEFuIGV4cG9uZW50aWFsIGJlYXRzIGEgbW9ub21pYWwgc29tZXdoZXJlIGFib3ZlIGFueSB0aHJlc2hvbGQuIC0vCnRoZW9yZW0gZXhpc3RzX3Bvd19sdCAoQSBEIE4gOiDihJUpIDog4oiDIG4gOiDihJUsIE4g4omkIG4g4oinIEEgKiBuIF4gRCA8IDIgXiBuIDo9IGJ5CiAgaGF2ZSBoIDo9IHRlbmRzdG9fcG93X2NvbnN0X2Rpdl9jb25zdF9wb3dfb2Zfb25lX2x0IEQgKHNob3cgKDEgOiDihJ0pIDwgMiBieSBub3JtX251bSkKICBoYXZlIGhwb3MgOiAoMCA6IOKEnSkgPCAxIC8gKEEgKyAxKSA6PSBieSBwb3NpdGl2aXR5CiAgaGF2ZSBldiA6PSAoaC5ldmVudHVhbGx5IChndF9tZW1fbmhkcyBocG9zKSkuYW5kIChGaWx0ZXIuZXZlbnR1YWxseV9nZV9hdFRvcCBOKQogIG9idGFpbiDin6huLCBobiwgaE7in6kgOj0gZXYuZXhpc3RzCiAgcmVmaW5lIOKfqG4sIGhOLCA/X+KfqQogIGhhdmUgaDIgOiAoMCA6IOKEnSkgPCAyIF4gbiA6PSBieSBwb3NpdGl2aXR5CiAgcncgW2Rpdl9sdF9kaXZfaWZm4oKAIGgyIChieSBwb3NpdGl2aXR5KV0gYXQgaG4KICBoYXZlIDogKChBICogbiBeIEQgOiDihJUpIDog4oSdKSA8ICgoMiBeIG4gOiDihJUpIDog4oSdKSA6PSBieQogICAgcHVzaF9jYXN0CiAgICBoYXZlIGhubiA6ICgwIDog4oSdKSDiiaQgKG4gOiDihJ0pIF4gRCA6PSBieSBwb3NpdGl2aXR5CiAgICBubGluYXJpdGgKICBleGFjdF9tb2RfY2FzdCB0aGlzCgovLS0gVGhlIG91dHB1dCBvZiBhIHBvbHlub21pYWwtdGltZSBmdW5jdGlvbiBvbiBzdHJpbmdzIGlzIGF0IG1vc3QgYSBtb25vbWlhbCBpbiB0aGUgaW5wdXQKbGVuZ3RoIChmb3Igbm9uZW1wdHkgaW5wdXRzKS4gLS8KdGhlb3JlbSBvdXRwdXRfbGVuZ3RoX2xlIChmIDogTGlzdCBCb29sIOKGkiBMaXN0IEJvb2wpCiAgICAoaGYgOiBDb21wdXRhYmxlSW5Qb2x5VGltZSAoZnVuIHggOiBMaXN0IEJvb2wgPT4geCkgKGZ1biB4IDogTGlzdCBCb29sID0+IHgpIGYpIDoKICAgIOKIgyBhIGQgOiDihJUsIOKIgCB4IDogTGlzdCBCb29sLCAxIOKJpCB4Lmxlbmd0aCDihpIgKGYgeCkubGVuZ3RoIOKJpCBhICogeC5sZW5ndGggXiBkIDo9IGJ5CiAgb2J0YWluIOKfqGPin6kgOj0gaGYKICBvYnRhaW4g4p+oYSwgZCwgaGFk4p+pIDo9IHBvbHlfbGVfbW9ub21pYWwgYy50aW1lCiAgcmVmaW5lIOKfqDEgKyBtYXhQdXNoIGMudG0gKiBhLCBkICsgMSwgZnVuIHggaHggPT4gP1/in6kKICBvYnRhaW4g4p+o4p+oc3RlcHMsIGhlduKfqSwgaGxl4p+pIDo9IGMub3V0cHV0c0Z1biB4CiAgaGF2ZSBoZXYnIDogKGZsaXAgYmluZCAoVE0yLnN0ZXAgYy50bS5tKSleW3N0ZXBzXQogICAgICAoc29tZSAo4p+oc29tZSBjLnRtLm1haW4sIGMudG0uaW5pdGlhbFN0YXRlLCBGdW5jdGlvbi51cGRhdGUgKGZ1biBfID0+IFtdKSBjLnRtLmvigoAKICAgICAgICAoTGlzdC5tYXAgYy5pbnB1dEFscGhhYmV0LmludkZ1biB4KeKfqSA6IFRNMi5DZmcgYy50bS7OkyBjLnRtLs6bIGMudG0uz4MpKSA9CiAgICAgIHNvbWUgKOKfqG5vbmUsIGMudG0uaW5pdGlhbFN0YXRlLCBGdW5jdGlvbi51cGRhdGUgKGZ1biBfID0+IFtdKSBjLnRtLmvigoEKICAgICAgICAoTGlzdC5tYXAgYy5vdXRwdXRBbHBoYWJldC5pbnZGdW4gKGYgeCkp4p+pIDogVE0yLkNmZyBjLnRtLs6TIGMudG0uzpsgYy50bS7PgykgOj0gYnkKICAgIHJ3IFvihpAgaW5pdExpc3RfZXEsIOKGkCBoYWx0TGlzdF9lcV07IGV4YWN0IGhldgogIGhhdmUga2V5IDo9IHJ1bl9sZW5ndGggYy50bSBjLnRtLmvigoEgc3RlcHMgXyBfIGhldicKICBzaW1wIG9ubHkgW0Z1bmN0aW9uLnVwZGF0ZV9zZWxmLCBMaXN0Lmxlbmd0aF9tYXBdIGF0IGtleQogIGhhdmUgaGluIDogKChGdW5jdGlvbi51cGRhdGUgKGZ1biBfID0+IChbXSA6IExpc3QgXykpIGMudG0ua+KCgAogICAgICAoTGlzdC5tYXAgYy5pbnB1dEFscGhhYmV0LmludkZ1biB4KSA6IOKIgCBrLCBMaXN0IChjLnRtLs6TIGspKSBjLnRtLmvigoEpLmxlbmd0aCDiiaQgeC5sZW5ndGggOj0gYnkKICAgIGJ5X2Nhc2VzIGhrIDogYy50bS5r4oKBID0gYy50bS5r4oKACiAgICDCtyBydyBbaGtdOyBzaW1wCiAgICDCtyBydyBbRnVuY3Rpb24udXBkYXRlX29mX25lIGhrXTsgc2ltcAogIGhhdmUgaHN0ZXBzIDogc3RlcHMg4omkIGEgKiB4Lmxlbmd0aCBeIGQgOj0gaGxlLnRyYW5zIChoYWQgXyBoeCkKICBoYXZlIGgxIDogeC5sZW5ndGgg4omkIHgubGVuZ3RoIF4gKGQgKyAxKSA6PSBieQogICAgY2FsYyB4Lmxlbmd0aCA9IHgubGVuZ3RoIF4gMSA6PSAocG93X29uZSBfKS5zeW1tCiAgICAgIF8g4omkIHgubGVuZ3RoIF4gKGQgKyAxKSA6PSBOYXQucG93X2xlX3Bvd19yaWdodCBoeCAoYnkgb21lZ2EpCiAgaGF2ZSBoMiA6IHgubGVuZ3RoIF4gZCDiiaQgeC5sZW5ndGggXiAoZCArIDEpIDo9IE5hdC5wb3dfbGVfcG93X3JpZ2h0IGh4IChieSBvbWVnYSkKICBjYWxjIChmIHgpLmxlbmd0aCDiiaQgeC5sZW5ndGggKyBtYXhQdXNoIGMudG0gKiBzdGVwcyA6PSBrZXkudHJhbnMgKGJ5IG9tZWdhKQogICAgXyDiiaQgeC5sZW5ndGggXiAoZCArIDEpICsgbWF4UHVzaCBjLnRtICogKGEgKiB4Lmxlbmd0aCBeIChkICsgMSkpIDo9CiAgICAgIGFkZF9sZV9hZGQgaDEgKE5hdC5tdWxfbGVfbXVsX2xlZnQgXyAoaHN0ZXBzLnRyYW5zIChOYXQubXVsX2xlX211bF9sZWZ0IF8gaDIpKSkKICAgIF8gPSAoMSArIG1heFB1c2ggYy50bSAqIGEpICogeC5sZW5ndGggXiAoZCArIDEpIDo9IGJ5IHJpbmcKCm9wZW4gUEVxdWFsTlAuU2VhcmNoIGluCnRoZW9yZW0gY29kZV9sZW5ndGggKG4gOiDihJUpIDogKGVuY29kZUNORiBbWygyIF4gbiwgdHJ1ZSldXSkubGVuZ3RoID0gMiAqIG4gKyA4IDo9IGJ5CiAgaGF2ZSBoYiA6IOKIgCBicyA6IExpc3QgQm9vbCwgKGJzLmZsYXRNYXAgZnVuIGQgPT4gW3RydWUsIGRdKS5sZW5ndGggPSAyICogYnMubGVuZ3RoIDo9IGJ5CiAgICBpbnRybyBiczsgaW5kdWN0aW9uIGJzIHdpdGgKICAgIHwgbmlsID0+IHJmbAogICAgfCBjb25zIGIgYnMgaWggPT4gc2ltcCBvbmx5IFtMaXN0LmZsYXRNYXBfY29ucywgTGlzdC5sZW5ndGhfYXBwZW5kLCBpaCwgTGlzdC5sZW5ndGhfY29ucywgTGlzdC5sZW5ndGhfbmlsXTsgb21lZ2EKICBoYXZlIGhzIDogKDIgXiBuKS5iaXRzLmxlbmd0aCA9IG4gKyAxIDo9IGJ5CiAgICBydyBbTmF0LnNpemVfZXFfYml0c19sZW4sIE5hdC5zaXplX3Bvd10KICBzaW1wIFtlbmNvZGVDTkYsIGVuY29kZUNsYXVzZSwgZW5jb2RlTGl0ZXJhbCwgaGIsIGhzXQogIG9tZWdhCgpvcGVuIFBFcXVhbE5QLlNlYXJjaCBpbgovLS0gTm8gcG9seW5vbWlhbC10aW1lIGZ1bmN0aW9uIG91dHB1dHMgc2F0aXNmeWluZyBhc3NpZ25tZW50cyBpbmRleGVkIGJ5IHZhcmlhYmxlIG51bWJlci4gLS8KdGhlb3JlbSBub19pbmRleGVkX2Fzc2lnbm1lbnQgOiDCrCDiiIMgZiA6IExpc3QgQm9vbCDihpIgTGlzdCBCb29sLAogICAgQ29tcHV0YWJsZUluUG9seVRpbWUgKGZ1biB4IDogTGlzdCBCb29sID0+IHgpIChmdW4geCA6IExpc3QgQm9vbCA9PiB4KSBmIOKIpwogICAgICDiiIAgz4YgOiBDTkYsIFNhdGlzZmlhYmxlIM+GIOKGkgogICAgICAgIENORi5ldmFsIChmdW4gaSA6IOKElSA9PiAoZiAoZW5jb2RlQ05GIM+GKSkuZ2V0RCBpIGZhbHNlKSDPhiA9IHRydWUgOj0gYnkKICByaW50cm8g4p+oZiwgaGYsIGjin6kKICBvYnRhaW4g4p+oYSwgZCwgaGxlbuKfqSA6PSBvdXRwdXRfbGVuZ3RoX2xlIGYgaGYKICBvYnRhaW4g4p+obiwgaG44LCBobuKfqSA6PSBleGlzdHNfcG93X2x0IChhICogMyBeIGQpIGQgOAogIGhhdmUgaHNhdCA6IFNhdGlzZmlhYmxlIFtbKDIgXiBuLCB0cnVlKV1dIDo9CiAgICDin6hmdW4gXyA9PiB0cnVlLCBieSBzaW1wIFtDTkYuZXZhbCwgQ2xhdXNlLmV2YWwsIExpdGVyYWwuZXZhbF3in6kKICBoYXZlIGh2IDo9IGggXyBoc2F0CiAgc2ltcCBvbmx5IFtDTkYuZXZhbCwgQ2xhdXNlLmV2YWwsIExpdGVyYWwuZXZhbCwgTGlzdC5hbGxfY29ucywgTGlzdC5hbGxfbmlsLCBMaXN0LmFueV9jb25zLAogICAgTGlzdC5hbnlfbmlsLCBCb29sLm9yX2ZhbHNlLCBCb29sLmFuZF90cnVlLCBiZXFfaWZmX2VxXSBhdCBodgogIGhhdmUgaGx0IDogMiBeIG4gPCAoZiAoZW5jb2RlQ05GIFtbKDIgXiBuLCB0cnVlKV1dKSkubGVuZ3RoIDo9IGJ5CiAgICBieV9jb250cmEgaGdlCiAgICBydyBbTGlzdC5nZXREX2VxX2RlZmF1bHQgXyBfIChub3RfbHQubXAgaGdlKV0gYXQgaHYKICAgIGV4YWN0IEJvb2wuZmFsc2VfbmVfdHJ1ZSBodgogIGhhdmUgaGIgOj0gaGxlbiAoZW5jb2RlQ05GIFtbKDIgXiBuLCB0cnVlKV1dKSAoYnkgcncgW2NvZGVfbGVuZ3RoXTsgb21lZ2EpCiAgcncgW2NvZGVfbGVuZ3RoXSBhdCBoYgogIGhhdmUgaDMgOiAoMiAqIG4gKyA4KSBeIGQg4omkICgzICogbikgXiBkIDo9IE5hdC5wb3dfbGVfcG93X2xlZnQgKGJ5IG9tZWdhKSBkCiAgaGF2ZSA6IGEgKiAoMiAqIG4gKyA4KSBeIGQg4omkIGEgKiAzIF4gZCAqIG4gXiBkIDo9IGJ5CiAgICBjYWxjIGEgKiAoMiAqIG4gKyA4KSBeIGQg4omkIGEgKiAoMyAqIG4pIF4gZCA6PSBOYXQubXVsX2xlX211bF9sZWZ0IF8gaDMKICAgICAgXyA9IGEgKiAzIF4gZCAqIG4gXiBkIDo9IGJ5IHJ3IFtOYXQubXVsX3BvdywgTmF0Lm11bF9hc3NvY10KICBvbWVnYQplbmQgUEVxdWFsTlAuTGlicmFyeS5IZWxwZXJzCg==",
    "type": "blob"
  },
  "d0b7533410fcb589c679b1f44cc243495cbd5c66": {
    "bytes": "NDAwMDAgLmdpdGh1YgC3zOzJfEEog+jLIdrHvqV06TypzTEwMDY0NCAuZ2l0aWdub3JlANzJH2iKhyliDV9ixOaebwwBRDV0MTAwNjQ0IENPTlRSSUJVVElORy5tZACm99jTLNx0B4y4UEO1hcT70BRcyjEwMDY0NCBMSUNFTlNFANZFaVZzNJ45R+jlrkIzLQrDFkzXMTAwNjQ0IFJFQURNRS5tZABSExOIlGf3IEmVRetvQ7tmAjhWUzQwMDAwIGxlYW4AevBa3msB3ME3dFOfzkr/LPs9Obc0MDAwMCBub3RlcwBiGs6dnd8u7P0o/mFtgDLdDGnx7zQwMDAwIHRvb2xzAOPTOz7JXOgcA2l8I0UL4wpsdauj",
    "type": "tree"
  },
  "d201e51a626afcf1065705fa9472e1f4bb24532b": {
    "bytes": "aW1wb3J0IFBFcXVhbE5QLkRlZnMKCi8tLSBQIGlzIHRoZSB1bmlvbiBvZiBEVElNRSBvdmVyIHBvbHlub21pYWwgYm91bmRzLiAtLwp0aGVvcmVtIFBFcXVhbE5QLkxpYnJhcnkuTDAwMyA6IOKIgCBMIDogTGFuZ3VhZ2UgQm9vbCwgTCDiiIggUEVxdWFsTlAuTGlicmFyeS5QIOKGlAogICAg4oiDIHAgOiBQb2x5bm9taWFsIOKElSwgTCDiiIggUEVxdWFsTlAuTGlicmFyeS5EVElNRSAoZnVuIG4gOiDihJUgPT4gUG9seW5vbWlhbC5ldmFsIG4gcCkgOj0gYnkKICBpbnRybyBMCiAgY29uc3RydWN0b3IKICDCtyByaW50cm8g4p+oZiwgaGYsIOKfqGPin6nin6kKICAgIGV4YWN0IOKfqGMudGltZSwgZiwgaGYsIGMudG9UTTJDb21wdXRhYmxlSW5UaW1lLCBmdW4gbiA9PiBsZV9yZmzin6kKICDCtyByaW50cm8g4p+ocCwgZiwgaGYsIGMsIGhj4p+pCiAgICByZWZpbmUg4p+oZiwgaGYsIOKfqOKfqGMudG9UTTJDb21wdXRhYmxlQXV4LCBwLCBmdW4gYSA9PiA/X+KfqeKfqeKfqQogICAgZXhhY3Qg4p+oKGMub3V0cHV0c0Z1biBhKS50b0V2YWxzVG8sIChjLm91dHB1dHNGdW4gYSkuc3RlcHNfbGVfbS50cmFucyAoaGMgXynin6kK",
    "type": "blob"
  },
  "ddd7b49e03ac769108b6e6384422b8fc04fb98e3": {
    "bytes": "aW1wb3J0IFBFcXVhbE5QLkxpYnJhcnkuU2VhcmNoSGVscGVycy5UYWJsZWF1U291bmQKaW1wb3J0IFBFcXVhbE5QLkxpYnJhcnkuU2VhcmNoSGVscGVycy5UYWJsZWF1Q29tcGxldGUKaW1wb3J0IFBFcXVhbE5QLkxpYnJhcnkuU2VhcmNoSGVscGVycy5UYWJsZWF1U3RlcENQVAppbXBvcnQgUEVxdWFsTlAuTGlicmFyeS5TZWFyY2hIZWxwZXJzLlRhYmxlYXVFZGdlQ1BUCmltcG9ydCBQRXF1YWxOUC5MaWJyYXJ5LlNlYXJjaEhlbHBlcnMuVGFibGVhdUFzc2VtYmx5CgovLS0gU0FUIGlzIE5QLWNvbXBsZXRlIChDb29rIDE5NzEsIExldmluIDE5NzMpLiBTQVQgaXMgaW4gTlAgKEwtbGliLTAyOSkuIEZvciBoYXJkbmVzcywgYW4gTlAKdmVyaWZpZXIgY29tcGlsZXMgdG8gYSBtaWNyby1pbnN0cnVjdGlvbiBjb2RlOyB0aGUgaW5wdXQgaXMgbWFwcGVkIHRvIHRoZSBlbmNvZGluZyBvZiB0aGUgdGFibGVhdQpmb3JtdWxhIG9mIHRoYXQgY29kZSwgd2hpY2ggaXMgc2F0aXNmaWFibGUgZXhhY3RseSB3aGVuIHNvbWUgd2l0bmVzcyBtYWtlcyB0aGUgY29kZSBhY2NlcHQsIGFuZAp3aG9zZSBlbmNvZGluZyBpcyB3cml0dGVuIGluIHBvbHlub21pYWwgdGltZS4gLS8KdGhlb3JlbSBQRXF1YWxOUC5MaWJyYXJ5LkwwMzEgOiBQRXF1YWxOUC5MaWJyYXJ5Lk5QQ29tcGxldGUgUEVxdWFsTlAuU2VhcmNoLlNBVCA6PQogIFBFcXVhbE5QLkxpYnJhcnkuU2VhcmNoSGVscGVycy5UYWIubnBDb21wbGV0ZV9TQVRfb2YKICAgIChmdW4gYyB6cyBtIFQgaHogaCA9PiBQRXF1YWxOUC5MaWJyYXJ5LlNlYXJjaEhlbHBlcnMuVGFiLmFjY2VwdHNfb2Zfc2F0IGMgenMgbSBUIGh6IGgpCiAgICAoZnVuIGMgenMgbSBUIGh6IHcgaHcgaCA9PiBQRXF1YWxOUC5MaWJyYXJ5LlNlYXJjaEhlbHBlcnMuVGFiLnNhdF9vZl9hY2NlcHRzIGMgenMgbSBUIGh6IHcgaHcgaCkKICAgIChmdW4gYyBwIHEgPT4gUEVxdWFsTlAuTGlicmFyeS5TZWFyY2hIZWxwZXJzLlRhYi5jcHRfdGFibGVhdV9vZiBjIHAgcQogICAgICAoUEVxdWFsTlAuTGlicmFyeS5TZWFyY2hIZWxwZXJzLlRhYi5jcHRfc3RlcFBhcnQgYyBwIHEpKQo=",
    "type": "blob"
  },
  "f19d152cdc37766a36ca40f694b8f03bdcf8f014": {
    "bytes": "NDAwMDAgQ2lyY3VpdExvd2VyQm91bmRzAH4wlAW6j4SzymYjbzx+XcB7xFrhMTAwNjQ0IERlZnMubGVhbgAfnatmW4f107ORbo3/zL5c2jVxZTQwMDAwIERlZnMAhG4ZCBttZiVuZumtbwGJx8YBRKg0MDAwMCBHY3QAnFwY+ToVbhFJvtXeu/jvZz5rI6I0MDAwMCBMaWJyYXJ5AIrluRRcTJdj1yZibs/AmgWKhHUeNDAwMDAgTWV0YUNvbXBsZXhpdHkAU6DOCtFEYlBeIWCRJzYTSPGSQPQ0MDAwMCBPdXRzaWRlAFqy/k0kLgxtV1vEf6Z4tF00bOyFNDAwMDAgUHJvb2ZDb21wbGV4aXR5AHfoZki7GjtDHthQw+pl5zrlh2fDNDAwMDAgU2VhcmNoAOVJTNCteKTBTdzgjN1hBv8AkaYs",
    "type": "tree"
  },
  "f8e9001bf5fe48dc432c1e087b97f4f7eaae9ef1": {
    "bytes": "aW1wb3J0IFBFcXVhbE5QLkxpYnJhcnkuTDAwNwoKLy0tIFAgaXMgY2xvc2VkIHVuZGVyIHBvbHlub21pYWwtdGltZSByZWR1Y3Rpb25zOiBydW4gdGhlIHJlZHVjdGlvbiwgdGhlbiB0aGUgZGVjaWRlci4gLS8KdGhlb3JlbSBQRXF1YWxOUC5MaWJyYXJ5LkwwMTYgOiDiiIAgTOKCgSBM4oKCIDogTGFuZ3VhZ2UgQm9vbCwKICAgIFBFcXVhbE5QLkxpYnJhcnkuUG9seVRpbWVSZWR1Y2libGUgTOKCgSBM4oKCIOKGkiBM4oKCIOKIiCBQRXF1YWxOUC5MaWJyYXJ5LlAg4oaSCiAgICBM4oKBIOKIiCBQRXF1YWxOUC5MaWJyYXJ5LlAgOj0KICBmdW4gXyBfIOKfqGYsIGhmLCBoZifin6kg4p+oZywgaGcsIGhnJ+KfqSA9PgogICAg4p+oZnVuIHggPT4gZyAoZiB4KSwgZnVuIHggPT4gKGhmJyB4KS50cmFucyAoaGcgKGYgeCkpLAogICAgICBQRXF1YWxOUC5MaWJyYXJ5LkwwMDcgXyBfIF8gXyBfIF8gXyBfIF8gZiBnIGhmIGhnJ+KfqQo=",
    "type": "blob"
  }
}
```

## Reference source license

```text

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```
