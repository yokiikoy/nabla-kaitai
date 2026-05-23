## Appendix B: Matrix Representation of the Exterior Derivative

The main text of this chapter proceeded with the basis $dx, dy, dz$ and the algebra of the wedge product. Here we rewrite the exterior derivative in the language of matrix representations, following the book's convention since Chapter 2 — <strong>arranging every component without exception into matrices</strong>.

### B.1 $0$-form: the $1 \times 3$ row vector of $df$

For $f = f(x,y,z)$, as defined in Chapter 1 §1.2:

$$df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy + \frac{\partial f}{\partial z}\,dz$$

As a row vector ($1 \times 3$ matrix):

$$df = \begin{pmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} & \frac{\partial f}{\partial z} \end{pmatrix}$$

### B.2 $1$-form: the Jacobian matrix $\mathbf{J}$ of the coefficients

For $\omega = P\,dx + Q\,dy + R\,dz$, the $3 \times 3$ matrix that arranges <strong>all</strong> partial derivatives of the coefficients $(P,Q,R)$ is:

$$\mathbf{J} := \begin{pmatrix}
\frac{\partial P}{\partial x} & \frac{\partial P}{\partial y} & \frac{\partial P}{\partial z} \\
\frac{\partial Q}{\partial x} & \frac{\partial Q}{\partial y} & \frac{\partial Q}{\partial z} \\
\frac{\partial R}{\partial x} & \frac{\partial R}{\partial y} & \frac{\partial R}{\partial z}
\end{pmatrix}$$

This is the Jacobian matrix of the vector field obtained by stacking $(P,Q,R)$ as a column. The reason §5.1 said that "a mere matrix of partial derivatives is not enough" is precisely that this $\mathbf{J}$ is not antisymmetric.

### B.3 $d\omega = \mathbf{J}^T - \mathbf{J}$

The result of §5.5 is:

$$d\omega = (\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z})\,dy \wedge dz + (\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,dz \wedge dx + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy$$

Following the convention of Chapter 2 §2.4.4, we seek the antisymmetric matrix $\mathbf{M}$ such that $(d\omega)(\mathbf{v}_1, \mathbf{v}_2) = \mathbf{v}_1^T \mathbf{M} \mathbf{v}_2$ for arbitrary column vectors $\mathbf{v}_1, \mathbf{v}_2$.

Writing out the entries of $\mathbf{J}^T - \mathbf{J}$:

$$\mathbf{J}^T - \mathbf{J} = \begin{pmatrix}
0 & \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} & \frac{\partial R}{\partial x} - \frac{\partial P}{\partial z} \\
\frac{\partial P}{\partial y} - \frac{\partial Q}{\partial x} & 0 & \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \\
\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} & \frac{\partial Q}{\partial z} - \frac{\partial R}{\partial y} & 0
\end{pmatrix}$$

That is, comparing with the matrix representation of a $2$-form found in Chapter 2:

$$d\omega = \mathbf{J}^T - \mathbf{J}$$

Thus, <strong>the matrix representation of the exterior derivative $d\omega$ is the antisymmetric matrix obtained by subtracting the Jacobian matrix of the coefficients from its transpose.</strong>

### B.4 $2$-form: $d\eta$ and the trace of the Jacobian matrix

For $\eta = A\,dy \wedge dz + B\,dz \wedge dx + C\,dx \wedge dy$, let the Jacobian matrix of the coefficients $(A,B,C)$ be:

$$\mathbf{J}_\eta := \begin{pmatrix}
\frac{\partial A}{\partial x} & \frac{\partial A}{\partial y} & \frac{\partial A}{\partial z} \\
\frac{\partial B}{\partial x} & \frac{\partial B}{\partial y} & \frac{\partial B}{\partial z} \\
\frac{\partial C}{\partial x} & \frac{\partial C}{\partial y} & \frac{\partial C}{\partial z}
\end{pmatrix}$$

Then the coefficient in the result of §5.7, $d\eta = (\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z})\,dx \wedge dy \wedge dz$, agrees with the <strong>trace</strong> (sum of diagonal entries) of $\mathbf{J}_\eta$:

$$\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z} = \operatorname{tr}(\mathbf{J}_\eta)$$

#### B.4.1 The 27 components of $d\eta$ — expanded into three matrices

The antisymmetric components of $\eta$ are $\eta_{yz}=A,\; \eta_{zx}=B,\; \eta_{xy}=C$ (the others are sign reversals or $0$). Write the components of $d\eta$ as $(d\eta)_{abc} = \partial_a \eta_{bc}$, where $\partial_x=\frac{\partial}{\partial x}$, $\partial_y=\frac{\partial}{\partial y}$, $\partial_z=\frac{\partial}{\partial z}$, and $a,b,c \in \{x,y,z\}$, so there are $3^3=27$ components. Arranging them into three $3 \times 3$ matrices with $a$ fixed gives:

