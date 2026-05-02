<!-- source-pdf: FleischVectorsAndTensors.pdf | pages 31-60 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 31–60

## Page 31

1.5 Non-Cartesian unit vectors
19
The following equations relate the Cartesian to the cylindrical unit vectors:
ˆr = cos(φ)ˆı + sin(φ) ˆj
ˆφ = −sin(φ)ˆı + cos(φ) ˆj
ˆz = ˆz.
(1.14)
In spherical coordinates a point P is speciﬁed by r, θ, φ where r represents
the distance from the origin, θ is the angle measured from the z-axis toward
the xy plane, and φ is the angle measured from the x-axis (or xz plane) to the
constant-φ plane containing point P. With the z-axis up, θ is sometimes called
the zenith angle and φ the azimuth angle. You can determine the spherical
coordinates r, θ, and φ, from x, y, and z using the following equations:
r =

x2 + y2 + z2
θ = arccos

z
	
x2 + y2 + z2

φ = arctan

 y
x

.
(1.15)
And you can ﬁnd x, y, and z from r, θ, and φ using:
x = r sin(θ) cos(φ)
y = r sin(θ) sin(φ)
z = r cos(θ).
(1.16)
In spherical coordinates, a vector at the point P is speciﬁed in terms of three
mutually perpendicular components with unit vectors perpendicular to the
sphere of radius r, perpendicular to the plane through the z-axis at angle φ,
and perpendicular to the cone of angle θ. The unit vectors (ˆr, ˆθ, ˆφ) form a
right-handed set, and are related to the Cartesian unit vectors as follows:
ˆr = sin(θ) cos(φ)ˆı + sin(θ) sin(φ) ˆj + cos(θ)ˆk
ˆθ = cos(θ) cos(φ)ˆı + cos(θ) sin(φ) ˆj −sin(θ)ˆk
ˆφ = −sin(φ)ˆı + cos(φ) ˆj.
(1.17)
You may be asking yourself “Do I really need all these different unit vec-
tors?” Well, need may be a bit strong, but your life will certainly be easier
if you’re trying to describe motion along a line of constant longitude on a
spherical planet (the ˆθ direction) or the direction of a magnetic ﬁeld around a

## Page 32

20
Vectors
current-carrying wire (the ˆφ direction). You’ll ﬁnd some examples of that in
the problems at the end of this chapter.
1.6 Basis vectors
If you think about the unit vectors ˆı, ˆj, and ˆk and vector components such as
Axˆı, Ay ˆj, and Az ˆk, you may realize that any vector in our three-dimensional
Cartesian coordinate system can be made up of three components, each one
telling you how many steps to take in the direction of one of the coordi-
nate axes. Since those steps may be large or small, in the positive or negative
direction, you can reach any point in the space containing these vectors. Little
wonder, then, that ˆı, ˆj, and ˆk are one example of “basis vectors” in this space;
combined with appropriate magnitudes, they form the basis of any vector in
the space.
And you don’t need to use only these particular vectors to make up any
vector in this space – you can easily imagine using three vectors that are twice
as long as the unit vectors ˆı, ˆj, and ˆk, as shown in Figure 1.13(a). Although
the vector components would change if you switched to these longer basis
vectors, you’d have no trouble using them to make up any vector within the
space. Speciﬁcally, if the unit vectors were twice as long, the values of Ax, Ay,
and Az would have to be only half as big to reach a given point in space.
You might even think of using three non-orthogonal, non-unit vectors such
as the vectors ⃗e1, ⃗e2, and ⃗e3 in Figure 1.13(b) as your basis vectors. Of course,
if you were to select three coplanar vectors (that is, vectors lying in the same
plane), you’d quickly ﬁnd that scaling and combining those vectors allows you
(a)
1
2
1
2
1
e3
x
y
z
1
2
1
2
1
2k
x
y
z
2i
2j
(b)
e2
e1
Figure 1.13 Alternative basis vectors.

## Page 33

1.6 Basis vectors
21
to reach any point within that plane, but all points outside the plane would be
unreachable. But as long as one of the three vectors is not coplanar with the
other two, then appropriate scaling and combining will get you to any point
in the space, and the vectors ⃗e1, ⃗e2, and ⃗e3 form a perfectly usable basis set
(mathematicans say that they “span” the vector space).
You can ensure that three vectors are not coplanar by requiring them to be
“linearly independent,” which means that no two of the vectors may be scaled
and combined to give the third, and no two are collinear (that is, lying along
the same line or parallel to one another). This is often stated as the requirement
that the only way to scale and combine the three vectors and get zero as the
result is to scale each of the vectors by zero. In other words, for three linearly
independent vectors ⃗e1, ⃗e2, and ⃗e3, the equation
A⃗e1 + B⃗e2 + C⃗e3 = 0
(1.18)
can only be true if A = B = C = 0.
So as long as you pick three linearly independent vectors, you have a viable
set of basis vectors. And if you choose three non-coplanar vectors ⃗e1, ⃗e2, and
⃗e3 of non-unit length, it’s quite simple to form unit vectors from these vec-
tors. Since dividing a vector by a positive scalar changes its length but not its
direction, you simply divide each vector by its magnitude:
ˆe1 = ⃗e1
|⃗e1|
ˆe2 = ⃗e2
|⃗e2|
ˆe3 = ⃗e3
|⃗e3|.
(1.19)
The concepts described in this section may be used to construct an inﬁnite
number of bases, but the most common are the “orthonormal” bases such as
ˆı, ˆj, and ˆk. These bases are called “ortho” because they’re orthogonal (per-
pendicular to one another) and “normal” because they are normalized to a
magnitude of one. Orthonormal bases will get you through the majority of
problems you’re likely to face.
One last fact about basis vectors in various coordinate systems will serve you
very well if you study physics and engineering beyond the basic level, espe-
cially if your studies include the tensors discussed in Chapters 4 through 6.
That fact is this: basis vectors that point along the axes of one coordi-
nate system may be described in another coordinate system using partial

## Page 34

22
Vectors
derivatives.8 Speciﬁcally, imagine that you’re converting from spherical to
rectangular coordinates. The basis vector along the original spherical (r) axis
can be written in the Cartesian (x, y, and z) system as
⃗er = ∂x
∂r ˆı + ∂y
∂r ˆj + ∂z
∂r
ˆk
= sin θ cos φ ˆı + sin θ sin φ ˆj + cos θ ˆk.
Likewise, the ⃗eθ and ⃗eφ basis vectors can be written as
⃗eθ = ∂x
∂θ ˆı + ∂y
∂θ ˆj + ∂z
∂θ
ˆk
= r cos θ cos φ ˆı + r cos θ sin φ ˆj −r sin θ ˆk,
⃗eφ = ∂x
∂φ ˆı + ∂y
∂φ ˆj + ∂z
∂φ
ˆk
= −r sin θ sin φ ˆı + r sin θ cos φ ˆj.
Notice that these basis vectors are not all unit vectors (because their magni-
tudes are not all equal to one), nor do they all have the same dimensions (⃗er
is dimensionless, but ⃗eθ and ⃗eφ have dimensions of length). Neither of these
characteristics disqualiﬁes these as basis vectors, and you can always turn them
into unit vectors by dividing by their magnitudes (take a look at the problems
at the end of this chapter and their on-line solutions if you want to see how this
works).
In general, if the coordinates of the original system are called x1, x2, and x3
(these were r, θ, and φ in the example just discussed), and the coordinates of
the new system are called x′
1, x′
2, and x′
3 (these were x, y, and z in the example),
then the basis vectors along the original coordinate axes can be written in the
new system as
⃗e1 = ∂x′
1
∂x1
⃗e ′
1 + ∂x′
2
∂x1
⃗e ′
2 + ∂x′
3
∂x1
⃗e ′
3,
⃗e2 = ∂x′
1
∂x2
⃗e ′
1 + ∂x′
2
∂x2
⃗e ′
2 + ∂x′
3
∂x2
⃗e ′
3,
⃗e3 = ∂x′
1
∂x3
⃗e ′
1 + ∂x′
2
∂x3
⃗e ′
2 + ∂x′
3
∂x3
⃗e ′
3.
(1.20)
In other words, the partial derivatives ∂x′
1
∂x1 ⃗e ′
1, ∂x′
2
∂x1 ⃗e ′
2, and ∂x′
3
∂x1 ⃗e ′
3 are the compo-
nents of the ﬁrst original (unprimed) basis vector expressed in the new (primed)
8 If you’re not familiar with partial derivatives or need a refresher, you’ll ﬁnd one in the next
chapter.

