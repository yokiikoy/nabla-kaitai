<!-- source-pdf: FleischVectorsAndTensors.pdf | pages 151-180 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 151–180

## Page 151

5.4 Tensor multiplication
139
by one) and then you summed over that index (reducing the rank by one
more). Note also that contraction produces another tensor only when the two
indices that are made equal are in different positions (one superscript and one
subscript).
The reason for this becomes clear if you consider the contraction of the
tensor that resulted from the outer-product operation in Eq. 5.11. Contracting
this tensor in the ﬁrst and fourth indices by setting q equal to n gives
C
′np
onr = ∂x
′n
∂xi
∂x j
∂x
′o
∂x
′ p
∂xk
∂xl
∂x
′n
∂xm
∂x
′r Cik
jlm
= ∂x
′n
∂xi
∂xl
∂x
′n
∂x j
∂x
′o
∂x
′ p
∂xk
∂xm
∂x
′r Cik
jlm
= ∂xl
∂xi
∂x j
∂x
′o
∂x
′ p
∂xk
∂xm
∂x
′r Cik
jlm.
But the derivative ∂xl
∂xi involves only coordinates in the same (unprimed) sys-
tem, and coordinates within the same system must be independent of one
another. Hence this derivative must equal zero unless l = i, in which case
it must equal one. This is most easily expressed using the Kronecker Delta
function, deﬁned by
δi
j =
 1
i = j
0
i ̸= j .
Thus
C
′np
onr = δi
l
∂x j
∂x
′o
∂x
′ p
∂xk
∂xm
∂x
′r Cik
jlm
= ∂x j
∂x
′o
∂x
′ p
∂xk
∂xm
∂x
′r Cik
jim,
which is a tensor of rank 3, as expected. But note that this reduction from 5
to 3 in rank required that two of the partial derivatives combine to produce
the delta function, which then invoked the summation process. That derivative
combination only works if one of the contracted indices is a superscript and
the other a subscript.
In this last example, the contraction was performed on a tensor that was the
result of an outer product. That two-step process (outer-product multiplication
followed by contraction) is called the “inner product” of two tensors. So if you
start with two vectors (tensors of rank 1), form their outer product (producing
a tensor of rank 2), and then contract the result, you end up with a tensor
of rank zero – a scalar. This illustrates why the inner-product process can be
considered to be a generalization of the dot product between two vectors.

## Page 152

140
Higher-rank tensors
5.5 Metric tensor
As you think about contravariant and covariant components of vectors and
tensors, you should not lose sight of the fact that these components exist only
when you’ve selected a coordinate system. And why do you need a coordinate
system? Because coordinate systems “arithmetize” space – that is, they give
you a way of applying the rules of arithmetic to objects that exist in the space
in which you’re working. That space may be the three-dimension space of
everyday experience, or the four-dimension spacetime of Einstein, or any other
space you can imagine. The coordinate system you apply may have straight
axes that intersect at right angles, or the axes may be curved and intersect at
any angle of your choosing.
However you choose to arithmetize a space, there is one tensor that allows
you to deﬁne fundamental quantities such as lengths and angles in a consistent
manner at different locations. That tensor, the one that “provides the metric”
for a given coordinate system in the space of interest, is called the fundamental
or metric tensor. The lower-case letter “g” has become the standard symbol for
the metric tensor, which you may see written as ⃗⃗g or g. The metric tensor has
contravariant components gi j and covariant components gi j.
To understand the role of the metric tensor, consider two points separated
by an inﬁnitesimal distance ds. If the vector d⃗r extends from one point to
the other, then the square of the differential length element may be written as
ds2 = d⃗r ◦d⃗r. The vector d⃗r may be written using contravariant components
and coordinate basis vectors (⃗ei) as
d⃗r = ⃗eidxi,
or using covariant components and dual basis vectors (⃗ei) as
d⃗r = ⃗e idxi.
Since ds2 involves the dot product of d⃗r with itself, you have the option of
using the contravariant components dxi on both sides of the dot:
ds2 = d⃗r ◦d⃗r = ⃗eidxi ◦⃗e jdx j
= (⃗ei ◦⃗e j)dxidx j
= gi jdxidx j,
where gi j represents the covariant components of the metric tensor. Alter-
natively, you may use the covariant components dxi on both sides of
the dot:

## Page 153

5.5 Metric tensor
141
ds2 = d⃗r ◦d⃗r = ⃗e idxi ◦⃗e jdx j
= (⃗e i ◦⃗e j)dxidx j
= gi jdxidx j,
where gi j represents contravariant components of the metric tensor. A third
option is to use contravariant components on one side of the dot and covariant
components on the other:
ds2 = ⃗eidxi ◦⃗e jdx j
= (⃗ei ◦⃗e j)dxidx j
= dxidx j.
Note that in this case no metric tensor is needed, since the deﬁnition of dual
basis vectors ensures that ⃗ei ◦⃗e j equals one if i = j and zero if i ̸= j.
Whether ds2 is written as gi jdxidx j, gi jdxidx j, or dxidx j, you can be
sure of one thing: the distance between two points must be the same no matter
which coordinate system you employ, whether you use contravariant, covari-
ant, or mixed components. Hence it must be the job of the metric tensor ⃗⃗g
and its components gi j and gi j to turn the product of incremental coordinate
changes expressed in either contravariant or covariant components into the
invariant distance between points. This is the rationale behind the statement
that the metric tensor “provides the geometry” of the space.
The geometry of vectors entails use of lengths and angles, so it’s useful
to understand the role of the metric tensor in deﬁning the length of a vector
such as ⃗A and the angle between two vectors ⃗A and ⃗B. Just as the incremental
distance ds can be found by dotting the separation vector d⃗r into itself, the
length of vector ⃗A can be found from ⃗A ◦⃗A. And there’s more than one way
to do that.
One option is to use only the contravariant components of ⃗A:
| ⃗A| =
	
⃗A ◦⃗A =

Ai ⃗ei ◦A j ⃗e j
=

(⃗ei ◦⃗e j)Ai A j =

gi j Ai A j.
Another option is to use only covariant components:
| ⃗A| =
	
⃗A ◦⃗A =

Ai ⃗e i ◦A j ⃗e j
=

(⃗e i ◦⃗e j)Ai A j =

gi j Ai A j.
And the ﬁnal option is to use mixed components:

## Page 154

142
Higher-rank tensors
| ⃗A| =
	
⃗A ◦⃗A =

Ai ⃗ei ◦A j ⃗e j
=

(⃗ei ◦⃗e j)Ai A j =

Ai A j.
As in the case of d⃗r, the metric tensor ensures that the length of vector ⃗A is
invariant.
To understand the role of the metric tensor in providing a consistent deﬁni-
tion of angles, consider the dot product ⃗A◦⃗B. Once again, there are alternative
ways of writing this product, and this means that the angle between ⃗A and ⃗B
can be written in the following equivalent ways:
cos θ =
⃗A ◦⃗B
| ⃗A|| ⃗B|
=
gi j Ai B j

gi j Ai A j

gi j Bi B j
=
Ai B j
	
Ai Ai	
Bi Bi
=
gi j Ai B j

gi j Ai A j

gi j Bi B j
.
This explains why you’re likely to run into the statement that the metric tensor
“provides a dot product” for a space – if you know how to ﬁnd the dot product,
you can deﬁne lengths and angles.
To see the tensor nature of the metric tensor, consider the transformation of
the contravariant components of the incremental separation vector d⃗r:
dx
′i = ∂x
′i
∂x j dx j.
This means that the square of the incremental length (ds2) becomes:
ds2 =

∂x
′1
∂x1
∂x
′1
∂x1 + ∂x
′2
∂x1
∂x
′2
∂x1 + ∂x
′3
∂x1
∂x
′3
∂x1

