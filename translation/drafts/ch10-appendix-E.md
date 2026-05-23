## Appendix E: Slice-Matrix Representation of $d_4F$ and $d_4(\ast_4F)$ — Seeing Maxwell's Equations as $4\times4\times4$ Arrays

In §10.4 and §10.5 we rewrote the symbolic equations $dF=0,\;d(\ast F)=\mu_0(\ast\mathcal J)$ into the computational notation $d_4F,\;d_4(\ast_4F)$ and expanded them as coefficients of basis $3$-forms. In this appendix we visualize the same calculation as a <strong>bundle of $4\times4$ slice matrices</strong>—essentially a third-order $4\times4\times4$ tensor. It extends Appendix A and is the culmination of this book's practice of "putting everything into matrices."

### E.1 Basis $3$-forms and their slice matrices — all 16

The four basis $3$-forms in four dimensions are (compared with the ordering in §10.4, the signs and order of $\omega_2$ and $\omega_3$ differ, but the four forms themselves are the same):

$$
\omega_1 = dt\wedge dx\wedge dy,\qquad
\omega_2 = dt\wedge dx\wedge dz,\qquad
\omega_3 = dt\wedge dy\wedge dz,\qquad
\omega_4 = dx\wedge dy\wedge dz
$$

For each $\omega_i$, we define <strong>slice matrices</strong> $\mathbf{S}_{t}^{(\omega_i)}, \mathbf{S}_{x}^{(\omega_i)}, \mathbf{S}_{y}^{(\omega_i)}, \mathbf{S}_{z}^{(\omega_i)}$ in the coordinate directions $t,x,y,z$. A slice matrix is the $3$-form formed by the three remaining directions after omitting that coordinate direction, recast as a $4\times4$ antisymmetric matrix. Rows and columns are ordered $(t,x,y,z)$. Nonzero entries are $\pm1$. Four bases $\times$ four slices $=$ all $16$ matrices.

<strong>(1)</strong> Slices of $\omega_1 = dt\wedge dx\wedge dy$:

$$
\mathbf{S}_{t}^{(\omega_1)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&1&0\\[2pt]0&-1&0&0\\[2pt]0&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{x}^{(\omega_1)}=\begin{pmatrix}0&0&-1&0\\[2pt]0&0&0&0\\[2pt]1&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

$$
\mathbf{S}_{y}^{(\omega_1)}=\begin{pmatrix}0&1&0&0\\[2pt]-1&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{z}^{(\omega_1)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

<strong>(2)</strong> Slices of $\omega_2 = dt\wedge dx\wedge dz$:

$$
\mathbf{S}_{t}^{(\omega_2)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&0&0\\[2pt]0&-1&0&0\end{pmatrix},\qquad
\mathbf{S}_{x}^{(\omega_2)}=\begin{pmatrix}0&0&0&-1\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]1&0&0&0\end{pmatrix}
$$

$$
\mathbf{S}_{y}^{(\omega_2)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{z}^{(\omega_2)}=\begin{pmatrix}0&1&0&0\\[2pt]-1&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

<strong>(3)</strong> Slices of $\omega_3 = dt\wedge dy\wedge dz$:

$$
\mathbf{S}_{t}^{(\omega_3)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&-1&0\end{pmatrix},\qquad
\mathbf{S}_{x}^{(\omega_3)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

$$
\mathbf{S}_{y}^{(\omega_3)}=\begin{pmatrix}0&0&0&-1\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]1&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{z}^{(\omega_3)}=\begin{pmatrix}0&0&-1&0\\[2pt]0&0&0&0\\[2pt]1&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

<strong>(4)</strong> Slices of $\omega_4 = dx\wedge dy\wedge dz$:

$$
\mathbf{S}_{t}^{(\omega_4)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{x}^{(\omega_4)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&-1&0\end{pmatrix}
$$

$$
\mathbf{S}_{y}^{(\omega_4)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&-1\\[2pt]0&0&0&0\\[2pt]0&1&0&0\end{pmatrix},\qquad
\mathbf{S}_{z}^{(\omega_4)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&-1&0\\[2pt]0&1&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

Of the 16 matrices, $\mathbf{S}_{z}^{(\omega_1)}, \mathbf{S}_{y}^{(\omega_2)}, \mathbf{S}_{x}^{(\omega_3)}, \mathbf{S}_{t}^{(\omega_4)}$ are zero matrices. The remaining 12 each contain one $\pm1$ (and one antisymmetric partner). This is the substance of the $4\times4\times4$ tensor.

### E.2 Writing $dF$ with slice matrices

From the expansion in §10.4, the basis coefficients of $dF$ are given by

$$
\begin{aligned}
A_{txy} &= \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} + \frac{\partial B_z}{\partial t} = (\mathrm{curl}\,\mathbf{E})_z + \frac{\partial B_z}{\partial t}
\quad (\text{coefficient of } \omega_1 = dt\wedge dx\wedge dy) \\[6pt]
A_{txz} &= \frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z} - \frac{\partial B_y}{\partial t} = -(\mathrm{curl}\,\mathbf{E})_y - \frac{\partial B_y}{\partial t}
\quad (\text{coefficient of } \omega_2 = dt\wedge dx\wedge dz) \\[6pt]
A_{tyz} &= \frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z} + \frac{\partial B_x}{\partial t} = (\mathrm{curl}\,\mathbf{E})_x + \frac{\partial B_x}{\partial t}
\quad (\text{coefficient of } \omega_3 = dt\wedge dy\wedge dz) \\[6pt]
A_{xyz} &= \frac{\partial B_x}{\partial x} + \frac{\partial B_y}{\partial y} + \frac{\partial B_z}{\partial z} = \mathrm{div}\,\mathbf{B}
\quad (\text{coefficient of } \omega_4 = dx\wedge dy\wedge dz)
\end{aligned}
$$

Each slice of $dF$ is a linear combination of the four basis slice matrices with coefficients $A_{\cdots}$. For example, the $t$-slice $\mathbf{S}_{t}^{(dF)}$ collapses into a single $4\times4$ antisymmetric matrix with all 16 entries displayed explicitly:

$$
\mathbf{S}_{t}^{(dF)}
{=}
\left(\begin{array}{c|cccc}
 & t & x & y & z \\\hline
t & 0 & 0 & 0 & 0 \\[6pt]
x & 0 & 0 &
\displaystyle \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} + \frac{\partial B_z}{\partial t} &
\displaystyle \frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z} - \frac{\partial B_y}{\partial t} \\[14pt]
y & 0 &
\displaystyle \frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x} - \frac{\partial B_z}{\partial t} &
0 &
\displaystyle \frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z} + \frac{\partial B_x}{\partial t} \\[14pt]
z & 0 &
\displaystyle \frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x} + \frac{\partial B_y}{\partial t} &
\displaystyle \frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y} - \frac{\partial B_x}{\partial t} &
0
\end{array}\right)
$$

The $x,y,z$ slices $\mathbf{S}_{x}^{(dF)}, \mathbf{S}_{y}^{(dF)}, \mathbf{S}_{z}^{(dF)}$ are obtained similarly from four-term linear combinations. The whole of $dF$ is this bundle of four slice matrices.

### E.3 Extracting coefficients by the Frobenius product

The Frobenius product introduced in Appendix D extends directly to $4\times4$ matrices.

> <strong>Note</strong> (not the metric-induced inner product) The Frobenius product here is not the spacetime inner product induced by the Minkowski metric. It is a pairing on arrays for extracting coefficients from the antisymmetric matrix representation. We use it as a coefficient-extraction operation against basis slice matrices; $\frac{1}{2}\operatorname{tr}(A^T B)$ is the computational device for that purpose.

$$
A \cdot B = \frac{1}{2}\operatorname{tr}(A^T B) = \frac{1}{2}\sum_{i=1}^{4}\sum_{j=1}^{4} A_{ij}B_{ij}
$$

With this inner product, each coefficient can be <strong>extracted in one line</strong> from each slice. For example,

$$
A_{txy} = \mathbf{S}_{t}^{(\omega_1)} \cdot \mathbf{S}_{t}^{(dF)}
$$