## Page 35

1.7 Chapter 1 problems
23
coordinate system. For this reason, you’ll ﬁnd that some authors deﬁne basis
vectors in terms of partial derivatives.
These relationships will prove to be extremely valuable in the study of
coordinate-system transformation and tensor analysis, so ﬁle them away if your
studies include those topics.
1.7 Chapter 1 problems
1.1 (a) If | ⃗B| = 18 m and ⃗B points along the negative x-axis, what are Bx
and By?
(b) If Cx = −3 m/s and Cy = 5 m/s, ﬁnd the magnitude of ⃗C and the
angle that ⃗C makes with the positive x-axis.
1.2 Vector ⃗A has magnitude of 11 m/s2 and makes an angle of 65 degrees
with the positive x-axis, and vector ⃗B has Cartesian components Bx = 4
m/s2 and By = −3 m/s2. If vector ⃗C = ⃗A + ⃗B,
(a) Find the x- and y-components of ⃗C;
(b) What are the magnitude and direction of ⃗C?
1.3 Imagine that the y-axis points north and the x-axis points east.
(a) If you travel a distance r = 22 km in a straight line from the origin in a
direction 35 degrees south of west, what is your position in Cartesian
(x, y) coordinates?
(b) If you travel 6 miles due south from the origin and then turn west and
travel 2 miles, how far from the origin and in what direction is your
ﬁnal position?
1.4 What are the x- and y-components of the polar unit vectors ˆr and ˆθ when
(a) θ = 180 degrees?
(b) θ = 45 degrees?
(c) θ = 215 degrees?
1.5 Cylindrical coordinates
(a) If r = 2 meters, φ = 35 degrees, and z = 1 meter, what are x, y, and
z?
(b) If (x, y, z) = (3, 2, 4) meters, what are (r, φ, z)?
1.6 (a) In cylindrical coordinates, show that ˆr points along the x-axis
if φ = 0.
(b) In what direction is ˆφ if φ = 90 degrees?
1.7 (a) In spherical coordinates, ﬁnd x, y, and z if r = 25 meters, θ = 35
degrees, and φ= 110 degrees.
(b) Find (r, θ, φ) if (x, y, z) = (8, 10, 15) meters.

## Page 36

24
Vectors
1.8 (a) For spherical coordinates, show that ˆθ points along the negative
z-axis if θ = 90 degrees.
(b) If φ also equals 90 degrees, in what direction are ˆr and ˆφ?
1.9 As you can read in Chapter 3, the magnetic ﬁeld around a long, straight
wire carrying a steady current I is given in spherical coordinates by the
expression ⃗B = μ0I
2π R ˆφ, where μ0 is a constant and R is the perpendicular
distance from the wire to the observation point. Find an expression for ⃗B
in Cartesian coordinates.
1.10 If ⃗e1 = 5ˆı −3 ˆj + 2ˆk, ⃗e2 = ˆj −3ˆk, and ⃗e3 = 2ˆı + ˆj −4ˆk, what are the
unit vectors ˆe1, ˆe2, and ˆe3?

## Page 37

2
Vector operations
If you were tracking the main ideas of Chapter 1, you should realize that
vectors are representations of physical quantities – they’re mathematical tools
that help you visualize and describe a physical situation. In this chapter, you
can read about a variety of ways to use those tools to solve problems. You’ve
already seen how to add vectors and how to multiply vectors by a scalar (and
why such operations are useful); this chapter contains many other “vector oper-
ations” through which you can combine and manipulate vectors. Some of these
operations are simple and some are more complex, but each will prove useful
in solving problems in physics and engineering. The ﬁrst section of this chapter
explains the simplest form of vector multiplication: the scalar product.
2.1 Scalar product
Why is it worth your time to understand the form of vector multiplication
called the scalar or “dot” product? For one thing, forming the dot product
between two vectors is very useful when you’re trying to ﬁnd the projection
of one vector onto another. And why might you want to do that? Well, you
may be interested in knowing how much work is done by a force acting on an
object. The ﬁrst instinct of many students is to think of work as “force times
distance” (which is a reasonable starting point). But if you’ve ever taken a
course that went a bit deeper than the introductory level, you may remember
that the deﬁnition of work as force times distance applies only to the special
case in which the force points in exactly the same direction as the displacement
of the object. In the more general case in which the force acts at some angle to
the direction of the displacement, you have to ﬁnd the component of the force
along the displacement. That’s one example of exactly what the dot product
can do for you, and you’ll ﬁnd more in the problems at the end of this chapter.
25

## Page 38

26
Vector operations
How do you go about computing the dot product between two vectors? Well,
if you know the Cartesian components of each vector (call the vectors ⃗A and
⃗B), you can use
⃗A ◦⃗B = Ax Bx + Ay By + Az Bz.
(2.1)
Or if you know the angle θ between the vectors,
⃗A ◦⃗B = | ⃗A|| ⃗B| cos θ,
(2.2)
where | ⃗A| and | ⃗B| represent the magnitude (length) of the vectors ⃗A and ⃗B.1
Note that the dot product between two vectors gives a scalar result (just a single
value, no direction).
To grasp the physical signiﬁcance of the dot product, consider vectors ⃗A
and ⃗B which differ in direction by angle θ, as shown in Figure 2.1a. For these
vectors, the projection of ⃗A onto the direction of ⃗B is | ⃗A| cos(θ), as shown in
Figure 2.1b. Multiplying this projection by the length of ⃗B gives | ⃗A|| ⃗B| cos(θ).
Thus the dot product ⃗A ◦⃗B represents the projection of ⃗A onto the direction of
⃗B multiplied by the length of ⃗B. The scalar result of this operation is exactly
the same as the result of ﬁnding the projection of ⃗B onto the direction of ⃗A
and then multiplying that value by the length of ⃗A. Hence the order of the
two vectors in the dot product is irrelevant; ⃗A ◦⃗B gives the same result as
⃗B ◦⃗A.
The scalar product can be particularly useful when one of the vectors in
the product is a unit vector. That’s because the length of a unit vector is by
deﬁnition equal to one, so a scalar product such as ⃗A ◦ˆk ﬁnds the projection of
vector ⃗A onto the direction of ˆk (the z-direction) multiplied by the magnitude of
ˆk (which is one). Thus to ﬁnd the component of any vector in a given direction,
you can simply form the dot product between that vector and the unit vector in
B
θ
The projection of A onto B:  |A| cosθ
times the length of B:                   x|B|
gives the dot product A  B: |A|B|cosθ
A
A
B
(b)
(a)
θ
Figure 2.1 Two vectors and their scalar product.
1 The equivalence between Equations 2.1 and 2.2 is demonstrated in the problems at the end of
this chapter.

## Page 39

