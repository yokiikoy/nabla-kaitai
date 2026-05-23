## Appendix F: The Four Equations of Chapter 5 and the Two Equations of Chapter 10

In the main text of Chapter 10, Maxwell's equations were written symbolically as two equations on four-dimensional spacetime:

$$
dF=0,
\qquad
d(\ast F)=\mu_0(\ast\mathcal{J})
$$

In component calculations, we read this as $d_4F=0,\;d_4(\ast_4F)=\mu_0(\ast_4\mathcal J)$.

However, in Chapter 5, rather than bundling everything at once into a $2$-form on four-dimensional spacetime, we worked with a viewpoint that treats the electric field, magnetic field, current, and charge at each instant as differential forms on space.

This appendix confirms that the "four equations on space" from Chapter 5 and the "two equations on spacetime" from the main text of Chapter 10 are simply the same Maxwell equations written in different splittings.

### F.1 $(E,B,J,\rho_{\mathrm e})$ on space

Consider space $(x,y,z)$ at each instant $t$.

Place the electric field as a $1$-form on space:

$$
E = E_x\,dx + E_y\,dy + E_z\,dz
$$

Place the magnetic field as a $2$-form on space:

$$
B = B_x\,dy\wedge dz + B_y\,dz\wedge dx + B_z\,dx\wedge dy
$$

The current density is also represented as a $2$-form, as a quantity that passes through space:

$$
J = J_x\,dy\wedge dz + J_y\,dz\wedge dx + J_z\,dx\wedge dy
$$

The charge density is written as a $3$-form on space:

$$
\rho_{\mathrm e}\,dx\wedge dy\wedge dz
$$

The $d$ and $\ast$ used here are the three-dimensional spatial $d$ and $\ast$. When we wish to distinguish them from the four-dimensional spacetime $d$ and $\ast$ used in the main text of Chapter 10, we write

$$
d_3,\quad \ast_3,
\qquad
d_4,\quad \ast_4
$$

### F.2 The four equations on space

In this notation, Maxwell's equations become the following four:

$$
d_3B=0
$$

$$
d_3E+\frac{\partial B}{\partial t}=0
$$

$$
d_3(\ast_3E)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)
$$

$$
d_3(\ast_3B)=\mu_0 c\,J+\frac{\partial(\ast_3E)}{\partial t}
$$

These are the four equations in differential-form style from Chapter 5.

Here the right-hand side has $\ast_3$ applied to read the scalar field $\rho_{\mathrm e}/\varepsilon_0$ as a $3$-form on space. In Cartesian coordinates,

$$
\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)=\frac{\rho_{\mathrm e}}{\varepsilon_0}\,dx\wedge dy\wedge dz
$$

In this book we do not place the vector-analytic $\mathrm{div}$ as a basic operation from the outset, but read it as the composite of $d$ and $\ast$:

$$
\mathrm{div}=\ast_3 d_3\ast_3
$$

Therefore, even for a scalar field such as charge density, on the right-hand side of an equation to be integrated we convert it to a $3$-form via $\ast_3$ before comparing. In particular, for the third equation we act with $\ast_3$ on both sides to read

$$
\ast_3d_3(\ast_3E)=\frac{\rho_{\mathrm e}}{\varepsilon_0}
$$

The left-hand side is what this book's dictionary calls $\mathrm{div}\,\mathbf E$.

Translating back to vector-analytic notation, these are respectively

$$
\mathrm{div}\,\mathbf B=0,
\qquad
\mathrm{curl}\,\mathbf E=-\frac{\partial\mathbf B}{\partial t},
$$

$$
\mathrm{div}\,\mathbf E=\frac{\rho_{\mathrm e}}{\varepsilon_0},
\qquad
\mathrm{curl}\,\mathbf B=\mu_0 c\,\mathbf J+\frac{\partial\mathbf E}{\partial t}
$$

Here $t$ and $\mathbf B$ are, as in the main text of Chapter 10, already normalized quantities with

$$
t=ct_{\mathrm{SI}},
\qquad
\mathbf B=c\mathbf B_{\mathrm{SI}}
$$

> <strong>Note</strong> (There is also a way to write without the metric) In this book we do not take the vector-analytic $\mathrm{div}$ as our starting basic operation, but read $\mathrm{div}=\ast d\ast$ to match the dictionary built up so far. Gauss's law is also written as $d_3(\ast_3E) = \ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)$ and then, when needed, read as $\mathrm{div}\,\mathbf E=\rho_{\mathrm e}/\varepsilon_0$. That is, we move back and forth among scalar fields, vector fields, and forms using the $\ast$ built from the metric. Maxwell's equations, however, also admit a standpoint that does not use the metric. In the view emphasized in Hehl–Obukhov's *Foundations of Classical Electrodynamics: Charge, Flux, and Metric*, one first separates two forms $F$ and $H$ and writes $dF=0, dH=J$. Here the Hodge star does not enter the equations themselves. The metric and properties of the medium enter later as a relation linking $H$ and $F$. This book does not go deep in that direction. The purpose is strictly to use the dictionary of $d$ and $\ast$ built up so far and see how the usual vector-analytic equations appear as components.

### F.3 Two equations emerge from $d_4F=0$

