<!-- OCR chunk: flanders_differentialform.pdf pages 91-120 (of 219 total) -->


---
## Page 91

6.2.WINDING NUMBERS,DEGREE OF AMAPPING
77
6.2.Winding Numbers, Degree of a Mapping
if M and N are closed oriented n-manifolds and f:M—→N,then the
chain f M is an integral multiple of N plus a boundary.This integer
multiplier is called the degree of f and written deg f.
Now suppose that ∑ is a closed oriented (n - 1)-manifold in E" --{0}.
Then by the Jordan-Brouwer theorem of topology, ∑ decomposes E" into
exactly tworegions.We assumeEis oriented by the outward normal.The
projection mapping π of Section 6.1 sends ∑ into S"-1.It is true that
degπ = 0 or l;our point is that this can be determined by an integral.Let
 =degπ.
Then
=π==8
o'=0An-1,
hence
=
An-1JE
More generally,let M"-1 be a closed oriented manifold,
f: M"-1 →E"-{0}.
Essentially we are thinking of f(Mn-1) as a hypersurface in E" -{0} which
may intersect itself.We look on this hypersurface as winding around the
origin and we want to count how many times it encircles. This winding
numberisgivenbytheKroneckerintegral
1C
An-1JM
f*t.
We may justify this as follows. Set g = π of: M"-1 → S"-1. What we
are afterisdegg.Now
9*(M) =(deg g)s"-1 + (boundary),
hence
= (deg g)
o'= An-1 degg,
sn-1
degg = A-1 JM
1C
g*o'

---
## Page 92

78
VI.APPLICATIONSIN EUCLIDEAN SPACE
f
E"-{0}
M"
But g*o'=(f*。π*)o'=f*t, so we have
degg = An-iJM
The mostgeneral situation is this:
f:M"-→→N".
Let β be the volume form on N taken so that
β =1. Then
/N
For f* M = (deg f)N + (boundary), hence
degf
JS.M
One interesting example: let T" be the n-torus, f: S"→ T" where n ≥ 2.
Then deg f = 0.
Because the integrals involved are integer-valued, they remain constant
when the mapping in question is subject to a deformation. Precisely, let
f:M—→N be a one-parameter family of maps.Then
degf
is a smooth function of t, always an integer, hence constant. It follows that
deg fo = deg f1.
One other remark.Suppose wehave
f:M-→N， g:N-→P
so that
h=g。f:M--→P.
Then
deg h = (deg f)·(deg g).

---
## Page 93

6.4.LINKING NUMBERS,THE GAUSSINTEGRAL
79
6.3.TheHopfInvariant
For each sphere S",leto, denote the element of area,normalized so that
O = 1.
sn
Consider first a map f: S3→S2.Then f*o2 is a 2-form on S3.Also
d(f*o2)=f*(do2)= 0.Since S3 has no nontrivial 2-dimensional cycles,
we deduce that
f*o2=da1
where the one-form α, on S3 is unique up to the differential of a function.
The 3-form α, ^ f*o2 has an integral
αf*2,
s3
which has the remarkable property of being an integer, called the Hopf
invariant off.It is invariant under deformation of f.More generally,let
f:S2n-1 -→S".
Then f*o, = dan-1 , and the Hopf invariant of f is
αn-1^f*on.
JS2n-1
We may represent S3by pairs of complex numbers
(2,20)，[2|²+ |2w|²= 1.
The mapping (z, w) -→ z/w provides a mapping of S3 into the closed complex
plane,i.e.,the Riemann sphere S².This map has Hopf invariant +1, hence
it is essential in the sense that it cannot be deformed to atrivial map,every-
thing going to a single point.
6.4. Linking Numbers, The Gauss Integral, Ampere's Law
Let M", N be oriented closed manifolds in E", where r + s = n - 1, and
curves in E3.)We want to count how many times they link.To do this,
we form the product space M X N which is an oriented manifold of dimen.
sion r + 8 = n - 1. We consider the map f: M X N-→ E" -{0} defined
by
f(x, y) =y-x.
Now we set
link (M, N) = deg f.

---
## Page 94

80
VI.APPLICATIONSINEUCLIDEANSPACE
Thus if t is the n-form in En - {o} we considered above,
1r
link(M, N) =
An-1JMXN
An-1JMJN
We shall work this out in E3for a pair of closed curves M,N:
1(z×dz)·dz
2
We let x, y be the moving points on M, N, respectively. Then
z =f(x, y) =y-x
so that
1
f*t=
2l1y - x13 (y -x) x(dy - dx)] (dy - dx)
1
1
1y-x13 [(y-x) x dy].dx,
link (M, N)= {
dx·
(y-x) x dy
4πJxeMJyeN
Nly-x13
(In this computation dy x dy = O, etc., since dy involves only one variable.)
Imagine a steady unit electric current flowing around the closed loop N.
By Ampere's law, the magnetic field at a point x due to the current in a
segment dy is
1(y-x)xdy
—4π1y-x13
hence the total magneticfield atxis
1f (y-x)×dy
N

---
## Page 95

6.4.LINKING NUMBERS,THE GAUSS INTEGRAL
81
Itfollowsthatlink(M,N)
F(x)·dxisprecisely thework done by this
JM
field on a unit magnetic pole which makes one circuit of M.
In the next example, link (M, N) = 0, which seems surprising since the
curves cannot really be separated.

---
## Page 96

VII
Applications to
DifferentialEquations
7.1.Potential Theory
We summarize the notation of Section 6.1. Space: E". Coordinates:
x，2，..·，x.
r²=x²+.·+x²
dr
(-1)-xdx..·dx...d.
=*（rdr）
W = dx, ·.· dx, = volume element of E".
do=nw,
dt =0.
mπm/2
F((n/2)+ 1)
Let u be a smooth function on a domain in E". Then
了=np
ne
dxl
*du =∑(-1)-1
.dx...r...dx,
dxi
d*du=
=（△u)
0x12
defining the Laplacian
a²u
(See Section 4.4 for details when n = 3.)
78