2.2 Cross product
27
the desired direction. It’s quite likely you’ll come across problems in physics
and engineering in which you have a vector ( ⃗A) and you wish to know the
component of that vector that’s perpendicular to a speciﬁed surface; if you
know the unit normal vector (ˆn) for the surface, the scalar product ⃗A ◦ˆn gives
you that perpendicular component of ⃗A.
The scalar product is also useful in ﬁnding the angle between two vectors.
To understand how that works, consider the two expressions for the dot product
given in Eqs. 2.1 and 2.2. Since
⃗A ◦⃗B = | ⃗A|| ⃗B| cos θ = Ax Bx + Ay By + Az Bz,
(2.3)
then dividing both sides by the product of the magnitudes of ⃗A and ⃗B gives
cos(θ) = Ax Bx + Ay By + Az Bz
| ⃗A|| ⃗B|
or
θ = arccos
 Ax Bx + Ay By + Az Bz
| ⃗A|| ⃗B|

.
(2.4)
So if you wish to ﬁnd the angle between two vectors ⃗A = 5ˆı −2 ˆj + 4ˆk and
⃗B = 3ˆı + ˆj + 7ˆk, you can use Eq. 2.4 to ﬁnd
θ = arccos

(5)(3) + (−2)(1) + (4)(7)
	
(5)2 + (−2)2 + (4)2	
(3)2 + (1)2 + (7)2

= arccos

41
√
45
√
59

= 37.3◦.
One ﬁnal note about the scalar product: any unit vector dotted with itself
gives a result of 1 (since, for example, ˆı ◦ˆı = |ˆı||ˆı| cos(0◦) = (1)(1)(1) = 1),
and the dot product between two different orthogonal unit vectors gives a result
of zero (since, for example, ˆı ◦ˆj = |ˆı|| ˆj| cos(90◦) = (1)(1)(0) = 0).
2.2 Cross product
Another way to multiply two vectors is to form the “cross product” between
them. Unlike the dot product, which gives a scalar result, the cross prod-
uct results in another vector. Why bother learning this form of vector
multiplication? One reason is that the cross product is just what you need when
you’re trying to ﬁnd the result of certain physical processes, such as applying a
force at the end of a lever arm or ﬁring a charged particle into a magnetic ﬁeld.

## Page 40

28
Vector operations
Computing the cross product between two vectors is only slightly more com-
plicated than ﬁnding the dot product. If you know the Cartesian components
of both vectors, the cross product is given by
⃗A × ⃗B = (Ay Bz −Az By)ˆı
+ (Az Bx −Ax Bz) ˆj
+ (Ax By −Ay Bx)ˆk,
(2.5)
which can be written as
⃗A × ⃗B =

ˆı
ˆj
ˆk
Ax
Ay
Az
Bx
By
Bz

.
(2.6)
If you haven’t seen determinants before and you need some help getting from
Eq. 2.6 to Eq. 2.5, you can ﬁnd an explanation of how this works on the book’s
website.
The direction of the vector formed by the cross product of ⃗A and ⃗B is
perpendicular to both ⃗A and ⃗B (that is, perpendicular to the plane contain-
ing both ⃗A and ⃗B), as shown in Figure 2.2. Of course, there are two directions
perpendicular to this plane, so how do you know which one corresponds to
the direction of ⃗A × ⃗B? The answer is provided by the “right-hand rule,”
which you can invoke by opening your right hand and making your thumb
perpendicular to the direction of your ﬁngers in the plane of your palm. Now
imagine using your right palm and ﬁngers to push the ﬁrst vector ( ⃗A in this
case) into the direction of the second vector ( ⃗B in this case) through the
smallest angle. As you push, your thumb shows you the direction of the cross
product.2
A very important difference between the dot product and the cross product is
that the order of the vectors is irrelevant for the dot product but matters greatly
for the cross product. You can see this by imagining the cross product ⃗B × ⃗A in
Figure 2.2. In order to push vector ⃗B into vector ⃗A with your right palm, you’d
have to turn your hand upside-down (that is, with your thumb pointing down).
And since your thumb shows you the direction of the cross product, you can
see that ⃗B × ⃗A points in the opposite direction from ⃗A × ⃗B. That means that
⃗A × ⃗B = −⃗B × ⃗A,
(2.7)
2 Some people ﬁnd it easier to imagine aligning the ﬁngers of your (open) right hand with the
direction of the ﬁrst vector, and then curling your ﬁngers toward the second vector. Or you can
point your right index ﬁnger in the direction of the ﬁrst vector and your right middle ﬁnger in
the direction of the second vector. Whether you use the pushing, curling, or pointing approach,
your right thumb shows you the direction of the cross product.

## Page 41

2.2 Cross product
29
A
A × B
Plane containing both A and B
A
B
B
A × B
θ
Figure 2.2 Direction of the cross product ⃗A × ⃗B.
B
The length of the cross product
equals the area of the parallelogram
formed by vectors A and B
Parallelogram
A × B
Height is
|B|sin(θ)
A
Plane containing both A and B
θ
Figure 2.3 The cross product as area.
since the negative of a vector is just a vector of the same magnitude in the
opposite direction. A quick method of computing the magnitude of the cross
product is to use
| ⃗A × ⃗B| = | ⃗A|| ⃗B| sin(θ),
(2.8)
where | ⃗A| is the magnitude of ⃗A, | ⃗B| is the magnitude of ⃗B, and θ is the angle
between ⃗A and ⃗B.3
One way to picture the length and direction of the cross product is illustrated
in Figure 2.3. Just as the dot product involves the projection of one vector onto
another, the cross product also has a geometrical interpretation. In this case,
the magnitude of the cross product between two vectors is proportional to the
area of the parallelogram formed with those two vectors as adjacent sides. As
you may recall, the area of a parallelogram is just its base times its height, and
3 The equivalence of Eq. 2.8 and the magnitude of the expression in Eq. 2.5 is demonstrated in
the problems at the end of this chapter.

## Page 42

30
Vector operations
in this case the height of the parallelogram is | ⃗B| sin(θ) and the length of the
base is | ⃗A|. That makes the area of the parallelogram equal to | ⃗A|| ⃗B| sin(θ),
exactly as given in Eq. 2.8.
So if the angle between two vectors ⃗A and ⃗B is zero or 180◦(that is, if ⃗A
and ⃗B are parallel or antiparallel), the cross product between them is zero. And
as the angle between ⃗A and ⃗B approaches 90◦or 270◦, the magnitude of the
cross product increases, reaching a maximum value of | ⃗A|| ⃗B| when the vectors
are perpendicular.
Using the deﬁnition of the cross product and the right-hand rule, you should
be able to convince yourself that the following relations are true:
ˆı × ˆı = 0
ˆı × ˆj = ˆk
ˆj × ˆı = −ˆk
ˆj × ˆj = 0
ˆj × ˆk = ˆı
ˆk × ˆj = −ˆı
ˆk × ˆk = 0
ˆk × ˆı = ˆj
ˆı × ˆk = −ˆj.
(2.9)
Applying these relations term-by-term to the product of ⃗A = Axˆı + Ay ˆj + Az ˆk
and ⃗B = Bxˆı + By ˆj + Bz ˆk should help you understand where Eqs. 2.6 and
2.5 come from (and if you need some help making that work out, there’s a
problem on this at the end of this chapter, with the full solution on the book’s
website).
Applications of the cross product include torque problems (in which ⃗τ =
⃗r × ⃗F) and magnetic force problems (in which ⃗FB = q⃗v × ⃗B); you can ﬁnd
examples of these in the chapter-end problems.
2.3 Triple scalar product
Once you understand the dot product and cross product described in the previ-
ous two sections, you may be wondering if it’s possible to combine these two
vector operations. Happily, it’s not only possible, it’s actually useful to do so.
After all, you can deﬁne all the mathematical operations you’d like, but unless
those operations result in something that you can apply to solve problems,
you’d have to leave them in the “curiosity” ﬁle. You’ve seen how the dot prod-
uct ﬁnds employment when projections of vectors onto speciﬁed directions are
needed and when work is to be calculated, and how the cross product can be
called into action when torques and magnetic forces are at play. But does it
make sense to combine the dot and cross product operations in a manner such
as ⃗A◦( ⃗B× ⃗C)? Yes it does.4 This is called the “triple scalar product” or “scalar
triple product” and it has several useful applications.
4 But ( ⃗A ◦⃗B) × ⃗C makes no sense, since ( ⃗A ◦⃗B) gives a scalar, and you can’t cross that scalar
into ⃗C.

