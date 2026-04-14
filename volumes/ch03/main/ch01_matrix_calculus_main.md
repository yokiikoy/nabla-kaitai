---
title: "第1章：1次元の微積分を「行列」で解体する"
series: dx-matrix
chapter: 1
---

# 第1章：1次元の微積分を「行列」で解体する

#### §1.1 数学者の1次元、物理学者の1次元
高校で $\int f(x) dx$ という1次元の積分を習ったとき、<strong>教科書の記述では</strong>「$x$軸という1本の線」が置かれる。数学の教科書としてはそれで妥当だ。<strong>数学者</strong>は1次元空間 $\mathbb{R}^1$ という自己完結した抽象世界を仮定し、その上で論理を積み上げる。点は実数 $x$、変位は実数 $\Delta x$、積分は「関数×微小幅」の極限として定義される。すべてが完結している。
<strong>しかし、我々は物理学者である。</strong>
我々が扱う<strong>現実の物理空間は、常に3次元だ。</strong>質点が直線上を運動しているように見えても、それは「架空の1次元空間」にいるのではなく、「3次元空間 $\mathbb{R}^3$ の中で、たまたま $y$ 方向と $z$ 方向への変位が観測されない（あるいは無視できる）断面」を見ているに過ぎない。
例えば、摩擦のない直線レール上を滑る台車を考えよう。我々は「これは $x$ 軸方向の1次元運動だ」と言うが、実際には：
* レールは3次元空間内に設置されている
* 台車は微小に上下に揺れているかもしれない
* 空気抵抗による横方向の微小変動もある

物理学者の「1次元運動」とは、<strong>3次元空間内で特定の方向への変位が支配的であり、他の方向の変位が無視できるほど小さいか、系の対称性によって厳密にゼロに拘束されている状況</strong>を指す。
したがって、物理学者が「1次元の微小変位」と呼ぶものの真の姿は、単なるスカラー $\Delta x$ ではなく、次のような<strong>縦ベクトル（列ベクトル）</strong>で表すのがふさわしい：
$$\mathbf{v} = \begin{pmatrix} \Delta x \\ 0 \\ 0 \end{pmatrix}$$

> <strong>注</strong> 筆者は行と列の見分けに迷うので、本書全体を通して<strong>縦ベクトル・横ベクトル</strong>という言い方をする（縦が列、横が行、と対応させて読んでほしい）。

我々はこのように、3次元空間内の一点からの変位を3成分で表したものを<strong>変位ベクトル</strong>と呼ぶ。成分の並びは慣習に従い、<strong>第1成分が $x$ 軸方向、第2が $y$ 軸方向、第3が $z$ 軸方向</strong>の変位に対応するものとする。

この第2成分・第3成分のゼロは、「無視されている」あるいは「存在しない」という消極的な意味ではない。<strong>「我々が今、$x$軸方向の運動だけに注目し、他の成分を測定対象から意図的に除外している」という積極的な選択の結果</strong>なのである。
この「物理学者としての3次元前提」こそが、積分記号の末尾にへばりついている $dx$ という記号の真の姿を暴き出す鍵となる。次節では、この視点から <strong>$dx$ を「微小量」から「行列」へと解体していく。</strong>

---

### §1.2 リーマン積分のベクトル解剖 — 区分求積法を行列作用として見る
前節で、物理的な微小変位を縦ベクトル $\mathbf{v} = \begin{pmatrix} \Delta x \\ 0 \\ 0 \end{pmatrix}$ と捉え直した。この視点を持って、今度は高校以来慣れ親しんだリーマン積分のプロセスを徹底的に解体し、その中に潜む「行列としての $dx$」を炙り出してみよう。

> <strong>注</strong> 数学や他文献では、縦ベクトルの成分を横に並べ、右上に ${}^T$ を添えて略記することもある（列ベクトルを行として見せる）。<strong>本書の第1章では縦ベクトルは主に $\begin{pmatrix}\cdots\end{pmatrix}$ で書き統一する。</strong> 他書や後の章で ${}^T$ が出たときは、転置の記号として読んでほしい。

#### 1.2.1 リーマン和の標準的構成（復習）
関数 $f(x)$ の区間 $[a, b]$ における定積分は、次のように定義される：

> <strong>注</strong> 記号 $[a,b]$ は、端点 $a$ と $b$ を両方含む<strong>閉区間</strong>（$a \le x \le b$ の実数 $x$ の集合）を表す。数学の教科書で慣れていない読者のために明示しておく。

1. 区間を $n$ 個の小区間に分割： $a = x_0 < x_1 < \cdots < x_n = b$
2. 小区間の幅を $\Delta x_i = x_i - x_{i-1}$
3. 各小区間 $[x_{i-1}, x_i]$ の<strong>中から</strong>代表点 $\xi_i$ を1つ選ぶ
4. リーマン和 $R_n = \sum_{i=1}^n f(\xi_i) \Delta x_i$ を作る（この $n$ 分割に対する和を $R_n$ と書く）
5. 分割を細かくする極限をとる： $\int_a^b f(x)dx = \lim_{n\to\infty} R_n$

この教科書的な説明では、$\Delta x_i$ は「微小な幅」というスカラー量だ。しかし、我々はもう一歩踏み込めるはずだ。

