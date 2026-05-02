<!-- OCR chunk: flanders_differentialform.pdf pages 1-30 (of 219 total) -->


---
## Page 1

Differential
Forms
with Applications to
the Physical Sciences
Harley Flanders
Universityof Michigan,AnnArbon
DOVERPUBLICATIONS,INC.
New York

---
## Page 2

Copyright1963,1989byHarleyFlanders.
All rightsreservedunderPanAmerican andInternational
Copyright Conventions.
Published in Canada by General Publishing Company, Ltd.,
30 Lesmill Road,Don Mills, Toronto, Ontario.
Published in theUnitedKingdom by Constable and Com-
pany,Ltd.
This Dover edition,first published in 1989,isan unabridged,
corrected republication of the work originally published in
1963 byAeademic Press,Inc.,NewYork.Please see thePreface
to the Dover Edition on page ix for an explanation of revisions
made in this text.
Manufactured in the United States ofAmerica
Dover Publications, Inc., 31 East 2nd Street, Mineola, N.Y.
11501
Library of Congress Cataloging-in-Publication Data
Flanders,Harley.
Differentiai forms with applications to the physical sci-
ences/HarleyFlanders.
p.
cm.
Unabridged,corrected republication of the work origi-
nally published in 1963 by AeademicPress, Ine.,New York"
T.p.verso.
Includes bibliographical references.
ISBN0-486-66169-5
1. Differential forms.2.Mathematical physics.
I. Title.
QA381.F56 1989
89-36936
515'.37—de20
CIP

---
## Page 3

To June

---
## Page 4

_(OCR produced no text; page 4)_

---
## Page 5

Foreword
After several friendly discussions of the pros and cons of tensors versus
differential forms in the solution of engineering problems, I persuaded my
colleague Dr. Flanders to prepare a number of lectures on differential forms.
The result was an. outstanding series of lectures which was presented to a
group of interested faculty members within the several schools of Engineering
at Purdue University.
Itbecameobvioustothoseattendingthattheuseofdifferentialforms
would give them another tool for the analysis and synthesis of engineering
systems.There are certain problems, normally very difficult to solve by
using tensors only,for which results are more quickly and directly obtained
with differentialforms.
The author was encouraged to formalize his notes to the extent necessary
for publication,to enable others to study this important subject.The text
is recommended highlybecause differentialforms and related conceptswhich
have evolved from modern mathematics are new and powerful analytical
toolsforusebytheengineerandscientist.
GEORGE A.HAWKINS, Dean
SchoolsofEngineeringandMathematicalSciences
PurdueUniversity
November20,1962

---
## Page 6

_(OCR produced no text; page 6)_

---
## Page 7

Preface totheDoverEdition
I have made the following changes to the 1963 edition. First, I have
rewritten the proof of the Third Lie Theorem,starting onpage109,to better
systematize the computations. Second, I have rewritten the derivation of
some basic relations in phase space,pp.164165,tobeless computational and
moreinthe spirit ofthebook.Finally,thereis an addendum tothebibliogra-
phy on page 199 which should be useful. In particular, it mentions the
forthcoming MAA Studies volume in which I give Kannai's differential
formproofoftheBrouwerfixedpointtheorem.
HARLEYFLANDERS
June1989

---
## Page 8

_(OCR produced no text; page 8)_

---
## Page 9