## Page 43

2.3 Triple scalar product
31
The mathematics of this operation are straightforward; you know that
⃗B × ⃗C = (ByCz −BzCy)ˆı
+ (BzCx −BxCz) ˆj
+ (BxCy −ByCx)ˆk,
(2.10)
and from Eq. 2.1 you also know that
⃗A ◦⃗B = Ax Bx + Ay By + Az Bz,
so combining the dot and cross product gives
⃗A ◦

⃗B × ⃗C

= Ax(ByCz −BzCy)
+ Ay(BzCx −BxCz)
+ Az(BxCy −ByCx).
(2.11)
A handy way to write this is
⃗A ◦

⃗B × ⃗C

=

Ax
Ay
Az
Bx
By
Bz
Cx
Cy
Cz

.
(2.12)
One geometrical interpretation of the triple scalar product can be under-
stood with the help of Figure 2.4. In this ﬁgure, vectors ⃗A, ⃗B, and ⃗C represent
the sides of a parallelepiped. The area of the base of this parallelepiped is
| ⃗B × ⃗C|, as in Figure 2.3, and its height is equal to | ⃗A| cos(φ), where φ
is the angle between ⃗A and the direction of ⃗B × ⃗C. That means that the
volume of the parallelepiped (the height times the area of the base) must be
| ⃗A| cos(φ)(| ⃗B × ⃗C|). Writing this as | ⃗A|| ⃗B × ⃗C| cos(φ) should help you see
that this has the same form as the deﬁnition of the dot product in Eq. 2.2 and
is therefore just ⃗A ◦( ⃗B × ⃗C).
Plane containing both B and C
Parallelepiped
Height is
|A|cos(φ)
B × C
A
Area of base
is B × C
B
C
φ
Figure 2.4 The triple scalar product as volume.

## Page 44

