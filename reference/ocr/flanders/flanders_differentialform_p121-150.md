<!-- OCR chunk: flanders_differentialform.pdf pages 121-150 (of 219 total) -->


---
## Page 121

7.5.SYSTEMSOFORDINARYEQUATIONS
107
and have by exterior multiplication,
=JQ.
Wedifferentiatethis:
d=(dJ)Q+JdQ.
Now
dn=(2)
dtdy·..dy”=（J
dtdx'...dx"
and
(dJ)Q + JdQ =
dtdxl... dxn
dtdx'.. dx",
dx
hence
aY
+
0(JX')
=
x
A function f =f(t,x) is called a first integral of the system if f is constant
along each trajectory, or solution curve. Since the usual existence and
uniqueness theorems guaranteea solution through each point of space where
the system is defined,we have the condition
P
i.e.,
df.
af
Xj=0,
for a first integral.
Suppose that each of the functions g',.··,y" in the transformation above
is a first integral.Then
Y'=O,J=dy'...dy".
(Such a transformation is always possible in a small region of space because
of the existence ofageneral solution,one depending onarbitrarily prescribed
initial conditions.)
A function M =M(t,x',.··,x") is called a last multiplier of the original
system if
d(MQ)= 0,
i.e.,
0M
(MX)
+
'0==
e
Cxi

---
## Page 122

108VII.APPLICATIONS TO DIFFERENTIAL EQUATIONS
Using the transformation abovebased on firstintegrals,
Hence
He
dtdy...dy"
so that M is a last multiplier if and only if H is independent of t, i.e.,
MQ=H(y)dy..·dy".
If M,and Mare two last multipliers, then
MQ=H(y)dy..·dy”,M2Q=H2(y)dy ..·dy”,
hence
M/M2=H(y)/H2(y).
It follows that M/M depends only on the y",hence is constant along
the importantresult:
The quotient of tuo last mulipliers is a first integral.
7.6.The Third Lie Theorem
Whatisknown as theThirdFundamental TheoremofSophusLiewas
devised in order to reconstruct a continuous group given only its constants of
structure.These concepts will be explained in Chapter IX.For our present
purposes, we shall look upon this theorem as a result, and a rather deep one
at that,inpartial differential equations.
We work in E". All indices run from 1 to n. First of all we are given n3
constants c'jk subject to these constraints:
0=+
∑(c'ikCrs+ c'jrCsk+ ciskr)=0.
The problem is to find n one-forms o',.'·,o”which are linearly indepen
denton someneighborhood ofOinE"andwhich satisfy therelations
do=c.
The Lie Theorem asserts that this can be done.
The quadratic relations we have assumed for the constants (c) are easily
verified to be the same as d(do’)=0, assuming our problem is solved,hence
they are necessary conditions.That they also are suficient conditions will
now be seen. The proof we give is based on those in Cartan [10, p. 239] and
[7,pp.280-283].Because the proof is lengthy,we shall break it into several
steps.

---
## Page 123

7.6.THE THIRD LIETHEOREM
109
Step 1. We define an n X n matrix F = [f] of homogeneous linear
forms by
fk =∑ciw.
Thenwe consider thelinearinitialvalueproblem
He
= I + HF, H(0,x) = 0
2e
for an n Xn matrix H=H(t,x). For each x it has a unique solution,
defined for all t,and the solution is analytic in (t,x).At x=0 we have
F=0, s0
He
(t,0)=I，H(0,0)=0,
e
hence
H(t,0)=tIand H(1,0)=1.
Step 2. We set
w=dxH(t,x)
so that w is a row vector of one-forms, free of dt. Clearly
dw=dtdx(I+HF)+入
=dt(dx+wF) +入,
where 入is arow vectorof two-forms,alsofree of dt.We alsodefine a square
matrix A=[α;] of one-forms by
αi=∑ckk.
We note the obvious relations :
xA=wF and dxA=-wdF.
We also note two less obvious relations:
d(wA)=2dw ^A and 2xA²=wAF.
Thefirst follows from the skew-symmetry of the constants c' in theirlower
indices. The second follows from the quadratic relations on the c's. We
multiply the quadratic relation (p. 108)by x'w*w² and sum :
0x++x
which in matrix language is -xA +wAF -- xA*= 0.

---
## Page 124

110VII.APPLICATIONS TODIFFERENTIAL EQUATIONS
Step3.From the formula for dw that defines 入,we have
d=dt^d(wF)=dt(dwF-wdF)
=dt(入F-wdF)=dt(AF+dxA).
Step4.We define
0=入-wA,
a row vector of two-forms, free of dt.We shall prove the decisive formula
d0=dt^0F-^A.
We have
d0=dA-dw ^A=dt(aF+dx^ A)-[dt(dx+∞F)+a]A
=dt(AF-wFA)-A^A
=dt(AF-xA²)-A^A
=dt(AF-∞AF)-A^A
=dt^OF-^A.
Step 5.We shall now prove that
0=0.
Since both the @ and the A'are free of dt, so is 0 and we have
0 =±∑9'skdx dx,9’ik = 9'iux(t,x).
We may even assert that
9'k(0, x) = 0.
For h',(0, x) = 0 which not only means that the coefficients of the o* vanishi
at t=0,but also that the coefficients of
=∑(
(oh';oh'k)
dxkdei
vanish at t = O according to the very definition of partial derivative,
oh',
oh';(0, x)
=0.
From these facts, what we say about the initial values of the g'jx follows.

---
## Page 125

7.6.THE THIRDLIE THEOREM
111
The result of Step 4 implies
2e
This homogeneous linear system taken together with the initial conditions,
the vanishing of the g's at t = O, has the unique solution
9²jk(t,x)=0,
and so 0i = 0.
Step 6.Now we can wind up this story.Since 0 =0 we have
=,
da' = ∑e'xw A @* + dt A α.
We consider this relation on the subspace t = 1.
Setting
o' =@=1 =∑h,(1, x)dx,
itbecomes
do'=.
Since h’§(1,0)=8)(Step 1),the one-forms o,.··,o”are linearly independent
at O,whichimplies of course that they are linearly independent in some
neighborhood of O.Theproof is complete.

---
## Page 126

VIII
Applications to
DifferentialGeometry
8.1.Surfaces (Continued)
Everything in this section will be based on the local theory of Section 4.5.
Now we have integration at our disposal andwe shall discuss a few global
results.Let E be a closed surface in E3.Forewe take the outward drawn
normal to E. The mapping
x-→e3
is a map on Z to the unit sphere S2.As x varies over E,e; varies over S²a
whole number of times, called the degree of the normal map (cf. Section 6.2).
Theelementofareaofthenormalmapis
@@2 = K002
since
de=@e +@e2.
HereK is the Gaussian curvature.Hence
K02 =4πn
JE
where n is the degree.The factor 4π is simply the area of theunit sphere.
In particular,if ∑ is a closed convex surface,then ecovers S²exactly
once asx coversE,hence
K02= 4π
JE
in this case.
After this, we shall limit our discussion to closed convex surfaces.Two
important invariants are the total area
A=
0102
and theintegratedmean curvature
=W
HoO2.
JE
112

---
## Page 127

8.1.SURFACES
113
Given a closed convex surface E and a fixed positive number a,we form
the surfaceE' parallel toEat distance a by marking off onthe outward-drawn
normal at each point x of E the distance a and taking the locus of all points
so obtained.Thus the typical point on the parallel surface is
y=x+ae3
where e always denotes the normal at x.We have
dy=dx+ade3
=（oe1+o2e2）+a（we+∞e2）
=（+aw)e+（o2+aw2)e2.
Itfollows that the normal to theparallel surfaceE'atyis againeand that
e, and e2 can be taken as a basis of the tangent space at y. Thus we have
dy=te+t2e2
with
T1=01+aW1，t2=02+a02.
Itfollows thattheelementofareaofE'is
t2=(0+aw)(2+a@2)
=0102+a(02-02w)+a²@2
= (1 + 2aH + a²K)02
so that the total area of E'is
A'=
(1 + 2aH+ a²K)2,
Tt2=
A' = A + 2aM + 4πa².
(This formula can alsobe provedby firstdoingitfor apolyhedron and then
taking limits in an approximation of E by a sequence of polyhedra.If one
examineswhattheformulameanswhenEis.aconvexpolyhedron,onewill
By integrating with respect to a,one easily comes to a relation between the
three-dimensional volumes V'and V enclosed by E' and Z, respectively:
V' = V + aA + a²M + §na3.
One can alsoverify the relations
M' = M+ 4πa,
H+aK
K

---
## Page 128

114VIII.APPLICATIONS TODIFFERENTIAL GEOMETRY
We next introduce the support function of our closed convex surface E.
This is defined by
p=x·e3.
It is convenient to fix E in space so that the origin O is insideE.Then we
have p > O at each point of E.
The following method will be used to obtain several identities.Let  be
any one-form on E.Then
d=0.
JE
For dE= 0 and Stokes'theorem givesus
1=0.
First we consider the form
α = e3 (x x dx).
Here
da = de3·(x x dx) + e3·(dx x dx).
Now
de3·(xxdx)=-x·(de3×dx)
= -x·(dx x de3) = -x·(2HoG2e3)
=-2Ho02（x·e3)=-2pHo2
and
e3·(dxxdx)=e3·(2002e3)
=2002,
so that
dα =2[002-pHo2].
Since the integral of dx is zero,
HoO2
Next we set
β=x·(e3xde3).
By a calculation similar to that used for α,
dβ=2[pK2-Ho02]
so that
W
Ho02
pKo02

