# Critical Prompt 07 検証結果：計量・内積・Hodge star

## 対象補正

元プロンプトは第6章を対象にしており、現行原稿でも計量と Hodge star は第6章で扱われる。

- `manuscript/ja/ch06/ch06.md`
- 付録D「フロベニウス積とホッジ・スターの完全な行列表現」

## 第6章の好意的再構成

第6章は、これまで暗黙に使っていた長さ・角度・面積の正の大きさを、計量 $g$ として明示する章である。パラメータ空間の内積を

$$
v_1^T g v_2,\qquad g=J^T J
$$

で表し、直交デカルト座標では $g=I$ になることを示している。

その上で、Hodge star を

$$
\ast 1=dx\wedge dy\wedge dz,\quad
\ast dx=dy\wedge dz,\quad
\ast dy=dz\wedge dx,\quad
\ast dz=dx\wedge dy
$$

という 3 次元ユークリッド右手系の辞書として導入している。第6章は、`*` が計量と向きに依存することも明示しているため、主張の骨格は妥当である。

## 計量依存・非依存の分類

| 構造 | 分類 | 備考 |
|---|---|---|
| $dx,dy,dz$ の作用 | 計量非依存 | covector が vector に作用する |
| wedge 積 | 計量非依存 | 向き付き投影量を作る |
| 外微分 $d$ | 計量非依存 | 第5章の主役 |
| 形式の引き戻し | 計量非依存 | 第4章 |
| 長さ・角度 | 計量依存 | $g$ が必要 |
| 1-form とベクトル場の同一視 | 計量依存 | $^\sharp/^\flat$ が必要 |
| 1-form と 2-form の対応 | 計量 + 向き依存 | Hodge star |
| curl/div の標準ベクトル表示 | 計量 + 向き依存 | `*` と同一視が必要 |

## 問題候補

### 1. frontmatter の章題が第5章になっている

該当箇所：

- `manuscript/ja/ch06/ch06.md:2`

本文見出しは「第6章」だが、frontmatter の `title` は「第5章：計量...」になっている。ビルドや目次生成で frontmatter を使う場合、章題がずれる可能性がある。

Issue 化判定：採用候補。章参照ずれ一括 Issue に含めてもよいが、frontmatter は生成物に影響しうるため明示する。

### 2. `grad f = df` は型としては covector であり、ベクトルの勾配には `sharp` が必要

該当箇所：

- `manuscript/ja/ch06/ch06.md:493`
- `manuscript/ja/ch06/ch06.md:499`
- `manuscript/ja/ch06/ch06.md:501`
- `manuscript/ja/ch06/ch06.md:553`
- `manuscript/ja/ch06/ch06.md:574`

第6章は計量を導入した直後なので、本来ここで

$$
\nabla f=(df)^\sharp
$$

または「本書では直交デカルト座標の同一視を通して $df$ の成分を勾配ベクトルの成分と呼ぶ」と明示するのが望ましい。

現在の `grad f = df` は、本書の「横ベクトルと縦ベクトルを分ける」契約から見ると強すぎる。第6章までに計量を導入した以上、ここは「形式としては $df$、ベクトル解析の矢印としては $df$ を計量で上げたもの」と書き分けるべきである。

Issue 化判定：採用候補。後章の grad/curl/div 翻訳に直接影響する。

### 3. `rot F = * dω` も vector ではなく 1-form として得られている

該当箇所：

- `manuscript/ja/ch06/ch06.md:505`
- `manuscript/ja/ch06/ch06.md:513`
- `manuscript/ja/ch06/ch06.md:515`
- `manuscript/ja/ch06/ch06.md:517`

`*dω` は 1-form である。標準ベクトル解析の $\nabla\times F$ はベクトル場なので、厳密には

$$
\nabla\times F = (\ast d F^\flat)^\sharp
$$

である。本文は係数列を「回転」と呼んでいるため、直交デカルト座標では実用上同じだが、第6章の主旨からすると、ここも `sharp` に相当する計量同一視を明示したほうがよい。

Issue 化判定：採用候補。ただし Prompt 08 の grad/curl/div 監査と統合するのがよい。

### 4. `div F = * d * ω` の型は正しいが、入力の `F` が 1-form 化されていることを強調したい

該当箇所：

- `manuscript/ja/ch06/ch06.md:521`
- `manuscript/ja/ch06/ch06.md:525`
- `manuscript/ja/ch06/ch06.md:529`

発散は最終的に 0-form になるため、`*d*ω` の型は合っている。ただし標準ベクトル場 $F$ から始めるなら、入力で $F^\flat$ を取っている。第6章は `ω = F_x dx + F_y dy + F_z dz` と置いているため大破綻ではないが、「ベクトル場を 1-form として読んだ後」と明記したほうが本書の契約に合う。

Issue 化判定：Prompt 08 まで保留。grad/curl と同じ翻訳表で扱う。

### 5. `*` の定義が 3D Euclidean の辞書から始まるため、一般計量での公式は後送り

該当箇所：

- `manuscript/ja/ch06/ch06.md:375`
- `manuscript/ja/ch06/ch06.md:399`
- `manuscript/ja/ch06/ch06.md:401`
- `manuscript/ja/ch06/ch06.md:533`

本文は「一般座標では `*` の係数は複雑になる」と明言しており、これは正しい。ただし第6章単独では一般計量下の Hodge star の具体公式は出てこない。これは欠落というより、第9章へ送った構成上の選択である。

Issue 化判定：保留。Prompt 10 の曲線座標監査で確認する。

## 採用しない候補

### Hodge star の右手系符号

辞書

$$
\ast dx=dy\wedge dz,\quad
\ast dy=dz\wedge dx,\quad
\ast dz=dx\wedge dy
$$

および逆向き

$$
\ast(dy\wedge dz)=dx,\quad
\ast(dz\wedge dx)=dy,\quad
\ast(dx\wedge dy)=dz
$$

は、3次元ユークリッド右手系では標準的である。ここは Issue 化しない。

### フロベニウス積の `1/2`

付録Dは反対称行列表示で重複成分を二重に数えないため、フロベニウス積に `1/2` を入れている。第2章の行列表示規約とは整合しているように見える。最終判断は Prompt 15/16 の係数2監査で行う。

## 今回の結論

Prompt 07 は妥当。Issue 候補は次の二系統に整理する。

1. 第6章 frontmatter の章題誤りを修正する。
2. `grad = d`, `rot = *d`, `div = *d*` の表を、形式としての型とベクトル解析としての型に分け、必要な計量同一視を明記する。

