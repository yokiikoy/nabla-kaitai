# 第4章：外微分 $d$ — 次元を上げる唯一の魔法

これまでの旅路を振り返ろう。第1章では、積分記号の末尾にへばりつく `dx` を「微小量」から「行列」へと解体し、それを<strong>1-形式</strong>（1-form）と呼んだ。第2章では、その物差し $dx, dy, dz$ を掛け合わせる<strong>ウェッジ積（$\wedge$）</strong> という魔法の工具を手に入れ、面積計（2-form）と体積計（3-form）を組み立てた。第3章では、これらの局所的「測定器」を曲線・曲面・領域という現場に持ち込み、引き戻しという翻訳アルゴリズムを使って集計（積分）する方法を確立した。

我々は今、強力な道具箱を手にしている。しかし、この箱の中身はすべて<strong>静的な測定器</strong>だ。ある一点で、向きを定めた長さ・面積・体積を測ることはできる。だが、物理学の本質は「変化」にある。温度が最も急峻に上昇する方向（勾配）、流体がどのくらい「渦を巻いている」か（回転）、ある点から物質が湧き出しているか吸い込まれているか（発散）——これらはすべて、場の<strong>局所的な変化の様子</strong>を記述する。

この「変化の方向へと測定器を押し上げる」操作こそが、<strong>外微分（exterior derivative）</strong>、記号 $d$ の正体である。本章では、このたった一つの演算子 $d$ が、0-form（スカラー場）を1-form（勾配）に、1-formを2-form（回転）に、2-formを3-form（発散）へと次々に「昇格」させていく魔法の詳細を、行列と成分のレベルで解き明かしていく。

---

## §4.1 $df$ から再出発 — 「変化率行列」の進化形

### 4.1.1 動機：測定器を「変化方向」に敏感にしたい

第1章§1.3で、我々は関数 $f$ の全微分を次のように定義した。
$$
df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz.
$$
これは、デカルト座標では $1 \times 3$ 行列 $[f_x, f_y, f_z]$ であり、「変位ベクトルに作用させると、その変位による $f$ の一次変化量を返す感度行列」だった。

重要なのは、$df$ の出力が<strong>スカラー</strong>（0-formの変化量）であるにもかかわらず、$df$ それ自体は<strong>1-form</strong>（ベクトルを食べてスカラーを返す行列）として振る舞うことだ。言い換えれば、$d$ という操作は、<strong>0-form（スカラー場 $f$）を入力として受け取り、1-form（$df$）を出力として吐き出す</strong>。これはまさに「次元を上げる」操作の原型である。

ここで一つの自然な問いが湧く。<strong>この「次元上げ」は、1-formから2-formへ、2-formから3-formへと繰り返せないだろうか？</strong> 例えば、風速のベクトル場（物理的には1-formに対応）が、どれだけ「渦を巻いているか」という面積的な量（2-form）へ昇格できれば、渦度を代数的に表現できるはずだ。

### 4.1.2 違和感：単なる偏微分の行列では足りない

1-formの一般形は $\omega = P\,dx + Q\,dy + R\,dz$ である。係数 $P, Q, R$ はそれぞれ $(x, y, z)$ の関数だ。これを「微分」したい。
安直に考えれば、各係数を偏微分して並べた $3 \times 3$ 行列
$$
\begin{pmatrix}
P_x & P_y & P_z \\
Q_x & Q_y & Q_z \\
R_x & R_y & R_z
\end{pmatrix}
$$
を作りたくなる。しかし、これは我々が求めている「2-form」にはならない。2-formは $3 \times 3$ <strong>反対称行列</strong>でなければならなかった（第2章§2.3）。上の行列は一般に反対称ではない。

では、どうすればこの行列から反対称な部分を抽出できるか？ 線形代数の常套手段は「反対称成分を取り出す」こと、すなわち行列からその転置を引き算することだ（$A \mapsto \frac{1}{2}(A - A^T)$）。この直感が、実は外微分 $d$ の核心へとつながる。

### 4.1.3 ルールの構築：ウェッジ積との整合性を指針に

我々は既に強力な代数的ツール、<strong>ウェッジ積（$\wedge$）</strong> を持っている。そして、0-formに対する $d$ の動作は $df = f_x dx + f_y dy + f_z dz$ で、これはあたかも $f$ と $dx, dy, dz$ の「積」を取って、$f$ を偏微分で「ひっぺがした」ように見える。

そこで、次のような<strong>計算ルール</strong>を仮定してみよう。それは、$d$ が<strong>関数（0-form）と形式の積に対して、ライプニッツ則（積の微分法則）に似た振る舞いをする</strong>という要請だ。

1.  $d(f \omega) = (df) \wedge \omega + f \wedge (d\omega)$ （ただし $f$ は0-form, $\omega$ は任意の形式）
2.  特に、$\omega$ が0-form（つまり関数 $g$）の場合、$d(f g)$ は通常の積の微分法則 $d(fg) = g\,df + f\,dg$ と整合することを望む。
3.  $d$ は線形性を持つ： $d(\omega_1 + \omega_2) = d\omega_1 + d\omega_2$。

