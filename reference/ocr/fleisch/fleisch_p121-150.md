<!-- source-pdf: FleischVectorsAndTensors.pdf | pages 121-150 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 121–150

## Page 121

4.3 Basis-vector vs. component transformations
109
 New basis
vectors

=
⎛
⎝
Direct
transformation
matrix
⎞
⎠
 Original basis
vectors

.
(4.19)
Comparing this to Eq. 4.14 should help you understand that transforma-
tion matrices can be used for two different but related operations: ﬁnding the
components of the same vector in a new coordinate system or ﬁnding the
components of a different vector (such as a new basis vector) in the original
coordinate system. The next section presents a comparison of these two types
of transformation matrix.
4.3 Basis-vector vs. component transformations
Since Eq. 4.14 and Eq. 4.19 both involve transformation matrices, it’s natural
to wonder how those transformation matrices might be related. You can ﬁnd a
clue to that relationship by comparing the transformation matrix in Eq. 4.7
(pertaining to component change due to a coordinate-axis rotation through
angle θ) with that of Eq. 4.15 (pertaining to basis-vector rotation through angle
θ). Extracting the transformation matrix from each of those equations gives:
From Eq. 4.7:

cos(θ)
sin(θ)
−sin(θ)
cos(θ)

↖
Transformation matrix for ﬁnding compo-
nents of same vector as coordinate system
is rotated through angle θ
From Eq. 4.15:
 cos(θ)
−sin(θ)
sin(θ)
cos(θ)

↖
Transformation matrix for ﬁnding new
basis vectors by rotating original basis vec-
tors through angle θ

## Page 122

110
Covariant and contravariant vector components
Multiplying these two matrices reveals the nature of the relationship
between them:

cos(θ)
sin(θ)
−sin(θ)
cos(θ)
  cos(θ)
−sin(θ)
sin(θ)
cos(θ)

=
 1
0
0
1

.
This means that in this case the component-transformation matrix is the inverse
of the basis-vector transformation matrix (since multiplying a matrix by its
inverse produces the identity matrix). The fact that in this case the transpose of
the transformation matrix is equal to its inverse means that this transformation
matrix is “orthogonal” (converting from one Cartesian coordinate system into
a different one).
In light of the inverse relationship between the basis-vector transformation
matrix and the vector-component transformation matrix, you might say that in
this case the vector components transform inversely to or “against” the man-
ner in which the basis vectors transform (provided that you remember that by
“components transform” you mean ﬁnding the components of the same vec-
tor in the new coordinate system, and by “basis vectors transform” you mean
rotating the basis vectors to point along different coordinate axes).
You should also remember that rotation of Cartesian coordinate axes is only
one among many possible forms of transformation. In general, any time you
choose to switch from one set of basis vectors to another, you must consider
the effect of your choice of new basis vectors on the components of the vectors
in your system. How the matrix that transforms the original basis vectors into
the new ones relates to the matrix that converts the vector components depends
on the type of component you’re using to represent the vector.
If you’re surprised to learn that there can be more than one type of compo-
nent for a given vector, you should consider a coordinate system in which
the axes are not perpendicular to one another. You can learn about such
“non-orthogonal” coordinate systems in the next section.
4.4 Non-orthogonal coordinate systems
In Cartesian coordinate systems, there’s no chance for ambiguity when you
consider the process of “projection” of a vector onto a coordinate axis. Using
the light source and shadow approach described in Chapter 1, you simply imag-
ine a source of light shining on the vector and the shadow produced by that
vector on one of the coordinate axes, as in Figure 1.6. In two-dimensional
Cartesian coordinates, the direction of the light may be speciﬁed in one of two
equivalent ways: parallel to one of the axes (actually antiparallel since the light

## Page 123

4.4 Non-orthogonal coordinate systems
111
Light rays
parallel
to y-axis
Light rays
parallel
to x-axis
Shadow cast
by vector A on
x-axis
Shadow cast
by vector A
on y-axis
x
y
y
x
A
A
Figure 4.10 Projections using light sources parallel to x- and y-axes.
shines back toward the origin), or perpendicular to the other axis. For example,
in Figure 1.6(a), you’re saying exactly the same thing if you describe the light
as shining “antiparallel to the y-axis” or “perpendicular to the x-axis.”
Now imagine a two-dimensional coordinate system in which the x- and
y-axes are not perpendicular to one another.4 In such cases, the process of
projecting a vector onto one of the coordinate axes takes on an additional com-
plication. Should the light sources shine (anti-) parallel to the coordinate axes,
as in Figure 4.10, or perpendicular to the axes, as in Figure 4.11?
In each case, a “projection” of the vector is formed onto one of the coordi-
nate axes, but those projections may have quite different lengths, as you can
see by comparing the lengths of the “shadows” cast in Figure 4.10 to those in
Figure 4.11.
You may certainly be forgiven for thinking “So what?” when confronted
with these differing projections. Does it really matter that there are two ways
to project a vector onto an axis in non-orthogonal coordinate systems?
One indication that the type of projection does matter comes about if you
attempt to use vector addition to form vector ⃗A from the projection compo-
nents using the rules of vector addition. As you can see in Figure 4.12, that
process works perfectly if you use the parallel-projection components but fails
miserably when you attempt to use the perpendicular-projection components.
4 This is not just an academic exercise; non-orthogonal coordinate axes turn up quite naturally in
problems in relativity, ﬂuid dynamics, and other areas.

## Page 124

112
Covariant and contravariant vector components
Light rays
perpendicular
to x-axis
Light rays
perpendicular
to y-axis
Shadow cast
by vector A
on x-axis
Shadow cast
by vector A
on y-axis
A
A
y
x
x
y
Figure 4.11 Projections using light sources perpendicular to x- and y-axes.
x
y
A
Components formed
by parallel projection
add to give vector A
x
y
A
Components formed
by perpendicular proj-
ection do not add to
give vector A
(b)
(a)
Figure 4.12 Vector addition of components formed by parallel and perpen-
dicular projection.
This may cause you to wonder why the perpendicular-projection components
are called “components” at all.
Another way to appreciate the signiﬁcance of the difference between paral-
lel and perpendicular projections is to consider how the components formed by
these two types of projection transform between coordinate systems. As you’ll
see later in this chapter, the components formed by projections perpendicular
to the coordinate axes transform between coordinate systems using the direct
transformation matrix that is also used to form the new basis vectors in the
new coordinate system, while the components formed by projections parallel

## Page 125