dx1dx1
+

∂x
′1
∂x2
∂x
′1
∂x2 + ∂x
′2
∂x2
∂x
′2
∂x2 + ∂x
′3
∂x2
∂x
′3
∂x2

dx2dx2
+

∂x
′1
∂x3
∂x
′1
∂x3 + ∂x
′2
∂x3
∂x
′2
∂x3 + ∂x
′3
∂x3
∂x
′3
∂x3

dx3dx3
+

∂x
′1
∂x1
∂x
′1
∂x2 + ∂x
′2
∂x1
∂x
′2
∂x2 + ∂x
′3
∂x1
∂x
′3
∂x2

dx1dx2

## Page 155

5.5 Metric tensor
143
+

∂x
′1
∂x2
∂x
′1
∂x1 + ∂x
′2
∂x2
∂x
′2
∂x1 + ∂x
′3
∂x2
∂x
′3
∂x1

dx2dx1
+

∂x
′1
∂x1
∂x
′1
∂x3 + ∂x
′2
∂x1
∂x
′2
∂x3 + ∂x
′3
∂x1
∂x
′3
∂x3

dx1dx3
+

∂x
′1
∂x3
∂x
′1
∂x1 + ∂x
′2
∂x3
∂x
′2
∂x1 + ∂x
′3
∂x3
∂x
′3
∂x1

dx3dx1
+

∂x
′1
∂x2
∂x
′1
∂x3 + ∂x
′2
∂x2
∂x
′2
∂x3 + ∂x
′3
∂x2
∂x
′3
∂x3

dx2dx3
+

∂x
′1
∂x3
∂x
′1
∂x2 + ∂x
′2
∂x3
∂x
′2
∂x2 + ∂x
′3
∂x3
∂x
′3
∂x2

dx3dx2.
(5.12)
This daunting expression becomes far more tractable if you realize that each
bracketed term involves the sum of the partial derivatives of each of the trans-
formed coordinates (x
′1, x
′2, and x
′3) taken with respect to two of the original
coordinates (x1, x2, and x3). More speciﬁcally, each of the three terms within
each bracket is a product of the components of the basis vectors tangent to the
original axes (recall that ∂x
′1
∂xi , ∂x
′2
∂xi , and ∂x
′3
∂xi are the components in the trans-
formed coordinate system of the basis vector tangent to the ith original axis).
If you assign the bracketed terms to the variable g with two subscripts
denoting the axes with respect to which the derivatives are taken, you will
have
g11 =

∂x
′1
∂x1
∂x
′1
∂x1 + ∂x
′2
∂x1
∂x
′2
∂x1 + ∂x
′3
∂x1
∂x
′3
∂x1

,
g22 =

∂x
′1
∂x2
∂x
′1
∂x2 + ∂x
′2
∂x2
∂x
′2
∂x2 + ∂x
′3
∂x2
∂x
′3
∂x2

,
g33 =

∂x
′1
∂x3
∂x
′1
∂x3 + ∂x
′2
∂x3
∂x
′2
∂x3 + ∂x
′3
∂x3
∂x
′3
∂x3

,
g12 =

∂x
′1
∂x1
∂x
′1
∂x2 + ∂x
′2
∂x1
∂x
′2
∂x2 + ∂x
′3
∂x1
∂x
′3
∂x2

,
g13 =

∂x
′1
∂x1
∂x
′1
∂x3 + ∂x
′2
∂x1
∂x
′2
∂x3 + ∂x
′3
∂x1
∂x
′3
∂x3

,
g23 =

∂x
′1
∂x2
∂x
′1
∂x3 + ∂x
′2
∂x2
∂x
′2
∂x3 + ∂x
′3
∂x2
∂x
′3
∂x3

,

## Page 156

144
Higher-rank tensors
and since the order of multiplication is irrelevant, g21 = g12, g31 = g13, and
g32 = g23. Substituting these into Eq. 5.12, the expression for ds2 becomes
ds2 = g11dx1dx1 + g22dx2dx2 + g33dx3dx3 + g12dx1dx2 + g21dx2dx1
+ g13dx1dx3 + g31dx3dx1 + g23dx2dx3 + g32dx3dx2.
This can be further simpliﬁed using index notation and the summation
convention:
ds2 = gi jdxidx j.
(5.13)
The gi j term in this equation meets all the requirements of a second-rank
tensor, but it’s not just any tensor. Because it relates the coordinate differentials
in various directions to a quantity that is invariant across all coordinate trans-
formations, it’s no wonder that this tensor is called the metric or fundamental
tensor.
To understand what’s so fundamental about this tensor, recall that the partial
derivatives that make up the elements of gi j also represent the components of
the basis vectors tangent to the original coordinate axes:
⃗e1 =

∂x
′1
∂x1 , ∂x
′2
∂x1 , ∂x
′3
∂x1

,
⃗e2 =

∂x
′1
∂x2 , ∂x
′2
∂x2 , ∂x
′3
∂x2

,
(5.14)
⃗e3 =

∂x
′1
∂x3 , ∂x
′2
∂x3 , ∂x
′3
∂x3

.
And since
gi j =

∂x
′1
∂xi
∂x
′1
∂x j + ∂x
′2
∂xi
∂x
′2
∂x j + ∂x
′3
∂xi
∂x
′3
∂x j

,
(5.15)
another way to represent the metric tensor is gi j = ⃗ei ◦⃗e j (the inner product
of the basis vectors tangent to the coordinate axes). Since the inner product
involves the projection of one vector onto the direction of another and scales
as the length of those two vectors, the elements of gi j specify the relationships
between the coordinate axes. Those relationships are determined by the shape
of the coordinate space.
The nature of the metric tensor can be readily understood by considering a
transformation from spherical polar (r, θ, φ) to Cartesian (x, y, z) coordinates.
In this case

## Page 157

5.5 Metric tensor
145
x
′1 = x = rsin(θ)cos(φ) = x1sin(x2)cos(x3),
x
′2 = y = rsin(θ)sin(φ) = x1sin(x2)sin(x3),
x
′3 = z = rcos(θ) = x1cos(x2),
(5.16)
and the partial derivatives appearing in the elements of the metric tensor are
∂x
′1
∂x1 = sin(x2)cos(x3) = sin(θ)cos(φ),
∂x
′1
∂x2 = x1cos(x2)cos(x3) = rcos(θ)cos(φ),
∂x
′2
∂x1 = sin(x2)sin(x3) = sin(θ)sin(φ),
∂x
′2
∂x2 = x1cos(x2)sin(x3) = rcos(θ)sin(φ),
∂x
′3
∂x1 = cos(x2) = cos(θ),
∂x
′3
∂x2 = −x1sin(x2) = −rsin(θ),
and
∂x
′1
∂x3 = −x1sin(x2)sin(x3) = −rsin(θ)sin(φ),
∂x
′2
∂x3 = x1sin(x2)cos(x3) = rsin(θ)cos(φ),
∂x
′3
∂x3 = 0.
Inserting these values into the expression for gi j (Eq. 5.15) gives the
diagonal terms:3
g11 =

∂x
′1
∂x1
∂x
′1
∂x1 + ∂x
′2
∂x1
∂x
′2
∂x1 + ∂x
′3
∂x1
∂x
′3
∂x1

= 1,
g22 =

∂x
′1
∂x2
∂x
′1
∂x2 + ∂x
′2
∂x2
∂x
′2
∂x2 + ∂x
′3
∂x2
∂x
′3
∂x2

= r2,
g33 =

∂x
′1
∂x3
∂x
′1
∂x3 + ∂x
′2
∂x3
∂x
′2
∂x3 + ∂x
′3
∂x3
∂x
′3
∂x3

