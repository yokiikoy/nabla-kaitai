---
title: "第3章：形式で積分を書き直す"
series: dx-matrix
chapter: 3
---

# 第3章：形式で積分を書き直す

第1章では、$dx$ を行ベクトルと見なし、1次元の積分を「行列作用の集計」として読み替えた。第2章では $dy$, $dz$ を加え、ウェッジ積によって 2-form（面積計）と 3-form（体積計）を組み立てた。

いま我々の手元には、次数 $0,1,2,3$ の「測定器」がそろった。本章の仕事は、**曲線・曲面・領域にわたって、それらをどう集計するか**を一つの言葉で統一することである。そして最後に、座標変換やパラメータ表示のときに現れる **引き戻し（pullback）** を導入し、**ヤコビ行列式**が「体積要素の歪み」として自然に出てくることを見る。

以下では、パラメータ表示は滑らかとし、向きの反転や自己交差などの細部は「物理でよく使う状況では問題にならない」レベルに留める。厳密な可積分論は本書の射程外である。

---

### §3.1 線積分の完全版 — 多成分 1-form を曲線に沿って集計する

#### 3.1.1 1-form の一般形

デカルト座標で、係数が点 $(x,y,z)$ に依存するスカラー場 $f_x, f_y, f_z$ をとるとき、
$$\omega = f_x(x,y,z)\,dx + f_y(x,y,z)\,dy + f_z(x,y,z)\,dz$$
を **1-form**（一次形式）の一般形と呼ぶ。各 $dx, dy, dz$ は第1章・第2章どおり、タテベクトル（変位）から成分を読み取る行ベクトルとして作用する。

変位ベクトル $\mathbf{v} = (v_x, v_y, v_z)^T$ に対して：
$$dx(\mathbf{v}) = v_x,\quad dy(\mathbf{v}) = v_y,\quad dz(\mathbf{v}) = v_z$$
だから：
$$\omega(\mathbf{v}) = f_x v_x + f_y v_y + f_z v_z$$
これは、ベクトル解析で慣れ親しんだ **内積** $\mathbf{f} \cdot \mathbf{v}$ に他ならない。ここで $\mathbf{f} = (f_x, f_y, f_z)^T$ である。

#### 3.1.2 曲線に沿った積分の定義