32
Vector operations
Hence the triple scalar product ⃗A◦( ⃗B× ⃗C) may be interpreted as the volume
of the parallelepiped formed by vectors ⃗A, ⃗B, and ⃗C. You should note that the
triple product will give a positive result so long as the vectors ⃗A, ⃗B, and ⃗C
form a right-handed system (that is, pushing ⃗A into ⃗B with the palm of your
right hand gives a direction onto which ⃗C projects in a positive sense (likewise
for pushing ⃗B into ⃗C and pushing ⃗C into ⃗A).
Seeing the relationship between the triple scalar product of three vectors and
the volume formed by those vectors makes it easy to understand why the triple
scalar product may be used as a test to determine whether three vectors are
coplanar (that is, whether all three lie in the same plane). Just imagine how
the parallelepiped in Figure 2.4 would look if vectors ⃗A, ⃗B, and ⃗C were all
in the same plane. In that case, the height of the parallelepiped would be zero
and the projection of ⃗A onto the direction of ⃗B × ⃗C would be zero, which
means the triple product ⃗A ◦( ⃗B × ⃗C) would have to be zero. Stated another
way, if the projection of ⃗A onto the direction of ⃗B × ⃗C is not zero, then ⃗A
cannot lie in the same plane as ⃗B and ⃗C. Thus
⃗A ◦( ⃗B × ⃗C) = 0
(2.13)
is both a necessary and a sufﬁcient condition for vectors ⃗A, ⃗B, and ⃗C to be
coplanar.
Equating ⃗A ◦( ⃗B × ⃗C) to the volume of the parallelepiped formed by vectors
⃗A, ⃗B, and ⃗C should also help you see that any cyclic permutation of the vectors
(such as ⃗B ◦( ⃗C × ⃗A) or ⃗C ◦( ⃗A × ⃗B)) gives the same result for the triple
scalar product, since the volume of the parallelepiped is the same in each of
these cases. Some authors describe this as the ability to interchange the dot
and the cross without affecting the result (since ( ⃗A × ⃗B) ◦⃗C is the same as
⃗C ◦( ⃗A × ⃗B)).
One application in which the triple scalar product ﬁnds use is the determi-
nation of reciprocal vectors, as explained in the sections in Chapter 4 dealing
with covariant and contravariant components of vectors.
2.4 Triple vector product
The triple scalar product described in the previous section is not the only use-
ful way to multiply three vectors. An operation such as ⃗A × ( ⃗B × ⃗C) (called
the “triple vector product”) comes in very handy when you’re dealing with
certain problems involving angular momentum and centripetal acceleration.
Unlike the triple scalar product, which produces a scalar result (since the sec-
ond operation is a dot product), the triple vector product yields a vector result

## Page 45

2.4 Triple vector product
33
(since both operations are cross products). You should note that ⃗A × ( ⃗B × ⃗C)
is not the same as ( ⃗A × ⃗B) × ⃗C; the location of the parentheses matters greatly
in the triple vector product. The triple vector product is somewhat tedious to
calculate by brute force, but thankfully a simpliﬁed expression exists:
⃗A × ( ⃗B × ⃗C) = ⃗B( ⃗A ◦⃗C) −⃗C( ⃗A ◦⃗B).
(2.14)
After all the previous discussion of the various ways in which vectors can be
multiplied, you can be forgiven for thinking that the right side of this equation
looks a bit strange, with no circle or cross between ⃗B and ⃗A ◦⃗C or between ⃗C
and ⃗A ◦⃗B. Just remember that ⃗A ◦⃗C and ⃗A ◦⃗B are scalars, so the expressions
in parentheses in Eq. 2.14 are simply scalar multipliers of vectors ⃗B and ⃗C.
Does this mean that the result of the operation ⃗A × ( ⃗B × ⃗C) is a vector that is
some linear combination of the second and third vectors in the triple product?
That’s exactly what it means, as you can see by considering Figure 2.5.
In this ﬁgure, you can see the vector ⃗B × ⃗C pointing straight up, perpendic-
ular to the plane containing vectors ⃗B and ⃗C. Now imagine forming the cross
product of vector ⃗A with vector ⃗B× ⃗C by pushing ⃗A into the direction of ⃗B× ⃗C
with the palm of your right hand. The result of this operation, labelled vector
⃗A × ( ⃗B × ⃗C), is back in the plane containing vectors ⃗B and ⃗C. To understand
why this is true, consider the fact that the vector that results from the operation
⃗B × ⃗C must be perpendicular to the plane containing ⃗B and ⃗C. If you now
cross ⃗A into that vector, the resulting vector must be perpendicular to both ⃗A
and to ( ⃗B × ⃗C), which puts it back in the plane containing vectors ⃗B and ⃗C.
And if the vector result of the operation ⃗A × ( ⃗B × ⃗C) is in the same plane as
vectors ⃗B and ⃗C, then it must be a linear combination of those two vectors.
You can remember Eq. 2.14 as the “BAC minus CAB” rule so long as you
remember to write the members of the triple product in the correct sequence
Plane containing both B and C
(but not A)
A × (B × C)
(same plane as B and C)
B × C
B
C
A
Figure 2.5 Vectors involved in the triple vector product ⃗A × ( ⃗B × ⃗C).

## Page 46

34
Vector operations
( ⃗A, ⃗B, ⃗C) with the parentheses around the last two vectors. To see where this
comes from, you can simply use the deﬁnition of the cross product (Eq. 2.6) to
write
⃗A × ( ⃗B × ⃗C) =

ˆı
ˆj
ˆk
Ax
Ay
Az
( ⃗B × ⃗C)x
( ⃗B × ⃗C)y
( ⃗B × ⃗C)z

.
(2.15)
And from Equation 2.5 you know that
⃗B × ⃗C = (ByCz −BzCy)ˆı
+ (BzCx −BxCz) ˆj
+ (BxCy −ByCx)ˆk.
(2.16)
Substituting these terms into Eq. 2.15 gives
⃗A × ( ⃗B × ⃗C) =

ˆı
ˆj
ˆk
Ax
Ay
Az
(ByCz −BzCy)
(BzCx −BxCz)
(BxCy −ByCx)

.
(2.17)
Multiplying this out looks ugly at ﬁrst:
⃗A × ( ⃗B × ⃗C) = [Ay(BxCy −ByCx) −Az(BzCx −BxCz)]ˆı
+ [Az(ByCz −BzCy) −Ax(BxCy −ByCx)] ˆj
+ [Ax(BzCx −BxCz) −Ay(ByCz −BzCy)]ˆk.
(2.18)
But a little rearranging gives
⃗A × ( ⃗B × ⃗C) = (AyCy + AzCz)(Bxˆı) −(Ay By + Az Bz)(Cxˆı)
+ (AzCz + AxCx)(By ˆj) −(Az Bz + Ax Bx)(Cy ˆj)
+ (AxCx + AyCy)(Bz ˆk) −(Ax Bx + Ay By)(Cz ˆk), (2.19)
which still isn’t pretty, but it does hold some promise. That promise can be
realized by adding nothing to each row of Eq. 2.19. Nothing, that is, in the
following form:
Ax BxCx(ˆı) −Ax BxCx(ˆı)
Add this to the top row;
Ay ByCy( ˆj) −Ay ByCy( ˆj)
Add this to the middle row;
Az BzCz(ˆk) −Az BzCz(ˆk)
Add this to the bottom row.

## Page 47

2.5 Partial derivatives
35
These additions make Eq. 2.19 a good deal more friendly:
⃗A × ( ⃗B × ⃗C)
= (AxCx + AyCy + AzCz)(Bxˆı) −(Ax Bx + Ay By + Az Bz)(Cxˆı)
+ (AxCy + AyCy + AzCz)(By ˆj) −(Ax Bx + Ay By + Az Bz)(Cy ˆj)
+ (AxCx + AyCy + AzCz)(Bz ˆk) −(Ax Bx + Ay By + Az Bz)(Cz ˆk).
Or
⃗A × ( ⃗B × ⃗C) = (AxCx + AyCy + AzCz)(Bxˆı + By ˆj + Bz ˆk)
−(Ax Bx + Ay By + Az Bz)(Cxˆı + Cy ˆj + Cz ˆk).
But Bxˆı + By ˆj + Bz ˆk is just the vector ⃗B, Cxˆı + Cy ˆj + Cz ˆk is the vector ⃗C,
and the other two terms ﬁt the deﬁnition of dot products (Eq. 2.1). Thus
⃗A × ( ⃗B × ⃗C) = ( ⃗A ◦⃗C) ⃗B −( ⃗A ◦⃗B) ⃗C
= ⃗B( ⃗A ◦⃗C) −⃗C( ⃗A ◦⃗B).
2.5 Partial derivatives
Once you understand the basic vector operations of dot, cross, and triple
products, it’s a small step to more advanced vector operations such as gradient,
divergence, curl, and the Laplacian. But these are differential vector operations,
so before you can make that step, it’s important for you to understand the dif-
ference between ordinary derivatives and partial derivatives. This is worth your
time and effort because differential vector operations have many applications
in diverse areas of physics and engineering.
You probably ﬁrst encountered ordinary derivatives when you learned how
to ﬁnd the slope of a line (m =
dy
dx ) or how to determine the speed of an
object given its position as a function of time (vx =
dx
dt ). Happily, partial
derivatives are based on the same general concepts as ordinary derivatives, but
extend those concepts to functions of multiple variables. And you should never
have any doubt as to which kind of derivative you’re dealing with, because
ordinary derivatives are written as d
dx or d
dt and partial derivatives are written as
∂
∂x or ∂
∂t .
As you may recall, ordinary derivatives come about when you’re interested
in the change of one variable with respect to another. For example, you may
encounter a variable y which is a function of another variable x (which means
that the value of y depends on the value of x). This can be written as y = f (x),
where y is called the “dependent variable” and x is called the “independent

## Page 48

36
Vector operations
variable.” The ordinary derivative of y with respect to x (written as dy
dx ) tells
you how much the value of y changes for a small change in the variable x. If
you make a graph with y on the vertical axis and x on the horizontal axis, as
in Figure 2.6, then the slope of the line between any two points (x1, y1) and
(x2, y2) on the graph is simply y2−y1
x2−x1 = 	y
	x . That’s because the slope is deﬁned
as “the rise over the run,” and since the rise is 	y for a run 	x, the slope of
the line between any two points must be 	y
	x .
But if you look closely at the expanded region of Figure 2.6, you’ll notice
that the graph of y versus x has a slight curve between points (x1, y1) and
(x2, y2), so the slope is actually changing in that interval. Thus the ratio 	y
	x
can’t represent the slope everywhere between those points. Instead, it rep-
resents the average slope over this interval, as suggested by the dashed line
between points (x1, y1) and (x2, y2) (which by the mean value theorem does
equal the slope somewhere in between these two points, but not necessarily
in the middle). To represent the slope at a given point on the curve more pre-
cisely, all you have to do is to allow the “run” 	x to become very small. As
	x approaches zero, the difference between the dashed line and the curved
line in Figure 2.6 becomes negligible. If you write the incremental run as dx
and the (also incremental) rise as dy, then the slope at any point on the line can
be written as dy
dx . This is the reasoning that equates the derivative of a function
to the slope of the graph of that function.
Now imagine that you have a variable z that depends on two other variables,
say x and y, so z = f (x, y). One way to picture such a case is to visualize a
surface in three-dimensional space, as in Figure 2.7. The height of this surface
above the xy plane is z, which gets higher and lower at different values of
x and y. And since the height z may change at a different rate in different
directions, a single derivative will not generally be sufﬁcient to characterize
the total change in height as you move from one point to another. You can see
y
x
y = f(x)
Slope = rise
run =
(x1, y1)
(x2, y2)
Δy = rise
Δx = run
Δy
Δx
Figure 2.6 Slope of the line y = f (x).

## Page 49

2.5 Partial derivatives
37
z
x
y
y1
x1
z1
z = f(x,y)
Figure 2.7 Surface in 3-D space (z = f (x, y)).
z
x
y
z = f(x,y)
Slope along x-direction
is not very steep
Slope along y-direction
is quite steep
Figure 2.8 Surface in 3-D space (z = f (x, y)).
the height z changing at different rates in Figure 2.8; at the location shown in
the ﬁgure, the slope of the surface is quite steep if you move in the direction of
increasing y (while remaining at the same value of x), but the slope is almost
zero if you move in the direction of increasing x (while holding your y-value
constant).
This illustrates the usefulness of partial derivatives, which are derivatives
formed by allowing one independent variable (such as x or y in Figure 2.8)
to change while holding other independent variables constant. So the partial
derivative ∂z
∂x represents the slope of the surface at a given location if you
move only along the x-direction from that location, and the partial derivative ∂z
∂y
represents the slope if you move only along the y-direction. You may ﬁnd these
partial derivatives written as ∂z
∂x |y and ∂z
∂y |x, where the variables that appear in
the subscript after the vertical line are held constant.

## Page 50

38
Vector operations
As you’ve probably already guessed, the change in the value of z as either
x or y changes is easily found using partial derivatives. If only x changes,
dz =
∂z
∂x dx, and if only y changes, then dz =
∂z
∂y dy. And if both x and y
change, then
dz = ∂z
∂x dx + ∂z
∂y dy.
(2.20)
The process of taking a partial derivative of a given function is quite straight-
forward; if you know how to take ordinary derivatives, you already have the
tools you’ll need to take partial derivatives. Simply treat all variables (with
the exception of the one variable over which the derivative is being taken) as
constants, and take the derivative as you normally would. This is best explained
using an example.
Consider a function such as z = f (x, y) = 6x2y+3x +5xy+10. The terms
of this polynomial are sufﬁciently complex to make its shape less than obvious,
which is where a computational tool such as Mathematica or MATLAB can
be very handy. Writing a few lines of code will help you understand how this
function behaves, as you can see in Figure 2.9. Even a quick look at this warped
little plane makes it clear that the slope of the function is quite different in the
x- and y-directions, and the slope is also highly dependent on the location
on the surface. In a 3D plot such as Figure 2.9, it’s always easiest to see the
slope at the edges of the plotted region, so take a look at the slope along the
x-direction for a y value of −3. As x varies from −3 to +3 (while y is held
250
200
150
100
50
0
–50
z
–100
–150
–200
3
2
1
0
–1
–2
y
x
–3
–3
–2
–1
0
1
2
3
Figure 2.9 Plot of the function z = f (x, y) = 6x2y + 3x + 5xy + 10
for −3 ≤x ≤3 and −3 ≤y ≤3.

## Page 51

2.5 Partial derivatives
39
constant at −3), the slope starts off positive and gets less steep as you move
in the +x-direction from x = −3 toward x = 0. The slope then becomes zero
somewhere near x = 0, then turns negative and becomes increasingly steep as
x approaches +3. Doing the same quick analysis along the y-direction while
holding x constant at −3 indicates that the slope is approximately constant and
positive as y varies from −3 to +3.
Now that you have some idea of what to expect, you can take the partial
derivative of z = 6x2y + 3x + 5xy + 10 with respect to x simply by treating
the variable y as a constant:
∂z
∂x = 12xy + 3 + 5y.
(2.21)
Likewise, the partial derivative with respect to y is found by holding x
constant:
∂z
∂y = 6x2 + 5x.
(2.22)
Before interpreting these derivative results, you may want to take a moment
to make sure you understand why the process of taking the derivative of a
function involves bringing down the exponent of the relevant variable and then
subtracting one from that exponent (so d(x2)
dx
= 2x, for example). The answer
is quite straightforward. Since the derivative represents the change in the func-
tion z as the independent variable x changes over a very small run, the formal
deﬁnition for this derivative can be written as
dz
dx ≡lim
	x→0
z(x + 	x) −z(x)
	x
.
(2.23)
So in the case of z = x2, you have
d(x2)
dx
≡lim
	x→0
(x + 	x)2 −x2
	x
.
(2.24)
If you think about the term in the numerator, you’ll see that this is x2+2x	x +
(	x)2 −x2, which is just 2x	x + (	x)2, and dividing this by 	x gives
2x + 	x. But as 	x approaches zero, the 	x term becomes negligible, and
this approaches 2x. So where did the 2 come from? It’s just the number of
cross terms (that is, terms with the product of x and 	x) that result from rais-
ing (x + 	x) to the second power. Had you been taking the derivative of x3
with respect to x, you would have had three such cross terms. So you bring
down the exponent because that’s the number of cross terms that result from
taking x + 	x to that power. And why do you then subtract one from the
exponent? Simply because when you take the change in the function z (that is,
(x +	x)2 −x2), the highest-power terms (x2 in this case) cancel, leaving only

## Page 52

40
Vector operations
terms of one lower power (x1 in this case). It’s a bit laborious, but the same
analysis can be applied to show that d(x3)
dx
= 3x2 and that d(xn)
dx
= nxn−1.
So that’s why you bring down the exponent and subtract one, but what does
it mean when you take derivatives and get answers such as Eqs. 2.21 and 2.22?
It simply means that the slope varies with direction and location on the sur-
face z. So, for example, the slope along the x-direction at location (−3,2) is
12xy + 3 + 5y = 12(−3)(2) + 3 + 5(2) = −59, while at the same location the
slope along the y-direction is 6x2 + 5x = 6[(−3)2] + 5(−3) = 39.
You can do a rough check on your calculated partial derivative in Eq. 2.21
by inserting the value of −3 for y to see that the slope of z at this value of y is
12(x)(−3) + 3 + 5(−3) = −36x −12. Thus as you move in the x-direction
at y = −3, the slope should vary from +96 at x = −3, to zero at x = −1/3,
and down to −120 at x = +3. This is consistent with the quick analysis of the
slope after Figure 2.9.
Likewise, Eq. 2.22 tells you that the slope of z in the y-direction at x = −3 is
constant and positive, also consistent with the behavior expected from a quick
analysis of the shape of the function z.
And just as you can take “higher order” ordinary derivatives such as
d
dx ( dz
dx ) = d2z
dx2 and d
dy ( dz
dy ) = d2z
dy2 , you can also take higher-order partial deriva-
tives. So for example ∂
∂x ( ∂z
∂x ) = ∂2z
∂x2 tells you the change in the x-direction slope
of z as you move along the x-direction, and ∂
∂y ( ∂z
∂y ) = ∂2z
∂y2 tells you the change
in the y-direction slope as you move along the y-direction.
It’s important for you to realize that an expression such as
∂2z
∂x2 is the
derivative of a derivative, which is not the same as ( ∂z
∂x )2, which is the square
of a ﬁrst derivative. That’s easy to verify for the example given above, in
which ∂z
∂x = 12xy + 3 + 5y. In that case,
∂2z
∂x2
= 12y, whereas ( ∂z
∂x )2 =
(12xy + 3 + 5y)2. By convention the order of the derivative is always written
between the “d” or “∂” and the function, as d2z or ∂2z, so be sure to look
carefully at the location of superscripts when you’re dealing with derivatives.
You may also have occasion to use “mixed” partial derivatives such as
∂
∂x ( ∂z
∂y ) =
∂2z
∂x∂y . If you’ve been tracking the discussion of partial derivatives as
slopes of functions in various directions, you can probably guess that
∂2z
∂x∂y rep-
resents the change in the y-direction slope as you move along the x-direction,
and
∂2z
∂y∂x represents the change in the x-direction slope as you move along
the y-direction. Thankfully, for well-behaved5 functions these expressions are
5 What exactly is a “well-behaved” function? Typically this means any function that is
continuous and has continuous derivatives over the region of interest.

## Page 53

2.6 Vectors as derivatives
41
interchangeable, so you can take the partial derivatives in either order. You can
easily verify this for the example given above by comparing
∂
∂y of Eq. 2.21
with ∂
∂x of Eq. 2.22 (the result is 12x + 5 in both cases).
There’s another widely used aspect of partial derivatives you should make
sure you understand, and that’s the chain rule. Up to this point, we’ve been
dealing with functions such as z = f (x, y) without considering the fact that
the variables x and y may themselves be functions of other variables. It’s com-
mon to call these other variables u and v and to allow both x and y to depend
on one or both of u and v. You may encounter situations in which you know
the variation in u and v, and you want to know how much your function z will
change due to those changes. In such cases, the chain rule for partial derivatives
gives you the answer:
∂z
∂u = ∂z
∂x
∂x
∂u + ∂z
∂y
∂y
∂u ,
(2.25)
and
∂z
∂v = ∂z
∂x
∂x
∂v + ∂z
∂y
∂y
∂v .
(2.26)
The chain rule is a concise expression of the fact that z depends on both x
and y, and since both x and y may change if u changes, the change in z with
respect to u is the sum of two terms. The ﬁrst term is the change in x due to
the change in u ( ∂x
∂u ) times the change in z due to that change in x ( ∂z
∂x ), and the
second term is the change in y due to the change in u ( ∂y
∂u ) times the change
in z due to that change in y ( ∂z
∂y ). Adding those two terms together gives you
Eq. 2.25, and the same reasoning applied to changes in z caused by changes in
v leads to Eq. 2.26.
2.6 Vectors as derivatives
In many texts dealing with vectors and tensors, you’ll ﬁnd that vectors are
equated to “directional derivatives” and that partial derivatives such as ∂
∂x and
∂
∂y are referred to as basis vectors along the coordinate axes.
To understand this correspondence between vectors and derivatives, con-
sider a path such as that shown in Figure 2.10. You can think of this as a
path along which you’re travelling with velocity ⃗v; for simplicity imagine
that this path lies in the xy plane. Now imagine that you’re keeping track of
time as you move, so you assign a value (such as the t values shown in the
ﬁgure) to each point on the curve. By marking the curve with values, you have

## Page 54

42
Vector operations
y
x
t = 1
t = 2
t = 3
t = N
t = N–1
Tangent
vectors
t = 4 t = 5
Figure 2.10 Parameterized curve and tangent vectors.
“parameterized” the curve (with t as your parameter).6 Note that there need
not be equal distance along the curve between your parameter values (there
deﬁnitely won’t be if you choose time as your parameter and then change your
speed as you move; the reckless driver depicted in Figure 2.10 has apparently
sped up in the turn).
As a ﬁnal bit of visualization, imagine that this curve lies in a region in which
the air temperature is different at each location. So as you move along the
curve, you will experience the spatial change in air temperature as a temporal
change (in other words, you’ll be able to make a graph of air temperature vs.
time). Of course, how fast the air temperature changes for you will depend
both on the distance between measurable changes in the temperature in the
direction you’re heading and on your speed (how fast you’re covering that
distance).
With this scenario in mind, the concept of a directional derivative is easy
to understand. If the function f (x, y) describes the temperature at each x, y
location, the directional derivative ( d f
dt ) tells you how much the value of the
function f changes as you move a small distance along the curve (in time dt).
But recall the chain rule:
d f
dt = dx
dt
∂f
∂x + dy
dt
∂f
∂y .
(2.27)
This equation says simply that the directional derivative of the function f along
the curve parameterized by t (that is, d f
dt ) equals the rate of change of the
x-coordinate ( dx
dt ) as you move along the curve times the rate of change of the
temperature function with x ( ∂f
∂x ) plus the rate of change of the y-coordinate
( dy
dt ) as you move along the curve times the rate of change of the temperature
6 Some authors are careful to distinguish between a “path” and a “curve,” using “curve” only
when a parameter has been assigned to each point on a path.

## Page 55

2.7 Nabla – the del operator
43
function with y ( ∂f
∂y ). But ( dx
dt ) is just vx, the x-component of your velocity, and
( dy
dt ) is vy, the y-component of your velocity. And since you know that your
velocity is a vector that is always tangent to the path on which you’re moving,
you can consider the directional derivative d f
dt to be a vector with direction
tangent to the curve and with length equal to the rate of change of f with t
(that is, the time rate of change of the air temperature).
Now here’s the important concept: since f can be any function, you can
write Eq. 2.27 as an “operator” equation (that is, an equation waiting to be fed
a function on which it can operate):
d
dt = dx
dt
∂
∂x + dy
dt
∂
∂y .
(2.28)
The trick to seeing the connection between derivatives and vectors is to view
this equation as a vector equation in which
Vector = x-component · x basis vector + y-component · y basis vector.
Comparing this to Eq. 2.28, you should be able to see that the directional
derivative operator d
dt represents the tangent vector to the curve, the dx
dt and
dy
dt terms represent the x- and y-components of that vector, and the operators
∂
∂x and ∂
∂y represent the basis vectors in the direction of the x and y coordinate
axes.
Of course, it’s not just air temperature that can be represented by f (x, y);
this function can represent anything that is spatially distributed in the region
around your curve. So f (x, y) could represent the height of the road, the qual-
ity of the scenery, or any other quantity that varies in the vicinity of your curve.
Likewise, you could have chosen to parameterize your path with markers other
than time; had you assigned a value s or λ to each point on your path, the
directional derivative
d
ds or
d
dλ would still represent the tangent vector to the
curve, dx
ds or dx
dλ would still represent the x-component of that vector, and dy
ds
or dy
dλ would still represent the y-component of that vector.
If you plan to proceed on to the study of tensors, you will ﬁnd that under-
standing this relationship between basis vectors along the coordinate axes and
partial derivatives is of signiﬁcant value.
2.7 Nabla – the del operator
The partial derivatives discussed in the previous section can be put to use in
a wide range of problems, and when you come across such problems you
may ﬁnd that they involve equations that contain an inverted upper case delta

## Page 56

44
Vector operations
wearing a vector hat ( ⃗∇). This symbol represents a vector differential operator
called “nabla” or “del,” and its presence instructs you to take derivatives of the
quantity on which the operator is acting. The exact form of those derivatives
depends on the symbol following the del operator, with ⃗∇( ) signifying gradi-
ent, “ ⃗∇◦” signifying divergence, “ ⃗∇×” indicating curl, and ∇2( ) signifying
the Laplacian. Each of these operations is discussed in later sections; for now
we’ll just consider what an operator is and how the del operator can be written
in Cartesian coordinates.
Like all good mathematical operators, del is an action waiting to happen.
Just as √tells you to take the square root of anything that appears under its
roof, ⃗∇is an instruction to take derivatives in three directions. Speciﬁcally, in
Cartesian coordinates
⃗∇≡ˆı ∂
∂x + ˆj ∂
∂y + ˆk ∂
∂z ,
(2.29)
where ˆı, ˆj, and ˆk are the unit vectors in the direction of the Cartesian
coordinates x, y, and z.
This expression may appear strange, since in this form it’s lacking anything
on which it can operate. However, if you follow the del with a scalar or vector
ﬁeld, you can extract information about how those ﬁelds change in space. In
this context, “ﬁeld” refers to an array or collection of values deﬁned at various
locations. A scalar ﬁeld is speciﬁed entirely by its magnitude at these locations:
examples of scalar ﬁelds include the air temperature in a room and the height
of terrain above sea level. A vector ﬁeld is speciﬁed by both magnitude and
direction at various locations: examples include electric, magnetic, and gravi-
tational ﬁelds. Speciﬁc examples of how the del operator works on scalar and
vector ﬁelds are given in the following sections.
2.8 Gradient
When the del operator ⃗∇is followed by a scalar ﬁeld, the result of the opera-
tion is called the gradient of the ﬁeld. What does the gradient tell you about a
scalar ﬁeld? Two important things: the magnitude of the gradient indicates how
quickly the ﬁeld is changing over space, and the direction of the gradient indi-
cates the direction in which the ﬁeld is increasing most quickly with distance.
So although the gradient operates on a scalar ﬁeld, the result of the gradient
operation is a vector, with both magnitude and direction. Thus, if the scalar
ﬁeld represents terrain height, the magnitude of the gradient at any location

## Page 57

2.8 Gradient
45
tells you how steeply the ground is sloped at that location, and the direction of
the gradient points uphill along the steepest slope.
The deﬁnition of the gradient of the scalar ﬁeld ψ in Cartesian coordinates is
grad(ψ) = ⃗∇ψ ≡ˆı ∂ψ
∂x + ˆj ∂ψ
∂y + ˆk ∂ψ
∂z
(Cartesian).
(2.30)
Thus the x-component of the gradient of ψ indicates the slope of the scalar
ﬁeld in the x-direction and the other components indicate the slope in the other
directions. The square root of the sum of the squares of these components
provides the total steepness of the slope at the location at which the gradient is
taken.
You can see a simple example of the result of the gradient operator by
considering the tilted plane in Figure 2.11(a). This plane is deﬁned by the sim-
ple equation ψ(x, y) = 5x + 2y, and you can ﬁnd the gradient using the
two-dimensional version of Eq. 2.30:
⃗∇ψ = ˆı ∂(5x + 2y)
∂x
+ ˆj ∂(5x + 2y)
∂y
= 5ˆı + 2 ˆj.
So even though ψ is a scalar function, its gradient is a vector; it has a com-
ponent along the x-axis and a component along the y-axis. And what do these
components tell you?
For one thing, the fact that the x-component is more than twice the size of
the y-component tells you that the tilt of the plane is steeper in the x-direction
than in the y-direction. You can also tell that the slope in each direction is
constant, because the components are not functions of x or y. Both of those
conclusions are consistent with Figure 2.11(a).
(a)
–0.6–0.4 –0.2 0
0.2 0.4 0.6
–0.6
–0.4
–0.2
0
0.2
0.4
0.6
x
Top view
Side view
25
20
15
10
50
–5
–10
–15
–20
–253 2
1
0 –1
y
x
–2 –3
–3 –2 –1
0
1
2
3
(b)
y
Figure 2.11 Function ψ = 5x + 2y and the gradient and contours of ψ.

## Page 58

46
Vector operations
And if you wish to determine the magnitude of the gradient, that’s easily
done. Since the x-component of the gradient is 5 and the y-component is 2, the
magnitude of the gradient is simply (52 + 22)1/2 = 5.39 over the entire plane.
You can also ﬁnd the angle that the gradient vectors make with the positive
x-axis using arctan(2/5) = 21.8◦. The gradient and contours of the central
portion of the function ψ are shown in Figure 2.11(b).
In cylindrical and spherical coordinates, the gradient is:
⃗∇ψ ≡ˆr ∂ψ
∂r + ˆϕ 1
r
∂ψ
∂ϕ + ˆz ∂ψ
∂z
(cylindrical),
(2.31)
and
⃗∇ψ ≡ˆr ∂ψ
∂r + ˆθ 1
r
∂ψ
∂θ + ˆϕ
1
r sin θ
∂ψ
∂ϕ
(spherical).
(2.32)
You’ll see more gradients in Section 2.11 covering the Laplacian opera-
tor, which represents the divergence of the gradient. You can read about the
divergence in the next section.
2.9 Divergence
When dealing with vector ﬁelds, you may encounter the del operator followed
by a dot ( ⃗∇◦), signifying the divergence of a vector ﬁeld. The concept of diver-
gence often arises in the areas of physics and engineering that deal with the
spatial variation of vector ﬁelds, because divergence describes the tendency
of vectors to “ﬂow” into or out of a point of interest.7 Electrostatic ﬁelds, for
example, may be represented by vectors that point radially away from points
at which positive electric charge exists, just as the ﬂow vectors of a ﬂuid point
away from a source (such as an underwater spring). Likewise, electrostatic ﬁeld
vectors point toward locations at which negative charge is present, analogous
to ﬂuid ﬂowing toward a sink or drain. It was the brilliant Scottish mathemat-
ical physicist James Clerk Maxwell who coined the term “convergence” for
the mathematical operation which measures the rate of vector “ﬂow” toward
a given location. In modern usage we consider the opposite behavior (vectors
ﬂowing away from a point), and outward ﬂow is considered positive diver-
gence. In the case of ﬂuid ﬂow, the divergence at any point is a measure of the
tendency of the ﬂow vectors to diverge from that point (that is, to carry more
material away from it than toward it). Thus points of positive divergence mark
the location of sources, while points of negative divergence show you where
the sinks are located.
7 In many instances, nothing in the vector ﬁeld is actually ﬂowing; the word “ﬂow” is used only
as an analogy in which the arrows pointing in the direction of the ﬁeld are imagined to
represent the physical ﬂow of an incompressible ﬂuid.

## Page 59

2.9 Divergence
47
To understand how this works, take a look at the vector ﬁelds shown in
Figures 2.12 and 2.13. To ﬁnd the locations of positive divergence in each of
these ﬁelds, look for points at which the ﬂow vectors either spread out or are
larger pointing away from the location and shorter pointing toward it. Some
authors suggest that you imagine sprinkling sawdust on ﬂowing water to assess
the divergence; if the sawdust is dispersed, you have selected a point of positive
divergence, while if it becomes more concentrated, you’ve picked a location of
negative divergence.
Using such tests, it’s clear that locations such as 1 and 2 in Figure 2.12
and locations 4 and 5 in Figure 2.13(a) are points of positive divergence (ﬂow
away from these points exceeds ﬂow toward), while the divergence is negative
at point 3 in Figure 2.12 (ﬂow toward exceeds ﬂow away).
The divergence at various points in Figure 2.13(b) is less obvious. Location
6 is obviously a point of positive divergence, but what about locations 7 and 8?
The ﬂow lines are clearly spreading out at those locations, as they do at location
5 in Figure 2.13(a), but they’re also getting shorter pointing away. Does the
spreading out compensate for the slowing down of the ﬂow?
1
2
3
x
0
1/2
1
Figure 2.12 Parallel vector ﬁeld with varying amplitude.
4
6
7
5
8
(a)
(b)
Figure 2.13 Radial vector ﬁelds with varying amplitudes.

## Page 60

48
Vector operations
Answering that question requires a useful mathematical form of the diver-
gence as well as a description of how the vector ﬁeld varies from place to place.
The differential form of the mathematical operation of divergence or “del dot”
( ⃗∇◦) on a vector ⃗A in Cartesian coordinates is
⃗∇◦⃗A =

ˆı ∂
∂x + ˆj ∂
∂y + ˆk ∂
∂z

◦

ˆı ⃗Ax + ˆj ⃗Ay + ˆk ⃗Az

,
(2.33)
and, since ˆı ◦ˆı = ˆj ◦ˆj = ˆk ◦ˆk = 1, this is
⃗∇◦⃗A =
∂Ax
∂x + ∂Ay
∂y + ∂Az
∂z

.
(2.34)
Thus the divergence of ⃗A is simply the change in its x-component along the
x-axis plus the change in its y-component along the y-axis plus the change in
its z-component along the z-axis. Notice that the divergence of a vector ﬁeld is
a scalar quantity; it has magnitude but no direction.
You can now apply this to the vector ﬁeld in Figure 2.12. In Figure 2.12,
assume that the magnitude of the vector ﬁeld varies sinusoidally along the x-
axis as ⃗A = sin(πx)ˆı while remaining constant in the y- and z-directions.
Thus,
⃗∇◦⃗A = ∂Ax
∂x
= π cos(πx),
(2.35)
since Ay and Az are zero. This expression is positive for 0 < x < 1/2, 0 at
x = 1/2, and negative for 1/2 < x < 3/2, just as a visual inspection suggests.
Now consider Figure 2.13(a), which represents a slice through a spherically
symmetric vector ﬁeld with amplitude increasing as the square of the distance
from the origin. Thus ⃗A = r2ˆr. Since r2 = (x2 + y2 + z2) and
ˆr = xˆı + y ˆj + z ˆk
	
x2 + y2 + z2 ,
this means
⃗A = r2ˆr = (x2 + y2 + z2) xˆı + y ˆj + z ˆk
	
x2 + y2 + z2
= (x2 + y2 + z2)1/2(xˆı + y ˆj + z ˆk),
and
∂Ax
∂x
= (x2 + y2 + z2)1/2 + x
1
2

(x2 + y2 + z2)−1/2(2x).