= r2sin2(θ).
3 If you don’t see how to get these results, you can ﬁnd more detail in the problems at the end of
this chapter and in the on-line solutions.

## Page 158

146
Higher-rank tensors
The off-diagonal terms are
g12 =

∂x
′1
∂x1
∂x
′1
∂x2 + ∂x
′2
∂x1
∂x
′2
∂x2 + ∂x
′3
∂x1
∂x
′3
∂x2

= 0,
g13 =

∂x
′1
∂x1
∂x
′1
∂x3 + ∂x
′2
∂x1
∂x
′2
∂x3 + ∂x
′3
∂x1
∂x
′3
∂x3

= 0,
g23 =

∂x
′1
∂x2
∂x
′1
∂x3 + ∂x
′2
∂x2
∂x
′2
∂x3 + ∂x
′3
∂x2
∂x
′3
∂x3

= 0.
Thus the metric tensor for spherical polar coordinates is
gi j =
⎡
⎣
g11
g12
g13
g21
g22
g23
g31
g32
g33
⎤
⎦=
⎡
⎣
1
0
0
0
r2
0
0
0
r2sin2(θ)
⎤
⎦.
(5.17)
A careful look at the metric tensor can tell you something about the coordinate
system you’re dealing with. For example, the fact that all off-diagonal elements
are zero in this case tells you that spherical polar coordinate axes, while curved,
are orthogonal (that is, the lines of increasing r, θ, and φ intersect at right
angles). Furthermore, by inserting these values into Eq. 5.13, you’ll have
ds2 = dr2 + r2dθ2 + r2sin2θdφ2.
(5.18)
This expression makes it clear that the elements of the metric tensor tell you
how to turn an incremental change in r, θ, or φ into a change in distance. For
example, the factor of one in front of the dr2 term means that a change in r
is already a distance. But a change in zenith angle (θ) must be multiplied by a
factor of r to turn it into a distance. And the distance corresponding to a change
in the azimuthal angle φ depends on both the zenith angle (hence the sin(θ)
term in g33) as well as the distance from the origin (hence the r term in g33).
Other coordinate systems require other factors to convert each change in a
coordinate value to a distance, and those factors always appear in the metric
tensor for that system. For orthogonal coordinate systems, the square roots of
the diagonal elements of the metric tensor (√g11, √g22, and √g33) are called
the “scale factors” (h1, h2, and h3) of the coordinate system. Thus the scale
factors for spherical polar coordinates are h1 = √g11 = 1, h2 = √g22 = r,
and h3 = √g33 = r sin θ.
Once you’re familiar with the metric tensor and scale factors, you can easily
ﬁnd the differential operators gradient, divergence, curl, and Laplacian in any
orthogonal coordinate system (curvilinear or rectangular). For example, the
gradient is given by

## Page 159

5.6 Index raising and lowering
147
⃗∇φ = 1
h1
∂φ
∂x1 ˆe1 + 1
h2
∂φ
∂x2 ˆe2 + 1
h3
∂φ
∂x3 ˆe3,
and the divergence may be written as
⃗∇◦⃗A =
1
h1h2h3
 ∂
∂x1 (h2h3A1) +
∂
∂x2 (h1h3A2) +
∂
∂x3 (h1h2A3)

.
The curl is given by
⃗∇× ⃗A =
1
h1h2h3

h1 ˆe1
h2 ˆe2
h3 ˆe3
∂
∂x1
∂
∂x2
∂
∂x3
h1A1
h2A2
h3A3

,
which expands to
⃗∇× ⃗A =
1
h1h2h3
∂h3A3
∂x2
−∂h2A2
∂x3

h1 ˆe1
+
∂h1A1
∂x3
−∂h3A3
∂x1

h2 ˆe2 +
∂h2A2
∂x1
−∂h1A1
∂x2

h3 ˆe3

.
The Laplacian can be found as
∇2φ =
1
h1h2h3
 ∂
∂x1
h2h3
h1
∂φ
∂x1

+
∂
∂x2
h1h3
h2
∂φ
∂x2

+
∂
∂x3
h1h2
h3
∂φ
∂x3

.
If you’d like to see some examples of how these expressions can be used, check
out the problems at the end of this chapter and the on-line solutions.4
5.6 Index raising and lowering
One of the many useful functions of the metric tensor is to convert between the
covariant and contravariant components of other tensors. Imagine that you’re
given the contravariant components and original basis vectors of a tensor and
you wish to determine the covariant components. One approach is to use the
techniques described in Chapter 4 (ﬁnding the dual basis vectors, performing
parallel and perpendicular projections, and the like), but with the metric tensor,
you have another option. You can use relations such as
gi j A j = Ai
(5.19)
to convert a contravariant index to a covariant one (thus “lowering” an index).
Furthermore, if you wish to convert a covariant index to a contravariant index,
4 You can ﬁnd the derivation of these extremely handy equations in Boas’ Mathematical
Methods in the Physical Sciences, John Wiley and Sons, 2006.

## Page 160

148
Higher-rank tensors
you can use the inverse of gi j (which is just gi j) to perform operations like
this:
gi j Bi = B j.
(5.20)
And this same process works for higher-order tensors:
gi j Aik = A j
k,
Ci
jk = g jsCis
k ,
T i jk = gilT jk
l
.
(5.21)
5.7 Tensor derivatives and Christoffel symbols
In many applications, it’s important to know how a vector ﬁeld changes as
you move from one location to another. For vectors expressed using Cartesian
coordinates, taking the derivative of a vector is quite straightforward: you sim-
ply take the derivative of each of the vector’s components. You can do that
because the Cartesian basis vectors (ˆı, ˆj, and ˆk) are everywhere constant in
both magnitude and direction. That means you don’t need to worry about the
derivatives of the basis vectors. But as you’ve seen for spherical polar coordi-
nates, the basis vectors (ˆr, ˆθ, and ˆφ) point in different directions as you move
around the space, which means that when you take a spatial derivative of a
vector expressed in these coordinates, you must also consider the derivatives
of the basis vectors.
Thus if you have a vector ⃗A expressed in general coordinates x1, x2, x3 with
covariant basis vectors ⃗e1, ⃗e2, and ⃗e3 as
⃗A = A1 ⃗e1 + A2 ⃗e2 + A3 ⃗e3,
the derivative of ⃗A with respect to coordinate x1 is
∂⃗A
∂x1 = ∂(A1 ⃗e1 + A2 ⃗e2 + A3 ⃗e3)
∂x1
= ∂(Ai ⃗ei)
∂x1
= ∂Ai
∂x1 ⃗e1 + Ai ∂⃗ei
∂x1 .
It’s the second term in this equation that complicates the process of taking a
derivative in coordinate systems in which the magnitude and/or direction of
the basis vectors change as you move around the space. And as you might
expect, similar terms appear when you take the derivatives of ⃗A with respect

## Page 161

5.7 Tensor derivatives and Christoffel symbols
149
to the other coordinates. So if you want to evaluate the changes in vector ﬁelds
expressed in non-orthonormal coordinates, you have to account for possible
changes in the basis vectors. Properly accounting for those changes means that
the result of the defferentiation process will retain the tensor characteristics of
the original object.
Fortunately, there’s a way to account for any change in the basis vectors and
to ensure that the derivative of a tensor is another tensor. That process, called
the “covariant derivative,” is described in the next section of this chapter. But
the process of covariant differentiation will make a lot more sense to you if
you’ve ﬁrst learned the meaning of the Christoffel symbols described in this
section.
To understand Christoffel symbols, you should begin by realizing that the
derivative of a basis vector will be another vector. Like any vector, that vector
can be described as the weighted combination of the basis vectors at the point
under consideration. Each Christoffel symbol, written as an uppercase Greek
gamma (), simply represents the weighting coefﬁcient for one of the basis
vectors. Hence the deﬁning relationship for Christoffel symbols5 is
k
i j ⃗ek = ∂⃗ei
∂x j ,
(5.22)
in which the index i speciﬁes the basis vector for which the derivative is being
taken, the index j denotes the coordinate being varied to induce this change
in the ith basis vector, and the index k identiﬁes the direction in which this
component of the derivative points, as shown in Figure 5.1.
This Christoffel symbol gives
you the magnitude of one
component of the
derivative vector
Tells you which basis vector
points in the direction of this
component of the derivative
vector
Tells you which basis
vector’s change is
being considered
Tells you which coordinate
is being varied to cause a
change in the basis vector
Γk
ij
Figure 5.1 Explanation of Christoffel symbol indices.
5 The Christoffel symbols written as k
i j are Christoffel symbols of the second kind; another
form of Christoffel symbol (the “ﬁrst kind”) is described in most General Relativity texts.