#### 1.2.2 小区間ごとの変位
第 $i$ 小区間 $[x_{i-1}, x_i]$ における変位は、§1.1 の<strong>変位ベクトル</strong>を、その区間の幅に合わせて
$$\mathbf{v}_i = \begin{pmatrix} \Delta x_i \\ 0 \\ 0 \end{pmatrix}$$
と書けばよい。添字 $i$ は「第 $i$ 小区間の分」という意味だけで、$\mathbf{v}_i$ もまた変位ベクトルである。今は直線運動を考えているので $y,z$ 成分はゼロだが、それは条件ではなく結果としてゼロになっているだけだ。

#### 1.2.3 $dx$ の登場 — 本書最大の特徴としての「断言」
さて、本書では $dx$ という記号に次のような意味を与える。<strong>大胆で奇妙に思えるかもしれないが、これが本書最大の特徴でもある——我々は $dx$ を次の $1\times 3$ <strong>行列</strong>だと断言する。</strong>

すなわち、<strong>横ベクトル</strong>（$1\times 3$ <strong>行列</strong>として成分を横に並べて書く）として
$$dx = \begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$$
と置く。

> <strong>注（成分並びの約束）</strong> 横ベクトル（行）や行成分の略記は <strong>$(1\ 0\ 0)$</strong> のように<strong>コンマを打たず</strong>、成分の間だけを区切って書く。<strong>$(1, 0, 0)$</strong> のように<strong>コンマのあとにスペース</strong>を入れる書き方は<strong>座標</strong>（点の位置など）を強調するときに用い、<strong>行列・横ベクトルの略記には使わない</strong>。

変位ベクトル $\mathbf{v}_i$ に左から掛けると
$$dx\,\mathbf{v}_i = \begin{pmatrix} 1 & 0 & 0 \end{pmatrix} \begin{pmatrix} \Delta x_i \\ 0 \\ 0 \end{pmatrix} = \Delta x_i$$
となる。ここで「$dx$ が変位ベクトル $\mathbf{v}_i$ を食べてスカラー $\Delta x_i$ を吐く」というイメージを、<strong>関数の値のように書く</strong>ことにする：
$$dx(\mathbf{v}_i) := dx\,\mathbf{v}_i = \Delta x_i$$
<strong>本書では、しばしばこの $dx(\mathbf{v})$ の形で「横ベクトル $dx$ が縦ベクトル $\mathbf{v}$ に作用する」と強調する。何度繰り返しても強調しすぎることはない。</strong>

> <strong>注</strong> この $dx(\mathbf{v})$ を<strong>関数</strong>と呼ぶか<strong>演算子</strong>と呼ぶか<strong>写像</strong>と呼ぶかは、文献によってさまざまな流儀がある。筆者は<strong>演算子</strong>と呼ぶことを好むので、この先も演算子と呼ぶことが多いだろう。

> <strong>注</strong> 数学者は、$dx$ を「座標に依存しない幾何学的主体」として語ることも多い。いま書いた $\begin{pmatrix}1&0&0\end{pmatrix}$ はデカルト座標での表示にすぎない。<strong>§1.5 で成分が場所とともに変わる話をきちんと触れる</strong>ので、ここでは落ち着いて読み進めてほしい。

リーマン和に現れる $\Delta x_i$ は、「1次元の謎の微小量」ではない。<strong>3次元空間の中での変位ベクトル $\mathbf{v}_i$ に対し、上の行列としての $dx$ が $x$ 成分だけを抜き出した結果</strong>である。

<strong>これが決定的な瞬間だ</strong>：
* 左辺：$dx(\mathbf{v}_i)$ は、行列 $dx$ が<strong>変位ベクトル $\mathbf{v}_i$ に</strong>作用する代数的操作
* 右辺：従来のリーマン和に現れる「小区間の幅 $\Delta x_i$」

つまり $\Delta x_i$ は、<strong>1次元の謎の微小変位ではなく、3次元の微小変位 $\mathbf{v}_i$ から $x$ 方向の成分だけを取り出した $dx(\mathbf{v}_i)$ である</strong>。

#### 1.2.4 リーマン和のベクトル再解釈と積分記号
この視点でリーマン和を書き直すと：
$$R_n = \sum_{i=1}^n f(\xi_i) \cdot dx(\mathbf{v}_i)$$

さらに、各小区間で
$$f(\xi_i)\,dx = \begin{pmatrix} f(\xi_i) & 0 & 0 \end{pmatrix}$$
とおけば（スカラー $f(\xi_i)$ が各行をスケールする）、
$$\bigl(f(\xi_i)\,dx\bigr)(\mathbf{v}_i) = f(\xi_i) \cdot dx(\mathbf{v}_i) = f(\xi_i)\,\Delta x_i$$
であり、リーマン和の各項そのものが得られる：
$$R_n = \sum_{i=1}^n \bigl(f(\xi_i)\,dx\bigr)(\mathbf{v}_i)$$

分割を無限に細かくする極限では、リーマン積分の定義より
$$\int_a^b f(x)\,dx = \lim_{n\to\infty} R_n = \lim_{n\to\infty} \sum_{i=1}^n \bigl(f(\xi_i)\,dx\bigr)(\mathbf{v}_i)$$
左辺の $\int_a^b f(x)\,dx$ は、<strong>高校数学で「積分記号と $dx$ をセットで置く」ことに慣れているであろう</strong>あの記号そのものである——すなわち、上の手順5で書いた $\lim_{n\to\infty} R_n$ と同じ量だ。右辺は、<strong>各小区間で「行列 $f(\xi_i)\,dx$ を変位ベクトルに作用させた値」を足し上げたものの極限</strong>という、同じ積分の別顔だ。

