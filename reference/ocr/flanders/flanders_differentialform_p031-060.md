<!-- OCR chunk: flanders_differentialform.pdf pages 31-60 (of 219 total) -->


---
## Page 31

2.8.PROBLEMS
17
Example 2. E3 with the ordinary metric. If f and g are functions,
=
of
of
+x
of
he
of
dyda+y
and we have
(ofgafogfg)
df^*dg=
dxdydz.
(2e)
2.8. Problems
1.Let L be an n-dimensional space.For each p-vector α≠0we let M。be
the subspace of L consisting of all vectors o satisfying α ^ o = 0. Prove
that dim(Ma)≤p.Prove also that dim(Ma)=p if and only if α=
O1 ^ ... A o, where o1, ...,o, are vectors in L.
2.(Continuation)Let α be any (n-1)-vector. Prove that α=
...n-1.
3.Let L be an n-dimensional space and α a 2-vector.Show that there
isa basis O1,.`.,o,of L such that
α=++.·+2-12
The number 2r,which depends only on α,is called the rank of the 2-vector α.
Show thatα≠0,αr+1=0.
4.(Continuation） Let o1,·"·,o, be a basis of L and let A = lajll be a
skew-symmetric matrix.Show that the rank of the matrix A coincides
with the rank of the 2-vector α=a,^j·
5.We are given alinear transformation
A: L-→L,
where dim L=n.Find the value of the determinant
[W A].
6.Let A be an m x n matrix and B an n x m matrix, where m <n.
Prove
[AB|=∑aH
where H runs over ordered sets,
H={h,h2,...,hm},
1≤h<h2<...<hm≤n,
and where
ah....ahm
bh1 ... bhm
aH
bH
Cmhm

---
## Page 32

18
II.EXTERIORALGEBRA
Note thatthe specialcase
B='A
yields a well-known formula of vector algebra,
|a×b|=|a|²1b²-(a·b)².
7.Let A be an nx n matrix and denote by cof A the matrix of cofactors
of A [so that A(cofA)=(cofA)A =|A|·I].Let bu,k be a typical element
of^"(cofA).Show that
bH,K = ±|A|P-laH',K'
where H' is the set of indices complementary to H, ditto K', K, and a',k?
is the correspondingelementof
△"-PA.
8.Express in terms of exterior algebra the formulafrom vector algebra
α×(β×y)=(α·y)β-（α·β)y.

---
## Page 33

III
The Exterior Derivative
3.1. Differential Forms
Let P be a point in E".The one-forms at P are the expressions
∑a;dx,
a;constants
These form an n-dimensional linear space L = Lp.The p-forms at P are
the elements of
^L=^"Lp,
i.e., expressions
ZaHdah .. da"e,  ay constants.
Note that we are dropping the notation“Λ” so that differentials dx’ juxta-
posed will always be multiplied by exterior multiplication.
Now let U denote an (open) domain in E".A p-form on U is obtained by
choosing at each point P of U a p-form at that point, and doing this smoothly.
Thus & p-form w has the representation
①=∑a(x,·.·,x")dx,
where the functions ag(x) are smooth functions on U, differentiable as often
as we please.
on the differential forms on U itself. Thus if w is a p-form and r is 8
q-form on U, then w ^n is a (p + q)-form on U. (Of course w ^ n = 0 if
p+q>n.）If
@=aHdx，n=∑bkdxK,
then
@n =abdx dxk
so that the coeffcients of w ∧ n are again smooth functions, being poly-
nomials in the coefficients of @ and .
For example a one-form
w = Pdx +Qdy+ Rdz
19

---
## Page 34

20
III.THE EXTERIORDERIVATIVE
may be identified with an ordinary vector feld (P,Q,R) in E3,a two-form
α=Adydz+Bdzdx+Cdxdy
may be identifed with a polar vector field in E3.
3.2. Exterior Derivatives
We denote by
FP(U)
the totality of p-forms on U.In particular F°(U) is simply the set of all
smoothfunctions onU.
We shall now set up an operation d which takes each p-form w to a
(p + 1)-form dw.In E3 it will work this way. For a O-form f,
=
af
af
dx+
dz.
dy
For the one-form w above,
(ORQ
(OPoR
dzdx+
(QQaP
dw=
dydz+
(x
dxdy
(ne_r)
whilefor thetwo-form αabove,
(0A.0B.0C
dα=
dx dy dz.
+y
Thus the operator d subsurnes the ordinary gradient,curl or rotation,and
divergence.
Itwill turn out that dis completely independent of coordinate systems.
This will be more or less clear when we axiomatize d.
We shallestablish the existence and uniqueness of an operator
d:FP(U)-→FP+1(U)
suchthat
(i)d(@+n)=dw+dn
(id(μ)=dμ+(-1)(deg）dμ
(ii)For each w, d(dw)= 0
(iv）For each function f,
Let us note the consistency of (iv) as it applies to the coordinate functions.
For examplex is a function on Uand d(x')the effect of d on this function
c is the symbol dx'. Thus from (i), d(dx') = O once we have d.

---
## Page 35

3.2.EXTERIORDERIVATIVES
21
First we prove there is only one such operation d. Suppose we are given
such a d. We first show that
d(dx..·dx)=0
by induetion on p. We have just noted this for p =1. If it is true for
p-1, then by (i),
d[x（da..·dx)]=dxh..·dx∞,
d(dax..·dx²)=d{d(xdx2..·dx)}=0
by (ii).Now if w is a p-form,
@=∑an(x)dxH,
do) = ∑ d(agda)
=∑(da)dxH
=#
OaH
dxidaH,
which shows that the recipe (i-iv) completely deterrnines do.To prove that
there exists such an operator d,we simply set
d=
aH
dxidxH
for w = ZagdxH and check that the properties are satisfied. Properties
(i) and (iv) are fairly clear; let us look at (i) and (i). Evidently if we can
Suppose
入 =adx#， μ= bdxK.
Then
d(μ)=d(abdxHdxK)
(ab)
dxdxHdxk
da
ab
dxdxdxk
dxdx)(bdxk)
+(-1)(dee)∑(adx)
db
dx'dx
= (dx) △μ + (-1)(deea)  d.

---
## Page 36

22
III.THE EXTERIORDERIVATIVE
The sign results from
dx' dx# =(- 1)(deg) dx dx².
This proves (ii).
Again, let @ = adx#.Then
ddao)=a( dx'dae)
0a
=
²a
dxide'dx
1 (a ²a)d
(_)
deidedxH
=0,
which verifies (i).
Property (i)is nothing more than the equality of mixed second partial
derivatives.It is the source of most “integrability conditions”in partial
differential equations and differential geometry.It is usually referred to as
thePoincareLemma.
3.3. Mappings
We study the following situation:U is a domain in E",Vis a domain in
E" and is a smoothmapping on U intoV.Wewrite
Φ: u-→v.
Also, we denote by x,···,x" the coordinates of E" and by y',."·,y” the
coordinatesofE".Thenwecanwrite
y'=y²(x,·.·,xm)
with coordinates y.The functions y'(x) are smooth.
As before,R denotes the reals.If g is any real-valued function on V,
g:V-→R
then we may combine this withΦ to obtain a function on U to Rwhich we
write
Φ*g =g。Φ.
Thus
Φ*:F(V)-→F°(U).
From the mapping Φ on U to V we have constructed a new (induced)
mappingΦ*on F°(V) to F°(U).

---
## Page 37

3.3.MAPPINGS
23
中
Φ*g=g。Φ
R
We are nowgoing to define a map Φ*taking p-forms onV to p-forms on U:
Φ*:FP(V)-→FP(U).
(Strictly speaking we should index Φ* and write Φ,*, p = 0, 1,···, but we
shall skip this.) We have taken care of p = O already. The crucial case is
p = l; after we do that, the algebraic considerations of Chapter II do the
rest of the work.
The basic idea is substitution of coordinate functions,replacing dy’by
Cy'
dx'
Thus if w =∑a(y)dy² is a one-form on V, we set
Φ*=∑a(y(x)
,he
dx
We now have
Φ*:F'(V)-→F'(U).
By the method of Section 2.4,we extend this mapping to the exterior products
to obtain
Φ*:FP(V)—→FP(U).
As an example,
b*(dy²dy²)=(Φ*dy²)(b*dy²)
dy 0y2
dx'dx
dx*dx
(x,x)

---
## Page 38

24
III.THEEXTERIORDERIVATIVE
We now list the basic properties of Φ*.
(i)Φ*（c+n)=Φ*①+Φ*n
(1Φ)v()=(v)Φ()
(ii）If w is a p-form on V,
d(Φ*c)=Φ*(dc)
(iv)If Φ:U—→V and y:V—→W,then
（4。Φ）*=Φ*。4*.
The first property is evident and the second follows from the final formula
of Section 2.4.
Property (ii) is essentially the chain rule for partial derivatives. First
we take a 0-form g on V.
=6p
g（y(x))oy
Φ*dg =∑
(中*g) dx =d中*g.
=>
It suffces to verify (i) for p-forms w which are monomial since each p-form
is a sum of such.Suppose then that
w= gdy”=gdn
where n = yh dyh ..· dy” is a (p - 1)-form.Then
(uΦp)v(bΦ)=(up*Φ)(bΦ）=M*Φ
(uΦ）pv(bΦ）p=(*Φ）p
and
do =dg ^ dn,
b*d=（Φ*dg)^(Φ*dn)
MΦp=(lΦ)pv(bΦ)p=
we have pushed through the next case.
We now look at the final property (iv).
For a O-form (function)h on W we have
[（(。Φ)*h](x)=h[（。Φ)（x）]=h{y[Φ（x)]}
=[y*h][Φ(x)]={Φ*[y*h]}（x)
=[(Φ*。↓*)h](x),

---
## Page 39

3.4.CHANGEOFCOORDINATES
25
hence
（xoΦ)*h=（Φ*。y*）h.
An induction similar to that above establishes the property in general.All
it means is that one can substitute directly the expressions for the coordinates
中
Φ*
U
FP(U)
F(V)
山。q
(4。Φ)*
=（Φ*。*)
W
F(W)
2* on W in terms of the coordinates x' on U, or indirectly by first going
through the coordinates y' of V; the results are the same.
Whathasreallybeenseeninthissectionisthatone can carry onfearlessly
withthemostobviouskindofcalculationswithdifferentialforms.
Examples.Consider the map Φ:t-→(x,y) on E1-→E² given by
x=t²,y=t3.Ifw =xdy,a one-form on E²,
Φ*=(t2)
Take the map : (x, y)-→t =x - y.
y*(dt) = dx-dy.
One final remark.Suppose m<n and Φ is a niap on the domainU of E"
into the domainVof E".If w is a p-form onVand p >m,then necessarily
0=m*中
3.4.Change ofCoordinates
We apply the results of the last section to the special case in which U and
V are both domains in E” and Φ is a one-to-one mapping on U onto V with
both Φ and  = Φ1 smooth.(Note the map x—→y=x² on E1 —→ E is
one-to-one and smooth. But the inverse map y -→ x = y1/3 is not smooth
no derivative at y = 0.) In each figure,1 is the identity map, 1(x)= x. It
follows that Φ* is a one-one map on F"(V) onto Fe(U) and its inverse is 4*.
If we interpret the coordinates y of V as new coordinates on U, the result
dΦ*w=Φ*dw
meansthattheexteriorderivaticeofadifferentialformisindependentof the
coordinate system in which it is computed.

---
## Page 40

26
III.THEEXTERIORDERIVATIVE
This inner consistency of the differentialform calculus is most important.
Later we shall base theglobal theory(forms onmanifolds)on this.
中
U
U
We note inpassing thatwith aproper formulation this independence of d
on the coordinate system can be obtained as a consequence of the four basic
defining properties (i-iv) of the exterior derivative in Section 3.2.
3.5.AnExamplefromMechanics
The following problem is taken from E. Goursat [15, p. 85]. We work in
& region with coordinates (x, u) = (x1,·"·,xn, u,·"·,un). We are given
afunction
Φ=Φ(x,u)
which is supposed homogeneous of degree 2 in the variable u.  (For example,
a kinetic energy form ∑a;(x)uμuj.)）Define
Pi= 0Φ/ou.
We assume that the mapping (x,u)-→(x, p) defines a regular change of
variables.Wethenwrite
Φ(x,u)=y(x,p).
The problem is to prove the relations
x-oxi'opk=
=uk·
The proof depends on two things,theEuler formula for homogeneous
functionswhichinour caseimplies
uk=2,
i.e.,
∑Pkuk= 2Φ,
and the fact that exterior relations are independent of how they are derived.

---
## Page 41

3.6.CONVERSE OF THEPOINCARELEMMA
27
We have
+xp
duk=
Zduk
x
and
2dΦ =∑pkduk +∑udpk,
hence by subtracting
Now everything follows from Φ =  and
Zax
dpk
3.6.Converseof thePoincareLemma
The Poincare Lemma,d(dw)= 0,has these interpretations in 3-space:
curl (grad f) = 0
div (curlv) = 0
according to theexamples at thebeginning of Section3.2.Invector
analysis oneproves thata curl-free vectorfield isagradientbylineintegrals
and that a divergence-free vector field is a curl, usually by a brute-force
method.We are now going to prove a general result.If w is a p-form
(p≥ 1) and dw =0, then there is a (p - I)-form α such that ∞) = dx. The
result is hard if p >1 because there are many solutions.Also the result is
valid only in domains which are not too complicated topologically.
The demonstration is based on a“cylinder construction."We begin with
a domain U in E".We denote by I=[0,1] the unit interval on the t-axis
and consider the cylinder or product space.
IXu.
This consists of all pairs (t, x) where 0 ≤t≤ 1 and x runs over points of U.
We single out the two maps which identify U with the top and bottom of
the cylinder, namely,
j: U→IXU. j(x)=(l,x)
jo: U→IX U, jo(x) = (0,x).
Thus
j;*:F(IXU)-→FP(U)(i=0,1).
For example, to form i*o where o is a form on I X U. simply replace
t by I wherever it occurs in o (and dt by O correspondingly).

---
## Page 42

28
III.THEEXTERIORDERIVATIVE
iXu
U
We now form a new operation K,
K: F+1(IXU)-→F(U);
Kis defined onmonomialsby theformulas
K(a(t, x)dx#) = 0
K(a(t,x)dtdx')：
and on general differential forms by summing the results on the monomial
parts. Here is the basic property of K:If w is any (p+ 1)-form on
IXU,then
K(d∞)+d(K∞) =j*w-jo*@.
It is enough to check this for monomials.
Case 1. @ =a(t, x)dxH.
We have Kw =0,dKw =0,
da
Kdw
da
lx= [a(1,x)-a(0,x)]dxH
But j1*@ = a(1, x) dxH, jo*@ = a(0, x) dxH, so the formula is valid.
Case 2. @ = a(t, x)dt dx'.
First j*w = jo*@ = 0. Next,

---
## Page 43

3.6.CONVERSEOF THEPOINCARELEMMA
29
Kw=d
[(falt, x)atl dax
so the formula again works.
Definition.A domain U is deformable to a point P if there is a mapping
$:-X-u
such that
Φ(l, x)=x,
Φ(0, x) = P.
The boundary conditions may be interpreted in terms of the j; as follows:
Φoj=l, Φ.jo= P.
For a (p + 1)-form w on U we have as a consequence
j1*[Φ*∞]=0，jo*[Φ*∞]=0.
Now we can state and prove the main result.
Let Ubea domain inE”which can be deformed toa point P.Letbe a
(p+1)-formonUsuch that dw=0.Then there isa p-form α onUsuch
that
W = da.
We merely substitute Φ*@ in the formula above to have
m=[)xp+[(Φ)p]y
But d(Φ*w) = Φ*(dw) = 0, hence @) = dα with α = K(Φ*@).
It is interesting to see how far the solution of the equation da = w is
determined.If β is another solution, then dβ = w = dα,d(α -β)=0.If
p≥ 1,we conclude by the main result again that α-β=d)where is a
(p -1)-form.In other words, given one solution α, the general solution is
α-dwhere is absolutely arbitrary.(When p =0,α andβare functions
and we conclude thatα-βis constant.)

---
## Page 44

30
III.THE EXTERIORDERIVATIVE
3.7. An Example
We shall illustrate this whole method in the case n =3,p = 2.Thus we
take a two-form
① = Adydz+ Bdzdx + Cdx dy
in E3 for which dw = 0, i.e.,
0A0BC
The space E?can be deformed to0 by themap
Φ(t,x,y,z)=(tx,ty,tz).
The assertion is that w = dα where
α =KΦ*(w).
First we compute Φ*@ :
Φ*=A(tx,ty,tz)d(ty)d(tz)+..
=A(tx,ty,tz)(t dy + ydt)(tdz +zdt) + ...
=A(tx,ty,tz)(yt dt dz -zt dt dy) +···+ (terms free of dt).
Now we have
, t)tat (y dx - dy)
α=K(Φ*∞)=
A(tx
B(tx,ty,tz)tdt)(zdx -xdz)
,tz)t dt)(xdy-ydx)
One verifes after some calculation that indeed da = 0.
3.8.Further Remarks
For
①=Adydz+Bdzdx+Cdxdy
theproblemoffinding
α=Pdx+Qdy+Rdz
so that
dα =(
is that of finding three unknown functions P,Q, R of the three variables
x,y. so that the system

---
## Page 45

3.9.PROBLEMS
31
OR
Q
oy
aP
OR
B
ax
Q
oP
C
0x
of three partial differential equations is satisfied, the given functions A,B,C
being subject to the necessary condition
0A.0B.C
++
=0.
It is remarkable that this system (and the more general ones covered in
Section 3.6) can be solved by an explicit formula involving quadratures.In
general, the theory of exterior differential forms exposes many types of
systems of partial diferential equations which are reducible to systems of
ordinary differential equations and often solved by quadratures.
Another point to be noted is this.If we are dealing with a(p +1)-form w)
such that dw= O and w happens to depend on several parameters smoothly,
then wecanfind anα such that da=w and αdepends on the same parameters
just as smoothly.This againfollows from the explicit formulasof Section3.6.
3.9.Problems
1.Let
@ = ±∑ ai;dx'dx, auy + ay; = 0.
Prove that
dw=∑
day
dajk
oaki
dedx'dx
2.Consider a linear transformation Φ: E”-→ E", Φ(x,··.,x")=
(y,..·,y”), where
y’=∑a’jx +b’，a',b’ constant.
What is Φ*(dxl ... dx")?
3.Consider the mapping
Φ:(x,y)—→(xy，1)
on E2 into E2. Compute Φ*(dx), Φ*(dy), and Φ*(ydx).
4.Complete the unfinished calculation of Section 3.7.

---
## Page 46

IV
Applications
4.1.Moving Frames in E3
We first point out that in dealing with vectors in Euclidean space,no
matter where we draw them for picturesque purposes, when we deal with
themanalytically,theyalways startattheorigin.
2
Weattach to each pointx of E3aright-handed orthonormal frame
e1,e2,e and suppose that the vectorfields e;are smooth fields.
What we shall do is express everything in sight in terms of the e;, apply d
to these relations to derive further ones, and continue until we obtain no
further results.
First of all, dx is a vector with one-form coefficients,for example,dx =
(dx,dy,dz)= dxi+ dyj + dzk. We express dx in terms of the frame
e1,e2,e at the point x,which we certainly may do,say,by first expanding
i,j,k in terms of the e;and then collecting terms:
dx=0e1+02e2+03e3,
32

---
## Page 47

4.1.MOVING FRAMESIN E3
33
where the o; are one-forms. We do the same with each e::
de; = @1e + Wi2e2 + w;3e3 (i = 1,2,3)
where the wt; are one-forms.
Sincee·ek=dik,we have
deek+ e;dek=0,
that is,
=∞+
In particular, W =0.
Itwill be convenienttointroduce some matrixnotation.We set
(e1
e2
=(01,2,3), Ω=ll
(e3/
and have these structure equations:
dx = oe,
de =Ωe,
Ω+'Ω=0.
the last equation,the left-hand superscript t denotes transpose of the matrix,
i.e., interchange of rows and columns, so this equation expresses the skew.
symmetry of Ω.
From d(dx)= 0 we have
doe-αde=0,
doe-oΩe=0,
(do -oΩ)e = 0.
Because the e; are linearly independent, this means
do =oΩ.
Similarly, from d(de) =0, we have
0=dΩe-Ωde=(dΩ-Ω²)e,
dQ =Q2.
In summary, then we have
Structure equations
Integrability conditions
dx =ox
(do =oΩ)
de =Ωe
(dQ=Q²)
Ω+=0

---
## Page 48

34
IV.APPLICATIONS
Further differentiation does not lead to new results. We shall see in our
studyof Riemanniangeometry thattheequation dQ-Q²=0expresses the
lackofcurvature ofEuclidean space.
A point to be noticed is that the three-form o, ^ 02^o3 is precisely the
elementofvolume inE3:
2=dxdyd2.
Weshallverifythisinthenextsection.
Itwill be observed that the calculations of this section work equally well
in E".
Z
Example. Spherical coordinates. The orthonormal unit vectors e1, e2, e3
are taken in the directions of increasing r,Φ,0,respectively.From
x = (rsin Φ cos0, rsinΦ sin0, rcos Φ)
wehave
dx =(sin Φ cos 0, sinΦ sin 0, cosΦ)dr
+ (r cos Φcos 0,rcos Φ sin 0,-rsin Φ)dΦ
+ (-rsin Φ sin0, rsin Φ cos 0, 0)d0
= (dr)e, + (rdΦ)e2 + (rsinΦ d0)e3

---
## Page 49

4.2.ORTHOGONALANDSKEW-SYMMETRICMATRICES
35
with
e = (sin Φ cos 0, sin Φ sin 0, cos Φ)
e2 = (cos Φ cos 0, cos Φ sin0,-sin Φ)
(e3 =(-sin0,cos 0,0)
and so
01=dr， o2 =rdΦ,  3=rsinΦd0.
Differentiating,
de, = (dΦ)e2 + (sinΦd0)e3
de2 =(-dΦ)e + (cosΦd0)e3
hence since Q is skew-symmetric,
0
dΦ
sinΦd0
=
-dp
0
cosΦdθ
-sinΦd0
-cos Φdθ
0
The volume element is
02^03=r²sinΦdrdΦd0.
4.2.RelationbetweenOrthogonal andSkew-symmetricMatrices
It is no accident that Q turns out to be skew-symmetric.This is a con-
sequence ofthe principle that the first-order approximationto an orthogonal
transformation is a skew-symmetric one.We shalllookatthisfrom several
viewpoints.
A matrix B is orthogonal if its transpose equals its inverse,'B=B-1,or
B'B='BB=I. Suppose A is skew-symmetric, A +'A =0. Then for
small ε we set B = I + &A and have
B ‘B = (I +εA)(I  εA)= I + O(e²)
so thatBis orthogonal uptofirst-order terms.
Here is another approach. Let A be skew-symmetric. Since the
characteristic roots of A are pure imaginary, I+ A and I - A are non-
singular.Set
I+A
Then
BB=(告A)(A)=1
so that B is orthogonal.

---
## Page 50

36
IV.APPLICATIONS
Next we re-examine the calculations of the last section.Let
/i)
\i3/
where the i, are the fixed unit vectors in the 2, y, z directions, respectively
(i, j, k in usual vector notation). Then
e;= ∑byi,  e= Bi
leading to a matrix B =Ibt;ll which is clearly orthogonal:
I=e'e=Bii'B=BI'B=B'B.
(Now we can prove the fact dxdydz=01^02^03 mentioned at the
end of the last section. We have
dx=(dx,dy,dz)i = oe = oBi,
(dx, dy, dz) = αB,
hence
dxdydz=|B23
But from 'B B = I we have |B|² = 1,|B} = ±1. Since we are supposing e
isaright-handed system,|B|=+1,
dxdydz=00203.)
Then we have
de =dBi=(dB)B-1e
so that
Ω = (dB)B-1.
We note this general result: If A is an orthogonal matrix whose elements are
functionsofanynumberofvariables,then
(dA)A-1
isa skew-symmetricmatrix of one-forms.
For we have
'AA=I,
dAA+'AdA = 0,
'0=-P+P-V;
“(dA A-')+ dAA-1 = 0.
There is also & converse which is important.Suppose A is a matrix of
functions defined on a domain U.Suppose A is orthogonal at a single point
of U and that
dA = ΛA

---
## Page 51

4.3.THE 6-DIMENSIONAL FRAME SPACE
37
where A is a skew-symmetric matrix of one-forms. Then A is orthogonal on
all of U.
We set C = 'A A and have
0=（v),+(V,-)=（p）,+(p)=Op
hence C is a constant matrix on U.But we are assuming C = I at one point
of U, hence C = I on U, *A A = I on U, A is orthogonal.
Another point is this.If A is a variable orthogonal matrix (transforma-
tion),each point v。 of space is sent by the general A to
V=Avo.
We then have
dv=dAv。=(dA)A-v
action of thegeneral Aofourfamilybymeans of
v-→v+dv=[I+(dA)A-]v
with the skew-symmetric (dA)A-′ representing this“infnitesimal trans-
formation."
All of these considerations work equally well in E".
4.3.The 6-dimensionalFrameSpace
We consider the space of allright-handed orthonormalframes E,,E2,E3
at all points x of E3.This space is 6-dimensional because we have three
degrees of freedom in choosing x,two degrees of freedom in choosing the
unit vector E,，one degree of freedom in choosing the unit vector E2per-
pendicular to E,and then E,is determined.
Wewrite
/E
E2
E3/
and have
E =Ae
where A is a variable (three parameter) orthogonal matrix and e = e(x) is &
definite moving frame.
Then
dx=e=oA-'E,
dE=(dA)e+Ade=[dA+AQΩ]e
= [dA + AQ]A-E.
We set
U+-(P)=‘=

---
## Page 52

38
IV.APPLICATIONS
These are matrices of one-forms on the 6-dimensional frame space and we
have
Structureequations
Integrability conditions
dx=E
[d =
dE=E
[d=².)
+=0
Tocheck theintegrability conditionswe note
0 = d(dx) = dE -dE = (d -)E, d = , etc.
In making a penetrating study of the differential geometry of E3 one is
necessarily led to this 6-dimensional frame space and its differential forms
',@y which, it will be noted, are entirely independent of the choice of the
moving frame e on E3.
4.4.The Laplacian,Orthogonal Coordinates
We continue the considerations of Sections 4.1 and 4.2.The forms
dx,dy,dz make up an orthonormalbasis for the Euclidean geometry of the
space of one-forms at each point; these are related to the fixed (absolute)
frame i.From
e=Bi，dx=oe=(dx,dy,dz)i
wehave
oB=(dx,dy,dz)
as already noted. As Bis orthogonal, we see that o1, 2, 03 is an orthonormal
basis for one-forms at eachpoint.
Let fbea function on E3.Then we have
=P
fdm+fd
dz,
f=
af
(²f²f²f）
d*df=
dxdy dz = (△f)dx dy dz.
(x+y+）
TheLaplacian△f of fis known as soon as the three-form d *df is known,for
this has turned out tobe the Laplacian multiplied by the volume element
dxdydz.

---
## Page 53

4.4.THE LAPLACIAN,ORTHOGONAL COORDINATES
68
Now we know that the * operator can be computed equally well in any
orthonormal coordinate system. Also  A 02 ^ 03 = dxdy dz, so our
df=ao+a202+a03.
Then
*df=a3+a030+a02
d*df=(△f)023.
A coordinate system u,v,w in a domain in E3 is called an orthogonal
coordinate system if thevectors
xx
are mutually perpendicular. This means that for suitable functions ∧, μ, v,
thevectors
10x
10x
m=Ea
10x
form an orthonormal, or moving frame. We shall presuppose that this is a
right-handed one.(Otherwise we merely permute w and v.)We have
0x.
0x.
0x
w
=(du)e +(μdv)e2+(vdw)e3
80that
0=Adu，o2=μdw，03=vdw
build an orthonormal frame for one-forms. Now we compute the Laplacian:
df=fdu+fdu+fdw
=(f/2)o+(f/μ)o2+(f∞/v)o.
*df=(f/2)o23+（f/μ)3+（f/v)o2
= (μv f/A)dvdw +(v fo/μ) dw du +(2μ f/v)dudv.
We compare this to
d*df =(△f)o02=μv(△f)dududw:
A品+(+)

---
## Page 54

40
IV.APPLICATIONS
Let us apply this to spherical coordinates r, Φ, 0:
x=rsincosθ
y=rsinΦ sinθ
(z =rcosΦ.
r sinΦd0
dΦ
The orthogonality is easily checked (it is obvious geometrically) and we have.
0= dr， 02=rdΦ， 03=rsinΦd0,
4.5.Surfaces
We study a smooth surface Ein E3.We choose a moving frame e at each
point x of Z in such a way that e, is the normal to the surface, Then e1
and e, span the tangent plane at each point.We shall see how the equations
ofSection4.1specialize.

---
## Page 55

4.5.SURFACES
41
Since x is constrained to move in the surface, dx must lie in the tangent
plane, 0 = 0:
dx=0e+2e2.
It is clear that the two-form oo2 represents the element of area of E.
2
unit normal
tangent plane
We exploit the skew-symmetry of Q by writing
0
0
①2
0
The structure and integrability conditions now reduce to
Structureequations
Integrability conditions
dx=oe1+02e2
do=w2
de =we2-we3
do2=-∞
de=-we-w2e3
@1+ 02@2=0
de=we+w2e2
dw+0@2=0
dw=w02
dw2=-w@1

---
## Page 56

42
IV.APPLICATIONS
In a certain sense,all of local surface theory is contained in these equations.
It remains to interpret them in terms of curvatures, curves on the surface,
etc.We illustrate a little of this.
As already remarked,o2 is the element of area on E.As xmoves over
E,e, moves over a region on the unit sphere S², called the normal, or
spherical,image of E.Since e and eare orthogonal to e,they lie in the
tangent plane to the spherical image and form a frame there.We see that
the equation de3 = @e, + @2e2 plays the same r6le for the spherical image
as dx = 01e1 + 02e2 does for Z, hence @@2 represents the element of area
of the spherical image.
Since there is only one linearly independent 2-form on the 2-dimensional
space E,wehave
W1W2= K0102
whereKisascalar called the Gaussian curvature.We shall see shortlythat
it is entirely independent of the choice of e, and e2.
Similarly o@2 - 02@ is a 2-form on ∑, and so
01@2- 02W1 =2H02
defines a scalarHcalled themean curvatureofE.
The one-forms W1, @2 are linear combinations of o, and 02. Because of
therelation
01@1+ 02W2=0
wehavea symmetryin the coefficients:
w=po+q2
W2 = q01 + ro2.
Weeasilyhavefrom this
2H=p+r，K=pr-q².
The characteristic roots of the symmetric matrix
1q
are called the principal curvatures K1,K2 of E.We consequently have
2H = K1 + K2,K =K1K2.
From the relation dw + ww2 = 0 we have
dw + Ko102 = 0.
This relation gives us K once we know o1, 02 and w.But the relations
do=w02， do2=-0

---
## Page 57

4.5.SURFACES
43
then, K is completely determined analytically from o, and o. This contains
the theorem of Gauss that the curvature K is an intrinsic invariant of ,
independent of how  is imbedded in E3, so long as the distance between
points of Z measured along  (on geodesics, or shortest paths) is preserved
locally.
When we apply vector operations to vectors with differential form
coefcients, we must always combine the coefficients according to the rules
of exterior algebra and pay strict attention to the ordering of the factors.
With this we form vector (cross) products:
dxxdx=(e+02e2）×(e+02e2)
=o²（exe)+2²(e2xe2)+2(exe2)+2（e2xe).
Now o1² = 0 (and e × e = 0), etc. Also
2（e2xe）=（-2)（-exe2)
=(0)e3,
so finally
dx×dx=2(2)e3
andwehaveobtainedthevectorialareaelement.
Precisely,thevectorialareaelementis
()e3;
a vector directed along the normal with magnitude oo2，the element of
area ofE.Since
dxx dx=(dx,dy,dz)x(dx,dy,d2)
= 2(dy dz, dz dx, da dy)
wehave
(dydz,ddx,dxdy)=(o02)e3.
If v = (P,Q, R) is a vector field, then
(Pdydz + Qdzdx + Rdx dy) =
v·(00e3)
1_(v-e3)(0102)
is the flux of v through ∑.
Similarly we have
dx×dx=2(02)e3
dx×de3=2H(a02)e3
de3 x de3 = 2K(a,02)e3

---
## Page 58

44
IV.APPLICATIONS
which shows the independence of H and K on the tangent vectors e1 e2.
If fisafunctiononEwith
df=a0+a2,
then onE,
*df=-a20+a2,
ddf=d(-a2+a2)=(△f）a2
defines the Laplacian of f on the surface or the second Beltrami operator .
The sameworksforvectorsandwehave
dx=e+0e2,
*dx=02e-0e2.
We notice that
dxxe3=（qe+2e2)×e3
=oe-oe2
hence
*dx=dx×e3,
d*dx=-dxxde3=-2H(o02)e3
and so
x=(△x,△y,△z)=-2He3.
A minimal surface (surface of stationary area) is one for which the mean
curvature vanishes,H =O.We have proved:The coordinate function8
x,y,z are harmonic on each minimal surface. (That is,they satisfy △x =
△y = z = 0.)
Inthis sectionwehavegiven a sampleofhow theexterior calculusfits
intothe classicaldifferentialgeometryofsurfaces.Furthermaterialwill be
foundinSections8.1and8.2,butthereis much ofthesubjectthatwe cannot
cover in this text.A treatment from this point of view of exterior calculus
bellished with historical comments ofteninbad taste isfound inBlaschke[3].
4.6.Maxwell'sFieldEquations
In classical electromagnetic field theory one deals with the following
quantities:
E = electric field
H = magnetic field
B =magnetic induction
J=electric current density
D=dielectric displacement
p = charge density.

---
## Page 59

4.6.MAXWELL'SFIELDEQUATIONS
45
These are allfunctions of the space variables x', x, x? and the timet. The
basic Maxwell equations in ordinary vector language are
10B
(i)
(Faraday's law of induction)
4π
10D
(i)
(Ampere'slaw)
(ii)
div D=4πp
(continuity)
(iv)
divB=0
(nonexistence of true magnetism)
Here c is the speed of light. We shall put these equations into the language
of exterior forms. To this end, we set
α=(Edx+Edx²+Edx²)(cdt)
+(Bdx²dx²+Bdx²dx+Bdxdx²),
β=-(Hdx²+Hdx²+Hdx²)(cdt)
+(Ddx²dx3+ Ddx²dx+Ddx²dx²),
y = (J, dx² dx3 + J2 dx3 dx1 + J3 dx dx2)dt - pdx dx² dx3.
Equations (i) and (iv) become
dα = 0.
Equations (ii) and (ii) become
dβ + 4πy = 0.
Applying d to this last equation yields
dy = 0,
in vector notation
%+AIP
op
From the equation da = 0 one concludes,at least in any region of space-time
which can be shrunken to a point, that there is a one-form A such that
d =α.
We introduce the vector potential A and a scalar A。 by writing
=Adx+Adx²+Adx²+Aocdt.
The equation d) = α in vector form is
{curlA = B
grad Ao -=ot
10A
=E.

---
## Page 60

46
IV.APPLICATIONS
In free space, everything simplifes according to
E =D,
H =B,
J=0,
p=0
so that the Maxwellequations become
10H
curl E =
div E = 0
1 0E
div H = 0.
Weintroduce theLorentzmetricinto4-spacewhereby
dx,dx²,dx²,cdt
is an orthonormal basis:
(dx²,dx)=8，
(dx',cdt) = 0,
(cdt,cdt) = -1.
The signature is 3 -- 1 = 2.
According to the formulas of Section 2.7,
*（dxdx²)=-dx²(cdt),
etc.,
*(dxcdt) =dx²dx3,
etc.
We see that
α=(Edx+···)(cdt)+(Hdx²dx²+···),
β=-(Hdx+..·)(cdt)+(Edx²dx²+·..)
二*α.
ConsequentlyMaxwell's equations in free space are simply
(dα=0
Id *α = 0.
We return to the general situation and refine our analysis by introducing
one-forms:
@=Edx+Edx²+Edx3
@2 = B dx² dx² + Bdx² dx + Bsdx²dx2
W=Hdx+Hdx²+Hdx3
@4= Ddx²dx²+ Ddx²dx+ Ddx²dx²
@5 =J dx²dx3+ J2dx²dx+ J3dx dx².