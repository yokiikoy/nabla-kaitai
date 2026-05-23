## Appendix D: Array Representation of the Hodge Star

§6.3.2 gave the dictionary for $\ast$ in real space. This appendix checks how that dictionary looks as array operations. The Hodge star is not an abstract symbol; once a basis is chosen, it is a linear transformation that can be displayed as a concrete array. We first view the $1$-form $\leftrightarrow$ $2$-form correspondence through antisymmetric matrices, and finally view the $0$-form $\leftrightarrow$ $3$-form correspondence through a third-order array.

### D.1 $\ast_{1\to2}$ — placing three coefficients into an antisymmetric matrix

For the $1$-form

$$
\omega =
\begin{pmatrix}P & Q & R\end{pmatrix}
=
P\,dx + Q\,dy + R\,dz
$$

apply the dictionary from the main text,

$$
\ast dx = dy \wedge dz,\qquad
\ast dy = dz \wedge dx,\qquad
\ast dz = dx \wedge dy
$$

to obtain

$$
\ast\omega
=
P\,dy\wedge dz
+
Q\,dz\wedge dx
+
R\,dx\wedge dy
$$

In the antisymmetric matrix representation of Chapter 2, let the matrix representing $dy\wedge dz$ be

$$
E_1 =
\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & -1 & 0
\end{pmatrix}
$$

Similarly, let the matrix representing $dz\wedge dx$ be

$$
E_2 =
\begin{pmatrix}
0 & 0 & -1 \\
0 & 0 & 0 \\
1 & 0 & 0
\end{pmatrix}
$$

and let the matrix representing $dx\wedge dy$ be

$$
E_3 =
\begin{pmatrix}
0 & 1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
$$

Therefore,

$$
\ast_{1\to2}
=
\begin{pmatrix}
E_1\\
E_2\\
E_3
\end{pmatrix}
$$

can be viewed as a "vertical vector of matrices." Multiplying the $1$-form $\omega=\begin{pmatrix}P&Q&R\end{pmatrix}$ on the left gives

$$
\omega\,\ast_{1\to2}
=
\begin{pmatrix}P&Q&R\end{pmatrix}
\begin{pmatrix}
E_1\\
E_2\\
E_3
\end{pmatrix}
=
P E_1+Q E_2+R E_3
$$

Hence

$$
\ast_{1\to2}(\omega)
=
\begin{pmatrix}
0 & R & -Q \\
-R & 0 & P \\
Q & -P & 0
\end{pmatrix}
$$

The three coefficients $P,Q,R$ of the $1$-form have been placed into the three independent components of the antisymmetric matrix of the $2$-form. This is the most visible form of $\ast_{1\to2}$.

> <strong>Note</strong> (relation to $\widehat{\epsilon}$ in Chapter 2) These $E_1,E_2,E_3$ are the same matrices written in Appendix A as $\varepsilon_{1,\cdot,\cdot},\varepsilon_{2,\cdot,\cdot},\varepsilon_{3,\cdot,\cdot}$. The essence of $\ast_{1\to2}$ is to place the first index of Einstein's epsilon $\varepsilon_{ijk}$ in the direction of the components of the $1$-form, and the remaining two indices in the directions of the $3\times3$ matrix. The same triple introduced in Chapter 2 as the volume-measuring device $\widehat{\epsilon}$ reappears here as the Hodge star.

### D.2 $\ast_{2\to1}$ — extracting coefficients by the Frobenius product

The reverse map $\ast_{2\to1}$ is the operation that extracts three independent components from an antisymmetric matrix. Looking at matrix entries alone, it suffices to read $A=M_{23}$, $B=M_{31}$, $C=M_{12}$. That is, to return from the antisymmetric matrix

$$
M=
\begin{pmatrix}
0 & C & -B \\
-C & 0 & A \\
B & -A & 0
\end{pmatrix}
$$

representing the $2$-form

$$
\eta
=
A\,dy\wedge dz
+
B\,dz\wedge dx
+
C\,dx\wedge dy
$$