4.5 Dual basis vectors
113
to the coordinate axes transform between coordinate systems using the inverse
transformation matrix. This behavior has caused the perpendicular-projection
components to traditionally be called the “covariant” components of the vec-
tor, while the parallel-projection components are called the “contravariant”
components of the vector. Of course, for orthogonal coordinate systems, the
direction parallel to one of the coordinate axes is exactly the same as the direc-
tion perpendicular to other axes, so in that case the covariant and contravariant
components of a vector are identical, and no distinction is needed.
To learn why the covariant values are called “components,” and, much more
importantly, to understand why covariant and contravariant components are
meaningful quantities and how they may be used to write physical laws that do
not depend on the reference frame of the observer, you should ﬁrst understand
the concept of dual basis vectors. You can read about such basis vectors in the
next section.
4.5 Dual basis vectors
For non-orthogonal coordinate systems, it’s clear from geometric considera-
tions such as those illustrated in Figure 4.12 that the perpendicular projections
of a vector onto the coordinate axes do not form “components” in the way
that parallel projections do; the perpendicular projections simply don’t add up
as vectors to give the original vector. But to truly understand the process of
“adding up” components as vectors, you have to think about the role of the
basis vectors in that addition. To see how that works for parallel projections,
take a look at the basis vectors ⃗e1 and ⃗e2 pointing along the (non-orthogonal)
coordinate axes in Figure 4.13 and the projections of vector ⃗A onto those
directions. In this case, vector ⃗A may be written as
⃗A = Ax ⃗e1 + Ay⃗e2,
(4.20)
where Ax and Ay represent the parallel-projection (contravariant) components
of ⃗A.5
The same approach doesn’t work for the perpendicular-projection (covari-
ant) components Ax and Ay, as you can tell by looking at the lengths of the
projections in Figure 4.12(b); it’s clear that those two “components” multiplied
by the basis vectors ⃗e1 and ⃗e2 do not add up to give ⃗A. So it’s reason-
able to wonder if there are alternative basis vectors that would allow the
5 The use of superscripts for the “x” and “y” in the contravariant components Ax and Ay is
deliberate and is the standard notation for distinguishing these contravariant components from
the covariant components Ax and Ay.

## Page 126

114
Covariant and contravariant vector components
Light rays
parallel
to y-axis
Light rays
parallel
to x-axis
y
x
x
A
A
Axe1
Aye2
e1
e2
y
Figure 4.13 Parallel-projection components and basis vectors.
perpendicular-projection components to form a vector in a manner analogous
to Eq. 4.20. Happily, there are, and those alternative basis vectors are called
“reciprocal” or “dual” basis vectors.
Dual basis vectors have two deﬁning characteristics. The ﬁrst is that each
one must be perpendicular to all original basis vectors with different indices.
So if you call the dual basis vectors ⃗e 1 and ⃗e 2 to distinguish them from the
original basis vectors ⃗e1 and ⃗e2, you can be sure that ⃗e 1 is perpendicular to
⃗e2 (and thus perpendicular to the y-axis in this case). Likewise, ⃗e 2 must be
perpendicular to ⃗e1 (and thus perpendicular to the x-axis in this case). The
directions of the dual basis vectors ⃗e 1 and ⃗e 2 are shown in Figure 4.14.
The second deﬁning characteristic for dual basis vectors is that the dot prod-
uct between each dual basis vector and the original basis vector with the same
index must equal one (so ⃗e 1 ◦⃗e1 = 1 and ⃗e 2 ◦⃗e2 = 1). This means that you
can ﬁnd the lengths of the dual basis vectors as long as you know the lengths of
the original basis vectors and the angle between each dual basis vector and the
corresponding original basis vector.6 So to ﬁnd the length of ⃗e 1, you simply
have to multiply the length of the original basis vector ⃗e1 by the cosine of the
angle between ⃗e 1 and ⃗e1 and then take the inverse of the result. Likewise, to
ﬁnd the length of ⃗e 2, multiply the length of the original basis vector ⃗e2 by the
cosine of the angle between ⃗e 2 and ⃗e2 and take the inverse of that result. Thus:
|⃗e 1| =
1
|⃗e1| cos(θ1),
(4.21)
6 Recall from Chapter 2 that ⃗A ◦⃗B = | ⃗A|| ⃗B| cos θ, where θ is the angle between ⃗A and ⃗B.

## Page 127

4.5 Dual basis vectors
115
Light rays
perpendicular
to x-axis
Light rays
perpendicular
to y-axis
y
A
x
x
e1
A
Aye2
e2
y
Axe1
Figure 4.14 Perpendicular-projection components and dual basis vectors.
and
|⃗e 2| =
1
|⃗e2| cos(θ2),
(4.22)
where θ1 is the angle between ⃗e 1 and ⃗e1 and θ2 is the angle between ⃗e 2 and ⃗e2.
With the concept of dual basis vectors in hand, you’re in a position to under-
stand why the perpendicular-projection (covariant) components Ax and Ay
may rightfully be called “components.” The key is that the projections must
be made onto the direction of the dual basis vectors rather than onto the direc-
tions of the original basis vectors. If you do that, then the covariant components
Ax and Ay can be multiplied by the relevant basis vectors and added to give the
original vector ⃗A in the same way as can be done using the parallel-projection
(contravariant) components Ax and Ay. The covariant-component equivalent
to Eq. 4.20 is thus
⃗A = Ax ⃗e 1 + Ay⃗e 2.
(4.23)
As you may have guessed, the use of superscripts to denote the dual basis
vectors ⃗e 1 and ⃗e 2 is not accidental; when these basis vectors are transformed
to a new coordinate system, the inverse transformation matrix is used, as it is
for the contravariant vector components Ax and Ay.
Note that in a two-dimensional coordinate system with orthonormal basis
vectors such as ˆı and ˆj, the dual basis vectors are identical to the original basis
vectors along the coordinate axes. That’s easily understood, because the direc-
tion of each of the dual basis vectors must be perpendicular to the direction
of one of the original basis vectors (and hence must point along the x- and

## Page 128

116
Covariant and contravariant vector components
y-axes). And since the length of the dual basis vectors must equal the inverse
of the length of the original basis vectors times cos(θ) (which is 1/[1 cos(0◦)]
in this case), the dual basis vectors have the same length as well as the same
direction as ˆı and ˆj. So the differences between original and dual basis vectors
disappear for orthonormal coordinate systems, just as the distinctions between
covariant and contravariant components disappear for such systems.
The concept of dual basis vectors can be readily extended to three dimen-
sions, and in that case determination of the length and direction of the dual
basis vectors is most easily done using the dot and cross product between vec-
tors. Speciﬁcally, the three-dimensional dual basis vectors ⃗e 1, ⃗e 2 and ⃗e 3 can
be found from the original basis vectors ⃗e1, ⃗e2, and ⃗e3 using the following
relations:
⃗e 1 =
⃗e2 × ⃗e3
⃗e1 ◦(⃗e2 × ⃗e3),
⃗e 2 =
⃗e3 × ⃗e1
⃗e1 ◦(⃗e2 × ⃗e3),
⃗e 3 =
⃗e1 × ⃗e2
⃗e1 ◦(⃗e2 × ⃗e3).
(4.24)
Each denominator is the triple scalar product of the original basis vectors,
which you may recall from Section 2.3 is the volume of the parallelepiped
formed by those vectors.
In these equations, the cross products in the numerators ensure that the ﬁrst
characteristic of dual basis vectors is met (for example, that ⃗e 1 is perpendicular
to ⃗e2 and to ⃗e3). The triple scalar products in the denominators ensure that the
second characteristic is met (for example, that ⃗e 1 ◦⃗e1 = 1).
The computation of dual basis vectors may seem like a long trek to make
simply to have an alternative way of writing vectors, but there’s a great truth to
be found by comparing Eqs. 4.20 and 4.23. Since these equations describe the
same vector, you may combine them to write
⃗A = Ax ⃗e1 + Ay⃗e2 = Ax ⃗e 1 + Ay⃗e 2,
(4.25)
which serves to emphasize an important fact. If you seek to deﬁne a quantity
(such as vector ⃗A) that remains invariant under a transformation of coordinates,
you have a choice: you can combine superscripted (contravariant) components
with subscripted (covariant) basis vectors, or you can combine subscripted
(covariant) components with superscripted (contravariant) basis vectors. That
should seem reasonable to you, because covariant quantities transform using
a direct transformation matrix, while contravariant quantities use an inverse