---
## Page 129

8.1.SURFACES
115
Since wehave found the integrals of H andKweighted by pit is also reason-
able to seek the integral over ∑ of the form po2.We get this by starting
with thevectorialarea
(02)e3=dx×dx=(dydz,dzdx,dxdy)
from which
p02=(x·e3)(o02)=x·(dydz,d2dx,dxdy)
=xdydz+ydzdx+zdxdy.
Let R be the region of E3 bounded by the closed convex surface and let V
denoteitsvolume.Then
p0102=
(xdydz + ydzdx +zdx dy)
(E=R)
d(xdydz+...)=3
dxdydz=3V,
R
po2=V.
We close this sectionwith thefollowinginteresting theorem:
Let E be a closed convex surface of constant Gaussian curvatureK.Then
E is a sphere.
To prove this,we recall the relations
dx=0e+02e2
(de =we + w2e2
[w=po1+ q02
@2=q+ro2
(H=(p+r)
K=pr-q²
developed in Section 4.5 for any moving frame. Since E is convex, the
matrix
(p 9)
is positive definite, p > 0,r > 0, K > 0. (See p. 120-121 in the next section
for details.） Because of the arithmetic-geometric mean inequality we have
K = pr-q²≤pr≤[±(p +r)]² =H2.

---
## Page 130

116VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
We also note that there can be equality,K = H²,only when q= 0 and
p=r=H,whichimplies ∞=H1,W=Ho2,de=Hdx.
But
f=K
where each integral is taken over ∑ and we have exploited the hypothesis
K = constant. Because the quantities at the ends of this chain of in-
equalities are equal, all integrands must be equal, H = √K.By our remarks
in the last paragraph,this implies that de, = Hdx with H constant,
Hx=e3+Hcwith ca constant vector,x-c|=(1/H)|e3|=1/H,∑ is a
sphere.
8.2.Hypersurfaces
We shall extend our study of surfaces to higher dimensions and at the same
time motivate some of the things in the next section on Riemannian geometry.
A hypersurface is an n-dimensional manifold M embedded in En+1.We
denote the moving point on M by x.Our study is local so we pick a definite
unit normal n at each point x of M.The mapx-→ n is a smooth map on
M into S".(This can be done globally on a hypersurface M precisely when
M is orientable.） The tangent space at x is an n-dimensional Euclidean
space; we pick an orthonormal basis for it, e1,"".,en. Thus at x, the
vectors e1,*"·, en,n make up an orthonormal basis of E"+1. Since dx is
in thetangent spacewehave
dx=01e1+...+onen
where o1,·"·, 0, are one-forms on M. From the relations
‘I=u.u‘0=u.'θ(#g=".'a
we deduce that
de;ek+edek=0,
de;n + e;dn =0，
0=up.u
and so
[de;=∑wje; -@n
(dn=∑w;e;
where wij, W;are one-forms on M and
Wij+@j=0.

---
## Page 131

8.2.HYPERSURFACES
117
It is convenient to write all of these structure relations in matrix form. We
set
=（，···，on）,
（Q=，
("...∞)=
Then
dx = oe
-%)()
0=,+
By taking exterior derivatives we obtain integrability conditions.(We
shall omit the symbol“^”in what follows.All products of differentials are
exterior.)
0=d(dx)=(do)e-o(de)
= (do)e --o(Ωe - tcon)
=(do-oΩ)e+o²on,
do=oΩ,o'@=0;
%)()
d?
d
(),(o-
do
{dΩ-Ω²+*∞∞
-"(d∞)+Ω
dΩ-∞Ω
0
dΩ-Ω²+'∞∞=0,
do = 0Ω.
We define a skew-symmetric matrix of two-forms:
 = 0,ll = dΩ - Q².
We sum up our results:
do =oΩ,
'0=U,+
'=0,
dw =0Ω,
(+'∞∞=0,

---
## Page 132

118VIII.APPLICATIONS TODIFFERENTIALGEOMETRY
or in terms of individual elements of the matrices,
do;=∑o;Wij,
Wy+Wj=0,
∑a;w=0,
d@;=∑@@,
(0i+@;@=0.
The o; form a basis for one-forms on M, hence we have relations
W=∑buj.
Because Z o;w; = O, the b; must be symmetric,
buj=bje·
The mean curvatureH and Gaussian curvatureKare defined by
H==∑，K=b
1
n
the corresponding quantity for S",K represents the ratio of volumes,volume
of spherical image over volume of M, due to
@···w=(∑b)..(∑bn)=b···n
= Ko1...On.
Suppose one has a function v = v(y, z,·".) of several variables where v is
always a tangentvector to M.For example,we might assign to each point
of a curve on M a tangent vector at that point, arriving at a vector-valued
function ofonevariable.
How does an observer constrained toM observe the motion of v?We
write
v=∑ce;
where the c;arefunctions and have
dv=dc;e;+∑c;de;
=∑dc;e;+∑c:(∑wie; -@n)
=∑(dc;+∑c;Wu)e;-(∑c;wi)n.
Our observer who is constrained to move in the hypersurface M cannot
“"see”the motion of v which takes place in the direction normal to M; he
sees only the tangential motion of v.Consequently he believes v is motion-
less provided
(dc;+∑c;@y)e;= 0;

---
## Page 133

8.2.HYPERSURFACES
119
that is,
dc;+∑c;Wy=0(j=l,...,n).
A vector function for which these equations are valid is said to move by
parallel displacerment.
The following can be checked. If v = v(y,z,·.·) and w = w(y,z,·"-)
are two such vector-valued functions which are compatible [for each point
(y,%,.".) in the parameter space v and w are tangent at the same point of
M] and each moves by parallel displacement, then v·w is constant. In
particular, Iv}² = v.v is constant.
Let P=P(s)be a curve on Mparametrized by its arclengths so that
t=t(8)=s
dP
is the unit tangent vector.The curve is called a geodesic provided t moves
by parallel displacement.
There is a geometric interpretation of the matrix b;jl which is quite
fundamental.To each particular displacement dxofthepositionvector x
corresponds a displacement dn of the unit normal n.Both dxand dnare
in the tangent space at x so that we can look on
dx-→→ dn
as a linear transformation A of this tangent space.More precisely, let v be
any tangentvector atx.Pick any curve x=x(t)through xso that
dx
p
=V.
We follow the normal n = n(t) as x traverses the curve. Then
dnm= Av
oP
is our definition of A.We see that this is quite independent of the choice of
the curve x(t) so long as it has the prescribed tangent v at t = 0.
For suppose
V=ce +... +c,en.
Then
dx=∑o;e;
so that
But
dn
=

---
## Page 134

120VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
Now
W=∑bij,
so our result is
A(c;e)=E(∑bc)e;
which establishes these points:(l) A is a well-defined function on the tangent
space at x to itself, (2) A is linear, (3) the matrix representation of A with
respect to the basis e is llb:jl.
Since the matrixb;lis symmetric,the linear transformation A on the
(Euclidean) n-dimensional tangent space at x is self-adjoint: for each pair
of tangentvectorsv,w,
(Av)·w =v·(Aw).
It is clear that our definition ofAdepends only on thehypersurface M and
the way it is embedded in E"+1, not on our choice of the moving frame e.
Consequentlytheformulas
H =trace (A)
1
n
K =|4|
showthatHandKaregeometricquantities.
Since A is self-adjoint,its characteristic roots are all real and they are
calledprincipalcurvatures.The corresponding characteristicvectors define
(in general) n direction fields on M called principal directions whose
integralcurvesarelinesofcurvature.
Convexity of M can be interpreted interms of a definiteness condition on
the transformation A.To make this precise, suppose M is convex and we
choosefor ntheinward unitnormal.
n0
Wefix apoint x on M and form a corresponding normal section,the curve*
of intersection of Mwith any (two-dimensional) plane on the line no.This

---
## Page 135

8.2.HYPERSURFACES
121
is a curve x = x(t) which is convex on its plane, which means that the function
no
（x-xo)·n
x=x(0)
f(t)=(x-xo)·no
is convex,hence satisfies
d²f
0=2P
Mo.
Wehave
器()mE(()m
Now
dn=Z()eyn-(a)nno.
de:
Since the tangent vectors e;(O) at x(0) = xo are orthogonal to the normal
n(0) = no, the condition reduces to
≥(),()。≤0. 
But @; = bujj, so we have
=()()
Since the direction
(.别。
is arbitrary,we conclude from this that the matrix
is negative semidefinite so that the same is true for the transformation A
which this symmetric matrix represents.

---
## Page 136

122VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
(The correctness of sign can be verified in the simplest possible case,that
of a convex curve in the plane.The usual Frenetformulas are
( dx = dse1
de;=rdsn
(dn = -kdse1 (8 = arc length)
s0 that01=d8,@1=-Kds,b1=-K≤0.)
n
x
Wereturn to thegeneral situation.The elementsOy of the curvature
matrixOarecurvatureforms.Wemaywrite
Oj=∑Rijkk，Rik+ Ru = O,
defining the Riemann curcature tensor Rijki of the hypersurface.Because of
the relations
0+@;@=0,
and
(q”qq#q)=qq=
we have
Bik+okbi
[bikbil]
Algebraic consequences of these formulas are the following:
Rijt + Rtu = 0,
Rjk +Rjik= 0,
Rijkt+ Riulj + Rjk = O,
Ruykt = Rlij,
all ofwhichfollow easily.
We shall see that theRiemann tensor is independent of howM is embedded
in En+1 so that these relations are particularly interesting,connecting the

---
## Page 137

8.2.HYPERSURFACES
123
intrinsic Riemann tensor with the quantities buj，whichclearly depend on
the embedding.
Indeed,it turns out that theR's are determined by the o'salone with no
reference to the normal n.This means that if two hypersurfaces M, and M2
are ina one-one correspondence which preserves distance(i.e.,preserves the
then M,and M,have the same Riemann curvature tensor.
Whatweshall showisthattheequations
d=αΩ，Ω+Ω=0
determine Q uniquely,so thatQ is completely determined by the o's alone.
This is more in context in generalRiemannian geometry sowe shall postpone
the proof until p. 129 ofthe next section.Having this result,it follows that
-p=θ
isalsocompletelydetermined by theo's,hence soistheRiemann tensor.
We shall now take up the special case in which our hypersurface M is
given in theform
u=u(x,···,x")
in x',..., x”, u-space.
It is convenient to set
du
02u
Pi='
Wehaveforthepositionvector
x=（x，x²,···,x"，u)

---
## Page 138

124VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
and so
dx =(de', dx²,..·,da”, du)
=(dx,···,dx”,∑p;dx')
pp'了=
where
t;=(oi,..·,dn，Pi).
The vectors t;,·.,t, are tangent vectors and evidently form a linear basis,
but generally not an orthonormal basis,of the tangent hyperplane.
The vector
=(-P1,···，-pn,1)
satisfies
w·t;=0
so it is a normal vector (with positive componentin the u-direction).The
unitnormalnisgivenby
w =wn
where
w2 = w·w= I +∑p:2.
We note that
wdw=Ep;dp;=∑piri;dx'.
We shall now determine the matrix representation of the basic linear trans-
formation A with respect to the basis t,.··,t, of the tangent hyperplane.
This matrix is not symmetric in general because (t;) is not an orthonormal
basis.However,its trace and determinant are the trace and determinant
of A since anymatrix representationyields avalid determination of these
quantities.
Suppose the matrix we seek is la;ll.Then this means
At;=∑aitj.
Let v be any tangent vector.Because of these relations plus the fact that A
is self-adjoint we have
(Av)·t;=(At;)·v=∑ai;(t;v).
Now going back to the very definition of A, symbolically,
A:dx-→dn,
wesee thatthisrelationmeans that
(dn)·t;=∑ai;(dx·t).

---
## Page 139

8.2.HYPERSURFACES
125
It is from this set of equations that we shall determine ayll. We have
dw = dw n + wdn,
dw·t;=w(dn)·t;
since n·t;=0.But
dw·t;=(-dp1,...,-dpn,O)·(o,...,oinPi)
=-dpi=-∑rdx
sowehaveobtained
dn·t;=-
Eridxi
On the other hand,
dx·t;=(dx,...,dx”,du)·(ji,·.·,jnP)
= dx + p;du = dx + p;pkdxk
=∑(6s + Pjpk)dx*,
80 we have
∑ai;(x +P;px)dx =-
∑ridak
1
∑aij(jk+pjpx)=
w
Setting
/p1
R=rxll,
：
A =all,
pn
wemaywritethisas
A(I +p'p)=
R
R(I + p'p)-1.
Since
p'p=∑p²=w²-1
we see that
=I + p'p--
w²-1
(I +p'p)(1
2
2p'p= I,
hence
(I +p'p)-1 = I-
A=-=R(1-

---
## Page 140

126
VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
The mean curvature H is found by taking the trace:
1
n
nw
nw
where△uistheLaplacian of u.
The Gaussian curvature K is found by taking the determinant:
K=|4| =(-1”
-|R||I + P'pl-1.
w"
One finds by a short calculationt that
|I + p'pl =u²
so that
(-1)"
K
1a+
For the special case n = 2 of surfaces, we use the standard Monge notation
ne
du
02u
d²u
a²u
=b
x2
0y2
andhave
w²=1+p²+q²,
H
[(b+8bdz+zd)-(2+)]
-1
and
K=(rt-8)
w4
both familiar formulas.
↑Sete=（1,0,...,0）,e2=（0,1,...,0),...,en=（0,0,...,0,1）.Then
[I+pp丨=|e1+p1p,...,en+pnpl
=|e1,...,en+∑p.@1,...,et-1,p,e+1,...,n]
=1+∑p²=w².

---
## Page 141

8.3.RIEMANNIANGEOMETRY,LOCALTHEORY
127
8.3.Riemannian Geometry,Local Theory
Theproblemhere is todeal withtheinner geometryof amanifoldwhichis
not part of a Euclidean space.If the manifold were part of Euclidean space,
itwould inheritalocalEuclideangeometry(distancefunction)fromthatof
theincluding space,as was the casefor the hypersurfaces discussed in thelast
section.However, it is not part of Euclidean space, so we must postulate
the existence of a local distance geometry.What we do in effect is to pre.
s
smooth.
Thus we let M be an n-dimensional manifold.We suppose that an inner
product is given in the tangent space at each point P of M.Thus if
vandwaretwotangent'vectorsatthesamepointP,v·wis areal number.
The inner product is supposed to be smooth in this sense: If v and w are
vector fields on M,then v·w is a smooth function on M.(Precisely,at
each point P of M, the values of the given fields v, w at P are Vp, Wp,
tangentvectors atP,andwe arerequiringthatvp·wpbea smoothfunction
of P.)
The procedure in Section 2.5 (pp. 13-14) for finding an orthbnormal basis
maybemadeconstructive,smooth operations ateach step.Weknowthat
there exists on eachlocal coordinate neighborhood on M a set of n vector
fields, forming a basis for the tangent space at each point of the neighbor-
hood.We convert these fields to orthonormal ones to arrive at smooth
vectorfields
e,...,en
defined on the local coordinate neighborhood in question and satisfying
e;'ej=oij.
Pretendingforamomentthatweareobserversconstrained tothemanifold
the right steps.We let P denote the moving point on M and wish to think
of its arbitrary displacement dP as a tangent vector with differential form
coefficients;wehopefullywrite
dP=∑o;e;
with o1，·"·,o,differential one-forms on our neighborhood.(Since dP
is in no sense an exterior derivative of anything,we distinguish this d by
bold-face type from the usual d. The same applies to the de; below.）We
expect to arrive at a basis o1,··', o, for the one-forms which in some sense
is orthonormal, dual to the basis e1,."',e, of vectors.
We must be guided by our experience in Euclidean space.There we
would takea coordinate system u',.'·,u”and without hesitation write

---
## Page 142

128VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
thevectors
dui,.
une：
being the natural frame associated with the coordinate system.But pre-
cisely this can be done on M.The expression
is independent of the local coordinate system.Indeed, if u,···,u” is
anothersystem,then
dui
d
e/ne
di
and so
that is,dPis the same either way.
Having this, we express the natural frame in terms of the orthonormal one,
(品)=Zave; 
and solve for the oj:
∑duiaye;=∑ojej,
O; = ∑aydu'.
We have reached our first equation of structure for local Riemannian
geometry:
dP=Eoe.
Ournextventureis to attempt ananalogueto the equationsfor thedisplace
mentsde;ofthevectors ofthemovingframe.Herewemakean essential
departure from what we did with surfaces and hypersurfaces; we must
"normal' direction.Thus we seek expressions
de;=∑we;

---
## Page 143

8.3.RIEMANNIAN GEOMETRY,LOCAL THEORY
129
with one-forms Wij.We try to find such wi; so as to be consistent with these
conditions:
(1)
de;ek+e;·dek=0,
(2)
d(dP) = 0.
The reason for (l) is that d(e;ek) = d(&u)= O and we hope to“differentiate"
the dot product by the usual product rule.In choosing (2) we simply go
according to the Euclidean analogue.In the usual way,(l) reduces to
(1)
W证+Wki= 0.
We explore condition (2):
d(∑o;e:)=0,
∑doe;-∑o;de;= 0,
∑(do-∑o;wu)e;=0,
so (2) is equivalent to
(2)
do;=∑o;Wij.
We have finally come to a well-formulated problem:given the basis
O1 , ."· , , of one-forms, find one-forms @; satisfying
((1)
@+@j=0
((2)
do;=∑o;@ji
We shall show that this problem has exactly one solution.(This completes a
point we left open on p.123 of the last section.)
Since theo;formabasiswemaywrite
Wj=∑Iijkk
wherethe (unknown)functions Iuyk aretheconnection coeficients,orChristoffel
symbols.Equivalent to (1') is
(1")
Iijk + Ijuk = 0.
The do; are known since the o; are known; we may write
0=+!do='op
We have
do;=ijkk=∑@ji
=∑k=（-kij）k
and so(2')is equivalent to
(2")
Fju -Ikij= Cijk·

---
## Page 144

130VIII.APPLICATIONS TODIFFERENTIAL GEOMETRY
Ourprecise statement nowis this:
sugonba inu fo uapshs ay 'o = ! + uf! mye yons !y suopounf uaaep
Tiyk +Iju=0
Ijuk-Ikij=Ctjk
has a unique solution given by
(xf1）=
For if Tu is any solution,then we use the equations alternately to derive
Iik=-juk=-Ikij-ik
!-!+!"1 =!-!* =
!-+ -!I=+-=
hence
2Iik=Ckij -Cjki-Cijk
which establishes the uniqueness of solution.It is easily verified that the
asserted values of Iijk really are a solution.
We have completed our structure equations,
dP=oe
de = Ωe
Ω+'Q=0,
wherewehaveintroducedthematrixnotation
/e1
=(，·.·,）,
Ω=wl
en
and alreadyhave one integrability condition,
do = oΩ.
There is no reason for believing that d(de)= O in any sense.We have
d²e = d(de) = d(Ωe) = (dΩ)e -Ω(de)
= (dQ - Q²)e.
We set
① = 0;l =dΩ -Ω²,
the curvature matrix which appears from the symbolic equation
d²e = Oe

---
## Page 145

8.3.RIEMANNIANGEOMETRY,LOCALTHEORY
131
as representing a“second derivative"--exactly how one thinks of curvature
inelementary differential geometry.
We derive further integrability conditions by differentiating.From
do=oΩ
we have
0=d(do)=(do)Ω-o(dΩ)
(p）-(）=
hence
=0.
From
-p=
wehave
d0 =d(dΩ) -d(Ω²)
=0-(d)Ω+Ω(dΩ)
++(+）-=
hence
d0=Ω0-0Ω,
which comprises the Bianchi identity.
We sum up:
Structure equations
Integrability conditions
dP=ce
( do =oΩ
de =Qe
=0
Ω+'Ω=0
[d0 = Ω0 -0Ω.
=dΩ-Ω²
The n form o, ..· o, is the volume element of M. It is determined up to
sign.If M is oriented, one may fix it by choosing only moving frames
coherentto the orientation.
The O:; are two-forms which may be written
0=Rik
which defines theRiemann curvature tensor.We have
Rikt+ Rijk = 0
Riukt + Rjkt = 0.
The relation o⊙ = 0, or
∑RikO;OkO;=0,
is equivalent to
Rijkt + Rikj + Rijk = 0.

---
## Page 146

132VIII.APPLICATIONS TODIFFERENTIALGEOMETRY
In the specialcase of ahypersurfacewehad the symmetry condition
Rijxt =Rkij
as an obvious consequence of the expression for R;jku as a two-round minor
(see p.122).Such a determinant representation is not possible in this
general situation,but it turns out that this symmetry of the Riemann
tensor is true anyway,an algebraic consequence of the other relations:
(Rik-Rkj）=Rikt+(Rki+Rkj)
=(Rijkt+Riklj)-Rjkli
=--Ruk-Rjkli
=Rlujk+(Rju+Rjikt)
=(Rluk +Rijkt) + Rjkl
= - Rkij + Rjikt
=-(Rik-Rknj),
and so
2(Rk-Rkj)=0
whichimpliesthesymmetryinquestion.
Those who have been through the mill in Riemannian geometry a la
classical tensors will be anxious to see the connection.There one deals with
a naturalframe
a
m=“
a
due to a local coordinate system (u',··· ,u"). One sets
9j=VV
defining thepositive definite symmetricmatrix(metric tensor)
G= ll9yll.
Usually one looks instead at the corresponding definite quadratic form
ds²=∑gi;[du²du]
where the brackets remind us that this is ordinary,not exterior,multiplica-
tion of differentials.Thisismotivatedby theformula
[()”
dt
for the arc length of a curve u' =u'(t).
Now one has
dP =∑du'v.
Wetry
!Au?='Ap

---
## Page 147

8.3.RIEMANNIANGEOMETRY,LOCAL THEORY
133
and thenintroduce Christoffel symbolsby
To have
dgi= dv;V;+ vdv;
and
0 = d(dP) = -∑du²dv;
requires
+
Lowering indices:
the equations become
[5,词] + [6,] =
ogij
[j,k]=[5,ki]
with the usual solution
[,j]=
and so it goes.
This digression out of theway,webriefly consider parallel displacement.
Let v be a tangent vector on M which is a function of one or more variables.
Wewrite
v=∑c;e;
where thec;are functionsand have
dv=dc;e;+∑c,@;
=∑(de;+∑c;wj)ej.
A vector v moves by parallel displacement if dv = 0, i.e.,
dc,+∑c;(Wy = 0.
With this interpretation of dv one has for two compatible vector functions
v,wthat
(MP)·A+M.(AP)=(M·A)p
Consequently if both v and w move by parallel displacement then v·w is
constant;its differential vanishes.

---
## Page 148

134VIII.APPLICATIONS TODIFFERENTIALGEOMETRY
A curve P = P(s) on M where s is the arc length is called a geodesic if
the unit tangent dP/dsmovesbyparallel displacement.
Example.We consider the upper half plane with the (Poincare) metric
ds2 = [dx]² + [dy]²
3y²
Here
dx
dy
0=
02=
y
y
Since theposition vector isP=(x,y)wehave
dP=（dx,dy)=0e+02e2
so that
e1 = (y,0),e2 =(0,y).
We have
dxdy
do=
=0102，
do2=0,
y²
hence
(do1, d02) = (01 , 02)(
Q=
0
=z-p=θ
-do，0
0102
The only significant component of the curvature tensor is
R12 12 = 1.
In our discussion of surfaces we wrote dw + Koo2=0 for the Gaussian
curvature K. Here the right interpretation is w = @2 = 0, K = - R12 12
= -1.For this reason we say that the upper half plane with the Poincare
metric has constantnegative curvature.
Weshallshowthateachsemicircle
P = (a + rcost,rsint)
0<t<π
orthogonal to the x-axis is a geodesic.In coordinates it is given by
=α+rcost, y=rsint,

---
## Page 149

8.3.RIEMANNIANGEOMETRY,LOCAL THEORY
135
and we have for the tangent
dP|dt = r(-sint,cost)
=[(-sint) e, + (cost)e2]
h
1
[(-sint)e +(cost)e2].
sint
Hence for the arc length 8,
d[(-sint)² +(cost)²]
sin²t
sint
t = dP/ds =(-sint)e, + (cost)e2·
Alongthe curvewehave
W12=0=-dt,
de, = - dte2:
de2 = dte1;
dt= d[(-sint)e, + (cost)e]
= --(cost)dte1 --(sint)dt e2 -- (sint)(-dte2) + (cost)(dte1)
=0,
the unit tangent moves by parallel displacement, the curve is a geodesic.
We shall close this local study with an application of The Frobenius
Integration Theorem of Sections 7.3and 7.4.
Let Mbe aRiemannian manifold with curvature tensor zero.ThenMis
flat:there exists a local coordinate systemu',..·,ufor which thenaturalframe
a
a
心...m
is an orthonormalframe.
This is proved as follws. We are assuming ⊙ = 0, i.e., dQ = Q2. By
the first application in Section 7.4,there is a matrix A of functions satisfying
(dA)A-1 =Ω,
and A is orthogonal. We define t = (T1,""·,t,) by t = oA. Then
0=（）-y(）=p-(op)=(v）p=p
Each of the one-forms t; is closed, dt; = O, hence exact locally,
T; =du'.

---
## Page 150

136VIII.APPLICATIONS TODIFFERENTIALGEOMETRY
This defines our local coordinate system (u',.··,u"). On the one hand we
have
du
and on the other,
dP=ce=tA-1e,
hence
Inelel
=A~le.
/anele)
Since theframe e is orthonormaland the matrixAis orthogonal,the natural
frame(0/du,.·.,0/0u") is also orthonormal.
8.4.Riemannian Geometry,HarmonicIntegrals
In this section we shall sketch the remarkable results of W. V. D. Hodge
on the potential theory of closed Riemannian manifolds.This work pertains
to differential forms alone so we can forget all about vector fields.In this
spirit we had better make a fresh start and reformulate the pertinent facts
about Riemannian manifolds which we shall need.We shall presuppose
that the manifolds we discuss are orientable,so this willbe built into the
structure.
Thus we have a manifold M. It is covered by a system of overlapping
neighborhoods U,,U2,·.·.On each U,there is a basis
01,...,0n
for the one-forms.If o1,·'.，o is this basis on U and ,·"·,, is the
one on O,then wherever U and O intersect we must have
=auj
where A = la;ll is a proper (determinant one) orthogonal matrix.
...o=|ao...o=o...on.
Next, the star operator of Section 2.7 applies.To each p-form @ corresponds
on (n - p)-form *@.Locally
*(o·..0)=p+1·..on
We recall that
**()=(-1)p(n-P)c0.
We define a new operator & by
80) = (- 1)p+n+1*d *(0.