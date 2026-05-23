# Japanese Backport Wave 4 — Close-Reading Structural Fixes

Issue: [#193](https://github.com/yokiikoy/nabla-kaitai/issues/193)
Branch: `edit/ja-backport-wave4`
Source report: `translation/reviews/ja-backport-candidates-from-en-close-reading.md`

## Policy (applied)

- No broad Japanese prose rewrite.
- No English-only polish backported.
- Japanese authorial voice preserved (`rot`, 方法①/②, FAQ tone, asides).
- Only notation, type safety, evaluation points, and chapter-structure references touched.

---

## Applied candidate IDs

| ID | File | Summary |
|----|------|---------|
| **JA-BP-001** | `manuscript/ja/ch03/ch03.md` | `dx/dt`, `dy/dt`, `dz/dt` → `x'(t)`, `y'(t)`, `z'(t)` in §3.3.1, §3.4.1; finite ratios `Δx_i/Δt` kept as ratios |
| **JA-BP-002** | `manuscript/ja/ch03/ch03.md` | Riemann sum uses explicit `ω_{γ(t_i)}` and `P(γ(t))` evaluation in limit line |
| **JA-BP-003** | `manuscript/ja/ch03/ch03.md` | §3.2.2 main sentence tightened to 「一次の変化を読み取る」 |
| **JA-BP-004** | `manuscript/ja/ch04/ch04.md` | `dγ/dt`, `dx/dt`, `dθ/dt` → `x'(t)`, `θ'(t)` etc. in pullback / summary contexts; **`dv/dt` preserved** in work–energy |
| **JA-BP-020** | `manuscript/ja/ch08/ch08.md` | §8.1.1: clarify `d` acts on 測定器側, not arrow fields; checkpoint and §8.6.2 「方法①——測定器側を変える」 aligned |
| **JA-BP-025** | `manuscript/ja/ch10/ch10.md` | §10.5 main text: `\ast_4F=dt∧(\mathbf{B}^T g_3)+∗_3(\mathbf{E}^T g_3)` with flat-notation note; downstream `d_4(∗_4F)` equations updated consistently |
| **JA-BP-034** | `manuscript/ja/ch12/ch12.md` | §12.2.2: wedge/cross identification note — デカルト右手系 / 第2章向き付き面積規約 |
| **JA-BP-035** | `manuscript/ja/ch12/ch12.md` | §12.3.1: `d\mathbf{A}` → 対応する 1-form `α` に `d` を作用 → `dα` |
| **JA-BP-040** | `manuscript/ja/references.md` | Burke comment: 「第5章まで」→ 第6章で計量・ホッジ・スターを導入するまでの構成 |
| **JA-BP-041** | `manuscript/ja/appendix.md` | FAQ: 第I部（第1章〜第4章）で外積、第5章で `d`、第6章で内積（計量） |

---

## Checked but not applied (representative)

| ID | Reason |
|----|--------|
| JA-BP-005 | ch04 signed `J` vs `\|J\|` already explicit — no edit |
| JA-BP-006 | English-only “differential coefficient” — JA uses 偏微分係数 (fine) |
| JA-BP-007 | **Preserve D** — JA 「方法①/②」 intentional |
| JA-BP-008–009 | ch05 cosmetic / fragment — not in scope files; not found |
| JA-BP-010–011 | ch05 appendix B — already adequate in JA |
| JA-BP-012 | **Preserve D** — concrete `d²=0` narrative |
| JA-BP-013–019 | ch06–07 — out of required file list; no parallel issue found in scoped files |
| JA-BP-021–024 | ch09–10 EN polish — not structural JA issues in scoped edits |
| JA-BP-026–033 | ch10–11 B items — Maxwell appendix F already defines `B` as spatial 2-form; `\ast_3B=B_x dx+…` **kept in 付録F** (type-safe there) |
| JA-BP-036–039 | ch12 / backmatter — LLM note, history, voice items **preserved** |
| JA-BP-042+ | C-category English polish — excluded |

---

## Preserved D items (explicit)

- `rot` notation throughout (intentional JA choice vs EN `curl`)
- 方法①/② terminology (not EN “Route”)
- Author asides, gatekeeping notes, LLM afterword (untouched)
- Concrete calculation route for `d²=0` in ch05 (untouched)
- Appendix F `\ast_3B=B_x\,dx+…` where `B` is defined as spatial magnetic **2-form** (F.1)

---

## Files changed

```
manuscript/ja/appendix.md
manuscript/ja/ch03/ch03.md
manuscript/ja/ch04/ch04.md
manuscript/ja/ch08/ch08.md
manuscript/ja/ch10/ch10.md
manuscript/ja/ch12/ch12.md
manuscript/ja/references.md
translation/reviews/ja-backport-wave4.md
translation/progress.md
```

(+7 manuscript files, +2 translation tracking files)

---

## Search results (issue checklist)

Target scope: required JA files only.

| Pattern | Result |
|---------|--------|
| `Chapter 5 §8.8` | no matches |
| `\ast_3B=B_x` | **1 match** — `ch10/ch10.md:1247` (付録F; `B` is spatial 2-form — intentional) |
| `\ast_3 B = B_x` | no matches |
| `B_x\,dx+B_y\,dy+B_z\,dz` | no matches in scoped files (appendix F uses `\ast_3B=B_x…` form) |
| `through Chapter 5` | no matches |
| `第5章まで` | no matches (fixed in references.md) |
| `lay row vectors` / `row vectors on their sides` | no matches |
| `East Asian students…` / `passed entrance-exam mathematics` | no matches |
| `rot` | many matches — **intentional JA notation** |
| `第5章 §8.8` / `第5章第8.8節` | no matches |
| `場はそのまま` | no matches (replaced in ch08) |
| `d\mathbf{A}` | no matches (fixed in ch12) |
| `外積とクロス積` | no matches |
| `曲がっている` | ch04:2 — physical / cylindrical geometry context, not curvature overclaim |

---

## `git diff --check`

```bash
git diff --check manuscript/ja/
```

**Result:** pass (no trailing whitespace / conflict marker issues)

---

## PR readiness

- Scope-limited edits complete on `edit/ja-backport-wave4`
- Review note and progress update included
- Ready for PR against `main` referencing #193
- PDF/HTML rebuild **not** required by acceptance criteria (optional for release prep)
