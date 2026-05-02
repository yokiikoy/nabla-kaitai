<!-- source-pdf: FleischVectorsAndTensors.pdf | pages 181-210 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 181–210

## Page 181

6.1 The inertia tensor
169
y′
z′
m1
r1
m4
m5
r5
r4
Velocity v4 is
out of page
L4 = m4r4× v4
Velocity v1 is
into page
Velocity v5 is
into page
L1 = m1r1× v1
L5= m5r5× v5
Figure 6.4 Angular momentum vectors for masses in plane of page.
And there’s the answer: the other four masses contribute exactly as much
angular momentum in the positive y-direction as m5 contributes to the negative
y-direction, as illustrated in Figure 6.4. And remember from Chapter 5 that
you can add tensors by adding their components. So when you add the inertia
tensor for m5 to the inertia tensor for the other four masses, you get the (nicely
diagonal) inertia tensor for the ﬁve-mass pyramid.
To demonstrate the balance between m5 and the other four masses, you may
ﬁnd it interesting to again move m5 up the z-axis to twice its original height
and then perform the 30 degree rotation of the coordinate axes. In this case,
you should ﬁnd the inertia tensor to be
⃗⃗I =
⎛
⎝
20ma2
0
0
0
17ma2
−5.2ma2
0
−5.2ma2
11ma2
⎞
⎠,
and clearly the Iyz terms from m5 and the other four masses no longer
cancel.
You can determine the inertia tensor for any orientation of the coordinate
axes by applying rotations about multiple axes. If you wish, for example, to
rotate ﬁrst about the x-axis by angle θ1 and then about the y-axis by angle θ2,
you can combine the rotation matrices as

## Page 182

170
Tensor applications
⎛
⎝
x′
y′
z′
⎞
⎠=
⎛
⎝
cos θ2
0
sin θ2
0
1
0
−sin θ2
0
cos θ2
⎞
⎠
⎛
⎝
1
0
0
0
cos θ1
sin θ1
0
−sin θ1
cos θ1
⎞
⎠
⎛
⎝
x
y
z
⎞
⎠,
(6.7)
which in the case of two 30 degree rotations (ﬁrst about the x-axis and then
about the y-axis) gives a combined rotation matrix of
⎛
⎝
x′
y′
z′
⎞
⎠=
⎛
⎝
0.866
−0.25
4.33
0
0.866
0.5
−0.5
−0.433
0.75
⎞
⎠
⎛
⎝
x
y
z
⎞
⎠.
(6.8)
If you leave m5 at height 4a and then apply this rotation to the coordinates,
the inertia tensor becomes
⃗⃗I =
⎛
⎝
17.8ma2
2.6ma2
3.9ma2
2.6ma2
17ma2
−4.5ma2
3.9ma2
−4.5ma2
13.3ma2
⎞
⎠.
(6.9)
You can perform a quick check on your calculation by verifying that the
coordinate-axis rotation has changed neither the trace nor the determinant of
the matrix.2
Instead of ﬁnding the new coordinates of each mass in the rotated system,
an alternative approach allows you to ﬁnd the inertia tensor for rotated coordi-
nates directly. That approach is to apply a “similarity transform” to the original
inertia tensor. Here’s how that works: the angular momentum is related to
the inertia tensor and angular velocity in the original (unrotated) coordinate
system as
⃗L = ⃗⃗I ⃗ω,
and you rotate the coordinates by applying a rotation matrix R (which may be
the product of several rotation matrices). You can therefore write
⃗L′ = R ⃗L = R( ⃗⃗I ⃗ω).
And since the product of any matrix and its inverse is just the identity matrix,
you can insert the term R−1R in front of ⃗ω:
⃗L′ = R ⃗L = R ⃗⃗I (R−1R)⃗ω
= (R ⃗⃗I R−1)R ⃗ω.
But R ⃗ω is just ⃗ω′, so
⃗L′ = (R ⃗⃗I R−1)⃗ω′.
2 The matrix review on the book’s website explains how to do these calculations.

## Page 183

6.2 The electromagnetic ﬁeld tensor
171
Thus the expression (R ⃗⃗I R−1) relates angular momentum to angular veloc-
ity in the rotated coordinate system, which means that this expression is the
inertia tensor in that system. So instead of calculating the new coordinates for
each mass and plugging them into the equation for the inertia tensor, you can
instead simply apply the rotation matrix and its inverse to the matrix represent-
ing the inertia tensor directly (but remember that the sequence matters when
you’re doing matrix multiplication).
Using this approach, the process looks like this:
⃗⃗I ′ =
⎛
⎝
0.866
−0.25
4.33
0
0.866
0.5
−0.5
−0.433
0.75
⎞
⎠
⎛
⎝
20ma2
0
0
0
20ma2
0
0
0
8ma2
⎞
⎠
×
⎛
⎝
0.866
−0.25
4.33
0
0.866
0.5
−0.5
−0.433
0.75
⎞
⎠
−1
=
⎛
⎝
17.8ma2
2.6ma2
3.9ma2
2.6ma2
17ma2
−4.5ma2
3.9ma2
−4.5ma2
13.3ma2
⎞
⎠,
which is identical to the result obtained by inserting the rotated coordinates
into the inertia tensor.
If you’ve studied matrix algebra, you may be wondering about the possibil-
ity of ﬁnding the principal axes and principal moments by manipulating the
matrix representing the inertia tensor into a diagonal form. That is certainly
possible, and you can read about doing that using eigenvectors and eigenvalues
on this book’s website.
And if you’re able by visual inspection to determine the angles of rotation
needed to align the axes with the symmetries of the object, you can use the
similarity transform approach to diagonalize the inertia matrix. You can see
how that works by looking at the problems at the end of this chapter and the
on-line solutions.
6.2 The electromagnetic ﬁeld tensor
One of the deﬁning characteristics of our modern world is the availabil-
ity of broadband communication channels which allow near-instantaneous
transfer of information over great distances without the need for physical con-
nection. The technology used in this communication descends directly from
the equations synthesized by Scotsman James Clerk Maxwell in the 1860s,

## Page 184

172
Tensor applications
now called “Maxwell’s Equations.” In view of the impact of electromagnetic
telecommunications on our lives, it’s not surprising that in 2004 the readers of
Physics World voted Maxwell’s Equations to be the “greatest equations” ever
developed.
The four vector equations that have come to be called Maxwell’s Equations
are Gauss’s Law for electric ﬁelds, Gauss’s Law for magnetic ﬁelds, Faraday’s
Law, and the Ampere–Maxwell Law, each of which may be written in inte-
gral or differential form. The integral forms describe the behavior of electric
and magnetic ﬁelds over surfaces or around paths, while the differential forms
apply to speciﬁc locations. The differential forms are most relevant to the vec-
tor and tensor operations discussed in this book, involving the scalar product,
divergence, curl, and partial derivatives discussed in Chapter 2. They’re also
closely related to the subject of this section, the electromagnetic ﬁeld-strength
tensor.
The differential forms of Maxwell’s Equations are usually written as
Gauss’s Law for electric ﬁelds:
⃗∇◦⃗E = ρ
ϵ0
,
Gauss’s Law for magnetic ﬁelds:
⃗∇◦⃗B = 0,
Faraday’s Law:
⃗∇× ⃗E = −∂⃗B
∂t ,
Ampere–Maxwell Law:
⃗∇× ⃗B = μ0 ⃗J + μ0ϵ0
∂⃗E
∂t .
In order to understand the electromagnetic tensor, you may ﬁnd it helpful to
brieﬂy review the meaning of each of these equations.3
⃗∇◦⃗E = ρ
ϵ0
Gauss’s Law for electric ﬁelds states that the divergence ( ⃗∇◦) of the electric
ﬁeld ( ⃗E) at any location is proportional to the electric charge density (ρ) at
that location. That’s because electrostatic ﬁeld lines begin on positive charge
and end on negative charge (hence the ﬁeld lines tend to diverge away from
locations of positive charge and converge toward locations of negative charge).
⃗∇◦⃗B = 0
Gauss’s Law for magnetic ﬁelds tells you that the divergence ( ⃗∇◦) of the
magnetic ﬁeld ( ⃗B) at any location must be zero. This is true because there
is apparently no isolated “magnetic charge” in the universe, so magnetic ﬁeld
lines neither diverge nor converge.
3 Complete descriptions may be found in any introductory electromagnetics text.

