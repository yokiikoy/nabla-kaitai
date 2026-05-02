<!-- OCR chunk: flanders_differentialform.pdf pages 61-90 (of 219 total) -->


---
## Page 61

4.6.MAXWELL'SFIELDEQUATIONS
47
These involve space variable diferentials only. Now we interpret d' to
denote the exterior derivative with respect to space variables only.We intro.
duce 0/at in this form
a
Now theMaxwell equations are
d'@
1
d'w=-
4πt
W5
d'@2 = 0
d'@4=4πpdxdx²dx3.
ThePoynting energy-fluxvectorSisintroducedby
()ExH
thatis
W, ^ w = S, dx² dx3 + S2 dx dx1 + Ss dxr dx2.
4π
Poynting's theorem,
()B·H+E·J+(
E·D+divS=0,
follows from
d’(@@)=d@@3-@d’w3
W3-W
4π
5+-@4
4π
1
C
For bodies at rest, one assumes D = kE, B = μH where the dielectric constant
K and the permeability μ are constant in time. Then Poynting's theorem
becomes
ne
=divS+E·」
where
1
(KE²+μH²)
8π

---
## Page 62

48
IV.APPLICATIONS
is the energy density of the field.The quantity E·J is called the thermoi
chemical activity.
4.7.Problems
1.Develop theformulafortheLaplacianin cylindrical coordinates.
2.A complex matrix A is unitary if AA*= I, where A* ='A, th
transpose conjugate of A.We call A skew-hermitian if A*+ A =0.
Discusstheconnectionbetweenunitaryandskew-hermitianmatrices.
3.Show that e^ is orthogonal if A is skew-symmetric.Here
eA=I+∑
A”
n=1n!
for the real matrix A.
4.Set up a frame and the structure equations for a sphere of radius R
Compute the curvatures.
5.Find Gaussian curvature of the surface of revolution obtained by
revolving the curve
(x=cosθ+lntan(0/2)
y=sinθ
about the x-axis.
6. Given a surface in the form z = f(x, y), develop formulas for H and K
in terms of f and its partial derivatives.
7.Let E be a surface. Let e1,e2 and e',e2 be two moving frames o:
tangentvectors to E.Determine the relation between the corresponding
W and w'andverify that dw=dw'.
8. Let e1,e2,e3 and e',e2,e' be two moving frames in E3. Set uf
theorthogonalmatrixrelatingtheseframesanddeterminehowthecorre
spondingQ andQ'are related.

---
## Page 63

V
ManifoldsandIntegration
5.1.lntroduction
An n-dimensional manifold isa space which is not necessarily a Euclidean
ofa short-sighted observer living in the space,looks just like such a domain
of Euclidean space.A case in point is the two-sphere S2.This cannot be
considered a part of the Euclidean plane E2.However our observer on S2
sees that he can describe his immediate vicinity by two coordinates and so
he fails to distinguish between this and a small domain on E2.
We have the technical problem of describing an n-manifold with suffcient
precision so that we can define functions,tensors,and differential forms on
such a space.The definition which follows is motivated in this way.Each
observer on the manifold has an immediate neighborhood (local coordinate
neighborhood) described by n coordinates.Each point of the space must
lie in at least one of these observed neighborhoods.Now if we consider
simultaneously two observers,their immediate neighborhoods may overlap,
and we must specify what happens in each such overlap.In the next three
sections we go over these matters with some care.
After this is accomplished we tackle the problem of defining the integral
of a differential form.In Sections 5 and 6 we lay the groundwork by
defining chains, the geometrical sets over which forms are integrated, and
inSection7we define the integral.
5.2.Manifolds
An n-dimensional manifold consists of a space M together with a collection
of local coordinate neighborhoods U,, U2,·*: such that each point of M lies
in at least one of these U. On each U is given a coordinate system
x,...,x”
so that thevaluesof the coordinates
(x(P),···,x"(P)),
where P ranges over U, make up an open domain in Euclidean n-space E".
49

---
## Page 64

50
V.MANIFOLDSANDINTEGRATION
Suppose that U with coordinate system
x',...,x”
andVwithcoordinatesystem
y',...,y"
overlap (intersect). We may express the V coordinates y of a point P in
terms of the U coordinates x of this point:
y’=y'（x,.··,x")(i=1,..·,n).
As part of the definition,we assume that these functions are smooth(different
tiable as often as we please).
U
Having this formal definition out oftheway,we explore some consequences
First of all, on the overlap of U and Vabove we may interchange the role
of U and V to write smooth functions
x=x（y²,·.·,y")(j=1,.·.·,n).
Substitutingyields
y²=y’(x²(y),···,x"(y))
andwemaydifferentiatebythe chainrule:
which has the matrix interpretation
xelllle
We take determinants by the product rule:
d(y,···,y”）d(x,.··,x")
0(x,..·,x”)0(y',..·,y”)
Itfollows that theJacobian
d(y',...,y")
0(x,...，x”)
≠0;
it is different from O at each point.

---
## Page 65

5.2.MANIFOLDS
51
A manifold is called orientable (two-sided) if it is possible to choose the
of local coordinate neighborhoods) is positive.
Example. We make the two-sphere S? into a manifold by using six
coordinate neighborhoods. We set
S²={(x,y,z)
where
x²+y²+x²=1}.
The neighborhoods are
Ut={x>0},
coordinate system y,z.
U={x<0},
coordinate system z, y.
U={y>0},
coordinate system z, x.
U={y<0},
coordinate system x, z.
U={2>0},
coordinate system x, y.
U={2<0},
coordinate system y,x.
In comparing the overlap of two of these, we shall not be pedantic and intro.
duce different letters,hoping the reader will forgive this sloppy notation.
On the intersection of U and U we have the coordinate transformation
-²-I=]
2=z，
x>0，y>0
and so
(y,2)
0(2,x)
On the intersection of Uand U3，
h=h
（2=-√1-y²-x²,
x>0，2<0,
1
0
d(y,2)
(y,x)
y
On the intersection of U and U3,
x=x
（2=-√1-y²-x²，
‘0>2‘0>f
0
1
0(a,2)
etc.
d(y,x)

---
## Page 66

52
V.MANIFOLDSANDINTEGRATION
proves it to be orientable.
ordinate neighborhoods by taking two opposite hemispheres, each extended
slightlytomakeopen overlappingneighborhoods.
The sphere S² has two opposite orientations (outward or inward normal,
corresponding to counterclockwise or clockwise sense of rotation). Similarly
an orientable n-manifold has two opposite orientations.A definite one of
these is determined by the order in which local coordinates x', ···, x” are
given,up to an even permutationof this order.Making an oddpermutation of
localcoordinatesgivestheoppositeorientation.
LetMbeann-manifold.Tosaythatareal-valued function fon Mis
smooth at apoint Pof M means thefollowing.Let U be alocal coordinate
neighborhood containing P with coordinates x',.'·,x".We require that
f(x,."·,x") be smooth near P.This restriction on fis independent of the
particular U one chooses,since two coordinate systems whose neighborhoods
overlap on a region including P are themselves related by smooth functions
(from the definition of manifold).A real-valued function fis smooth on M
ifit is smooth ateach pointof M.
Similarly,if MandNaremanifoldsof dimensions mand n,respectively,
one defines a smooth mapping
Φ:M-→N
by the requirements that in local coordinates x,..·,x"m on U in M and
y',·.·,y”onVin N,we have Φrepresented by smooth functions
y'=y"（x',·.·,x")(i=l,·..,n)
on that part of U which Φ maps into V.
A manifold M is called a submanifold of a manifold N provided there is &
one-to-one smooth mapping
j:M-→N
the matrix

---
## Page 67

5.3.TANGENT VECTORS
53
imbedding of M in N.
in E" with n = 2m + 1.
5.3.TangentVectors
We study a manifold M and a point P on M. Our job is to define the
Euclidean space we cannot merely draw arrows emanating at P. We need
a way of considering ordinary Euclidean vectors which depends in no way
on arrows, or directed line segments. The answer is simple. We may
identify Euclidean vectors with directional differentiations.Thus in case P
is a point of E? and v = (a, b, c) is a vector at P, we may identify v with the
operator
(十品十
This does the usual things to sums and products, which motivates the
following definition.
First some notation.If M is a manifold, we denote by
F°(M)
the space of all smooth real-valued functions on M.
Let P be a point on a manifold M.A tangent vector v at P is an operator
V:F°(M)→→R,the reals
satisfying
(i）v(af + bg)= av(f)+ bv(g),a,b constant.
(i)v(f·g)=g(P)·v(f) +f(P)·v(g).
Thus v assigns to each smooth function f on M a real number v(f).
We shall first observe that if we take a constant function c, then v(c) = 0.
v(1) = 0, and setting f = 1, a =0, and g = 0 in (i) yields v(c) = 0. Observe 
that
v(cf) =cv(f)
for any f and constant c.
Next, suppose x',.-,x" is a local coordinate system, valid in some
Ie
=

---
## Page 68

54
V.MANIFOLDS AND INTEGRATION
(the vertical bar means “"evaluated at P") is a tangent vector, as one easily
verifies.
The totality of tangent vectors at P makes up a linear space, Tp, called
the tangent space to M at P. We shall show that these vectors v; form a
basis of this tangent space.We set
(x,..·,x"))p=(c,...，c").
If v is any tangent vector at P, set
v(x) = v(x²-c) =a².
Now if f is any smooth function on M, we expand f in a Taylor series up to
first-order termswith theintegralform ofremainder:
f(x)=f(c)+∑(x²-c)g;(x),
g(c)=
of
xP
Then
v(f)=v[f(c)] +∑g(c)v(x²-c²) +∑(c²-c)v(g)
hence
v=Eαl
xP
which establishes the result.We refer to a',...,a" as the components of v
with respect to the coordinate system x.If y is another coordinate system
valid at P, and
oyP
we find,by the chain rule,
b=器
x
the usual transformation law for contravariant components of a vector.
Note here that we are working at a single point so that a and b are constant.
A vector field on M consists of a smooth assignment of a tangent vector to
each point of M. In local coordinates,
v=∑a(x
a
a'(x) smooth.
On an overlap,
v=
b(x)=Ea(x)器
oyi

---
## Page 69

5.4.DIFFERENTIALFORMS
55
5.4. Differential Forms
space F°(M), the space of forms of degree 0 on M.
expression
∑a;dx'，a; constant
for each local coordinate system (x) valid in a neighborhood U which
includes P and such that any two such expressions
∑adx，∑b dy²
at P are related by
y
the usual transformation law for covariant vectors.Evidently this is
completely consistent with our local study in Chapter II.
Having this, we may form sums of exterior products of one-forms at P to
construct p-forms at P.Now we can define a p-form on M.This is &
smooth assignment of a p-form to each point P of M.If U is given with
local coordinates(x'),then on the neighborhood U wehave the representation
① =∑ag(x)dxH
with smooth functions ag(x) on U, H = {h1,..· ,hp}.
If we have the representation
=∑bk(y)dyk
with respect to a second coordinate system which overlaps the first,then the
relation between the b's and a's is given by substitution of y' = y'(x) for y"
and
dxs
for dy.As a consequence of our study of coordinate changes in Section 3.4,
we seethatthespace
FP(M)
of p-forms on M is completely defined, that exterior multiplication
uvm
eachlocal coordinate system.

---
## Page 70

56
V.MANIFOLDSANDINTEGRATION
All the rules of Chapter III are readily verified,
d(∞ △ n) = dc △ n +(-1)(dee) @ ^ dn 
for example.
If M and N are two manifolds and
Φ:M-→N
is a smooth mapping, then there is a natural induced mapping Φ*,
Φ*:FP(N)—→FP(M)
which again is defined by applying the local construction in one local co-
ordinate system at a time and piecing together the results.As in the local
theory,we have the re'sults
(i)Φ*(@+n)=Φ*c）+Φ*n.
(Φ)v（Φ)=(v)Φ（11)
(p)*Φ=(Φ)p(!)
The last of these can be expressed by means of a commutative diagram
F（M)
FP(N)
Φ*
FP+1(M)-
一FP+1(N)
Each of the two possible paths from F(N) to FP+1(M) leads to the same
result.
In practice,one often constructs differential forms on a manifold this
way. One knows in advance several smooth functions f,g,... on M.
From these one constructs one-forms df, dg, .·· and from these in turn forms
of higher degrees by taking exterior products.
Example 1.On the two sphere S² considered in Section 5.2, the functions
2, y,z are smooth O-forms. Thus dx,dy,dz are one-forms and dx dy, dy dz,
etc.,are two-forms.On the neighborhood Uwe have
x²=1-y²-2²,
dx =-dy-zd
1，
dxdy =-ydy-zdz d

---
## Page 71

5.5.EUCLIDEAN SIMPLICES
57
S'and
xdx+ ydy=0.
This means we can define a one-form α. At a point where x ≠ 0,
dy
α=—
x
At a point where x = 0, we have y ≠ 0 and
dx
-=x
y
On any arc of Si which is not the complete circle, we can find a function 0
such that
x= cos0, y= sinθ,
hence
α=d0.
It must be emphasized that no such function θ exists on all of S1—-it would
have to jumpby 2n somewhere.
5.5.Euclidean Simplices
In this section we shall describe the standard building blocks which we
later piece together toform fields of integration,p-dimensional spreads in a
manifold over which we can integrate p-forms. These building blocks will
be called Euclidean simplices of various dimensions- we shall omit repetition
of the adjectiveEuclidean in this section,butwe understand that everything
takes place in Euclidean space.
A 0-simplex is a single point (Po).
A l-simplex is a directed closed segment on a straight line.It is com-
pletely determined by its ordered pair of vertices (P。P1).
A 2-simplex is a closed triangle with vertices taken in some definite order.
It is completely determined by its ordered triple of vertices in the proper
order,
(Po,P1,P2).
Similarly one has a 3-simplex based on an ordered quadruple
(Po,P,P2,P3)
of four points, no three collinear. Geometrically it represents a tetrahedron.
Finally, an n-simplex is the closed convex hull
(Po,...,P)

---
## Page 72

58
V.MANIFOLDSANDINTEGRATION
of (n + l) independentt points taken in a definite order.The geometrical
set so spanned consists of all points
‘I='了‘0'‘"d”+...+°d=d
i.e., all possible centroids of systems of nonnegative masses to,."·,t
located at Po,... , Pn, respectively.
The boundary ds of a simplex s is a formal sum of simplices of one lower
dimension with integer coeffcients:
d(Po,P,...,P) =(-I)(Po, P,...,P-1,Pi+,..., Pn).
i=0
An examination of the lower dimensional cases convinces one that this is
consistent with the customary ideas onboundaries of oriented regions.
a(P。,P1)=(P)-(Po),
d(Po,P,P2)=(P,P2)-(P。，P2)+(Po,P1),
d(P，P,P2,P3)=(P,P2，P3)-(Po，P2,P3)+(Po,P,P3)
-(Po,P1,P2).
Po
P1
P
In the triangle,the ordering of the vertices gives a sense of rotation of the
triangle.In the tetrahedron,the ordering of the vertices gives a right-
handed screw sense in space and induces a positive sense of rotation in each
triangular face (outward drawn normal).One thinks of each minus sign
in Os as representing a reversal in this rotation sense. The result is that
d(P。,···,P3)represents the oriented geometric boundary of the tetrahedron
according to the outward drawnnormal.
↑This means that the n vectors (P1--Po), (P2--Po),...,(Pn-Po) are linearly
independent.

---
## Page 73

5.5.EUCLIDEANSIMPLICES
59
An n-chain is a formal sum
c=∑as;
where the a' are constants and the s; are n-simplices. Its boundary is
definedby
oc = ∑a'(0s;).
A basic result is that the boundary of each chain itself has zero boundary:
[0c] = 0.
It suffices to check this for simplices.Let us try low-dimensional cases:
d[(P。,P,P2)}=d(P,P2)-0(Po,P2)+(P。,P)
=[(P2)-(P)]-[(P2)-(Po)]+[(P)-(Po)]=0,
d[0(Po,···,P3）]=[(P2，P3)-(P,P3)+(P1，P2)]
-[(P2,P3)-(P。,P3)+(P。,P2)]
+[(P,P3)-(Po,P3)+(Po,P)]
--[(P1,P2)-(Po,P2)+(Po,P)]=0,
which illustrates the general idea; each face occurs twice with opposite signs.

---
## Page 74

60
V.MANIFOLDS ANDINTEGRATION
More generally,in computing
[a(P。,..·,P)],
one obtains
(Po,...,Pi-1,Pi+1,...,Pj-1,Pj+1....,Pn)
twice, with opposite signs, once each from
d(Po,...,Pi-1,Pi+1,...,Pn)
and
d(P,...,Pj-1,Pj+1,...,Pn),
so that everything cancels.
Given two n-simplices (Po,·.· , Pn), (Qo,··· ,Qn), there is a unique linear
correspondence between them which preserves the ordering of the vertices.
It is given by
tQi
(t;≥0,
∑t;= 1).
It is convenient for defining integrals to have standard models of the
simplices of each dimension.We define the standard n-simplex
s" =(R。,·.·,R)
as the simplex in E" based on
R。=0
R=(10...0)
R2= (010..·0)
R, = (00 ..·01).
(001)
(010)
(100)
We must now agree on a certain convention for integration.Let o be an

---
## Page 75

5.6.CHAINSANDBOUNDARIES
61
n-form defined on a domainU of E"which includes s".Wewish to define
C
w.
Jsn
We do this by writing w in the unique way
@ = A(x,..·,x")dx dx²..· da"
with the variables in their natural order,and then setting
_A(x)dat a..d*,.
where the right-hand side is now the standard ordinary n-fold integration,
which may be evaluated by any scheme of iteration,regardless of what order
in which the variables are taken.
For example,if w = dzdy dx, then
dxdy dz = -
| dy |.'dx |
dz = -1/6.
5.6. Chains and Boundaries
Nowwe consider a manifold M and we shall define an n-simplex in M.
As a preliminary definition,this consists of three things: a Euclidean n-
simplex s",an n-dimensional neighborhood U of s"inEuclidean space,↑ and
a smooth mapping Φ,
Φ:U-→M.
We denote this preliminary simplex by
(s", U, Φ).
If we are given a second one,
(t", V,山),
it will be considered the same as the frst provided
(tP)=(t)(t=0，t=1).
where
s"=(Po,P1,...,Pn),t"=(Qo,Q,...,@n).
In other words, if we set up the natural order-preserving linear equivalence
↑That is,a neighborhood in the smallest fat subrmanifold of Euclidean space contain.
where sn =(Po,..., Pn).

---
## Page 76

62
V.MANIFOLDSANDINTEGRATION
between s" and t":
s²←→t",
then Φ(P)=W(Q) whenever P and Q are corresponding points.This is also
expressedby the commutative diagram
M
The totality of these preliminary simplices (s", U,Φ) which in this way
in M, denoted by a symbol o".
The open neighborhoods U wehave introduced merely serve to eliminate
difficulties with differentiability on theboundary.
If o" is a simplex represented by (s", U, Φ), then s" has faces to,·"·, t,
each aEuclidean (n-1)-simplex,where
Os" = ∑ ±t;.
By restricting Φ to the various t;,each extended a little in U to make open
neighborhoods V,we define the faces of o", each represented by
;=(t,V,Φ)
and the corresponding boundary
0o"=∑±·
U
to
This is an (n -- 1)-chain in M. By an n-chain c of M we mean a formal sum
c=∑aio
with constant coefficients a and n-simplices o?. Chains may be added and
multiplied by constants.We denote by
C,(M)

---
## Page 77

5.7.INTEGRATIONOF FORMS
63
the set of all n-chainst on M.We set
dc = ∑a;o²for c= ∑a;o.
Thus
0:C(M)-→Cn-1(M)(n = 1,2,··-).
The basic property of the boundary operator ? follows readily from the
corresponding Euclidean situation: for each n-chain c,
(ac)=0.
A cycle is a chain z whose boundary vanishes,oz = 0.
A bounding cycle (or simply boundary)b is a chain which is the boundary
of a chain of one higher dimension,b = 0c.
Each boundary is a cycle, for if b = dc, then
d(b)=0(ac)=0.
One further thing to be noted is this.In our preliminary definition of a
simplex (s",U,Φ）we do not require that the smooth mapping Φ on U
into M be a one-to-one mapping. Indeed, it may happen that it takes all of
s" into a lower dimensional space, even into a single point! A close analysis
that there are very great technicaldifficulties involved in attempting to avoid
them.
5.7.Integration ofForms
Our data is a manifold M of any dimension, a p-form w on M and a p-chain
con M.We must define
0.
Je
Firstwe set
c=∑a
where the a; are constants and the o; are p-simplices and write
=∑a;
a
so it renains to define the integral of w over a p-simplex o.Now we can
representoin theform
(S,U,Φ)
where s is the standard p-simplex in EP and Φ is a smooth mapping of the
neighborhood U of sr into M.Our definition is
↑ Precise topological terminology: ordered singular differentiable n-chains.

---
## Page 78

64
V.MANIFOLDSANDINTEGRATION
p* (0).
=
Since Φ*w is a p-form on U, this is an ordinary p-fold integral, as discussed
inthenexttolastsection.
In application, one often does not bother to spell out in detail how a given
geometrical region may be considered as a chain, but rather relies on the
usual combination of experience and intuition,the latter an excellent guide
in geometry. Forexample, suppose wisa 2-form on S² = {x² + y² + z² = 1}
and one seeks
@ taken over S2. There will usually be a more effective
procedure than using the coordinate planes to decompose the surface S2 into
eight spherical triangles, setting up mappings of the standard triangle onto
each of these,etc.
What then is the value of this rather long story on chains,boundaries,and
logicaland rigorous basis things which are only understood in an intuitive
sense.In addition, we have here a powerful theoretical tool as we shall see
immediatelyin thefollowingsection on thegeneralStokes'theorem.
As an exercise, one could check that each of the standard tricks used to
evaluate surface integrals,etc.,fitsinto the above scheme of things.It
hardly seemsworth our timehere.
5.8.Stokes'Theorem
The general result we establish now includes all known formulas which
transform an integral into one over a one-higher dimension spread.
Let ∞ be a p-form on a manifold M and ca(p+1)-chain.Then
=
Jac
Since c is a sum of (p + 1)-simplices with constant coefficients, it suffices
toprove
=dw
where o is a (p + 1)-simplex.According to a representation
(sp+1, U, Φ)
ofowehavefromthedefinition
[do=S,*(da)=d(o*0).
p+1
This reduces the problem to a Euclidean one. Let n be a p-form on a

---
## Page 79

5.8.STOKES'THEOREM
65
neighborhood U of sp+1 in Ep+1.To prove
dn
Now
n=∑A;(x)dx...da²-1dxi+1...dxp+1
so that it suffces to check the formula in case r is a monomial only.Since
we may permute coordinates provided we are careful about signs,it suffices
to takethecase
n=Adx...dxP.
Then
0A
dn =(-1)p
Op+I de!... daD+1.
We remember that s+1 consists of all points (x,···, c+1) satisfying
x≥0,
I>x
Wehave
0A
dn=(-1)p
(1-∑x)
DA
=(-1)p
(x²≥0，x≤1}
=(-1)²
(x²≥0，
x≤1)
-A(x，·.·,
，xP,0)
drl
...dxP
We must next investigate dsp+1.We write
sp+1=(Ro,R,...,Rp+1),
R=0
R=(10..·0)
points in EP+1.
Rp+1 =(0 ...01)
We have 
D+1=(R,...,Rp+1)+(-1)p+(R。,R,...,Rp)
+ other faces,

---
## Page 80

66
V.MANIFOLDSANDINTEGRATION
where n = O on each of the other faces since some one ofx, .··, xP is constant
there.
Thus
n+(-1)p+1
(R,..·,Rp+1)
(Ro,R...,Rp)
R
R
The face (Ro, R1,...,R,) is the standard s. On it x+1 = 0 and so
(-1)p+1
n=(-1)p+1
A(x,a²,..·,xP,0)dx..·dxP
(Ro,...,Rp)
which is precisely the second term in the expression for
dnabove.
The
first term is obtained by projecting downward in the x+1 direction:
·.·,x,1-
∑x)dxr... dxr
(R1,..·,Rp+1)
(R,..·,Rp.Ro)
=(~1)p
···，∞°，1-
dx...dc
（Ro,R1,·.
...dxP
and this is thefirstterm in the expression for
dn.
.The proof is completed.
5.9. Periods and De Rham's Theorems
We consider an example.The manifold M consists of E? with the origin
removed,
M=e'-{}.

---
## Page 81

5.9.PERIODSANDDE RHAM'STHEOREMS
67
Suppose w is a one-form on M such that dw = 0. Then is @ exact? That
is,is it the differential of a function on M？ The proof in Section 3.6 will
not avail here because M cannot be shrunk to a point. Nonetheless, @ = df,
where
J(1.0.0)
the integraltaken along any path c which avoids O.That this isindependent
of the path follows from Stokes'theorem.For if c'is another path in M
from (1,0,0) to x,then the chain c-c'is the boundary of a piece of surface
E(2-chain)in Mand
Next suppose α is a two-form on M such that da = 0.We seek a one-
form on M such that α=d1.By the converse toPoincare'slenima in
Section 3.6,such a form  exists locally.But we are asking the global
question: Is there such a form Λ on all of M?The answer to this one is no
in general, we shall have explicit examples later. For if there were such a
one-form with d)=α we would have
α=
=p
=0
s2
Jos2
since the unit sphere S² has no boundary.But there is no reason a priori
for assuming that
α=0.
JS2
The correct result is this.If α is a two-form on M = E3-{0} with da = 0
and
α=0，
Js2
then α =d for some one-form  on M.
Thisresultis contained inDeRham'stheoremswhichwe shallformulate
nowwithoutproofs.
We dealwithafixed manifold Maboutwhichwe assume only somemild
sufficientlyhigh dimensionalEuclideanspace.
A closedformisa differential form w on Msatisfying do=0.
An exact form isa differential form w on M satisfying @ = dn for some form
7 on M.
Eachexact form is closed:
dw = d(dn) = 0.

---
## Page 82

V.MANIFOLDSANDINTEGRATION
68
Let o be a closed p-form. To each p-cycle z on M corresponds a periodt
of w,
m
J
If z happens to be a boundary b = ?c, the period vanishes,
Because of this there is a relation between periods:
(Whenever cyclesZ,,..·are related by)
∑az;=boundary,
(t)then
Ea;
∞=0.
z
DE RHAM's FiRsT THEoREM.A closed form is exact if and only if all of
itsperiodsvanish.
De RHAM's SECOND THEOREM.Suppose to each p-cycle z is assigned a
number,per(z),subject to the consistency relations
(whenever
Zaiz;=boundary,
(+）
then
∑a;per(z;) = 0.)
Then there is a closed form o on M which has the assigned periods,
W) = per(z)for each p-cycle z.
On many spaces one is able to apply these results because there is a finite
set of independent p-cycles which spans all p-cycles,up to boundaries.For
example,on the n-sphere S"it is known that each p-cycle is a boundary for
p>O,p ≠n,and that in dimension n there is a single n-cycle (S"itself with
outwardnormal for orientation)suchthat each n-cycle is a multiple of this
one plus aboundary.These things are established by algebraic topology.
A complete analysis of De Rham's theorems reveals the following result,
which has considerable attraction in itself.
Suppose we consider only chains c = a;o; which are sums of simplices
↑Thenomenclaturederivesfromthe periodsofellipticintegralsand thecorresponding
differentials for algebraic functions.

---
## Page 83

5.10.SURFACES;SOME EXAMPLES
69
with integer coefcients.Then we may talk of these as integer-chains and
haveinteger-cycles andinteger-boundaries.Theinteger-periods
of a closed form w are the periods taken over integer-cycles only.
Let w andn be closed forms of degrees p and q respectively.Suppose that
the integer-periods of w and n are all integers.Then the same is true of @ Λ n.
5.10.Surfaces;Some Examples
It is shown in topology that each closed surface in E? may be smoothly
deformed into a sphere with h handles,or alternatively,a button with h
holes.Let us consider the case h = 2 and orient this surfaceEwith the out-
ward drawn normal. The only significant two-cycle is Eitself.By De Rham's
First Theorem,a two-form α on this surface is an exact differential if and
onlyif
α=0.
c1
C2
normal
There are four significant one-cycles, , , C2, 2 . Here C and c intersect
once and cross, the same for C2 and c2.But ci and c2 intersect once
without crossing.To see the geometric plausibility of the statement that
each one-cycle c onE is a sum of multiples of the Cand c plus a boundary,
one cuts the surface E along these basic cycles.Having done this, E may be
smoothly deformed intoaplane domainwithoutholes.
De Rham's First Theorem now asserts that if w is a closed one-form on E,
then @ is an exact differential if and only if

---
## Page 84

70
V.MANIFOLDSANDINTEGRATION
=-=]
∞=0.
Applied to dimension one,De Rham's Second Theorem asserts that if real
numbers a,a,a2,a are given, there exists a closed one-form w satisfying
w=a1,
の=a,
①=a2,
①=a².
C'2
m
It is also interesting to consider non-orientable closed surfaces.These of
course cannot be realized in E3. Perhaps the simplest is the projective
plane P2.This is defined by pasting the edges of a rectangle together in the
orderindicated.Theboundaryrelationsare
(P²)=2c'-2c,
oc=(P)-(Q)
dc'=(P)-(Q).
This means first of all that there is no effective two-cycle, each two-form is
exact. The only effective one-cycle is e' -- c, and this actually bounds,

---
## Page 85

5.11.MAPPINGS OF CHAINS
71
c'-- c = ap2.Thus each closed one-form is exact.
Q
C
Another interesting example is the Klein bottle K², again defined by
pasting edges together.The boundary relations are
K2=-2c
dc=0c'=0.
P
The one independent one-cycle is c'.
5.11. Mappings of Chains
Suppose M and N are manifolds and f is a smooth mapping:
f:M-→N.
Then to each p-chain c on M there corresponds in a natural way a p-chain
f+c on N.
It suffices to explain this when c is a simplex op.Such a simplex is
represented by (s,U,Φ）where U is a neighborhood of the Euclidean
simplex s” and Φ: U→ M. We merely compose f and Φ so that f*c is
representedby
(sP, U,f。Φ).
中
f。q
N

---
## Page 86

72
V.MANIFOLDSANDINTEGRATION
We illustrate the process for the case of a two-simplex
M
N
This induced map f* takes the space of chains onto the space of chains:
M→N
C,(M)TC,(N).
We observe that if c is a p-chain in M, then
f*(0c) =0(f*c),
which leads to the commutative diagram
C,(M)-
f*
C,(N)
C,-1(M)
—C,-1(N)
f*
which is certainly analogous to the corresponding diagram in Section 5.4
for f* and d.The validity of the result is established by looking at in-
dividual simplices.
We now seewhat happens with two mappings.Let
f
9
Then the assertion is
(g 。f)*=g*of*

---
## Page 87

5.12.PROBLEMS
73
which again follows for a simplex almost directly from the definition of f*.
Finally we consider this situation.Let
f:M-→N.
Suppose that w is a p-form on N and c is a p-chain on M. Then f*w is a
p-form on M and f*c is a p-chain on N.Wehave
Js.c
This importantresult alsofollows directlyfrom the definitionforasimplex
andisobtained forageneral chain by summation.
5.12.Problems
1.Show that the totality of unit tangent vectors to the sphere S2 is a
three-manifold.Constructlocal coordinates.
2.Show that the set of all directed lines in E2 is a 2-manifold. Discuss
orientation.
3. More generally, consider the set of all oriented r-dimensional planes in
E".Show that this is a manifold, compute its dimension,and discuss
orientation.
4.Projective n-space P" consists of all (n + 1)-tuples (ao,""",an) of
real numbers not all zero, where proportional (n + 1)-tuples are considered as
representing the same point. Show that P" is an n-manifold.
5.’Complex projective n-space CP" consists of all (n+ l)-tuples
(ao,·"·,a) of complex numbers not all zero, where two such n-tuples are
considered the same if they differ bya(complex)proportionality factor.
Show that Cp" is a manifold and determine its dimension.
6.Showthatthemanifolds ofExamples 4and 5are closed (compact).
7.Let M be the manifold of Example 3. Show that the set N of all
oriented r-planes in E" which pass through the origin is a closed submanifold
of M.
8.Denote by U the open region
U={x²+·.:+x²>1}
in E". Suppose w is an r-form in E" which vanishes identically on U.
Under what conditions does there exist an (r -l)-form α on E” which also
vanishes identically onUand which satisfies da=@?
9.Show by direct calculation (i.e., without De Rham's theorems) that
if wis a two-form on S²whose integral over S²vanishes,then w =dα for a
suitable one-forntαonS2.

---
## Page 88

VI
Applications in Euclidean Space
6.1.Volumes in E"
We denote by
@ = dx,... dan
the element of volume in E",an n-form,and set
r²=∑x²，
so that V, is the volume of the unit ball.Next we denote by o'the element
of (n - 1)-dimensional volume on the unit sphere Sn-1 ={x|r = 1},and set
Thus A=2π,A2=4π，V=2,V2=π,V3=π.It is clear that the
volume of the sphere of radius r is r-1An-1,hence
n
One may evaluate V, by integrating over slabs:
(1 -x²)(n-1)/2 Vn- dx
=Vn-1Jn
where
(1 -x²)(n-1)/2 dx.
Integration by parts once leads to
-x²)(n-3)12 dx = (n -1)(-Jn + Jn-2),
74

---
## Page 89

6.1.VOLUMESINEn
75
Theserecursionformulaelead tothe standardresult
π/2
Next we obtain an explicit formula for o' in terms of the Euclidean co-
ordinates 2,·"',x,.We begin with the form
rdr=xdx,
a one-form in E" which is invariant under rotations (orthogonal transforma-
tions)of E".Consequently
*rdr=∑（-1)i-xdx...dx...dxn
(the “hat”denotes a missing factor) is an (n -1)-form in E” which is in-
variant under rotations.It follows that on S"-1,
'=c*rdr,
where.c is a constant.
Nextwe note that
d(*rdr) =∑(-1)i-1dx;dx,.. dx;..· dx, = no,
hence
d(*rdr)
1
no =cnV,= cAn-1,
≤1
C = 1,o'= *rdr on Sn-1.

---
## Page 90

76
VI.APPLICATIONSINEUCLIDEANSPACE
Summarizing, we set
=*rdr =∑(-1)-xdx..·dx...dxn,
defining an (n - 1)-form o in E". Then do = nw, and if o is restricted to
S"-1,the result is the (n -1)-dimensional volume form o'of S"-1.
Next we consider the natural projection
π: E"-{0}-→S"-1
defined by π(x)=x//x|.
We seek π* o',an (n - 1)-form on E" -{0} satisfying
d(π*o')=0sinced(π*o')=π*(do')=π*(0)=0.
(do' is an r-form on S"-1, hence O.)We shall prove
We could prove this by directly substituting
y;=xr  ino' =∑(-1)-y;dy...dy;.dyn,
We set
Then
nonr²c)
Now we observe that *(n*o’) is a one-form in E"-{0}which is invariant
under rotations, hence dependent on r alone.We may write
(*g）=(
(rdr).
From this we have
o=f(r),
dr
a constant,π*o'= ct.To evaluate c, we simply note that on S"-1,both
π*o' and t collapse to o, hence c = 1,
π*o'=t.