## Page 162

150
Higher-rank tensors
has zero
magnitude
caused by a
change in θ
rθ
Γr =0
in the er
direction
The change
in er
1
r
varies inversely
with distance
caused by a
change in θ
The change
in er
Γθ =
in the eθ
direction
rθ
Figure 5.2 Example of Christoffel symbol indices.
Hence if you ﬁnd two Christoffel symbols such as r
rθ = 0 and θ
rθ = 1
r ,
you know that
∂⃗er
∂θ = 0⃗er + 1
r ⃗eθ,
which is further explained in Figure 5.2.
As this example illustrates, Christoffel symbols are really quite simple to
understand once you know the code of their indices. Best of all, the values of
these useful symbols are easy to determine if you know the elements of the
metric tensor for the coordinate system in which you’re working. It will take
a bit of algebra to get to the relationship between Christoffel symbols and the
metric tensor, but the result makes the trip worthwhile.
A good way to start is to form the dot product of the basis vector ⃗e l with
both sides of Eq. 5.22:
k
i j ⃗ek ◦⃗e l = ⃗e l ◦∂⃗ei
∂x j .
Remembering that ⃗ek ◦⃗e l = δl
k, this becomes
k
i jδl
k = ⃗e l ◦∂⃗ei
∂x j ,
l
i j = ⃗e l ◦∂⃗ei
∂x j .
Since the term ∂⃗ei
∂x j is the same as ∂⃗e j
∂xi , this may be written as
l
i j = 1
2 ⃗e l ◦∂⃗ei
∂x j + 1
2 ⃗e l ◦∂⃗e j
∂xi ,

## Page 163

5.7 Tensor derivatives and Christoffel symbols
151
which seems rather pointless until you add nothing to it. Nothing, that is, in the
following form:
l
i j = 1
2 ⃗e l ◦∂⃗ei
∂x j +
1
2gkl ∂⃗ek
∂x j ◦⃗ei −1
2gkl ∂⃗e j
∂xk ◦⃗ei

+ 1
2 ⃗e l ◦∂⃗e j
∂xi +
1
2gkl ∂⃗ek
∂xi ◦⃗e j −1
2gkl ∂⃗ei
∂xk ◦⃗e j

.
Note that the terms in parentheses on each line add to zero, so you haven’t
changed the quantity on the right side of the equation by adding these terms.
It may look like things are getting worse, but the situation will become more
clear once you’ve accomplished a few more bits of manipulation. The ﬁrst bit
is to realize that ⃗e l = gkl ⃗ek, so the Christoffel symbol becomes
l
i j = 1
2gkl⃗ek ◦∂⃗ei
∂x j +
1
2gkl ∂⃗ek
∂x j ◦⃗ei −1
2gkl ∂⃗e j
∂xk ◦⃗ei

+ 1
2gkl⃗ek ◦∂⃗e j
∂xi +
1
2gkl ∂⃗ek
∂xi ◦⃗e j −1
2gkl ∂⃗ei
∂xk ◦⃗e j

.
Now it’s just a matter pulling out the common factor of 1
2gkl and grouping the
terms by their sign:
l
i j = 1
2gkl

⃗ek ◦∂⃗ei
∂x j + ∂⃗ek
∂x j ◦⃗ei

+

⃗ek ◦∂⃗e j
∂xi + ∂⃗ek
∂xi ◦⃗e j

−
 ∂⃗e j
∂xk ◦⃗ei + ∂⃗ei
∂xk ◦⃗e j

,
which may be further simpliﬁed if you recognize that
⃗ek ◦∂⃗ei
∂x j + ∂⃗ek
∂x j ◦⃗ei = ∂(⃗ek ◦⃗ei)
∂x j
,
⃗ek ◦∂⃗e j
∂xi + ∂⃗ek
∂xi ◦⃗e j = ∂(⃗e j ◦⃗ek)
∂xi
,
⃗ei ◦∂⃗e j
∂xk + ∂⃗ei
∂xk ◦⃗e j = ∂(⃗ei ◦⃗e j)
∂xk
.
So
l
i j = 1
2gkl
∂(⃗ek ◦⃗ei)
∂x j
+ ∂(⃗e j ◦⃗ek)
∂xi
−∂(⃗ei ◦⃗e j)
∂xk

.
But you know from the deﬁnition of the elements of the metric tensor that
⃗ei ◦⃗ek = gik and that ⃗ei ◦⃗e j = gi j, which means you can write
l
i j = 1
2gkl
∂gik
∂x j + ∂g jk
∂xi −∂gi j
∂xk

.
(5.23)

## Page 164

152
Higher-rank tensors
With this expression, ﬁnding the Christoffel symbols for any coordinate sys-
tem for which you know the metric tensor is quite straightforward. And why
is that worth doing? Simply because using the Christoffel symbols, you can
take a derivative of vectors and tensors that accounts for changes in the basis
vectors as well as changes in the components. This preserves the most impor-
tant property of a tensor: invariance across coordinate systems. Such covariant
derivatives are the subject of the next section, but before getting to that, you
might want to consider an example of the Christoffel symbols for a familiar
coordinate system.
Consider the cylindrical coordinates (r, φ, and z) described in Section 1.5.
In this system, the square of the differential length element is related to the
coordinate differentials by ds2 = dr2 + r2dφ2 + dz2. Hence the covariant
metric tensor may be represented by
gi j =
⎡
⎣
g11
g12
g13
g21
g22
g23
g31
g32
g33
⎤
⎦=
⎡
⎣
1
0
0
0
r2
0
0
0
1
⎤
⎦,
which suggests that most of the Christoffel symbols will be zero in this case.
You can verify that by taking the derivatives indicated in Eq. 5.23, beginning
with l = 1, i = 1, and j = 1 (and don’t forget that the summation convention
means that you must sum over k):
1
11 = 1
2g11
∂g11
∂x1 + ∂g11
∂x1 −∂g11
∂x1

+ 1
2g21
∂g12
∂x1 + ∂g12
∂x1 −∂g11
∂x2

+ 1
2g31
∂g13
∂x1 + ∂g13
∂x1 −∂g11
∂x3

,
and then using the relations x1 = r, x2 = φ, and x3 = z:
1
11 = 1
2(1)
∂(1)
∂r
+ ∂(1)
∂r
−∂(1)
∂r

+ 1
2(0)
∂(0)
∂r
+ ∂(0)
∂r
−∂(1)
∂φ

+ 1
2(0)
∂(0)
∂r
+ ∂(0)
∂r
−∂(1)
∂z

= 0.
OK, that one was pretty boring, as are most of the others in this case. But have
a go at the Christoffel symbol for l = 1, i = 2, and j = 2:

## Page 165

5.8 Covariant differentiation
153
1
22 = 1
2g11
∂g21
∂x2 + ∂g21
∂x2 −∂g22
∂x1