## Page 129

4.6 Finding covariant and contravariant components
117
transformation matrix. Multiplying such quantities guarantees that the result is
unaffected by the transformation.
You can see an example of how dual basis vectors and covariant and
contravariant components are determined in the next section.
4.6 Finding covariant and contravariant components
Once you grasp the concept of dual basis vectors in non-orthonormal coordi-
nate systems, ﬁnding the covariant and contravariant components of a vector
is straightforward. As an example, take a look at vector ⃗A in Figure 4.15, with
non-orthogonal basis vectors ⃗e1 and ⃗e2.
Finding the contravariant components A1 and A2 is simply a matter of
parallel-projecting vector ⃗A onto the directions of the original basis vectors
⃗e1 and ⃗e2, as shown in Figure 4.16. A quick visual inspection suggests that
component A1|⃗e1| should be about 2/3 the length of original basis vector ⃗e1,
y
x
(1, 3)
(7, 2)
(4, 0)
e1
A
e2
Figure 4.15 Non-orthogonal basis vectors.
y
x
(1, 3)
(7, 2)
(4, 0)
e1
y
x
(1, 3)
(7, 2)
A1|e1|
(4, 0)
(a)
(b)
e1
e2
e2
A
A
A2|e2|
Figure 4.16 Parallel projections onto original basis vectors.

## Page 130

118
Covariant and contravariant vector components
and component A2|⃗e2| should be about 1.5 times the length of original basis
vector ⃗e2. The values of A1 and A2 can be found by writing the vector equation
⃗A = A1⃗e1 + A2⃗e2,
(4.26)
which can be written as two equations for the components of ⃗A:
Ax = A1e1,x + A2e2,x,
Ay = A1e1,y + A2e2,y.
These two simultaneous equations may readily be solved for A1 and A2 using
the elimination or substitution method (both of which are demonstrated in the
on-line solutions to the problems at the end of this chapter). Another approach
is the matrix method and Cramer’s Rule (described in the matrix-algebra
review on the book’s website). Using this approach, you begin by substituting
the known values for vector ⃗A as well as ⃗e1 and ⃗e2:
 7
2

= A1
 1
3

+ A2
 4
0

,
(4.27)
which may also be written as
 7
2

=
 1
4
3
0
  A1
A2

.
(4.28)
Now use Cramer’s Rule to ﬁnd A1 and A2:
A1 =
 7
4
2
0

 1
4
3
0

= −8
−12 = 0.667,
A2 =
 1
7
3
2

 1
4
3
0

= −19
−12 = 1.583.
(4.29)
These values are consistent with the visual estimates from Figure 4.16.
To use the same process to ﬁnd the perpendicular-projection (covariant)
components A1 and A2, you must ﬁrst determine the length and direction of
the dual basis vectors. You know that the direction of ⃗e 1 must be perpendicular
to that of ⃗e2, and the direction of ⃗e 2 must be perpendicular to that of ⃗e1. As for
the lengths, ﬁrst ﬁnd the lengths of ⃗e1 and ⃗e2:
|⃗e1| =
	
(1)2 + (3)2 = 3.16,
|⃗e2| =
	
(4)2 + (0)2 = 4.00.
(4.30)
Then you can use Eqs. 4.21 and 4.22 to ﬁnd |⃗e 1| and |⃗e 2|, but ﬁrst you have
to ﬁgure out the angle between ⃗e1 and ⃗e 1 (which is θ1) and the angle between
⃗e2 and ⃗e 2 (which is θ2). If you look at Figure 4.17, you should be able to
determine that θ1 = θ2 = arctan(1/3) = 18.43◦, so you have

## Page 131

4.6 Finding covariant and contravariant components
119
y
x
x
(7, 2)
(4, 0)
e2
A
y
(1, 3)
(7, 2)
(b)
(a)
(4, 0)
e1
e2
e2
e1
e1
A
A1|e1|
A2|e2|
θ
θ2
1
2
1
Figure 4.17 Perpendicular projections onto dual basis vectors.
|⃗e 1| =
1
|⃗e1| cos(θ1) =
1
3.16 cos(18.43◦) = 0.333,
|⃗e 2| =
1
|⃗e2| cos(θ2) =
1
4.00 cos(18.43◦) = 0.264.
(4.31)
You can see the (very short) dual basis vectors ⃗e 1 and ⃗e 2 in Figure 4.17.
Note that ⃗e 1 is perpendicular to ⃗e2 and that ⃗e 2 is perpendicular to ⃗e1, and their
lengths are given by Eq. 4.31.
Once you have the dual basis vectors in hand, you’re in a position to ﬁnd
the perpendicular-projection (covariant) components A1 and A2. You can do
this geometrically by continuing the perpendicular-projection lines beyond the
direction lines of ⃗e1 and ⃗e2 and onto the direction lines of ⃗e 1 and ⃗e 2, as shown
in Figure 4.17. The magnitude of vector ⃗A is
| ⃗A| =
	
(7)2 + (2)2 = 7.28,
(4.32)
and the angle between ⃗A and the x-axis is arctan( 2
7) = 15.94◦. Using this
value and θ1 from above, you can determine that the angle between ⃗A and ⃗e1
is 55.62◦and the angle between ⃗A and ⃗e2 is 15.94◦. So the length of ℓ1 in
Figure 4.17(a) is
ℓ1 = | ⃗A| cos(55.62◦) = 4.11,
(4.33)
and
A1|⃗e 1| =
ℓ1
cos(18.43◦) = 4.33,
(4.34)
so A1 = 4.33/0.333 = 13.0.

## Page 132

120
Covariant and contravariant vector components
Using the same approach to ﬁnd A2 from Figure 4.17(b) gives
ℓ2 = | ⃗A| cos(15.94◦) = 7.00,
(4.35)
and
A2|⃗e 2| =
ℓ2
cos(18.43◦) = 7.38,
(4.36)
so A2 = 7.38/0.264 = 28.0.
These results serve as a reminder that when you use non-normalized basis
vectors (that is, basis vectors with magnitude not equal to one), you cannot
equate the lengths of the projections onto the coordinate axes with the value
of a vector’s components. That’s because those projections are the products of
the components with the magnitudes of the basis vectors.
If you prefer the algebraic approach to ﬁnding A1 and A2, you can do that
by proceeding as you did for A1 and A2, although in this case you begin with
⃗A = A1⃗e 1 + A2⃗e 2,
(4.37)
and then substitute the known values for vector ⃗A as well as the x- and y-
components of the dual basis vectors ⃗e 1 and ⃗e 2:
e 1
x = |⃗e 1| cos(90◦) = 0.000,
e 2
x = |⃗e 2| cos(360◦−18.43◦) = 0.250,
e 1
y = |⃗e 1| sin(90◦) = 0.333,
e 2
y = |⃗e 2| sin(360◦−18.43◦) = −0.083.
So
 7
2

= A1

0
0.333

+ A2

0.25
−0.083

.
(4.38)
As before, this may be written as
 7
2