to $A\,dx+B\,dy+C\,dz$, one need only read these three components. If we stop at this mere "reading," however, the transpose relation with $\ast_{1\to2}$ is hard to see. So we rewrite coefficient extraction itself as an inner product between matrices.

Define the inner product of $3\times3$ matrices $A,B$ by

$$
A\cdot B
=
\frac{1}{2}\operatorname{tr}(A^T B)
=
\frac{1}{2}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
A_{ij}B_{ij}
$$

> <strong>Note</strong> (trace) $\operatorname{tr}$ is the <strong>trace</strong> of a matrix (the sum of diagonal entries). It appeared when we treated the matrix representation of the exterior derivative in Appendix B. $\operatorname{tr}(A^T B)$ is the three-step operation "transpose $A$, multiply by $B$, and add the diagonal entries." Because it is equivalent to $\frac{1}{2}\sum A_{ij}B_{ij}$, use the latter expression when you want to think in components.

This is the same notation as the inner product $\mathbf{v}_1 \cdot \mathbf{v}_2$ between column vectors in §6.2.3. Matrices, too, are "things of the same kind," and we multiply corresponding components and take the sum. Because we contract successively over the two indices $i$ and $j$, this is called the <strong>Frobenius product</strong> or <strong>consecutive contraction</strong>.

> <strong>Note</strong> (the factor $1/2$) Some conventions adopt $\operatorname{tr}(A^T B)$ (without $1/2$) as the Frobenius product. For antisymmetric matrices, however, that picks up both members of a pair such as $M_{23}$ and $M_{32}=-M_{23}$, and the inner product is doubled. In this book we build $1/2$ into the definition. Then the inner product of the $2$-form $M$ with itself, $M\cdot M=M_{23}^2+M_{31}^2+M_{12}^2$, agrees directly with the "squared unsigned area of the parallelogram" in §6.2.2.

> <strong>Note</strong> (the pull of abstraction) §6.2.3 touched on an axiomatic inner product, but once you actually work by hand like this, you can see why that brevity is attractive. For the inner product of column vectors we use $\mathbf{v}_1^T \mathbf{v}_2$; for the inner product of matrices we use $\frac{1}{2}\operatorname{tr}(A^T B)$—redefining the inner product from scratch every time the representation changes is, when you think about it, quite a burden. One notices the urge to lump these together and settle everything with one phrase: "an inner product is an operation satisfying certain axioms." Even so, this book does not abandon its policy of making representations explicit to the end. By this point, that is stubbornness.

The $E_1,E_2,E_3$ of D.1 are orthonormal with respect to this inner product. Indeed, each $E_k$ has only two nonzero components; for the same $E_k$ we get $\frac{1}{2}(1^2+(-1)^2)=1$, and for different $E_i,E_j$ the positions of the nonzero components do not overlap. Therefore,

$$
E_i\cdot E_j=\delta_{ij}
$$

Using this orthonormality, the reverse transformation $\ast_{2\to1}$ can be written as inner products with $E_1,E_2,E_3$. Let $M$ be an arbitrary $3\times3$ matrix; when it comes from a $2$-form, $M$ is an antisymmetric matrix.

$$
\ast_{2\to1}(M)
=
\begin{pmatrix}
E_1\cdot M & E_2\cdot M & E_3\cdot M
\end{pmatrix}
$$

Here $E_k\cdot M=\frac{1}{2}\operatorname{tr}(E_k^T M)$ is the Frobenius product defined above. In components,

$$
\begin{aligned}
E_1 \cdot M &= \frac{1}{2}(M_{23}-M_{32}) \\
E_2 \cdot M &= \frac{1}{2}(M_{31}-M_{13}) \\
E_3 \cdot M &= \frac{1}{2}(M_{12}-M_{21})
\end{aligned}
$$

If $M$ is an antisymmetric matrix, then $M_{32}=-M_{23}$, $M_{13}=-M_{31}$, $M_{21}=-M_{12}$, so

$$
\ast_{2\to1}(M)
=
\begin{pmatrix}
M_{23} & M_{31} & M_{12}
\end{pmatrix}
$$

Therefore, $\ast_{2\to1}$ is at once the operation that extracts independent components from an antisymmetric matrix and coefficient extraction by the Frobenius product with $E_k$.

