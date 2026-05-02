<!-- OCR chunk: flanders_differentialform.pdf pages 151-180 (of 219 total) -->


---
## Page 151

8.4.RIEMANNIAN GEOMETRY,HARMONICINTEGRALS137
The significance of the sign will appear shortly.We note that So is a
(p - 1)-form when @ is a p-form. If @ = f is a zero-form, or function, then
8f = 0.The final operator we define is the harmonic operator (generalized
Laplacian) according to
=doo+8od.
We henceforth restrict attention to a closed (compact) manifold M.We
denotebytthevolume element,an n-form on Mwhichnowherevanishes
and which satisfies t = o, ... o, locally.
We propose to turn the spaceof p-forms on Mintoan(infinite dimensional)
inner product space.If w and n are two p-forms then w ^ *n is an n-form
andwe define
①*n.
JM
Thisisevidentlylinearineachvariable andwehave
(w,n) =(n,∞0),
a consequence of
*=*（).
Locally, if
@=∑ano",
then
W *=(∑a²)t
hence
(∞,0)=0
and (w, w) = 0 if and only if @ = 0.
We shall now establish thefundamental formula:
If w isap-form andna(p+1)-form then
(dw, n) = (@, on).
Forweintegrate over the closed manifold M the relation
d*n+（-1）cd*=d(c*n）:
dc^*+（-1）p
①d*n=
d(w^*n)=
①*=0,
JM
M
/M
oM
(d∞,n) =(-1)p-1
①∧ d*n.
M
Since d*n is an (n - p)-form, we have
**(d*n）=#（*d*n）=(-1)(n-D)d#n
so that
(lu*p*)*(d-u)a(I-)-a(I-)=u*p-d(I-)
=(-1)np+1#(*d*n).

---
## Page 152

138VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
But n is a (p + 1)-form, hence
h*p*+d(-)=lp*+u+（1+d)u（-)=ug
andso
(-1）p-d*n=*on,
JM
M
Aform@iscalledharmonicprovided
△w=0.
It is clear that if the p-form w satisfies the two equations dw=0, 8o = 0,
then w is harmonic. The converse is also true. Indeed, if w is any p-form,
then
(△∞,∞)=(d∞,@) +(od∞,@)
= (8∞, 8@) + (dw, do).
Nowif w isharmonic,then△w=0,
(∞, ∞) + (d, d∞) = 0.
But each term is nonnegative, hence each vanishes, (dw, dw) = 0, (oo, 8@)
=0 and this implies in turn that do=0,o=0.
The operators d, 5, act on the space of p-forms. The relation (dw,n)
=(o, on) may be interpreted as saying that d and  are adjoint to each other.
We next see that △, which maps p-forms into p-forms, is self-adjoint,
(△,n) =(@,△n),
indeed, either side is (dw, dn) + (b, n). Since (△o,@) ≥ 0 with equality
only when △o =0, we are entitled to call  a positive definite (or elliptic)
self-adjoint differential operator.
We may now state Hodge's main result,a deep theorem in harmonic
analysis:
If w is any p-form then there is a (p - 1)-form α, a (p + 1)-form β and a
harmonicp-formy such that
@= da + β+y.
The forms da, 8β, y are unique.
The proof that α,β,and y exist is difficult.We shall only settle the
uniquenesspart.Supposewehave
dα+8β+y=0.

---
## Page 153

8.4.RIEMANNIAN GEOMETRY,HARMONICINTEGRALS
139
We then have d(da) = 0 and also dy = O since y is harmonic.Hence
dβ=0,
(dβ,β) = 0,
(β,8β) = 0,
β=0,
dα + y =0.
Similarly da =0,y= 0.
By an almost identical argument one shows that in case w is a closed
p-form, dw = 0, then the term 8β in the Hodge decomposition of w is absent.
①=da +y.
It follows from this that if z is any p-cycle,then
=∞
y，
Jz
Jz
that is, y has the same periods as does w. (See De Rham's theorems,
Section 5.9.）The result of this is that if w is any closed form, then there
ecistsauniqueharmonicformy withthesameperiodsas thoseof@.
We can also answer the following question.Given a p-form X,when is
thereap-formrsuchthattheequation
n=
is satisfied?The answer is: if and only if
(y,)=0
for every harmonic form y.
For suppose Λ = △r and y is harmonic.Then
(y, 2) =(y, △n) =(△y,n) =(0,n) = 0.
On the other hand, suppose is a form satisfying (,)=O foreach harmonic
form y.From the decomposition
=dα++
we have, using the particular y which is part of ,
0 =(y,) =(y,dα) +(y,8β) +(y, 2)
=(6y,α) +(dy,β)+(y,v)
= (y,v),
hence  = 0,
1 = da + β.

---
## Page 154

140VIII.APPLICATIONS TODIFFERENTIALGEOMETRY
We shall setn=μ+v and try to solve △μ=dα,△v=8β,separately.We
take the first
△μ = da.
Decomposing α,
α=da+β+y1,
da =d1.
Next,
β=da2+oβ2+y2,
dβ=d da2=(d8+od)(da2)=△(da2),
dα=△μwithμ=da2.
We find v similarly.
Example .1. E".We shall compute the operator △ in E".Contrary to our
previous notation in dealing with the standard Laplacian,we shall denote the
Laplacian by Lap,
.=n=ndeI
0²u
The result is this: if
@= ∑anda,
then
△@ = -∑ (Lapan)dxH.
Itwill sufficetoestablish thisfor themonomial
① = Adr ...dxP.
We shall abbreviate the calculationby these conventions:
(1) subscripts on A denote partial derivatives;
(2)α=1,2,...,p,j=p+1,..·,n;
(3) each repeated index is summed over its range.
We also remark that in taking the star of a monomial,the choice of sign is
always governed by the rule n^ *n=Bdx..·dx”where B>0,for
example,
*(dxdp+1..·da... da")=(--1)+p+a+idx...d...dxPdx.
Another point: since @ is a p-form and dw is a(p +1)-form,
00 = (-1)p+n+1*d *(0,
d=(-1)p+1d*dc.

---
## Page 155

8.4.RIEMANNIANGEOMETRY,HARMONICINTEGRALS
141
Wehave
*0 = AdxP+1 ... dx",
d*0) = Aαdxda+1 ..· da",
*d*(0) =(-1)mp+n+a+1Aadx .dx.. dxp,
@0 =(-1)Adx...da..da,
dod = --Aa det .. dxP + (--1)a+p++ Aay dax' ... dxa .. deP dev.
Next,
dw = A;dxida ... dxP,
*do =(-1)+1A;dap+...dx)..dx,
ddo=(-1)PAydap+...d+(-1)+Adx~dx+.....da",
#d *deo (-1)mPAy;dat .. deP + (-1)mp+p+a+ Ayadx...da ..daxP dax,
odo = --Ayde..· dxP +(-1)p+aAadx..·da... dxP de.
Combining these expressions,
△@ = d8@ + od@ = -[Aaa + Aj)]dx1 ... dcP
=-(LapA)dx...dxp.
Theminus sign seems strange inview of the relation
(△∞,∞)≥0
on closed manifolds. An example may clear this point. Let us take the
zero-form sin x on the fat torus 0 ≤x, y,2≤ 2n, where numbers are identified
if they differ by a multiple of 2n.Then
d(sinx)= (cosx)dx
*d(sinx) = (cosx)dy dz
d *d(sinx) = -(sin x)dx dy d2,
*d *d(sinz)= -(sin x),
△(sinx)=0d(sinx)=+sinx,
2元
(△(sin x), sinz) = (2π)2
sin²x dx = (2π)²π > 0.

---
## Page 156

142VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
We have used the fact that d(sinx) is a one-form, n = 3, p = 1,
[d(sin x)] = (- 1)mp+n+ 1(* d*)d(sin x) = -*d *d(sin x).
Example 2. S2. If f is a function on E3, we have the spherical coordinate
form of the Laplacian (Section 4.4, p. 40),
Suppose thatLapf=O and thatfis of theform
f(r,Φ,0)=rg(Φ,0).
Then g is called a spherical harmonic and must satisfy
a
( 9e
n(n + 1)(sinΦ)g +:
[(sinΦ)g$]+
pe
(use
0
The function g may be considered as a function, or zero-form, on S²,the unit
sphere.There we have
0= dΦ，
02= sinΦ d0,
dg=901+
9
sin
*dg=
0+92
sin
9e
dΦ + (sin Φ)gd0,
sinΦ
d*dg
9
a
[(sin Φ)g]dΦdθ
00sinΦ
pe
(sinΦ)g)
sin0（sinΦ）
0102
1.[0(9
*d*dg
a
sin0（sinΦ)
(ggsin
a
But
g =(d8+ od)g =odg=-*d *dg,
so the condition for g to bea spherical harmonic is
△g -n(n + 1)g = 0.
In otherwords,the spherical harmonics areeigenfunctionsforthegeneralized
Laplacian on S2.Many of the usual facts about spherical harmonics
follow from our calculations.We take one example,the orthogonality

---
## Page 157

8.5.AFFINE CONNECTION
143
relation: If g and h are spherical harmonics of distinct degrees m and n,
respectively,then(g,h)=0.
For△g=m(m+1)g,△h=n(n+1)h,hence
1
1
(g,h)=-
(NV 0) (I + u)u
n(n+1)
(g,h),
m(m+ 1)
(g,h) = 0.
8.5.AffineConnection
We shall approach the problem of affine connection this way.We seek
displacement ofvectorsalong curves ispossible.Considerablyless than a
Riemannian structure is required.
Let M be a manifold.An affine frame (or simply frame) on a neighborhood
U of M consists of n vector fields e1,.".,e, on U which are linearly
independent at each point of U.Thus at each point P of U the vectors
(et)p,·".,(en)p furnish a basis of the tangent space T at P. There is a
dual basis o',···,o” of one-forms on U so we may write
dP=Eoie;
aswedidfor theRiemanniancaseinSection8.3.
WenowwanttoassociatewitheachvectorfieldvonMavectorfielddv
withone-form coeffcients.Wemustbeabletodothisforthevectorfields
e; of the basis, so we require
de;=∑∞}'ej,
where the ware one-forms on the neighborhood U.There are certain
consistency conditionswhichguarantee that the computation of dvwill be
independentof anyframe.
Locally we may describe an affine connection as follows.We are given
U, the affine frame el , *.. , en, and the dual basis o', ... , o" of one-forms.
An affine connection consists of n² one-forms w; subject to no constraints
whatever.
Weshall develop some ofthelocalgeometryofanaffine connectionbefore
attacking the crucial problem of finding proper consistency conditions which
make the definition of an affine connection over awhole manifold possible.
By introducing matrix notation:
/e1)
@11...@1n
=(o²，···,o"）)，Ω=
：
u..."∞

---
## Page 158

144VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
we maywrite ourbasic structure equations:
dP = oe, de = Ωe.
Weshallquicklypointouttherelationtothecustomary tensorformulation
of an affine connection.First we expand each win the basis o*:
=∑rko,
defining the connection coeficients F/k.In the usual tensor formulation,
the frame e1,·`·,e, stems from local coordinates:
a
='
and correspondingly, o' = du'. The F = F/(u,."·,u") are then n3
arbitraryfunctions assigned on U.
We derive relations by differentiating the structure equations several
times.First
d²P = (do)e -ode = (do - oΩ)e = te.
Here
t=(t',...,t")=do -oΩ.
The two-forms t' are the torsion forms.We may write
t'=∑To，T+T=0,
defning the torsion coeficients T'jx. Next,
d²e = (dΩ)e -- Ωde = (dΩ - Ω²)e = e.
Here
ll=-p=
is the matrix of curvature forms 0.The curvature tensor Rk: is obtained
from
0=∑Roo'，R+Ru=0.
Integrability conditions are obtainedby applying the exterior derivativeto
the equations  = do - oΩ and ⊙ = dΩ - Q²:
dt=(-do)Ω+odΩ
=-(π+Ω)Ω+a(+Ω²),
d=oθ-tΩ,
and
p+(p-)=Op
“++(+)-=
d0=Ω0-0Ω.

---
## Page 159

8.5.AFFINECONNECTION
145
Ifvisavector field,then
v=∑f²e;=Fe,F=(f,···,f"),
where thefiare scalars;we have
dv=(dF)e+F(de)=(dF+FQ)e.
Suppose the vector field v is defined over a submanifold.It is said to move
by parallel displacement if dv = O, i.e.,
dF+FQ=0.
If P = P(t) is a smooth curve on U defined over an interval to ≤t≤t, of
the t axis, if v。 is a tangent vector at P。 = P(to), then there exists a unique
assignment of a tangent vector v(t) at P(t) for each value of t such that
v(to)=Vand v(t)moves by parallel displacement.
For we write v=∑f'ei. Along the curve the conditions for parallel
displacementbecome
=0，
a first order linear system which taken with the initial data determines the
f'uniquely.
Nowwe tacklethe global situation.We have a manifoldM in front of
us and we must consider each conceivable moving affine frame e1,.",en
togetherwith itsneighborhoodof definitionU.Witheachone of thesee
wehave anaffine connection,i.e.,an nx n matrixQ of one-forms on U.
We want these to“fit together”whenever two such neighborhoods overlap.
Thus let (U,e,o,Q)be one such system and (U,é,,)another,where
we assume the neighborhoods U and O overlap.The basic thingwerequire
is that for any vector feldv defined on the intersection of U and O,the
computationfordvineitherconnectionmustyield thesameresult.
On the overlap,where we shall always operate in what follows,
é =Ae
where A = Ja/ll is a nonsingular matrix of functions. Since
dP=é=e,
wehave
Ae = oe,
=0A-1.
Now
dé = d(Ae)=(dA)e + A(de)
= (dA + AΩ)e
=(dA +AQ)A-é.

---
## Page 160

146VIII.APPLICATIONSTODIFFERENTIALGEOMETRY
Butalsode=Qe,sowehavethetransformationlawforQ:
= AQA-1 + (dA)A-1.
Thisisquite differentfrom thetransformationlawforowhich isforced
by the very definition of manifold andframe.Ittells ushow the various
matricesQweareassociatingwith thevariousmovingframesemustbe
related ifwearetodefinean affineconnectiononMasawhole.
From theseformulasonecanderive thetransformation lawsfortandO:
=TA-,
 = AOA-1.
Ifv = Fe = Feis a vector feld, then F = FA-,
(dF+F)é
(+)+()=
= (dF + FQ)e,
sothatdvisthe same,either way itis computed.(Wehaveused therule
We shall now have a second look,only in our present context,at the
considerations of Section 4.3. This will provide us with another way of
looking at affine connection.What we shall dofits into a general pattern:
quantitiessubjecttoatransformationlawbecomeabsoluteinvariantswhen
considered on a suitably extended space.
F of dimension (n + n²).This frame manifold consists of all frames at all
points of M.Precisely, at each point P of M consider all possible bases
e1,.".,e, of the tangent space Tp at P, and do this for all P.
We obtain coordinates on F this way.First let U be a local coordinate
neighborhood on M with coordinates u',.··,u". Pick a moving frame
e1,*"., e, on F. Thus at each point P of U, (e)p,.",(en)p is one basis
of the tangent space Tp at P.The most general basis of Tp stems from this
f,....f,where
f=∑b·(e)p
with b/l an arbitrary n x n nonsingular matrix. It is clear from this
thatthe(n+n²)independentvariables
u,...，u",bi
serve as & coordinate system for the neighborhood in F consisting of all
frames at all points P of U.

---
## Page 161

8.5.AFFINE CONNECTION
147
With the moving frame e1,"., e, on U goes the dual basis o', ... , o"
of one-forms on U.The forms ,..·,o" defined by
=αB-1,
where
=(o,···,o”)，=(,···,o"),B=b//l,
are one-forms on the part of F lying over U. More precisely, the values of
theforms',..·atthepointfof Fgiven by
f=∑b（ej）p
are
=(olp)B-1.
Now suppose that O is a second coordinate neighborhood,é a moving
frame on O, etc.. Suppose that P lies both in U and in O. We have
e=Ae
where A is a matrix of functions,
=oA-1,
allworkedoutabove.If thepointfof Fhas coordinatesBwithrespectto e
and B with respect to é,then
Be =Be =BAe,
B=BA.
Thus
= αB-1 =(A)(BA)-′=B-1.
Thisimpliesthattheone-forms,...,”aredefinedonallofFandare
completelyindependentoftheparticularlocalcoordinateneighborhoodsand
movingframesusedintheirdefinitions.
This is of first importance.We began with an n-manifold M.We
constructed over it a new manifold F. On this new manifold we auto-
matically have, free of charge, the n (linearly independent) one-forms
o',...,”.
hood U with a definite affine frame e is given a matrix Q = llw'll of one.
forms. The matrix Q corresponding to the frame é on O is related to Q
(on the overlap of U and O) by a certain transformation law. This trans-
formation law means nothing more nor less than that the n² one-forms @?
defined by
Q=/l= BQB- + (dB)B-1,
apparently defined only on the part of F lying over U,are defined on all of
F, are completely independent of e and its U.

---
## Page 162

148VIII. APPLICATIONS TO DIFFERENTIAL GEOMETRY
This statement may be verified by a calculation.According to the nota.
tion above,one mustprovetheformula
We leave the details to the reader,but point out that the result can be
motivated by a symbolic calculation:
f =Be,
df=(dB)e+B(de)=(dB+BQ)e
= (dB + BΩ)B-f,
similarly
(+)
hence
(dB + BQ)B-1 = (dB + BQ)B-1.
From the one-forms ',..·,@ on F, one constructs two-forms ',0
according to
=(t,...,t)=d-,
 = 0/l = d - 2.
8.6.Problems
1.Let E be a closed convex surface with constant mean curvature H.
Prove thatE is a sphere.
2. A surface Z is given in the Monge form z = f(x, y), defined for all x, y.
We suppose this surface is convexfrom below.Show that this means that
(r8)
is positive semidefinite.
3.(Continuation.)Show that the mapping
(x,y)-→(x+p，y+q)
increases distance andhenceis one-one.
4.Apoint ofahypersurface is an umbilicif the transformation Aat that
point has all of its characteristic roots (principal curvatures) equal.Let M
be a hypersurface all of whose points are umbilics. Prove that M is &
portion of a hyperplane or sphere.
5.Suppose on aRiemannian manifold M there is a scalarK such that
0=-Ko;oj
Prove that K is a constant.

---
## Page 163

8.6.PROBLEMS
149
6.Let M be a manifold with an affine connection given.Show that
thetwo-formαdefinedlocallyby
α=θ=trace
is actuallydefinedon allof M,independentoflocalframes.Showalso that
da=0.Itiseven true that there existsa one-formonM such thatα=d,
butthisisdifficulttoestablish.
7.(Continuation.）Prove
d0'=Ω0'-0'Ω
andthat
d[trace(O")]=0.
8.LetMbe amanifold with affine connection.Givenan affine frame
e1,·"·,e,_ with corresponding connection coeffcients F and torsion co-
efficients T，define & newconnection by specifying the new connection
coefficients r*:
r*k=r/k+T'k.
ShowthatthisindeeddefinesaconnectiononallofMandthatthiscon-
nection is symmetric (no torsion). Investigate the meaning of “symmetric"
for a local coordinate frame.
9.Consider the flat torus T" which consists of all points (x1,""·,x)
where each x;is taken modulo one.That is,(x1,·"·,xn)=(y1,·"·,y)
  A u i   o ('... I = )  = 2 
normal basis
01=dx,·.·， on=dxn
of one-forms.(In older notation, [ds]² = [dx,}² + ·.·+ [dx,]².） Find all
harmonicdifferentialsofalldegrees.

---
## Page 164

IX
Applications to
Group Theory
9.1.LieGroups
A Lie group consists of a smooth manifold G which has a group structure
(x,y) -→ 2y.
We suppose that this group operation, which may be considered as a mapping
GXG-→g,
is smooth and also that the map x—→x-1 on G—→ G is smooth.
With each elementxin G,there isassociated a transformation Lof
G,called left translation:
Lx(y) = xy.
A differential p-form w is called left invariant provided
L*W=W
for all r in G.
Let e denote the unit element of G. The left translation Lx-1 = Lx-1
sends x to e. If w is left invariant, @ = L*-,@ is completely determined at 2
by its value wo at e.If wo is any given p-form at e, then a left invariant
form (w is defined by
Wx = L*-Wo.
These remarks serve todetermine theexistence ofleftinvariantforms.
Letusbeginwith one-forms.Weletnbe thedimension of G.Since the
space of one-formsateisan n-dimensional linear space,there are exactly n
linearly independent left invariant one-forms on G.Let
o',..·,o”
be suchasystem.Any otherleftinvariantone-formisalinear combination
ofthesewithconstantcoeffcients.
More generally, if w is any left invariant p-form on G,
W=∑CHOH,
150

---
## Page 165

9.2.EXAMPLESOFLIEGROUPS
151
where the ch are constants and oH = ou ..-o*r. Any p-form @ can be
expanded in this way and the coefficients Ch will, in general, be scalars on G.
Supposing w left invariant forces each of these scalars to be left invariant.
This means that each cg takes the same value at each point of G,hence is
constant.
Next,if wis left invariant,so is dw,since
Lx*(d) =d(L*@) = dc0.
It follows that there are constants of structure c' such that
do²=∑c²o，c²jk+ckj=0.
Substituting this into the relations d(do')== O eventually yields
∑(cks+c²rsk+c²jsk)=0.
Particularly important is the n-form
g1 ...on
which defines a left invariant volume element on G.It is clear from this
that G is orientable.
The right translation R. associated to a group element z is the mapping
y -→ R,y = yz
on G to G.From the associativelaw
x(yz)=(xy）z
we deduce that
LxoR=RoLx,
hence
R*。L*=L*。R*.
Suppose w is a left invariant p-form. Then for each x and z,
L*（R*∞）=R*（Lx*∞)=R*W,
hence R,*w is also a left invariant p-form.
9.2. Examples of Lie Groups
Example 1. n = 1. We shall determine the local structure of all one-
dimensional groups. Let t be a parameter on G, chosen so that t = O is the
identity e. Let o be a nontrivial left invariant one-form; locally,
0 = f(t)dt,，never zero.
We integrate o to get a new parameter for G,
f(t)dt.

---
## Page 166

152
IX.APPLICATIONSTOGROUPTHEORY
Thus we may assume we have started with a parameterization of a neighbor-
hoodofebyasinglevariabletsuchthat
p=0
isaleftinvariantform.
We next express the group product analytically.The product of the
point with coordinate s with that of coordinate t will have coordinate u
givenby
u = p(s, t)
with
p(s,0)=8，p(0,t)=t
according to xe = x,ey = y. In coordinates,
L,:t-→u=p(s,t).
The left invariance of o,L*α=o,means
dt=
ap
e
dt,
hence
dp
= 1， p(8,t)=t+Φ(s).
Ot
Setting t = 0:
8 = p(s, 0) = Φ(8),
and so
p(s,t) = 8 +t.
It follows that thegroup operation corresponds to nothing more than ordinary
addition of coordinates.As a corollary,G is abelian(commutative).
Example 2.G is a group for which the constants of structure c' all vanish.
Thus
do' = ... = do" = 0.
Ina small neighborhood of é,
‘np=
taken so that (0, 0,···,0)←—-→e. The product of points with coordinates
u,v,respectively,is a point with coordinates wgiven by
w² = p’(u, v)
with
p’(u, 0) =u',p’(0, v) =v.
Theinvarianceofo'under thelefttranslation
v~→w， w²=p'(u, v)

---
## Page 167

9.3.MATRIXGROUPS
153
is expressed analytically by
which implies
=I
p’(u, v) = u + Φ′(u).
Setting v = 0 yields
u²= b'(u),
hence
p'(u, v) =u + u.
If P(u) denotes the point with coordinates u, this says
P(u)·P(v)=P(u+v)
so that locally the group looks like a neighborhood of O in E".
Corollary.G is abelian.
9.3.Matrix Groups
Now we shall consider a group G which is a smooth subgroup of the group
GL(m) of m x m nonsingular matrices.(The notation stems from the
commonname,generallinear group.)
Suppose u',.··, u" is a coordinate systemonG in some neighborhood of I,
theidentity matrix,and that X = X(u',···,u") is a typical point in this
neighborhood.The matrix dX of one-forms certainly contains n linearly
independent one-forms because the n-dimensional group G is smoothly
imbedded in GL(m).Consequently the matrix
Ω=X-dx
of one-forms contains nlinearlyindependent ones.But each element of Q
is left invariant.For if A is any fixed element of G,the left translation
by A is given by
X -→AX,
while
XP-X=(xpv)(,-V-x)=(xv)p-(xV)
Nextwe note an importantgeometricinterpretation of Q.Weinterpret

---
## Page 168

154
IX.APPLICATIONSTOGROUPTHEORY
each element X of G as a linear transformation on the space E" of row
vectors v=(v,"·,).Thus
V-→ w =vX.
We ask, how does dw grow out of w under the group action? Here v is
fixed andXvaries over G.Wehave
dw=vdX=(wX-1)dX,
dw = wΩ.
This means Q can be interpreted as an “infinitesimal group element."
(Cf. Section 4.2.)
One final remark. The constants of structure can often be explicitly
obtained from these considerations:
Ω=X-1dx
dX = XΩ,
0=d(dx)=dXQ+XdQ
px + (x) =
Hence,
dΩ + Ω²= 0.
9.4. Examples of Matrix Groups
Example 3.
the proper affine group on the line.One easily sees the isomorphism between
G and the transformation group
t-→ at + y.
Here
x=(),x-=-)
()=()(- =5
Hence o = dx/x, o² = dy/x are left invariant. The left invariant volume
elementis
=
dxdy
x2

---
## Page 169

9.4.EXAMPLESOFMATRIXGROUPS
155
Since do1 = 0, do² = -dx dy/x²= -o ^ o², the only significant constant
ofstructureis
c²2=-c2 =-1.
If we seek right invariant forms,we find them in
1/dx
1/dx
：-ydx+xdy
(dx)x-1=
0
x0
0
so a basis is
dx
α=α1
α² = -ydx + xdy
The right invariantvolume elementis
dxdy
x
very different from the left invariant one.Also
dxdy
dα²
αα².
x
We shall compute the effect on o²of the right translation R,where
We have
R(X)=XA
d(bx+y)
bdx
R*o² =
ax
ax
ax
a
Example 4.The step transformation group of all matrices
x>0.
1(xdxxdy-ydx)
Q=X-1dX =
xdx
We may take
dc
α1
 d(lnx),o² = xdy -ydx
x2
The choice of new coordinates
u=lnx,
y
=
follows the procedure in Example 2.

---
## Page 170

156
IX.APPLICATIONSTOGROUPTHEORY
Thus
x=(% )==( i).
JI
A=<(0 i)
is another, then
AX =e+(1 b+∞).
1)
0
The invariantvolume element is dxdy/x²=dudu.
Example 5. G =GL(n), the general linear group of all nonsingular n × n
matrices. The general element is X =x/ll where the x are independent
variables(subject to the inequality= det(x)≠ O).Set
△
Wehave
Q =x-1 dx =lo*ll,
where
=yda.
The n² left invariant forms o are necessarily linearly independent. We
computethevolumeelement
ol=1
in two steps:
T=vA...v",
=..·=
(ydx)..(ydx)
】
det (y+)dx,* ... da.*.
△”
From XY = △I we have det(X)det(Y)= △", hence
det(Y) = △-1,
=
1
II (dx...da).

---
## Page 171

9.4.EXAMPLESOFMATRIXGROUPS
157
It is clear from this that the right invariant volume element will also be t,
which is an unusual feature of this group since itishighly non-abelian.
Example 6. G = SL(n), the special linear or unimodular group of all n × n
matrices of determinant one.The special feature we shall note is
trace (Ω) = 0.
This follows from a general formula for a matrix functionX of any number
ofvariables.Set = det(X).The formula is
d
：trace(X-1dX).
This is proved as follows.Denote by
x
the jth column of Xand consider
△= det(c,..·, c")
as a function of the columns.Then
d=
∑△（c,.·.,e-1,de,cj+1,...,e”)
后台
=trace[△x-1dX}=△trace(X-1dX).
For G =SL(n) we have △ = 1, d△ = 0, hence trace(Q) = 0. For n = 2 we
have
=xv - yu = 1,
()
Ω = x-1dx =
vdx-yduvdy-ydu)
-udx+xdu-udy+xdu)
Differentiating =1 yields
xdv+ vdx-ydu-udy=0,o+o4=0.

---
## Page 172

158
IX.APPLICATIONSTOGROUPTHEORY
For theleftinvariantvolume elementwemay take
=oo²o²=dxdu(vdy-yde)
=vdx dudy - ydx dudv.
Example 7. G = 0+(n), the proper orthogonal group of all n × n matrices
X for which
'X =X-1，det(X)= +1.
Here the superscript t denotes transpose.The essential feature about Q is
thatit is a skew-symmetric matrix,
Ω+Ω=0.
Because the group G has dimension n(n - 1)/2, it follows that the elements
above the main diagonal in Q form a basis for left invariant one-forms and
their product is the left invariant volume element.We establish this
property of Ω as follows:
XX=I,(dx)*X+X"(dX)=0,
x-1dx +"(dx)'x-1 =0,
x-1dx+′(x-1dx)=0,Ω+'Q=0.
For n = 2,
cos0sin0
X
-sinθcos0]
cosθ-sin0\/-sinθcos0
Ω=X-1dx =
sinθcos0/-cosθ-sin0)
de
For n>2the calculationbecomes complicated and hinges on explicit
parametrizations of G.The cases of even and odd n are rather different.
9.5. Bi-invariant Forms
We take aLie group Gwith identity element e.Because G is a manifold,
thereisacoordinateneighborhoodUofewithalocalcoordinatesystemsuch
that the coordinates of e are(o,O,·..,O).Suppose x and y are very near
to e and in U.Then z = xy is in U.If the coordinates of these three
points are (x,··,x”),(y,.··,y”),(z,.··,2”), respectively, we may write
2²=x（(x',···,x，y,.··,y”).
Since xe =x and ey = y,we have
z'（(x,···.,x”,0,···,0)=x',
z(0,.·.·,0,y,..·,y")=y',

---
## Page 173

9.5.BI-INVARIANT FORMS
159
and because of these facts,
2′ = x* + y' + (higher order terms in the x' and y*).
In particular, if y = x-1, then z = e, and
0 = x²+ y’ + (higher order terms).
We apply these simple remarks as follows. Let w denote the mapping
y(x)=x-1,
:G-→G.
If we write
y=y(x),
y²=y’(x,...,x"),
thenbytherelationjustdiscussed,
y
This means that
y' = -x' + (higher order terms in the x').
We may also express this another way:
:(x,···,x")-→-(x',···,x") + (higher order terms).
Since y(e) =e1 = e, the induced mapping w* takes each differential form
at e to another form ate.Evidently we have
y*(dxr)=-dx²(at e),
y*(dx..·dx)=(-1)(dx..·dx)
(ate).
Thus if we is any p-form at e, then
4*(@e) =(-1)Pwe.
For each y in G, the right translation R, was defined by
R,(x) = xy.
A form @ is called right invariant if
R,*∞=∞
for each y in G.Our first application of the map  is the following:
A form @ is left invariant if and only if 4*w is right invariant.
For
y(R,(x)=4(xy)=(xy)-1=y-x-1
((x))-T=(-x)-T=

---
## Page 174

160
IX.APPLICATIONSTOGROUPTHEORY
hence
。R,= Ly-io,
R,*。μ*=*。Ly-1*.
If w isleft invariant,then for each y in G
R*(*(0)=4*(Ly-*∞）=4*,
hence y*@ is right invariant.Similarly, if w is right invariant then y*@ is
left invariant. Since (x-1)-1=x,。=1 and so w*(μ*∞)=0. It
follows thatify*wisrightinvariantthen wisleftinvariant.
Next we shall see that using right invariant forms instead of left invariant
ones does not give additional constants of structure. For let o',···,o" be a
basis of the left invariant one-forms. Then the corresponding constants of
structure are read from the equations
do=.
The forms t = y* o', .'· , t” = y* o” are now a basis for the right invariant
one-forms. But y* applied to our equation yields, since the c's are constants,
“V)=（p）
(）（)=（）p
dt²=∑ct.
Now we pass on to the study of bi-invariant forms, i.e., forms which are
both left and right invariant. We derive one important result.
Letwbeabi-invariantp-form.Then
dw = 0.
For y*w isleft invariant since w is right invariant.We know from our
calculation on the previous page that at the point e,
y*(@e) =(-1)∞e.
But w and y*(w) are both left invariant,hence what is true at e is true
everywhere,
*(∞)=(-1)P∞.
On the other hand, do is a (p + l)-form, also bi-invariant, so the same
conclusion applies:
y*(d∞)=(-1)p+1dco.
But,
y*(d∞)=d(μ*∞)=d[(-1)∞]=(-1)Pd).
From these equations follows dw = 0.

---
## Page 175

9.6.PROBLEMS
161
We apply this to the case in which G is a commutative group.Then the
leftand right translations are the same thing so that eachleftinvariantform
is bi-invariant.In particular if o',...,o”is a basis of left invariant one-
forms, each do' = 0; the constants of structure all vanish. In Example 2
of Section 9.2 we showed that any group with vanishing structure constants
has the local structure of Euclidean space (and incidentally is commutative).
Here is one more result on bi-invariant forms which goes in a different
direction.
Let G be an n-dimensional closed(compact）Lie group and let w bea left
invariant n-form on G.Then @is bi-invariant.
For each x in G,R*w is also left invariant.Assuming @≠0,we have
R*∞=f(x)w,wheref(x)is areal number,since the space ofleft invariant
n-forms has dimension one. Because R*.R,* = Ryx*, we have f(xy)
=f(x)f(y).(Real numbers commute!) Now f(x)never vanishes since
1 = f(e)=f(x)f(x-').Thus f maps G into the reals R with 0 removed.
Since G is compact the image of G underfis a bounded interval in R,
ofpositiverealssincefpreservesmultiplication.[Positivebecausethe
since a”mustremainintheintervalf(G)whichis closedundermultiplication.
Hence f(G) consists of 1 alone,f(x)=1 for each x in G,R*w = W,w is
bi-invariant as asserted.(Wehave used the fact thatGis amanifold,hence
connected,toconclude thatf(G)is an interval.)
9.6.Problems
1.Let C* denote the multiplicative group of nonzero complex numbers.
Find theinvariantvolume(area)element.
2.Considerthe4-dimensionalgroupofallmatrices
2W
0
where z and w are complex numbers, z ≠ 0. Determine constants of struc.
ture.Showthattheleftinvariantvolumeelementis
一(dzddwdw)/z1.
Here dz = dx - idy if dz = da + i dy.
3.Discuss other groups of complex matrices analogous to the examples
of Section 9.3.For example, discuss the relation between unitary matrices
andskew-hermitian ones.
4.Extend the coordinate considerations of Section 9.5 by showing that
2 = x²+ y’ + ∑a²sx'y* + (terms of order three and higher).

---
## Page 176

162
IX.APPLICATIONSTOGROUPTHEORY
Showalsothat
(a'jk-akj)
are the constants of structure for a suitable basis of left invariant one-forms.
Compare xy and yx.
5.We know that each left invariant p-form can be expressed in terms of
left invariant one-forms. Does a corresponding result hold for bi-invariant
forms?
6.Let c'jkbe constants of structure of agroup and set
Show that gjn is a symmetric tensor. Now set
Ciyk=cyguk·
Show thatCuyk is a skew-symmetric tensor.
7.Let z be a p-cycle on G.Show that for each closed p-form @ and
eachginG,
L*①
(We must assume that G is connected,i.e.,consists of one piece only.)

---
## Page 177

X
Applications to
Physics
10.1. Phase and State Space
Weproposetostudyaholonomicmechanical systemwithafinitenumber
of degrees of freedom,avoiding collision phenomena.In this section we
formulatethegeometryofsuchasystem.
The position space is simply an n-dimensional manifold M.
We next define the phase space attached to M.This is the space of all
covariant vectors at all points of M. To make this precise, we consider a
coordinatepatchUon Mwithlocal coordinates
q',...,”.
At a point P of U,a covariant vector is simply a one-form at P,hence is
givenbyitscomponents
Pi,...,Pn, p;real
(where the one-form itself is ≥ p;dq').
If
a'，...,”
is another local coordinate system valid atP,then the components of the
samecovariantvectorwithrespecttothe?'are
P=E
be
The totality of all such covariantvectors at all points of M constitutes the
(2n)-dimensional phase space P.To each coordinate neighborhood U on M
U× E" with local coordinates
q',...,q”,P,...,Pn.
It follows that the one-form
α=∑p;dq²
is a one-form on P, entirely independent of local coordinates. We have
da =dp;dq²
163

---
## Page 178

164
X.APPLICATIONS TOPHYSICS
s0 that the phase density (see Section 2.3)
dp....dpndq...dq"
is a 2n-form on P,never zero,defined by
±(dα)”=(nl)(dp ···dpndq²..·dq”),
and serves us as a volume element on P.
We shall derive some useful relations from the transformation of co-
ordinates
(q=’(q，..·，q”)
P=EPa
rbe
(i=1,...,n)
velid on the overlap of local coordinate neighborhoods U and O.
We set
q=(q',…"",q")and
p
and define q and p similarly.Then q=q(q) implies
rbe
dq=dqA,
=A(q).
be
Since α= dq p=da p, we have
p= Ap, that is, p= Ap,
where A=A-' is also a Jacobean matrix.From
dp=dAp+ Adpanddq=dqA
we deduce first that (dp,/dp;)=A=(dqi/ag').
To continue,we note two relations.From A= A-' we have
dA= -A-' dA A-'= -A dA A.
From dq=dqA we have 0=dq dA, which easily implies
da'k
da';
dqi
ybe
Now
dp=dAp+Adp=-AdAA p+Adp
=-AdAp+Adp.
Also
dp=d(Ap)=dAp+Adp.‘
Thus dp/aq* is the coefficient of dq* in the i-th row of -A dA p and dp/dqi
is thecoefficient of dgiin thek-th rowof dAp.Now

---
## Page 179

10.2.HAMILTONIAN SYSTEMS
165
AdA=
and
(a)-(a)
Therefore the coefficient of dq* in the i-th row of -AdAp and the coeffi-
cientof dgiinthek-throwof dAp arerespectively
=
pe
be
dq;
We conclude that dp;/dq*=--dp*/ag', so we have proved
(opi_opk
熙-=
op:g
.e_de)
Finally,the state space is the product
S=PXE1
a (2n + 1) dimensional space. We think of E1 as the time axis. Local
coordinatesforS are
q,...,q”，Pi,...,Pn，t.
10.2. Hamiltonian Systems
Wewish to consideradynamical system inHamiltonianform.Webegin
by tracing the evolution of this from Lagrange's equations of motion, which
in Euclidean coordinates reduce to Newton's law of motion.We deal only
withconservativeholonomic systems.
The treatment first of all is local. We deal with a coordinate patch in
q',."· ,q" space. For each instant of time, there is a point (position)
(a(t),·.·,"(t))
which represents the trajectory of the system. As is customary, we set
u = du/dt.The kinetic energy is a function
T(g',...,”,,..·,”)

---
## Page 180

166
X.APPLICATIONS TOPHYSICS
which is supposed to be a positive definite quadratic form in the variables q.
Thepotential energyisafunction
V =V(q²,..·,q”,t)
and the Lagrangian function,or kinetic potential,is
L=T-V.
The differential equations ofmotion are then
Te(Te/p
Forthefirsttermwehave
TTTe/p
so that the Lagrange equations are a system of n second order ordinary
equations for the unknowns q',."' , d". We now convert these to a system
of 2n first order equations in 2n unknowns.
Weintroducethegeneralizedmomentumcomponents
P1,...,Pn
by
OLoT
Pi=a=n
Because the quadraticform Tis definite,the transformation ofvariables
(q,..·,”，a,..·,”）<→(q,..·,q”,P1,..·,pn)
is a smooth one both ways.
Toreach the Hamilton form,we shall follow tradition and use a rather
confusing notation. The matter was better expressed in Section 3.5.
The function T is always considered as a function of the 2nvariables
q,...,”,,...,”.
The function V which involves the q’(and t) alone may be considered as &
function on the space of variables q',."·,Y, a',."·,",t or on the space of
variables q',...,q”,P,...,Pn,t.
We introduce theHamiltonian
H=H(q,..·,qp,·.·,P,t)=∑p²-L,
always considered asafunction on the space ofvariables
q,...,d,P,...,Pn,t.