## Page 185

6.2 The electromagnetic ﬁeld tensor
173
⃗∇× ⃗E = −∂⃗B
∂t
Faraday’s Law indicates that the curl ( ⃗∇×) of the electric ﬁeld ( ⃗E) at any loca-
tion is equal to the negative of the time rate of change of the magnetic ﬁeld at
that location. That’s because a changing magnetic ﬁeld produces a circulating
electric ﬁeld.
⃗∇× ⃗B = μ0 ⃗J +μ0ϵ0 ∂⃗E
∂t
Ampere’s Law, as modiﬁed by Maxwell, tells you that the curl ( ⃗∇×) of the
magnetic ﬁeld ( ⃗B) at any location is proportional to the electric current density
( ⃗J) plus the time rate of change of the electric ﬁeld at that location. This is
the case because a circulating magnetic ﬁeld is produced both by an electric
current and by a changing electric ﬁeld.
Note that Maxwell’s Equations relate the spatial behavior of ﬁelds to the
sources of those ﬁelds. Those sources are electric charge (with density ρ)
appearing in Gauss’s Law for electric ﬁelds, electric current (with density ⃗J)
appearing in the Ampere–Maxwell Law, changing magnetic ﬁeld (with time
derivative ∂⃗B
∂t ) appearing in Faraday’s Law, and changing electric ﬁeld (with
time derivative ∂⃗E
∂t ) appearing in the Ampere–Maxwell Law.
One additional equation is needed to fully characterize electromagnetic
interactions. That equation is called the “continuity equation,” usually written
like this:
∂ρ
∂t = −⃗∇◦⃗J,
where ρ is the density of electric charge and ⃗J is the current density.
The continuity equation tells you that the time rate of change of the density
of electric charge ( ∂ρ
∂t ) equals the negative of the divergence of the electric
current density ( ⃗∇◦⃗J). That’s because negative divergence means convergence,
and if the convergence of the current density ⃗J is positive at a point, then more
positive charge must be arriving at that location than is being carried away. If
that’s happening, then the density of positive charge at that point must increase
(meaning that ∂ρ
∂t will be positive in this case).
As valuable as Maxwell’s Equations are individually, the real power of these
equations is realized by combining them together to produce the wave equa-
tion. Taking the curl of both sides of Faraday’s Law and inserting the curl of ⃗B
from the Ampere–Maxwell Law results in the equation
∇2 ⃗E = μ0ϵ0
∂2 ⃗E
∂t2 ,
(6.10)

## Page 186

174
Tensor applications
where ∇2() = ⃗∇◦⃗∇() is the vector form of the Laplacian operator.4 This
equation applies to regions in which the charge density (ρ) and the current
density ( ⃗J) are both zero.
You can ﬁnd a similar equation for the magnetic ﬁeld by taking the curl of
both sides of the Ampere–Maxwell Law and then inserting the curl of ⃗E from
Faraday’s Law. This gives
∇2 ⃗B = μ0ϵ0
∂2 ⃗B
∂t2 .
(6.11)
It’s instructive to compare Eqs. 6.10 and 6.11 to the general equation for a
propagating wave:
∇2 ⃗A = 1
v2
∂2 ⃗A
∂t2 ,
(6.12)
where v is the speed of propagation of the wave. Note the 1/v2 term, which
leads to the conclusion that the velocity of an electromagnetic wave depends
only on the electric permittivity (ϵ0) and magnetic permeability (μ0) of free
space (speciﬁcally, μ0ϵ0 = 1/v2, or v = 1/√μoϵ0 = 3 × 108 m/s). Most
importantly, that velocity is completely independent of the motion of the
observer. It was this feature of electromagnetic waves that put Albert Einstein
onto the path that eventually led to the Theory of Special Relativity.
To arrive at the Theory of Special Relativity, Einstein held fast to two
postulates. Those postulates are:
1) The laws of physics must be the same in all inertial (that is, non-
accelerating) frames of reference.
2) The speed of light in a vacuum is constant and does not depend on the
motion of the source or observer.
Steadfast faithfulness to these postulates even in the face of counter-intuitive
conclusions allowed Einstein to see that distances in space and intervals of time
are not absolute but depend on the relative motion of the observer. Additionally,
space and time are not separate but are linked together into four-dimensional
spacetime, and it is the four-dimensional spacetime interval that is invariant
across all inertial reference frames.
To understand Einstein’s approach, consider the two Cartesian reference
frames shown in Figure 6.5. As indicated by the arrow in the ﬁgure, the primed
reference frame is moving with velocity ⃗v in the positive x-direction. Using the
traditional Galilean approach, the coordinate (x, y, and z) and time (t) values
4 If you’d like to see the details of the derivation of the electromagnetic-wave equation, you’ll
ﬁnd them in the on-line solutions to the problems at the end of this chapter.

## Page 187

6.2 The electromagnetic ﬁeld tensor
175
x
y
z
x′
y′
z′
v
Figure 6.5 Primed reference frame moving along x-axis with velocity ⃗v.
for a point measured in both the unprimed and primed coordinate systems are
related by these equations:
t′ = t,
x′ = x −vt,
y′ = y,
z′ = z,
since the primed frame is moving only in the x-direction.5
Einstein realized that the second postulate of Special Relativity (the con-
stancy of the speed of light) is inconsistent with the Galilean transform shown
above, and that consistent results are obtained only when a different transform
is used between the unprimed and primed coordinate systems. That transform
must hold the space–time interval invariant across inertial reference frames.
But what exactly is the space–time interval (that is, how should you combine
the space terms and the time term)?
The answer to that question can be understood by imagining a pulse of light
radiating spherically outward from a certain location. Calling the speed of
light c, an observer in the unprimed coordinate system will ﬁnd the square
of the distance covered by a wavefront of the light wave in time t to be
5 These equations assume that the origins of the two coordinate systems coincide at time t = 0.

## Page 188

176
Tensor applications
x2 + y2 + z2 = ct2. Likewise, an observer in the primed coordinate system
will write this as x′2 + y′2 + z′2 = ct′2. But by the second postulate of special
relativity, the speed of light must be the same for all observers. So
ct2 −x2 −y2 −z2 = ct′2 −x′2 −y′2 −z′2,
which indicates that the sign of the time term must be opposite to the sign of
the spatial terms if the speed of light is to be the same for all observers. Of
course, the negative sign could equally well be attached to the time term (as
long as the spatial terms were made positive), and you’ll ﬁnd some texts using
that convention.
The combination of one time and three spatial coordinates into a single
“four-vector” is best expressed using index notation:
x0 = ct,
x1 = x,
x2 = y,
x3 = z,
in which the speed of light (c) is used in the time term to ensure that all four
coordinates have dimensions of length.
Using this notation, the space–time interval (ds) can be written as
(ds)2 = (dx0)2 −(dx1)2 −(dx2)2 −(dx3)2.
This interval is the space–time equivalent of distance (ds2 = dx2 +dy2 +dz2)
in three-dimensional space.
Transformations that preserve the invariance of the space–time interval
across inertial reference frames are called “Lorentz transforms” after the Dutch
physicist Hendrik Lorentz. For motion in +x-direction with speed v, the
Lorentz transformation is
x′
0 = γ (x0 −βx1),
x′
1 = γ (x1 −βx0),
x′
2 = x2,
x′
3 = x3,
where
β = |v|
c ,
and