Writing out all components, $\ast_{2\to1}$ is the following "horizontal vector of matrices":

$$
\ast_{2\to1} = \begin{pmatrix}
\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix} &
\begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} &
\begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
\end{pmatrix}
$$

In $\ast_{1\to2}$ we multiply by coefficients and add; in $\ast_{2\to1}$ we extract coefficients by inner product. Vertical and horizontal, weighted sum and inner-product extraction, correspond to each other.

### D.3 $\ast\ast=\mathrm{id}$ in the $1$-form and $2$-form case

Combining D.1 and D.2, $\ast\ast=\mathrm{id}$ for $1$-forms and $2$-forms appears as orthonormality of arrays.

For

$$
\omega=P\,dx+Q\,dy+R\,dz
$$

D.1 gives

$$
\ast_{1\to2}(\omega)=P E_1+Q E_2+R E_3
$$

Applying $\ast_{2\to1}$ to this,

$$
\begin{aligned}
\ast_{2\to1}(\ast_{1\to2}(\omega))
&=
\begin{pmatrix}
E_1\cdot (P E_1+Q E_2+R E_3) \\
E_2\cdot (P E_1+Q E_2+R E_3) \\
E_3\cdot (P E_1+Q E_2+R E_3)
\end{pmatrix}^{T} \\
&=
\begin{pmatrix}
P & Q & R
\end{pmatrix}
=
\omega
\end{aligned}
$$

In the last equality we used $E_i\cdot E_j=\delta_{ij}$. That is, the three coefficients placed into $E_1,E_2,E_3$ by $\ast_{1\to2}$ are recovered unchanged by $\ast_{2\to1}$ through inner products with the same $E_1,E_2,E_3$.

The reverse direction is the same. For the antisymmetric matrix

$$
M=P E_1+Q E_2+R E_3
$$

D.2 gives

$$
\ast_{2\to1}(M)
=
\begin{pmatrix}
E_1\cdot M & E_2\cdot M & E_3\cdot M
\end{pmatrix}
=
\begin{pmatrix}
P & Q & R
\end{pmatrix}
$$

and applying D.1's $\ast_{1\to2}$,

$$
\ast_{1\to2}(\ast_{2\to1}(M))
=
P E_1+Q E_2+R E_3
=
M
$$

Therefore, in the $1$-form and $2$-form case,

$$
\ast_{2\to1}(\ast_{1\to2}(\omega))=\omega,
\qquad
\ast_{1\to2}(\ast_{2\to1}(M))=M
$$

hold. $\ast_{1\to2}$ places three coefficients into $E_1,E_2,E_3$; $\ast_{2\to1}$ extracts coefficients by inner product with $E_1,E_2,E_3$. Using the normalized Frobenius product, the transpose relation between the two appears as this correspondence between placement and coefficient extraction.

### D.4 Array representation of $\ast_{0\to3}$ and $\ast_{3\to0}$

So far we have displayed $\ast_{1\to2}$ and $\ast_{2\to1}$ as transformations that move coefficient arrays. What remains is $\ast_{0\to3}$ and $\ast_{3\to0}$.

A $0$-form has a single coefficient. A $3$-form, viewed purely as an array, is a completely antisymmetric third-order array with three indices. Therefore, $\ast_{0\to3}$ is the transformation that spreads one component into $3\times3\times3$ components, and $\ast_{3\to0}$ is the transformation that extracts one component from $3\times3\times3$ components.

Here we bring $\varepsilon_{ijk}$, which also appeared in Chapter 2, to the fore and look at its form.

> <strong>Note</strong> (what $\varepsilon_{ijk}$ really is) $\varepsilon_{ijk}$ is the completely antisymmetric symbol that appeared in Chapter 2. If the indices $(i,j,k)$ are an even permutation of $(1,2,3)$, it is $+1$; if an odd permutation, $-1$; if the same index appears twice, $0$. In an orthonormal Cartesian basis, it can be read as the component of a completely antisymmetric tensor. In this book we use those components as the representation of the Hodge star.