---
## Page 97

7.1.POTENTIALTHEORY
83
If u and v are functions on the finite domain R, the Dirichlet (bilinear)
integralis
au au=()()o.
D[u,] =
JR
Next we have by Stokes' theorem
u*dv =I d(u *de).
JR
JR
But
d(u*de)=du^*dv+ud*dv
= du^ *dv+u@,
hence we have
GREEN'SFORMULA
u*de=D[u,]+
u△vw.
JoR
JR
By reversing u and v and subtracting the results, we obtain
GREEN'SSYMMETRICALFORMULA
（#d-v*d）=
(u-v△u)o.
JoR
[One usually writes *du =(du/0v)2 where  is the (n - 1)-dimensional volume
elementonoRandou/dyis thenormal derivative.]
In case v is harmonic in the region R,△v = 0, and we have
(u*dv-w*du)+
△u∞=0.
JoR
JR
By specializing further we have this result:
Let u and v be harmonic functions in a region R.Then
U*d =
V*du.
JoR
JoR
We derive further consequences by setting
1
g-2,
dv ==(n -2)
(rdr),
*d=-(n --2)t,
d*dv=0,
△=0.

---
## Page 98

VII.APPLICATIONSTODIFFERENTIALEQUATIONS
The function v is defined on E" --{o}. We suppose the region R contains 0.
and we apply the forrmula above to the punctured region
R-{r≤}
with e a small positive constant. We suppose u is harmonic on all of R.
Since
d[R-{r≤e]=oR-{r=e},
wehave
u*dv
u*d
U*du-
V*du
oR
-(n~2)
ut+(n-2) / ut =
np
JeR
R
We evaluate theindividual terms:
d(uo)=
(du ^o+u·na).
Now for [xl ≤e, u(x) = u(0) + O(e), hence
uw) = u(0) V + O(e)e".
Jr≤e
Similarly
du=(2x)=s
O(e)w = O(e)e",

---
## Page 99

7.1.POTENTIALTHEORY
85
hence
ut = nV,u(0) + O(e) = An-1(0) + O(e).
Jr=g
1
*du
d(du)
87-2
r≤e
1
(△u)@ =0.
gh-2
re
We substitute these results and let e—→0 to get
u(0) = An-1JoR
1C
1
*du
+2n
which gives the value of a harmonic function at a point in terms of the
boundary values of it and its normal derivative.
Special case. Let R be the spherical region of radius a centered at 0,
R ={r ≤a}.In this case the second term on the right-hand side vanishes
for the same reason that the corresponding integral taken over {r = e}
vanishes. On oR ={r = a} we have
1
a"
where
μ=μx ==∑(-1)-1xdx,...dx..·dxn
is the element of (n - 1)-dimensional volume on {r =a}. (For a = 1 this
reduces to o. Since there are n x-terms in the numerator and a = |x| is in
the denominator,it is homogeneous of the right degree, n — 1.) We have the
GAUSSMEANVALUE THEOREM
rn
1
=（0）n
μ
which tell us that the mean value of u over the sphere of radius a is the value
of u at the center.
Two important properties of harmonic functions follow from this result.
R unless u is constant.

---
## Page 100

86VII.APPLICATIONS TODIFFERENTIALEQUATIONS
For suppose u assumes its maximum at an interior point x.ofR which,after
translation of coordinates, may be taken to be 0.Let ∑ be any (n - 1)-
sphere of radius a centered at 0 with a so small that {r ≤a} is in R.Since
u(x)≤u(0)wehave
u（0）={u/{μ≤{0/{μ=0)
so we must have u(x) = u(0)for all x in E.Hence u is constant on the largest
spherical neighborhood of x。we can draw in R.Evidently this means u is
of such overlapping spheres. The result for minima follows the same way.
UNIQUENESS PRINCIPLE FOR THE BoUNDARY VALUE PROBLEM. Let u and
v be harmonic on afinite domainRand coincide onoR.Thenu=vonR.
For u - v vanishes on oR and is harmonic. By the Maximum Principle,
u-v≤O onR,u≤v.Similarly v≤u,hence u=v.
The function (1/rn-2) is ideally suited to the sphere.On other domains
itisinconvenientbecause oftheterminvolving thenormal derivativeinthe
expression above for u(O). Hence we introduce the Green's function.
Let R be a finite domain.A function v(x,y)defined for x and y distinct
points of R is called the Green's function of R if
(i)For each fixed y in R,v(x, y) is a harmonic function of x for x in
R -{y).
(i)For each fixed y in R, v(x, y) = O for x in R.
(i）For each fixedy in R,
1
is asmoothharmonic function on all of R.
Using the samemethod as above one proves thefollowing:
If uis any harmonic function on afinite domainR andv=v(x,y)is tha
Green'sfunctionforR,then
-1
=（A）n
u(x)*dx0(x,y).
(n-2)An-1JoR
In case R is the spherical domain r ≤a centered at 0, the Green's funa-
tionis
1
α-2

---
## Page 101

7.1.POTENTIALTHEORY
87
We note that
1y2）
is the inverse of y with respect to the sphere R(reciprocal radi).For x on
0R, ↓x| = a and we have
[x-y1²= (x-y)·(x-y)=a² -2
q2
a4
1y2 x·y +
1y|2
a²
a²
｜x-yl=
x-yl.
lyl
This explains why v vanishes for x on 0R.
Next
where
1
1
t(x-y)=
x-y(x-yi)d
We only need du for x on oR. Recalling that y' = (a²/lyl²)y for |xl = a we
have
d
|x|=a
-(n-2)a²-1y1²
_-(n-2)a²-Iy1²
[x-y1a²
。=
[x-y1a
μx,
so that the representation of u in terms of its boundary values specializes to
a²-1y1²{
u(x)
u(y)=
This is the PoIssoN INTEGRAL FoRMULA which provides an explicit solution
formula for the Dirichlet problem on the sphere.-find a harmonic function
with prescribed boundary values.
Returning to a general finite domain, we mention the important symmetry
propertyoftheGreen'sfunction:
v(x, y) = v(y,x).

---
## Page 102

88VII. APPLICATIONS TO DIFFERENTIAL EQUATIONS
(That this is the case for the sphere is not apparent from the unsymmetrical
formula above.Butfor the denominator of the secondterm we have
1y1²]x-y12 =1y1²(x-y)·(x-y) = 1y1²(1x|²
=x1²1y|²-2a²(x·y) +a4,
which turns out tobe symmetricalafter all.)
One of the many important consequences of the Poisson Integral Formula
is the
LiouvILLE THEoREM.Let u be a harmonic function on all of E"and u ≥ O.
Then uis constant.
We shall show that for each y in E", u(y) = u(0).We fix y with Iy| = b
and selectanya>b.Then
a²-b²{
u(x)
u(y) =
aAn-1 J1x1a 1x-yx
Now
x-≤x|+=α+6,
｜x-y≥｜x|-ly|=a-b,
hence
1
1
1
1xm+
Since u(x)≥ O we may use these inequalities to estimate the integral:
(a²-b²)
u(x)μx≤u(y) ≤aAn-1(a - b) Jx1=a
(a²-b²){
u（x)μx
aAn-1(a + b) Jx=a
But from the Mean Value Theorem,
u(x)μx =(an-1An-1）u(0),
Jx|=a
so we have
(a² - b2)an-2
(a² -b²)an-2
 (A)n(0)n
(a~b)”
u(0).
(a+b)
By letting a → o we have
u(0) ≤u(y)≤u(0),
and so for each y, u(y) = u(O), u is constant.

---
## Page 103

7.1.POTENTIALTHEORY
89
Remark 1.We return to the symmetrical Green'sformula
（*d-y*d）=
(u△-v△u)@.
JR
R
Weapply thisin this situation:
R={e≤r≤a},
vharmonic in R for all ε > 0,
v vanishes on r = a,
u smooth in {r ≤a}.
We do not require that u be harmonic. The formula reduces to
u*du
ap*n
+np*a
v（△u）∞）=0.
First case.
*dv=-（n-2)t.
By the methods above,
u*dv=
-(n-2)
u =(n~2)An-1u(0)+O(e),
d(*du) = O(e²).
Substituting these in and letting&—→0we obtain
{-"V-=（0）n
uμx-(n-2)An-
a-2)(a)@o.
This gives information about a solution u of the Poisson equation △u = f
with boundary values of u assigned.
Second case.
dv：
x,
One differentiates this to prove △u =0. This also follows when one notes
that
-(n-2)

---
## Page 104

90VII.APPLICATIONS TODIFFERENTIALEQUATIONS
The end result in this case is
Ine
n
xuμ-An-iJr≤a
1
x(-)(4u)o
Dxl = a*+1An-1 Jr=a
Analogous formulas for higher derivatives are possible.
Remark 2.We have avoided n = 2.In this case the basic difference is
thatthe symmetricalharmonicfunction with singularity atOis lnrrather
than r-(n-2). Using this, results similar to those above follow.
7.2. The Heat Equation
We consider the parabolic equation
²u0²uu
. = + 
Suppose u is a solution, valid in a region of x, y,t space which includes a
region R and its boundary.
First we consider
α = (uxdy -u,dx)dt -udxdy.
Then
da =(uxx +uy)dxdydt-u,dt dx dy =0,
hence
[α = fdx=0. 
R
√R
Next we consider
β = 2u(uxdy - u,dx)dt-u²dx dy.
Then
dβ=2(uxdx+udy)(uxdy-u,dx)dt+2u(uxx+uyy)dxdydt-2uu,dt dx dy
=2（u²+u²)dxdy dt.
It follows that
C
[2u(uxdy-udx)dt -u²dx dy] = 2 ↓ (u² + u²)dxdy dt.
JoR
VR
Suppose R is taken in the special form of a cylinder T X [O, b] where T is a
region in the x, y-plane.We then have
{0} X1-{o}X1+[q'0] X(1e)=e
We now assert the basic uniqueness theorem:
Ifu ranishes on the base T X{0} and on the lateral surface 0T X [0, b],then u
vanishes identically in R.For the integral formula above reduces to
(u²+u²)dxdydt+
u(x, y, b)² dxdy = 0.

---
## Page 105

7.2.THEHEATEQUATION
16
Since everything ispositive,this implies
ux=uy=0 in、R,
u=0”on TX{b},
which is more than enough to imply u = O in R. Because the heat equation
is linear,we deduce that two temperature distributions which coincide
initially at t = O and always coincide on the boundary of R must be identical
for all t at each point of R.
We shall now do the same thing in n dimensions, where there is an inter-
esting sign change. Our variables are x1 ,''' , &n,t and the heat equation is
△u=du/ot
where as usual △u = Z0²ulox². The operator * will apply to space
variables only.
This time we set
β=2u(*du）dt +(-1)-u²）,
where @ = dx, ... dx,. Now
du（*du)=（gradu)²=
and we have
dβ = 2(grad u)²@dt + 2u(△u)@dt + 2(- 1)n-uu, dt 0)
= 2(gradu)²wdt,
hence
β=2
(grad u)²wdt.
JoR
R

---
## Page 106

92VII. APPLICATIONS TO DIFFERENTIAL EQUATIONS
Now let T be a region in E", R = T X [0, b]. Then
0R=0TX[0,b]+(-1)"TX 0[0,b]
= TX[0,b] + (-1)T X b+(-1)-iTX 0.
Suppose u vanishes on T X [0, b] and on T X o. Since dt = 0 on T X b
(i.e.,t =b = constant) we have
‘0=pnp*n
JoR
consequently
JoR
JR
thatis.
u²@0 + 2 / (grad u)²wdt = 0
qX1
JR
and we conclude as before (grad u)² =∑ (du/dx;)² = 0 on R, du/dx; = 0 on
R,u is constant on R,u = 0.
7.3.The Frobenius Integration Theorem
Everything is local in this section; we operate in a neighborhood of O in
E".Let obe a one-form which does notvanish at O.We ask,under what
conditions are there functions f and g satisfying @ = fdg?In other words,
we seek an integrating factor for the differentialequation @ = 0.If @ = fdg,
then f does not vanish in a neighborhood ofo,hence
dw=df dg =df f-∞,
dw=0∞(0=f²df=dln|fl)
and so
@Ad∞=∞θw=0.
For a one-form @ =Pdx+Qdy +Rdz in E3,this is the condition
P(R-Q)+Q(P-Rx)+R(Qx-P)=0.
We note that if w=fdg,then the equations @ =0 and dg = 0 are the same
and hence the solutions or integral surfaces of @ = O are the hypersurfaces
g = constant.
s
Example 1.Let∞=yzdx+xzdy+dz so that do=ydzdx+xdzdy.It
follows that
↑Material in this and the next sectionis taken from aUniversity of California Tech-
nical Report of June 1957,Seminar on exterior differential forms.This was prepared
for theU.S.Army Office of OrdnanceResearch ContractDA-04-200-ORD-456.

---
## Page 107

7.3.THEFROBENIUSINTEGRATION THEOREM
86
which is not so useful since dz/z is singular along the z-axis.A better choice
Buoun oa suuap o o v 0 = op aaey am pue px -xpfi- = 0s!
we use the fact that each integral surface g = constant will be cut by the
plane {x = at,y = bt} in a curve which intersects the z-axis in the solution
z of g(o,0,z)= constant.The equation @ =0 on the plane x = at,y = bt
becomes
0=pzq+2p
with solution
2=cexp(-abt²)
satisfying the initial condition z(0) = c. However abt² = xy so these curves
span outa surface
z=ce-xy.
Wenow think ofa,b,c asvariables and make the transformation
x=a
(x, y, z)
y=b
with
=e~ab≠0.
d(a, b, c)
(z=ce-ab
Wehave
dz=e-abdc-2(adb+bda),
whichyields
W =e-abdc,
orin the originalvariables
W =e-xy d(zexy)
and theintegral surfacesare
ze*y=constant.
It willbe observed that we have arranged the function g sothat g=c
intersects thez-axispreciselyin =c.
Example 2.This time we try the procedure on w = dz-ydx --dy.On
the plane x =at, y =bt, the equation @) = 0 becomes dz = (abt + b)dt,
2=abt²+ bt+ c and we arrive at the surface
2 =xy + y+ c.
But on the parabolic cylinders x = at, y = bt² we have
dz =(abt²+ 2bt)dt，2 = abt²+ bt²+ c,
2=y+y+c,
a different family of surfaces.The reason for this failure to obtain integral
surfacesis seenfrom
d) =-dydx，@ ^ dw = -dzdydx ≠ 0.

---
## Page 108

94VII.APPLICATIONS TO DIFFERENTIAL EQUATIONS
THEoREM. Let w =∑fdx’ be a one-form which does not vanish at 0.
Suppose there is a one-form 0 satisfying dow = 0 ^ w.Then there are functions
f and g in a sufficiently small neighborhood of O which satisfy w = fdg.
Note 1.Since w is given while 0 is certainly not uniquely determined,it
simplifies the proof if we avoid explicit use of 0 as long as possible.
Note 2.The condition on w@ is unchanged when we replace @ by a multiple
of w.In fact,if h≠0,then
d(h∞)=dh∞+hdw=dh∞+hθ@=（dh+h0）∞,
d(hco)=[(dh)h-1+0](hc∞).
Proof.Since w ≠ 0 at 0, we may assume some one of the functions f; does
we multiply w by a nonvanishing factor,we may assume
@ = dz - A;dx,
A; = A;(x,2).
a =(a,...,a")
We fix any point a in x-space and consider the equation @) = 0 on the
hyperplane x = at,(i = l, ·.· , n):
dz
We solve this equation with the initial condition z(O) = c.More precisely,
we seek a function F(t,a,c) satisfying
(F(t,a, c) =∑ A[at, F(t,a,c)]a
( F(0, a, c) = c.

---
## Page 109

7.3.THE FROBENIUSINTEGRATION THEOREM
95
The usualexistence theorem of ordinary differentialequations yields a unique
solution.We see thata change of scaleis possible:
since the function on the right is again a solution to the same problem. In
particular, setting k = 1/t,
F(t,a, c) =F(1, ta, c).
Weintroducethechangeofvariables
(x=u
(2=F(1,u,v)
with
a(x,z)| =[1 
(u,v)。
since
a
P
d
F(1,u,v)
=d
F(1, 0,v)
ap=
F(0,a,v)
=0
=0
du
dulv=0
= 1.
Thus the new variables u,v form a local coordinate system in a suffciently
small neighborhood of o. We suppose that in these coordinates we have
 =∑ P;du'+ Bdu，P;= P(u,u),B= B(u,v).
Since @ vanishes identically on u = at, v = constant, we have the relation
∑ P(at, v)a' = 0.
To continue, we consider the mapping Φ on (t,a, v)-space to (u, v)-space
givenby
Φ(t,a,u)=(ta,u)=(u,v).
Wehave
Φ*(0 =∑ P;(ta,v)(adt +tda)+B(ta,u)du
=∑tP;(ta,u)da²+B(ta,u)du,
*@ =∑P;(t,a,v)da+B(t,a, v)du,
where P;(t, a, v) = tP(ta, v) so that P(0,a, v) =0. The important point is
that Φ*w is free of dt.
The equation do =0 ^ @ implies d(Φ*∞) =(Φ*θ) ^(Φ*@). We may
set
Φ*0 = H(t, a, u)dt + other terms.

---
## Page 110

Then
ap
dtda'+other terms.
We compare the dt da’ terms in this on the one hand and (Φ*0)^(Φ*w)on
theothertoobtain
=HP.
Ot
But this combined with P;(0,a,v)=0 implies,by the uniqueness theorem
for ordinary equations,that P;= 0. Hence P;= 0,
@ = Bdw,
the desired result.
References.For thistheoremand thegeneralizationwhich follows,see
E. Cartan [9, p. 46], [7, p. 367].
Example.@=xdy-ydx.Certainly @^ dw0 since wA dw is a three.
form.However, the form w vanishes at 0 so one does not expect that the
integral curves of w=0will span out evenlyaneighborhood of 0;in fact
these curves are just the lines ax + by = O through 0.We note,however,
that dw =0^ w is impossible in any neighborhood of 0.For do=2dxdy
so that if 0=Adx+Bdy,then 2=Ax+By which fails atx=y=0.
Remark.From the theoremwe easily deduce again that a one-form @
satisfying dw = 0 is exact.For consider 0 = dz -- @ where w is a form in
x-space. Then d0 = O, hence there is a one-parameter family z = F(x,c)
of integral surfaces,F(o,c)=c.For each choice of c,θ vanishes on
z =F(x,c),i.e.,@ = dF.(We cannot proceed without passing to one
more dimension since @ may vanish at O.）This trick of introducing a new
independentvariablefor anunknown function isauseful one.
We now pass to the general problem.Let w',.··,@" be one-forms in
r+s space,linearly independent at 0.Set Q=@·.·^ w.The
systemis called completely integrableif it satisfies any ofthe conditions of the
following lemma.
LEMMA.The following conditions are equivalent:
(i)There exist one-forms 0'; satisfying
dw=∑0;^∞²(i=1,···,r)(n=r+s)
j=1
(ii）d∞Ω=0
(i=l,...,r)
(ii)There ezists a one-form I satisfying
'v=Up

---
## Page 111

97
Proof. That (i) implies (i) is obvious (but unnecessary).Also (i) implies
(ii) with =∑0.Next,(i) implies (ii)is the case since(iii)means
...V+v-...vvp-(I-)
=..·∞
and we merely multiply by @' to deduce (i).
It remains to prove that (i) implies (i). Let o+1, ."·, @" be one-forms so
that @,."·,@" form a basis of all one-forms.We write
do' = Ef'nw' A ok.
Since dw* ^ Ω = 0, we have
fkA ... A@Aw@=0,
hencef’k=0 forr<j<k,
do =( -fnw)^@.
=k+
FROBENIUs INTEGRATION THEOREM. Let O',···,W' be one-forms in E",
n=r + s,linearly independent at 0.Suppose there are one-forms 0'; satisfying
do² = 0;^@
(i=I,...,r).
=1
Then there arefunctionsf'j,g’ satisfying
@=f;dg(i=1,...,r).
Discussion. The hypothesis is certainly a necessary one. For if we
write
∞=(w',···,w"),F=llf'jll，g=(g,···,g"),
the conclusion is w = dg F.The matrix F must be nonsingular in a neigh.
borhood of 0 and so
dw=-dgdF=-∞F-dF=∞
where
O= -F-'dF.
Next we note the hypothesis is invariant under a linear transformation of
the o'. In fact, if  = oA where A is an r x r matrix of functions, non-
singular near 0, then
dn=d∞A+∞dA=∞A+∞dA
(p-+O-)=

---
## Page 112

98VII.APPLICATIONS TO DIFFERENTIALEQUATIONS
We shall give two proofs of the theorem,eachfrom a somewhat different
point of view.The starting point is always the same.We write
w = n;dx (i=I.,...,).
=1
Since the o′are linearly independent at 0, somer×r minor of|h'lis non-
singular in a neighborhood of 0. We multiply (@',."·, @') by the inverse
of this minor. On changing our notation slightly then we have
w'= dx -
First proof.For each point a =(a,."·,a) in x-space we consider the
system of equations ′= O along the linear variety x = ta:
dz
d =∑A';(ta, z)a
with initial conditions z*(0)= c'.By ordinary differential equations, there
isaunique solution in a suffciently small neighborhood of0,i.e.,there exist
functions F’(t, a, c) satisfying
Ori
=1
Fi(0,a,c) = c(i= l,·"·,r).
We shall write F = (F1, ... , F").
Next, we fix k and set G(t, a, c) = F(kt, a, c). Then G(0, a, c) = c and
aGi
.0Fi
hence by uniqueness, G(t,a, c)=F(t,ka, c),i.e.,
F(kt,a, c) =F(t,ka, c).
In particular, setting t = 1 and then replacing k by t,
F(t, a, c) =F(1, ta, c).
We pass to new variables u,v according to the transformation
x=u
z = F(I, u, v).
This is nonsingular in some neighborhood of O since
d(u, v)o

---
## Page 113

7.3.THE FROBENIUS INTEGRATION THEOREM
66
For
2e
Fi(1,0,v)
v。=
= F'(0, a,v).
=8
In these newvariableswe maywrite
@ = B'(u, )d* + P'(u, )duy.
The fact that each w' vanishes identically along the curve u = ta, v = con-
stant implies
P(ta,ya=0(i=1,..,).
We propose to show that the functions P',(u, v) vanish identically. To do
this we consider the cone mapping Φ on (t,a, v)-space to (u,v)-space
defined by
Φ(t,a, v) = (ta, v) =(u, v).
Wehave
Φ*( =∑ P'(ta, v)t da + terms in duk
=∑P';(t, a, v)da' + terms in dk
where P';(t, a, v) = P';(ta, v)t so that P;(0, a, v) = 0. It follows that
d中*∞²=∑
aPi
dtda’+ other terms.
Finally we use the hypotheses dw' =  0' ^ o*. We write
Φ*0=H(t,a,v)dt + other terms
and compare the coefficients of dt da' in the relation
dΦ*∞²=∑(b*θ)(Φ*k):
OPi
(t,a,v)=∑H'(t,a,v)P*;(t,a,v).
We conclude from the uniqueness of solutions of ordinary systems together
with the initial conditions P'(0, a, v) = 0 that Pi, = 0, P' = 0,
@ = Bk(u,v)dek
k=1
as required.
Our next proof is based on the sketch in E. Cartan [10, pp. 188, 193].
We begin as before with the system
w =d2 -, A'de
(i=l,·.·,r)

---
## Page 114

100VII.APPLICATIONSTODIFFERENTIALEQUATIONS
with the conditions do′=∑0';^ w.We take any smooth curve from
the origin to apoint a.We solve the systemc′=0on the cylinder this
curve spans in x,z-space,taking some definite initial point c on the z-axis.
We shall show that the point on this curve lying over x=a isindependent
of the particular curve we start with in x-space. The point is that in a suffci-
ently small neighborhood of 0 in x-space,any two smooth curves with the
same end points O,a can be smoothly deformed, one to the other. Thus let
x=x(t,0)
x=x(t, 1)
X=x(t,α)be a one-parameter family of curves from O to a,the time variable
toneach curve runningfrom 0 to1 and the parameterαtaking allrealvalues;
x(0,α)=0，x(1,α)=a.
Fixing α,the solution of o′=0 on the corresponding cylinder with initial
value c is given by functions F'(t,α) satisfying
de
Ot
j=1
(Fi(0,α) =c²(i= l,···,r).
We reduce the problem toa two-dimensional oneby considering the mapping
Aq uds-(zx) 0 -(2) 0 
p(t,α)=(x(t,α),F(t,α))=(x,z).
Then
OFi
-da-EA'
：dxi
-dt-EA';
Φ*Ci=OFi
iot
da
2e
H=

---
## Page 115

101
where
aFi
H'=H'(t,α) =
aa
jaa
We set
Φ*0²=P²dt+Q²da
and compare coeffcients of dt dα in
d*∞=∑(*θ)(*∞)
to obtain
OH'
=∑PH.
But
H'(0, α) = α l=0
0F'
—∑4(0,α)
αr=0
d
Fi(0,α)
dx(0,α)
-∑A';(O,α)
da
da
d
op
-∑A'(0,α)
da
It follows that H=0,
We apply this in particular at t = l; here
d
x(1,α)=
d
(t，α)
a=0，
da
da
da
hence
OFi
F'(1, α) = constant.
We next fix the notation more precisely; we write F'(t, α; a, c) instead
of Fi(t, α) so as to specify the dependence of this function on the initial
conditions.Since Fi(1,α) is independent of α we may set
G’(a, c) = F(1, α; a, c),
and also
F=(F,·.·,F"),
G =(G,..·,G).
Then we have the following facts:
(i)G(0,c)=c
(i)For fixed c, a (→ (a, G(a, c)) is a I-1 correspondence on a neighbor-
any curve from O to a and use it to define F and then G.)

---
## Page 116

(ii)Each wi vanishes identically on Ve.(For w′ vanishes on each
curve on V。,since it is a one-form it vanishesidentically.)
We consider the mapping
(a, c) -→ (a, G(a, c)) =(x, z)
on a, c-space to x, z-space.Because of (i),
（x,z)
=1,
（a,c)
of 0.Writing @ in these new coordinates and using (i) shows us that @
involves only the differentials dc',.'·,dd',which completes theproof.
The strikingfeature of theseproofsis thatwereducethe original system of
partial differential equations (with integrability conditions) to a system of
ordinary differential equations.
7.4.ApplicationsoftheFrobeniusTheorem
Example 1:We begin with a question in matrix form which is motivated
by considerations in differential geometry centering around infinitesimal
transformations.
Let Ω = w′lbe an r × r matrix of one-forms defined in a neighborhood
of O, say, in E". We ask when it is possible to find an r × r matrix A of
functions, nonsingular, satisfying
Ω=dAA-1.
To fix matters, let us require the initial value A。 = I. It is convenient to
① =dΩ -Ω2.
Then thebasicresultis this.
There is amatrix of functionsA defined in a neighborhood of O such that both
A。=I and
Ω= (dA)A-1
ifandonlyif
 =0.
When this is the case, then there is only one such matrix A.First of allsuppose
thereisa solution A.Then(dA)A-=Q,dA=QA,and wehave
0 = d(dA) = dQA -ΩdA =(O + Ω”)A -Ω(ΩA) =OA.
Hence OA = 0.Since A is nonsingular we have O=0.If B is another
solution so that dA = ΩA,dB = QB and Ao = B。= I, then
d(B-A)=-B-1dBB-1A+ B-dA
=()+-()-=
hence B-1A is constant, B"-1A = (B-1A)o = I, B = A.

---
## Page 117

7.4.APPLICATIONS OF THE FROBENIUS THEOREM103
Now we come to the existence. We pass to (n + r²)-dimensional space
with cqordinates x，·".,x",2)(1≤i,j≤r)and introduce the r²forms
which are thecoefficientsof thematrix
A=dZ-ΩZ，Z=/
WeareassumingO=O,hencewehave
d=-dZ+ΩdZ=-Ω²Z+Ω(+ΩZ),
'VU=Vp
integrable,hence there exists a matrix A of functions of x with prescribed
initial values at x = 0, so that Z = A is an integral manifold of A = 0, that is,
dA = QA.
Weremark that if Q is skew-symmetric,then A is orthogonal(provided
the initial condition is Ao = I). For we set B = *A-′,the inverse transpose
of A,and have
B。= I,dB= -B(d*A)B= -B*A*QB = + QB.
Example 2. We next consider another equation:
dA =QA-AQ.
Here Q is the same as before, an r x r matrix of one-forms in a neighborhood
of E" and A is the unknown matrix of functions.Again we set ⊙ = dQ-Q2.
Let us pose the problem this way.Can we find a solution A of the above
equation taking an arbitrary initialvalueAo?We seek a necessary con-
dition by differentiating:
py-Uvp-p-Up=（p）p=0
= (O + Q²)A - Ω(ΩA - AΩ) - (ΩA - AQ)Ω - A(O + Q²),
which simplifies to
OA=AO.
Since we are assuming the initial values A。 may be arbitrarily prescribed,
the values of A at each point of a sufficiently small neighborhood of 0 will
fll an n-dimensional domain; the commutativity of ⊙ at such points with
so many different A evidently implies that the matrix O of two-forms must
be of type
①=αl
where α is a two-form.From
=-p

---
## Page 118

104VII.APPLICATIONS TODIFFERENTIALEQUATIONS
we have, differentiating,
p+p-=1p
=-(αI + Ω²)Ω + Ω2(αI + Ω²) = 0.
Thus, locally,α= do where o is a one-form.The necessary condition we
arrive at is this: There must exist a one-form o satisfying
dΩ- Ω² = (do)I.
This can also be expressed another way:The matrix
H=Ω-ol
satisfies
dH-H²=0.
Under this condition, the sufficiency is easily demonstrated.As before
weform
=dZ-QZ+ZQ
in x,z-space,and note that
d=-dΩz+ΩdZ+dZΩ+Zd
=-(Q²+)Z+Ω(T+ΩZ-ZQ)+(T+ΩZ-ZQ)Ω+Z(Q²+)
1+10+Z0-0Z=
hence
dF =ΩF +TΩ,
which shows that the systemIis acompletely integrable one.The existence
proof now proceeds as in the last example.Uniqueness can be handled this
way.Since the systemI= O is in normal form and is completely integrable
we know there is a unique integral surface passing through a given initial
point Zlo = Ao.
Example 3. We shall consider a type of system of partial differential
equations known as a system of A. Mayer (see C. Caratheodory [6, pp.
26-31]).
We work in a neighborhood of O in Er+s with coordinates x',."·,x,
2,..·,2as before and aregivenfunctions B'(x,z),i = I,·.·,r,j = 1,·.· ,8.
The Mayer system is
 = B'(x, z).
We define
B'B
B-
OB

---
## Page 119

7.4.APPLICATIONS OF THE FROBENIUS THEOREM105
We evidently have A'+A'= 0.The Mayer system is called completely
integrableina neighborhood of 0provided to each choice of initial conditions
c there exists a solution z = F(x,c) of the system with F(0,c)= c.The
necessary and sufficient condition for complete integrability is precisely
A'jk = O. The reason is the following. We set
o=dx-B;(x,z)dx(i= 1,.,r)
a system of one-forms in x, z-space in our standard form. The vanishing
A'jk = O implies, after a short calculation,
sothat the system @',·"',w'is completely integrable.Theintegral
surfaces Z = F(x, c) solve the Mayer system. Conversely, suppose the
Mayer system is completely integrable.Then it is clear that the system
w′=·.·=w'=0 has integral surfaces,one for each choice of initial
conditions c.Hence the necessary condition
dw=∑0;∞
must be satisfied.On the other hand,we directly verify that
d=Adxdx+n∞
where
n=2
dx.
Since dx',..·,dx,@',.··,@ are linearly independent we conclude that
0; ^w =∑n²a∧∞,∑A'kdxdx*=0,A'k= 0.
Note. If o', .·', w' is completely integrable, there is an r x r matrix of
one-forms ⊙ = |0';Il satisfying
dw' =∑0;^∞,
or
dw=-w
in matrix notation.However,from the solution
w=dgF， g=(g',···,g)，F=llf'l
the very special form O = F-1 dF. (This provides some motivation for the
problem in Example 1.)
We shall see further applications of the Frobenius theorem in our study of
local Riemannian geometry. Also cf. Problems 4-7, p. 194.

---
## Page 120

106
6VII.APPLICATIONSTODIFFERENTIALEQUATIONS
7.5.Systems of Ordinary Equations
We consider a system
de1
=X1(t,x，...,a")
dt
den
X"(t, x',..., x").
dt
=
Closely associated with this system is the differential n-form
Ω =(dx1 -- X1 dt)···(da"  X"dt)
in (t, x)-space. By a short computation,
ax
dΩ=
dt dx...da".
dx
We make a change of variables
y'=y*(t,x,...,a")
(i=1,..·,n)
and suppose that the systems
de'
dy'
Xi(t,x)
and
Yi(t,y)
dt
dt
are equivalent under thischange.We set
 =(dy - Y dt)···(dy”- Y"dt)
and propose to determinehow dQ and dare related.Now
dy'
,he
oydei
p
at
+
,he
dy
e
Also
dyi
dy
dy'
Ot
hence
dyi
We denote the Jacobian by J:
d(y',...,y")
d(x，...,x")