# 第2章：面積とは何か —— theoretical minimum

## 0. 対象範囲

3次元ユークリッド空間 $\mathbb R^3$（デカルト座標 $(x,y,z)$）における $k$-form（$k=0,1,2,3$）を行列表現で構成する。

第1章で定義した $dx, dy, dz$ を構成要素として、面積測定器（$2$-form）と体積測定器（$3$-form）を代数的に組み立てる。

---

## I. 定義

<strong>定義 1：面積測定器の公理的要件</strong>

2つのベクトル $\mathbf{v}_1, \mathbf{v}_2 \in \mathbb R^3$ を入力とし、スカラー $S(\mathbf{v}_1, \mathbf{v}_2) \in \mathbb R$ を返す装置 $S$ が面積測定器であるとは、以下の3条件を満たすことを言う：

1. <strong>双線形性</strong>: 各引数について線形。
   $$S(a\mathbf{v}_1 + b\mathbf{u},\, \mathbf{v}_2) = a\,S(\mathbf{v}_1,\mathbf{v}_2) + b\,S(\mathbf{u},\mathbf{v}_2)$$
   （第2引数についても同様）

2. <strong>交代性</strong>: 同じベクトルを2つ入れるとゼロ。
   $$S(\mathbf{v}_1, \mathbf{v}_1) = 0$$
   これより直ちに $S(\mathbf{v}_1,\mathbf{v}_2) = -S(\mathbf{v}_2,\mathbf{v}_1)$ が導かれる。

3. <strong>規格化</strong>: 標準基底の面積を1とする。
   $$S(\hat e_x, \hat e_y) = 1,\quad \hat e_x = \begin{pmatrix}1\\0\\0\end{pmatrix},\; \hat e_y = \begin{pmatrix}0\\1\\0\end{pmatrix}$$

<strong>定義 2：体積測定器の公理的要件</strong>

3つのベクトル $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ を入力とする装置 $V$ が体積測定器であるとは、以下を満たす：

1. <strong>多重線形性</strong>: 各引数について線形。
2. <strong>交代性</strong>: 任意の2引数を入れ替えると符号反転。特に同じベクトルが2つあるとゼロ。
3. <strong>規格化</strong>: $V(\hat e_x, \hat e_y, \hat e_z) = 1$

---

## II. 定理

<strong>定理 1：$xy$ 平面の面積測定器の正体——反対称行列</strong>

$z=0$ の制限下で、定義1の3条件を満たす $S$ は一意に存在し、次の $3\times 3$ 反対称行列で表現される：

$$
S(\mathbf{v}_1, \mathbf{v}_2) = \mathbf{v}_1^T M \mathbf{v}_2,
\qquad
M = \begin{pmatrix}
0 & 1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

計算すると：

$$
S(\mathbf{v}_1,\mathbf{v}_2) = \begin{pmatrix}x_1&y_1&0\end{pmatrix}
\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}
\begin{pmatrix}x_2\\y_2\\0\end{pmatrix}
= x_1 y_2 - x_2 y_1.
$$

<strong>定理 2：ウェッジ積の定義</strong>

$dx, dy$ のテンソル積 $dx\otimes dy$ を次で定義する：

$$
(dx\otimes dy)(\mathbf{v}_1,\mathbf{v}_2) := dx(\mathbf{v}_1)\,dy(\mathbf{v}_2) = x_1 y_2.
$$

ウェッジ積（外積）$dx\wedge dy$ を、テンソル積の反対称化として定義する：

$$
dx\wedge dy := dx\otimes dy - dy\otimes dx.
$$

作用：

$$
(dx\wedge dy)(\mathbf{v}_1,\mathbf{v}_2) = x_1 y_2 - x_2 y_1.
$$

これは定理1の $S$ と完全に一致する。

<strong>定理 3：三つの基底 $2$-form</strong>

同様にして三つの基底 $2$-form が得られる：

$$
\begin{aligned}
dy\wedge dz &:= dy\otimes dz - dz\otimes dy, \\
dz\wedge dx &:= dz\otimes dx - dx\otimes dz, \\
dx\wedge dy &:= dx\otimes dy - dy\otimes dx.
\end{aligned}
$$

行列表現：

$$
dy\wedge dz \longleftrightarrow \begin{pmatrix}0&0&0\\0&0&1\\0&-1&0\end{pmatrix},\quad
dz\wedge dx \longleftrightarrow \begin{pmatrix}0&0&-1\\0&0&0\\1&0&0\end{pmatrix},\quad
dx\wedge dy \longleftrightarrow \begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}.
$$

一般の $2$-form はこれらの線形結合で書ける：

$$
\omega = \alpha\,dy\wedge dz + \beta\,dz\wedge dx + \gamma\,dx\wedge dy.
$$

<strong>定理 4：体積測定器 $dx\wedge dy\wedge dz$（$3$-form）</strong>

3つの $1$-form のウェッジ積 $dx\wedge dy\wedge dz$ を、$3! = 6$ 個のテンソル積の符号つき和として定義する：

$$
dx\wedge dy\wedge dz := \sum_{\sigma\in S_3} \mathrm{sgn}(\sigma)\; d_{\sigma(1)}\otimes d_{\sigma(2)}\otimes d_{\sigma(3)}.
$$