+ 1
2g21
∂g22
∂x2 + ∂g22
∂x2 −∂g22
∂x2

+ 1
2g32
∂g23
∂x2 + ∂g23
∂x2 −∂g22
∂x3

,
which is:
1
22 = 1
2(1)
∂(0)
∂φ + ∂(0)
∂φ −∂r2
∂r

+ 1
2(0)
∂r2
∂φ + ∂r2
∂φ −∂r2
∂φ

+ 1
2(0)
∂(0)
∂φ + ∂(0)
∂φ −∂r2
∂z

,
or
1
22 = 1
2(1)[0 + 0 −2r] + 0 + 0 = −r.
Now you’re getting somewhere. And exactly where is that? Just remember
the meaning of a Christoffel symbol, and you’ll see that this result means that
the change in the covariant ⃗φ basis vector as you move in the φ direction has
a component in the −⃗r direction that increases directly with distance from the
origin.
A similar analysis shows that 2
12 = 2
21 = 1/r, which are the only other
non-zero Christoffel symbols for the cylindrical coordinate system.6 If you
don’t see how to get that result, take a look at the problems at the end of this
chapter and the on-line solutions.
5.8 Covariant differentiation
With Christoffel symbols in hand, you have a way of differentiating a vector or
higher-order tensor that includes the effect of changes (if any) in the magnitude
and direction of the basis vectors used to expand that vector or tensor. This type
of derivative is called the “covariant” derivative, and it ﬁnds application not
only in the Euclidean space in which many engineering and physics problems
are worked, but also in the curved Riemanian space of General Relativity.
In Euclidean space, two vectors at different locations may be compared and
combined by dragging one of the vectors to the location of the other without
6 Note that the symmetry of the metric tensor means that Christoffel symbols of this type are
symmetric in the two lower indices.

## Page 166

154
Higher-rank tensors
changing its magnitude or its direction. If the vector is expanded using Carte-
sian coordinates, such “parallel transport” is accomplished simply by keeping
each of its components the same (because the Cartesian basis vectors have the
same magnitude and direction everywhere). But if the vector is expressed in
non-Cartesian coordinates, the length and direction of the basis vectors may be
different at the two locations. In such cases, the covariant derivative provides
a means of parallel-transporting one of the vectors to the location of the other.
The situation is more complicated for curved spaces. You can ﬁnd the details
of the use of the covariant derivative in curved spaces in Chapter 6, but for
now you can understand the role of the covariant derivative by considering a
two-dimensional spherical surface embedded in a three-dimensional Euclidean
space. Imagine a series of tangent planes just touching the sphere at each loca-
tion, and picture a vector lying in one of those tangent planes. If that vector is
moved to a different location on the sphere while holding its direction constant
(as viewed in the larger three-dimensional space), it will not lie in the tangent
plane at the new location (you can think of the vector as “sticking out” of
the two-dimensional space of the sphere). In such cases, the covariant deriva-
tive serves to project the derivative of the vector into the tangent space of the
sphere.
You should also note that the covariant differentiation process produces
a result that retains the properties of a tensor, which means that the result
transforms between coordinate systems according to the rules of tensor
transformation.
To understand how the process of covariant differentiation works, consider
the vector ⃗A = A1 ⃗e1 + A2 ⃗e2 + A3 ⃗e3 and its derivatives
∂⃗A
∂x j = ∂(A1 ⃗e1 + A2 ⃗e2 + A3 ⃗e3)
∂x j
= ∂(Ai ⃗ei)
∂x j
= ∂Ai
∂x j ⃗ei + Ai ∂⃗ei
∂x j .
Now replace the partial derivative in the second term with the Christoffel-
symbol deﬁnition (Eq. 5.22):
∂⃗A
∂x j = ∂Ai
∂x j ⃗ei + Ai(k
i j ⃗ek).
Since the indices i and k in the second term are both dummy indices by the
summation rule, you can switch them and then extract the common factor that
is now the basis vector ⃗ei:

## Page 167

5.8 Covariant differentiation
155
∂⃗A
∂x j = ∂Ai
∂x j ⃗ei + Ak(i
kj ⃗ei)
=
∂Ai
∂x j + Aki
kj

⃗ei.
The covariant derivative is deﬁned as the combination of the two terms inside
the parentheses. Common notation for the covariant derivative is to use a semi-
colon (;) in front of the index with respect to which the covariant derivative is
being taken ( j in this case). Thus you’re likely to see the components of the
covariant derivative deﬁned as
Ai
; j ≡∂Ai
∂x j + Aki
kj.
(5.24)
A similar analysis leads to the covariant derivative of a vector expanded
using covariant coefﬁcients:
Ai; j ≡∂Ai
∂x j −Akk
i j.
(5.25)
Note that the term involving Christoffel symbols is subtracted in this case.
To make the meaning of Eqs. 5.24 and 5.25 more explicit, consider the
covariant derivative of vector ⃗A with respect to φ in cylindrical coordinates
(so x1 = r, x2 = φ, and x3 = z). Setting j = 2 in Eq. 5.24 (since we’re
interested in the covariant derivative with respect to φ),
Ar
;φ = ∂Ar
∂φ + Arr
rφ + Aφr
φφ + Azr
zφ
= ∂Ar
∂φ + 0 + Aφ(−r) + 0,
which says that a change in the r-component of vector ⃗A caused by a change
in φ is caused both by a change in Ar with φ and by a change in the basis
vectors which causes a portion of ⃗A that was originally in the φ-direction to
now point in the −r-direction. Likewise, for the change in Aφ as the value of
φ is changed,
Aφ
;φ = ∂Aφ
∂φ + Aφφ
rφ + Arφ
φφ + Azφ
zφ
= ∂Aφ
∂φ + Ar
1
r

+ 0 + 0.
Thus
∂⃗A
∂φ =
∂Ar
∂φ −r Aφ

⃗er +
∂Aφ
∂φ + 1
r Ar

⃗eφ.
The process of covariant differentiation can also be applied to higher-
order tensors. As you might expect, this simply requires the addition of a

## Page 168

156
Higher-rank tensors
Christoffel-symbol term for each contravariant index, and the subtraction of
a Christoffel-symbol term for each covariant index. Hence
Ai j
;k = ∂Ai j
∂xk + Alji
lk + Ail j
lk,
Bi j ;k = ∂Bi j
∂xk −Bljl
ik −Bill
jk,
Ci
j ;k =
∂Ci
j
∂xk + Cl
ji
lk −Ci
ll
jk.
5.9 Vectors and one-forms
If you look up the subject of tensors in recently published physics texts, espe-
cially those dealing with General Relativity, you may be surprised to ﬁnd little
mention of contravariant and covariant components in favor of terms such as
“covectors” and “one-forms.” Have you wasted your time struggling to under-
stand complicated concepts and terminology that have now become obsolete?
I obviously don’t think so, or I wouldn’t have devoted so many pages to the
developments of the last two chapters. Instead, I believe there’s value in seeing
the “traditional” presentation as well as the “modern” approach, because the
differences arise from perspective rather than from the core concepts. But those
different perspectives do lead to very different terminology, and the purpose of
this section is to provide a short introduction to that terminology.
The ﬁrst thing to understand is that the traditional approach tends to treat
contravariant and covariant components as representations of the same object,
whereas in the modern approach objects are classiﬁed either as “vectors” or
as “one-forms” (also called “covectors”). In the modern terminology, vectors
transform as contravariant quantities, and one-forms transform as covariant
quantities. Quantities with dimension of length in the numerator (such as
velocity, with units that include “meters per”) ﬁt naturally into the vector
category; quantities with dimension of length in denominator (such as the gra-
dient of a scalar ﬁeld, with units that include “per meter”) ﬁt naturally into the
one-form category.
In illustrations involving vectors and one-forms, vectors are represented as
arrows and one-forms are represented as small sections of surfaces, as shown
in Figure 5.3. As indicated in the ﬁgure, for vectors the angle of the arrow
shows direction and the length of the arrow shows the magnitude. For one-
forms, surfaces are aligned normal to the direction and the spacing between
surfaces is inversely proportional to the magnitude. This means that vectors
with greater magnitude are represented by longer arrows, while one-forms of
greater magnitude are represented by closer spacing.