この仮定のもとで、最も簡単な1-form $P\,dx$ に $d$ を作用させるとどうなるか試そう。上記のルール1（$f=P$, $\omega=dx$ と見る）を適用すると、
$$
d(P\,dx) = (dP) \wedge dx + P \wedge (d(dx)).
$$
ここで $dP$ は $P$ が0-formなので $dP = P_x dx + P_y dy + P_z dz$ である。また、$d(dx)$ は「$dx$ の微分」だが、$dx$ は定数係数1-form（デカルト座標では $[1,0,0]$）なので、その「変化」はどう定義すべきか？ 直感的には、定数関数の微分が0になるように、<strong>定数係数形式の微分は0</strong>と定義したい。つまり $d(dx)=0$, $d(dy)=0$, $d(dz)=0$ とする。

すると、
$$
\begin{aligned}
d(P\,dx) &= (P_x dx + P_y dy + P_z dz) \wedge dx + P \wedge 0 \\
&= P_x (dx \wedge dx) + P_y (dy \wedge dx) + P_z (dz \wedge dx).
\end{aligned}
$$
ウェッジ積の反対称性 $dx \wedge dx = 0$, $dy \wedge dx = -dx \wedge dy$ を使うと、
$$
\begin{aligned}
d(P\,dx) &= 0 - P_y (dx \wedge dy) + P_z (dz \wedge dx) \\
&= P_z (dz \wedge dx) - P_y (dx \wedge dy).
\end{aligned}
$$

<strong>見てほしい。</strong> 入力は1-form $P dx$（独立成分は1つ）だったが、出力は $dz \wedge dx$ と $dx \wedge dy$ の線形結合、すなわち2-form（独立成分は2つ）になった。まさに次元が1つ上がったのである。しかも、出力の係数 $P_z$ と $-P_y$ は、最初に違和感を覚えたあの $3 \times 3$ 行列
$$
\begin{pmatrix}
P_x & P_y & P_z \\
Q_x & Q_y & Q_z \\
R_x & R_y & R_z
\end{pmatrix}
$$
のうち、<strong>1行目（$P$ の勾配）からは直接は出てこない</strong>。代わりに、$P$ の $z$ 微分と $y$ 微分が、特定の組み合わせで現れている。これは、偏微分を単に並べるのではなく、<strong>交叉するように組み合わせる</strong>操作、つまり「回転（rot）」の萌芽である。

> <strong>【ここまでのチェックポイント】</strong>
> - 外微分 $d$ の動機は、静的測定器（微分形式）を「変化の方向」へと押し上げ、物理的微分量（勾配・回転・発散）を生成すること。
> - 0-form（関数）に対する $d$ は既知の全微分 $df = f_x dx + f_y dy + f_z dz$ である。これは0-form→1-formへの「次元上げ」操作。
> - 1-formへの $d$ を定義するために、<strong>ライプニッツ則に似た積の法則</strong>と、<strong>定数係数1-formの微分は0</strong>というルールを仮定した。
> - 具体的に $d(P\,dx)$ を計算すると、それが2-form $P_z (dz \wedge dx) - P_y (dx \wedge dy)$ となることを確認した。次元が上がり、係数は偏微分の交叉的組み合わせとなる。

---

## §4.2 昇格の現場 — 1-form → 2-form、2-form → 3-form

### 4.2.1 一般の1-formへの適用

前節で得た感触をもとに、一般の1-form
$$
\omega = P\,dx + Q\,dy + R\,dz
$$
に外微分 $d$ を作用させてみよう。線形性より、各項に別々に作用させて足せばよい。
$$
d\omega = d(P\,dx) + d(Q\,dy) + d(R\,dz).
$$
$d(P\,dx)$ は前節で計算済み。同様の計算を $d(Q\,dy)$ と $d(R\,dz)$ について行う：
$$
\begin{aligned}
d(Q\,dy) &= (dQ) \wedge dy = (Q_x dx + Q_y dy + Q_z dz) \wedge dy \\
&= Q_x (dx \wedge dy) + Q_y (dy \wedge dy) + Q_z (dz \wedge dy) \\
&= Q_x (dx \wedge dy) + 0 - Q_z (dy \wedge dz).
\end{aligned}
$$
$$
\begin{aligned}
d(R\,dz) &= (dR) \wedge dz = (R_x dx + R_y dy + R_z dz) \wedge dz \\
&= R_x (dx \wedge dz) + R_y (dy \wedge dz) + R_z (dz \wedge dz) \\
&= -R_x (dz \wedge dx) + R_y (dy \wedge dz) + 0.
\end{aligned}
$$
これらをすべて足し合わせ、基底2-form $dy \wedge dz$, $dz \wedge dx$, $dx \wedge dy$ の順に整理する：
$$
\begin{aligned}
d\omega &= \bigl( -Q_z (dy \wedge dz) + R_y (dy \wedge dz) \bigr) \\
&\quad + \bigl( P_z (dz \wedge dx) - R_x (dz \wedge dx) \bigr) \\
&\quad + \bigl( -P_y (dx \wedge dy) + Q_x (dx \wedge dy) \bigr) \\[4pt]
&= (R_y - Q_z)\, dy \wedge dz \;+\; (P_z - R_x)\, dz \wedge dx \;+\; (Q_x - P_y)\, dx \wedge dy.
\end{aligned}
$$