## Page 189

6.2 The electromagnetic ﬁeld tensor
177
γ =
1

1 −v2
c2
=
1
	
1 −β2 .
This form of the space–time interval can be written using the metric tensor
gαβ:
(ds)2 = gαβdxαdxβ,
in which the tensor gαβ corresponds to the Minkowski metric for ﬂat space-
time. In matrix form, that metric is
⃗⃗g =
⎛
⎜⎜⎝
1
0
0
0
0
−1
0
0
0
0
−1
0
0
0
0
−1
⎞
⎟⎟⎠.
As you may recall if you’ve studied modern physics, the invariance of
the space–time interval under Lorentz tranformation leads to several interest-
ing results for observers in different inertial reference frames. Those results
include:
(1) Length contraction: An observer in a given reference frame measures
lengths in a moving reference frame to be contracted along the direction
of motion.
(2) Time dilation: An observer in a given reference frame measures time in a
moving reference frame to run more slowly.
(3) Relativity of simultaneity: An observer in a given reference frame will
not agree with an observer in a moving reference frame as to whether two
events are simultaneous.
Writing physical laws in a form that clearly ﬁts within the framework of
Special Relativity has several beneﬁts: such “manifestly covariant” laws have
the same form in all inertial reference frames, and the quantities involved
transform between reference frames in predictable ways. Any covariant the-
ory of electromagnetism must incorporate the experimental fact that quantity
of charge is a scalar (invariant between reference frames), and that Maxwell’s
Equations and the Lorentz force law are true in all inertial reference frames.
This requires a tensor version of the electromagnetic ﬁeld equations and a
four-vector version of the Lorentz force law, which can be accomplished by
expressing the electric charge density ρ and current density ⃗J as a four-vector
called the “four-current”:
⃗J = (cρ, Jx, Jy, Jz).

## Page 190

178
Tensor applications
With the four-current in hand, a tensor version of Maxwell’s Equations
can be achieved by combining the components of the electric and magnetic
ﬁeld into an “electromagnetic ﬁeld tensor.” The matrix representing the
contravariant version of this tensor is6
Fαβ =
⎛
⎜⎜⎝
0
−Ex/c
−Ey/c
−Ez/c
Ex/c
0
−Bz
By
Ey/c
Bz
0
−Bx
Ez/c
−By
Bx
0
⎞
⎟⎟⎠.
(6.13)
The covariant version of this tensor can be found by lowering the indices
using the metric tensor. The result is
Fαβ =
⎛
⎜⎜⎝
0
Ex/c
Ey/c
Ez/c
−Ex/c
0
−Bz
By
−Ey/c
Bz
0
−Bx
−Ez/c
−By
Bx
0
⎞
⎟⎟⎠.
(6.14)
Another useful tensor is the dual contravariant electromagnetic ﬁeld tensor
Fαβ =
⎛
⎜⎜⎝
0
−Bx
−By
−Bz
Bx
0
Ez/c
−Ey/c
By
−Ez/c
0
Ex/c
Bz
Ey/c
−Ex/c
0
⎞
⎟⎟⎠.
(6.15)
One beneﬁt of these tensor expressions is that all of Maxwell’s Equations
may now be expressed using just two tensor equations. Those two equations
are:
∂Fαβ
∂xα = μ0J β,
(6.16)
and
∂Fαβ
∂xα = 0.
(6.17)
Where are Maxwell’s Equations in these expressions? Well, to ﬁnd Gauss’s
Law for electric ﬁelds, take β = 0 in Eq. 6.16:
∂Fα0
∂xα = μ0J 0.
6 You should be aware that there are almost as many versions of this matrix as there are authors;
this book’s website has an explanation of the reasons for the differences between the versions
found in several popular texts.

## Page 191

6.2 The electromagnetic ﬁeld tensor
179
Inserting the values from the electromagnetic ﬁeld-strength tensor of Eq. 6.13
and summing over the dummy index α gives
∂(0)
∂(ct) + ∂(Ex/c)
∂x
+ ∂(Ey/c)
∂y
+ ∂(Ez/c)
∂z
= μ0(cρ).
Thus
∂(Ex)
∂x
+ ∂(Ey)
∂y
+ ∂(Ez)
∂z
= μ0(c2ρ),
and, since c2 = 1/(ϵ0μ0),
∂(Ex)
∂x
+ ∂(Ey)
∂y
+ ∂(Ez)
∂z
=
μ0
ϵ0μ0
ρ,
or
⃗∇◦⃗E = ρ
ϵ0
,
which is Gauss’s Law for electric ﬁelds.
To get the Ampere–Maxwell Law, look at the equations that result from
setting β equal to 1, 2, and 3 in Eq. 6.16:
∂Fα1
∂xα = μ0J 1,
∂Fα2
∂xα = μ0J 2,
∂Fα3
∂xα = μ0J 3.
As above, just insert the values from the electromagnetic ﬁeld-strength tensor
of Eq. 6.13 and sum over the dummy index α:
∂(−Ex/c)
∂(ct)
+ ∂(0)
∂x + ∂(Bz)
∂y
+ ∂(−By)
∂z
= μ0(Jx),
∂(−Ey/c)
∂(ct)
+ ∂(−Bz)
∂x
+ ∂(0)
∂y + ∂(Bx)
∂z
= μ0(Jy),
∂(−Ez/c)
∂(ct)
+ ∂(By)
∂x
+ ∂(−Bx)
∂y
+ ∂(0)
∂z
= μ0(Jz).
Hence
∂(Bz)
∂y
−∂(By)
∂z
= μ0(Jx) + 1
c2
∂(Ex)
∂t
,
∂(Bx)
∂z
−∂(Bz)
∂x
= μ0(Jy) + 1
c2
∂(Ey)
∂t
,
∂(By)
∂x
−∂(Bx)
∂y
= μ0(Jz) + 1
c2
∂(Ez)
∂t
.

## Page 192

180
Tensor applications
Recognizing the partial derivatives of the magnetic ﬁeld as the components of
the curl of ⃗B, this is
⃗∇× ⃗B = μ0 ⃗J + μ0ϵ0
∂⃗E
∂t ,
the Ampere–Maxwell Law.
The other two Maxwell Equations (Gauss’s Law for magnetic ﬁelds and
Faraday’s Law) may be obtained in a similar fashion using the dual electro-
magnetic ﬁeld-strength tensor (Eq. 6.15). For example, to ﬁnd Gauss’s Law
for magnetic ﬁelds, take β = 0 in Eq. 6.17:
∂Fα0
∂xα = 0.
Inserting the values from the dual electromagnetic ﬁeld-strength tensor of
Eq. 6.15 and summing over the dummy index α gives
∂(0)
∂(ct) + ∂(Bx)
∂x
+ ∂(By)
∂y
+ ∂(Bz)
∂z
= 0,
which is
⃗∇◦⃗B = 0,
Gauss’s Law for magnetic ﬁelds.
And to get Faraday’s Law, look at the equations that result from setting β
equal to 1, 2, and 3 in Eq. 6.17:
∂Fα1
∂xα = 0,
∂Fα2
∂xα = 0,
∂Fα3
∂xα = 0.
As before, just insert the values from the dual electromagnetic ﬁeld-strength
tensor of Eq. 6.15 and sum over the dummy index α:
∂(−Bx)
∂(ct)
+ ∂(0)
∂x + ∂(−Ez/c)
∂y
+ ∂(Ey/c)
∂z
= 0,
∂(−By)
∂(ct)
+ ∂(Ez/c)
∂x
+ ∂(0)
∂y + ∂(−Ex/c)
∂z
= 0,
∂(−Bz)
∂(ct)
+ ∂(−Ey/c)
∂x
+ ∂(Ex/c)
∂y
+ ∂(0)
∂z
= 0.