## Page 169

5.10 Chapter 5 problems
157
x
y
z
One-form with
small magnitude
One-form with
large magnitude
Vector with
large magnitude
Vector with
small magnitude
Figure 5.3 Representation of vectors as arrows and one-forms as surfaces.
As in the traditional approach, vectors (which utilize contravariant com-
ponents) expand using original basis vectors, while one-forms (which utilize
covariant components) expand using basis one-forms, which are equivalent to
dual basis vectors in the traditional approach. That correspondence means that
the product of a vector and a one-form is an invariant (a scalar), just as the
multiplication of a contravariant and a covariant quantity produces a scalar
without requiring the metric tensor. One very nice graphical interpretation
of such products is that the resulting scalar is represented by the number of
one-form surfaces through which the arrow of a vector passes.
Authors using the modern approach often place strong emphasis on vectors
and one-forms as operators (or rules), so you’re likely to encounter statements
that vectors “take” one-forms and produce scalars, just as one-forms “take”
vectors and produce scalars. Likewise, a higher-order tensor takes multiple
vectors and/or one-forms and produces a scalar. From this perspective, the met-
ric tensor is an operator that takes two vectors or two one-forms and produces
their dot product, and the components of the metric tensor may be found by
feeding it basis vectors or one-forms.
5.10 Chapter 5 problems
5.1 Show that the process of subtracting one tensor from another results in a
quantity that is also a tensor.

## Page 170

158
Higher-rank tensors
5.2 Find the elements of the metric tensor for spherical coordinates by
forming the dot products of the relevant basis vectors.
5.3 Show how the derivatives given after Eq. 5.16 lead to the elements of the
metric tensor for spherical polar coordinates (Eq. 5.17).
5.4 Use the scale factors for spherical polar coordinates to verify the expres-
sions given in Chapter 2 for the gradient, divergence, curl, and Laplacian
in spherical coordinates.
5.5 Show that for cylindrical coordinates (r, φ, z) the Christoffel symbols
2
12 and 2
21 are equal to 1/r.
5.6 Find gi j, the inverse of the spherical metric tensor gi j.
5.7 Use gi j to raise the indices of the vector Ai = (1,r2sinθ, sin2θ).
5.8 On the two-dimensional surface of a sphere of radius R, the square of
the differential length element is given by ds2 = R2dθ2 + R2sin2θdφ2.
Find the metric tensor gi j and its inverse gi j for this case.
5.9 What are the Christoffel symbols for the 2-D spherical surface of
Problem 5.8?
5.10 Show that the covariant derivative of the metric tensor equals zero.

## Page 171

6
Tensor applications
This chapter provides examples of how to apply the tensor concepts contained
in Chapters 4 and 5, just as Chapter 3 provided examples of how to apply
the vector concepts presented in Chapters 1 and 2. As in Chapter 3, the intent
for this chapter is to include more detail about a small number of selected
applications than can be included in the chapters in which tensor concepts are
ﬁrst presented.
The examples in this chapter come from the ﬁelds of Mechanics, Elec-
tromagnetics, and General Relativity. Of course, there’s no way to compre-
hensively cover any signiﬁcant portion of those ﬁelds in one chapter; these
examples were chosen only to serve as representatives of the types of tensor
application you’re likely to encounter in those ﬁelds.
6.1 The inertia tensor
A very useful way to think of mass is this: mass is the characteristic of matter
that resists acceleration. This means that it takes a force to change the velocity
of any object with mass. You may ﬁnd it helpful to think of moment of inertia
as the rotational analog of mass. That is, moment of inertia is the characteristic
of matter that resists angular acceleration, so it takes a torque to change the
angular velocity of an object.
Many students ﬁnd that rotational motion is easier to understand by keeping
the relationships between translational and rotational quantities in mind. So
where translational motion dealt with position (x), velocity (⃗v), and accelera-
tion (⃗a), rotational motion has the analogous quantities of angle (θ), angular
velocity (⃗ω), and angular acceleration (⃗α). There are rotational analogs for
many other quantities; the translational quantities of force ( ⃗F), mass (m), and
momentum ( ⃗p) have the rotational equivalents of torque (⃗τ), moment of inertia
(I), and angular momentum (⃗L).
159

## Page 172

160
Tensor applications
As you may also recall, several of the equations relating various translational
quantities have direct parallels in rotational motion. So the rotational equiva-
lent of Newton’s Second Law ( ⃗F = m⃗a) is ⃗τ = I ⃗α.1 And whereas translational
momentum is related to mass and velocity by ⃗p = m⃗v, you probably learned
that angular momentum is related to moment of inertia and angular velocity by
Lz = Iω.
When ﬁrst presenting these relationships, most texts restrict the motion to
planar rotation of a single particle to keep things simple. So when you think of
the relationship between linear and angular velocity, you may think of some-
thing like v = ωr. And if Lz = mvr, then Lz = mr2ω. Taking mr2 as the
moment of inertia (I) of a single particle, this becomes Lz = Iω. But the v
and the ω in those equations can’t really be velocities, since they’re written
as scalars rather than vectors, and that z subscript on the angular momentum
seems to be trying to tell you something.
It is. It’s telling you that you’re using an equation for one component of the
angular momentum (the z-component in this case), and this pertains to a single
particle moving about the origin in the xy plane. So these equations aren’t
wrong, they just have limited application. Speciﬁcally, they apply to cases of
planar motion about the z-axis.
The more-general relationship between the vectors that represent velocity,
angular velocity, and position is this:
⃗v = ⃗ω × ⃗r,
(6.1)
in which the cross represents the vector cross product described in Chapter 2.
And the equations relating angular momentum to linear momentum, linear
velocity, and mass are
⃗L = ⃗r × ⃗p
= ⃗r × (m⃗v)
= m⃗r × ⃗v.
(6.2)
Before delving more deeply into these equations, you should consider the
implications of the (planar-motion) equation that says that the moment of
inertia of a single particle is Iparticle = mr2. One important idea in this
equation is that the moment of inertia of a particle depends not only on its
mass, but also on the location of that mass – speciﬁcally, the distance (r) of
the mass from the axis of rotation. Thus the moment of inertia of an extended
object made up of many particles must depend not only on the object’s mass,
1 Or, if you prefer the more-general form of Newton’s Second Law ( ⃗F = d ⃗p
dt ), the analogous
rotational relationship is ⃗τ = d ⃗L
dt .

## Page 173

6.1 The inertia tensor
161
but on the distribution of that mass. That’s true in the case of general motion
as well as planar rotation.
If you think of the rotational analog to the translational equation ⃗p = m⃗v,
you may be tempted to write an equation such as ⃗L = I ⃗ω. But that equation
would indicate that the angular momentum ⃗L must be in the same direction as
the angular velocity ⃗ω, since multiplication by a scalar can change the length
but not the direction of a vector (unless the scalar is negative, in which case
the direction of the vector is reversed). For general motion, the situation is
more complex, as you can see by applying Eq. 6.2 to a single particle cir-
cling about the axis shown in Figure 6.1. In this ﬁgure, the particle “m” is
circling around the z-axis, so the angular velocity (⃗ω) points straight up, paral-
lel to the z-axis. In this view, you’re looking down the x-axis toward the origin
of the coordinate system, which is well below the plane of the particle’s path.
The particle is initially at the position shown on the left side of the ﬁgure,
and its velocity vector is coming out of the page. Since the vector angular
momentum is given by ⃗L = m⃗r × ⃗v, you can ﬁnd the direction of the angular
momentum at this initial instant by using your right hand to form the cross
product between ⃗r and ⃗v, as described in Section 2.2. If you do this properly,
you should see that ⃗L initially points up and to the right, as shown by ⃗Linitial
in the ﬁgure. At a later time, after the particle has completed one-half revolu-
tion about the z-axis, its velocity vector is into the page, as shown in the right
y
z
ω
m
m
rlater
Velocity vlater
is into page
 Llater = mrlater × vlater