$$
\begin{aligned}
d\eta_{x,\cdot,\cdot}
&= \begin{pmatrix}
0 & \frac{\partial C}{\partial x} & -\frac{\partial B}{\partial x} \\
-\frac{\partial C}{\partial x} & 0 & \frac{\partial A}{\partial x} \\
\frac{\partial B}{\partial x} & -\frac{\partial A}{\partial x} & 0
\end{pmatrix}, \\
d\eta_{y,\cdot,\cdot}
&= \begin{pmatrix}
0 & \frac{\partial C}{\partial y} & -\frac{\partial B}{\partial y} \\
-\frac{\partial C}{\partial y} & 0 & \frac{\partial A}{\partial y} \\
\frac{\partial B}{\partial y} & -\frac{\partial A}{\partial y} & 0
\end{pmatrix}, \\
d\eta_{z,\cdot,\cdot}
&= \begin{pmatrix}
0 & \frac{\partial C}{\partial z} & -\frac{\partial B}{\partial z} \\
-\frac{\partial C}{\partial z} & 0 & \frac{\partial A}{\partial z} \\
\frac{\partial B}{\partial z} & -\frac{\partial A}{\partial z} & 0
\end{pmatrix}
\end{aligned}
$$

When these $27$ components are contracted with the corresponding basis wedge products of $1$-forms (for example, if $a=x,\;b=y,\;c=z$, then $dx \wedge dy \wedge dz$), terms with repeated indices (diagonal entries, $b=c$, and so on) vanish because $dx \wedge dx = 0$, and only the $6$ terms with all of $a,b,c$ distinct (permutations of $3!$) survive. Each is summed with its sign. Because each component is antisymmetrized and arranged in a matrix here, we are double-counting; as in Chapter 2 §2.4.4 and Appendix D, a factor of $\frac{1}{2}$ enters:

$$d\eta = \left( \frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z} \right) dx \wedge dy \wedge dz$$

In other words, of the $27$ components of $d\eta$, $6$ survive and pair up to converge to the trace of $\mathbf{J}_\eta$.

A $3$-form has only the single basis element $dx \wedge dy \wedge dz$, so as a matrix it degenerates to a scalar coefficient.

### B.5 $d^2 f = 0$ and the Hessian

The Hessian of a $0$-form $f$:

$$\mathbf{H}_f := \begin{pmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} & \frac{\partial^2 f}{\partial x \partial z} \\
\frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} & \frac{\partial^2 f}{\partial y \partial z} \\
\frac{\partial^2 f}{\partial z \partial x} & \frac{\partial^2 f}{\partial z \partial y} & \frac{\partial^2 f}{\partial z^2}
\end{pmatrix}$$

arranges the second partial derivatives of $f$. If $f$ is $C^2$, then $\mathbf{H}_f$ is a symmetric matrix ($\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$, and so on).

$d(df) = 0$ is the §5.5 formula for $d\omega$ with $(P,Q,R) = (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z})$. We have $\mathbf{J} = \mathbf{H}_f$, and because $\mathbf{H}_f$ is symmetric, $\mathbf{J}^T - \mathbf{J} = 0$; hence $d(df) = 0$. In the language of matrices, this is rephrased as "the antisymmetric part of the Hessian is zero."

## Appendix C: Integral Forms of Electromagnetism and Differential Forms

This appendix verifies, in component form, the passage from the integral forms of the four fundamental equations of electromagnetism to their local forms. What we use here are the exterior derivative $d$ and the degree of a differential form. The metric of space does not appear in this localization itself.

### C.1 Degrees of physical quantities

Quantities measured along a line are placed as $1$-forms, quantities measured through a surface as $2$-forms, and quantities measured over a volume as $3$-forms. In components:

$$
E = E_x\,dx+E_y\,dy+E_z\,dz,
\qquad
H = H_x\,dx+H_y\,dy+H_z\,dz
$$

$$D = D_x\,dy\wedge dz + D_y\,dz\wedge dx + D_z\,dx\wedge dy$$

$$B = B_x\,dy\wedge dz + B_y\,dz\wedge dx + B_z\,dx\wedge dy$$

$$J = J_x\,dy\wedge dz + J_y\,dz\wedge dx + J_z\,dx\wedge dy$$

$$
\rho = \rho\,dx\wedge dy\wedge dz
$$

To keep the notation simple, we write both the coefficient representing charge density and the $3$-form obtained by multiplying it by the volume form with the same symbol $\rho$.

$E$ and $H$ are $1$-forms measured along a line; $D$, $B$, and $J$ are $2$-forms measured through a surface; $\rho$ is a $3$-form measured over a volume.

### C.2 Gauss's law for charge

The integral form is:

$$
\int_{\partial V}D=\int_V\rho
$$

Applying the generalized Stokes' theorem to the left-hand side:

$$
\int_{\partial V}D=\int_V dD
$$

Therefore, if