## Page 193

6.2 The electromagnetic ﬁeld tensor
181
So
∂(Ey)
∂z
−∂(Ez)
∂y
= ∂(Bx)
∂t
,
∂(Ez)
∂x
−∂(Ex)
∂z
= ∂(By)
∂t
,
∂(Ex)
∂y
−∂(Ey)
∂x
= ∂(Bz)
∂t
.
Recognizing the partial derivatives of the electric ﬁeld as the components of
the curl of ⃗E, this is Faraday’s Law:
⃗∇× ⃗E = −∂⃗B
∂t .
So the use of tensors allows you to write Maxwell’s Equations in a simpler
form. But the real power of tensors is to help you understand the behavior
of electric and magnetic ﬁelds when viewed from different reference frames.
Speciﬁcally, by transforming to a moving reference frame, it becomes clear
that electric and magnetic ﬁelds depend on the state of motion of the observer.
To see how that comes about, imagine an observer in a reference frame
moving along the positive x-axis at a constant speed v. You can investi-
gate the behavior of electric and magnetic ﬁelds as seen by this observer by
transforming the electromagnetic ﬁeld tensor to the observer’s reference frame.
Recall the Lorentz transform matrix for motion along the x-axis with
speed v:
A =
⎛
⎜⎜⎝
γ
−γβ
0
0
−γβ
γ
0
0
0
0
1
0
0
0
0
1
⎞
⎟⎟⎠.
(6.18)
So to transform to the primed coordinate system, use
⃗⃗F′ = A ⃗⃗F AT ,
which is
⃗⃗F′ =
⎛
⎜⎜⎝
γ
−γβ
0
0
−γβ
γ
0
0
0
0
1
0
0
0
0
1
⎞
⎟⎟⎠
⎛
⎜⎜⎝
0
−Ex/c
−Ey/c
−Ez/c
Ex/c
0
−Bz
By
Ey/c
Bz
0
−Bx
Ez/c
−By
Bx
0
⎞
⎟⎟⎠
×
⎛
⎜⎜⎝
γ
−γβ
0
0
−γβ
γ
0
0
0
0
1
0
0
0
0
1
⎞
⎟⎟⎠.

## Page 194

182
Tensor applications
Multiplying the center matrix by the right matrix gives
⎛
⎜⎜⎝
(−Ex/c)(−γβ)
(−Ex/c)(γ )
−Ey/c −Ez/c
(Ex/c)(γ )
(Ex/c)(−γβ)
−Bz
By
(Ey/c)(γ ) + (Bz)(−γβ)
(Ey/c)(−γβ) + (Bz)(γ )
0
−Bx
(Ez/c)(γ ) + (−By)(−γβ) (Ez/c)(−γβ) + (By)(−γ )
Bx
0
⎞
⎟⎟⎠,
which, when multiplied by the left array, gives
⎛
⎜⎜⎝
(Ex/c)γ 2β −(Ex/c)γ 2β
−(Ex/c)γ 2 + (Ex/c)γ 2β2
(Ex/c)γ 2 −(Ex/c)γ 2β2
0
(Ey/c)γ −(Bz)γβ
−(Ey/c)γβ + (Bz)γ
(Ez/c)γ + (By)γβ
−(Ez/c)γβ −(By)γ
−(Ey/c)γ + (Bz)γβ
−(Ez/c)γ −(By)γβ
(Ey/c)γβ −(Bz)γ
(Ez/c)γβ + (By)γ
0
−Bx
Bx
0
⎞
⎟⎟⎠.
Thus
⃗⃗F′ =
⎛
⎜⎜⎝
0
−Ex/c
Ex/c
0
γ (Ey/c −βBz)
γ (Bz −βEy/c)
γ (Ez/c + βBy)
−γ (By + βEz/c)
γ (Ey/c −βBz)
−γ (Ez/c + βBy)
−γ (Bz −βEy/c)
γ (By + βEz/c)
0
−Bx
Bx
0
⎞
⎟⎟⎠.
Comparing this to Eq. 6.13, the components of the electric ﬁeld in the new
(primed) coordinate system can be related to the components of the electric
ﬁeld in the original (unprimed) coordinate system by
E′
x = Ex,
E′
y = cγ (Ey/c −βBz),
E′
z = cγ (Ez/c + βBy),
(6.19)
and the magnetic ﬁeld components in the new (primed) system are
B′
x = Bx,
B′
y = γ (By + βEz/c),
B′
z = γ (Bz −βEy/c).
(6.20)

## Page 195

6.3 The Riemann curvature tensor
183
This is a profound result, since it indicates that the existence of electric and
magnetic ﬁelds depends on the motion of the observer.
To understand the implications of these results, consider the case in which
Ex = Ey = Ez = 0 but one or more components of ⃗B are non-zero (this
occurs, for example, when a long, straight wire carries a steady electric cur-
rent). This means that an observer in the unprimed coordinate system sees
a magnetic ﬁeld but no electric ﬁeld. However, transforming to the primed
coordinate system, Eqs. 6.19 and 6.20 tell you that an observer in the primed
coordinate system sees both electric and magnetic ﬁelds (since in this case
E′
y = −cγβBz and E′
z = cγβBy). So does the magnetic ﬁeld exist or not?
The answer depends on the motion of the observer.
Now consider a case in which Bx = By = Bz = 0 but one or more
components of ⃗E are non-zero in the unprimed system (for example, an elec-
tric charge at rest in the unprimed system). For this case, an observer in the
primed system does see a magnetic ﬁeld with components B′
y = γβEz/c and
B′
z = −γβEy/c (this makes sense, since the observer in the primed system
sees a moving electric charge, which is an electric current, and electric currents
produce magnetic ﬁelds). Cases such as these explain the reasoning behind the
statement that electric and magnetic ﬁelds “have no independent existence.”
The problems at the end of this chapter will give you an idea of the relative
magnitudes of ﬁelds seen by an observer at rest and a second observer moving
at a signiﬁcant fraction of the speed of light.
6.3 The Riemann curvature tensor
In the decade after publishing his Theory of Special Relativity in 1905, Albert
Einstein turned his attention to what he called a “deﬁciency” in classical
mechanics: the lack of an explanation for the precise equality of inertial and
gravitational mass. An object’s inertial mass determines its resistance to accel-
eration, and its gravitational mass determines its response to a gravitational
ﬁeld. The equality of these differently deﬁned masses cannot be explained
by classical mechanics, and Einstein’s scientiﬁc instincts told him that the
resolution of this deﬁciency could be achieved by “an extension of the prin-
ciple of relativity to spaces of reference which are not in uniform motion
relative to one another.”7 He applied the word “General” to this extension of
his theory of relativity because this new theory would not be restricted to the
non-accelerating reference frames of Special Relativity.
7 A. Einstein, The Meaning of Relativity.

## Page 196