mrinitial × vinitial =  Linitial
Velocity vinitial
is out of page
rinitial
Figure 6.1 Single point mass moving around an axis.

## Page 174

162
Tensor applications
portion of the ﬁgure. At that later instant, the cross product between ⃗r and ⃗v
means that the direction of the angular momentum vector ⃗L is up and to the
left, as shown by ⃗Llater.
So not only is the angular-momentum vector ⃗L not parallel to the angular-
velocity vector ⃗ω, the direction of the ⃗L is changing as the particle moves
around the axis, while the direction of ⃗ω remains ﬁxed along the z-axis.
Under these circumstances, you clearly cannot use a scalar value for the
moment of inertia to relate the angular momentum to the angular velocity
through an equation such as ⃗L = I ⃗ω. A scalar moment of inertia simply isn’t
capable of relating a vector in one direction to a different vector in another
direction. But if you’ve followed the developments of Chapters 4 and 5, you’re
already familiar with a type of object that is capable of taking in a vector (such
as ⃗ω) and producing another vector (such as ⃗L) that points in a different direc-
tion. That object is a tensor. So although you may have initially learned about
the moment of inertia as a scalar value in the case of planar motion about
the origin, you should now understand why more-general problems require a
more-powerful approach, and that involves the representation of inertia as a
tensor rather than a scalar.
You may be thinking that simply by adding another particle of equal mass
at the same distance on the other side of the z-axis, you could produce an
additional bit of angular momentum that would add to the angular momentum
of the original mass. In that case, the total angular momentum would indeed
point straight up the z-axis, in exactly the same direction as the angular veloc-
ity. So you may suspect that the relationship between the angular momentum
and the angular velocity (and hence the nature of the inertia tensor) depends on
the symmetry of the object. That suspicion is correct, as you’ll see when you
examine the components of the inertia tensor.
You can begin to understand the components of the inertia tensor by ﬁrst
writing the tensor equation relating angular momentum to angular velocity:
⃗L = ⃗⃗I ⃗ω,
(6.3)
and then using the deﬁnition of angular momentum:
⃗L = ⃗r × ⃗p
= ⃗r × (m⃗v)
= m⃗r × ⃗v
= m⃗r × (⃗ω × ⃗r).
The triple vector product in this expression can be simpliﬁed using the “BAC
minus CAB” rule described in Section 2.4, giving

## Page 175

6.1 The inertia tensor
163
⃗L = m[⃗ω(⃗r ◦⃗r) −⃗r(⃗r ◦⃗ω)].
This is a usable expression for the angular momentum of a single particle,
and you can modify it for use with multiple masses simply by summing (or for
a continuous object by integrating) over all the masses. Thus the expression
you’ll most often encounter will probably look something like this:
⃗L =

i
mi[⃗ω(⃗ri ◦⃗ri) −⃗ri(⃗ri ◦⃗ω)],
(6.4)
where the index i denotes each element of mass of the object.
To see the moment of inertia in this expression, ﬁrst expand the position
vector as ⃗ri = xi ˆı + yi ˆj + zi ˆk and the angular velocity vector as ⃗ω = ωxˆı +
ωy ˆj +ωz ˆk (note that the angular velocity ⃗ω is the same for every mass element
in a rigid body, so it’s not necessary to write ⃗ωi). Thus the expression for
angular momentum is
⃗L =

i
mi[⃗ω(xi ˆı + yi ˆj + zi ˆk) ◦(xi ˆı + yi ˆj + zi ˆk)
−⃗ri(xi ˆı + yi ˆj + zi ˆk) ◦(ωxˆı + ωy ˆj + ωz ˆk)],
and performing the dot products gives
⃗L =

i
mi[⃗ω(x2
i + y2
i + z2
i ) −⃗ri(xiωx + yiωy + ziωz)].
Since the x-component of ⃗ω is ωx and the x-component of ⃗ri is xi, the x-
component of the angular momentum can be written
Lx =

i
mi[ωx(x2
i + y2
i + z2
i ) −xi(xiωx + yiωy + ziωz)]
=

i
mi[ωxx2
i + ωx y2
i + ωxz2
i −x2
i ωx −xi yiωy −xiziωz]
=

i
mi[ωx(y2
i + z2
i ) −xi yiωy −xiziωz].
The y- and z-components come out as
L y =

i
mi[ωy(x2
i + z2
i ) −yi xiωx −yiziωz],
Lz =

i
mi[ωz(x2
i + y2
i ) −zi xiωx −zi yiωy].
These three equations for the components of angular momentum ( ⃗L) may be
written as a single matrix equation:

## Page 176

164
Tensor applications
⎛
⎝
Lx
L y
Lz
⎞
⎠=
⎛
⎝

i mi(y2
i + z2
i ) −
i mi xi yi
−
i mi xizi
−
i mi yi xi

i mi(x2
i + z2
i ) −
i mi yizi
−
i mizi xi
−
i mizi yi

i mi(x2
i + y2
i )
⎞
⎠
⎛
⎝
ωx
ωy
ωz
⎞
⎠.
(6.5)
The elements of the center matrix represent the components of the inertia ten-
sor ( ⃗⃗I ). Note that the dimensions of each element are mass times distance
squared (SI units of kg m2), just as in the case of scalar moment of inertia.
In some texts, you’ll ﬁnd the elements of the inertia tensor written as
something like
Iab = mi(δabr2
i −rarb),
which are the same elements as shown in Eq. 6.5.
The diagonal elements of the inertia tensor are called “moments of inertia”
and the off-diagonal elements are called “products of inertia.” To understand
the physical meaning of each of these elements, recall that the moment of
inertia characterizes an object’s tendency to resist angular acceleration. That
resistance depends not only on the object’s mass, but on the distribution of that
mass relative to the axis of rotation.
Each term Iab tells you how much angular momentum in the a-direction
is produced by rotation about the b-axis. So I11 = Ixx tells you how much
angular momentum the object produces in the x-direction due to rotation about
the x-axis. And I23 = Iyz tells you how much angular momentum the object
produces in the y-direction due to rotation about the z-axis.
How those off-diagonal terms come about is explained below, but you
should ﬁrst take a look at the diagonal terms. In the expression for Ixx, for
each element of mass (mi), the element’s mass is multiplied by the square of
the distance from the x-axis (y2
i +z2
i ). So this is just the three-dimensional ver-
sion of the equation you may have learned for planar rotation that says that the
moment of inertia of a particle is I = mr2, where r is the particle’s distance
from the axis of rotation. Looking down the diagonal of the inertia tensor, you
see the contribution to the x-component of angular momentum due to rotation
about the x-axis, the contribution to the y-component of angular momentum
due to rotation about the y-axis, and the contribution to the z-component of
angular momentum due to rotation about the z-axis. The bottom line is that dis-
tributions of mass that are symmetric about each axis contribute to the diagonal
terms of the moment of inertia matrix.
The off-diagonal elements of the inertia tensor are somewhat different. In
Iyz, for each element of mass (mi), the element’s mass is multiplied by the
product of the element’s y- and z-coordinates (yizi). As explained above, this