=

0
0.25
0.333
−0.083
  A1
A2

.
(4.39)
Again using Cramer’s Rule to solve for A1 and A2 gives
A1 =
 7
0.25
2
−0.083


0
0.25
0.333
−0.083

= −1.081
−0.083 = 13.0,
A2 =

0
7
0.333
2


0
0.25
0.333
−0.083

= −2.331
−0.083 = 28.0,
(4.40)
as expected from the geometric approach.

## Page 133

4.6 Finding covariant and contravariant components
121
A simpler approach to ﬁnding the contravariant and covariant components
of a vector once you have both the original and dual basis vectors in hand is to
use these relations:
A1 = ⃗A ◦⃗e1 = Axe1,x + Aye1,y
A2 = ⃗A ◦⃗e2 = Axe2,x + Aye2,y,
(4.41)
and
A1 = ⃗A ◦⃗e 1 = Axe1
x + Aye1
y
A2 = ⃗A ◦⃗e 2 = Axe2
x + Aye2
y.
(4.42)
In the current example, this approach gives the covariant components as
A1 = (7, 2) ◦(1, 3) = (7)(1) + (2)(3) = 13,
A2 = (7, 2) ◦(4, 0) = (7)(4) + (2)(0) = 28,
and
A1 = (7, 2) ◦(0, 0.333) = (7)(0) + (2)(0.333) = 0.666,
A2 = (7, 2) ◦(0.250, −0.083) = (7)(0.250) + (2)(−0.083) = 1.58,
in agreement with the geometric and matrix-algebra approaches taken above.
It’s important for you to realize that what you’ve just found are the parallel-
projection (contravariant) and perpendicular-projection (covariant) compo-
nents of vector ⃗A with respect to the original basis vectors ⃗e1 and ⃗e2 and the
dual basis vectors ⃗e 1 and ⃗e 2. So does that mean that ⃗A is a covariant vector or
a contravariant vector?
The answer is neither (or both, if you prefer); it’s not the vector itself that
is contravariant or covariant, it’s the set of components that you form through
its parallel or perpendicular projections. As you read the literature on tensors,
you’re very likely to run into expressions such as “the contravariant vector
⃗A” or “the covariant vector ⃗B,” and what the author generally means is that
the contravariant components of vector ⃗A and the covariant components of
vector ⃗B are being used for the problem (perhaps because they’re simpler).
But you can be sure that like all vectors, ⃗A and ⃗B both have contravariant and
covariant components, and you can ﬁnd them using the techniques described
in this section.7
And if you’re wondering why you might want to go through the effort of
ﬁnding those components, rest assured that the payoff is worth the effort. To
appreciate the value of that payoff, you’ll have to begin thinking of vectors not
just as arrows with a certain length and pointing in a speciﬁed direction, but
rather as members of a class of objects called tensors that have very predictable
7 In Chapter 5, you can learn to move between contravariant and covariant components using the
metric tensor.

## Page 134

122
Covariant and contravariant vector components
(and useful) properties under transformation of coordinates. In that view, the
vectors you’ve been dealing with up to this point have all been tensors of rank
one. Seeing them as such, and understanding what that means, will be made
a great deal easier through the use of a notation called “index notation” and
a convention known as the “Einstein summation convention.” You can read
about index notation and the summation convention in the next section.
4.7 Index notation
You’ve seen the ﬁrst glimmerings of index notation in the earlier section of
this chapter describing coordinate transformations. As you may recall, the
angles between the transformed (rotated) coordinate axes and the original
(non-rotated) axes of a two-dimensional coordinate system were called α11,
α12, α21, and α22. These angles could just as well have been designated αx′x,
αx′y, αy′x, and the like, but there are several good reasons to use the index num-
bers 1, 2, and 3 rather than the letters x, y, and z to refer to coordinate axes
and vector components. One of those reasons is that many problems in physics
and engineering involve a number of dimensions greater than 3, and although
everyone agrees that “4” comes after “3,” a consensus hasn’t been reached on
what comes after “z.” Another reason is that index notation enables the great
convenience of the summation convention that you can read about later in this
section.
Using index notation, the coordinates of a point in three-dimensional
space are written as (x1, x2, x3) or (x1, x2, x3) rather than (x, y, z), and
the components of a vector are written as (A1, A2, A3) or (A1, A2, A3)
rather than (Ax, Ay, Az) or (Ax, Ay, Az). This system is easily extended to
N-dimensional space, in which the coordinates become (x1, x2, . . . , xN) or
(x1, x2, . . . , x N) and the vector components become (A1, A2, . . . , AN) or
(A1, A2, . . . , AN).
Applying this notation to the equation for the transformation of contravariant
vector components produced by a rotation of two-dimensional axes, Eq. 4.6
becomes

A
′1
A
′2

=
 cos (α11)
cos (α12)
cos (α21)
cos (α22)
  A1
A2

.
(4.43)
In three dimensions, this is
⎛
⎜⎝
A
′1
A
′2
A
′3
⎞
⎟⎠=
⎛
⎝
cos (α11)
cos (α12)
cos (α13)
cos (α21)
cos (α22)
cos (α23)
cos (α31)
cos (α32)
cos (α33)
⎞
⎠
⎛
⎝
A1
A2
A3
⎞
⎠.
(4.44)

## Page 135

4.7 Index notation
123
Designating the elements of the transformation matrix a11, a12, a13, and so
forth allows you to write Eq. 4.44 as
A
′1 = a11A1 + a12 A2 + a13A3,
A
′2 = a21A1 + a22 A2 + a23A3,
A
′3 = a31A1 + a32 A2 + a33A3,
(4.45)
or
A
′1 =
3

j=1
a1 j A j,
A
′2 =
3

j=1
a2 j A j,
A
′3 =
3

j=1
a3 j A j.
(4.46)
Allowing “i” to stand for any of the indices 1, 2, or 3 makes this:
A
′i =
3

j=1
ai j A j.
i = 1, 2, 3
(4.47)
As a ﬁnal simpliﬁcation, whenever an index appears twice in the same term,
once as a superscript and once as a subscript (as “ j” does in Eq. 4.47), you can
omit the summation symbol and write simply
A
′i = ai j A j,
(4.48)
in which the reader knows to sum over the repeated index ( j in this case).
Such repeated indices are often called “dummy” indices, since any letter may
be used for that index and the result will be the same.8 It was Albert Einstein
who ﬁrst suggested this summation convention, which he jokingly called his
“great discovery in mathematics.”9 Whatever you call it, this idea certainly has
saved a lot of ink and time since Einstein proposed it in 1916.
Before moving on, you should take a careful look at Eq. 4.48 and make
sure you understand that these few symbols mean exactly the same thing as
the many terms in the three separate equations of Eq. 4.45. They tell you that
8 Unlike the repeated “dummy” indices which indicate summation, i is called a “free” index and
no summation is implied.
9 Pais, A. 1983, Subtle Is the Lord: The Science and the Life of Albert Einstein, Oxford
University Press, Oxford.

## Page 136