The only nonzero entries of $\mathbf{S}_{t}^{(\omega_1)}$ are $(x,y)=+1$ and $(y,x)=-1$, so the Frobenius product gives $(1 \cdot S_{xy} + (-1) \cdot S_{yx})/2 = (S_{xy} - S_{yx})/2 = S_{xy}$ (because $\mathbf{S}_{t}^{(dF)}$ is antisymmetric, $S_{yx}=-S_{xy}$). The coefficient pops out immediately.

Similarly, <strong>every coefficient is obtained by the Frobenius product with the corresponding basis slice</strong>. This structure is completely analogous to Appendix D, where $\ast_{2\to1}(\mathbf{M}) = (E_1\!\cdot\!\mathbf{M},\;E_2\!\cdot\!\mathbf{M},\;E_3\!\cdot\!\mathbf{M})$ extracted the components of a $2$-form $\mathbf{M}$. Only the degree has risen from $1\to2$ to $2\to3$, and the inner-product partner has changed from a column vector to a bundle of $4\times4$ matrices.

### E.4 Reading $dF=0$ through the slices

$dF=0$ means that all four slice matrices are zero matrices:

$$
\mathbf{S}_{t}^{(dF)} = \mathbf{0},\quad
\mathbf{S}_{x}^{(dF)} = \mathbf{0},\quad
\mathbf{S}_{y}^{(dF)} = \mathbf{0},\quad
\mathbf{S}_{z}^{(dF)} = \mathbf{0}
$$

Reading the nonzero entries of the $t$-slice (above),
- from the $(x,y)$ entry $=0$: $(\mathrm{curl}\,\mathbf{E})_z + \partial B_z/\partial t = 0$
- from the $(x,z)$ entry $=0$: $-(\mathrm{curl}\,\mathbf{E})_y - \partial B_y/\partial t = 0$
- from the $(y,z)$ entry $=0$: $(\mathrm{curl}\,\mathbf{E})_x + \partial B_x/\partial t = 0$

These three are nothing but $\mathrm{curl}\,\mathbf{E} = -\partial\mathbf{B}/\partial t$. From the nonzero entries of the $z$-slice (arising from $\mathbf{S}_{z}^{(\omega_4)}$) we obtain $\mathrm{div}\,\mathbf{B} = 0$. The appearance is huge, but the content is merely the repetition of the four coefficient comparisons from §10.4.

### E.5 Slice representation of $d_4(\ast_4F) = \mu_0(\ast_4\mathcal{J})$

The source side has the same structure. $\ast_4F$ and $\ast_4\mathcal{J}$ were expanded in §10.5, and $d_4(\ast_4F)$ becomes slice matrices of the same type as $d_4F$—only the positions of the $\mathbf{E}$ and $\mathbf{B}$ coefficients are swapped.

Write the $\omega_1\sim\omega_4$ coefficients of $d_4(\ast_4F)$ as $B_{txy}, B_{txz}, B_{tyz}, B_{xyz}$.

$$
\begin{aligned}
B_{txy} &= \frac{\partial B_x}{\partial y} - \frac{\partial B_y}{\partial x} + \frac{\partial E_z}{\partial t}
\quad (\text{coefficient of } dt\wedge dx\wedge dy \text{ in §10.5}) \\[6pt]
B_{txz} &= \frac{\partial B_x}{\partial z} - \frac{\partial B_z}{\partial x} - \frac{\partial E_y}{\partial t} \\[6pt]
B_{tyz} &= \frac{\partial B_y}{\partial z} - \frac{\partial B_z}{\partial y} + \frac{\partial E_x}{\partial t} \\[6pt]
B_{xyz} &= \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z}
\quad (= \mathrm{div}\,\mathbf{E})
\end{aligned}
$$

Each slice of $d_4(\ast_4F)$ is likewise a linear combination of the basis slice matrices with the four coefficients $B_{\cdots}$, just as for $d_4F$. Writing the $t$-slice term by term:

$$
\begin{aligned}
\mathbf{S}_{t}^{(d_4(\ast_4F))}
&= \left(\frac{\partial B_x}{\partial y} - \frac{\partial B_y}{\partial x} + \frac{\partial E_z}{\partial t}\right)
\begin{pmatrix}0&0&0&0\\[2pt]0&0&1&0\\[2pt]0&-1&0&0\\[2pt]0&0&0&0\end{pmatrix} \\[10pt]
&\quad+ \left(\frac{\partial B_x}{\partial z} - \frac{\partial B_z}{\partial x} - \frac{\partial E_y}{\partial t}\right)
\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&0&0\\[2pt]0&-1&0&0\end{pmatrix} \\[10pt]
&\quad+ \left(\frac{\partial B_y}{\partial z} - \frac{\partial B_z}{\partial y} + \frac{\partial E_x}{\partial t}\right)
\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&-1&0\end{pmatrix}
{+} B_{xyz}
\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
\end{aligned}
$$

Add corresponding entries into a single matrix. Compare with the $t$-slice of $d_4F$—$\mathbf{E}$ and $\mathbf{B}$ (and the cyclic permutations of indices) swap cleanly.

$$
\mathbf{S}_{t}^{(d_4(\ast_4F))}
{=}
\left(\begin{array}{c|cccc}
 & t & x & y & z \\\hline
t & 0 & 0 & 0 & 0 \\[6pt]
x & 0 & 0 &
\displaystyle\frac{\partial B_x}{\partial y} {-} \frac{\partial B_y}{\partial x} {+} \frac{\partial E_z}{\partial t} &
\displaystyle\frac{\partial B_x}{\partial z} {-} \frac{\partial B_z}{\partial x} {-} \frac{\partial E_y}{\partial t} \\[14pt]
y & 0 &
\displaystyle{-}\frac{\partial B_x}{\partial y} {+} \frac{\partial B_y}{\partial x} {-} \frac{\partial E_z}{\partial t} &
0 &
\displaystyle\frac{\partial B_y}{\partial z} {-} \frac{\partial B_z}{\partial y} {+} \frac{\partial E_x}{\partial t} \\[14pt]
z & 0 &
\displaystyle{-}\frac{\partial B_x}{\partial z} {+} \frac{\partial B_z}{\partial x} {+} \frac{\partial E_y}{\partial t} &
\displaystyle{-}\frac{\partial B_y}{\partial z} {+} \frac{\partial B_z}{\partial y} {-} \frac{\partial E_x}{\partial t} &
0
\end{array}\right)
$$

The right-hand side $\mu_0(\ast_4\mathcal{J})$ can also be written as the same linear combination of four slice matrices. Re-expanding $\ast_4\mathcal{J}$ in the basis order of this appendix (see §10.5), the coefficients of $\omega_1\!\sim\!\omega_4$ are, in order, $-\mu_0 c J_z,\; +\mu_0 c J_y,\; -\mu_0 c J_x,\; \rho_{\mathrm e}/\varepsilon_0$. That is,

$$
\mathbf{S}_{t}^{(d_4(\ast_4F))} = \mathbf{S}_{t}^{(\mu_0\ast_4\mathcal{J})},\quad
\mathbf{S}_{x}^{(d_4(\ast_4F))} = \mathbf{S}_{x}^{(\mu_0\ast_4\mathcal{J})},\quad
\mathbf{S}_{y}^{(d_4(\ast_4F))} = \mathbf{S}_{y}^{(\mu_0\ast_4\mathcal{J})},\quad
\mathbf{S}_{z}^{(d_4(\ast_4F))} = \mathbf{S}_{z}^{(\mu_0\ast_4\mathcal{J})}
$$

Reading the nonzero entries of the $t$-slice gives $-\mathrm{curl}\,\mathbf{B} + \partial\mathbf{E}/\partial t = -c\mu_0\mathbf{J}$, i.e. the components of $\mathrm{curl}\,\mathbf{B} = c\mu_0\mathbf{J} + \partial\mathbf{E}/\partial t$. From the $(x,y)$ entry of the $z$-slice we obtain $\mathrm{div}\,\mathbf{E} = \rho_{\mathrm e}/\varepsilon_0$.

---

Thus the full content of Maxwell's equations has been visualized as a bundle of $4\times4\times4$ slice matrices. What is written in each cell of this "giant array" is nothing but a combination of partial derivatives—and we have seen how the two algebraic operations of four-dimensional exterior differentiation $d_4$ and the Hodge star $\ast_4$ describe physical laws in the tidy grammar of matrices. That is the achievement of this appendix.