#### 1.2.5 物理的解釈 — 仕事の計算を例に
直線上の質点に力 $F(x)$ が作用する場合の仕事を考えよう。力学を学んだ読者であれば
$$W = \int_a^b F(x)\,dx$$
という表現を知っているだろう。本書の流儀で行列表現すると、
$$W = \lim_{n\to\infty} \sum_{i=1}^n \bigl(F(\xi_i)\,dx\bigr)(\mathbf{v}_i) = \int_a^b F(x)\,dx$$
である。左は<strong>リーマン和を行列作用で書いた極限</strong>、右は<strong>慣用の積分記号</strong>であり、<strong>同じ量</strong>を二通りに表している。ここで $\mathbf{v}_i$ は各小区間の変位ベクトルである。

$F(x)\,dx = \begin{pmatrix} F(x) & 0 & 0 \end{pmatrix}$ は演算子であり、$\bigl(F(x)\,dx\bigr)(\mathbf{v}) = F(x)\,\Delta x$ が一次近似としての微小仕事になる。

この視点の強みは、<strong>力が $y$ 方向にも成分を持つ一般的な場合に自然に拡張できる</strong>点だ。次章で $dy$ を導入すれば、$F_x dx + F_y dy$ という形で2次元の仕事を統一的に扱える。

#### 1.2.6 一次形式（1-form）

ここまで、我々は $dx$ を「変位ベクトルに作用して特定の成分を抽出し、スカラー（実数）を返す横ベクトル」として定義してきた。このような、ベクトルを食べてスカラーを吐き出す<strong>線形</strong>な測定器のことを、微分幾何学や現代物理学では<strong>一次形式（1-form）</strong>と呼ぶ。本稿で「行列としての $dx$」と呼んできたものは、まさにこの一次形式に他ならない。

> <strong>注</strong> 数学者は <strong>一次形式（1-form）</strong> のあとに <strong>covector</strong>（余ベクトル）と続けて呼ぶ流儀をとることもよくある。他書を読むときの辞書として、頭の片隅に置いておけばよい。

命名の由来は単純だ：

* <strong>「一次」</strong>：変位ベクトルを<strong>一次（線形）</strong>に処理するから
* <strong>「形式」</strong>：「測定の形式」「作用の形式」を意味する

これ以降、この測定器のことを「行列」とも「一次形式（1-form）」とも呼ぶことにする。どちらの呼び方も、同じ実体を指している。

> <strong>注（本書における記号 $dx$ の契約）</strong> <strong>$dx$ を単独で「微小な変位」や「微小変化」の意味には用いない</strong>——変位の幅と測定器（横ベクトル）を混同しないために、次のように約束する。$x$ 方向の（微小）変位の大きさは <strong>$\Delta x$</strong> を使うか、変位ベクトル $\mathbf{v}$ を明示して <strong>$dx(\mathbf{v})$</strong> と書く。
>
> 一方、<strong>単独で現れる $dx$</strong> は、<strong>$x$ 成分を抜き出す横ベクトル（一次形式）としての演算子</strong>を指す。式 $df = f'(x)\,dx$ のように並ぶ $dx$ も、<strong>常に演算子として読む</strong>。<strong>何度繰り返しても強調しすぎることはない</strong>。
>
> 積分記号 $\int_a^b f(x)\,dx$ の末尾の $dx$ は、高校以来の<strong>慣用記法</strong>として残す（積分変数 $x$ とセットの「ひとかたまり」）。本書ではここを毎回 $dx(\mathbf{v})$ まで展開しないことも多いが、<strong>変位や微小幅を語る本文では $\Delta x$ か $dx(\mathbf{v})$ に揃え、裸の $dx$ には幅や変化量のイメージを載せない</strong>。

> <strong>注</strong> 数学者や物理学者は、変位の成分を $dx$ と書く慣習もよく使う。本書の記法に慣れると、<strong>測定器としての $dx$ と変位のスカラーを切り分けた</strong>読みがしやすくなる——より進んだ本では、その区別がそのまま効いてくる。

> <strong>注</strong> 同じ注意を繰り返し書くが、<strong>それほど記号の使い分けが本書の骨格だから</strong>である。

次節では、この視点を関数の微分へと拡張し、全微分 $df$ を行列として定義していく。

---

> <strong>【ここまでのチェックポイント】</strong>
> - 微小変位は縦ベクトル $\mathbf{v}$。$\Delta x$ はスカラー幅であり、単独の $dx$ は横ベクトル（一次形式）としての演算子である。
> - リーマン和の各項は $(f\,dx)(\mathbf{v}_i)$ の形で、積分はその極限として理解できる。
> - 積分記号 $\int_a^b f(x)\,dx$ の末尾の $dx$ は慣用記法であり、変位そのものは $\Delta x$ や $dx(\mathbf{v})$ で書く（§1.2.6 の契約）。

---

### §1.3 全微分 $df$ — 変化率を行列にまとめた演算子
前節では、リーマン積分を「行列 $f(x)\,dx$ の変位ベクトルへの作用の和の極限」として解剖した。この節では、その考え方を関数自体の微分へと拡張し、<strong>全微分 $df$ を横ベクトル（行列）として定義する</strong>。「微分」は、単なる数値の変化率ではなく、<strong>変位ベクトルに掛けて初めて「変化量の一次部分」が出てくる演算子</strong>として扱う。数学者は<strong>関数</strong>や<strong>写像</strong>という表現を好むことも多いが、本書では<strong>演算子</strong>と呼ぶことが多い。