124
Covariant and contravariant vector components
each component in the primed coordinate system is a weighted linear combi-
nation of the components in the original (unprimed) coordinate system, with
the transformation matrix elements (ai j) providing the weighting factors for
each term.
And if you want to know the exact meaning of each of those factors in
the transformation of covariant and contravariant vector components, the next
section will help with that.
4.8 Quantities that transform contravariantly
With the convenience of index notation and the summation convention at your
disposal, you should be ready to take the next step in the transition from think-
ing of vectors as quantities with magnitude and direction to understanding why
vectors belong to the class of objects known as tensors. That step begins by
asking the question of how a differential element of length d⃗s transforms from
one coordinate system to another.
In general, the equations relating the coordinates in one system to those in
another do not involve simple linear combinations of coordinate values. For
example, in transforming from spherical (r, θ, φ) to Cartesian (x, y, z) coordi-
nates, it’s not possible to write equations such as x = a11r + a12θ + a13φ,
because x depends on the product of r with the sine of θ and the cosine
of φ. And y and z have similar non-linear relationships to the spherical
coordinates.
If, however, you ask how the differentials of x, y, and z (that is, dx, dy, and
dz) depend on the differentials of r, θ, and φ (that is, dr, dθ, and dφ), you’ll
ﬁnd that on this inﬁnitesimally small scale, dx does depend linearly on dr, dθ,
and dφ (as do dy and dz). So you are able to write
dx = a11dr + a12dθ + a13dφ,
(4.49)
and likewise for dy and dz.
For any two coordinate systems in which a linear relationship exists between
differential length elements, writing the equations which transform between
the systems is straightforward. If you call the differentials of one coordinate
system dx, dy, and dz and the other coordinate system dx′, dy′, and dz′,
the transformation equations from the unprimed to the primed systems come
directly from the rules of partial differentiation, as shown in the left column
below:

## Page 137

4.8 Quantities that transform contravariantly
125
dx′ = ∂x′
∂x dx + ∂x′
∂y dy + ∂x′
∂z dz ⇒dx
′1 = ∂x
′1
∂x1 dx1 + ∂x
′1
∂x2 dx2 + ∂x
′1
∂x3 dx3,
dy′ = ∂y′
∂x dx + ∂y′
∂y dy + ∂y′
∂z dz ⇒dx
′2 = ∂x
′2
∂x1 dx1 + ∂x
′2
∂x2 dx2 + ∂x
′2
∂x3 dx3,
dz′ = ∂z′
∂x dx + ∂z′
∂y dy + ∂z′
∂z dz ⇒dx
′3 = ∂x
′3
∂x1 dx1 + ∂x
′3
∂x2 dx2 + ∂x
′3
∂x3 dx3.
(4.50)
Using the index-notation approach of substituting x1, x2, and x3 for x, y,
and z results in the column shown on the right.10 Putting this into matrix
notation gives
⎛
⎜⎝
dx
′1
dx
′2
dx
′3
⎞
⎟⎠=
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎝
∂x
′1
∂x1
∂x
′1
∂x2
∂x
′1
∂x3
∂x
′2
∂x1
∂x
′2
∂x2
∂x
′2
∂x3
∂x
′3
∂x1
∂x
′3
∂x2
∂x
′3
∂x3
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎠
⎛
⎝
dx1
dx2
dx3
⎞
⎠,
(4.51)
or, using individual equations with summation symbols
dx
′1 =
3

j=1
∂x
′1
∂x j dx j,
dx
′2 =
3

j=1
∂x
′2
∂x j dx j,
dx
′3 =
3

j=1
∂x
′3
∂x j dx j.
If you now allow the letter i to represent each of the numerical values of the
index (1, 2, and 3), this can be written as
dx
′i =
3

j=1
∂x
′i
∂x j dx j.
(4.52)
Since the j index is repeated, a ﬁnal simpliﬁcation results from the Einstein
summation convention, allowing you to write
dx
′i = ∂x
′i
∂x j dx j.
(4.53)
So index notation has allowed the expression in Eq. 4.50, consisting of three
equations with three terms in each, to be written as this single equation. More
importantly, the form of this equation will help you understand why differential
length elements (dxi) are considered to be contravariant quantities.
10 Superscripts are used for the indices because differential length elements transform as
contravariant quantities, as described later in this section.

## Page 138

126
Covariant and contravariant vector components
To gain that understanding, it’s useful to recall Eq. 4.48 from the previous
section:
A
′i = ai j A j,
which tells you that the components of a vector in the primed (transformed)
coordinate system are the weighted linear combination of the components
of that same vector in the unprimed (original) coordinate system. And the
weighting factors ai j are the elements of the transformation matrix.
Now compare Eq. 4.53 to Eq. 4.48. On the left side of both equations,
a primed quantity (dx
′i or A
′i) with free index i appears. On the right
side, both equations contain the product of a factor with free index i and
dummy index j ( ∂x
′i
∂x j or ai j) with the left-side quantity unprimed and with
dummy index j (dx j or A j). And you know that the factor ai j in Eq. 4.48
represents the elements of a transformation matrix for contravariant vector
components between the unprimed and the primed coordinate systems. So
it seems reasonable to conclude that the
∂x
′i
∂x j
terms in Eq. 4.53 can be
seen as the elements of the transformation matrix for the differential length
elements.
So instead of looking at Eq. 4.53 as simply the index-notation version of the
chain rule, you should see it as a transformation equation that takes differential
length elements from the unprimed to the primed coordinate system (just as
Eq. 4.48 does for the contravariant components of vector ⃗A).
And here’s the important insight: the
∂x
′i
∂x j terms are not only the ele-
ments of a transformation matrix from the unprimed to the primed coordinate
system, they’re also the components of the basis vectors tangent to the orig-
inal (unprimed) coordinate axes, expressed in the new (primed) coordinate
system.11
Furthermore, you know that basis vectors tangent to the original coordinate
axes are the covariant basis vectors described earlier. And since contravariant
vector components combine with covariant basis vectors to produce invariant
quantities, differential length elements must transform as contravariant vector
components. This is the reason that the indices are written as superscripts in
Eqs. 4.51 through 4.53; the differential length element is the “prototype” of
contravariant vector components.
Using index notation and representing the components of the basis vec-
tors as ∂x
′i
∂x j , you should now understand why the transformation equation for
contravariant components of vector ⃗A is often written as
11 If you’re wondering how partial derivatives can represent basis vectors, you should review
Section 2.6 of Chapter 2.

## Page 139

