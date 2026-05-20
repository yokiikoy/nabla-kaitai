---
title: "第3章：曲がったものを測る——形式の積分"
series: ナブラ解体新書 - 行列表示の微分形式によるベクトル解析の抜け道 -
chapter: 3 / 11
---

# 第3章：曲がったものを測る——形式の積分

#### §3.1 曲がったものを測る——小学校以来の借りを返す

第2章では、平行四辺形の面積や平行六面体の体積といった平らな図形の測り方を定義した。$${dx \wedge dy}$$ という面積測定器に二本のベクトルを食わせれば符号付き面積が返り、$${dx \wedge dy \wedge dz}$$ という体積測定器に三本のベクトルを食わせれば符号付き体積が返る。小学校の「$${1 \times 1}$$ の正方形がいくつ入るか」という直感を、代数的な測定器として再設計したのである。

しかし、物理学者が本当に知りたいのは平らな図形ではない。曲線の長さ、曲面の面積、曲がった領域の体積——すなわち曲がったものの測り方だ。

円周 $${2\pi r}$$、球の表面積 $${4\pi r^2}$$、球の体積 $${\frac{4}{3}\pi r^3}$$。これらの公式は小学校以来「そういうもの」として使ってきた。だが、部分に刻んで足し上げる操作として——積分として——一度でも定義したことがあるだろうか。ないはずだ。

考えてみれば当然である。曲線を細かく刻んで足し上げるには「各小区間で何を測り、どう足すか」を決めなければならないが、それは微分形式という測定器なしには定義できない操作だからだ。いま我々の手元には、第1章と第2章で作り上げた測定器——$${0}$$-form、$${1}$$-form、$${2}$$-form、$${3}$$-form——がそろっている。本章の仕事は、これらを曲線・曲面・領域に沿って適用し、集計することである。

原理はどの次数でも同じだ。まずは係数1の体積測定器がそのまま領域の体積を返してくれるケースから始め、次元を降りながら「どこで係数1の限界が姿を現すか」を確かめていこう。

以下では、パラメータ表示は滑らかとし、向きの反転や自己交差などの細部は「物理でよく使う状況では問題にならない」レベルに留める。厳密な可積分論は本書の射程外である。

---

### §3.2 体積——3次元、係数1

#### 3.2.1 直方体から曲がった領域へ——リーマン和で定義する

第2章 §2.5 で、我々は $${dx \wedge dy \wedge dz}$$ という体積測定器を組み立てた。これに三本のベクトル $${\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3}$$ を食わせると、それらが張る平行六面体の符号付き体積が返ってくる。

いま、空間内の領域 $${V}$$ の体積を測りたい。$${V}$$ の形がどんなに曲がっていても、十分細かく刻めば各小片はほぼ直方体と見なせる。そこで $${V}$$ を $${x}$$ 方向・$${y}$$ 方向・$${z}$$ 方向に刻み、$${V}$$ の内部にある小直方体に番号 $${i}$$ を振る。第 $${i}$$ 小直方体の三辺を


$$
\Delta x_i \hat{e}_x,\quad \Delta y_i \hat{e}_y,\quad \Delta z_i \hat{e}_z
$$


とする。これら三本のベクトルを体積測定器 $${dx \wedge dy \wedge dz}$$ に食わせると：


$$
(dx \wedge dy \wedge dz)(\Delta x_i \hat{e}_x, \Delta y_i \hat{e}_y, \Delta z_i \hat{e}_z) = \det\begin{pmatrix}\Delta x_i & 0 & 0 \cr 0 & \Delta y_i & 0 \cr 0 & 0 & \Delta z_i\end{pmatrix} = \Delta x_i \Delta y_i \Delta z_i
$$



---

【注】（はかりと図形の縮約）

ここで起きていることは、第2章 §2.5.10 で見たパターンそのものだ。$${3}$$-form（体積測定器＝はかり）が$${3}$$-vector（体積素＝図形）を食べてスカラーを吐き出す。この縮約が各小直方体で行われる。

---


各小直方体から得られたスカラー $${\Delta x_i \Delta y_i \Delta z_i}$$ を、$${V}$$ の内部にあるすべての小直方体について足し上げる：


$$
\sum_{\text{小直方体 }i \subset V} \Delta x_i \Delta y_i \Delta z_i
$$


そして刻みを無限に細かくする極限をとる。この極限を


$$
\iiint_V dx \wedge dy \wedge dz
$$


と書くことにする。これが $${3}$$-form の積分——体積分——の定義である。


---

【注】（$${\iiint}$$ という記号について）

本書では $${\iiint_V}$$ を「3次元領域 $${V}$$ における $${3}$$-form の積分」を表す記号としてここで初めて定義する。高校数学の延長にある何かではなく、上記のリーマン和の極限に与えた名前である。

---


さて、定義はした。ではこの和を実際にどう計算するか。$${V}$$ が $${x^2+y^2+z^2 \le R^2}$$ のような曲がった領域のとき、どの小直方体が $${V}$$ の内部にあるかを判定しながら和をとるのは面倒だ。しかし和のとり方を工夫すれば、見通しがよくなる。次節で実際にやってみよう。

#### 3.2.2 球の体積——泥臭く、愚直に足す

半径 $${R}$$ の球 $${x^2 + y^2 + z^2 \le R^2}$$ の体積を、本当に泥臭く計算してみよう。これから示したいことはただ一つ——特別な座標系に逃げずとも、$${x, y, z}$$ のまま愚直にリーマン和を整理するだけで、見慣れた $${\frac{4}{3}\pi R^3}$$ に到達できることである。特別な座標系は使わない。$${x, y, z}$$ のまま、小直方体 $${\Delta x \Delta y \Delta z}$$ を愚直に積み重ねるだけだ。

§3.2.1 のリーマン和をどう整理すれば計算できるか。球の内部で $${z}$$ をある値に固定すると、$${x, y}$$ の満たすべき条件は $${x^2 + y^2 \le R^2 - z^2}$$ である。さらに $${y}$$ も固定すれば $${x^2 \le R^2 - z^2 - y^2}$$。したがって $${x}$$ の動く範囲は $${-\sqrt{R^2 - z^2 - y^2}}$$ から $${+\sqrt{R^2 - z^2 - y^2}}$$ まで、$${y}$$ の範囲は $${-\sqrt{R^2 - z^2}}$$ から $${+\sqrt{R^2 - z^2}}$$ まで、$${z}$$ の範囲は $${-R}$$ から $${+R}$$ まで。この順に和をとる——第1章 §1.2 でやった1次元のリーマン和を三回重ねる——と考えれば、極限では：


$$
\iiint_V dx \wedge dy \wedge dz = \int_{-R}^{R} \Biggl( \int_{-\sqrt{R^2 - z^2}}^{\sqrt{R^2 - z^2}} \Biggl( \int_{-\sqrt{R^2 - z^2 - y^2}}^{\sqrt{R^2 - z^2 - y^2}} dx \Biggr) dy \Biggr) dz
$$


右辺の $${dx, dy, dz}$$ は、左辺の $${dx \wedge dy \wedge dz}$$ を順に和の整理に使った結果として並んでいる。$${\wedge}$$ を省略しているのではない。カッコの内側から順に、$${x}$$ についての和（$${\int dx}$$）→ $${y}$$ についての和（$${\int dy}$$）→ $${z}$$ についての和（$${\int dz}$$）を実行する、という意味である。

一番内側の $${x}$$ についての和（極限で $${x}$$ 積分）はすぐに実行できる：


$$
\int_{-\sqrt{R^2 - z^2 - y^2}}^{\sqrt{R^2 - z^2 - y^2}} dx = 2\sqrt{R^2 - z^2 - y^2}
$$


次に $${y}$$ 積分。$${a = \sqrt{R^2 - z^2}}$$ とおけば：


$$
\int_{-a}^{a} 2\sqrt{a^2 - y^2} dy
$$


ここで置換積分（高校数学）を使う。$${y = a\sin t}$$ とおくと、$${dy = a\cos t dt}$$。$${y}$$ が $${-a \to a}$$ のとき $${t}$$ は $${-\pi/2 \to \pi/2}$$。また $${\sqrt{a^2 - y^2} = \sqrt{a^2 - a^2\sin^2 t} = a\cos t}$$（$${t \in [-\pi/2,\pi/2]}$$ では $${\cos t \ge 0}$$ だから絶対値が外れる）。したがって：


$$
\begin{aligned}
\int_{-a}^{a} 2\sqrt{a^2 - y^2} dy
&= \int_{-\pi/2}^{\pi/2} 2\cdot a\cos t \cdot a\cos t dt \\
&= 2a^2\!\int_{-\pi/2}^{\pi/2} \cos^2 t dt
\end{aligned}
$$


$${\cos^2 t = (1 + \cos 2t)/2}$$ だから：