184
Tensor applications
Early in his work on the General Theory, Einstein constructed a Gedanken-
experiment (that is, a mental exercise) in which he imagined a group of objects
with different mass far away from the Earth and from all other masses – you
can think of this as a bunch of rocks far out in space. The behavior of these
objects is observed from two reference systems, one of which is called sys-
tem K and is “inertial” or non-accelerating with respect to the rocks. The other
system, called system K′, is in uniform acceleration with respect to the ﬁrst.
For an observer in the K′ system, the objects all accelerate in the same direc-
tion (opposite to the direction of the acceleration of the K′ system) and at
the same rate (equal to the rate of acceleration of the K′ system). Seeing all
objects accelerating in the same direction and at the same rate, that observer
would be entirely justiﬁed in concluding that the acceleration of the objects
is produced by an external gravitational ﬁeld and that the K′ system is at rest.
Einstein realized that both the K and the K′ systems are valid frames of refer-
ence, and he termed the complete equivalence of such systems the “principle
of equivalence.”
Einstein’s next step was to overlay the z′-axis of K′ system with the z-axis
of the K system and then to allow the K′ system to rotate about the z′-axis
with uniform angular speed (recall that a rotating object experiences centripetal
acceleration, so rotation makes K′ an accelerated system). If system K′ were
not rotating, the size of objects and rate of time ﬂow measured in the K and K′
systems would be the same. But when system K′ is rotating, objects at rest in
K′ will be moving when measured in the K system and will therefore experi-
ence length contraction and time dilation, and the amount of contraction and
dilation will depend on the location of the objects (since objects farther from
the rotation axis will have higher velocity). Since the principle of equivalence
demands that an accelerated system and a system at rest in a gravitational ﬁeld
are equivalent, Einstein was forced to conclude that length contraction and
time dilation could also be produced by gravity, or as he put it “the gravita-
tional ﬁeld inﬂuences and even determines the metrical laws of the space–time
continuum.”
Those metrical laws are expressed using tensors, so the General Theory
of Relativity relies on tensor formulation of physical laws and on concepts
described in earlier chapters, such as the metric tensor, Christoffel symbols,
and covariant derivatives. The most important tensor in General Relativity is
the Riemann curvature tensor, sometimes called the Riemann–Christoffel ten-
sor after the nineteenth-century German mathematicians Bernhard Riemann
and Elwin Bruno Christoffel. The importance of this tensor stems from the
fact that non-zero components are the hallmark of curvature; the vanishing of

## Page 197

6.3 The Riemann curvature tensor
185
the Riemann tensor is both a necessary and a sufﬁcient condition for Euclidean
(ﬂat) space.
Most texts use one of two ways to derive the Riemann curvature tensor:
parallel transport or the commutator of the covariant derivative. To understand
the parallel-transport approach, you should ﬁrst understand that “parallel trans-
port” refers to a method of moving a vector around a space while keeping the
length and direction of the vector the same. In Cartesian ﬂat space, making
sure the vector’s magnitude and direction don’t change is straightforward –
just move the vector around without allowing the x-, y-, or -z components to
change. If the components don’t change, then the length and the direction of
the vector don’t change, and this satisﬁes the requirements of parallel transport.
In curved spaced, the situation is more complex. For one thing, “pointing
in the same direction” becomes more difﬁcult to deﬁne. Consider the two-
dimensional space that is the surface of the Earth (and pretend for the moment
that it’s perfectly smooth). Imagine a vector that is initially at the equator (say
a bit north of Quito, Ecuador) and is pointing due north, directly along the
meridian line. Now imagine transporting that vector toward the north pole,
all the while making sure it remains pointed exactly along the meridian line.
Remember, the entire space is the surface of the Earth, so the vector must
remain tangent to the surface (that is, locally horizontal) as you move it. If you
continue moving your vector along the meridian line and pass over the North
Pole and then “down” the other side of the Earth, you will eventually reach the
equator again somewhere near the middle of Indonesia. Your vector will still
be pointing along the meridian, but now it will be pointing south. So although
you’ve kept your vector pointing “in the same direction” (that is, along the
meridian) over the entire trip, it’s gone from pointing north to pointing south.
Now imagine making another trip, also starting with a north-pointing vector
at the equator near Quito, but this time moving along the equator instead of
over the North Pole. Once again, as you move you make sure that your vector
continues to point north (along the local meridian). After a long journey, you
arrive in the middle of Indonesia, but this time you ﬁnd that your vector is
pointing north. Hence the direction of the vector at the end of the journey
depends on the path taken, even though you used parallel transport in each
case. And whenever the result of parallel transport is a change in the direction
of a vector, you can be sure you’re dealing with a curved space.
This raises a larger issue: it’s not possible to add, subtract, multiply, or in
any way compare vectors at different locations – you have to transport one of
the vectors to the location of the other before you can perform such operations.
That’s no problem in ﬂat space, because you can parallel-transport a vector to
any other location simply by keeping its coefﬁcients constant (ensuring that the

## Page 198

186
Tensor applications
vector’s length is constant and that it remains pointed in the same direction).
But while “pointed in the same direction” is easily deﬁned at different locations
in ﬂat space, you’ve just seen that this phrase is problematic in curved space.
Hence a more-general deﬁnition of parallel transport is required.
In that deﬁnition, “parallel transport” is deﬁned as transport for which the
covariant derivative is zero. Remember that the covariant derivative is the com-
bination of two terms, the ﬁrst of which is the usual partial derivative, and the
second of which involves a Christoffel symbol. As described in Section 5.7
in Chapter 5, the purpose of that second term is to account for changes in
the basis vectors. Holding the covariant derivative at zero while transporting a
vector around a small loop is one way to derive the Riemann tensor.8
The Riemann curvature tensor falls naturally out of the commutator of the
covariant derivative of a vector. In this usage, “commutator” refers to the dif-
ference that results from performing two operations ﬁrst in one order and then
in the reverse order. So if one operator is denoted by A and another operator
by B, the commutator is deﬁned as [AB] = AB−BA. Thus if the sequence of
the two operations has no impact on the result, the commutator has a value of
zero.
To get to the Riemann tensor, the operation of choice is covariant differenti-
ation. That’s because in a ﬂat space the order of covariant differentiation makes
no difference, so the commutator must yield zero. Any non-zero result of
applying the commutator to covariant differentiation can therefore be attributed
to the curvature of the space.
To begin this process, take the covariant derivative of vector Vα ﬁrst with
respect to xβ:
Vα;β = ∂Vα
∂xβ −σ
αβVσ.
(6.21)
Now call this result Vαβ and take another covariant derivative (this time with
respect to xγ ):
Vαβ;γ = ∂Vαβ
∂xγ −τ
αγ Vτβ −η
βγ Vαη.
(6.22)
Substituting the expression from Eq. 6.21 into this equation gives
Vαβ;γ =
∂2Vα
∂xγ ∂xβ −
∂σ
αβ
∂xγ Vσ −σ
αβ
∂Vσ
∂xγ
−τ
αγ
∂Vτ
∂xβ −σ
τβVσ

−η
βγ
∂Vα
∂xη −σ
αηVσ

.
(6.23)
8 You can ﬁnd the details in Schutz, A First Course in General Relativity, Cambridge University
Press, 2009.

## Page 199

6.3 The Riemann curvature tensor
187
It’s not easy to see the physical signiﬁcance in this expression, but remember
how you got here: ﬁrst by ﬁnding the incremental change in Vα as you take a
small step in the xβ-direction, and then ﬁnding the change in that quantity as
you take a small step in the xγ -direction. And now you’re going to compare the
result of these two operations with the result you get when you take the steps
in reverse order – from the same starting point, you’ll ﬁrst ﬁnd the incremental
change in Vα as you take a small step in the xγ -direction, after which you’ll
ﬁnd the change in that quantity as you take a small step in the xβ-direction.
To take the covariant derivatives in the opposite order, differentiate ﬁrst with
respect to xγ :
Vα;γ = ∂Vα
∂xγ −σ
αγ Vσ.
(6.24)
Call this result Vαγ and take another covariant derivative (this time with respect
to xβ):
Vαγ ;β = ∂Vαγ
∂xβ −τ
αβVτγ −η
γβVαη.
(6.25)
As before, you can substitute the expression from Eq. 6.24 into this equation
to get
Vαγ ;β =
∂2Vα
∂xβ∂xγ −
∂σ
αγ
∂xβ Vσ −σ
αγ
∂Vσ
∂xβ
−τ
αβ
∂Vτ
∂xγ −σ
τγ Vσ

−η
γβ
∂Vα
∂xη −σ
αηVσ

