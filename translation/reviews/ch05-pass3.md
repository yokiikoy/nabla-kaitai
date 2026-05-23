# Pass 3 Review: Chapter 5

Review date: 2026-05-22
Branch: `ai/english-translation-ch05`
File: `manuscript/en/ch05/ch05.md`

Pass 3 scope: authorial voice, note handling, publication polish. Minimal edits only.

---

## Decisions

### 1. Chapter title and § headings

Decision: **maintain**; Pass 2 aligned §5.2, §5.3, §5.8 with TOC.

### 2. "Mismatch" (ズレ) metaphor

Decision: **keep** throughout §5.2–§5.4 and checkpoints.

Reason: Central pedagogical term for this chapter; do not replace with "curl" prematurely.

### 3. Tiny-loop dissection (§5.3)

Decision: **keep** full $xy$-plane rectangle calculation.

Reason: Geometric origin of $d\omega$; matches Japanese emphasis.

### 4. Kelvin–Stokes naming (§5.6)

Decision: **keep** "Kelvin–Stokes theorem (also called simply Stokes' theorem)."

Reason: Source distinction; English readers benefit.

### 5. EM examples (§5.10.2)

Decision: **keep** form-degree table and localization walkthrough; defer details to Appendix C.

Reason: Architecture matches Japanese; avoids duplicating Appendix C in body.

### 6. Hodge star foreshadow (§5.11)

Decision: **keep** conceptual only; no $\ast$ correspondence formulas.

Reason: Matches preview policy from YAML/recap and ch04 close.

### 7. Appendices B and C

Decision: **keep** in `ch05.md` (not split); full matrix and EM component expansions.

Reason: Japanese source structure; B parallels ch02 Appendix A pattern.

### 8. Minor edits (Pass 2)

| Location | Change | Reason |
|----------|--------|--------|
| §5.10+ | `Stokes's` → `Stokes'` | Apostrophe consistency |
| §5.2–§5.3, §5.8 | Heading TOC alignment | Publication |

### 9. No change

- Leibniz rule derivation (§5.5.2).
- $27$-component $d\eta$ exposition (Appendix B.4.1).
- Chapter 5 end checkpoint length.

---

# Overall Chapter 5 Pass 3 Result

**Chapter 5 passes Pass 3** on `ai/english-translation-ch05`.

English Chapter 5 is **Pass 1 + Pass 2 + Pass 3 complete**.

Next: PR with base `ai/english-translation-ch04`; begin Chapter 6.