$$
\begin{aligned}
2a^2\!\int_{-\pi/2}^{\pi/2} \frac{1 + \cos 2t}{2} dt
&= a^2\int_{-\pi/2}^{\pi/2} (1 + \cos 2t) dt \\[4pt]
&= a^2\Bigl[t + \frac{\sin 2t}{2}\Bigr]_{-\pi/2}^{\pi/2} \\[4pt]
&= a^2\Bigl[\Bigl(\frac{\pi}{2} + 0\Bigr) - \Bigl(-\frac{\pi}{2} + 0\Bigr)\Bigr] \\[4pt]
&= \pi a^2 = \pi(R^2 - z^2)
\end{aligned}
$$


最後に $${z}$$ 積分：


$$
\int_{-R}^{R} \pi(R^2 - z^2) dz = 2\pi\Bigl[R^2 z - \frac{z^3}{3}\Bigr]_{0}^{R} = 2\pi\cdot\frac{2R^3}{3} = \frac{4}{3}\pi R^3
$$



---

【注】（この計算の意味）

ここで我々がやったことは、§3.2.1 のリーマン和の整理にすぎない。$${x,y,z}$$ のまま、どの小直方体が球の内部にあるかを判定しながら和をとるかわりに、和の順序を $${x \to y \to z}$$ と整理した。各段階は第1章でやった1変数のリーマン和であり、極限で見慣れた1変数積分の計算になる。それだけである。測定器と図形の縮約を愚直に集計すれば $${\frac{4}{3}\pi R^3}$$ に到達する。

---


こうして、$${dx \wedge dy \wedge dz}$$ という一つの測定器の積分が、曲がった領域の体積 $${\frac{4}{3}\pi R^3}$$ を正しく与えることが確認できた。3次元では、係数1の体積測定器がそのまま体積を直接測れるのである。

【ここまでのチェックポイント】

- $${dx \wedge dy \wedge dz}$$ の積分とは、領域を小直方体に刻み、各小片の体積素を体積測定器に食わせた値を足し上げるリーマン和の極限である。$${\iiint_V}$$ は本書がこの極限に与えた記号である。
- 係数1でそのまま体積が測れる。球の体積 $${\frac{4}{3}\pi R^3}$$ が、リーマン和を $${x \to y \to z}$$ の順に整理することで得られる。特別な座標系は不要。
- 次節では次元を一つ下げ、曲面の面積を測る。

---

### §3.3 表面積——2次元、係数1

#### 3.3.1 平行四辺形から曲面へ

第2章 §2.4 で、我々は $${dx \wedge dy}$$ という面積測定器を組み立てた。これに二本のベクトル $${\mathbf{v}_1, \mathbf{v}_2}$$ を食わせると、それらが $${xy}$$ 平面に落とす影の符号付き面積が返ってくる。同様に $${dy \wedge dz}$$ は $${yz}$$ 平面への影、$${dz \wedge dx}$$ は $${zx}$$ 平面への影を測る。

では曲面の面積を測るにはどうすればよいか。まず平らな場合で確認しておこう。$${xy}$$ 平面に乗った単位正方形 $${\mathbf{r}(u,v) = (u, v, 0), 0 \le u,v \le 1}$$ を考える。$${\mathbf{r}_u = (1,0,0), \mathbf{r}_v = (0,1,0)}$$ だから、$${(dx \wedge dy)(\mathbf{r}_u, \mathbf{r}_v) = \det\begin{pmatrix}1&0\cr0&1\end{pmatrix} = 1}$$。全区間で集計すれば $${\iint_{[0,1]^2} 1 = 1}$$——正方形の面積だ。これは第2章の平らな平行四辺形の拡張にすぎず、面素という新しい道具が平らな面では正しく面積を返すことの確認である。

では曲面が曲がっていたらどうなるか。一般に、曲面 $${S}$$ が二つのパラメータ $${u, v}$$ で


$$
\mathbf{r}(u,v) = \bigl(x(u,v),  y(u,v),  z(u,v)\bigr)
$$


と表されているとする。$${u, v}$$ が平面内の領域 $${D}$$ を動くとき、$${\mathbf{r}(u,v)}$$ が曲面 $${S}$$ を描く。

曲面を小区画に刻む。$${u}$$ 方向に $${\Delta u}$$、$${v}$$ 方向に $${\Delta v}$$ だけ進んだときの変位ベクトルは、偏微分を使って


$$
\mathbf{r}_u = \frac{\partial \mathbf{r}}{\partial u},\qquad \mathbf{r}_v = \frac{\partial \mathbf{r}}{\partial v}
$$


と近似できる（$${\Delta u, \Delta v}$$ が十分小さいとき）。この二本が張る平行四辺形が、曲面の小片の近似だ。$${\mathbf{r}_u, \mathbf{r}_v}$$ が平行でなく、ちゃんと面を張っているとする。


---

【注】（偏微分に不慣れな読者へ）

$${\mathbf{r}_u}$$ は「$${v}$$ を止めて $${u}$$ だけを少し動かしたときの変位ベクトル」と思えばよい。第1章の $${\Delta x}$$ を2次元に拡張したものである。

---


この面素 $${\mathbf{r}_u \Delta u, \mathbf{r}_v \Delta v}$$ を面積測定器 $${dx \wedge dy}$$ に食わせる。$${u,v}$$ 方向の刻みに番号 $${i,j}$$ を振れば、第 $${(i,j)}$$ 小区画からの寄与は：


$$
(dx \wedge dy)(\mathbf{r}_u \Delta u, \mathbf{r}_v \Delta v) = (dx \wedge dy)(\mathbf{r}_u, \mathbf{r}_v) \Delta u \Delta v
$$


第2章 §2.4.4 の定義より：


$$
(dx \wedge dy)(\mathbf{r}_u, \mathbf{r}_v) = \det\begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \cr \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{pmatrix} = \frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \frac{\partial y}{\partial u}
$$



---

【注】（$${2}$$-form と $${2}$$-vector の縮約）

ここでも同じ構図だ。$${2}$$-form（面積測定器＝はかり）が$${2}$$-vector（面素＝図形）を食べてスカラー（影の面積）を返す。各小区画でこの縮約が行われる。

---


これを $${D}$$ 内のすべての小区画について足し上げる：


$$
\sum_{i,j} (\frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \frac{\partial y}{\partial u}) \Delta u \Delta v
$$


刻みを無限に細かくする極限を


$$
\iint_S dx \wedge dy
$$


と書くことにする。これが $${2}$$-form の積分——面積分——の定義である。構成は §3.2 の体積分と同じ型で、食わせるベクトルが2本になっただけだ。

#### 3.3.2 dx \wedge dy が測るもの——球面で試す

実際に球面で計算してみよう。半径 $${R}$$ の球面の上半分（$${z \ge 0}$$）を考える。この曲面は、$${x, y}$$ をそのままパラメータとして


$$
z = f(x,y) = \sqrt{R^2 - x^2 - y^2},\qquad x^2 + y^2 \le R^2
$$


と書ける（グラフ表示）。$${\mathbf{r}(x,y) = (x, y, f(x,y))}$$ とパラメータ表示すれば、偏微分は：


$$
\mathbf{r}_x = \frac{\partial \mathbf{r}}{\partial x} = \begin{pmatrix} 1 \cr[2pt] 0 \cr[2pt] \frac{\partial f}{\partial x} \end{pmatrix},\qquad \mathbf{r}_y = \frac{\partial \mathbf{r}}{\partial y} = \begin{pmatrix} 0 \cr[2pt] 1 \cr[2pt] \frac{\partial f}{\partial y} \end{pmatrix}
$$


ここで $${\frac{\partial f}{\partial x} = \dfrac{\partial f}{\partial x} = -\dfrac{x}{\sqrt{R^2 - x^2 - y^2}}, \frac{\partial f}{\partial y} = \dfrac{\partial f}{\partial y} = -\dfrac{y}{\sqrt{R^2 - x^2 - y^2}}}$$。

まず $${dx \wedge dy}$$ だけを曲面に食わせてみる：


$$
(dx \wedge dy)(\mathbf{r}_x, \mathbf{r}_y) = \det\begin{pmatrix} 1 & 0 \cr 0 & 1 \end{pmatrix} = 1
$$


したがって上半球面での $${dx \wedge dy}$$ の積分は：


$$
\iint_{S_{\text{upper}}} dx \wedge dy
$$


の計算は §3.2.2 の $${y}$$ 積分と同じ方法でできて（$${a}$$ を $${R}$$ と思えばまったく同じ）、結果は $${\pi R^2}$$ である。これは上半球を $${xy}$$ 平面に落とした影——半径 $${R}$$ の円板——の面積にほかならない。

下半球（$${z = -\sqrt{R^2 - x^2 - y^2}}$$）でも同様に計算すると、$${(dx \wedge dy)(\mathbf{r}_x, \mathbf{r}_y) = 1}$$ は変わらない（確かめてほしい）が、面の向きが裏返るために符号が反転し、積分は $${-\pi R^2}$$ になる。