.
(6.26)
In ﬂat space, the order of covariant differentiation should make no differ-
ence, so Eq. 6.26 should be identical to Eq. 6.23. Any differences between
these equations can therefore be attributed to the curvature of the space.
Examining these two equations term by term, the ﬁrst terms are equal:
∂2Vα
∂xγ ∂xβ =
∂2Vα
∂xβ∂xγ ,
(these terms are equal because the order of normal partial derivatives does
not matter). Hence these terms cancel in the commutator. Now comparing the
second terms,
−
∂σ
αβ
∂xγ Vσ ̸= −
∂σ
αγ
∂xβ Vσ,
so these terms do not cancel one another. Comparing the third term of Eq. 6.23
to the fourth term of Eq. 6.26, they’re found to be equal:

## Page 200

188
Tensor applications
−σ
αβ
∂Vσ
∂xγ = −τ
αβ
∂Vτ
∂xγ ,
because the symbols used for dummy indices (σ and τ) are irrelevant. The
fourth term of Eq. 6.23 equals the third term of Eq. 6.26:
−τ
αγ
∂Vτ
∂xβ = −σ
αγ
∂Vσ
∂xβ ,
for the same reason. The ﬁfth terms are not equal:
τ
αγ σ
τβVσ ̸= τ
αβσ
τγ Vσ.
But the sixth terms are equal:
−η
βγ
∂Vα
∂xη = −η
γβ
∂Vα
∂xη ,
because Christoffel symbols are symmetric in their lower indices. The seventh
terms are equal for the same reason:
η
βγ σ
αηVσ = η
γβσ
αηVσ.
So when the commutator AB−BA is formed, most of the terms cancel out,
but the second and ﬁfth terms remain after subtraction. Those terms are
Vαβ;γ −Vαγ ;β = −
∂σ
αβ
∂xγ Vσ +
∂σ
αγ
∂xβ Vσ + τ
αγ σ
τβVσ −τ
αβσ
τγ Vσ
=

∂σ
αγ
∂xβ −
∂σ
αβ
∂xγ + τ
αγ σ
τβ −τ
αβσ
τγ

Vσ.
(6.27)
The terms within the parentheses deﬁne the Riemann curvature tensor:
Rσ
αβγ ≡
∂σ
αγ
∂xβ −
∂σ
αβ
∂xγ + τ
αγ σ
τβ −τ
αβσ
τγ .
(6.28)
If you’re wondering why the curvature tensor involves the derivative of
Christoffel symbols, consider this: in any space, you can always deﬁne a coor-
dinate system for which the Christoffel symbols are all zero at some point. But
unless the space is ﬂat, the Christoffel symbols will not be zero at all other
locations, which means that the partial derivatives of the Christoffel symbols
will not be zero. So a necessary and sufﬁcient condition for ﬂat space is that
Rσ
αβγ = 0.
(6.29)
Another tensor related to the Riemann curvature tensor is the Ricci ten-
sor, which you can ﬁnd by contracting the Riemann tensor along the σ and β
indices. In four dimensions, this is
Rαγ ≡Rσ
ασγ = R1
α1γ + R2
α2γ + R3
α3γ + R4
α4γ .
(6.30)

## Page 201

6.3 The Riemann curvature tensor
189
If you contract the Ricci tensor by raising one index and setting it equal to
the other, the result is the Ricci scalar. Again in four dimensions, this is
R ≡gαγ Rαγ = Rγ
γ = R1
1 + R2
2 + R3
3 + R4
4.
(6.31)
Finally, the tensor known as the “Einstein tensor” can be written as a
combination of the Ricci tensor, the Ricci scalar, and the metric:
Gαγ ≡Rαγ −1
2 Rgαγ .
(6.32)
This is the tensor that appears in Einstein’s ﬁeld equation for General
Relativity, often written as
Gμν + gμν = 8πG
c4 Tμν,
(6.33)
where Tμν is the energy-momentum tensor and  is the “cosmological con-
stant” introduced by Einstein to maintain a static Universe. It is this equation
that gives rise to the ﬁrst half of the concise statement of General Relativity:
“Matter tells spacetime how to curve, and spacetime tells matter how to move.”
To appreciate the full content of the Riemann tensor, consider a two-
dimensional space that is the surface of a sphere. The metric for such a
space is
ds2 = a2dθ2 + a2 sin2(θ)dφ2,
from which the components of the metric tensor may be found to be
gθθ = a2,
gθφ = gφθ = 0,
gφφ = a2 sin2(θ).
(6.34)
Inserting these values into the equation for Christoffel symbols gives
l
i j = 1
2gkl
∂gik
∂x j + ∂g jk
∂xi −∂gi j
∂xk

.
Even in two dimensions, writing out all the terms of the Christoffel symbols
can be something of a chore:
θ
θθ = 1
2

gθθ ∂gθθ
∂θ
+ gφθ ∂gθφ
∂θ
+ gθθ ∂gθθ
∂θ
+ gφθ ∂gθφ
∂θ
−gθθ ∂gθθ
∂θ
−gφθ ∂gθθ
∂φ

,
θ
θφ = 1
2

gθθ ∂gθθ
∂φ + gφθ ∂gθφ
∂φ
+ gθθ ∂gφθ
∂θ
+ gφθ ∂gφφ
∂θ
−gθθ ∂gθφ
∂θ
−gφθ ∂gθφ
∂φ

,
θ
φθ = 1
2

gθθ ∂gφθ
∂θ
+ gφθ ∂gφφ
∂θ
+ gθθ ∂gθθ
∂φ + gφθ ∂gθφ
∂φ
−gθθ ∂gφθ
∂θ
−gφθ ∂gφθ
∂φ

,
φ
θθ = 1
2

gθφ ∂gθθ
∂θ
+ gφφ ∂gθφ
∂θ
+ gθφ ∂gθθ
∂θ
+ gφφ ∂gθφ
∂θ
−gθφ ∂gθθ
∂θ
−gφφ ∂gθθ
∂φ

,

## Page 202

190
Tensor applications
φ
θφ = 1
2

gθφ ∂gθθ
∂φ + gφφ ∂gθφ
∂φ
+ gθφ ∂gφθ
∂θ
+ gφφ ∂gφφ
∂θ
−gθφ ∂gθφ
∂θ
−gφφ ∂gθφ
∂φ

,
φ
φθ = 1
2

gθφ ∂gφθ
∂θ
+ gφφ ∂gφφ
∂θ
+ gθφ ∂gθθ
∂φ + gφφ ∂gθφ
∂φ
−gθφ ∂gφθ
∂θ
−gφφ ∂gφθ
∂φ

,
θ
φφ = 1
2

gθθ ∂gφθ
∂φ
+ gφθ ∂gφφ
∂φ
+ gθθ ∂gφθ
∂φ
+ gφθ ∂gφφ
∂φ
−gθθ ∂gφφ
∂θ
−gφθ ∂gφφ
∂φ

,
φ
φφ = 1
2

gθφ ∂gφθ
∂φ
+ gφφ ∂gφφ
∂φ
+ gθφ ∂gφθ
∂φ
+ gφφ ∂gφφ
∂φ
−gθφ ∂gφφ
∂θ
−gφφ ∂gφφ
∂φ

.
But given the metric tensor components shown in Eq. 6.34, all the partial
derivatives except those involving ∂gφφ
∂θ
are zero, as are any terms involving
gθφ or gφθ. That leaves only three non-zero Christoffel symbols, which are
φ
θφ =
1
2

gφφ ∂gφφ
∂θ
=
1
2

1
a2 sin2(θ)
[2a2 sin(θ) cos(θ)] = cos(θ)
sin(θ) = cot(θ),
φ
φθ =
1
2

gφφ ∂gφφ
∂θ
= cot(θ),
θ
φφ =
1
2

−gθθ ∂gφφ
∂θ
= −
1
2
 1