First, apply $\ast_{0\to3}$ to the $0$-form $f$. The output is a $3$-form, so it can be written in components with three indices. Here we take the components of $\ast_{0\to3}$ itself to be

$$
(\ast_{0\to3})_{ijk}
=
\varepsilon_{ijk}
$$

Display this as three $3\times3$ matrices with $i$ fixed—that is, for each of $i=1,2,3$, arrange the $(j,k)$ components as a matrix:

$$
(\ast_{0\to3})_{1jk}
=
\begin{pmatrix}
0&0&0\\
0&0&1\\
0&-1&0
\end{pmatrix},
$$

$$
(\ast_{0\to3})_{2jk}
=
\begin{pmatrix}
0&0&-1\\
0&0&0\\
1&0&0
\end{pmatrix},
$$

$$
(\ast_{0\to3})_{3jk}
=
\begin{pmatrix}
0&1&0\\
-1&0&0\\
0&0&0
\end{pmatrix}.
$$

As you can see, these are exactly the antisymmetric matrices $E_1,E_2,E_3$ used in D.1. That is,

$$
(\ast_{0\to3})_{1jk}= (E_1)_{jk},
\qquad
(\ast_{0\to3})_{2jk}= (E_2)_{jk},
\qquad
(\ast_{0\to3})_{3jk}= (E_3)_{jk}
$$

Almost nothing new happens here. The antisymmetric matrices $E_1,E_2,E_3$ seen in D.1 are now simply arranged as three slices with $i=1,2,3$. In the $1$-form and $2$-form case we read three coefficients as the coefficients of three antisymmetric matrices. In the $0$-form and $3$-form case we build, from one coefficient, the completely antisymmetric third-order array obtained by stacking all three slices at once.

Indeed, acting on the $0$-form $f$,

$$
(\ast_{0\to3}f)_{ijk}
=
(\ast_{0\to3})_{ijk}f
=
\varepsilon_{ijk}f
$$

This is the operation of spreading the coefficient $f$ into a completely antisymmetric third-order array.

Next, consider the reverse map $\ast_{3\to0}$. This is the transformation that takes a third-order array and returns a single coefficient. Its components are

$$
(\ast_{3\to0})_{ijk}
=
\frac{1}{3!}\varepsilon_{ijk}
$$

Therefore, displayed again as three $3\times3$ matrices with $i$ fixed,

$$
(\ast_{3\to0})_{1jk}
=
\frac{1}{3!}
\begin{pmatrix}
0&0&0\\
0&0&1\\
0&-1&0
\end{pmatrix},
$$

$$
(\ast_{3\to0})_{2jk}
=
\frac{1}{3!}
\begin{pmatrix}
0&0&-1\\
0&0&0\\
1&0&0
\end{pmatrix},
$$

$$
(\ast_{3\to0})_{3jk}
=
\frac{1}{3!}
\begin{pmatrix}
0&1&0\\
-1&0&0\\
0&0&0
\end{pmatrix}.
$$

That is, $\ast_{3\to0}$ uses the same three antisymmetric matrices. The only difference is that the whole thing is multiplied by $1/3!$.

If we think of the indices $(i,j,k)$ lined up in a row as a single number, then $\ast_{0\to3}$ is a column vector that spreads one component into $27$ components, and $\ast_{3\to0}$ is a row vector that extracts one component from $27$ components. Apart from the normalization factor $1/3!$, the two are in a transpose relation.

Acting on the $3$-form

$$
\eta
=
\eta_{ijk}
$$

with $\ast_{3\to0}$ sums over all three indices:

$$
\ast_{3\to0}\eta
=
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
(\ast_{3\to0})_{ijk}\eta_{ijk}
$$

Therefore,

$$
\ast_{3\to0}\eta
=
\frac{1}{3!}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
\varepsilon_{ijk}\eta_{ijk}
$$

This is a triple contraction that extracts one coefficient from a completely antisymmetric third-order array.

The factor $1/3!$ plays the same role as the $1/2$ that appears in the Frobenius product of D.2. In an antisymmetric matrix, each independent component appears twice, so we multiply by $1/2$ to correct for the duplication. Here, each independent component of a completely antisymmetric third-order array appears $3!=6$ times, so we multiply by $1/3!$ to correct for the duplication.

