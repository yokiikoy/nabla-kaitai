## Appendix A: Tensor-Product Representation of the Volume-Measuring Device — Full Component Calculation

In §2.5.5 we stated that contraction of $\widehat{\epsilon}$ (components $\epsilon_{ijk}$) with three vectors agrees with the determinant. Here we follow that entire process by hand calculation and verify it term by term.

#### A.1 Extension of the Tensor Product to Three Arguments

Let us review. The $(i,j)$ component of $dx \otimes dy$ was the product of the $i$th component of $dx$ and the $j$th component of $dy$:
$$(dx \otimes dy)_{ij} = (dx)_i\,(dy)_j$$

Extension to three measuring devices is natural—we merely add one more index:
$$(dx \otimes dy \otimes dz)_{ijk} = (dx)_i\,(dy)_j\,(dz)_k$$

Substituting $dx = (1\ 0\ 0)$, $dy = (0\ 1\ 0)$, $dz = (0\ 0\ 1)$, among the $3^3 = 27$ cells only the one at $(i,j,k) = (1,2,3)$ is $1$; the remaining 26 cells are all $0$. Each of the other five permutations ($dx \otimes dz \otimes dy$, and so on) is likewise nonzero in exactly one place—for $dy \otimes dx \otimes dz$ the $1$ sits at $(2,1,3)$, and for $dz \otimes dy \otimes dx$ at $(3,2,1)$.

#### A.2 Antisymmetrization — Superposing Six Permutations with Signs

In §2.4.5, for area we had $dx \wedge dy = dx \otimes dy - dy \otimes dx$ (a signed sum of two terms). The three measuring devices are $dx, dy, dz$ in Cartesian coordinates. There are $3! = 6$ permutations, so for each permutation $\sigma$ we connect $(dx,dy,dz)$ in the permuted order by the tensor product $\otimes$, attach the sign $\mathrm{sgn}(\sigma)$, and sum over $S_3$—that is, the following six-line sum written in one line in the language of permutations.

> <strong>Note</strong> (symmetric group and sign of a permutation) $S_3$ is the symmetric group of degree 3 (the set of permutations). $\mathrm{sgn}(\sigma)$ is defined to be <strong>$+1$ for an even permutation</strong> and <strong>$-1$ for an odd permutation</strong>.

Written out:

$$\underbrace{dx \otimes dy \otimes dz}_{(1,2,3)\text{ with }+1} - \underbrace{dx \otimes dz \otimes dy}_{(1,3,2)\text{ with }-1} + \underbrace{dy \otimes dz \otimes dx}_{(2,3,1)\text{ with }+1}$$
$$- \underbrace{dy \otimes dx \otimes dz}_{(2,1,3)\text{ with }-1} + \underbrace{dz \otimes dx \otimes dy}_{(3,1,2)\text{ with }+1} - \underbrace{dz \otimes dy \otimes dx}_{(3,2,1)\text{ with }-1}$$

Superposing these six “arrays with only one nonzero entry” with signs leaves only 6 of the 27 components at $\pm 1$; the other 21 are zero. Compare with the permutation table in §2.5.2—this is the construction principle that yields each component $\epsilon_{ijk}$ of $\widehat{\epsilon}$.

#### A.3 Writing Down the Matrix for Each Component

Let us verify cell by cell the three component matrices shown in §2.5.5.

<strong>Component 1 (</strong>$i = 1$<strong>, </strong>$x$<strong>):</strong> among the six terms, those with $i = 1$ are $+1$ at $(1,2,3)$ and $-1$ at $(1,3,2)$.

$$\epsilon_{1,\cdot,\cdot} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$$

<strong>Component 2 (</strong>$i = 2$<strong>, </strong>$y$<strong>):</strong> $+1$ at $(2,3,1)$ and $-1$ at $(2,1,3)$.

$$\epsilon_{2,\cdot,\cdot} = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$$

<strong>Component 3 (</strong>$i = 3$<strong>, </strong>$z$<strong>):</strong> $+1$ at $(3,1,2)$ and $-1$ at $(3,2,1)$.

$$\epsilon_{3,\cdot,\cdot} = \begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

To repeat: these are exactly the matrices of $dy \wedge dz$, $dz \wedge dx$, and $dx \wedge dy$, respectively.

#### A.4 Feeding Three Vectors — The Full Contraction Process

<strong>Step 1: weighted sum over index </strong>$i$<strong> using the components of </strong>$\mathbf{v}_1$<strong> (collapse index </strong>$i$<strong>)</strong>

Add the three area-measuring-device matrices, weighted by the components of $\mathbf{v}_1$. One vector is fed in and the $3$-dimensional array drops to a $3 \times 3$ matrix:

$$M := \sum_i v_{1i}\, \epsilon_{i,\cdot,\cdot} = x_1 \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix} + y_1 \begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} + z_1 \begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

Adding component by component gives:

$$M = \begin{pmatrix} 0 & z_1 & -y_1 \\ -z_1 & 0 & x_1 \\ y_1 & -x_1 & 0 \end{pmatrix}$$

An area-measuring device specialized to $\mathbf{v}_1$ has appeared, built from the three area-measuring devices weighted by the components of $\mathbf{v}_1$. Note that it is an antisymmetric matrix—the antisymmetry in the indices of $\widehat{\epsilon}$ is inherited.

<strong>Step 2: sandwich the matrix with the remaining two vectors (collapse indices </strong>$j, k$<strong>)</strong>

What remains is the familiar “row $\times$ matrix $\times$ column” from §2.4:

$$V = \mathbf{v}_2^T\, M\, \mathbf{v}_3 = \begin{pmatrix} x_2 & y_2 & z_2 \end{pmatrix} \begin{pmatrix} 0 & z_1 & -y_1 \\ -z_1 & 0 & x_1 \\ y_1 & -x_1 & 0 \end{pmatrix} \begin{pmatrix} x_3 \\ y_3 \\ z_3 \end{pmatrix}$$

First compute $\mathbf{v}_2^T \times M$ (row $\times$ matrix → row):

$$= \begin{pmatrix} y_1 z_2 - z_1 y_2, & z_1 x_2 - x_1 z_2, & x_1 y_2 - x_2 y_1 \end{pmatrix}$$

Finally, the sum of products of corresponding components of the resulting row vector and $\mathbf{v}_3$ (row $\times$ column → scalar):

$$V = (y_1 z_2 - z_1 y_2)\,x_3 + (z_1 x_2 - x_1 z_2)\,y_3 + (x_1 y_2 - x_2 y_1)\,z_3$$

Expanding and collecting terms gives:

$$= x_1 y_2 z_3 + y_1 z_2 x_3 + z_1 x_2 y_3 - y_1 x_2 z_3 - x_1 z_2 y_3 - z_1 y_2 x_3$$

which <strong>matches the determinant in §2.5.2 term for term—all six terms agree.</strong>