4.9 Quantities that transform covariantly
127
A
′i = ∂x
′i
∂x j A j.
(4.54)
Many authors present this as the deﬁnition of contravariant components.
To see how this notation works in practice, consider the transformation
from polar (r, θ) to two-dimensional Cartesian (x, y) coordinates. In this case,
x
′1 = x, x
′2 = y, x1 =r, and x2 = θ, and you know that x =r cos(θ) and
y =r sin(θ). So what are the weighting factors (that is, the elements of the
transformation matrix) in this case? Taking the appropriate derivatives, you
ﬁnd that
∂x
′1
∂x1 = ∂x
∂r = cos(θ),
∂x
′2
∂x1 = ∂y
∂r = sin(θ),
(4.55)
∂x
′1
∂x2 = ∂x
∂θ = −r sin(θ),
∂x
′2
∂x2 = ∂y
∂θ = r cos(θ).
(4.56)
Are these really the components of the tangent vectors to the original (r, θ)
coordinate axes (that is, are they pointing along those axes)? You can see that
they are by writing these terms as components in the primed coordinate system
(Cartesian in this case):
⃗e1 = ∂x
′1
∂x1 ˆı + ∂x
′2
∂x1 ˆj = cos(θ)ˆı + sin(θ) ˆj,
(4.57)
⃗e2 = ∂x
′1
∂x2 ˆı + ∂x
′2
∂x2 ˆj = −r sin(θ)ˆı + r cos(θ) ˆj.
(4.58)
The ﬁrst of these expressions is a vector pointing radially outward (along the
ˆr-direction in polar coordinates) and the second is a vector pointing perpendic-
ular to the radial direction (along the ˆθ-direction).12 This demonstrates that the
partial derivatives in Eq. 4.53 do indeed represent components of the original
(unprimed) covariant basis vectors expressed in the new (primed) coordinate
system.
4.9 Quantities that transform covariantly
If the differential length element of the previous section serves as the “proto-
type” for quantities that transform as contravariant vector components, you
may be wondering if there’s a similar “prototype” for covariant quantities.
You can answer that question by considering a quantity such as the change
in temperature with distance (degrees per meter) over some region, which
you may recognize from Chapter 2 as the gradient of that quantity. Unlike
12 These basis vectors can be understood in terms of the non-Cartesian unit vectors discussed in
Section 1.5 of Chapter 1.

## Page 140

128
Covariant and contravariant vector components
the differential length element, which has dimensions directly related to the
coordinate dimensions, quantities such as the gradient have dimensions that
include the inverse of the coordinate dimensions (per unit length rather than
length in the case of spatial coordinates). This dimensional consideration sug-
gests that the gradient may be a good candidate for the prototype of quantities
that transform as covariant vector components. And index notation makes this
easy to see.
Imagine a scalar quantity such as temperature or density whose value at
various positions is given by the function f (x, y, z); the rate of change of
that quantity is ∂f
∂x in the x-direction, ∂f
∂y in the y-direction, and ∂f
∂z in the z-
direction. It’s reasonable to ask how these rates of change vary if the coordinate
system is changed. To answer that question, you can proceed as we did for the
differential length element, using the chain rule for partial derivatives and then
employing index notation as follows:
∂f
∂x′ = ∂f
∂x
∂x
∂x′ + ∂f
∂y
∂y
∂x′ + ∂f
∂z
∂z
∂x′
⇒∂f
∂x
′1 = ∂f
∂x1
∂x1
∂x
′1 + ∂f
∂x2
∂x2
∂x
′1 + ∂f
∂x3
∂x3
∂x
′1 ,
∂f
∂y′ = ∂f
∂x
∂x
∂y′ + ∂f
∂y
∂y
∂y′ + ∂f
∂z
∂z
∂y′
⇒∂f
∂x
′2 = ∂f
∂x1
∂x1
∂x
′2 + ∂f
∂x2
∂x2
∂x
′2 + ∂f
∂x3
∂x3
∂x
′2 ,
∂f
∂z′ = ∂f
∂x
∂x
∂z′ + ∂f
∂y
∂y
∂z′ + ∂f
∂z
∂z
∂z′
⇒∂f
∂x
′3 = ∂f
∂x1
∂x1
∂x
′3 + ∂f
∂x2
∂x2
∂x
′3 + ∂f
∂x3
∂x3
∂x
′3 .
As before, you can write this as a matrix equation
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎝
∂f
∂x
′1
∂f
∂x
′2
∂f
∂x
′3
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎠
=
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎜⎝
∂x1
∂x
′1
∂x2
∂x
′1
∂x3
∂x
′1
∂x1
∂x
′2
∂x2
∂x
′2
∂x3
∂x
′2
∂x1
∂x
′3
∂x2
∂x
′3
∂x3
∂x
′3
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎟⎠
⎛
⎜⎜⎜⎜⎜⎜⎜⎜⎜⎝
∂f
∂x1
∂f
∂x2
∂f
∂x3
⎞
⎟⎟⎟⎟⎟⎟⎟⎟⎟⎠
,
(4.59)

## Page 141

4.9 Quantities that transform covariantly
129
or as individual equations using the summation symbol:
∂f
∂x
′1 =
3

j=1
∂x j
∂x
′1
∂f
∂x j ,
∂f
∂x
′2 =
3

j=1
∂x j
∂x
′2
∂f
∂x j ,
∂f
∂x
′3 =
3

j=1
∂x j
∂x
′3
∂f
∂x j .
Once again employing i as the free index gives
∂f
∂x
′i =
3

j=1
∂x j
∂x
′i
∂f
∂x j ,
(4.60)
and the Einstein summation convention simpliﬁes this to
∂f
∂x
′i = ∂x j
∂x
′i
∂f
∂x j .
(4.61)
Comparing this to the equivalent expression for the differential length element
(Eq. 4.53) suggests that once again the vector components in the primed coor-
dinate system are the weighted linear combination of the components in the
original coordinate system. But in this case the elements of the transformation
matrix ( ∂x j
∂x′i ) are the inverse of those in the transformation of the differen-
tial length elements (which are ∂x
′i
∂x j ). And just as in that case the ∂x
′i
∂x j terms
represent the components of vectors that point along the original coordinate
axes, in this case the
∂x j
∂x′i terms represent the components of vectors that
are perpendicular to the original coordinate surfaces. Hence in this case the
weighting factors are the components of the (contravariant) dual basis vectors,
which means that the components of the gradient vector transform as covari-
ant components. Of course, for orthonormal coordinate systems the lengths
and directions of the original and dual basis vectors are exactly the same, and
there is no difference between the covariant and contravariant vector com-
ponents. In non-orthonormal coordinate systems, this distinction is critically
important.
Again using index notation and representing the dual basis vectors as ∂x j
∂x′i ,
you probably won’t ﬁnd it surprising that many authors deﬁne the covari-
ant components of vector ⃗A as components that transform according to the
equation
A′
i = ∂x j
∂x
′i Ai.
(4.62)
At this point you should be convinced that vectors are more than just lit-
tle arrows with magnitude and direction; they’re quantities that transform in
certain ways between coordinate systems. Speciﬁcally, every vector has both
contravariant and covariant components that transform in predictable ways.

## Page 142