Let us verify that applying $\ast$ twice returns the original. First, start from the $0$-form $f$:

$$
\ast_{3\to0}(\ast_{0\to3}f)
=
\frac{1}{3!}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
\varepsilon_{ijk}(\ast_{0\to3}f)_{ijk}
$$

Since $(\ast_{0\to3}f)_{ijk}=\varepsilon_{ijk}f$,

$$
\ast_{3\to0}(\ast_{0\to3}f)
=
\frac{1}{3!}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
\varepsilon_{ijk}\varepsilon_{ijk}f
$$

Only the $3!=6$ cases in which $(i,j,k)$ is a permutation of $(1,2,3)$ are nonzero; then $\varepsilon_{ijk}\varepsilon_{ijk}=1$, so

$$
\ast_{3\to0}(\ast_{0\to3}f)
=
\frac{1}{3!}(3!)f
=
f
$$

Let us also check the reverse direction. An arbitrary $3$-form has only one independent component in three dimensions. Therefore the completely antisymmetric components $\eta_{ijk}$ can be written using some coefficient $h$ as

$$
\eta_{ijk}
=
h\,\varepsilon_{ijk}
$$

Then

$$
\ast_{3\to0}\eta
=
\frac{1}{3!}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
\varepsilon_{ijk}(h\varepsilon_{ijk})
=
h
$$

Therefore,

$$
(\ast_{0\to3}(\ast_{3\to0}\eta))_{ijk}
=
(\ast_{0\to3}h)_{ijk}
=
h\varepsilon_{ijk}
=
\eta_{ijk}
$$

Thus we have confirmed $\ast\ast=\mathrm{id}$ in the $0$-form and $3$-form case as well, in the array representation.

In the end, what we saw here is the same as in D.1–D.3. In $\ast_{1\to2}$ we distributed three coefficients among three antisymmetric matrices. In $\ast_{0\to3}$ we distributed one coefficient simultaneously among all three antisymmetric matrices. In $\ast_{2\to1}$ we extracted coefficients from an antisymmetric matrix; in $\ast_{3\to0}$ we extracted coefficients by triple contraction with the three antisymmetric matrices. The Hodge star, at every degree, is a linear transformation that can be displayed as a concrete array once a basis is chosen.

### D.5 Summary

> <strong>Checkpoint so far — Appendix D</strong>
> - $\ast_{1\to2}$ is the linear transformation that places three coefficients into the antisymmetric matrices $E_1,E_2,E_3$.
> - $\ast_{2\to1}$ is the linear transformation that extracts coefficients from an antisymmetric matrix, and can be written by the Frobenius product with $E_k$.
> - Using the Frobenius product $A\cdot B=\frac{1}{2}\operatorname{tr}(A^TB)$, we have $E_i\cdot E_j=\delta_{ij}$.
> - Therefore, in the $1$-form and $2$-form case, $\ast_{2\to1}(\ast_{1\to2}(\omega))=\omega$ and $\ast_{1\to2}(\ast_{2\to1}(M))=M$ hold.
> - $\ast_{0\to3}$ can be displayed as a third-order array obtained by stacking the three antisymmetric matrices $E_1,E_2,E_3$. In components, $(\ast_{0\to3})_{ijk}=\varepsilon_{ijk}$.
> - $\ast_{3\to0}$ can be displayed as the same array multiplied by the normalization factor $1/3!$. In components, $(\ast_{3\to0})_{ijk}=\frac{1}{3!}\varepsilon_{ijk}$.
> - The factors $1/2$ and $1/3!$ correct for duplication of antisymmetric components.
> - In the $0$-form/$3$-form case as well, $\ast_{3\to0}(\ast_{0\to3}f)=f$ and $\ast_{0\to3}(\ast_{3\to0}\eta)=\eta$ hold.
> - Therefore, the Hodge star $\ast$, for both $0\leftrightarrow3$ and $1\leftrightarrow2$, is a linear transformation that can be displayed as a concrete array once a basis is chosen.