ここで $d_1=dx,\; d_2=dy,\; d_3=dz$。$S_3$ は3次対称群、$\mathrm{sgn}(\sigma)$ は置換の符号。

3つのベクトルに作用させると $3\times3$ 行列式になる：

$$
(dx\wedge dy\wedge dz)(\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3)
= \det\begin{pmatrix}
x_1 & x_2 & x_3 \\
y_1 & y_2 & y_3 \\
z_1 & z_2 & z_3
\end{pmatrix}.
$$

展開すると6項：

$$
= x_1 y_2 z_3 + y_1 z_2 x_3 + z_1 x_2 y_3 - y_1 x_2 z_3 - x_1 z_2 y_3 - z_1 y_2 x_3.
$$

<strong>定理 5：$2$-form の行列式表示</strong>

$$
(dx\wedge dy)(\mathbf{v}_1,\mathbf{v}_2) = \det\begin{pmatrix} dx(\mathbf{v}_1) & dx(\mathbf{v}_2) \\ dy(\mathbf{v}_1) & dy(\mathbf{v}_2) \end{pmatrix}
= \det\begin{pmatrix} x_1 & x_2 \\ y_1 & y_2 \end{pmatrix}.
$$

<strong>定理 6：向き付き面積の成分分解</strong>

3次元空間における任意の平行四辺形の向き付き面積は、三つの座標平面への射影として分解される：

$$
\begin{aligned}
A_{yz} &:= (dy\wedge dz)(\mathbf{v}_1,\mathbf{v}_2) = y_1 z_2 - z_1 y_2, \\
A_{zx} &:= (dz\wedge dx)(\mathbf{v}_1,\mathbf{v}_2) = z_1 x_2 - x_1 z_2, \\
A_{xy} &:= (dx\wedge dy)(\mathbf{v}_1,\mathbf{v}_2) = x_1 y_2 - x_2 y_1.
\end{aligned}
$$

これらは各座標平面（$yz$, $zx$, $xy$）への正射影の符号付き面積である。

スカラー面積（正の値）は二乗和の平方根：

$$
S = \sqrt{A_{yz}^2 + A_{zx}^2 + A_{xy}^2}.
$$

<strong>定理 7：クロス積との対応</strong>

$$
\mathbf{v}_1\times\mathbf{v}_2 = \begin{pmatrix} A_{yz} \\ A_{zx} \\ A_{xy} \end{pmatrix}
= \begin{pmatrix} (dy\wedge dz)(\mathbf{v}_1,\mathbf{v}_2) \\ (dz\wedge dx)(\mathbf{v}_1,\mathbf{v}_2) \\ (dx\wedge dy)(\mathbf{v}_1,\mathbf{v}_2) \end{pmatrix}.
$$

---

## III. 追加構造

<strong>追加構造 1：レヴィ=チヴィタ記号</strong>

$dx, dy, dz$ の成分表示を用いると、$dx\wedge dy\wedge dz$ のテンソル表現は3階の反対称テンソル $\epsilon_{ijk}$（レヴィ=チヴィタ記号）で書ける：

$$
\epsilon_{ijk} = \begin{cases}
+1 & (i,j,k) \text{ が } (x,y,z) \text{ の偶置換} \\
-1 & (i,j,k) \text{ が } (x,y,z) \text{ の奇置換} \\
0 & \text{添字に重複あり}
\end{cases}
$$

これを用いると：

$$
(dx\wedge dy\wedge dz)(\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3) = \sum_i\sum_j\sum_k \epsilon_{ijk}\, v_{1i}\, v_{2j}\, v_{3k}.
$$

---

## IV. 次元の系列

| $k$ | $k$-form（はかり） | $k$-vector（図形） | 成分数 | スカラー |
|:---|:---|:---|:---|:---|
| 0 | スカラー場 $f$ | 点 | 1 | $\sqrt{f^2}$ |
| 1 | $dx, dy, dz$ | $\hat e_x, \hat e_y, \hat e_z$ | 3 | $\sqrt{x^2+y^2+z^2}$ |
| 2 | $dy\wedge dz,$ $dz\wedge dx,$ $dx\wedge dy$ | $\hat e_y\wedge\hat e_z,$ $\hat e_z\wedge\hat e_x,$ $\hat e_x\wedge\hat e_y$ | 3 | $\sqrt{A_{yz}^2+A_{zx}^2+A_{xy}^2}$ |
| 3 | $dx\wedge dy\wedge dz$ | $\hat e_x\wedge\hat e_y\wedge\hat e_z$ | 1 | $\sqrt{V^2}$ |

---

## V. 中心命題

$$
\boxed{dx\wedge dy := dx\otimes dy - dy\otimes dx}
$$

$$
\boxed{(dx\wedge dy)(\mathbf{v}_1,\mathbf{v}_2) = x_1 y_2 - x_2 y_1}
$$

$$
\boxed{(dx\wedge dy\wedge dz)(\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3) = \det\!\begin{pmatrix}x_1&x_2&x_3\\y_1&y_2&y_3\\z_1&z_2&z_3\end{pmatrix}}
$$

$$
\boxed{k\text{-form は }k\text{ 個のベクトルを食べてスカラーを返す反対称多重線形写像である。}}
$$