$$
\int_V dD=\int_V\rho
$$

holds for every region $V$, the local form is:

$$
dD=\rho
$$

Expanding in components:

$$
dD
=
\left(\frac{\partial D_x}{\partial x}
{}+\frac{\partial D_y}{\partial y}
{}+\frac{\partial D_z}{\partial z}\right)
dx\wedge dy\wedge dz
$$

Hence:

$$
\frac{\partial D_x}{\partial x}
{}+\frac{\partial D_y}{\partial y}
{}+\frac{\partial D_z}{\partial z}
=\rho
$$

### C.3 The law of magnetic flux

The integral form stating that the net magnetic flux through a closed surface is zero is:

$$
\int_{\partial V}B=0
$$

By the generalized Stokes' theorem:

$$
\int_V dB=0
$$

If this holds for every region $V$, the local form is:

$$
dB=0
$$

Expanding in components:

$$
dB
=
\left(\frac{\partial B_x}{\partial x}
{}+\frac{\partial B_y}{\partial y}
{}+\frac{\partial B_z}{\partial z}\right)
dx\wedge dy\wedge dz
$$

Therefore:

$$
\frac{\partial B_x}{\partial x}
{}+\frac{\partial B_y}{\partial y}
{}+\frac{\partial B_z}{\partial z}
=0
$$

### C.4 Faraday's law

The integral form is:

$$
\int_{\partial S}E
=
-\frac{\partial}{\partial t}\int_S B
$$

Applying the generalized Stokes' theorem to the left-hand side:

$$
\int_S dE
=
-\frac{\partial}{\partial t}\int_S B
$$

If this holds for every surface $S$, the local form is:

$$
dE=-\frac{\partial B}{\partial t}
$$

Expanding in components:

$$dE = \left(\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z}\right)dy\wedge dz + \left(\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x}\right)dz\wedge dx + \left(\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y}\right)dx\wedge dy$$

On the other hand,

$$
-\frac{\partial B}{\partial t}
=
-\frac{\partial B_x}{\partial t}\,dy\wedge dz
-\frac{\partial B_y}{\partial t}\,dz\wedge dx
-\frac{\partial B_z}{\partial t}\,dx\wedge dy
$$

so the components are:

$$
\frac{\partial E_z}{\partial y}
-
\frac{\partial E_y}{\partial z}
=
-\frac{\partial B_x}{\partial t}
$$

$$
\frac{\partial E_x}{\partial z}
-
\frac{\partial E_z}{\partial x}
=
-\frac{\partial B_y}{\partial t}
$$

$$
\frac{\partial E_y}{\partial x}
-
\frac{\partial E_x}{\partial y}
=
-\frac{\partial B_z}{\partial t}
$$

### C.5 Ampère–Maxwell's law

The integral form is:

$$
\int_{\partial S}H
=
\int_SJ+\frac{\partial}{\partial t}\int_S D
$$

Applying the generalized Stokes' theorem to the left-hand side:

$$
\int_S dH
=
\int_SJ+\frac{\partial}{\partial t}\int_S D
$$

If this holds for every surface $S$, the local form is:

$$
dH=J+\frac{\partial D}{\partial t}
$$

Expanding in components:

$$dH = \left(\frac{\partial H_z}{\partial y}-\frac{\partial H_y}{\partial z}\right)dy\wedge dz + \left(\frac{\partial H_x}{\partial z}-\frac{\partial H_z}{\partial x}\right)dz\wedge dx + \left(\frac{\partial H_y}{\partial x}-\frac{\partial H_x}{\partial y}\right)dx\wedge dy$$

Also,

$$J+\frac{\partial D}{\partial t} = \left(J_x+\frac{\partial D_x}{\partial t}\right)dy\wedge dz + \left(J_y+\frac{\partial D_y}{\partial t}\right)dz\wedge dx + \left(J_z+\frac{\partial D_z}{\partial t}\right)dx\wedge dy$$

so the components are:

$$
\frac{\partial H_z}{\partial y}
-
\frac{\partial H_y}{\partial z}
=
J_x+\frac{\partial D_x}{\partial t}
$$

$$
\frac{\partial H_x}{\partial z}
-
\frac{\partial H_z}{\partial x}
=
J_y+\frac{\partial D_y}{\partial t}
$$

$$
\frac{\partial H_y}{\partial x}
-
\frac{\partial H_x}{\partial y}
=
J_z+\frac{\partial D_z}{\partial t}
$$

### C.6 Where a metric is needed

The four local forms above can be written using only the exterior derivative $d$ and the degree of differential forms. At this stage, no metric for measuring lengths or angles is used.

A metric becomes necessary when relating $E$ to $D$ and $B$ to $H$. It is also needed when pairing $1$-forms with $2$-forms so that the usual three-component fields can be treated as objects of the same kind.

The Hodge star, introduced in the next chapter, is the tool that provides this correspondence.