したがって球面全体での $${dx \wedge dy}$$ の積分は $${\pi R^2 + (-\pi R^2) = 0}$$。上半球の影と下半球の影が打ち消し合ったのだ。これではっきりした：$${dx \wedge dy}$$ が測るのは「$${xy}$$ 平面への影の符号付き面積」であり、曲面の面積そのものではない。同様に、$${dy \wedge dz}$$ は $${yz}$$ 平面への影、$${dz \wedge dx}$$ は $${zx}$$ 平面への影を測る。

#### 3.3.3 三つの影から本当の面積へ

では曲面の本当の面積はどう測ればよいのか。各点で三つの面積測定器すべてに面素を食わせ、その結果を合成する。

上半球面で残り二つも計算しよう（§3.3.1 の $${u=x, v=y}$$ の例）：


$$
\begin{aligned}
(dy \wedge dz)(\mathbf{r}_x, \mathbf{r}_y) &= y_x z_y - y_y z_x = 0\cdot \frac{\partial f}{\partial y} - 1\cdot \frac{\partial f}{\partial x} = -\frac{\partial f}{\partial x} = \frac{x}{\sqrt{R^2 - x^2 - y^2}} \\[4pt]
(dz \wedge dx)(\mathbf{r}_x, \mathbf{r}_y) &= z_x x_y - z_y x_x = \frac{\partial f}{\partial x}\cdot 0 - \frac{\partial f}{\partial y}\cdot 1 = -\frac{\partial f}{\partial y} = \frac{y}{\sqrt{R^2 - x^2 - y^2}} \\[4pt]
(dx \wedge dy)(\mathbf{r}_x, \mathbf{r}_y) &= 1
\end{aligned}
$$


これら三つの値——$${A_{yz}, A_{zx}, A_{xy}}$$——が、各点での面素の向きと大きさの情報を完全にエンコードしている。第2章 §2.4.6 で見た「向き付き面積＝三つの基底 $${\hat{e}_y \wedge \hat{e}_z}$$ 等の線形結合」の曲面版である。

では、これら三つの「影」から曲面のスカラー面積を取り出す。やることは第2章 §2.4.7 の平行四辺形のときと一字一句同じ——三つの値の二乗和の平方根をとればよい：


$$
\begin{aligned}
\sqrt{A_{yz}^2 + A_{zx}^2 + A_{xy}^2}
&= \sqrt{\Bigl(\frac{x}{\sqrt{R^2 - x^2 - y^2}}\Bigr)^2 + \Bigl(\frac{y}{\sqrt{R^2 - x^2 - y^2}}\Bigr)^2 + 1^2} \\
&= \sqrt{\frac{x^2 + y^2}{R^2 - x^2 - y^2} + 1} \\
&= \sqrt{\frac{R^2}{R^2 - x^2 - y^2}}
= \frac{R}{\sqrt{R^2 - x^2 - y^2}}
\end{aligned}
$$


これをパラメータ領域 $${x^2 + y^2 \le R^2}$$ 全体で積分すれば、上半球面の面積が得られる：


$$
\iint_{x^2+y^2 \le R^2} \frac{R}{\sqrt{R^2 - x^2 - y^2}} dx \wedge dy = R\int_{-R}^{R}\int_{-\sqrt{R^2-x^2}}^{\sqrt{R^2-x^2}} \frac{dy}{\sqrt{R^2 - x^2 - y^2}} dx
$$



内側の $${y}$$ 積分。$${a = \sqrt{R^2 - x^2}}$$ とおく：


$$
\int_{-a}^{a} \frac{dy}{\sqrt{a^2 - y^2}}
$$


置換積分 $${y = a\sin t}$$ を使う（§3.2.2 と同じ手順）。$${dy = a\cos t dt}$$、$${\sqrt{a^2 - y^2} = a\cos t}$$、$${y}$$ が $${-a \to a}$$ のとき $${t}$$ は $${-\pi/2 \to \pi/2}$$：


$$
\int_{-a}^{a} \frac{dy}{\sqrt{a^2 - y^2}} = \int_{-\pi/2}^{\pi/2} \frac{a\cos t}{a\cos t} dt = \int_{-\pi/2}^{\pi/2} dt = \pi
$$


積分結果は $${a}$$ に依らず $${\pi}$$ になる。したがって：


$$
R\int_{-R}^{R} \pi dx = R \cdot \pi \cdot 2R = 2\pi R^2
$$


これが上半球面の面積。下半球面でも符号は一部反転するが二乗和は同じなので、同じく $${2\pi R^2}$$。よって球面全体の面積は：


$$
2\pi R^2 + 2\pi R^2 = 4\pi R^2
$$


見事に $${4\pi R^2}$$ が出た。第2章 §2.4.7 で平行四辺形の面積を三つの影から復元したのと、まったく同じパターンである。

#### 3.3.4 ここまででわかったこと

係数1の $${2}$$-form は、それ単独では曲面の面積を直接返さない。$${dx \wedge dy}$$ だけでは「$${xy}$$ 平面への影の面積」しか測れず、曲面の本当の面積を知るには三つの基底 $${2}$$-form の測定値を合成しなければならない。これは第2章の平行四辺形の面積のときとまったく同じ状況だ。

しかし、物理ではしばしば「各点でどの方向の影をどれだけ重視するか」を制御したくなる。たとえば、曲面を貫く流体の流れを測るとき、流れが $${x}$$ 方向に強ければ $${dy \wedge dz}$$（$${yz}$$ 平面への影）に大きな重みをかけたい。そのような場所ごとに変わる重み——係数——の必要性が、ここで自然に姿を現す。これが §3.5 への伏線である。

【ここまでのチェックポイント】

- 曲面積分は $${\iint_D \eta(\mathbf{r}_u, \mathbf{r}_v) du \wedge dv}$$。各小区画で面素を面積測定器に食わせてスカラーにし、集計する。
- $${dx \wedge dy}$$ は単独では $${xy}$$ 平面への影の面積を測る。球面全体では正味ゼロ（上半球と下半球の影が打ち消し合う）。
- 三つの基底 $${2}$$-form の測定値の二乗和の平方根をとれば曲面のスカラー面積が得られる。球面では $${4\pi R^2}$$。
- 次節ではさらに次元を下げ、曲線の長さを測る。そこで係数1の限界が最もはっきりと姿を現す。

---

### §3.4 曲線——1次元、係数1（限界があらわになる）

#### 3.4.1 直線から曲線へ——リーマン和で定義する

第1章で、我々は $${dx, dy, dz}$$ を「ベクトルを食べて各成分を返す $${1}$$-form（横ベクトル）」として定義した。$${dx = \begin{pmatrix}1&0&0\end{pmatrix}}$$、$${\mathbf{v} = \begin{pmatrix}\Delta x\cr\Delta y\cr\Delta z\end{pmatrix}}$$ のとき $${dx(\mathbf{v}) = \Delta x}$$ である。$${dy, dz}$$ も同様。

では曲線に沿ってこれらを適用し、集計すると何が出るか。曲線を時刻 $${t}$$ の関数として


$$
\gamma(t) = \bigl(x(t),  y(t),  z(t)\bigr),\qquad t \in [t_0, t_1]
$$