130
Covariant and contravariant vector components
The contravariant components vary in the opposite manner to the basis vec-
tors pointing along the original coordinate axes, and the covariant components
vary in the same manner as those basis vectors. Most importantly, by combin-
ing the vector’s contravariant components with the original basis vectors, or
by combining the vector’s covariant components with the dual basis vectors,
the resulting quantity (the vector itself) remains invariant under all coordinate
transformations. It is this characteristic that qualiﬁes vectors to join the ranks
of tensors.
Understanding the distinction between contravariant and covariant vector
components is extremely helpful in understanding tensors, because vectors are
tensors. Speciﬁcally, since all the components of a vector can be delineated
using only a single index, vectors are tensors of rank one. Under this deﬁnition,
scalars are tensors of rank zero, since scalars are single numbers and require
no index at all. And of what use are tensors of rank two and higher? You’ll
encounter those in Chapter 5.
4.10 Chapter 4 problems
4.1 Write the inverse transformation matrix for a 70◦rotation of the 2-D
Cartesian coordinate axes and the indirect transformation matrix for the
rotation of a vector through an angle of 70◦degrees. Show that the
product of these two transformation matrices is the identity matrix.
4.2 Use the inverse transformation matrix from Problem 4.1 to ﬁnd the
components of vector ⃗A = 2ˆı + 5.5 ˆj in the rotated coordinate system.
4.3 Use the direct transformation matrix from Problem 4.1 to rotate the origi-
nal coordinate basis vectors ˆı and ˆj by 70◦, so they point along the rotated
axes.
4.4 Use a direct transformation matrix to rotate vector ⃗A from Problem 4.2
through an angle of −70◦, and compare the x- and y-components of
the rotated vector (in the original coordinate system) to the x′- and
y′-components of the unrotated vector in the rotated coordinate system.
4.5 Use the dot product of the original vector ⃗A with the rotated basis vectors
( ⃗A ◦ˆı′ and ⃗A ◦ˆj′) to ﬁnd the components of ⃗A in the rotated coordinate
system.
4.6 For vector ⃗A = −5ˆı +6 ˆj and basis vectors ⃗e1 = ˆı +2 ˆj and ⃗e2 = −2ˆı −ˆj,
ﬁnd the contravariant components ⃗A1 and ⃗A2.
4.7 Find the dual basis vectors ⃗e 1 and ⃗e 2 for the basis vectors ⃗e1 and ⃗e2 of
Problem 4.6.
4.8 Find the covariant components ⃗A1 and ⃗A2 for vector ⃗A of Problem 4.6.

## Page 143

4.10 Chapter 4 problems
131
4.9 Use the subsitution method and the elimination method to solve the two
simultaneous equations that result from vector Eq. 4.26.
4.10 Show that the elements of the Cartesian-to-polar transformation matrix
are the components of the basis vectors tangent to the original (Cartesian)
coordinate axes.

## Page 144

5
Higher-rank tensors
The previous chapter contains several ideas that are important to a full
understanding of tensors. The ﬁrst is that any vector may be represented by
components that transform between coordinate systems in one of two ways.
“Covariant” components transform in the same manner as the original basis
vectors pointing along the coordinate axes, and “contravariant” components
transform in the inverse manner of those basis vectors.1 The second main idea
is that coordinate basis vectors are tangent to the coordinate axes, and that
there also exist reciprocal or dual basis vectors that are perpendicular to the
coordinate axes; these dual basis vectors transform inversely to the coordinate
basis vectors. The third idea is that combining contravariant components with
original basis vectors and combining covariant components with dual basis
vectors produces a result that is invariant under coordinate transformation. That
result is the vector itself, and the vector is the same no matter which coordinate
system you use for its components.
This chapter extends the concepts of covariance and contravariance beyond
vectors and makes it clear that scalars and vectors are members of the class of
objects called “tensors.”
5.1 Deﬁnitions (advanced)
In the basic deﬁnitions of Chapter 1, scalars, vectors, and tensors were deﬁned
by the number of directions involved: zero for scalars, one for vectors, and
more than one for tensors.2 Now that you’ve seen the concepts of components,
basis vectors, and the transformation properties of each, you’re in a position
1 The prototype of a vector expressed in contravariant components is the displacement vector,
and the prototype of a vector expressed in covariant components is the gradient vector.
2 Note that specifying one direction in 3-dimensional space requires two angles.
132

## Page 145

5.1 Deﬁnitions (advanced)
133
to understand the more-advanced deﬁnitions of scalars, vectors, and tensors.
Speciﬁcally:
A scalar is a single value with no directional indicator that represents a
quantity that does not vary as the coordinate system is changed.
So for a scalar with value φ in one coordinate system and value φ′ in another
coordinate system, you can be certain that the quantity represented by φ (com-
bined with the relevant unit) and φ′ (combined with its unit) is the same no
matter which system you use to represent it. Thus 1 inch and 2.54 centimeters
represent the same quantity of length.
A vector is an array of three values (in 3-D space) called “vector compo-
nents” that combine with directional indicators (“basis vectors”) to form a
quantity that does not vary as the coordinate system is changed.
So vector ⃗A represents the same entity whether it is expressed using contravari-
ant components Ai or covariant components Ai:
⃗A = Ai ⃗ei = Ai ⃗e i,
where ⃗ei represents a covariant basis vector and ⃗e i represents a contravariant
basis vector.
In transforming between coordinate systems, a vector with contravariant
components A j in the original (unprimed) coordinate system and contravariant
components A
′i in the new (primed) coordinate system transforms as
A
′i = ∂xi′
∂x j A j,
where the ∂xi′
∂x j terms represent the components in the new coordinate system
of the basis vectors tangent to the original axes.
Likewise, for a vector with covariant components A j in the original
(unprimed) coordinate system and covariant components A′
i in the new
(primed) coordinate system, the transformation equation is
A′
i = ∂x j
∂xi′ A j,
where the ∂x j
∂xi′ terms represent the components in the new coordinate system
of the (dual) basis vectors perpendicular to the original axes.

## Page 146

134
Higher-rank tensors
A tensor of rank n is an array of 3n values (in 3-D space) called “tensor com-
ponents” that combine with multiple directional indicators (basis vectors) to
form a quantity that does not vary as the coordinate system is changed.
From this deﬁnition, you can see that a second-rank tensor has 32 = 9 compo-
nents in three-dimensional space. Note that a tensor of rank 0 is a scalar and a
tensor of rank 1 is a vector.
There is no standard notation for tensors; you may see a tensor represented
with double overhead arrows (such as ⃗⃗T ) or with a tilde or two-directional
arrow above or below (such as ˜T , ←→
T or T
←→). Many authors don’t bother with
arrows or tildes and represent tensors simply by writing the letter signifying the
tensor with “placeholder” indices to indicate the contravariant and covariant
rank of the tensor (such as T i j or T a
b ).
5.2 Covariant, contravariant, and mixed tensors
You should by this point understand that the expression
A
′i = ∂xi′
∂x j A j
(5.1)
presents the contravariant components of vector ⃗A in the transformed (primed)
coordinate system (A
′i) as a weighted sum of the components of ⃗A in the origi-
nal (unprimed) coordinate system (A j). The weighting factors ( ∂xi′
∂x j ) are simply
the elements of the transformation matrix from the unprimed to the primed
coordinate systems, and those elements represent the components of the basis
vectors tangent to the original coordinate axes. With that understanding, a
tensor expression such as
A
′i j = ∂xi′
∂xk
∂x j′
∂xl Akl
(5.2)
should have some recognizable elements. As you can probably surmise, in
this expression A
′i j are the contravariant tensor components in the new coor-
dinate system, Akl are the contravariant tensor components in the original
coordinate system, and ∂xi′
∂xk as well as ∂x j′
∂xl are elements of the transforma-
tion matrix between the original and new coordinate systems. And just as in
Eq. 5.1, the elements of the direct transformation matrix also represent the
basis vectors tangent to the original coordinate axes. But in the vector expres-
sion Eq. 5.1 each component pertains to a single basis vector, whereas the

## Page 147