## Page 177

6.1 The inertia tensor
165
determines the contribution to the y-component of angular momentum due to
rotation about the z-axis. And when does rotation about the z-axis produce a
y-component of angular momentum? When there’s an asymmetric distribution
of mass about the z-axis, for example as shown with the single particle in Fig-
ure 6.1. Likewise, the Ixy term determines the contribution to the x-component
of angular momentum due to rotation about the y-axis. Such contributions
come from mass distributions that are asymmetric about the y-axis. Hence
distributions of mass that are asymmetric about a given axis contribute to the
off-diagonal terms of the moment of inertia matrix.
To see how this works, consider the ﬁve point masses on the corners and top
of a pyramid as shown in Figure 6.2. To determine the inertia tensor for this
conﬁguration of masses, you simply have to plug the mass and coordinates of
each of the masses into Equation 6.5. If the mass of each of the ﬁve masses is
the same and equal to “m” and the height of the pyramid is equal to the length
of each of the bottom sides (with a value of 2a as shown in Figure 6.2), the Ixx
term is simply
Ixx = m1(y2
1 + z2
1) + m2(y2
2 + z2
2) + m3(y2
3 + z2
3) + m4(y2
4 + z2
4)
+ m5(y2
5 + z2
5)
= m1(a2 + 02) + m2(a2 + 02) + m3[(−a)2 + 02] + m4[(−a)2 + 02]
+ m5(02 + (2a)2)
= 8ma2,
y
x
z
m1
(a,a,0)
m2
m3
(–a,–a,0)
m4
(a,–a,0)
m5 (0,0,2a)
a
2a
a
a
a
(–a,a,0)
Figure 6.2 Five point masses arrayed as a pyramid.

## Page 178

166
Tensor applications
and you should obtain the same result for the other diagonal elements Iyy and
Izz. Moving on to the off-diagonal elements, the Ixy term is
Ixy = −m1x1y1 −m2x2y2 −m3x3y3 −m4x4y4 −m5x5y5
= −m1(a)(a) −m2(−a)(a) −m3(−a)(−a) −m4(a)(−a) −m5(0)(0)
= −m(2a2 −2a2) = 0,
which is the same as all other off-diagonal elements. Thus the matrix repre-
senting the inertia tensor for the conﬁguration shown in Figure 6.2 is
⃗⃗I =
⎛
⎝
8ma2
0
0
0
8ma2
0
0
0
8ma2
⎞
⎠.
There’s a great deal of information in the components of this inertia tensor.
The fact that the off-diagonal elements are all zero means that the selected x-,
y-, and z-axes are “principal axes” for this object and choice of origin, and
the moments of inertia are “principal moments” of the object. When an object
rotates about one of the principal axes, the angular momentum vector and the
angular velocity vector are parallel. This is an indication of the object’s sym-
metry. In this case, the fact that all three principal moments are equal means
that this object qualiﬁes as a “spherical top” (in Mechanics, “top” refers to any
rigid rotating object). And for a spherical top, any three mutually orthogonal
axes are principal axes.
If the height of mass m5 above the plane of the other four masses is increased
to twice its original height (so that its z-coordinate becomes 4a instead of 2a),
the greater distance from the x- and y-axes increases the moment of inertia
about those axes, so that the inertia tensor becomes
⃗⃗I =
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
⎠.
Of course, the distance of m5 from the z-axis remains zero irrespective of its
height, so this mass is not contributing to the component Izz in either case, and
that component remains the same. Now that only two of the principal moments
of inertia are equal, the object is no longer a spherical top, and has become a
“symmetric top” (and if all three principal moments were different, the object
is called an “asymmetric top”). One ﬁnal bit of terminology: if one of the
principal moments of an object is zero and the other two are equal to one
another, the object is called a “rotor.”
Another way to change the inertia tensor of this object is to ﬁddle with the
masses of the particles. If, for example, you double the mass of m5 from its

## Page 179

6.1 The inertia tensor
167
original value of m to 2m, while leaving the other four masses the same, the
inertia tensor becomes
⃗⃗I =
⎛
⎝
12ma2
0
0
0
12ma2
0
0
0
8ma2
⎞
⎠.
As expected, there’s no change in the Izz component since m5 doesn’t
contribute to that moment.
Now consider what will happen to the inertia tensor if you rotate the coor-
dinate axes. Remember, the inertia tensor is determined for a given location of
the origin and a given orientation of the coordinate axes, so it seems reasonable
to expect a change in the components if the coordinate axes are rotated.
To test this, imagine rotating the coordinate axes counter-clockwise about
the x-axis, as shown in Figure 6.3. In this ﬁgure, you’re looking down the
x-axis toward the origin, so the y- and z-axes appear tilted (they’re labeled
y′ and z′ to distinguish them from the original y- and z-axes). In this case,
the rotation angle is approximately 30◦. Figure 6.3(a) shows that the axes
have rotated while the masses remained in their original positions, while Fig-
ure 6.3(b) shows the view you would get if you tilted your head to make the
z′-axis vertical and y′-axis horizontal.
What effect might this have on the inertia tensor? To determine that, you’ll
need to know the coordinates of each of the masses in the new (rotated) coordi-
nate system (that is, you need to know x′, y′, and z′ for each mass). Fortunately,
Chapter 4 should have given you some idea of how to do that by using a rota-
tion matrix to convert between the original and rotated coordinates. In this
case, that rotation matrix is given by
y′
z′
m1
m2
m3
m4
m5
2a
a
a
y′
z′
m1
m2
m3
m4
m5
2a
a
a
(a)
(b)
Figure 6.3 Coordinate axes rotated 30◦anti-clockwise around x-axis.

## Page 180

168
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
1
0
0
0
cos θ
sin θ
0
−sin θ
cos θ
⎞
⎠
⎛
⎝
x
y
z
⎞
⎠.
(6.6)
If you go back to the original masses (all ﬁve masses equal to mass m)
and original height of m5 (which is 2a above the xy plane) and then apply this
rotation, you should ﬁnd the following values for the components of the matrix
representing the inertia tensor:
⃗⃗I =
⎛
⎝
8ma2
0
0
0
8ma2
0
0
0
8ma2
⎞
⎠.
If you’re suprised to ﬁnd that there’s no change from the original inertia ten-
sor (the one without the rotation), remember that the symmetry of this object
makes it a spherical top, which means that any set of three orthogonal axes will
be principal axes. So tilting the axes should not have caused any change in the
inertia tensor.
That sounds reasonable enough, but if you compare the location of the
masses in Figure 6.3 to the single-mass case shown in Figure 6.1, doesn’t it
also seem reasonable to expect that m5 will produce a component of angular
momentum in the −y-direction (as the single mass did in Figure 6.1)?
Yes, it does. And, in fact, mass m5 does indeed produce a component of
angular momentum in the −y-direction. To demonstrate that, just set the other
four masses to zero and calculate the inertia tensor for m5 alone (don’t forget
that the coordinate axes are rotated). You should get
⃗⃗I =
⎛
⎝
4ma2
0
0
0
3ma2
−1.73ma2
0
−1.73ma2
ma2
⎞
⎠.
So there it is: Iyz (which represents the y-component of angular momentum
produced by rotation around the z-axis) is clearly not zero. But why did you
get zero for all the off-diagonal elements when you ﬁrst calculated the inertia
tensor for the pyramid with tilted coordinate axes? The answer is that the other
four masses also have something to say about the inertia tensor. To isolate their
contribution to Iyz, try setting the mass of m5 to zero and leaving the other four
masses equal to m. The inertia tensor should then be
⃗⃗I =
⎛
⎝
4ma2
0
0
0
5ma2
1.73ma2
0
1.73ma2
7ma2
⎞
⎠.