と表す。曲線を小区間に刻み、$${i}$$ 番目の小区間での変位ベクトルを $${\Delta\mathbf{r}_i = \gamma(t_i + \Delta t) - \gamma(t_i)}$$ とする。$${\Delta t}$$ が十分小さければ $${\Delta\mathbf{r}_i \approx \gamma'(t_i) \Delta t}$$ と近似できる。

各小区間で行列 $${dx}$$ を変位ベクトル $${\Delta\mathbf{r}_i}$$ に作用させる：


$$
dx(\Delta\mathbf{r}_i) = \begin{pmatrix}1&0&0\end{pmatrix} \begin{pmatrix}\Delta x_i \cr \Delta y_i \cr \Delta z_i\end{pmatrix} = \Delta x_i \approx \frac{dx}{dt} \Delta t
$$


これを全区間で足し上げる：


$$
\sum_i dx(\Delta\mathbf{r}_i) \approx \sum_i \frac{dx}{dt} \Delta t
$$


刻みを無限に細かくする極限を


$$
\int_\gamma dx
$$


と書くことにする。これが $${1}$$-form の積分——線積分——の定義である。


---

【注】（$${1}$$-form と $${1}$$-vector の縮約）

§3.2・§3.3 と同じく、$${1}$$-form（横ベクトル＝はかり）が$${1}$$-vector（縦ベクトル＝図形）を食べてスカラーを返す。各小区間でこの縮約を行い、集計する。次数が違うだけで原理は同じだ。

---


この極限は第1章 §1.3.5 の置換積分とまったく同じ形であり：


$$
\int_\gamma dx = \int_{t_0}^{t_1} \frac{dx}{dt} dt = x(t_1) - x(t_0)
$$


同様に $${\int_\gamma dy = y(t_1) - y(t_0)}$$、$${\int_\gamma dz = z(t_1) - z(t_0)}$$。すなわち$${dx, dy, dz}$$ という $${1}$$-form の線積分は、曲線の正味の変位——始点と終点の座標の差——を返す。

#### 3.4.2 円周で試す——弧長は出ない

確認しよう。半径 $${R}$$ の円を


$$
\gamma(t) = (R\cos t, R\sin t, 0),\qquad t \in [0, 2\pi]
$$


とパラメータ表示する。$${\gamma'(t) = (-R\sin t, R\cos t, 0)}$$ だから：


$$
\begin{aligned}
\int_\gamma dx &= \int_0^{2\pi} dx(\gamma'(t)) dt = \int_0^{2\pi} (-R\sin t) dt = R\bigl[\cos t\bigr]_0^{2\pi} = 0 \\[4pt]
\int_\gamma dy &= \int_0^{2\pi} dy(\gamma'(t)) dt = \int_0^{2\pi} (R\cos t) dt = R\bigl[\sin t\bigr]_0^{2\pi} = 0
\end{aligned}
$$


いずれもゼロである。閉曲線だから始点と終点が同じで、行きと帰りで打ち消し合う——当然の結果だ。

しかし、この円の弧長が $${2\pi R}$$ であることも我々は知っている。係数1の $${dx, dy}$$ だけではゼロになってしまうが、ではどうすれば弧長が出るのか。

各瞬間に $${dx, dy}$$ が測った値はすでに手元にある。$${dx(\gamma'(t)) = -R\sin t}$$、$${dy(\gamma'(t)) = R\cos t}$$。これらはスカラーだから、二乗して足すことができる：


$$
dx(\gamma'(t))^2 + dy(\gamma'(t))^2 = R^2\sin^2 t + R^2\cos^2 t = R^2
$$


その平方根をとれば、その瞬間の速さ $${|\gamma'(t)| = R}$$ が得られる。全区間で積分すれば：


$$
\int_0^{2\pi} \!\sqrt{dx(\gamma'(t))^2 + dy(\gamma'(t))^2} dt = \int_0^{2\pi} \!R dt = 2\pi R
$$


弧長 $${2\pi R}$$ が出た。ここで起きていることは重要だ——$${dx}$$ も $${dy}$$ も単独では閉曲線でゼロになったのに、それらの二乗和の平方根をとって積分すると、正しい弧長が姿を現した。係数1の $${1}$$-form にはなかった「長さを測る力」が、二乗和という代数的な組み換えによって回復されたのである。

弧長 $${2\pi R}$$ が出た。

ここで起きていることを整理しよう。各時刻 $${t}$$ で $${dx(\gamma'(t))}$$ と $${dy(\gamma'(t))}$$ という二つのスカラーを得て、それらの二乗和の平方根 $${\sqrt{dx(\gamma'(t))^2 + dy(\gamma'(t))^2}}$$ をとり、$${t}$$ で積分した。これはすなわち、「変位 $${\mathbf{v}}$$ に対して $${\sqrt{dx(\mathbf{v})^2 + dy(\mathbf{v})^2}}$$ を返す」という新しい $${1}$$-form を曲線上で積分したことにほかならない。この $${1}$$-form を $${ds}$$ と書く：


$$
ds(\mathbf{v}) = \sqrt{dx(\mathbf{v})^2 + dy(\mathbf{v})^2}
$$



---

【注】（記法について）

第1章 §1.2.6 の契約により、単独の $${dx}$$ は横ベクトル（演算子）であり、それ自体を二乗することはできない。$${dx(\mathbf{v})^2}$$ は、$${1}$$-form $${dx}$$ をベクトル $${\mathbf{v}}$$ に作用させて得たスカラーを二乗したものである。この区別を崩さないことが、本書の記法の一貫性を保つ。

---


この $${ds}$$ も立派な $${1}$$-form であり、$${\int_\gamma ds}$$ は $${1}$$-form の積分である。しかしながら、この $${ds}$$ を $${dx}$$ と $${dy}$$ の線形結合——$${\frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy}$$ の形——で書くことはできない。$${ds}$$ の定義には二乗和の平方根が含まれており、$${dx, dy}$$ について線形ではないからだ。


---

【注】（計量への伏線）

$${dx(\mathbf{v})^2 + dy(\mathbf{v})^2}$$ という「成分の二乗和」の形は、第2章 §2.4.7 で平行四辺形のスカラー面積を $${\sqrt{A_{yz}^2 + A_{zx}^2 + A_{xy}^2}}$$ と出したのと完全に並行である。この「ピタゴラスの組み合わせ方」の背後にあるのが計量（内積）であり、本書では第5章で正式に導入する。ここでは「$${dx, dy, dz}$$ の作用結果の二乗和の平方根をとれば、向きを捨てた正の大きさ（長さ・面積・体積）が得られる」という事実だけを押さえておけばよい。

---


#### 3.4.3 では 1-form で何が測れるのか

弧長は $${ds(\mathbf{v}) = \sqrt{dx(\mathbf{v})^2 + dy(\mathbf{v})^2}}$$ という $${1}$$-form の積分として測れた。しかし本書では計量を第5章まで封印しているから、いまは二乗和の平方根を使うこの形を正面から扱うことはできない。では、計量なしで $${dx, dy, dz}$$ の線形結合として書ける $${1}$$-form は、いったい何を測るのだろうか。

空間の各点に力の場 $${\mathbf{F}(x,y,z) = (F_x, F_y, F_z)}$$ が働いている。曲線に沿って質点を動かすとき、各小区間で力がする微小仕事は、力の変位方向成分と変位の大きさの積——すなわち $${F_x \Delta x + F_y \Delta y + F_z \Delta z}$$——である。これを全区間で足し上げたものが仕事 $${W = \int_\gamma \mathbf{F}\cdot d\mathbf{r}}$$ だ。

ここで重要なのは、力の成分 $${F_x, F_y, F_z}$$ は場所ごとに変わることである。体積（§3.2）や表面積（§3.3）では係数1で十分な部分が多かったが、仕事を測るには場所ごとに変わる係数が不可欠だ。これが係数の必然性をもっとも鮮明に示す。

これが、次節で係数を導入する動機である。

【ここまでのチェックポイント】

- $${dx, dy, dz}$$ の線積分は「正味の変位」を返す。閉曲線ではゼロ。
- 弧長は $${ds(\mathbf{v}) = \sqrt{dx(\mathbf{v})^2 + dy(\mathbf{v})^2}}$$ という $${1}$$-form の積分で計算できる。$${ds}$$ は $${dx, dy}$$ の線形結合では書けず、二乗和の平方根（計量）を必要とする（第5章）。
- 計量なしの $${1}$$-form（$${dx, dy, dz}$$ の線形結合）が測るのは「仕事」のような量である。→ §3.5 へ。

---

### §3.5 係数をつける——密度と幾何の積

#### 3.5.0 なぜ係数なのか——物理が要求する

§3.2〜§3.4 では、係数1の形式で曲がった図形を測ってきた。しかし現実の物理では、測定器に場所ごとに変わる重みを掛けたくなる場面が無数にある：

- 力の場（場所ごとに変わる）$${\times}$$ 変位 $${=}$$ 仕事
- 流速の場（場所ごとに変わる）$${\times}$$ 断面 $${=}$$ 流量
- 密度の場（場所ごとに変わる）$${\times}$$ 体積 $${=}$$ 質量

ここに共通する構造は明白だ。「場所ごとに変わる重み（$${0}$$-form ＝ スカラー場）」と「幾何的な測り方（$${k}$$-form）」の積が、一般の $${k}$$-form を構成する。第2章 §2.4.8 で「$${0}$$-form はベクトルを0本食べる測定器、すなわちスカラー場」と述べたのは、まさにこの布石である。

以下、1次元・2次元・3次元の順に、係数付き形式の積分を定義していく。

#### 3.5.1 一般の 1-form の線積分（仕事）

デカルト座標で、係数が点 $${(x,y,z)}$$ に依存するスカラー場 $${\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}}$$ をとり、


$$
\omega = \frac{\partial f}{\partial x}(x,y,z) dx + \frac{\partial f}{\partial y}(x,y,z) dy + \frac{\partial f}{\partial z}(x,y,z) dz
$$


を$${1}$$-form の一般形と呼ぶ。各 $${dx, dy, dz}$$ は第1章どおり、縦ベクトルから成分を読み取る横ベクトルである。係数 $${\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}}$$ は場所ごとに変わる重み——$${0}$$-form——である。

曲線 $${\gamma(t)}$$ に沿った積分は、§3.4.1 のリーマン和に係数を乗せるだけだ。各小区間の変位 $${\Delta\mathbf{r}_i}$$ に $${\omega}$$ を食わせると：


$$
\omega(\Delta\mathbf{r}_i) = \frac{\partial f}{\partial x} \Delta x_i + \frac{\partial f}{\partial y} \Delta y_i + \frac{\partial f}{\partial z} \Delta z_i \approx \bigl(\frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + \frac{\partial f}{\partial z}\frac{dz}{dt}\bigr) \Delta t
$$


ここで $${\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}}$$ は点 $${\gamma(t_i)}$$ での値。全区間で足し上げて極限をとる：


$$
\sum_i \omega(\Delta\mathbf{r}_i)  \xrightarrow{\Delta t \to 0} \int_{t_0}^{t_1} \bigl(\frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + \frac{\partial f}{\partial z}\frac{dz}{dt}\bigr) dt
$$


この極限を


$$
\int_\gamma \omega
$$


と書く。§3.4.1 の係数1の場合とまったく同じ型で、各瞬間に横ベクトル（係数付き $${1}$$-form）が縦ベクトル（$${\gamma'(t)}$$）を食べてスカラーを返し、それを集計している。これは第1章 §1.3.5 の $${F(x) dx}$$ を3次元に自然拡張しただけである。


---

【注】（ベクトル解析との対応）

ベクトル解析では、この量を $${\int_\gamma \mathbf{F}\cdot d\mathbf{r}}$$ と書く。本書の $${\int_\gamma \omega}$$ はそれと同じでありながら、場 $${\omega}$$ と経路 $${\gamma}$$ が記号上も明確に分離されている。

---


具体例を見よう。力場 $${\mathbf{F} = (y, x, 0)}$$ が、単位円 $${\gamma(t) = (\cos t, \sin t, 0), t \in [0, 2\pi]}$$ に沿ってする仕事を計算する。

$${\omega = y dx + x dy}$$ だから、係数は $${\frac{\partial f}{\partial x} = y, \frac{\partial f}{\partial y} = x}$$。曲線上では $${\frac{\partial f}{\partial x} = \sin t, \frac{\partial f}{\partial y} = \cos t}$$。また $${dx/dt = -\sin t, dy/dt = \cos t}$$ より：


$$
\omega(\gamma'(t)) = (\sin t)(-\sin t) + (\cos t)(\cos t) = -\sin^2\!t + \cos^2\!t = \cos 2t
$$


したがって：


$$
\int_\gamma \omega = \int_0^{2\pi} \cos 2t dt = \Bigl[\frac{1}{2}\sin 2t\Bigr]_0^{2\pi} = 0
$$


仕事がゼロになった。この力場は単位円に沿って正味の仕事をしないのである。

#### 3.5.2 一般の 2-form の面積分（流量）

同様に、三つのスカラー場 $${P, Q, R}$$ を係数とする一般の $${2}$$-form：


$$
\eta = P dy \wedge dz + Q dz \wedge dx + R dx \wedge dy
$$


曲面 $${\mathbf{r}(u,v)}$$ に沿った積分も、§3.3.1 のリーマン和に係数を乗せるだけだ。各小区画の面素 $${(\mathbf{r}_u \Delta u, \mathbf{r}_v \Delta v)}$$ に $${\eta}$$ を食わせる：


$$
\eta(\mathbf{r}_u \Delta u, \mathbf{r}_v \Delta v) = \bigl(P (dy \wedge dz) + Q (dz \wedge dx) + R (dx \wedge dy)\bigr)(\mathbf{r}_u, \mathbf{r}_v) \Delta u \Delta v
$$


全区画で足し上げて極限をとる。この極限を


$$
\iint_S \eta
$$


と書く。各点で面素を面積測定器 $${\eta}$$ が食べてスカラーを返し、それを $${D}$$ 全体で集計する点は §3.3 と同じである。

$${dy \wedge dz, dz \wedge dx, dx \wedge dy}$$ がそれぞれ各平面への「影の面積」を測ることは §3.3 で見た。係数 $${P, Q, R}$$ は、それらの影に場所ごとに変わる重みをつける役割を果たす。物理的には、$${(P, Q, R)}$$ が流速場の成分であり、$${\iint_S \eta}$$ が曲面を貫く流量（フラックス）に対応するが、この対応を厳密に整理するには計量（内積）が必要である。詳しくは第5章で行う。


---

【注】（ここではベクトル解析との対応は補助線）

流量との対応は、既にベクトル解析を知っている読者のための橋渡しにすぎない。本書の本線はあくまで「$${2}$$-form を食わせて集計する」という操作であり、ベクトル解析の知識がなくともこの先の議論に支障はない。

---


#### 3.5.3 一般の 3-form の体積分（総質量）

$${3}$$-form の一般形は、スカラー場 $${\rho(x,y,z)}$$ を係数として：


$$
\Omega = \rho(x,y,z) dx \wedge dy \wedge dz
$$


§3.2.1 のリーマン和に密度 $${\rho}$$ を乗せればよい。各小直方体の体積素に $${\Omega}$$ を食わせる：


$$
\Omega(\Delta x_i \hat{e}_x, \Delta y_i \hat{e}_y, \Delta z_i \hat{e}_z) = \rho(x_i,y_i,z_i) \Delta x_i \Delta y_i \Delta z_i
$$


全区間で足し上げて極限をとる。この極限を


$$
\iiint_V \Omega
$$


と書く。$${\rho=1}$$ なら §3.2 の係数1の場合に戻る。$${\rho}$$ が質量密度なら総質量、電荷密度なら総電荷を与える。$${3}$$-form の独立成分は $${dx \wedge dy \wedge dz}$$ の1つだけなので、「密度（$${\rho}$$）」と「体積の測り方（$${dx \wedge dy \wedge dz}$$）」がきれいに分離して見通しがよい。

#### 3.5.4 線・面・体の統一像

ここまでを俯瞰しよう。

| 対象 | 形式 | 積分の骨格 | 物理的意味の例 |
|:---:|:---|:---|:---|
| 曲線 $${\gamma}$$ | $${1}$$-form $${\omega}$$ | $${\displaystyle\int \omega(\gamma') dt}$$ | 仕事 |
| 曲面 $${S}$$ | $${2}$$-form $${\eta}$$ | $${\displaystyle\iint \eta(\mathbf{r}_u, \mathbf{r}_v) du \wedge dv}$$ | 流量 |
| 領域 $${V}$$ | $${3}$$-form $${\Omega}$$ | $${\displaystyle\iiint \Omega(\hat{e}_x,\hat{e}_y,\hat{e}_z)}$$ | 総質量 |

いずれも「$${k}$$-form（はかり）が $${k}$$-vector（図形）を食べてスカラーを返し、それを領域全体で集計する」という同一の型である。次数が上がるごとに食わせるベクトルの本数が増え、交代性が面積・体積の向きを司る。次数が違うだけで、原理はどこまでも同じだ。

【ここまでのチェックポイント】

- 一般の $${k}$$-form は「場所ごとに変わる重み（$${0}$$-form）」と「幾何的な測り方（基底 $${k}$$-form）」の積。
- 線積分 $${\int_\gamma \omega}$$ は仕事、面積分 $${\iint_S \eta}$$ は流量、体積分 $${\iiint_V \Omega}$$ は総質量に対応する。
- いずれも「はかりと図形の縮約 → 集計」という同一原理。次節では、これらの積分を別の座標で計算し直す方法——引き戻し——を導入する。

#### 3.5.5 積分の一般形

§3.2〜§3.4 で別々に定義した線積分、面積分、体積分は、実は一つのパターンにまとまる。$${k}$$-form $${\omega}$$ を $${k}$$ 次元領域 $${M}$$ 上で積分するという操作を、次元によらず


$$
\int_M \omega
$$


と書く。$${M}$$ が曲線（$${k=1}$$）なら $${\int_\gamma}$$、曲面（$${k=2}$$）なら $${\iint_S}$$、立体（$${k=3}$$）なら $${\iiint_V}$$ ——積分記号の重なりは $${M}$$ の次元で決まるにすぎない。中身は常に「小区分に刻む → $${k}$$-form を $${k}$$-vector に食わせる → 和 $${\sum}$$ → 極限」である。

本書の舞台は 3 次元空間だから $${k=1,2,3}$$ で十分だが、この式が $${k}$$ によらず成立するという事実は頭の片隅に置いておいて損はない。第 4 章で外微分 $${d}$$ を導入したとき、この統一的な見方がストークスの定理の一般形 $${\int_{\partial M} \omega = \int_M d\omega}$$ へと結実する。

---

### §3.6 引き戻し（pullback）——積分を別のデカルト座標で計算し直す

#### 3.6.1 置換積分は「別のデカルト座標」だった

第1章 §1.3.5 の置換積分を思い出そう：


$$
\int_a^b F(x) dx = \int_{t_0}^{t_1} F(x(t)) \frac{dx}{dt} dt
$$


左辺は「$${x}$$ という座標」の世界での積分。右辺は「$${t}$$ という座標」の世界での積分。どちらも直線の目盛りを持ったデカルト座標であることに注意してほしい。

すなわち置換積分とは：積分が難しい座標から、積分しやすい座標へ移し替える操作だったのである。右辺の $${F(x(t)) \frac{dx}{dt}}$$ は、元の世界の測定器 $${F(x) dx}$$ を $${t}$$ の世界用に焼き直した姿だ。

この「焼き直し」の考え方は、1次元の置換積分にとどまらず、多次元の曲面・領域の積分すべてに通用する。それが本節の主題——引き戻し（pullback）——である。

#### 3.6.2 変数変換の話に切り替わる——二つの世界

ここから変数変換の議論をする。本節で我々が理解したいのはこれだ：§3.2〜§3.5 で定義した曲線・曲面・領域上の積分を、より計算しやすい座標で実行する方法。

「別の世界」とは何か。平らな方眼紙の上に張られた、別のデカルト座標である。

二つの世界を対比してみよう：

|  | 元の世界（図形のある空間） | パラメータの世界（方眼紙） |
|:---|:---|:---|
| 座標軸 | $${(x, y, z)}$$ | $${(u, v, 0)}$$ や $${(r, \theta, z)}$$ |
| 図形 | 曲がった曲線・曲面・領域 | 平らな長方形・直方体 |
| グリッド | 図形に沿って歪んでいる | 真っ直ぐ等間隔 |
| 積分 | $${\int_\gamma \omega}$$（測りにくい） | $${\iint (\text{普通の }du \wedge dv\text{ 積分})}$$ |

元の世界で曲がった図形の上で積分するのは大変だ。しかしパラメータの世界は平らな方眼紙——ここで積分できればずっと楽である。

問題は一つだけある。元の世界に置いてある測定器（形式）をそのままパラメータの世界に持ち込んでも、目盛りが合わない。パラメータの世界の方眼紙は元の世界とは縮尺が違い、しかも場所によって伸び縮みしている。この伸び縮みを補正して、測定器をパラメータの世界用に焼き直す操作——それが引き戻し（pullback）であり、その補正を司るのが連鎖律である。

では、この「焼き直し」は具体的にどうやるのか。鍵は「パラメータの世界の一歩が、元の世界ではどれだけ進んだことになるか」を知ることだ。次節でそれを追う。

#### 3.6.3 連鎖律——パラメータの世界の「一歩」は、元の世界でどれだけ進むか

引き戻しの心臓部は連鎖律だ。まず直感から入れよう。

元の世界 $${(x,y,z)}$$ から、円柱座標 $${(r,\theta,z)}$$ への変換を考える（第1章 §1.5 で導入したものだ）：


$$
x = r\cos\theta,\qquad y = r\sin\theta,\qquad z = z
$$


この変換は3次元から3次元への写像である。パラメータの世界でも——第1章 §1.1 の物理学者として——変位は縦ベクトル、測定器は横ベクトル、作用の結果はスカラー、の型を崩さない。

パラメータの世界の変位を $${\mathbf{v} = \begin{pmatrix}\Delta r \cr \Delta\theta \cr \Delta z\end{pmatrix}}$$ とする。この世界の $${1}$$-form——$${r,\theta,z}$$ 成分を抜き出す横ベクトル——は


$$
dr = \begin{pmatrix}1&0&0\end{pmatrix},\quad d\theta = \begin{pmatrix}0&1&0\end{pmatrix},\quad dz = \begin{pmatrix}0&0&1\end{pmatrix}
$$


であり、$${dr(\mathbf{v}) = \Delta r, d\theta(\mathbf{v}) = \Delta\theta, dz(\mathbf{v}) = \Delta z}$$。

いま知りたいのは、元の世界の物差し $${dx = \begin{pmatrix}1&0&0\end{pmatrix}}$$（$${(x,y,z)}$$ 空間の横ベクトル）が、このパラメータの世界ではどのような横ベクトルとして表現されるか——すなわち、$${dx}$$ を $${dr, d\theta, dz}$$ の線形結合で書くとどうなるか、である。

- 純粋に $${r}$$ 方向の一歩 $${\mathbf{v}_r = \begin{pmatrix}\Delta r \cr 0 \cr 0\end{pmatrix}}$$ が元の世界の $${x}$$ 方向に効く量は約 $${\cos\theta \cdot \Delta r}$$。$${dx}$$ を $${dr, d\theta, dz}$$ で展開した形 $${dx = a dr + b d\theta + c dz}$$ を仮定すれば、$${dx(\mathbf{v}_r) = a \Delta r}$$。これが $${\cos\theta \cdot \Delta r}$$ に一致すべきだから $${a = \cos\theta}$$。
- 同様に $${\theta}$$ 方向の一歩 $${\mathbf{v}_\theta = \begin{pmatrix}0 \cr \Delta\theta \cr 0\end{pmatrix}}$$ から $${b = -r\sin\theta}$$。
- $${z}$$ 方向の一歩 $${\mathbf{v}_z = \begin{pmatrix}0 \cr 0 \cr \Delta z\end{pmatrix}}$$ から $${c = 0}$$（$${x = r\cos\theta}$$ は $${z}$$ に依存しないから）。

つまり、偏微分係数こそが、$${dx}$$ をパラメータ世界の横ベクトルで展開したときの成分にほかならない。したがって：


$$
dx = \frac{\partial x}{\partial r} dr + \frac{\partial x}{\partial \theta} d\theta + \frac{\partial x}{\partial z} dz = \cos\theta dr - r\sin\theta d\theta + 0\cdot dz
$$



---

【注】（横ベクトル×縦ベクトル→スカラー）

一般の一歩 $${\mathbf{v} = \begin{pmatrix}\Delta r \cr \Delta\theta \cr \Delta z\end{pmatrix}}$$ に対して：
$$dx(\mathbf{v}) = \cos\theta dr(\mathbf{v}) - r\sin\theta d\theta(\mathbf{v}) + 0\cdot dz(\mathbf{v}) = \cos\theta \Delta r - r\sin\theta \Delta\theta$$
$${dx}$$ は横ベクトル、$${\mathbf{v}}$$ は縦ベクトル、$${dx(\mathbf{v})}$$ はスカラー。第1章 §1.2.3 以来変わらぬこの型が、引き戻しのただ中でも保たれていることに注目してほしい。連鎖律とは、この「横ベクトルの基底を取り替える」操作にほかならない。

---


左辺の $${dx}$$ は元の世界の横ベクトル。右辺は「パラメータの世界の横ベクトル $${dr, d\theta, dz}$$ を使って $${dx}$$ を表現し直した」式である。これこそが引き戻しの基本操作だ。同じことを $${dy, dz}$$ についても行う。


$$
\begin{aligned}
dy &= \frac{\partial y}{\partial r} dr + \frac{\partial y}{\partial \theta} d\theta + \frac{\partial y}{\partial z} dz = \sin\theta dr + r\cos\theta d\theta + 0\cdot dz \\[4pt]
dz &= \frac{\partial z}{\partial r} dr + \frac{\partial z}{\partial \theta} d\theta + \frac{\partial z}{\partial z} dz = 0\cdot dr + 0\cdot d\theta + 1\cdot dz
\end{aligned}
$$


どの式も、左辺は $${(x,y,z)}$$ 空間の横ベクトル、右辺は $${(r,\theta,z)}$$ 空間の横ベクトルどうしの線形結合である。次元は常に3。型は常に「横ベクトル×縦ベクトル→スカラー」。これを崩さないことが、引き戻しを正しく理解する唯一の道である。

#### 3.6.4 置換積分を引き戻しの言葉で読み直す

§3.6.1 の置換積分の式を、いまの連鎖律の言葉で見直そう。

左辺の $${F(x) dx}$$ が「元の世界の測定器」、右辺の $${F(x(t)) \frac{dx}{dt} dt}$$ が「パラメータの世界に引き戻された測定器」である。引き戻しは二段階からなる：

1. 係数部分 $${F(x) \to F(x(t))}$$：座標を $${x}$$ から $${t}$$ に書き換えるだけ（$${0}$$-form の引き戻し）
2. 測定器部分 $${dx \to \frac{dx}{dt} dt}$$：連鎖律（§3.6.3 の1変数版）による展開

第1章 §1.5 でやった $${dx = \cos\theta dr - r\sin\theta d\theta}$$ は、まさにこの操作だった。あのとき無意識にやっていたことが、引き戻しという名で呼ばれるものの正体である。

#### 3.6.5 一般の 1-form の引き戻し——手順

一般の $${\omega = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz}$$ を引き戻す手順は三つだけ：

1. 連鎖律：$${dx, dy, dz}$$ をパラメータの全微分で展開する
2. 係数の代入：$${\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}}$$ にパラメータ表示を代入する
3. 足し合わせる

具体例で確認しよう。円柱座標 $${x = r\cos\theta, y = r\sin\theta, z = z}$$ のもとで、$${\omega = x dy - y dx}$$ を引き戻す。$${\frac{\partial f}{\partial z} = 0}$$ だから $${z}$$ 成分は自明だが、§3.6.3 の型に従い常に3成分で扱う。

まず $${dx, dy}$$ を §3.6.3 のとおり展開する：


$$
dx = \cos\theta dr - r\sin\theta d\theta,\qquad dy = \sin\theta dr + r\cos\theta d\theta
$$


係数は $${\frac{\partial f}{\partial x} = -y = -r\sin\theta, \frac{\partial f}{\partial y} = x = r\cos\theta}$$。これらを代入して：


$$
\begin{aligned}
\omega &= (r\cos\theta) dy - (r\sin\theta) dx \\
&= r\cos\theta (\sin\theta dr + r\cos\theta d\theta) - r\sin\theta (\cos\theta dr - r\sin\theta d\theta) \\
&= r\cos\theta\sin\theta dr + r^2\cos^2\theta d\theta - r\sin\theta\cos\theta dr + r^2\sin^2\theta d\theta \\
&= r^2(\cos^2\theta + \sin^2\theta) d\theta = r^2 d\theta
\end{aligned}
$$


引き戻した結果は $${r^2 d\theta}$$。第1章 §1.5 で見た $${-r\sin\theta}$$ の仲間が、今度は $${r^2}$$ として現れた。この $${r^2}$$ が、極座標での「角度方向の物差しの歪み」を表す係数である。

ここまで $${1}$$-form の引き戻しを見てきた——係数の代入と連鎖律による展開の二段階だけだった。次は、同じ手順を $${2}$$-form・$${3}$$-form に適用する。ウェッジ積 $${\wedge}$$ の交代性が式を劇的に簡単にしてくれることを、これから見よう。

#### 3.6.6 2-form・3-form の引き戻し

原理は同じだ。各 $${dx, dy, dz}$$ を連鎖律で展開し、ウェッジ積 $${\wedge}$$ の代数に従って整理する。

例として $${dx \wedge dy}$$ を二つのパラメータ $${u, v}$$ に引き戻してみよう：


$$
dx = \frac{\partial x}{\partial u} du + \frac{\partial x}{\partial v} dv,\qquad dy = \frac{\partial y}{\partial u} du + \frac{\partial y}{\partial v} dv
$$


この二つを $${\wedge}$$ でつなぐ：


$$
\begin{aligned}
dx \wedge dy &= (\frac{\partial x}{\partial u} du + \frac{\partial x}{\partial v} dv) \wedge (\frac{\partial y}{\partial u} du + \frac{\partial y}{\partial v} dv) \\
&= \frac{\partial x}{\partial u} \frac{\partial y}{\partial u} du \wedge du + \frac{\partial x}{\partial u} \frac{\partial y}{\partial v} du \wedge dv + \frac{\partial x}{\partial v} \frac{\partial y}{\partial u} dv \wedge du + \frac{\partial x}{\partial v} \frac{\partial y}{\partial v} dv \wedge dv
\end{aligned}
$$


ここで第2章 §2.4.4 の交代性——$${du \wedge du = 0}$$、$${dv \wedge dv = 0}$$、$${dv \wedge du = -du \wedge dv}$$——が効く：


$$
dx \wedge dy = (\frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \frac{\partial y}{\partial u}) du \wedge dv
$$


係数 $${\frac{\partial x}{\partial u} \frac{\partial y}{\partial v} - \frac{\partial x}{\partial v} \frac{\partial y}{\partial u}}$$ は、$${\mathbf{r}_u}$$ と $${\mathbf{r}_v}$$ が $${xy}$$ 平面に落とす影の面積である。これは §3.3.1 で曲面積分の定義に現れた式とまったく同じだ。つまり§3.2・§3.3 で我々が無意識にやっていた積分計算こそが、引き戻しだったのである。

$${3}$$-form も同様。各 $${dx, dy, dz}$$ を展開して $${\wedge}$$ でつなぎ、交代性で整理すればよい。

#### 3.6.7 体積の伸び縮み——グリッドの比率が自動で出る

ここが最も重要な帰結である。

新しい座標 $${(u,v,w)}$$ で等間隔のグリッドを切ることを考えよう。一マス $${\Delta u \times \Delta v \times \Delta w}$$ が、元の世界 $${(x,y,z)}$$ ではどれだけの体積に対応するのか。一般に場所によって伸び縮みしているから、比率を求めなければならない。

この比率を、引き戻しは自動的に教えてくれる。実際にやってみよう。

デカルト座標 $${(x,y,z)}$$ の体積測定器 $${dx \wedge dy \wedge dz}$$ を、極座標 $${(r,\theta,z)}$$ に引き戻す。§3.6.3 の展開式：


$$
dx = \cos\theta dr - r\sin\theta d\theta,\qquad dy = \sin\theta dr + r\cos\theta d\theta,\qquad dz = dz
$$


これらを $${\wedge}$$ でつなぐ：


$$
\begin{aligned}
dx \wedge dy \wedge dz &= (\cos\theta dr - r\sin\theta d\theta) \wedge (\sin\theta dr + r\cos\theta d\theta) \wedge dz
\end{aligned}
$$


二つの括弧を先に展開する。$${dr \wedge dr = 0}$$、$${d\theta \wedge d\theta = 0}$$ で多くの項が消え：


$$
\begin{aligned}
(\cos\theta dr - r\sin\theta d\theta) \wedge (\sin\theta dr + r\cos\theta d\theta)
&= \cos\theta \cdot r\cos\theta dr \wedge d\theta - r\sin\theta \cdot \sin\theta d\theta \wedge dr \\
&= r\cos^2\theta dr \wedge d\theta - r\sin^2\theta (-dr \wedge d\theta) \\
&= r(\cos^2\theta + \sin^2\theta) dr \wedge d\theta \\
&= r dr \wedge d\theta
\end{aligned}
$$


したがって：


$$
dx \wedge dy \wedge dz = r dr \wedge d\theta \wedge dz
$$


係数 $${r}$$ が出てきた。これがグリッドの比率——$${\Delta r \times \Delta\theta \times \Delta z}$$ の一マスに対応する元の世界での体積は $${r}$$ 倍——である。


---

【注】（$${r}$$ の次元）

$${\Delta r}$$ は長さの次元、$${\Delta\theta}$$ は無次元（ラジアン）、$${\Delta z}$$ は長さの次元。係数 $${r}$$ が長さの次元を1つ補うことで、積 $${r \Delta r \Delta\theta \Delta z}$$ が正しく体積（長さ³）の次元を持つ。これは第1章 §1.6.3 で見た「一次形式が次元を自動調整する」話の、体積版である。

---


ここで注目してほしいのは、この $${r}$$ を出すために角度の弧の長さ（$${r\Delta\theta}$$）といった幾何学的考察を一切していないことだ。$${dx, dy, dz}$$ を機械的に連鎖律で展開し、$${\wedge}$$ でつなぎ、交代性で整理しただけで、$${r}$$ が自動的に姿を現した。$${\cos^2\theta + \sin^2\theta = 1}$$ という代数的な恒等式が、すべての幾何を代行してくれたのである。

第1章 §1.5.3 で行列成分の中に潜んでいた $${r}$$ が、ここで「体積の伸び率 $${r}$$」として結実した。あのとき $${-r\sin\theta}$$ という一つの行列成分を見て感じた違和感の答えが、ここにある。

#### 3.6.8 どんな座標変換でも同じこと

一般に、デカルトの体積測定器 $${dx \wedge dy \wedge dz}$$ を任意の座標変換 $${(u,v,w) \mapsto (x,y,z)}$$ に引き戻すと、かならず次の形になる：


$$
\Phi^\ast(dx \wedge dy \wedge dz) = J(u,v,w) du \wedge dv \wedge dw
$$


$${J(u,v,w)}$$ は、各点でのグリッドの歪み具合——一マス $${\Delta u \Delta v \Delta w}$$ が元の世界で何倍の体積になるか——を表す一個の関数である。

数学ではこの $${J}$$ をヤコビ行列式、略してヤコビアンと呼ぶ。名前は知らなくてよい。知っていれば、いま見た $${r}$$ が極座標のヤコビアンの具体例だとわかるだろう。

$${J}$$ の正体を具体的に書けば、$${x,y,z}$$ を $${u,v,w}$$ で偏微分したものを並べた行列の行列式である。が、その式を覚える必要はない。毎回 $${dx, dy, dz}$$ を連鎖律で展開して $${\wedge}$$ でつなげば、必ずこの形が出てくるからだ。

したがって、$${3}$$-form の積分を別の座標で計算するときの規則


$$
\iiint_V f dx \wedge dy \wedge dz = \iiint_U f(\Phi(u,v,w)) |J(u,v,w)| du \wedge dv \wedge dw
$$


は、「元の世界の体積測定器を新しい座標に引き戻したら、グリッドの一マスが $${J}$$ 倍に歪んだ」という幾何的事実の、積分版にすぎない。右辺の絶対値 $${|J|}$$ は、向きを無視して正の体積だけを扱いたいときに使うもので、本質は符号付きの $${J}$$ のほうにある。


---

【注】（ベクトル解析を学んだ読者へ）

変数変換で「極座標にすると $${r dr d\theta}$$ が出る」と習ったとき、多くの教科書は「$${\theta}$$ 方向の弧の長さ $${r\Delta\theta}$$ を考えて、$${\Delta V \approx \Delta r \cdot r\Delta\theta \cdot \Delta z}$$」という幾何学的な説明をする。その説明に間違いはないが、引き戻しの立場では角度の弧の長さを一切考えなくてよい。連鎖律とウェッジ積の代数だけが、正しい比率を自動的に導く。

---


【ここまでのチェックポイント】

- 引き戻しとは「測定器（形式）をパラメータの世界に焼き直す」操作。連鎖律がそのすべてを司る。
- 第1章 §1.5 の $${dx = \cos\theta dr - r\sin\theta d\theta}$$ が引き戻しの原型。置換積分も同じ構造。
- $${dx \wedge dy \wedge dz}$$ を極座標に引き戻すと $${r dr \wedge d\theta \wedge dz}$$。グリッドの体積比率 $${r}$$ が、角度の考察なしに代数だけで出る。
- 一般の座標変換では $${J}$$（ヤコビアン）がグリッドの歪み率として現れる。

---

## 第3章 付録B：2次元で見るグリッドの引き戻し


---

【注】（本書のポリシーに反するが）

本書は第1章 §1.1 以来、一貫して「物理学者の3次元」にこだわってきた。しかし引き戻しによる面積要素の歪みは、3次元のままでは絵に描きづらい。この付録では補助線として、あえて実2次元 $${(x,y)}$$ に落としてグリッドの対応を目で追う。3次元の体積要素 $${dx \wedge dy \wedge dz}$$ から $${z}$$ を省略するので、厳密には本書の記法契約に反する——そのことを断ったうえで、直感を得るためのおまけとして読んでほしい。

---


### B.1 平面上の極座標——グリッドを重ねて見る

§3.6.3 と §3.6.7 で、$${dx \wedge dy \wedge dz = r dr \wedge d\theta \wedge dz}$$ という等式を代数的に導いた。係数 $${r}$$ が「グリッドの歪み率」だと言われても、式だけではぴんと来ない読者もいるだろう。ここでは $${z}$$ 方向を省略して、$${xy}$$ 平面だけで考えてみる。

変換は $${x = r\cos\theta, y = r\sin\theta}$$。元の世界の $${(x,y)}$$ 平面に、等間隔 $${\Delta x, \Delta y}$$ の正方形グリッドを切る。一マスの面積は $${\Delta x \Delta y}$$ であり、これは $${dx \wedge dy}$$ を一マスの二辺 $${(\Delta x \hat{e}_x, \Delta y \hat{e}_y)}$$ に食わせた値に等しい。

同じ領域をパラメータの世界 $${(r,\theta)}$$ で見ると、$${r}$$ が一定の線は原点を中心とする同心円、$${\theta}$$ が一定の線は原点から放射状に伸びる直線になる。このグリッドの一マスは、（$${\Delta r, \Delta\theta}$$ が小さいとき）ほぼ長方形だが、その大きさは場所によって変わる。

具体的に一マスを計算してみよう。$${r}$$ 方向の辺は長さ $${\Delta r}$$。$${\theta}$$ 方向の辺は、半径 $${r}$$ の円周上で角度 $${\Delta\theta}$$ に対する弧の長さ——約 $${r\Delta\theta}$$——である。したがって、一マスの面積は約 $${(r\Delta\theta) \times \Delta r = r \Delta r \Delta\theta}$$。

つまり、$${(x,y)}$$ 平面で面積 $${1}$$ だった正方形グリッドの一マスが、$${(r,\theta)}$$ 平面に移ると面積が $${r}$$ 倍に伸びる。場所 $${(r,\theta)}$$ によって伸び率が変わる——原点から遠いほど（$${r}$$ が大きいほど）一マスが大きくなる——のも、この $${r}$$ から読み取れる。

### B.2 代数が幾何を代行する

さて、上の説明では「$${\theta}$$ 方向の弧の長さは約 $${r\Delta\theta}$$」という幾何学的な考察をした。これは直感的でわかりやすいが、§3.6.7 で我々がやった計算はこれとはまったく違う——$${dx \wedge dy}$$ を連鎖律で展開し、$${dr \wedge dr = 0}$$ や $${d\theta \wedge d\theta = 0}$$ といった代数のルールだけで $${r dr \wedge d\theta}$$ を導いた。弧の長さのことは一言も考えていない。

これが引き戻しの威力だ。幾何学的直感が及ばない複雑な座標変換でも、連鎖律と $${\wedge}$$ の代数は同じ手順で正しいグリッド比率を算出する。$${r\Delta\theta}$$ と幾何で考えられるのは、たまたま極座標が単純だからにすぎない。


---

【注】（3次元への復帰）

本書の本文に戻れば、常に3次元である。$${dx \wedge dy}$$ だけでは「$${xy}$$ 平面への影の面積」しか測れず、§3.3 で見たように曲面の面積を得るには三つの $${2}$$-form の合成が必要だった。この付録はあくまで補助線であり、本文の記法契約（$${dx}$$ は常に3成分の横ベクトル）を一時的に緩めたものであることを理解されたい。

---


---

### §3.7 本章のまとめと第4章への展望

第I部「積分記号の尻尾の正体」の三段が、これで完結した：

1. 第1章：$${dx}$$ を行列（$${1}$$-form）と見なし、積分を行列作用の極限と読む
2. 第2章：ウェッジ積 $${\wedge}$$ で $${2}$$-form・$${3}$$-form を構成し、面積・体積を代数で測る
3. 第3章（本章）：曲線・曲面・領域に形式を適用し集計する（積分）。引き戻しで座標変換を統一的に扱い、グリッドの歪み率（ヤコビアン）が角度抜きで出ることを見る

本章で確立したのは、次の統一原理である：

$${k}$$-form（はかり）が $${k}$$-vector（図形）を食べてスカラーを返し、それを領域全体で集計する。次数が $${0,1,2,3}$$ と変わっても、この構図は不変だった。曲線上の仕事も、曲面上の流量も、領域内の総質量も——すべて同じ言語で書ける。

引き戻しは「積分を別のデカルト座標で計算し直す」技術であり、その核心は§3.6.3 で見た連鎖律の直感——「パラメータの世界の一歩が元の世界でどれだけ進むか」——に尽きる。ウェッジ積の交代性と組み合わせることで、極座標の体積比率 $${r}$$ や一般のヤコビアンが、幾何学的直感に頼らず機械的な代数計算だけで導かれる。

【ここまでのチェックポイント——第3章・第I部全体】

- $${1}$$-form $${\omega}$$ の線積分 $${\int_\gamma \omega}$$ は、$${\gamma'(t)}$$ に $${\omega}$$ を食わせて集計する操作。仕事は $${\int_\gamma \omega}$$ で、$${\mathbf{F}\cdot d\mathbf{r}}$$ と同じ量。
- $${2}$$-form $${\eta}$$ の面積分 $${\iint_S \eta = \iint_D \eta(\mathbf{r}_u, \mathbf{r}_v) du \wedge dv}$$。係数1では各平面への「影」を測り、三つの影を合成すればスカラー面積が得られる。一般には流量（フラックス）を測る。
- $${3}$$-form $${\Omega}$$ の体積分 $${\iiint_V \Omega}$$。係数1でそのまま体積、係数 $${\rho}$$ で総質量・総電荷。
- 引き戻し $${\Phi^\ast}$$ は「形式をパラメータ空間での影に焼き直す」操作。第1章 §1.5 の $${dx = \cos\theta dr - r\sin\theta d\theta}$$ がその具体例。
- $${3}$$-form の引き戻しにグリッドの体積比率（ヤコビアン）が現れ、変数変換公式の幾何的意味が説明できる。角度の考察は不要——連鎖律と $${\wedge}$$ の代数がすべてをやってくれる。

---

ここから先の第II部では、いよいよ外微分 $${d}$$ を導入する。$${d}$$ は形式の次数を1つ上げる線形演算子であり、勾配・回転・発散が一つの操作のバリエーションであることが明らかになる。積分側の言葉がそろったいま、微分側の代数を完成させる準備が整ったのである。