a2 [2a2 sin(θ) cos(θ)] = −sin(θ) cos(θ).
With the Christoffel symbols for the spherical surface in hand, the components
of the Riemann curvature tensor may be found using
Rσ
αβγ ≡
∂σ
αγ
∂xβ −
∂σ
αβ
∂xγ + τ
αγ σ
τβ −τ
αβσ
τγ .
As in most tensor equations, the full content of this tensor can only be appre-
ciated by writing out the components. Not only must you allow each of the
indices σ, α, β, and γ to represent both θ and φ, you must also allow the
dummy index τ to represent both θ and φ and then sum those terms. Hence
in two-dimensional space, the last two terms of the Riemann tensor equation
(those involving the products of the Christoffel symbols) become four terms,
making a total of six terms for each set of indices. The ﬁrst eight components
of the Riemann tensor can be found by setting σ equal to θ and letting the other
indices represent both θ and φ:
Rθ
θθθ = ∂θ
θθ
∂θ
−∂θ
θθ
∂θ
+ θ
θθθ
θθ + φ
θθθ
φθ −θ
θθθ
θθ −φ
θθθ
φθ,
Rθ
θθφ =
∂θ
θφ
∂θ
−∂θ
θθ
∂φ
+ θ
θφθ
θθ + φ
θφθ
φθ −θ
θθθ
θφ −φ
θθθ
φφ,

## Page 203

6.3 The Riemann curvature tensor
191
Rθ
θφθ = ∂θ
θθ
∂φ
−
∂θ
θφ
∂θ
+ θ
θθθ
θφ + φ
θθθ
φφ −θ
θφθ
θθ −φ
θφθ
φθ,
Rθ
φθθ =
∂θ
φθ
∂θ
−
∂θ
φθ
∂φ
+ θ
φθθ
θθ + φ
φθθ
φθ −θ
φθθ
θθ −φ
φθθ
φθ,
Rθ
θφφ =
∂θ
θφ
∂φ
−
∂θ
θφ
∂φ
+ θ
θφθ
θφ + φ
θφθ
φφ −θ
θφθ
θφ −φ
θφθ
φφ,
Rθ
φθφ =
∂θ
φφ
∂θ
−
∂θ
φθ
∂φ
+ θ
φφθ
θθ + φ
φφθ
φθ −θ
φθθ
θφ −φ
φθθ
φφ,
Rθ
φφθ =
∂θ
φθ
∂φ
−
∂θ
φφ
∂θ
+ θ
φθθ
θφ + φ
φθθ
φφ −θ
φφθ
θθ −φ
φφθ
φθ,
Rθ
φφφ =
∂θ
φφ
∂φ
−
∂θ
φφ
∂φ
+ θ
φφθ
θφ + φ
φφθ
φφ −θ
φφθ
θφ −φ
φφθ
φφ.
Inserting the Christoffel symbols found above, you can see that the non-zero
components are
Rθ
φθφ =
∂θ
φφ
∂θ
−φ
φθθ
φφ,
Rθ
φφθ = −
∂θ
φφ
∂θ
+ φ
φθθ
φφ.
And since
∂θ
φφ
∂θ
= sin2(θ) −cos2(θ),
and
φ
φθθ
φφ = −cos2(θ),
this means the surviving terms from the σ = θ group are
Rθ
φθφ = [sin2(θ) −cos2(θ)] −[−cos2(θ)] = sin2(θ),
Rθ
φφθ = −[sin2(θ) −cos2(θ)] + [−cos2(θ)] = −sin2(θ).
Now allowing σ to equal φ, the other eight terms are
Rφ
θθθ = ∂φ
θθ
∂θ
−∂φ
θθ
∂θ
+ θ
θθφ
θθ + φ
θθφ
φθ −θ
θθφ
θθ −φ
θθφ
φθ,
Rφ
θθφ =
∂φ
θφ
∂θ
−∂φ
θθ
∂φ
+ θ
θφφ
θθ + φ
θφφ
φθ −θ
θθφ
θφ −φ
θθφ
φφ,
Rφ
θφθ = ∂φ
θθ
∂φ
−
∂φ
θφ
∂θ
+ θ
θθφ
θφ + φ
θθφ
φφ −θ
θφφ
θθ −φ
θφφ
φθ,

## Page 204

192
Tensor applications
Rφ
φθθ =
∂φ
φθ
∂θ
−
∂φ
φθ
∂θ
+ θ
φθφ
θθ + φ
φθφ
φθ −θ
φθφ
θθ −φ
φθφ
φθ,
Rφ
θφφ =
∂φ
θφ
∂φ
−
∂φ
θφ
∂φ
+ θ
θφφ
θφ + φ
θφφ
φφ −θ
φθφ
θφ −φ
θφφ
φφ,
Rφ
φθφ =
∂φ
φφ
∂θ
−
∂φ
φθ
∂φ
+ θ
φφφ
θθ + φ
φφφ
φθ −θ
φθφ
θφ −φ
φθφ
φφ,
Rφ
φφθ =
∂φ
φθ
∂φ
−
∂φ
φφ
∂θ
+ θ
φθφ
θφ + φ
φθφ
φφ −θ
φφφ
θθ −φ
φφφ
φθ,
Rφ
φφφ =
∂φ
φφ
∂φ
−
∂φ
φφ
∂φ
+ θ
φφφ
θφ + φ
φφφ
φφ −θ
φφφ
θφ −φ
φφφ
φφ.
Again inserting the Christoffel symbols, the non-zero terms are found to be
Rφ
θθφ =
∂φ
θφ
∂θ
+ φ
θφφ
φθ,
Rφ
θφθ = −
∂φ
θφ
∂θ
−φ
θφφ
φθ.
And since
∂φ
θφ
∂θ
= −sin(θ)
sin(θ) −cos2(θ)
sin2(θ)
= −[1 + cot2(θ)],
and
φ
θφφ
φθ = cot2(θ),
the surviving terms are
Rφ
θθφ = −[1 + cot2(θ)] + cot2(θ) = −1,
Rφ
θφθ = [1 + cot2(θ)] −cot2(θ) = 1.
As expected, a two-dimensional space with the metric of a sphere (ds2 =
a2dθ2 + a2 sin2(θ)dφ2) has non-zero components of the Riemann curvature
tensor, conﬁrming that this space is non-Euclidean.
You can see how to use these results to ﬁnd the Ricci tensor and the Ricci
scalar in the on-line solutions to the problems at the end of this chapter.
6.4 Chapter 6 problems
6.1 Find the inertia tensor for a cubical arrangement of eight identical masses
with the origin of coordinates at one of the corners and the coordinate
axes along the edges of the cube.

## Page 205

6.4 Chapter 6 problems
193
6.2 How would the moment of inertia tensor of Problem 6.1 change if one of
the eight masses is removed?
6.3 Find the moment of inertia tensor for the arrangement of masses of Prob-
lem 6.2 if the coordinate system is rotated by 20 degrees about one of
the coordinate axes (do this by ﬁnding the locations of the masses in the
rotated coordinate system).
6.4 Use the similarity-transform approach to verify the moment of inertia
tensor you found in Problem 6.3.
6.5 Show how the vector wave equation results from taking the curl of both
sides of Faraday’s Law and inserting the curl of the magnetic ﬁeld from
the Ampere–Maxwell Law.
6.6 If an observer in one coordinate system measures an electric ﬁeld of
5 volts per meter in the z-direction and zero magnetic ﬁeld, what electric
and magnetic ﬁelds would be measured by a second observer moving at
1/4 the speed of light along the x-axis?
6.7 If an observer in one coordinate system measures a magnetic ﬁeld of 1.5
tesla in the z-direction and zero electric ﬁeld, what electric and magnetic
ﬁelds would be measured by a second observer moving at 1/4 the speed
of light along the x-axis?
6.8 Show that ⃗E ◦⃗B is invariant under Lorentz transformation.
6.9 The differential line element in 2-D Euclidean space may be expressed
in polar coordinates as ds2 = dr2 + r2dθ2. Show that the Riemann
curvature tensor equals zero in this case, as it must for any ﬂat space.
6.10 Find the Ricci tensor and scalar for the 2-sphere of Section 6.3.

