# GitHub Issue 作成前の候補整理

## 方針

25 個のプロンプトは、現行原稿にそのまま対応しない章指定を含んでいた。そのため、各プロンプトを現行章構成へ補正して実行した。

GitHub Issue にする条件は次の通り。

- 該当箇所が具体的に特定できる。
- 修正方針が明確である。
- 単なる好みや文体批判ではなく、型・符号・射程・参照・読者誤読リスクに関わる。
- 重複候補は一つの Issue に統合する。

## 優先 Issue 候補

### 1. 第3章の `ds` を 1-form と呼ぶ箇所を修正する

根拠：

- `manuscript/ja/ch03/ch03.md:340`
- `manuscript/ja/ch03/ch03.md:346`
- `manuscript/ja/ch03/ch03.md:352`
- `manuscript/ja/ch03/ch03.md:362`

問題：

`ds(v)=sqrt(dx(v)^2+dy(v)^2)` は $v$ に線形ではないため、微分形式としての 1-form ではない。計量から得る線素・ノルムとして扱うべき。

### 2. 第3章の「一般の 1-form」を exact form に見えないようにする

根拠：

- `manuscript/ja/ch03/ch03.md:383-387`

問題：

一般の 1-form を `∂f/∂x dx + ...` と書いており、`df` と区別しにくい。`P dx + Q dy + R dz` を一般形にすべき。

### 3. 第4章の一般 pullback 定義を有限差分記号から偏微分・ヤコビ行列へ直す

根拠：

- `manuscript/ja/ch04/ch04.md:224-228`
- `manuscript/ja/ch04/ch04.md:290-302`
- `manuscript/ja/ch04/ch04.md:342-346`

問題：

有限マス目の導入としての `Δx_u` はよいが、「一般的な定義」としては偏微分・ヤコビ行列式で書く必要がある。

### 4. 第5章の `d` と積分の「片側逆」説明を型安全にする

根拠：

- `manuscript/ja/ch05/ch05.md:146`

問題：

`∫∘d=id` や `d∘∫` は型が合わない。基本定理または Stokes 型公式の 0-form 版として説明する。

### 5. `∂(∂M)=∅` を「向き付き境界としてゼロ」に直す

根拠：

- `manuscript/ja/ch05/ch05.md:535-537`
- `manuscript/ja/ch05/ch05.md:569`
- `manuscript/ja/ch05/ch05.md:643`

問題：

境界の境界は集合として空というより、向き付き境界として相殺してゼロである。

### 6. Stokes の誘導向きと局所化の仮定を補う

根拠：

- `manuscript/ja/ch05/ch05.md:372-388`
- `manuscript/ja/ch05/ch05.md:595-601`

問題：

曲面の向きと境界の誘導向きが第5章単独では弱い。また、任意領域で積分ゼロなら局所式、という推論には滑らかさ・任意小領域の仮定が必要。

### 7. `grad/rot/div` の翻訳表に `♭/♯` 相当の計量同一視を明記する

根拠：

- `manuscript/ja/ch06/ch06.md:493-529`
- `manuscript/ja/ch07/ch07.md:145-147`
- `manuscript/ja/ch08/ch08.md:108-144`

問題：

`grad f = df`, `rot F = *dω` は形式としては covector/1-form であり、ベクトル解析の矢印に戻すには計量同型が必要。

### 8. 第9章の射程を直交曲線座標中心に限定する

根拠：

- `manuscript/ja/ch09/ch09.md:56-62`
- `manuscript/ja/ch09/ch09.md:86`
- `manuscript/ja/ch09/ch09.md:300`

問題：

円柱・球座標は直交曲線座標であり、非直交座標では Hodge star の辞書に混合項が出る。「任意の座標系」と言い切るには説明不足。

### 9. 曲線座標の正規直交成分と form 係数の規約を固定する

根拠：

- `manuscript/ja/ch09/ch09.md:110-112`
- `manuscript/ja/ch09/ch09.md:172-174`

問題：

`F_theta` と `rF_theta` の区別を「文脈で判断」とすると危険。表で規約を固定するべき。

### 10. 円柱・球座標の座標特異点と定義域を明示する

根拠：

- `manuscript/ja/ch09/ch09.md:69`
- `manuscript/ja/ch09/ch09.md:145`
- `manuscript/ja/ch09/ch09.md:290`

問題：

公式は $r=0$, $\rho=0$, $\theta=0,\pi$ を除く座標パッチ上の公式であることを導入時に明記する。

### 11. 第10章 Maxwell の反対称行列表示と 2-form 表示の符号を検算する

根拠：