この結果は極めて示唆的である。入力の1-form $\omega = (P, Q, R)$ から出力の2-form $\eta = (A, B, C) = (R_y - Q_z,\; P_z - R_x,\; Q_x - P_y)$ が得られた。物理学を学んだ読者は、この係数の組 $(A, B, C)$ が<strong>ベクトル場 $(P, Q, R)$ の回転（rot）</strong> そのものであることに気付くだろう。つまり、<strong>外微分 $d$ は、1-formを2-formへ昇格させるとき、自動的に「回転」を計算してくれる</strong>のである。

### 4.2.2 具体計算：$d(f\,dx) = df \wedge dx$ の展開

前節の一般公式の特別な場合として、§4.1で途中まで計算した $d(f\,dx)$ を、改めて公式 $d(f\,dx) = df \wedge dx$（ライプニッツ則から）を使って最初から展開し、係数がどう組み合わさるかを追ってみよう。

$df = f_x dx + f_y dy + f_z dz$ であるから、
$$
d(f\,dx) = df \wedge dx = (f_x dx + f_y dy + f_z dz) \wedge dx.
$$
ウェッジ積の分配法則と反対称性を用いて展開する：
$$
\begin{aligned}
&= f_x (dx \wedge dx) + f_y (dy \wedge dx) + f_z (dz \wedge dx) \\
&= f_x \cdot 0 + f_y \cdot (-dx \wedge dy) + f_z (dz \wedge dx).
\end{aligned}
$$
したがって、
$$
d(f\,dx) = f_z (dz \wedge dx) - f_y (dx \wedge dy).
$$
これは、一般公式で $P=f, Q=0, R=0$ とした場合 $(P_z - R_x) = f_z$, $-(P_y - Q_x) = -f_y$ に一致する。

この計算過程で、$f_x (dx \wedge dx)$ の項が反対称性により <strong>消える</strong> ことが決定的だ。もしウェッジ積が対称（$dx \wedge dx \neq 0$）だったら、$f_x$ という余計な項が残ってしまい、きれいな2-formにならない。<strong>外微分 $d$ が生成する形式が自動的に反対称（高次形式）となる秘密は、ライプニッツ則とウェッジ積の反対称性が織りなす必然の産物</strong>なのである。

### 4.2.3 2-formから3-formへ — 発散の出現

同じルールを2-formに適用しよう。一般の2-formは
$$
\eta = A\,dy \wedge dz + B\,dz \wedge dx + C\,dx \wedge dy
$$
と書ける。これに $d$ を作用させる。線形性から、各項ごとに計算する。まず第一項：
$$
d(A\,dy \wedge dz) = (dA) \wedge (dy \wedge dz) + A \wedge d(dy \wedge dz).
$$
ここで $d(dy \wedge dz)$ を計算する必要がある。ライプニッツ則を再帰的に適用すると、
$$
d(dy \wedge dz) = (d(dy)) \wedge dz + dy \wedge (d(dz)) = 0 \wedge dz + dy \wedge 0 = 0.
$$
したがって、$d(A\,dy \wedge dz) = (dA) \wedge (dy \wedge dz)$ となる。$dA = A_x dx + A_y dy + A_z dz$ だから、
$$
(dA) \wedge (dy \wedge dz) = (A_x dx + A_y dy + A_z dz) \wedge dy \wedge dz.
$$
これを展開する。分配法則を使い、3-formにおけるウェッジ積の反対称性（同じ基底が2回出ると0）に注意する：
$$
\begin{aligned}
&= A_x (dx \wedge dy \wedge dz) + A_y (dy \wedge dy \wedge dz) + A_z (dz \wedge dy \wedge dz) \\
&= A_x (dx \wedge dy \wedge dz) + 0 + 0.
\end{aligned}
$$
すなわち、
$$
d(A\,dy \wedge dz) = A_x (dx \wedge dy \wedge dz).
$$
全く同様に、
$$
d(B\,dz \wedge dx) = B_y (dx \wedge dy \wedge dz), \quad d(C\,dx \wedge dy) = C_z (dx \wedge dy \wedge dz).
$$
これらを足し合わせると、
$$
d\eta = (A_x + B_y + C_z)\, dx \wedge dy \wedge dz.
$$

ここに現れた係数 $A_x + B_y + C_z$ は、2-formの係数 $(A, B, C)$ の<strong>発散（div）</strong> に他ならない。<strong>外微分 $d$ は、2-formを3-formへ昇格させるとき、自動的に「発散」を計算してくれる</strong>のである。

### 4.2.4 第2章の直感との整合性

第2章で我々は、2-formを「2つのベクトルの絡み合いを測る反対称行列」と定義した。外微分 $d$ が1-formから作り出した2-form $d\omega = (R_y - Q_z) dy\wedge dz + \dots$ は、まさにそのような反対