In the main text of Chapter 10, the electromagnetic field $F$ was defined by

$$
F=-E_x\,dt\wedge dx-E_y\,dt\wedge dy-E_z\,dt\wedge dz+B_x\,dy\wedge dz+B_y\,dz\wedge dx+B_z\,dx\wedge dy
$$

Using the spatial $E$ and $B$, this can be written as

$$
F=-dt\wedge E+B
$$

For a spatial form $\alpha(t)$,

$$
d_4\alpha = dt\wedge\frac{\partial\alpha}{\partial t}+d_3\alpha
$$

Therefore, computing

$$
d_4F=d_4(-dt\wedge E+B)
$$

we have

$$
d_4(-dt\wedge E)=dt\wedge d_3E
$$

and

$$
d_4B=dt\wedge\frac{\partial B}{\partial t}+d_3B
$$

Hence

$$
d_4F=dt\wedge\left(d_3E+\frac{\partial B}{\partial t}\right)+d_3B.
$$

Therefore,

$$
d_4F=0
$$

is the same as setting to zero separately the part that contains $dt$ and the part that does not, giving

$$
d_3E+\frac{\partial B}{\partial t}=0,
\qquad
d_3B=0
$$

In other words, the first equation of the main text of Chapter 10,

$$
d_4F=0
$$

splits in Chapter 5 style into the two equations

$$
d_3B=0,
\qquad
d_3E+\frac{\partial B}{\partial t}=0
$$

### F.4 The remaining two emerge from $d_4(\ast_4F)=\mu_0(\ast_4\mathcal J)$

Next we look at the source side.

Under the conventions of the main text of Chapter 10,

$$
\ast_4F= B_x\,dt\wedge dx+B_y\,dt\wedge dy+B_z\,dt\wedge dz+E_x\,dy\wedge dz+E_y\,dz\wedge dx+E_z\,dx\wedge dy.
$$

In spatial notation, this is

$$
\ast_4F=dt\wedge(\ast_3B)+\ast_3E
$$

Indeed,

$$
\ast_3B=B_x\,dx+B_y\,dy+B_z\,dz
$$

so

$$
dt\wedge(\ast_3B)=B_x\,dt\wedge dx+B_y\,dt\wedge dy+B_z\,dt\wedge dz
$$

Also,

$$
\ast_3E=E_x\,dy\wedge dz+E_y\,dz\wedge dx+E_z\,dx\wedge dy
$$

Apply $d_4$ to this.

First,

$$
d_4\bigl(dt\wedge(\ast_3B)\bigr)=-dt\wedge d_3(\ast_3B)
$$

On the other hand,

$$
d_4(\ast_3E)=dt\wedge\frac{\partial(\ast_3E)}{\partial t}+d_3(\ast_3E).
$$

Therefore,

$$
d_4(\ast_4F)=dt\wedge\left(\frac{\partial(\ast_3E)}{\partial t}-d_3(\ast_3B)\right)+d_3(\ast_3E).
$$

The right-hand side, under the conventions of the main text of Chapter 10, is

$$
\mu_0(\ast_4\mathcal J)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)-\mu_0 c\,dt\wedge J
$$

where

$$
J=J_x\,dy\wedge dz+J_y\,dz\wedge dx+J_z\,dx\wedge dy
$$

Therefore, comparing the part that does not contain $dt$,

$$
d_3(\ast_3E)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right).
$$

And comparing the part that contains $dt$,

$$
\frac{\partial(\ast_3E)}{\partial t}-d_3(\ast_3B)=-\mu_0 c\,J.
$$

Rearranging,

$$
d_3(\ast_3B)=\mu_0 c\,J+\frac{\partial(\ast_3E)}{\partial t}.
$$

Therefore, the second equation of the main text of Chapter 10,

$$
d_4(\ast_4F)=\mu_0(\ast_4\mathcal J)
$$

splits in Chapter 5 style into the two equations

$$
d_3(\ast_3E)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)
$$

and

$$
d_3(\ast_3B)=\mu_0 c\,J+\frac{\partial(\ast_3E)}{\partial t}
$$

### F.5 Summary

In the differential-form style of Chapter 5, Maxwell's equations appear as four equations on space:

$$
d_3B=0
$$

$$
d_3E+\frac{\partial B}{\partial t}=0
$$

$$
d_3(\ast_3E)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)
$$

$$
d_3(\ast_3B)=\mu_0 c\,J+\frac{\partial(\ast_3E)}{\partial t}
$$

On the other hand, in the main text of Chapter 10, time is treated as one coordinate on the same footing as space, and the electric and magnetic fields are bundled into $F$:

$$
F=-dt\wedge E+B
$$

Then the four equations above consolidate into the two

$$
d_4F=0
$$

and

$$
d_4(\ast_4F)=\mu_0(\ast_4\mathcal J)
$$

In other words, the fact that four become two is not so much compressing the equations as reassembling what was viewed with space and time separated into a single spacetime $2$-form measuring device.

The four equations of Chapter 5 are the way of writing that looks at space and time separately.
The two equations of Chapter 10 are the way of writing that looks at a spacetime $2$-form.

Both are looking at the same Maxwell equations. What differs is what one treats as a single bundled measuring device.