- `manuscript/ja/ch10/ch10.md:96-107`
- `manuscript/ja/ch10/ch10.md:111-123`
- `manuscript/ja/ch10/ch10.md:269-344`

問題：

提示された行列の `E` 成分と、基底 2-form 表示 `E_x dt∧dx + ...` が逆符号に見える。`F=-dA` との整合も含めて検算が必要。

### 12. 第10章の正規化済み `B`, `t`, `J`, `\mathcal{J}` を表で固定する

根拠：

- `manuscript/ja/ch10/ch10.md:58-77`
- `manuscript/ja/ch10/ch10.md:103`
- `manuscript/ja/ch10/ch10.md:240-250`
- `manuscript/ja/ch12/ch12.md:274-276`

問題：

`B'=cB`, `w=ct` を再び `B`, `t` と呼ぶため、後続の Maxwell 式で単位・係数を誤読しやすい。

### 13. 第11章の「第9章の `g` は定数行列だった」を修正する

根拠：

- `manuscript/ja/ch11/ch11.md:52`

問題：

第9章の円柱・球座標計量は座標依存である。平坦性と座標依存計量を区別する必要がある。

### 14. 第12章の「真の」「究極」などの過大表現を弱める

根拠：

- `manuscript/ja/ch12/ch12.md:25`
- `manuscript/ja/ch12/ch12.md:296`
- `manuscript/ja/ch12/ch12.md:304`

問題：

第12章はおまけと限定しているが、厳密な幾何代数の章ではないため、最終主張の表現は弱めたほうが安全。

### 15. 章番号・節番号の参照ずれを一括修正する

根拠：

代表例：

- `manuscript/ja/ch01/ch01.md:410`
- `manuscript/ja/ch02/ch02.md:684`
- `manuscript/ja/ch04/ch04.md:356`
- `manuscript/ja/ch04/ch04.md:366`
- `manuscript/ja/ch05/ch05.md:562`
- `manuscript/ja/ch07/ch07.md:47`
- `manuscript/ja/ch08/ch08.md:158`
- `manuscript/ja/ch08/ch08.md:209`
- `manuscript/ja/ch09/ch09.md:60`
- `manuscript/ja/ch11/ch11.md:122`
- `manuscript/ja/ch12/ch12.md:190`

問題：

現行章構成と一致しない参照が多く、読者の追跡を妨げる。内容修正とは別に一括 Issue にするのがよい。

## Issue 化しない候補

- `dx=(1 0 0)` 単独批判：第11章でかなり回収済み。
- 3D Euclidean の Hodge star 辞書：符号は概ね標準。
- 円柱・球座標の主要な発散・回転公式：標準公式と一致。
- Prompt 19〜25：Issue ではなく、総合レビュー・読解ガイド・メタプロンプト生成用。

## 推奨実行順

1. まず `章番号・節番号の参照ずれ` を一括 Issue 化する。
2. 次に数式の型誤りとして `ds`, `一般 1-form`, `pullback`, `d と積分の逆`, `∂^2=0` を Issue 化する。
3. その後、横断 Issue として `grad/rot/div の ♭/♯`, `曲線座標の射程`, `Maxwell 符号規約`, `正規化表` を作る。
4. 最後に表現調整として第12章の過大表現を扱う。

## 作成済み GitHub Issue

- #16: 第3章: `ds` を 1-form と呼ぶ箇所を計量的線素として修正する
- #17: 第3章: 一般の 1-form を exact form と誤読されない形に修正する
- #18: 第4章: 一般 pullback 定義を有限差分記号から偏微分・ヤコビ行列へ修正する
- #19: 第5章: `d` と積分を片側逆として説明する注を型安全にする
- #20: 第5章: `境界の境界は空` を向き付き境界としてゼロに修正する
- #21: 第5章: Stokes の誘導向きと局所化の仮定を補う
- #22: 第6〜8章: grad/rot/div の翻訳表に計量同一視を明記する
- #23: 第9章: 曲線座標公式の射程を直交曲線座標中心に限定する
- #24: 第9章: 曲線座標での正規直交成分と form 係数の規約を固定する
- #25: 第9章: 円柱・球座標の座標特異点と定義域を明示する
- #26: 第10章: Maxwell の反対称行列表示と 2-form 表示の符号を検算する
- #27: 第10章: 正規化済みの B, t, J, current form の意味を表で固定する
- #28: 第11章: 第9章の計量を「定数行列」とする記述を修正する
- #29: 第12章: 「真のナブラ」「究極のマクスウェル方程式」などの過大表現を弱める
- #30: 全体: 章番号・節番号の参照ずれを一括修正する