滑らかな曲線 $\gamma: [t_0, t_1] \to \mathbb{R}^3$ を考える。各 $t$ におけるベクトル $\gamma'(t)$（曲線がその瞬間に進む向きと速さを表す）に $\omega$ を作用させ、時間パラメータ $t$ に沿って集計する：
$$\int_\gamma \omega := \int_{t_0}^{t_1} \omega|_{\gamma(t)}\bigl(\gamma'(t)\bigr)\,dt$$

ここで $\omega|_{\gamma(t)}$ は、係数 $f_x, f_y, f_z$ を点 $\gamma(t)$ で評価したものである。

成分で書けば：
$$\omega|_{\gamma(t)}\bigl(\gamma'(t)\bigr) = f_x\,\dot{x}(t) + f_y\,\dot{y}(t) + f_z\,\dot{z}(t),\quad \gamma(t) = (x(t), y(t), z(t))$$

これは第1章 §1.4 で扱った
$$\int_\gamma f(x)\,dx = \int_{t_0}^{t_1} \bigl(f(\gamma(t))\,dx\bigr)\,\gamma'(t)\,dt$$
の **自然な拡張**である。$f(x)\,dx$ は $\omega$ の $f_x$ だけが非ゼロで $f_x = f$、他はゼロという特別場合にすぎない。新しい公理は要らない。**1-form は各基底成分について線形だから、3本の「物差し」を同時に足し合わせればよい**だけなのだ。

#### 3.1.3 仕事としての線積分

力場 $\mathbf{F}(x,y,z) = (F_x, F_y, F_z)^T$ が質点に働き、曲線 $\gamma$ に沿って移動するときの仕事は、ベクトル解析では
$$W = \int_\gamma \mathbf{F} \cdot d\mathbf{r}$$
と書かれる。これを本書の言葉で書けば、$\omega = F_x\,dx + F_y\,dy + F_z\,dz$ とおいて
$$W = \int_\gamma \omega$$
である。$d\mathbf{r} = (\dot{x}\,dt,\, \dot{y}\,dt,\, \dot{z}\,dt)^T$ と見なせば、被積分関数 $\mathbf{F}\cdot d\mathbf{r}/dt = \omega(\gamma')$ となる。

**場（何を測るか）** と **経路（どこをどう進むか）** が、記号上も明確に分離されていることが、微分形式の記法の強みである。

---

### §3.2 面積分 — 2-form をパラメータ曲面に沿って集計する

#### 3.2.1 パラメータ曲面と座標方向のベクトル

平面領域 $D \subset \mathbb{R}^2$ から空間への滑らかな写像
$$\Phi: D \to \mathbb{R}^3,\quad (u,v) \mapsto \mathbf{r}(u,v) = (x(u,v),\, y(u,v),\, z(u,v))$$
が与えられたとき、像 $S = \Phi(D)$ を **パラメータ曲面**と呼ぶ。各点における偏微分
$$\Phi_u := \frac{\partial \mathbf{r}}{\partial u},\quad \Phi_v := \frac{\partial \mathbf{r}}{\partial v}$$
は、曲面の接平面を張る2本のベクトルである（線形独立を仮定する）。

#### 3.2.2 2-form の曲面積分

第2章で、2-form $\eta$ は2つの変位ベクトル $\mathbf{v}_1, \mathbf{v}_2$ に対して **反対称かつ双線形**なスカラー $\eta(\mathbf{v}_1, \mathbf{v}_2)$ を返す「面積計」として定義された。曲面では、各点でパラメータ $u,v$ の偏微分が与える2本のベクトル $\Phi_u, \Phi_v$ に食わせる：
$$\iint_S \eta := \iint_D \eta|_{\Phi(u,v)}\bigl(\Phi_u(u,v),\,\Phi_v(u,v)\bigr)\,du\,dv$$

向きの約定として、$(u,v)$ の並びと曲面の「表側」を対応させる。$(u,v) \mapsto (v,u)$ と入れ替えると $\eta(\Phi_v, \Phi_u) = -\eta(\Phi_u, \Phi_v)$ となり、**符号が反転**する——向きを制御する操作が、代数として自動的に組み込まれている。

#### 3.2.3 通量 $\displaystyle\iint \mathbf{F}\cdot d\mathbf{S}$ との橋渡し

ベクトル場 $\mathbf{F} = (P, Q, R)^T$ に対し、デカルト座標で
$$\eta_{\mathbf{F}} := P\,dy \wedge dz + Q\,dz \wedge dx + R\,dx \wedge dy$$
と定める（係数はすべて点の関数）。任意のベクトル $\mathbf{u}, \mathbf{v}$ に対して次の恒等式が成り立つ：
$$\eta_{\mathbf{F}}(\mathbf{u}, \mathbf{v}) = \mathbf{F} \cdot (\mathbf{u} \times \mathbf{v})$$

実際、$dy \wedge dz(\mathbf{u}, \mathbf{v}) = u_y v_z - u_z v_y = (\mathbf{u} \times \mathbf{v})_x$ のように、各 2-form 基底は外積の成分に対応するからである。

したがって：
$$\iint_S \eta_{\mathbf{F}} = \iint_D \mathbf{F}\bigl(\Phi(u,v)\bigr) \cdot \bigl(\Phi_u \times \Phi_v\bigr)\,du\,dv$$

右辺は、ベクトル解析で書く **通量** $\iint_S \mathbf{F} \cdot d\mathbf{S}$（$d\mathbf{S} = \mathbf{n}\,dS$ で法線と面積要素の積）と、向きの取り方が一致すれば同一になる。すなわち **「2-form を $\Phi_u,\Phi_v$ で評価して集計する」** と **「ベクトル場を法線成分で面に打ち込む」** は、同じ幾何量の二つの表現なのである。

ホッジ・スター $\ast$ を使えば $\eta_{\mathbf{F}}$ と $\mathbf{F}$ の対応をより機械的に書けるが、その本格導入は第5章に譲る。ここでは **成分がピタリと合う** ことを踏み台にすれば十分だ。

```text
[図の挿入プレースホルダー]
パラメータ空間 (u,v) の長方形が、空間内の曲面片 S に貼り付けられる模式図。
$\Phi_u,\Phi_v$（$u,v$ を動かしたときの曲面の進む向き）と、それらの外積の向き（法線）を示す。
```

---

### §3.3 体積分 — 3-form の積分

#### 3.3.1 3-form と体積要素

第2章で、基底 3-form $dx \wedge dy \wedge dz$ は3つの変位ベクトルに対する **符号付き体積**（平行六面体の行列式）を与えることが分かった。スカラー場 $\rho(x,y,z)$ を係数として
$$\Omega = \rho(x,y,z)\,dx \wedge dy \wedge dz$$
を考える。空間領域 $V \subset \mathbb{R}^3$ に対し、デカルト座標で
$$\iiint_V \Omega := \iiint_V \rho(x,y,z)\,dx\,dy\,dz$$
と定める。右辺は通常の **三重積分**である。

第2章 §2.5.8 で述べたように、3次元では 3-form の独立成分は $dx \wedge dy \wedge dz$ の1つだけなので、**「密度」$\rho$ と「体積の測り方」が分離**して見通しがよい。質量や電荷の総量を求める式 $\iiint_V \rho\,dV$ は、形式的にも $\iiint_V \rho\,dx \wedge dy \wedge dz$ と読み替えられる。

#### 3.3.2 線・面・体の統一像

ここまでを俯瞰しよう。

| 対象 | 形式 | 積分の骨格 |
|:---:|:---|:---|
| 曲線 $\gamma$ | 1-form $\omega$ | $\displaystyle\int \omega(\gamma')\,dt$ |
| 曲面 $S$ | 2-form $\eta$ | $\displaystyle\iint \eta(\Phi_u, \Phi_v)\,du\,dv$ |
| 領域 $V$ | 3-form $\Omega$ | $\displaystyle\iiint \rho\,dx\,dy\,dz$ |

いずれも **「形式を、パラメータ表示が各座標で与えるベクトル（曲線では $\gamma'(t)$ の1本、曲面では $\Phi_u,\Phi_v$ の2本）に食わせ、スカラーになったものを集計する」** という同じ型の操作である。次数が上がるごとに、食わせるベクトルの本数が増え、反対称性が面積・体積の向きを司る。

---

### §3.4 引き戻し（pullback）とヤコビアン

#### 3.4.1 動機 — パラメータ空間で「影」を計算する

曲面積分で既に、空間内の $S$ 上の積分を、$(u,v)$ 平面の領域 $D$ 上の積分に還元した。これは **「$S$ 上の形式を、写像 $\Phi$ を通じて $D$ 上に引き戻す」** という操作の特殊場合である。一般に、写像 $\Phi: U \to \mathbb{R}^3$（$U$ は $\mathbb{R}^k$ の開集合、$k=1,2,3$ など）が与えられたとき、目標空間上の微分形式 $\omega$ に対して、**引き戻し** $\Phi^\ast \omega$ は $U$ 上の形式として定義される。直観的には、「$\Phi$ の像の上で $\omega$ が値を返すのと同じ情報を、$U$ の座標だけで書き表したもの」である。

#### 3.4.2 0-form（関数）の引き戻し

スカラー場 $f$（0-form）に対しては、合成だけでよい：
$$\Phi^\ast f := f \circ \Phi$$
すなわち $(\Phi^\ast f)(u) = f(\Phi(u))$ である。

#### 3.4.3 1-form の引き戻し — 第1章の円柱座標がモデル

第1章 §1.5 で、デカルトの $x$ と円柱座標 $(r,\theta,z)$ の関係 $x = r\cos\theta$ から
$$dx = \cos\theta\,dr - r\sin\theta\,d\theta$$
と計算した。これは、包含写像 $(r,\theta,z) \mapsto (x,y,z)$ に沿う **$dx$ の引き戻し**を、円柱座標側の 1-form として表したものだと見なせる。

一般に、$\Phi: U \to \mathbb{R}^3$ が $\mathbf{x} = \Phi(\mathbf{u})$ と書け、デカルトで $\omega = \sum_i f_i\,dx_i$ のとき、**連鎖律**が行列形式で $d\mathbf{x} = J\,d\mathbf{u}$（$J$ はヤコビ行列）を与え、
$$\Phi^\ast \omega = \sum_i (f_i \circ \Phi)\,(d\Phi_i)$$
として計算する。ここで $d\Phi_i$ は $\Phi_i$ の全微分（1-form）である。成分を丁寧に追えば、第1章で手を動かした $dx$ の変形と同じ手続きの繰り返しにすぎない。

#### 3.4.4 2-form・3-form — 曲面積分・体積分との同一視

曲面 $S$ 上の 2-form $\eta$ を $\Phi: D \to \mathbb{R}^3$ でパラメータ化するとき、§3.2 の積分は
$$\iint_D (\Phi^\ast \eta)$$
と書ける。ここで右辺の $\Phi^\ast \eta$ は $D$ 上の 2-form となり、$du \wedge dv$ に比例する形に整理できる（$du, dv$ が接座標）。**「空間側の $\eta$ を $(u,v)$ に引き戻してから、平面領域で積分する」** のが pullback の本質である。

#### 3.4.5 体積変換とヤコビ行列式

$\Phi: U \subset \mathbb{R}^3 \to \mathbb{R}^3$ を、座標変換（または体積領域のパラメータ化）とみなす。デカルトの体積 3-form $\Omega = dx \wedge dy \wedge dz$ の引き戻しは
$$\Phi^\ast \Omega = \det J(\mathbf{u})\,du \wedge dv \wedge dw$$
の形になる。ここで $J(\mathbf{u}) = \dfrac{\partial(x,y,z)}{\partial(u,v,w)}$ はヤコビ行列、$\det J$ が **ヤコビアン**である。

したがって：
$$\iiint_V f(x,y,z)\,dx\,dy\,dz = \iiint_{U} f(\Phi(\mathbf{u}))\,\bigl|\det J(\mathbf{u})\bigr|\,du\,dv\,dw$$
のように、解析学で習う **変数変換の公式**が、**3-form の引き戻しで体積要素がどう歪むか**という幾何として読み取れる。符号は向き（向きが反転すれば $\det J$ が負）に吸収され、絶値を取るか向き付き積分にするかは、問題設定に応じて選べばよい。

**第I部（積分記号の尻尾の正体）** で我々が積み上げてきたのは、次の三段だ：

1. $dx$ などを **行列（測定器）** と見なし、積分を **作用の集計** と読む（第1章）。
2. ウェッジ積で **2-form・3-form** を構成し、面積・体積を **代数**で測る（第2章）。
3. 曲線・曲面・領域にわたる **積分**を統一し、**引き戻し**で座標・パラメータに落とし、**ヤコビアン**を自然に説明する（本章）。

ここから先の **第II部** では、いよいよ **外微分 $d$** を導入する。$d$ は「形式の次数を1つ上げる」線形演算子であり、勾配・回転・発散が **一つの操作のバリエーション**であることが明らかになる。積分側の言葉がそろったいま、微分側の代数を完成させる準備が整ったのである。

---

> **【ここまでのチェックポイント — 第3章】**
> - 一般の 1-form $\omega = f_x dx + f_y dy + f_z dz$ の線積分は、§1.4 の1成分版を線形に拡張したもの。仕事は $\int_\gamma \mathbf{F}\cdot d\mathbf{r} = \int_\gamma \omega_{\mathbf{F}}$。
> - 2-form の曲面積分は $\iint_D \eta(\Phi_u, \Phi_v)\,du\,dv$。$\eta_{\mathbf{F}} = P\,dy\wedge dz + \cdots$ と $\mathbf{F}\cdot(\Phi_u\times\Phi_v)$ が一致する。
> - 3-form $\rho\,dx\wedge dy\wedge dz$ の体積分は三重積分 $\iiint \rho\,dV$。
> - 引き戻し $\Phi^\ast$ はパラメータ空間での「影の形式」。3-form の引き戻しに $\det J$ が現れ、変数変換公式の幾何的意味が説明できる。
> - 次章（第4章）では外微分 $d$ を定義し、第II部へ入る。

---