#### 1.3.1 微分可能性のベクトル表現
関数 $f(x)$ が点 $x$ で微分可能であるとは、次の一次近似が成り立つことである：
$$\Delta f = f(x + \Delta x) - f(x) = f'(x) \Delta x + o(|\Delta x|) \quad (|\Delta x| \to 0)$$

> <strong>注</strong> <strong>$o(|\Delta x|)$</strong> は<strong>ランダウのオーダー記法</strong>の一種である。$\Delta x \to 0$ のとき、$o(|\Delta x|)$ でまとめて書いた量は <strong>$|\Delta x|$ よりずっと速くゼロに近づく余り</strong>を意味し、主項 $f'(x)\Delta x$ に比べれば<strong>無視してよいほど小さい</strong>、という約束である。理工系の専門書ではよく出るが、初めて見る読者もいるかもしれない。

ここで $\Delta x$ はスカラーだが、我々はこれを前節同様、3次元の変位ベクトルとして捉え直す：
$$\mathbf{v} = \begin{pmatrix} \Delta x \\ 0 \\ 0 \end{pmatrix}$$

すると、関数の変化 $\Delta f$ は、この $\mathbf{v}$ によって引き起こされる効果と見なせる。

#### 1.3.2 $df$ の行列としての定義と $df(\mathbf{v})$
点 $x$ における関数 $f$ の<strong>全微分</strong> $df$ を、次の $1 \times 3$ 横ベクトルとして定義する：
$$df := f'(x) \, dx = \begin{pmatrix} f'(x) & 0 & 0 \end{pmatrix}$$

この $df$ を変位 $\mathbf{v}$ に作用させた結果を、前節と同様に <strong>$df(\mathbf{v})$</strong> と書く：
$$df(\mathbf{v}) = \begin{pmatrix} f'(x) & 0 & 0 \end{pmatrix} \begin{pmatrix} \Delta x \\ 0 \\ 0 \end{pmatrix} = f'(x)\,\Delta x$$

<strong>重要な認識の転換</strong>（<strong>常に次のように読む</strong>）：
* 式 $df = f'(x)\,dx$ は、微積分でおなじみの<strong>全微分の記法</strong>だが、本書では <strong>$df$ も $dx$ も演算子としての横ベクトル</strong>であり、<strong>単体では微小変化量ではない</strong>、と読む。
* <strong>$df(\mathbf{v})$</strong> と書いたときは、<strong>有限の（ただし十分小さい）変位 $\mathbf{v}$ に対する一次近似としての変化量</strong>を意味する。

$df$ それ自体は変化量ではない。<strong>変化量の一次部分を生成する「装置」</strong>なのである。

> <strong>注</strong> §1.2.6 の記号契約と同じ区別を、ここでもう一度述べる。くどいと感じるかもしれないが、<strong>ここを誤読すると以降すべてがずれる</strong>ので、繰り返しに価値がある。

#### 1.3.3 具体例： $f(x) = x^2$ の場合
$f(x) = x^2$ とする。$f'(x) = 2x$ である。

たとえば <strong>$x=3$ において</strong>全微分を具体的に書き下ろす。横ベクトルと縦ベクトルを並べて、
$$df = 6\,dx = \begin{pmatrix} 6 & 0 & 0 \end{pmatrix}, \qquad \mathbf{v} = \begin{pmatrix} 0.1 \\ 0 \\ 0 \end{pmatrix}$$
であるから、行列の積は
$$df(\mathbf{v}) = \begin{pmatrix} 6 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0.1 \\ 0 \\ 0 \end{pmatrix} = 6\cdot 0.1 + 0\cdot 0 + 0\cdot 0 = 0.6$$

実際、$f(3.1) - f(3) = 9.61 - 9 = 0.61$ であり、一次近似 $0.6$ はよく一致している。

#### 1.3.4 置換積分の行列解釈
置換積分は、積分変数を取り換えて被積分関数を書き換える操作である（高校数学で扱う）。本節の目的はそれ<strong>単体の公式暗記ではない</strong>。§1.2 までに整えた言葉で言えば、<strong>「空間側の一次形式 $F\,dx$ が各ステップの変位 $\Delta\mathbf{r}$ に作用する」リーマン和</strong>と、<strong>「時間パラメータ $t$ 上のステップ幅 $\Delta t$」</strong>を、<strong>同じステップの中で対応づける</strong>と、置換後の積分 $\int F(x(t))\,\frac{dx}{dt}\,dt$ の形に自然に落ちる、という骨格を見せることである（いま必要なのは 1-form とパラメータの話までで、ウェッジ積 $\wedge$ や 2-form はまだ登場しない）。

仕事を例に取る。仕事は
$$W = \int_a^b F(x)\,dx$$
と書ける（§1.2.5 でも同じ量を行列作用の極限として見た）。位置が時間 $t$ とともに動き、$t_0<t_1$ で $x(t_0)=a,\; x(t_1)=b$ となるようにパラメータ表示すると、空間内の点は
$$\mathbf{r}(t) = \begin{pmatrix} x(t) \\ 0 \\ 0 \end{pmatrix}$$
と書ける。

<strong>時間軸側の1ステップ</strong>を、縦1成分のベクトル
$$\mathbf{w} := \begin{pmatrix} \Delta t \end{pmatrix}$$
で表す。$dx=\begin{pmatrix}1&0&0\end{pmatrix}$ と<strong>並べて考えるなら</strong>、$t$ 成分だけを抜き出す「測定器」を $1\times 1$ 行列
$$dt := \begin{pmatrix} 1 \end{pmatrix}$$
とおき、$dt(\mathbf{w})=\Delta t$ と読む。これは §1.2.6 の「横が測定器・縦がステップ・作用でスカラー」という<strong>型</strong>を、時間だけに縮めたものである。