PrefacetotheFirstEdition
Last spring theauthorgaveaseriesoflecturesonexteriordifferential
forms toagroupof facultymembers andgraduate studentsfrom thePurdue
Engineering Schools.The material that was covered in these lectures is
presented here in an expanded version. The book is aimed primarily at
engineers and physical scientists in thehope of making available to them new
tools of very great power in modern mathematics. Although none of our
is covered in each case to indicate the usefulness of this machinery.
A word about the organization of the book is in order.The first chapter is
introductory and sketches where we are going and why. Chapters II, III,
andVinclude all of thetheoretical material;aknowledge of this opens the
door to the applications.Probably on first reading,one should aim more at
developing some intuition for the subject and getting a firm idea of what the
various different things which are defined look like,rather than at working
out proofs in detail.Applications to questions in differential geometry (in-
Chapters IV, VI, VIII, and IX. Applications to various topics in ordinary
and partial differential equations will be found in Chapter VII.Finally,
applications to several topics in physics are in Sections 3.5, 4.6, 6.4, and
ChapterX.
What is presupposed of the reader is first of all a certain amount of scien-
tific maturity,the precise direction not being too important.While the book
is not really advanced mathematics,it is not exactly ground foor mathe-
maticseither,and areasonableknowledge of the calculusof functions of
severalrealvariablesisnecessary,asisaworkingknowledgeoflinearalgebra
through theideas of linear combination,basis,dimension,linear transforma
tion.Some exposure to a minimum amount of the ground rules of modern
mathematics,sets,cartesian products,functions on sets,is helpful but not
essential. This material is usually picked up by osmosis anyway,and the
Glossary of Notation at the end of the book should be helpful.The reader
shouldalsoknowabouttheexistenceofsolutionsofordinarydifferential
equations.A passing familiarity with tensor methods is useful,but not
essential.
Ifour audience consistedofmathematiciansalone,itwouldbein order to
use somewhat more carein our formulations of definitions and proofs of
theorems and to discuss in considerably more depth numerous technical
pointsweherepass overlightly.Ourgoal,however,istodevelopanintuition
Xi

---
## Page 10

xiiPREFACE TO THE FIRST EDITION
and a working knowledge of the subject with as much dispatch as is possible.
This perhaps could be done in less space except for our insistence ona degree
of rigor matching that found in thebetter treatises on theoretical physics.
This falls short of the extremely great precision which is customary in modern
abstract mathematics and pretty muchinherent inits nature.One who quite
rightly is searching recent developments inmathematics for applicable
material must find this precision a considerable barricade, overpedantic if not
downright tedious—avery realfactorin the great separationbetween modern
mathematics andmodern science.Makinghis craft available to science is not
alight taskfor the mathematicianandthe extent towhich thisbookmakes a
contribution therein must necessarily be its primary measure of success.
In spite of all this,we do not hesitate torecommend this material to
graduate students in mathematics as an introduction to modern differential
geometry;indeed,a well-trained advanced undergraduate should find the
bookquiteaccessible.Consideringthedegree towhichpresentdaymathe-
maticaltraining consists ofone abstraction after another,some of the things
in thisbook could beabit ofan eye-opener,even toamathematics student
whois wellalong.For example,one could envisage such a student meeting
formationfortheveryfirsttime.
It ismy pleasant duty to acknowledge the substantialhelp and encourage-
mentIhave always had from my teachers,colleagues,and students.In this
respect a special vote of thanks is due George A.Hawkins,Dean of the
Schools of Engineering and Mathematical Sciences of Purdue University.
Finally, I wish to express my gratitude to Elizabeth Young, whose beautiful
typing of the manuscriptwasa substantial contribution.
July1963
HARLEYFLANDERS

---
## Page 11

Contents
FOREWORD
vii
PREFACE TOTHEDOVEREDITION
ix
PREFACETOTHEFIRSTEDITION
xi
1.Introduction
Page
1.1.
ExteriorDifferentialForms
1
1.2.
Comparison with Tensors
2
ll. Exterior algebra
2.1.
The Space of p-vectors
5
Determinants
·
2.2.
·
·
7
2.3.
Exterior Products
8
Linear Transformations
·
·
2.4.
·
10
Inner Product Spaces
2.5.
12
2.6.
Inner Products of p-vectors
+
·
··
14
The Star Operator
2.7.
15
2.8.
Problems
17
Ill.The Exterior Derivative
3.1.
Differential Forms
19
3.2.
Exterior Derivative
20
Mappings
3.3.
22
3.4.
Change of Coordinates
·
·
·
25
3.5.
·
·
An Example from Mechanics
·
·
·
26
3.6.
Converse of thePoincare Lemma
27
AnExample
·
·
·
·
3.7.
30
3.8.
Further Remarks
·
30
3.9.
Problems
·
31
*
IV.Applications
4.1.
Moving Frames in E3
32
4.2.
Relation between Orthogonal and Skew-symmetric Matrices
35
4.3.
The 6.dimensional Frame Space
37
4.4.
The Laplacian,Orthogonal Coordinates
·
38
4.5.
Surfaces
40
4.6.
Maxwell's Field Equations
44
4.7.
Problems
48
!!IX

---
## Page 12

xiv
CONTENTS
V.Manifolds and Integration
Page
5.1.
Introduction
49
5.2.
Manifolds.
49
5.3.
Tangent Vectors
·
53
5.4.
Differential Forms
·
55
5.5.
Euclidean Simplices
57
5.6.
Chains and Boundaries
·
61
5.7.
Integration of Forms
89
5.8.
Stokes'Theorem
·
64
Periods and De Rham's Theorems
5.9.
66
5.10.
Surfaces; Some Examples
69
5.11. Mappings of Chains
71
5.12.Problems
73
Vl.Applications in Euclidean space
6.1.
Volumes in En
74
6.2.
Winding Numbers, Degree of a Mapping
·
77
6.3.
The HopfInvariant
79
Linking Numbers,the Gauss Integral,
Ampere'sLaw
6.4.
79
VI1.Applications to Differential Equations
7.1.
Potential Theory
82
7.2.
The Heat Equation
·
·
·
90
7.3.
The FrobeniusIntegration Theorem
92
Applications of the Frobenius Theorem
·
7.4.
··
102
7.5.
Systems of Ordinary Equations
106
7.6.
108
Vlll.Applications to Differential Geometry
8.1.
Surfaces (Continued)
112
Hypersurfaces
··
8.2.
116
Riemannian Geometry,Local Theory
8.3.
127
8.4.
Riemannian Geometry,Harmonic Integrals
136
8.5.
Affine Connection
143
8.6.
Problems
148
IX.Applications to Group Theory
9.1.
Lie Groups
150
9.2.
Examples of Lie Groups
·
151
9.3.
Matrix Groups
153
Examples ofMatrix Groups
9.4.
154
9.5.
Bi-invariant Forms
158
9.6.
Problems
161

---
## Page 13

CONTENTS
xV
X. Applications to Physics
Page
10.1.Phase and State Space
163
10.2.Hamiltonian Systems
165
10.3.Integral-invariants
171
10.4.Brackets
179
10.5.Contact Transformationg
183
10.6.Fluid Mechanics
188
10.7.Problems
193
BIBLIOGRAPHY
197
GLOSSARY OF NOTATION
201
INDEX
203

---
## Page 14

_(OCR produced no text; page 14)_

---
## Page 15

TII
Introduction
1.1. Exterior Differential Forms
The objects which we shall study are called exterior differential forms.
These are the things which occur under integral signs.For example,a line
integral
Adx+Bdy+Cdz
leadsustothe one-form
①=Adx+Bdy+Cdz;
a surface integral
leadsustothetwo-form
α=Pdydz+Qdzdx+Rdxdy;
and a volume integral
[f H aradyda 
leads ustothethree-form
入=Hdxdydz.
These are allexamples of differential forms which live in the space E3 of three
variables.If we work in an n-dimensional space, the quantity under the
integral signinanr-fold integral(integral over anr-dimensionalvariety)is an
r-form inn variables.
In the expression α above,we notice the absence of terms in dzdy,dxdz,
dydx,which suggests symmetry or skew-symmetry.The further absence
of terms dxdz, ·.· strongly suggests the latter.
We shall set up a calculus of differential forms whichwillhave certain
inner consistency properties, one of which is the rule for changing variables
in a multiple integral. Our integrals are always oriented integrals, hence
wenevertakeabsolutevaluesofJacobians.
Consider

---
## Page 16

2
I.INTRODUCTION
withthechangeofvariable
(x=x(u,v)
(y = y(u, v).
Wehave
A(x,g)ddy=A[r(u,0),(u,0)
(2, y)
dudy,
d(u,v)
whichleadsustowrite
0x0x|
0(x, y)
ane
dxdy=
dud=
dudv.
（u,v)
dyy
ane
If we set y= x, the determinant has equal rows, hence vanishes.Also if
we interchange  andy,thedeterminantchanges sign.This motivates the
rules
(dxdx=0
Idydx=-dxdy
formultiplication ofdifferentialsin our calculus.
In general, an (exterior)r-form in n variables x,.·· , x” will be anexpression
@=A...., da...da,
1
where the coeffcients A are smooth functions of the variables and skew.
symmetric in the indices.
We shall associate with each r-form w an (r + 1)-form dw called the exterior
derivative of @.Its definition will be given in such away that validates the
generalStokes'formula
do
Here E is an (r + 1 )-dimensional oriented variety and E is its boundary.
A basicrelation isthePoincareLemma:
d(d∞) = 0.
1.2.Comparison with Tensors
At the outset we can assure our readers that we shall not do away with
tensors by introducing differential forms. Tensors are here to stay;in a
greatmany situations,particularly those dealing with symmetries,tensor

---
## Page 17

1.2.COMPARISONWITHTENSORS
3
methods are very natural and effective.However, in many other situations
the use of the exterior calculus,often combined with the method of moving
frames of E.Cartan,leads to decisive results in a way which is very difficult
with tensors alone. Sometimes a combination of techniques is in order. We
listseveralpoints of contrast.
(a)Tensor analysis per se seems to consist only of techniques for cal.
culations with indexed quantities.It lacks a body of substantial or deep
results established once andfor all within the subject and then available for
application. The exterior calculus does have such a body of results.
If one takesaclose look atRiemannian geometry as it is customarily
developedbytensor methods one must seriously askwhether thegeometric
results cannot be obtained more cheaply by other machinery.
(b)In classical tensor analysis, one never knows what is the range of
applicability simply because one is never told what the space is.Everything
seems to work in a coordinate patch,but we know this isinadequate for most
applications. For example,if a particle is constrained to move on the
sphere S2,a single coordinate system cannot describe its position space,let
aloneitsphase orstate spaces.
This diffculty has been overcome in modern times by the theory of
differentiablemanifolds(varieties)which wediscuss in Chapter V.
(c)Tensor fields do not behave themselves under mappings. For
example,given a contravariant vector field a² on x-space and a mapping Φ
on x-space to y-space, there is no naturally induced field on the y-space.
[Try the map t—→(t²,t²) on Einto E².]
With exterior forms we have a really attractive situation in this regard.If
Φ：M-N
and if w is a p-form on N, there is naturally induced a p-form Φ*w on M.
Let us illustrate this for the simplest case in which w is a O-form,or scalar,
i.e.,areal-valued function on N.Here Φ*w=@。Φ,the composition of the
mappingΦfollowedby w.
M
中
m
*=
Reals
(d)In tensor calculations themaze of indices often makes one lose sight
of the very great differences between yarious types of quantities which can

---
## Page 18

4
I.INTRODUCTION
be represented by tensors, for example, vectors tangent to a space,
mappings between such vectors,geometric structures on the tangent spaces.
(e）It is often quite dificult using tensor methods to discover the deeper
invariants in geometric and physical situations, even the local ones.Using
exterior forms, they seem to come naturally according to these principles:
(i）All localgeometric relations arise one way or another from the
equality of mixed partials, i.e., Poincare's Lemma.
(ii)Local invariants themselves usuallyappearas the resultof applying
exteriordifferentiation to everythingin sight.
(ii) Global relations arise from integration by parts, i.e., Stokes'
theorem.
(iv）Existence problems which are not genuine partial differential
equations (boundary value or Cauchy problems) generally are of the type of
Frobenius-Cartan-Kahlersystemofexteriordifferentialformsandcanbe
reducedtherebytosystemsofordinaryequations.
(f）In studying geometry by tensor methods,one is invariably restricted
to the naturalframes associated with a local coordinate system.Let us
consider a Riemannian geometry as a case in point.This consists of a
manifold in which a Euclidean geometry has been imposed in each of the
tangent spaces.A naturalframe leadstoan oblique coordinate system in
each tangent space.Now who in hisright mind would study Euclidean
geometry with oblique coordinates?Of course the orthonormal coordinate
systems are the natural ones for Euclidean geometry, so they must be the
correctonesforthemuchharderRiemanniangeometry.Weareledto
introduce moving frames, a method which goes hand-in-glove with exterior
forms.
We conclude the case by stating our opinion,that exterior calculus is here
whereitisthemorenaturaltool,thatitwillfindmoreandmoreapplications
because ofitsinner simplicity,bodyof substantialresultsbeggingforfurther
use, and because it simply is there wherever integrals occur. There is
generally a time lag of some fiftyyears between mathematical theories and
their applications.The mathematicians H.Poincare,E. Goursat, and E.
Cartandevelopedtheexteriorcalculusintheearlypartofthis century;in
thelasttwentyyears it hasgreatlycontributedto therebirthof differential
ning to realize its usefulness; perhaps it will soon make its way into
engineering.

---
## Page 19

II
Exterior Algebra
2.1.TheSpace ofp-Vectors
Notation:
R =field of real numbers a,b,c,·...
L = an n-dimensional vector space over R with elements α,β,·...
For each p = 0,1,2,···,n we shall construct a new vector space
1。V
over R,called the space of p-vectors on L.We begin with
^ol=r,  A'l= L.
Next we shall work out ² L in some detail. This space consists of allsums
∑a;(α;^βi)
subject only to these constraints,or reduction rules,and no others:
(aα+aα2)β-α（αβ)-a2(α2β)=0,
α(bβ+b2β2)-b(αβ)-b2(αβ2)=0,
‘0=∞
α^β+βα=0.
Here α,β,etc., are vectors in L and a, b, etc.,are real numbers; α ^βis called
the exterior product of the vectors α and β.If α and β are dependent, say
β=ca,then
αβ=α(cα)=c(αα)=c·0=0
according to our reductions.Otherwise α^β≠0.
Suppose o',.". , o" is a basis of L. Then
α=∑ao，β=∑b,
αβ=(a)(∑b)=∑ab(o²o).
We rearrange this as follows. Each term o' ^ o = O and each o' ^ o² =
-o²ofori<j.Hence
αAβ = E(ab;-abi)o^ oi.
5

---
## Page 20

6
II.EXTERIOR ALGEBRA
The typical element of ^2 L is a linear combination of such exterior pro.
ducts,hence the 2-vectors
',l≤i<j≤n,
form a basis of ² L.We conclude
dim ^² L = n(n - 1) =
2
In general, we form ^"L (2 ≤p ≤n) by the same idea.It consists of
all formal sums (p-vectors, or vectors of degree p)
(v... vI)
subject only to these constraints:
(i）(aα+bβ)α2··αp
=a(αα2.α)+b(βα··α）
and the same if anyα; is replaced by alinear combination.
sgod s o..(（)
(ii)α ^·.·A α, changes sign if any two α; are interchanged.
It follows easily from (i) that α ^ ··· ^ α, is linear in each variable; we may
ofothervectorsand compute thevalueby distributing,for example
α(b+b2+b3)y
=b(αβ)+b(αβ)+b（α）.
It follows from (ii) that if π is any permutation of the {1, 2,···,p}, then
αx(1) ^·.·απ(p) =(sgnπ)α .·αp·
Exactly as in the case p = 2, we can show that if
o',...,o"
is a basis of L, then a basis of "L is made up as follows: for each set of
indices
H={h1,h2,...,hp},1≤h<h2<...<hp≤n,
weset
=oh....
Then the totality of o is a basis of ^"L. We conclude that
dim ∧"L =(")
the number of combinations of n things taken p at a time. In particular
dim ^"L = 1.

---
## Page 21

2.2. DETERMINANTS
If 入 is in ^ L, then
A=∑aHo,
summed over all of these ordered sets H. One can also sum over all p-tuples
of indices by introducing skew-symmetric coefficients:
1
=一
p!h.,...,hp
where the bh...·h, is a skew-symmetric tensor and
bh...h, =aHforH={h,...,hb}，h<h2<...<hp.
This skew-symmetric representation is often quite useful.
Let us note why we do not define ^"L for p>n.(Sometimes it is
convenient to simply set ^"L =0 for p > n.) We express each α in a
product α ^·". ^ α, as a linear combination of the basis vectors o, ... , o"
and completely distribute according to Rule (i).This leads to
α  ...α=an..., oh  ...oh.
Each term oh1 ^ ·"· ^ o is a product of p > n vectors taken from the set
o,."·,o" so there must be a repetition; by Rule (i) it vanishes. We are
left with α ^ ·· ^ α, = O as the only possibility.
We close with a very important property of the spaces " L.
In order to define a linear mapping f on ^"L it sufices to present a
function g of p variables on L such that (i) g is linear in each variable
separately,(i) g is alternating in the sense that g vanishes when two of its
variables.are equal and g changes sign when two of its variables are inter-
changed. Then
f(α...△αp)=g(α,·..，α)
defines f on the generators of ^" L.
It can be shown that this property provides an axiomatic characterization
of "L. In the next section we apply this property to define the deter-
minant ofialinear transformation.
2.2. Determinants
As above L is a fixed linear space of dimension n. Let A be a linear
transformation onL into itself.We define a function g = gA of nvariables
on L as follows:
gA（α,·.·,αn)=Aα·..A Aαn
9: X"L→^"L

---
## Page 22

8
1I.EXTERIORALGEBRA
where X"L denotes the cartesian product. Since g is multilinear and
alternating,there is a linear functional f =fA;
1V←-1V:f
satisfying
fA(α ·..αn) =gA(α1,·.·,αn)=Aα ·..A Aαn
But ^"L is one-dimensional so the only linear transformation on this space
is multiplication by a scalar.We denote the particular one here by |A|
and have
Aα···AAα=｜Al（α·.·Aα).
This serves to define the determinant|A|of A.We must not fail to note
that this definition is completely independent of a matrix representation
of A.
We observe next
[ABl(α·.·^α)=(ABα)^···(ABα)
=[A](Bα ^·.·^ Bα)
=|A|·|B(α···α),
hence
[AB| = |A]·|B].
We can relate this to the determinant of a matrix as follows. Let
o'.-..,o" be a basis of L and la;ll an n x n matrix. Set
α;=∑ajoj.
Then
α A .. Aαn=ayo A... o".
In particular,if one obtains the matrix representation of A with respect to
the basis (o') by
Ao'=∑a',
then
Ao ·.·Ao"=|a'·"·o”，[A|=[a.
2.3.Exterior Products
We now observe that our spaces Lhave a built-in multiplication process
called exterior multiplication anddenoted by^for obvious reasons.We
is 0 by definition if p+q>n):
:(^"L)X(△"L)→→^+L.
It suffices to define ^ on generators and use the basic principle at the end of
Section 1 to extend it to all p- and q-vectors:
gv...vgvdv...v=(gv...vg)v(v...v)

---
## Page 23

2.3.EXTERIORPRODUCTS
The basic properties of this exterior product are
(1)入 μ is distributive,
(2)^ (μv)=(μ) v, the associative law
(3）μ=(-1）pμ.
Property (3) simply says that any two vectors of odd degrees anticommute,
otherwise vectors commute.The following will illustrate why this is the
case:
(ααα3)β=-（αα2βα3)
=(-1)²(αβα2α3)
=（-1)²β（αα2α3),
(ααα3)(ββ2)=(-1）β（αα2α3)β2
=(-1)²(-1)²(ββ2)(αα2α3)
=(-1）)32(β β2)(αα2α3).
Examples.We take for L the linear space based on the differentials
dx,dy,...and,as is customary,omit the exterior multiplication sign ^
between dx's.Thus dx dy denotes dx ∧ dy.
1.(Adx+Bdy+Cdz)^(Edx+Fdy+Gdz)
= (BG -CF)dy dz + (CE -AG)dzdx +(AF -BE)dx dy,
illustrating the vector-, or cross-product of two ordinary vectors.
2.(Adx + Bdy + Cdz) ^ (Pdydz + Qdzdx + R dx dy)
=(AP+BQ+CR)dxdy dz,
illustrating the dot-, or inner-product of vector algebra.
3.Let α be any form of odd degree.Then
α²=αα=0.
For if α and β are of odd degree p, then
β^α=-αβ.
We setβ=α to have
αα=-αα，2（αα)=0，αα=0.
4.Here we take
@= dpdq+ ...+ dpndy”,
a form arising in mechanics. The two-forms dp;dq' all commute, hence
@=（n!)dpdq²dpdq²..·dpdq
= (-1)(n-1)/2(nl)dp..- dpn dq ..· dq".

---
## Page 24

10
II.EXTERIOR ALGEBRA
The product dp1·.·d" is called phase-density. We shall discuss this
further in ChapterX.
We apply the exterior product to obtain the Laplace expansion of a
determinantbycomplementaryminors.
Let lla;ll be an n x n matrix. For H = {h,.".,h,}, set
@1,h,...a1,hp
Set p+q=n.ForK={k,..·,kg}, set
ap+1,k
CK
an,k1
Thus if K = H', the complementary set of indices to H (always arranged in
natural order), then bh and ck are complementary minors of la;ll.
Now set
α=∑ajoj
where (o') is a basis of L. We easily see that
α...α,=∑bHH,
αp+1  ... αn =∑cKoK,
hence
α···αn=（α··.α)（αp+1···α）
=∑bHCxoH AoK.
But
α1·.·α=a(···o)
and
0
H+YH
H,H'(..·o”)
ifK=H',
hence
HH=
H
If H={h,...,h},H'={k1,...,ka},then
H,H' = sgn(
/1
h，
2.4. Linear Transformations
In this section we deal with two linear spaces M and N with
dim M=m，
dim N =n.

---
## Page 25

2.4.LINEAR TRANSFORMATIONS
11
Let us agree that when we need bases, o,..· , o" willdenote a basis of M and
T', ... , t" a basis of N.
Let A be a linear transformation,
A:M→N.
The mapping
(α，·.·,α)—→Aα·.·Aαp
sends
X"M-→>'n.
It is alternating multilinear, hence defines a linear transformation, denoted
^” A on ^" M to ^” N. This exterior pth power of A is defined on
generators by
(PA)(α  ... α,) =Aα ...  Aαp.
Suppose A is represented by the m × n matrix |a; according to
Ao' =∑a';t.
The oH and tK form bases of ^ M and  N, respectively, where H and K
are ordered sets of p indices. 'We have
...V=(V)
=ak···a,.·.t
=∑aktK.
Hence ^A is represented by the matrix
Hakll
of all p × p minors of la',l. This is sometimes called the pth compound of
Ila',ll.
Suppose one has three spaces L, M, N and this situation:
B
AB
N
We compute ^”(AB):
^”(AB)(α ^ ..·^α,) = (ABa) ^ ·… ^(ABap)
=(∧²A)[(Ba)··△(Bap)]
=(>P A)[(>B)(α  ···α,)]
=[(△A)(△B)](α ···α),

---
## Page 26

12
II.EXTERIORALGEBRA
hence
^” (AB)=(ΛP A)(A B).
It follows that the pth compound of the product of two matrices is the
product of their pth compounds, a nontrivial result.
We must consider one other matter. Again let A:M -→ N. Suppose
w is in ^" M and n is in ^ M. Then
(△P+aA)(∞n)=(ΛPA)(∞)(ΛA)(n).
For if we take monomials, @ = α ^ "· ^ αp, = β ^ ·"·  βq, then
(△p+aA)(@n)=(<p+aA)(α··αβ···βq)
=Aα··Aβq
=(Aα·.·Aα)(Aβ·.·Aβ)
·()(VbV)v(∞)(VaV)=
2.5. Inner Product Spaces
In the remainder of the chapter we shall study a space L which has an
inner product (α, β). This is a real-valued function on L X L which is
(i)Linear in each variable,
(ii)Symmetric: (α,β)=(β,α),
(iiNondegenerate: if for fixed α,(α,β) = 0 for all β, then α = 0.
Example 1. The Euclidean inner product on E" is given by
α=(a，·..,an)，β=(b1，·..,bn),
(α,β)=ab+..·+anbn.
Example 2. The Lorentz inner product in four-space:
α=(a，·.·,a4),，β=(b1，·.·,b4),
(α,β) =ab1 + a2b2+ a3b3  c²a4b4
where c is the speed of light.
Condition (ii) is equivalent to the following. If o, .. , o" is a basis of L,
then
(o, o)l ≠ 0.
(The left-hand member is the Gram determinant,or Grammian.）For this
determinant vanishes if and only if there is a nontrivial solution(a1,·,an)
of the homogeneous system
∑a(o',o)=0.

---
## Page 27

2.5.INNERPRODUCTSPACES
13
But this is the same as having the vector
α=∑a;gi
satisfy the relation (α, β) = 0 for all β.
An orthonormal basis of L consists ofa basis o',.··,o"such that
(,0)=±8i.
If there are r plus signs and s minus signs, then r + s = n, and t = r -- 8 is
the signature of the inner product.It does not depend on the choice of basis.
Itis abasicfactthateachinner productspaceLhas anorthonormalbasis.
This is proved in several steps.
1.If dim L >0,there is a vector o in L such that (o,o)≠ 0.
For if (α, α) = O for all α, then
0=(α+β,α+β)=(α,α)+2(α,β)+(β,β)
=2(α,β),(α,β)=0for all α,β,
a contradiction to nondegeneracy.
2.Pick a maximal sequence o',.·,o”of vectors satisfying
(0',∞)=±8.
Let M be the subspace of L these vectors span.Then dim M =r.[The
o′ are independent since ∑a;o′ = 0 implies ∑a;(o',o) = 0, ±a; = 0.] We
supposer<n.
3.LetN be the orthogonal complement of M,i.e.,N is the space of all
vectors β such that (α, β) = 0 for all α in M. Since N is determined by the
r relations (o',β)=0, dim N ≥n -r. But obviously M N = 0 (i.e.,
the only vector common to M and N is 0),hence dim N =n-r,M and N
together span L, M + N = L.
4. N itself is an inner product space relative to the inner product of L.
Only the property (i) of nondegeneracy must be checked. Suppose β is in
N and (, β) = 0 for all y in N. But (α, β) =0 for allα in M, hence (α, β) = 0
for all α in L since M and N together span L. Hence β = 0.
5.By (l), there is a vector α in N such that (α,α) ≠ 0. We set
gr+1 =α/(α,α)1/2
and see that we have constructed a sequence o,..·,or+1 longer than a
maximal one.Since this is impossible we conclude that we must have had
r = n in the first place, which completes the proof.
There is another basic property of inner product spaces which we shall
need below.
Let f be a linear functional on L.Then there is a unigue vector β in L such
that
f(α) =(α,β).

---
## Page 28

14
11.EXTERIOR ALGEBRA
This is easily established by taking an orthonormal basis o',...,o". We
setb;=f(o²)andforβsimplytake
β=∑±b=∑(o,o)bo.
For then
(0²,β) = ∑(0,o)b;(0,0)=b; =f(o).
2.6.InnerProductsofp-Vectors
Againwe startwith ann-dimensional vector spaceLwith aninner product
(α,β). We shall define an induced inner product on each of the spaces
^"L. We set
(入,μ)=I(α;β;)1
for =α··αp,μ=β·.·βp.This definition works because
the determinant on the rightis an alternating multilinear function of the
α's, ditto the β's.This means the formula defines a scalar-valued function
on (^" L) X(^" L) which is linear in each variable. Next (μ, A) = (, μ)
because interchanging the rows and columns of a matrix (transposing) does
not change its determinant.
ing with respect to an orthonormal basis o,."·,o" of L. As usual the
o, H ={h <h2<·..<hp}, form a basis of ^²L. We have
(,oK) = I(o,o)).
If H ≠ K, this is zero since the determinant has a row (also a column) of
zeros. If H = K, all but the diagonal elements vanish and these are ±1,
hence
(H,oK)=±SH,K
In other words; the o form an orthonormal basis of " L, nondegeneracy
follows free of charge.
In particular o = o ^ ·"· Λ o" is an orthonormal basis of ^" L and
(0,0) =(0, 01) ..·(0”, 0") = (-1)(n-3/2
where t is the signature of L.
For another example, set
V...V+V-V...V=,
forming a basis of "-1 L. Clearly
(α,α)=(0,0)/(0',0′)=(o,0)(o',0′),
hence
(∑aα'Eb;a)=(o,o)E(o,o)ab;
=(o, o)(∑a;o', ∑b,o).

---
## Page 29

2.7.THESTAROPERATOR
15
2.7.The Star Operator
Again let L have inner product (α, β). We shall take a definite orientation
of L which will remain fixed. (This simply means we take one basis for L
and only consider other bases which are expressed in terms of this one by a
matrix with positive determinant. The space L has two orientations and
we take one of them.） We only use bases coherent to the orientation.
We shall define an operation *, called the (Hodge)star operator.This will
be a linear transformation on "L onto "-P L.This operator depends,
of course, on the inner product and also depends on the orientation.Re-
versing orientation will change its sign.
WenotethattheorientationofLdeterminesadefiniteorthonormalbasis
OofA"L.
Now fix Λ in ^" L.The mapping
μ-→μ
is a linear transformation on ^"-P L into the one-dimensional space ^" L.
Wemaywrite
μ=f（μ)
where f, is a linear functional on ^"-p L.By our result at the end of
Section 2.5, there is a unique (n -- p)-vector, which we denote *入 to indicate
its dependence on ,such that
μ=(*,μ).
This equation defines the * map which is evidently linear on ^"L into
'1a-V
In order to compute * for generators of ^" L, in view of the linearity, it
is enough to compute *where入=o^··^o”and where o',··,o”is
an orthonormal basis.Let K run over sets of q = n -- p indices.Then
入oK=(*入,αK).
The left-hand side vanishes unless K = {p + l, p+ 2,·"·,n}, hence
*=co+1·.·”
and the constant c is determined taking K = {p + 1,·",n}:
=oK=c(o,oK)o,
c=(oK,o)=±l,
*入=(cK,oK)oK.
For definiteness, set H = {1, ··,P},K = {p + 1, ..·, n}. We have proved
*oH =(oK, oK)oK.

---
## Page 30

16
II.EXTERIORALGEBRA
Since oK ^ oH =(-1)(n-p)oH ^ oK, we deduce, taking orientation into
account,
*K=(-1)p(n-P)(H,H)H,
hence
*(*H)=（-1)(n-P)(OH,H)(oK,oK)H,
*(*H)= (-1)p(n-p)(α,c)H
= (- 1)p(n-p)+(n-t)/2gH.
wheretis thesignature.
It follows that if α is any p-vector,then
**α = (- 1)p(n-p)+(nt)2α.
Another consequence of theseformulasis thisresult.
Ifα,βarep-vectors,then
α *β=β *α =(-1)(n-)/2(α,β).
For when β= o# as above, the only generator α= o′for which both sides
do not vanish is α = o, and then
αA *β=(ok,K)K=（k,K）
=(H,oH)(-1)(n-t)/2
= (- 1)(n-t)/2(α,β),
Example 1. We take 4-space with coordinates so normalized that dx,dx2,
dx3,dt is an orthonormal basis with (dx,dx) =1,(dt,dt) = -1. We have
n = 4, t = 2, (-1)(n-t)/2 = -1. We shall study certain two-forms. For
p = 2, p(n --p) =4. Thus
*(dx²dt)= dx/ dxk
where (i,§, k) is cyclic order,
*(dx′dx) =-dx'dt.
Let E; be the components of electric field strength,H; the components of
magnetic field strength (all in free space) and consider the form
@=(Edx+Edx²+Edx²)dt+(Hdx²dx²+Hdx²dx²+Hdxdx²).
Then
*0=-(Hdx²+Hdx²+Hdx²)dt
+(Edx²dx²+Edx²dx+Edx²dx²).
We shall see the use of these forms in Maxwell's equations later.