## Page 206

Further reading
Arfken, G. and Weber, H., Mathematical Methods for Physicists, Elsevier Academic
Press 2005.
Boas, M., Mathematical Methods in the Physical Sciences, John Wiley and Sons 2006.
Borisenko, A. and Tarapov, I., Vector and Tensor Analysis, Dover Press 1979.
Carroll, S., Spacetime and Geometry: An Introduction to General Relativity, Benjamin-
Cummings 2003.
Einstein, A., The Meaning of Relativity, Princeton University Press 2004.
Grifﬁths, D., Introduction to Electrodynamics, Benjamin-Cummings 1999.
Jackson, J., Classical Electrodynamics, John Wiley and Sons 1999.
Lieber, L., The Einstein Theory of Relativity, Paul Dry Books 2008.
Matthews, P., Vector Calculus, Springer-Verlag 1998.
McMahon, D., Relativity Demystiﬁed, McGraw-Hill 2006.
Morse, P. and Feshbach, H., Methods of Theoretical Physics, McGraw-Hill 1953.
Schutz, B., A First Course in General Relativity, Cambridge University Press 2009.
Spiegel, M., Vector Analysis, McGraw-Hill 1959.
Stroud, K., Vector Analysis, Industrial Press 2005.
194

## Page 207

Index
acceleration, 72
acceleration of gravity, 67
active transformation, 108
Ampere–Maxwell Law, 173
angular momentum, 160
angular velocity, 160
arithmetized space, 140
asymmetric top, 166
BAC minus CAB rule, 33, 162
basis vectors, 20
as partial derivatives, 23
dual, 113
orthonormal, 21
basis-vector transformation, 105
bound vectors, 2
Cartesian coordinates
unit vectors, 5
center of mass, 64
centrifugal force, 76
centripetal acceleration, 75
centripetal force, 76
chain rule, 41, 42
Christoffel, Elwin Bruno, 184
Christoffel symbols, 148
column vectors, 4
commutator, 186
continuity equation, 173
convergence, 46
coordinate-system transformation, 97
cosmological constant, 189
Coulomb constant, 85
covariant differentiation, 153, 186
notation, 155
covectors, 156
Cramer’s Rule, 118, 120
cross product, 27
curl, 50
curvilinear motion, 72
cylindrical coordinates, 17
unit vectors, 19
del cross, 51
del dot, 48
del operator, 43
differential length element, 140
direct transformation, 108
direction cosines, 102
directional derivative
as tangent vector, 43
directional derivatives, 41
divergence, 46
of gradient, 54
dot product, 25
dual basis vectors, 113
dual contravariant electromagnetic ﬁeld tensor,
178
Einstein, Albert, 123, 174, 183
Einstein summation convention, 123
Einstein tensor, 189
electric ﬁeld, 81
electric force, 83
electric potential, 88
electromagnetic ﬁeld tensor, 171, 178
electromagnetic wave equation, 174
electrostatic ﬁeld, 83
equipotential surfaces, 88
Euclidean space, 185
195

## Page 208

196
Index
Faraday’s Law, 173
ﬁeld
deﬁnition, 81
electric, 81
electrostatic, 46, 83
irrotational, 52, 88
magnetic, 89
magnetostatic, 89
scalar, 44
vector, 44
ﬁeld lines, 83
four-current, 177
four-dimensional spacetime, 174
four-vector, 176
free vectors, 2
free-body diagram, 63
friction, 69
frictional force, 70
Galilean transformation, 175
Gauss’s Law
for electric ﬁelds, 87, 172
for magnetic ﬁelds, 90, 172
General Relativity, 183
gradient, 44
inclined plane, 62
index notation, 122
index raising and lowering, 147
inertia tensor, 159, 164
inertial reference frame, 184
inner product, 138
inverse transformation, 105
irrotational ﬁelds, 52, 88
kinetic friction, 70
Kronecker Delta function, 139
Laplace, Pierre-Simon, 54
Laplace’s Equation, 89
Laplacian, 54
as difference from surrounding points, 57
as divergence of gradient, 54
as peak ﬁnder, 57
length contraction, 177
linearly independent vectors, 21
Lorentz, Hendrik, 176
Lorentz transform, 176
Lorentz transformation matrix, 181
magnetic ﬁeld, 89
magnetic force, 91
magnetostatic ﬁeld, 89
manifest covariance, 177
Maxwell, James Clerk, 46, 81, 171
Maxwell’s Equations, 172
tensor form, 178
metric tensor, 140
notation, 140
Minkowski metric, 177
moment of inertia
for a single particle, 160
moments of inertia, 164
nabla, 43
Newton, Isaac, 67
Newton’s Second Law, 63
non-Cartesian coordinate systems
cylindrical coordinates, 17
polar coordinates, 15
spherical coordinates, 19
non-Cartesian coordinates
unit vectors, 14
non-orthogonal coordinate systems, 110
normal force, 63
one-forms, 156
operator, 44
operator equation, 43
ordinary derivatives, 35
orthogonal transformation, 110
outer product, 137
parallel projection, 111
parallel transport, 154, 185
parameterized curve, 42
partial derivatives, 35
as basis vectors, 23
as slope, 37
chain rule, 41
higher-order, 40
mixed, 40
notation, 35
passive transformation, 105
perpendicular projection, 112
Poisson’s Equation, 88
polar coordinates, 15
unit vectors, 16
principal axes, 166
principal moments, 166
principle of equivalence, 184
products of inertia, 164

## Page 209

Index
197
Pythagorean theorem, 10
radial acceleration, 72
reciprocal basis vectors, 114
relativity of simultaneity, 177
Ricci scalar, 189
Ricci tensor, 188
Riemann, Bernhard, 184
Riemann curvature tensor, 183
right-hand rule, 28
rotor, 166
row vectors, 4
scalar, 4
deﬁnition, 4, 133
ﬁeld, 44
Ricci, 189
scalar product, 25
scalar triple product, 30
scale factors, 146
similarity transform, 170
sliding vectors, 3
space–time interval, 176
Special Relativity, 174
spherical coordinates, 19
unit vectors, 19
spherical top, 166
static friction, 70
summation convention, 123
symmetric top, 166
tangential acceleration, 72
tensor, 4
addition and subtraction, 135
deﬁnition, 5, 134
derivatives, 148
Einstein, 189
electromagnetic ﬁeld, 171, 178
higher-rank, 132
inertia, 159, 164
inner product, 138
metric, 140
multiplication, 137
notation, 134
rank, 5
Ricci, 188
Riemann curvature, 183
test charge, 82
time dilation, 177
top, 166
transformation
basis-vector, 105
coordinate-system, 97
direct or active, 108
equation, 102
inverse or passive, 105
matrix, 102
orthogonal, 110
triple scalar product, 30, 116
triple vector product, 32
unit vectors
Cartesian, 5
non-Cartesian, 14
vector, 1
addition, 11
graphical, 12
using components, 13
as an ordered set, 3
as derivative, 41
basis, 2
bound, 2
column, 4
components, 4, 7
covariant and contravariant, 97, 105
deﬁnition, 1, 133
ﬁeld, 44
free, 2
graphical depiction, 1
linearly independent, 21
multiplication by a scalar, 11
notation, 1
outer product, 137
row, 4
sliding, 3
unit
Cartesian, 5
non-Cartesian, 14
vector components, 4, 7
as projections onto coordinate axes, 8
vector ﬁeld, 3
versors, 6
weighted linear combination, 101
work, 25

## Page 210

_(no text on this page)_