> <strong>注</strong> すまない——$dt$ を $1\times 1$ の横ベクトルとみなすのは、第1章までに導入した $3$ 次元の $dx$ とは次元が異なり、<strong>厳密には本書の導入だけではカバーしきれていない</strong>。数学者はここで言葉を増やして一気に厳密化するかもしれない。<strong>しかし物理学者として、時間は空間の3次元の中にすっぽり埋め込めるものではない——空間だけの話に丸めてごまかすわけにもいかなかったのだ。</strong> だから $t$ の軸は $1\times1$ として切り出して正面から置く。時間 $t$ は $x,y,z$ とは<strong>別の独立なパラメータ</strong>であることはそのままだ。横が測定器、縦が微小ステップ、作用でスカラー——という $dx$ と<strong>同じ型</strong>にそろえてあるので、理解は容易であろう。

この $\Delta t$ に対応する<strong>空間での実際の変位</strong>は
$$\Delta \mathbf{r} = \mathbf{r}(t+\Delta t) - \mathbf{r}(t) = \begin{pmatrix} \Delta x \\ 0 \\ 0 \end{pmatrix}, \qquad \Delta x = x(t+\Delta t)-x(t)$$
である。ここで $\Delta t \neq 0$ とする。商 $\Delta x/\Delta t$ は<strong>そのステップにおける $x$ の平均変化率</strong>であり、中学生でも知っている恒等式
$$\Delta x = \frac{\Delta x}{\Delta t}\,\Delta t$$
が成り立つ。したがって
$$\Delta \mathbf{r} = \begin{pmatrix} \dfrac{\Delta x}{\Delta t} \\ 0 \\ 0 \end{pmatrix}\,\Delta t
= \begin{pmatrix} \dfrac{\Delta x}{\Delta t} \\ 0 \\ 0 \end{pmatrix}\,dt(\mathbf{w})$$
と書ける。<strong>これは近似でも微積の魔法でもなく、$\Delta x$ を $\Delta t$ で割った商を途中に挟んだだけの書き換えである。</strong>左の縦ベクトルは「そのステップでの $x$ 方向の平均変化率」、右の $dt(\mathbf{w})=\Delta t$ は時間ステップの幅である。

さて $F\,dx$ は横ベクトル（演算子）なので、各ステップで
$$\bigl(F(x)\,dx\bigr)(\Delta \mathbf{r}) = F(x)\,\Delta x = F(x)\,\frac{\Delta x}{\Delta t}\,\Delta t = F(x)\,\frac{\Delta x}{\Delta t}\,dt(\mathbf{w})$$
という<strong>スカラー</strong>が得られる。積分記号 $\int_{t_0}^{t_1} g(t)\,dt$ の末尾の $dt$ は、§1.2.6 の $\int f(x)\,dx$ の $dx$ と同じく<strong>積分変数とセットの慣用記法</strong>であり、リーマン和の段階では <strong>$\Delta t$ と $dt(\mathbf{w})$ が対応する</strong>と読めばよい。

分割を細かくし $\Delta t \to 0$ の極限をとると、各ステップで平均変化率 $\Delta x/\Delta t$ は接線の傾き $\dfrac{dx}{dt}$ に近づく。したがって高校数学の置換積分の形
$$W = \int_a^b F(x)\,dx = \int_{t_0}^{t_1} F(x(t))\,\frac{dx}{dt}\,dt$$
に帰着する（$\dfrac{dx}{dt}$ は $\Delta x/\Delta t$ の極限）。極限の内側のリーマン項は
$$\bigl(F(x(t))\,dx\bigr)(\Delta \mathbf{r}) \approx F(x(t))\,\frac{dx}{dt}\,\Delta t$$
と読め、<strong>空間側の一次形式 $F\,dx$ が $\Delta\mathbf{r}$ に作用した値</strong>と、<strong>時間側のステップ $\Delta t$（すなわち $dt(\mathbf{w})$）を積み上げる構造</strong>が対応している。

微小ステップでは、運動エネルギーの変化と仕事の関係 $\Delta\bigl(\tfrac12 m v^2\bigr) \approx F\,\Delta x$ が成り立つ。ここで $v$ はそのステップにおける速度の代表値である。右辺の $F\,\Delta x$ は $\bigl(F\,dx\bigr)(\Delta\mathbf{r})$ に他ならない。