5.3 Tensor addition and subtraction
135
components in the tensor expression Eq. 5.2 pertain to two basis vectors. This
should seem reasonable to you, since the basic deﬁnitions in Chapter 1 state
that vectors involve a single direction while higher-rank tensors involve two or
more directions.
The vector Eq. 5.1 involves contravariant components (as indicated by the
use of superscripted indices in A
′i and A j), but you know that an equivalent
expression exists for the covariant components:
A′
i = ∂x j
∂xi′ A j.
(5.3)
In this equation, the covariant components of vector ⃗A in the transformed
(primed) coordinate system (A′
i) are expressed as a weighted sum of the covari-
ant components of ⃗A in the original (unprimed) coordinate system (A j). In this
case, the weighting factors ( ∂x j
∂xi′ ) are the elements of the inverse transformation
matrix from the unprimed to the primed coordinate systems, and those ele-
ments represent the dual basis vectors perpendicular to the original coordinate
axes.
Extending this to a second-rank tensor gives a transformation equation such
as this:
A′
i j = ∂xk
∂xi′
∂xl
∂x j′ Akl.
(5.4)
In this expression, A′
i j are the covariant tensor components in the new coordi-
nate system, Akl are the covariant tensor components in the original coordinate
system, and ∂xk
∂xi′ as well as
∂xl
∂x j′ are elements of the transformation matrix
between the original and new coordinate systems. And much as in Eq. 5.3,
the elements of the transformation matrix represent the dual basis vectors
perpendicular to the original coordinate axes.
As you may have anticipated, another possibility exists for second-rank
tensors:
A
′i
j = ∂xi′
∂xk
∂xl
∂x j′ Ak
l ,
(5.5)
in which the tensor ⃗⃗A is represented by one contravariant and one covariant
index; each uses the transformation matrix appropriate for its type.
5.3 Tensor addition and subtraction
As you may recall from Section 1.4, two or more vectors can be added simply
by adding their corresponding components. Hence a single vector equation
such as

## Page 148

136
Higher-rank tensors
⃗C = ⃗A + ⃗B,
(5.6)
actually consists of three equations (in three-dimensional space), since each
component of the resultant vector ⃗C must be the sum of the corresponding
components of vectors ⃗A and ⃗B:
Cx = Ax + Bx,
Cy = Ay + By,
Cz = Az + Bz.
(5.7)
Higher-order tensors can be added using the same process, provided that the
tensors to be added have the same structure (that is, they are the same order and
have the same number of covariant indices and the same number of contravari-
ant indices). The result of tensor addition is also a tensor, and the resultant
tensor has the same structure as each of the tensors that are added:
Ci j = Ai j + Bi j,
Ci j = Ai j + Bi j,
Ci
j = Ai
j + Bi
j.
(5.8)
Note that each of these expressions represents more than one equation; the
exact number depends on the number of values that each index may take on.
Note also that you can add tensors with any number of covariant and con-
travariant indices, as long as the tensors being added have the same number of
each type of index.
To see that the result of adding two tensors ﬁts the deﬁnition of a tensor, con-
sider how the tensor components Ai
j and Bi
j transform to another coordinate
system:
A
′k
l = ∂x
′k
∂xi
∂x j
∂xl′ Ai
j,
B
′k
l = ∂x
′k
∂xi
∂x j
∂xl′ Bi
j.
(5.9)
Hence
A
′k
l + B
′k
l = ∂x
′k
∂xi
∂x j
∂x
′l Ai
j + ∂x
′k
∂xi
∂x j
∂x
′l Bi
j
= ∂x
′k
∂xi
∂x j
∂x
′l (Ai
j + Bi
j).

## Page 149

5.4 Tensor multiplication
137
If you compare this last expression to the expression for the transformation of
the tensor components Ci
j to the primed coordinate system
C
′k
l = ∂x
′k
∂xi
∂x j
∂x
′l Ci
j,
you’ll see that the addition of Ai
j and Bi
j does produce an object Ci
j that meets
the transformation requirements for a tensor.
Subtraction of tensors is equally straightforward; you simply subtract the
corresponding components rather than adding them:
Ci j = Ai j −Bi j,
Ci j = Ai j −Bi j,
Ci
j = Ai
j −Bi
j,
(5.10)
and the result of tensor subtraction is also a tensor, as you can see in the
problems at the end of this chapter.
5.4 Tensor multiplication
As described in Chapter 2, there are several different ways to multiply vectors –
the scalar (dot) product and vector (cross) product both take two vectors as
inputs and produce a result that depends on the magnitudes and directions of
those two vectors. Not mentioned in that chapter was another form of vector
product called the “outer” product between a column vector ( ⃗A) and a row
vector ( ⃗B), which operates like this:
⃗A ⊗⃗B =
⎛
⎝
A1
A2
A3
⎞
⎠(B1B2B3) =
⎛
⎝
A1B1
A1B2
A1B3
A2B1
A2B2
A2B3
A3B1
A3B2
A3B3
⎞
⎠.
Note that the outer product of two rank-1 tensors (vectors) is a rank-2 tensor,
formed simply by multiplying the individual components of the two vectors.
The outer product is indicated with the ⊗symbol in some texts; others just
write the two vectors or tensors next to one another, such as Ai B j = Ci j.
The outer-product operation may also be performed on higher-order tensors:
Ai
j Bk
lm = Cik
jlm.
In this case, the outer product of a rank-2 tensor and a rank-3 tensor is a rank-5
tensor. This illustrates the fact that the covariant rank of the outer-product ten-
sor is the sum of the covariant ranks of the input tensors, and the contravariant

## Page 150

138
Higher-rank tensors
rank of the outer-product tensor is the sum of the contravariant ranks of the
input tensors.
The result of the outer-product operation is easily shown to be a tensor by
considering how tensors ⃗⃗A, ⃗⃗B, and ⃗⃗C transform from the unprimed to the
primed coordinate system. The transform of tensors ⃗⃗A and ⃗⃗B is given by
A
′n
o = ∂x
′n
∂xi
∂x j
∂x
′o Ai
j,
B
′ p
qr = ∂x
′ p
∂xk
∂xl
∂x
′q
∂xm
∂x
′r Bk
lm.
Multiplying these expressions gives
A
′n
o B
′ p
qr = ∂x
′n
∂xi
∂x j
∂x
′o Ai
j
∂x
′ p
∂xk
∂xl
∂x
′q
∂xm
∂x
′r Bk
lm
= ∂x
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
′q
∂xm
∂x
′r Ai
j Bk
lm.
So if Ai
j Bk
lm = Cik
jlm and A
′n
o B
′ p
qr = C
′np
oqr, then
C
′np
oqr = ∂x
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
′q
∂xm
∂x
′r Cik
jlm,
(5.11)
and the result of the outer product operation does indeed meet the transforma-
tion requirements for a tensor.
Another way to multiply tensors is called the “inner product,” which you can
think of as a generalization of the scalar or dot product discussed in Section 2.1.
As described in that section, the dot product between two vectors produces a
scalar result, so you might expect the inner product between two tensors to
produce a tensor of lower rank. That’s exactly right, but to understand how it
happens, you ﬁrst need to understand the process of tensor contraction.
To contract a tensor, simply set one contravariant index equal to a covariant
index (or vice versa) and then sum over the repeated index. This leads to a
tensor with a rank that is two less than the rank of the tensor with which you
started.
To see how this works in practice, consider the rank-4 tensor Ci j
kl. To contract
this tensor in the second and third indices, set the index k equal to the index j,
resulting in
Ci j
jl = Ci1
1l + Ci2
2l + Ci3
3l = Di
l ,
assuming that the indices j and k run from 1 to 3. Note that the rank is reduced
by two because you made one index the same as another (reducing the rank