同じ骨格は $df = f'(x)\,dx$ の積分にも入る。同じパラメータ表示で $\Delta\mathbf{r}=\begin{pmatrix} \Delta x \\ 0 \\ 0 \end{pmatrix}$ とすれば
$$\bigl(f'(x(t))\,dx\bigr)(\Delta \mathbf{r}) = f'(x(t))\,\Delta x = f'(x(t))\,\frac{\Delta x}{\Delta t}\,\Delta t$$
であり、$\Delta t \to 0$ で $\Delta x/\Delta t \to \dfrac{dx}{dt}$ として
$$\bigl(f'(x(t))\,dx\bigr)(\Delta \mathbf{r}) \approx f'(x(t))\,\frac{dx}{dt}\,\Delta t$$
の極限から
$$\int_a^b f'(x)\,dx = \int_{t_0}^{t_1} f'(x(t))\,\frac{dx}{dt}\,dt$$
となる。

#### 1.3.5 なぜ行列表示が優れているか — 拡張性の観点から
$df$ を横ベクトルとして定義する利点は、<strong>多次元への自然な拡張</strong>にある。
1変数では： $df = f'(x) dx = \begin{pmatrix} f'(x) & 0 & 0 \end{pmatrix}$
2変数関数 $f(x, y)$ では（次章で詳述）： $df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy = \begin{pmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} & 0 \end{pmatrix}$
3変数では： $df = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \frac{\partial f}{\partial z} dz = \begin{pmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} & \frac{\partial f}{\partial z} \end{pmatrix}$

このように、<strong>次元が増えても形式は変わらない</strong>。ただ横ベクトルの成分が増えるだけだ。これが「代数の武器」としての威力である。

$df$ を行列と見なすことで、微分は「変位に対する線形近似を与える演算子」として統一的に扱える。次節では、ライプニッツの記法がこの流儀とどう響き合うかを短く拾い、続いてデカルト座標の「特権」へ進む。

---

> <strong>【ここまでのチェックポイント】</strong>
> - 微分可能性は $\Delta f = f'(x)\Delta x + o(|\Delta x|)$（$o$ はランダウのオーダー記法）で表される一次近似として捉えられる。
> - $df = f'(x)\,dx$ は横ベクトル；数値の変化量は $df(\mathbf{v})$ として読む。
> - 置換積分は、一次形式 $F\,dx$ が空間の変位に作用する構造と、時間軸上の $dt$ を積み上げる構造の対応としても見られる。

---

### §1.4 ライプニッツの記法と代数的直感
ライプニッツが $dx$, $dy$ という記号を導入したとき、彼はこれらを「無限小」として直感的に扱った。現代の我々は、その直感を<strong>線形代数の言葉</strong>で再配置したと言える。
ライプニッツの記法 $df = f'(x)dx$ は、単なる形式的等式ではない：
* $dx$：ライプニッツの無限小の直感 → 本書では <strong>演算子</strong>としての $x$ 成分抽出（微小変位そのものを語るときは $\Delta x$ や $dx(\mathbf{v})$）
* $df$：ライプニッツの無限小変化の直感 → 本書では <strong>演算子</strong>としての全微分（数値の変化量は $df(\mathbf{v})$ などで）

<strong>ライプニッツの天才は、微分・積分が本質的に代数的操作であることを見抜いていた</strong>。我々は、彼の直感に行列という具体的な骨格を与えたに過ぎない。

次節では、この枠組みが依存している暗黙の前提——デカルト座標系の「使いやすさ」——を明らかにし、より一般的な座標への接続を示唆する。

---

> <strong>【ここまでのチェックポイント】</strong>
> - ライプニッツの $dx$、$df$ の直感は、本書ではいずれも「変位に作用する横ベクトル（演算子）」として再配置されている。
> - 微小変化量を語るときは $\Delta x$ や $df(\mathbf{v})$ とし、記号の役割を混同しない。

---

### §1.5 「デカルトの特権」と物理学の現実

本章を通じて、我々は $dx$ の<strong>デカルト行列表現</strong> $\begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$ を用いて議論してきた。このアプローチの威力は疑いようもないが、物理学者としてここで一つの厳粛な事実を認めなければならない。それは、この美しい行列表示の成分が場所によらず一定に保たれるという性質は、我々が<strong>特別に選ばれた座標系</strong>——デカルト座標（直交直線座標）——の中にいるからに他ならない、という事実である。数学者は「$dx$ は座標によらない一次形式だ」と語る話と、いま目の前にある「成分が $(1\ 0\ 0)$ で一定」という表示は、どう両立するのか——<strong>§1.5.3 で座標変換の式を見れば、一本の線でつながる</strong>（§1.2.3 の注で先に触れた「表示にすぎない」という注意の続きでもある）。

#### 1.5.1 デカルト座標の「特権」とは何か

デカルト座標系が物理学において特別な地位を占める理由は、それが<strong>最も単純で、空間のどこでも性質が変わらない</strong>座標系だからだ。この「平坦な方眼紙」の上では：
1. <strong>基底ベクトルが一定</strong>：$\hat{e}_x, \hat{e}_y, \hat{e}_z$ は空間のどこでも同じ向き・同じ大きさを持つ。
2. <strong>行列表現が場所によらない</strong>：$x$ 方向の単位変位がどこでも同じなので、$dx$ のデカルト行列表現が空間のどこでも $\begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$ のまま変わらない。

#### 1.5.2 物理学の現実は「四角い」とは限らない — 曲線座標への先手

現実の物理現象、特に電磁気学や流体力学の問題を解くとき、世界は必ずしもデカルト座標にとって都合よくできてはいない。直線状の回路の周りの磁場や、円形パイプ内の流れなど、<strong>円柱座標 $(r,\theta,z)$ や球座標 $(r,\theta,\phi)$</strong> のほうが自然な場面が多い。球座標を本書で具体的に使う節では、$\theta$ と $\phi$ が<strong>天頂角と方位角のどちらに対応するか</strong>をその都度明示する（記法は文献によってまちまちなので、本書の定義を先に置く）。

重積分や体積要素で「極座標に変えると $r$ や $\sin\theta$ が出る」といった経験は、<strong>デカルトの $x,y,z$ から別の座標へ写すと、基底や積分の要素がどう変わるか</strong>という問題の入り口である。§1.3.4 では<strong>仕事の積分を手がかりに、置換積分を一次形式とパラメータに沿った変位のステップの組として読み直した</strong>が、ここでは<strong>曲線座標のほうに視点を移す</strong>。

> <strong>注</strong> 本書では、まだ<strong>微分形式の変数変換を厳密には定式化してはいない</strong>。読者の既知の計算経験と、本章の「横ベクトル $dx$ が変位に作用する」という流儀が、のちほど接続できそうだという<strong>動機</strong>だけ先に示す。詳細は後の章で補う。

#### 1.5.3 座標変換による $dx$ の変貌

デカルト座標 $(x, y, z)$ から、円柱座標 $(r, \theta, z)$ へ変換する場面を考えよう。変換則は：
$$
x = r\cos\theta,\quad y = r\sin\theta,\quad z = z
$$

微分の連鎖律から、<strong>座標関数 $x$ の微分</strong>としての $dx$ は次のように書き換えられる：
$$
dx = \frac{\partial x}{\partial r}dr + \frac{\partial x}{\partial \theta}d\theta + \frac{\partial x}{\partial z}dz = \cos\theta\, dr - r\sin\theta\, d\theta
$$

ここでの $dx, dr, d\theta$ はいずれも <strong>演算子（一次形式）</strong>であり、右辺は「円柱座標の基底 $dr, d\theta, dz$ で $dx$ を展開した」式である。<strong>スカラーの微小変位 $\Delta x$ とは別物</strong>だ（§1.2.6 の契約）。

驚くべきことに、$dx$ という測定器（幾何学的実体）そのものは不変であるにもかかわらず、それを円柱座標系の基底 $(dr, d\theta, dz)$ に対する成分として表現しようとした途端、デカルト座標での定数成分 $\begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$ から、場所 $(r, \theta)$ に依存する関数を成分に持つ行列へと姿を変えるのである。対象そのものは不変であっても、「基準となる基底が変われば、その行列表現（成分）も変わる」 ——これが基底変換の核心である。

> <strong>注</strong> では $dr$ や $d\theta$ についても、$dx$ と同じように「数ベクトルとしての行列表現は何か」と気になるだろう。率直に言えば、円柱座標の座標軸に合わせて書けば「第1成分を抜く」形はまた $(1\ 0\ 0)$ のように見えなくもない。<strong>だがそれはデカルトで書いた $dx=\begin{pmatrix}1&0&0\end{pmatrix}$ とは、載っている座標系も基底も違う</strong>。数学者はここで<strong>空間や基底を言葉で切り分けて</strong>論じるのが常だが、本書のいまの段階でそれをやり切ると筆者も読者も疲れる。<strong>深追いはしないでおく。</strong>

#### 1.5.4 なぜ代数的な武器が必要なのか

この事実こそが、我々が微積分を「代数」として再構築しなければならない最大の理由である。

従来の「$\Delta x$ は微小な幅である」という素朴なイメージのままでは、座標系が曲がった瞬間に直感が破綻する。しかし、$dx$ を「変位ベクトルから成分を抽出する一次形式」として定義しておけば、座標系が変わっても<strong>「基底変換に伴う行列の成分変化」という線形代数の単純なルール</strong>に従って、機械的かつ厳密に計算を進めることができる。

本書の後半で電磁気学や流体力学の複雑な問題に挑むとき、この「座標に依存しない代数構造」がどれほど強力な武器になるかを目の当たりにするだろう。

---

> <strong>【ここまでのチェックポイント】</strong>
> - デカルトでは $dx$ の行列表現が場所に依らないが、曲線座標では基底展開により成分が場所 $(r,\theta)$ などに依存する。
> - 幾何学的な一次形式そのものと、選んだ座標系での成分表示とを切り分ける（§1.5.3）。

---

### §1.6 基底変換の気づき（演習と展望）

本章の終盤で、読者自身の手で「座標変換」を一度、計算として体験してもらう。ここではまだ<strong>基底変換を一般論として定義したわけではない</strong>が、§1.5.3 で見たように、<strong>同じ $dx$ でも座標の取り方で行列表現が変わる</strong>ことは既に述べた。この演習は、その感覚を手で確かめるためのものである。<strong>いま基底変換の厳密な言語を全部そろえるより先に、なぜ計算をしておきたいのか</strong>——それは、後の章で式が一気に忙しくなるときに、「成分が変わるのは当たり前」という腹落ちを持っておくためだ。

#### 1.6.1 演習問題：円柱座標での測定

<strong>問題設定</strong>  
前節で見た通り、円柱座標 $(r, \theta, z)$ における $dx$ の行列表示は以下のようになる：
$$
dx = \begin{pmatrix} \cos\theta & -r\sin\theta & 0 \end{pmatrix}
$$
このとき、次の問いに答えよ。

<strong>問1</strong>  
円柱座標空間内の点 $P(r=2, \theta=\pi/6, z=0)$ に質点があるとする。この質点が、$r$ 方向に $0.1$ だけ微小変位した。この変位ベクトル $\mathbf{v}$ を円柱座標の成分で表せ。

<strong>問2</strong>  
問1の変位ベクトル $\mathbf{v}$ に対して、点 $P$ における行列 $dx$ を作用させよ。（$\cos(\pi/6) = \sqrt{3}/2$ を用いよ）

<strong>問3</strong>  
問2で計算した結果 $dx(\mathbf{v})$ は、物理的に何を意味しているか説明せよ。

#### 1.6.2 解答と解説

<strong>問1の解答</strong>  
変位は $r$ 方向に $0.1$、$\theta$ 方向と $z$ 方向にはゼロなので、円柱座標の基底における縦ベクトルとして次のように書ける：
$$
\mathbf{v} = \begin{pmatrix} 0.1 \\ 0 \\ 0 \end{pmatrix}
$$

<strong>問2の解答</strong>  
点 $P$ における行列 $dx$ は、$\theta = \pi/6, r=2$ を代入して：
$$
dx|_P = \begin{pmatrix} \cos(\frac{\pi}{6}) & -2\sin(\frac{\pi}{6}) & 0 \end{pmatrix} = \begin{pmatrix} \frac{\sqrt{3}}{2} & -2 \times \frac{1}{2} & 0 \end{pmatrix} = \begin{pmatrix} \frac{\sqrt{3}}{2} & -1 & 0 \end{pmatrix}
$$
重要なのは、第2成分は一般に <strong>$-r\sin\theta$</strong> という係数であり、$r$ のおかげで<strong>長さの次元を持つ</strong>ことだ。$r=2,\;\theta=\pi/6$ と代入するとその係数の値として $-1$ が見えるが、<strong>数値の $-1$ そのものに次元が付いているのではない</strong>。行列の成分としての $-r\sin\theta$ が長さの次元を運んでいる、と読むのが正確である。これが次元解析の鍵となる。
これを変位ベクトル $\mathbf{v}$ に作用させると：
$$
dx|_P(\mathbf{v}) = \begin{pmatrix} \frac{\sqrt{3}}{2} & -1 & 0 \end{pmatrix} \begin{pmatrix} 0.1 \\ 0 \\ 0 \end{pmatrix} = 0.1 \times \frac{\sqrt{3}}{2} \approx 0.0866
$$

<strong>問3の解答（物理的意味）</strong>  
この結果は、<strong>「円柱座標において外側（$r$方向）へ $0.1$ だけ進むという運動は、デカルト座標の $x$ 軸方向から見ると約 $0.0866$ の前進に相当する」</strong>という物理的事実を表している。

<strong>【次元解析の深い考察】</strong>  
計算結果 $dx|_P(\mathbf{v}) = 0.1 \times \frac{\sqrt{3}}{2}$ を見ると、$r$方向成分$0.1$（長さの次元）と、第1成分の係数$\frac{\sqrt{3}}{2}$（無次元）の積となっており、出力は確かに長さの次元を持つ。
しかし、もし$\theta$方向の変位$\mathbf{v} = \begin{pmatrix} 0 \\ 0.1 \\ 0 \end{pmatrix}$（角度変位$0.1$ラジアン）を入力したとすると：
$$dx|_P(\mathbf{v}) = \begin{pmatrix} \frac{\sqrt{3}}{2} & -1 & 0 \end{pmatrix} \begin{pmatrix} 0 \\ 0.1 \\ 0 \end{pmatrix} = -0.1$$
この場合、<strong>入力ベクトルの第2成分</strong> $0.1$ は角度（無次元）だが、<strong>行列の第2列に対応する係数</strong> $-r\sin\theta$ が長さの次元を運ぶため、積としての出力 $-0.1$ は長さの次元を持つ。

ここに<strong>一次形式</strong>の驚くべき性質がある： $dx$ の行列成分自体が $r$ を含む関数であり、入力が座標成分（次元がバラバラでも）であっても、出力は常に「$x$ 方向の長さ」という正しい物理的次元を持つように自動調整される。<strong>一次形式は、座標系の歪みを吸収し、物理的に意味のある測定値を出力する「賢い測定器」</strong>なのである。

<strong>測定器の較正（キャリブレーション）としての基底変換</strong>  
デカルト座標の $dx = \begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$ は、「純粋な$x$方向の変位を1と測定する装置」である。これを円柱座標で使おうとすると、装置は「$r$方向や$\theta$方向の変位も$x$成分に影響する」ことを考慮しなければならない。
つまり、座標系を変えるということは、<strong>測定器（行列）の目盛りを場所ごとに較正し直す作業</strong>に他ならない。これが基底変換の正体である。

#### 1.6.3 この先の章へ

> <strong>【ここまでのチェックポイント — 第1章全体】</strong>
> - 第1章の主役は「$dx$ を行列・一次形式として読み、$\int f\,dx$ を作用の極限として読む」ことである。
> - $df$ も横ベクトルとして統一し、多次元への拡張は成分の増加として素直に繋がる。
> - 次章以降は $dy, dz$、ウェッジ積、曲線積分、外微分、ホッジスターへと拡張する。

本章では $dx$ だけを扱い、$y, z$ 方向は常に「断面」として無視してきた。
次章からは $dy = \begin{pmatrix}0&1&0\end{pmatrix}$, $dz = \begin{pmatrix}0&0&1\end{pmatrix}$ を正式に導入し、3次元空間全体を記述する<strong>一次形式（1-form）</strong>の理論を仕上げる。そのうえで、直線的な変位だけに閉じない<strong>曲線に沿った積分</strong>や、ベクトルに作用してスカラーを返す型にとどまらない<strong>高次の微分形式</strong>への拡張へと進む。それらを掛け合わせる「外積（ウェッジ積 $\wedge$）」も導入する。

その後の部では、<strong>微分演算子 $d$</strong>、<strong>ホッジスター演算子 $*$</strong>、ベクトル解析の $\mathrm{grad}$（$\nabla$）、$\mathrm{rot}$（$\nabla\times$、$\mathrm{curl}$）、$\mathrm{div}$（$\nabla\cdot$）、ストークスの定理、マクスウェル方程式や流体力学の基礎方程式へと進む。3次元での微分形式とベクトル場の対応は、ホッジスターで整理できる。

3次元ユークリッド空間の真の姿を解き明かす旅へ、いざ出発しよう。
