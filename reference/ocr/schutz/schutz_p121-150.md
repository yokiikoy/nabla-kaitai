<!-- source-pdf: Bernard F. Schutz-Geometrical Methods in Mathematical Physics-Cambridge University Press (1980).pdf | pages 121-150 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 121–150

## Page 121

3.18 Spherical symmetry 
111 
Exercise 3.26 
Let {y! j= 
= 1,2,3}stand for the functions (Y, -1, Yio, Y, 1). and let 
{x7} stand for te 
y, 2}. Find the transformation matrix Ai, = dy! /ax® 
and its inverse ΛΙ, 
;'. Find the matrix xt ,' of the operator J, on the 
spherical harmonic basis 
L(yi) = Xi py®, 
by the methods of exercise 3.24(b). Transform X J be to the Cartesian 
basis 
Xi, = 
My A", X'y, 
and show that it is just L,; of equation (3.63). 
Notice that / = 1 is the smallest faithful representation of SO(3): 1 = 0 is not 
faithful. This is usually called the fundamental representation of SO(3). We will 
encounter another set of irreducible representations of SO(3) when we study 
vector spherical harmonics in §4.28. There the representation space will not be 
that of functions on the sphere but of vector fields on the sphere. 
Finally, we need to remark on the relation between representations of SO(3) 
and of its covering group SU(2). (This passage may be skipped by readers who 
have not studied §3.16.) Since there is a unique element of SO(3) associated 
with any one of SU(2), any reprensentation R(g) for elements g of SO(3) auto- 
matically defines a representation S of SU(2): for any u in SU(2) the transforma- 
tion S(u) is R(n(u)). If wu 
and u’ both correspond to the same element of SO(3), 
then S(u) = S(u’) for such representations. But SU(2) will also have other repre- 
sentations, say T, for which T(u) # Τι) even when π(ιι) = πί(ι). These are 
sometimes called double-valued representations of SO(3). Again we shall merely 
quote the result: the irreducible representations of SU(2) are characterized by an 
index k 2 0 which is either an integer or half an odd integer. Those for which k 
is an integer are representations of SO(3) for the same index (i.e. k = 1). The 
others are only double-valued representations of SO(3). An example of the latter 
is provided by the matrix representation we used to define 
SU(2), which is a 
representation in two complex dimensions. It has k = 3 and is called the spin-} 
representation. As with the 7 = 1 SO(3) representation, it is the smallest faithful 
one for SU(2). If we take any basis vector of the space (called a spinor) and 
operate on it by exp (Μι) as ¢ goes from 0 to Απ. we see that the corresponding 
path in SO(3), exp (11,1). goes from 0 to 2m twice. When the sequence of trans- 
formations reaches t = 27 we are back at the origin of SO(3), but are at —e 
in 
SU(2). For this reason it is said that the spinor changes sign (e > — e) if it is 
rotated once through an angle 27.

## Page 122

Lie derivatives and Lie groups 
112 
It is indeed remarkable that this correspondence between representations is 
not simply a mathematical game. The wave-function of a spin-} elementary 
particle is described by an element of an irreducible vector space of SU(2) for 
nonintegral k. This is one example of what a physicist might regard as the 
beautiful simplicity of nature. We begin with the Lie algebra of spherical sym- 
metry and we find that the group 
SU(2), not SO(3), is the simplest one having 
that algebra, in that it has the simplest global topology. We then find that, 
despite the difficulty of ‘visualizing’ the action of SU(2) in R*, nature has made 
the group more fundamental than SO(3) by providing particles which belong to 
those of its representations which are not representations of SO(3)! 
3.19 
Bibliography 
An old-fashioned but very complete book on Lie dervatives is K. Yano, 
The Theory of Lie Derivatives and its Applications (North-Holland, 
Amsterdam, 1955). 
The completeness theorems for self-adjoint operators may be found in 
F. Riesz & B. Sz.-Nagy, Functional Analysis (Ungar, New York, 1955). 
The close relation between Lie groups and Lie derivatives is explored in 
F. W. Warner, Foundations of Differentiable Manifolds and Lie Groups 
(Scott, Foresman, Glenview, ΠΙ.. 1971);in M. Spivak, A Comprehensive 
Introduction to Differential Geometry (Publish or Perish, Boston, 1970) 
vol. 1; and in L. Auslander & R. E. MacKenzie, Introduction to Differ- 
entiable Manifolds (McGraw-Hill, New York, 1963). 
For more on Lie groups, see: R. Hermann, Lie Groups for Physicists 
(Benjamin, Reading, Mass., 1966); or H. Weyl, The Theory of Groups 
and Quantum Mechanics (Dover, New York, 1950). Representation 
theory for the most important groups is discussed in most quantum 
mechanics textbooks, in Weyl above, and in: H. Lipkin, Lie Groups for 
Pedestrians (North-Holland, Amsterdam, 1966);M. A. Naimark, Linear 
Representations of the Lorentz Group (Pergamon, New York, 1964); 
and I. Μ. Gel’Fand, R. A. Minlos & Z. Ya. Shapiro, Representations of 
the Rotation and Lorentz Groups and Their Applications (Pergamon, 
New York, 1963). 
A helpful reference for the matrix algebra we have used is M. W. Hirsch 
& S. Smale, Differential Equations, Dynamical Systems, and Linear 
Algebra (Academic Press, New York, 1974).

## Page 123

4 
DIFFERENTIAL FORMS 
The calculus of differential forms, developed in the early part of this century by 
E. Cartan, is one of the most useful and fruitful analytic techniques in differ- 
ential geometry. The catalogue of concepts that are unified and simplified by 
forms is astonishing: the theory of integration on manifolds, the cross-product, 
divergence, and curl of three-dimensional Euclidean geometry, determinants 
of matrices, orientability of manifolds, integrability conditions for systems of 
partial differential equations, Stokes’ theorem, Gauss’ theorem, and much more. 
As with most mathematical and physical ideas which are truly fundamental, the 
mathematics of forms is very simple. In this chapter, we introduce forms in the 
geometrical context in which they arise most naturally, and we then systemati- 
cally develop their power. 
A The algebra and integral calculus of forms 
4.1 
Def:nition of volume — the geometrical role of differential forms 
Until now we have avoided giving our manifolds any shape or rigidity. 
We have mentioned the possibility of defining metric tensors, but we have con- 
centrated on those analytic tools which are definable without reference to any 
particular metric. Now we will turn to the study of a particularly useful class of 
tensors: those which can serve to define volume elements on manifolds. 
Consider the notion of volume in two dimensions, where it is called area. Any 
pair of (infinitesimal) vectors in Euclidean space defines an (infinitesimal) area, 
as in figure 4.1: the area enclosed by the parallelogram they define. Now, a given 
area is defined by many different pairs of vectors, which may differ from one 
another in length and enclosed angle, as in figure 4.2. The notion of area is, 
therefore, less restrictive than the notion of a metric: the Euclidean metric 
defines the lengths of vectors and their enclosed angle, while the specification 
of area gives only one number associated with the two vectors. Naturally, if a 
metric exists it should uniquely define the area, and we shall show how this 
comes about later. But it is possible to define an area for a two-manifold (or a 
volume on an arbitrary manifold) without having to define a metric on the 
manifold. Indeed, many different metrics could define the same volume.

## Page 124

Differential forms: algebra and integral calculus 
114 
Suppose that in a two-dimensional manifold we have at a point two linearly 
independent infinitesimal vectors, forming a two-dimensional parallelogram. We 
wish to define for this figure a (small) area, i.e. to associate with the two vectors 
a single number. This number ought to double if we double the length of one 
vector; moreover, we should require it to be additive under addition of vectors, 
1.6. 
_ 
κ 
area(@, ϱ) + ατεα(α, ϐ) = area(@,b+ 6). 
That this is true in Euclidean space is proved geometrically in figure 4.3. In the 
second-to-last step we have used the fact that the area of a parallelogram is 
Fig. 4.1. Two pairs of vectors and the area they define. 
Fig. 4.3. Geometrical proof that the area of a parallelogram is the value 
of a tensor. 
1 
! 
_ 
α 
a 
] 
area (a, b) = | 
; 
area(a,c) =| 
| 
area (a, b + 7) 
Se 
sd 
= area (da, b) + area (a,c).

## Page 125

4.2 Notation and definitions for antisymmetric tensors 
115 
unchanged if one of its sides is displaced an arbitrary amount along the straight 
line it defines. So we have proved that area( , ) isin fact a tensor, bilinear 
in its arguments. Since the area is a number, this is a (9) tensor. Moreover, if a 
and ὃ are parallel, the area must vanish. The following exercise shows that as a 
consequence the tensor must change sign if @ and b are exchanged. 
Exercise 4.1 
Prove that if B is a (8) tensor with the property that B(V, V) = 0 for 
all V, then B(U, W) = — B(W, U) for all U, W. (Hint: take V= U+ W.) 
We say that B is antisymmetric in its arguments. 
Consider this more closely. In figure 4.4 two vectors are drawn defining a 
parallelogram of a certain area. In terms of components, the area is (to within a 
sign) the determinant 
y~ 
y* 
w* 
Ww 
Its antisymmetry under interchange of V and W is manifest. 
In ordinary uses one forgets the sign and calls the area the absolute value of 
that determinant. It will be convenient for us to keep the sign, since it contains 
information about the left- or right-handedness of the pair of vectors. We shall 
discuss this in more detail below. We shall also develop in more detail the evident 
relation between volume-tensors and determinants of matrices. But first we must 
develop the algebra of antisymmetric tensors. At first we will concentrate on 
their properties at any point, generalizing to fields later on. 
area 
= 
4.2 
Notation and definitions for antisymmetric tensors 
As in exercise 4.1 above, a (2) tensor is said to be antisymmetric if its 
value changes sign on interchange of its arguments: 
G(U,V) = — @(V, U) forall U, Ve & antisymmetric. 
(4.1) 
A tensor of type (), p 2 3, is said to be completely antisymmetric if it changes 
sign on interchange of any two of its arguments. Antisymmetric tensors can 
always be constructed from arbitrary ones. For example, if @ is a (9) tensor and 
Fig. 4.4. The area defined by V and W.

## Page 126

Differential forms: algebra and integral calculus 
116 
pa (3) tensor then their totally antisymmetric parts are the tensors whose values 
on arbitrary arguments are given by: 
+ 
(U,V) = Lad, V)— @(V,U)], 
(4.2) 
A 
3,(0,V,W) = -_ 
(a0. 7.) + VW, 0) + 
0,7) 
—~ BV, U, W) — p(w, V, U) — p(U, W, γ)] . 
(4.3) 
The rule is to take every permutation of the arguments; odd permutations con- 
tribute minus signs and even ones plus signs. The factors 1/2! and 1/3! are the 
conventional normalization, which is appropriate to calling @, the antisym- 
metric part of @&. These considerations all have counterparts in index notation, 
obtained by letting the arbitrary vectors be basis vectors: 
. 
1 
. 
4 
(Oa) = 21 (Wi; — Wj) = wry), 
(4.4) 
. 
1 
_ 
4 
air = 31 (Dijn + Pini + Prij — Pjix μι δι) = Pury. 
(4.5) 
Here we have introduced the square bracket notation [i...k]| to denote a com- 
pletely antisymmetric set of indices, including the corresponding normalization 
factor. In what follows we will use a notation introduced above: a tilde (~ ) over 
a tensor’s name, e.g. f, denotes a completely antisymmetric tensor. The one- 
form, for which we use the same notation, is a ‘degenerate’ case of this, because 
it has only one argument. 
Exercise 4.2 
(a) Prove that if the components of a (%) tensor ῥ are antisymmetric under 
interchange of any two indices, then f is a completely antisymmetric 
tensor. 
(b) Suppose {A;;,} are the components of a completely antisymmetric 
tensor. Show that 
Αμ 
Αμ: 
(ο) Suppose that A is an antisymmetric (9) tensor and B an arbitrary (2) 
tensor. Show that 
A,BY = AjBM™), 
i.e. that the contraction of A with B involves only the antisymmetric 
part of B. 
(d) Suppose A is as in (ο) and B is a symmetric (6) tensor: B(®, 6) 
= B(G, ὤ) for all one-forms © and &. Show that

## Page 127

4.3 Differential forms 
117 
A,B = 0. 
(4.6) 
An important property of completely antisymmetric tensors is the following: 
on an n-dimensional vector space, a completely antisymmetric (ϱ) tensor (p <n) 
has at most 
n! 
p\(n—p)! 
independent components. To see this, note that any component is defined by 
choosing p different numbers from the set (1,..., 7). (They must be different, 
because the component vanishes if any two indices are equal, just as in exercise 
4.1.) The order in which the p numbers are chosen — their order as indices on 
the tensor — can at most affect the sign of the component, so all components 
whose indices are simply rearrangements of a given set of p numbers are known 
if any one of them is known. The number of independent components is there- 
fore the number of different sets of p numbers chosen from n numbers, which 
is the binomial coefficient given above. 
n 
Dp 
(4.7) 
Exercise 4.3 
Prove that if p >n all the components of a completely antisymmetric 
(ϱ) tensor on an n-dimensional vector space vanish. 
4.3 
Differential forms 
A p-form (p 2 2) is defined to be a completely antisymmetric tensor 
of type ()). As before, a one-form is a (°) tensor. A scalar function is a zero- 
form. The number p is the degree of the form. 
Exercise 4.4 
Show that the set of all p-forms for fixed p is a vector space itself, 
under the addition operation defined in exercise 2.4. This is then a 
subspace of all (ϱ) tensors. What is its dimension? 
Just as (2) tensors could be made from (@) tensors using the operation ®, we 
define an operation a (called ‘wedge product’) for constructing two-forms from 
one-forms: If δ and g are one-forms then 
+ 
PAG = P®G-GOp 
(4.8) 
is their wedge product. There is no factor of 1/2! in front, by contrast with 
equation (4.2)!

## Page 128

Differential forms: algebra and integral calculus 
118 
Exercise 4.5 
Show that 6 a g is a two-form. Show that pf a p = 0. 
Exercise 4.6 
Let {é,,i=1,...,n} bea basis for a vector space and {ῶ)} its dual 
basis for one-forms. Show that {@/ , @" 
,j,k=1,..., n} is a basis for 
the vector space of all two-forms. Hint: by considering explicitly the 
numbers a;; = &(@;, é;), where & is an arbitrary two-form, show that 
1 
oo. 
9 
ἃ --σιαμῶ λῶ). 
(4.9) 
Note carefully the factor of 1/2! in (4.9), which occurs because the sum on 
(i, 7) includes equal contributions from 63 © @! and @ ® 6. This factor 
appears here because we did not put it into the definition of &' a ὤ], equation 
(4.8), as some textbooks do. This is a matter of convention. 
The rule for wedge products extends naturally to three-forms: 
PA({TAF) = HAG ar 
= PraGanr=pOBG@F+gGgBr@pt+—... 
(4.10) 
using the same permutations and signs as in the previous paragraph. Notice that 
this expression and its generalization to higher numbers of one-forms permits 
one to define wedge products for arbitrary p- and q-forms, since by exercise 
4.6 any p-form can be written as a linear combination of wedge products of p 
one-forms (the basis one-forms). 
The set of all forms of arbitrary degree, equipped with the anticommutative 
multiplication a, is called a Grassmann algebra. 
Exercise 4.7 
Show that the sum of the dimensions of all the N-form spaces for 
p <nis 2”. (Hint: use the binomial theorem.) This is the dimension 
of the space which has the Grassman algebra. 
Exercise 4.8 
Show that if f is a one-form and g a two-form, then 
(δλδ = Pidin + Dini t+ Pedi 
= 3Ppidjr} 
More generally, show that if δ is a p-form and g a q-form, 
+ 
AQ). je 
= Ορ Pri. Ve...) - 
(4.11)

## Page 129

4.4 Manipulating differential forms 
119 
4.4 
Manipulating differential forms 
The algebra of forms is fairly simple, but it can lead to difficulties 
keeping track of signs and factorials. In this and later sections the student should 
find that careful, patient reasoning is the best approach to proving any result. 
For instance, let us prove the commutation rule for forms. If δ is a p-form and 
ᾷ aq-form, then 
+ 
Dag = 
© αι) σᾷλρ. 
(4.12) 
To see this, first express f and ᾷ as sums over their components times wedge 
products of the form @'a...a @! and @* a ...a G! (p-factors and q-factors, 
respectively, in each wedge product). Now we shall show that (4.4) applies to 
each of the simple products 
(SIAL. AB)A(@EA... 
AG). 
By the associativity of the wedge product, the parentheses in this expression 
are unnecessary. Now, if any two factors are exchanged (e.g. @! with @*) the 
expression changes sign. To move @ through the g-factors @’ a... a G3! 
requires g such exchanges, so that 
k 
WA. AIAG A... AG = (1) GAL. AGFA... 
AG! A 6S, 
Doing this for each of the p-factors in @'a ... A @ gives [(— 12412 times the 
original, which proves (4.12). 
An operation we will find useful later is the contraction of a vector with a 
form. A p-form requires p vector arguments to give a real number. If it is 
supplied with one argument then it becomes a (p — 1)-form. To be definite we 
define 
+ 
ἂ(ξ) = a(é, 
> 
9 
9788 .), 
[α(2)1/ 
= αμ... εξ. 
(4.13) 
p — 1 empty slots 
as the (p — 1)-form obtained by contracting & with £. Note that putting £ into 
any slot other than the first would only affect the sign of &(£). To get a feeling 
for what this means, consider & = p λᾶ, where pf and q are one-forms: 
(Dag) = C@FI—-JT OPE) 
PE) 
F— GE) 
B. 
Thus, although ἕ is contracted with the first slot of B a J, the permutations 
implicit in the a-operation ensure that ἕ is contracted with each one-form in the 
wedge product. Similarly, for a product of p one-forms we find 
Pi 
, 
(Sn BaA.. AP)(E) = HOA... 
nO --δῶλ...λῶ" 
nl, 
(4.14)

## Page 130

Differential forms: algebra and integral calculus 
120 
From this and the generalization of (4.2) it follows that if & is a p-form, 
| 
i 
o— iF" 
This is, of course, implied directly by (4.13) and (4.9). Similarly, if @ is any form 
and Bis a p-form, then 
(Baa) (E) = BE)AG+ (— 1PBn GE). 
(4.16) 
Again this can be proved by looking at each component of B a @. 
ijk OIA. AO. 
(4.15) 
aE) = 
Exercise 4.9 
Prove (4.16). 
A widely used alternative notation for ἄ(ξ) is £|@. 
4.5 
Restriction of forms 
An elementary but important concept is that of restricting a form to 
a subspace of the original vector space V. Since a p-form @ is a (ϱ) tensor, its 
domain is the set of all vectors in V (strictly, the domain is the product space 
VxVx...XV,p ‘copies’ of V). The restriction of & to a subspace W of V is 
the same p-form & whose domain is now restricted to vectors in W. We call this 
Gly: 
dlw(X,...,¥) = a¥,..., 
7), 
where all of 
¥,..., Y are in W. Thus, &y is defined only on W. Note that if the 
dimension m of W is less than p, the restriction &|y is necessarily zero (any p- 
form is zero on an m-dimensional space if p > m), and if p =m then &| 
yw has 
only one independent component. The operation of restricting a form is often 
called sectioning it, because the picture one has is of the vector subspace W 
being a plane passing through (sectioning) the series of surfaces that represent 
a form. A form is said to be annulled by a vector subspace if its restriction to it 
vanishes. 
4.6 
Fields of forms 
As with any tensor, a field of p-forms on a manifold Μ is a rule (with 
appropriate differentiability conditions) giving a p-form at each point of M. 
Then all our remarks up to now apply to forms as functions on the space ΤΡ at 
any point P of M. Only one point needs to be made: since a submanifold S of M 
picks out a subspace Vp of the manifold’s tangent space ΤΡ at every point P of S, 
we define the restriction of a p-form field & to S to be that field formed by re- 
stricting @ at P to Vp. We have seen an example of this for a one-form in $3.6.

## Page 131

4.8 Volumes and integration on oriented manifolds 
121 
4.7 
Handedness and orientability 
In an n-dimensional manifold there is only a one-dimensional space of 
n-forms at any point (equation 4.7). Choose some n-form field, and call it ©. 
Consider a vector basis {é,,..., @,} at a point P. Since these are linearly inde- 
pendent vectors, the number (@é,,..., @,) is nonzero if and only if @ #0 
at 
P. Therefore 6 separates the set of all vector bases at P into two classes, those 
for which @(é,,..., @,) is positive and those for which it is negative. These 
classes are in fact independent of ὤ. For, if ὤ' is any other n-form nonzero at 
P, then there exists a number f# 0 such that @’ = f@&. Any two bases which 
made © positive will give @’ the same sign (positive if f > 0, negative if f< 0) 
and so will again be in the same class. So all bases at a point can be put into one 
of two classes: right-handed and left-handed. (Which class has which name is, 
of course, a convention; what is important is that the classes themselves are 
distinct.) A manifold is said to be (internally) orientable if it is possible to define 
handedness consistently (i.e. continuously) over the entire manifold, in the sense 
that it is possible to define a continuous vector basis {@,;(P),..., @,(P)} whose 
handedness is the same everywhere. Clearly this is equivalent to being able to 
define an n-form which is continuous and nonzero everywhere. Euclidean space 
is orientable; the MObius band is not. 
4.8 
Volumes and integration on oriented manifolds 
We return now to our view that forms are related to volume-elements. 
In an n-dimensional manifold, a set of ή linearly independent (‘infinitesimal’ ) 
vectors define a region of nonzero volume, an n-dimensional parallelepiped. The 
volume of this region is then the value of an n-form. One is free to choose any 
n-form as the volume n-form; which one chooses will be determined by the 
particular problem one is solving. 
Now, integration of a function on a manifold involves essentially multiplying 
the value of the function by the volume of a small coordinate element and then 
adding up all such values. Following our discussion of volume-forms, we shall 
introduce a useful notation for this. Suppose @ is an n-form on a region U 
of an n-dimensional manifold M whose coordinates are {x',...,x”}. Then 
because all m-forms at a point form a one-dimensional vector space, there exists 
some f(x',..., x’) such that 
6 = fdx' an... a dx". 
To integrate over the U, we divide it up into tiny regions (‘cells’) spanned by 
n-tuples of vectors {Ax! 0/dx1, Ax? 0/dx?,..., Ax” 0/dx”}, where the {Ax’? 
are very small numbers. The integral of the function f over one small cell is 
approximately the value of f times the product 
Ax! Ax?... Ax” = dxta...adx™(Ax! a/dx!,..., Ax” δ/9χ3).

## Page 132

Differential forms: algebra and integral calculus 
122 
Thus, we have 
| fel, ...,x")d"x & G(cell). 
(4.17) 
cell 
Adding up all the contributions from the different cells and taking the limit as 
the size of each cell goes to zero gives what we call the integral of & over U: 
9 
Επ... 
(4.18) 
where the integral on the right is the ordinary integral of calculus and the 
integral on the left is our new notation. Since the version on the left does not 
mention coordinates, we must prove that it really does not depend on the co- 
ordinates chosen for U. We shall restrict our proof to two dimensions, since the 
generalization will be obvious. Consider first coordinates A and uw. Then we have 
ik = [200 μ) dad =| FO, μ) dr du. 
When we change to coordinates x and y, the chain rule gives 
~ 
~ 
δλ». 
ολ. 
dx = ἅλα, ν) = --ἄχ 
+— dy, 
Ox 
oy 
~ 
ὂμ» , ON~ 
du = “dk 
+ ἄν, 
Ox 
oy 
which follows from the definition of ἆλ as a gradient. So we get (remember 
dx a dx = 0 since it is antisymmetric) 
woo 
OAX~ , Ox 
ὃμ- , Or 
Dade = (eet AH) (Hes Hey 
Ox 
oy 
Ox 
oy 
= HE 
tH 
ἄνλᾶν 
Ox Oy 
we 
Oy Ox *” 
OXNOu 
ὀΌλομὶ- 
- 
[τπτ τπτ 
dx a dy. 
4.19 
ο. 4 
(4.19) 
The factor in front of dx Λ dy is the Jacobian of the coordinate transformation, 
O(A, µ)/(α. γ). From ordinary calculus we know that is how volume elements 
do in fact transform. Therefore, the (A, u)-integral of fis related to the (x, y)- 
integral of fin exactly the right way. 
But the value of f @ is not quite independent of the coordinates originally 
chosen. What we have shown is that a coordinate transformation does not 
change its value, but there is an ambiguity of sign in equation (4.17). This 
equation provided the original definition of f ὤ, and this definition would have 
given us the opposite sign had our original coordinate system had a basis of the

## Page 133

4.8 Volumes and integration on oriented manifolds 
123 
opposite handedness to the one we chose. The right-hand side of (4.17) would 
have been the same — the form is basis-independent — but on the left-hand 
side f would have changed sign. (This change is not the sort of coordinate trans- 
formation we discussed above, in which d”x would be multiplied by a negative 
Jacobian and all would be well. It is a change in the original identification of 
the symbol f @ with an integral from the calculus.) This ambiguity cannot be 
avoided. It is conventional to choose an orientation in U — i.e. define which of 
the two sets of bases is right-handed — and to use a right-handed coordinate 
system in the definition (4.17). We therefore find that the integral of @ over 
the region U is independent of everything except orientation. 
It was important in this argument that U be covered by a single coordinate 
system. Can we extend this integral to all of M, which may not have a global 
coordinate system? It is clear that if two coordinate patches have a single 
connected overlap region, the orientation chosen on one induces a unique 
orientation on the other, and the integral over the union of the two regions is 
well-defined. Clearly this can be extended to M as a whole if and only if Μ is 
orientable. From now on we shall restrict ourselves to integration on orientable 
manifolds, but it must be mentioned that the theory has been extended to non- 
orientable manifolds by de Rham, and this can have interesting physical appli- 
cations (see the paper by Sorkin (1977) in the bibliography). 
Integration as we have defined it is always done over forms of the maximum 
degree: n-forms on n-dimensional manifolds. One can of course integrate a 
p-form over a p-dimensional submanifold, provided the submanifold is itself 
internally orientable. How is the internal orientation of a submanifold S related 
to that of M? Suppose Μ is orientable and P is a point of ο. Given an n-form 
ὦὤ defined as ‘right-handed’ (or ‘positively oriented’) at P, is there a unique 
‘induced’ orientation for p-forms of S at 
P? Unfortunately not, because & on 
its own does not do anything for S, as its restriction to S is zero since p <n. 
What is usually done is to reduce ὢ from an n-form to a p-form by defining 
n — p linearly independent ‘normal vectors’ at P not tangent to S and defining 
the restriction of the p-form 
ο.” ὤ(Πι,.... An-p) 
to S to be right-handed. This definition clearly depends on the choice of the 
vectors {f;}, including the order in which they are numbered. Such a choice is 
called choosing an external orientation for S at P. We shall give an example of 
this in our proof of Stokes’ theorem below. If it is possible to define the external 
orientation {#;,i=1,...,—p} continuously over all of S (and ‘continuously’ 
means keeping the 7; linearly independent and not tangent to ) then S is said 
to be externally orientable.

## Page 134

Differential forms: algebra and integral calculus 
124 
It is clear that if some open region of M containing S is orientable then either 
S is both internally and externally orientable or it is neither, and that if no such 
region of M is orientable S may be one but not both. For example, consider a 
Mobius strip as a two-dimensional submanifold of R? (figure 4.5) and a curve in 
the strip as a one-dimensional submanifold of the strip (figure 4.6). Set up a 
right-handed triad of vectors at any point P of the strip, two lying in the strip 
and one out of it. Carry them continuously once around the strip, keeping the 
two always tangent to it. The outward pointing one always returns pointing to 
the opposite side: the Mébius band is not externally orientable in R?. Similarly, 
set up two vectors in the strip, one tangent to the curve @, and the other not. 
Transport these continuously around and the outward pointing one returns 
pointing to the other side of the curve in the strip. Since we know that the curve 
is internally orientable (this is a property independent of any space it is em- 
bedded in) it cannot be externally orientable in a larger nonorientable manifold. 
Fig. 4.5. The Mobius band in R®. It is easiest to imagine it made of 
rubber, lying flat on the page except near the top of the figure, where 
the single twist is. A triad at P, carried clockwise around (dashed path) 
returns in a way which cannot be continuously deformed into its 
original while keeping vectors | and 2 in the band and all three linearly 
independent. 
Fig. 4.6. Curves in the Mobius band. Curve @, is not externally orien- 
ted: vectors 1 and 2 begin at P and are transported as in figure 4.5. 
They return in a way which cannot be continuously deformed into 
the original while keeping 1 tangent to the curve and both linearly 
independent. But curve @, is externally orientable because it has a 
neighborhood (dotted line) in which a consistent choice of orientation 
is possible.

## Page 135

4.9 N-vectors, duals, and the symbol ευ x 
125 
By contrast, the curve 62 is both internally and externally orientable in the 
strip because it does not ‘feel’ the nonorientability of the strip: it has a neigh- 
borhood in the strip which is orientable. 
4.9 
N-vectors, duals, and the symbol εη _, 
We have so far considered completely antisymmetric (9) tensors, but 
of course the Grassmann algebra can be constructed for (0) tensors in a parallel 
fashion. A completely antisymmetric (0) tensor is called a N-vector. As for 
forms, the vector space of all p-vectors at any point in an n-dimensional mani- 
fold is of dimension CP. 
Notice that at a point there are four spaces which have equal dimension: the 
vector spaces of p-forms, (n — p}-forms, p-vectors, and (nm — p}vectors all have 
dimension Cp = 6η. 
ρ. Under certain circumstances one can find a 1-1 mapping 
between various of these spaces. We saw in §2.29 that a metric tensor gives a 
1-1 map from (ϱ) tensors to (§) tensors. It is not hard to see that this map pre- 
serves antisymmetry, so that it maps p-forms into p-vectors invertibly. Whether 
or not a metric is defined, however, a volume n-form @ (i.e. an n-form which is 
nowhere zero) provides a mapping between p-forms and (η — p}vectors. This 
map is called the dual map, and we now show how to construct it. (Do not con- 
fuse this map, which depends on & and maps a single (ϱ) tensor into a unique 
("9 ?) tensor and viceversa, with the concept of a dual basis for one-forms dis- 
cussed in chapter 2, which does not involve & and maps a set of n (4) tensors 
into a unique set of n (3) tensors and vice versa.) 
A given g-vector T with components T*-* = ΤΗ: (ᾳ indices) defines a 
tensor A by the equation 
1 
; 
¢ 
Aj. = ο. 
(4.20) 
Symbolically, we write 
A = 6(T) 
or simply 
4 
A = *T. 
(4.21) 
We say that A is the dual of T with respect to ὤ. From (4.20) and the anti- 
symmetry of ww; 1 under interchange of any two indices it is clear that Aisa 
completely antisymmetric tensor of degree n — g (which is the number of indices 
on @ left over after contracting with the g indices on T). That is, Ais an (n—q} 
form. This map defines a unique (n — q}-form from any q-vector. We will show 
that it is invertible below, but first we will show that one has already become 
familiar with this map in the form of the cross-product in three-dimensional 
Euclidean vector algebra.

## Page 136

Differential forms: algebra and integral calculus 
126 
To understand this, recall that in Euclidean space one usually does not 
distinguish between vectors and one-forms: in Cartesian coordinates the com- 
ponents of a vector and of its associated one-form are equal. So consider two 
vectors U and V 
and their one-forms U and V. The two-form U a V 
has C3 =3 
independent components, which are U;V, —U,V,,U,V3 — U3V,, U2V3 
— U3V,.The vector U x V has the same components, and it is easy to show that 
*“UxV) = UanV 
(three dimensions). 
(4.22) 
Exercise 4.10 
Prove (4.22) by using (4.20). 
This iluminates a number of odd things about the cross-product: why it exists 
at all, why it does not exist in other than three-dimensions (only in three dimen- 
sions does the dual map take vectors into two-forms), and why U x V 
is an 
‘axial’ vector. This last fact comes from the fact that it is conventional to define 
ὦ in Euclidean space to give a positive volume to the basis (€, , 61, @3). If the 
handedness of the basis is changed, then so is the sign of @ and, consequently, 
the sign of U x V (which depends on the sign of @ in that it must be mapped by 
G into Un V, whose sign does not change). Under an inversion of coordinates, 
then, the conventional cross-product changes sign. 
The map between T and “T is invertible because they each have the same 
number of components. (Said another way, contracting T with ὤ in (4.20) loses 
no information from T because T is already antisymmetric on all its indices.) 
That is, for a given p-form A there is a unique (n — p}-vector Τ for which 
A =*T. This can be formalized by defining an n-vector ω'"''", the inverse of 
a3, by the equation 
+ 
we Fo, ν = ΠΙ. 
(4.23) 
The factor of 
n! is used because the sum in (4.23) has n! equal terms: w!?3"--” 
Χ W493...n = W701 
ῃ =.... Then! factor assures the normalization 
] 
(123-9 
— 
; 
(4.24) 
© 123...n 
Then we say that 5 is the dual of B with respect to ®, 
4 
S = *B, 
(4.25) 
if (for B a p-form) 
; 
1 
. 
4 
ςἰ-..Ε 
— 7 Gght™ Εν. 
(4.26) 
To illustrate the inverse property of the two dual relations, let us look first at

## Page 137

4.9 N-vectors, duals, and the symbol εη. x 
127 
scalar functions. The function /, viewed as a zero-vector, has the n-form dual 
1ῶ. This n-form has the dual zero-vector 
1 
*(f®) = πως ως.) =f. 
Thus we have proved **f= 
f. 
The general relation of this sort is found as follows. Start with a p-form B 
and define the (ή — p)-vector 5 by (4.26). We take the dual of 5: 
1 
CS) = (n—p)! ωι. κ). 
1 
= p\(n—p)! ων). 
ως 
se 
FB. ς 
(— 1212-Ρ) 
= pi(n—p)! Wj 
nj... Jor” SB, g. 
To get the last line one has to move each of the (n — p) indicesi...k ‘through’ 
(by permutation) all of the p indicesr...s, giving (n — p) factors of (— 1)’. 
Now, fix the indices (7... ἢ) at, say, (1 ...p). (Their names clearly cannot 
matter.) Then in the sum (for fixed (r.. . s)) 
Wi μι. ρω 
the indicesi...k must be chosen from the set (p + 1,..., 7). There will 
therefore be at most (ή — p)! nonzero terms in this sum, and each such term 
will be equal to every other one, just as in (4.23). So we have 
.RY...8 
i...Rr...g 
— 
__ 
ptl...nr...s 
Wi...k1...p~ 
— 
(n 
ϱ)' Wp+1...n1...pW 
. 
Moreover, this will be zero unless (7... s) is a permutation of (1 ...p), for 
otherwise the second w will have repeated indices. In the sum over (7... 8), 
pti...nr...s 
ω 
By. .s> 
there are thus at most p! nonzero terms, and again each of them equals every 
other. So we have 
ωλ ARNT SB — Ρἱ ωδ 11 ΣΤΡ 
ρ. 
Combining all these results gives 
(5). ρ = 
(— 1) 0 
Con at πι...ρ ωδ thle P Bi ° 
But, from (4.24) we see that 
ώρκ1.. πι. ρω 
ο ο 
ΝΕ = 
1, 
and so 
(*S)1...p τσ ΟΤΙ ρ. 
Since the labels 1... p could have stood for any indices, we have proved that

## Page 138

Differential forms: algebra and integral calculus 
128 
+ 
*#B = (-- 1)ΡΦ:ΡΡ, 
(4.27a) 
Similarly, had we started with a qg-vector T, we would have found 
+ 
ET = (- ασ OT, 
(4.27b) 
Notice that if 7 is odd, the factor (— 1? is always + 1. 
As mentioned before, a metric maps p-forms into p-vectors. Combined with 
the dual map this gives a map from p-forms to (ή — p} forms, or q-vectors to 
(n — q}vectors. This map is usually simply called * as well. But some caution 
regarding signs is necessary when the metric is indefinite (when, as in relativity, 
some lengths are positive and some negative). This is discussed in more detail 
in a later section, and an example of the use of this metric dual is given in 
exercise 5.13. 
In the algebra of forms it is often convenient to introduce the completely 
antisymmetric Levi—-Civita symbols 
+ 1lifi...k isan even permutation of 1,2,...,7; 
¢ 
εν. = ek =( —1ifij...k isan odd permutation of 1, 2,..., 2; 
0 otherwise. 
(4.28) 
For instance, the form dx! λ dx? ~ dx? on a three-dimensional manifold has 
components ¢;;, in the coordinate system (x', x”, x°*), but will have com- 
ponents he;;, in other coordinates, where h is some function. Suppose that a 
volume-form ὦ has components 
Wijk = Seize 
(4.29) 
where fis some function. Then its inverse is 
. 
| 
.. 
GF _— πω. 
(4.30) 
4.Ι0 
Tensor densities 
We have taken the point of view that any nonzero n-form on an n- 
dimensional manifold defines a volume element. It sometimes happens that a 
given problem has two or three such n-forms. (An example of this is the flow 
of a perfect fluid, discussed in chapter 5. In the three-dimensional manifold 
of Euclidean space there are three physically defined three-forms: one whose 
integral gives the volume of a region, another the mass, and a third a conserved 
quantity related to the vorticity.) This makes it more convenient on occasion 
to relate all such forms to the coordinate-dependent n-form dx! λ dx? 
A...A dx", whose components are simply €;;_,. If @ is ann-form of interest, 
then the relation (4.29) rewritten as 
Wij...k = W Ei, ke

## Page 139

4.10 Tensor densities 
129 
defines a quantity w which is called a scalar density. Although w is a function 
on the manifold, it is not a true scalar because it depends on the coordinates. 
Under a change of coordinates to xi = fix’), the components of & are multi- 
plied by the Jacobian J of the transformation (equation (4.19)) while ευ. κ is 
by definition unchanged. So w obeys the law 
w = Jw. 
This is the transformation law for a scalar density of weight 1. (The term 
‘weight’ is defined below.) It is possible to extend this to tensor densities. 
Suppose, for instance, that T is a (0) tensor on an n-dimensional manifold which 
is completely antisymmetric in its vector arguments: 
a 
= 
T’ tron: 
al 
n indices 
Then upon contraction with two one-forms & and B, T produces a volume-form 
r(&, B): 
{(ᾱ.β) -- T@,B; ,...,), 
te. = Ty .1048;. 
(Such tensors may arise in physics. For instance, the stress tensor mentioned in 
chapter 2 gives the density of stress when given two one-forms; the total stress 
is the integral of this over the volume, the integral of the contraction of the (2) 
tensor obtained by multiplying the stress tensor by the volume-form.) It is pos- 
sible to write the components of T as 
Τον | =2 Yen. 
which defines the numbers {πο}, which are components of a (@) tensor density. 
(It is conventional to use German letters to denote densities.) The transfor- 
mation law for such a density is 
xii = JAY ΣΑ, 
(4.31) 
where again J is the Jacobian (determinant of Ai). This is the transformation 
law for a (2) tensor density of weight 1. 
The term weight refers to the number of factors of J in the transformation 
law. For instance, a number w which transforms by 
w' = J*w 
is a scalar density of weight two. The generalization to tensor densities and to 
other weights is obvious. (An ordinary tensor is a density of weight zero.) The 
interpretation of densities of weights other than zero or one is more compli- 
cated, but such quantities do on occasion prove useful. In this book we shall 
not deal with densities, preferring to use the n-forms themselves.

## Page 140

Differential forms: algebra and integral calculus 
130 
4.11 
Generalized Kronecker deltas 
The Levi—Civita symbol has many useful and interesting properties, 
some of which we explore in this and the next section. As we saw earlier, one 
often encounters products of es, such as εὖ "δε 
γι. It is possible to develop a 
systematic and convenient method of handling them. 
First we note that, in two dimensions, for any nonzero two-form 63 we have 
wyw = exe” = 5",5',— δ”,δ'. 
(4.32) 
The first equality follows from (4.29) and (4.30). To establish the second it is 
easiest simply to note that both sides are antisymmetric in (kK, ἢ and (i, 7), so it 
suffices to consider the case 
i#/,k #1. There is, up to a sign, only one such 
term, ει εἰ = 1. Clearly the right-hand side of (4.32) also gives one, which 
proves the result. A nearly identical chain of reasoning leads to the general 
result for ή dimensions: 
é;..pern” = 655, ...5", 
— 556", ...87, +... 
= n! 6';6,...8"%y- 
(4.33) 
There is an abbreviated notation for this. We define the p-delta symbol by 
+ 
biel = pl δἱμ.... 
8 y, 
(4.34) 
where the sets (i... 7) and (kK... 1) each contain p indices. Then we have as a 
special case 
+ 
eye = OF. 
(4.35) 
The p-delta symbol can be obtained from the (p + 1)-delta symbol by con- 
traction, conventionally on the first indices. We begin with 
Simi..s = (P+ 1)! 8G md"... 5's. 
The terms can be arranged as: 
= p! 58) tm", ..-5'9) —p! 8 mb) 8", . .. 84] 
—p! 85 tm"; ...8'47 —...—p! 88 pmb", .. δη 
= p! {08 m5", ... δη — 8 md"... δρ] 
— m5", 
2 
8 gy me 
8 *, 
2. 8}, 
which gives 
9 
δι τς = (1 --ϱ) διὰ 
(4.36) 
for the single contraction of a (p + 1)-delta in an n-dimensional space. 
Exercise 4.11 
(a) Justify each of the steps in the derivation of (4.36). 
(b) Obtain the p-delta from the n-delta by n — p contractions:

## Page 141

4.12 Determinants and ει ον 
13] 
Ors kad = (np)! beh 
(4.37) 
n—p p 
As an example of the utility of this algebra, we shall calculate the triple cross- 
product in three-dimensional Euclidean space. In Cartesian coordinates the * 
operator uses €, SO 
(UXV); = ej,U'V®, 
and therefore 
[WxOxV)]; = eg,We"1,UV™ 
epi Η/Υ. 
Using (4.34) and (4.36) we have 
[Wx (Ux V)]; = (867, — 85" )WUVin 
= U,W-V)—V,(W- 
U). 
This derivation is so quick that it should make memorization of the triple cross- 
product formula completely unnecessary! 
4.12 
Determinants ande ;;__x 
Consider a 2 x 2 matrix with elements A”. We shall show that 
det(A) = ει 1431. 
(4.38) 
To show this, write the sum on the right-hand side out explicitly: 
6A 11431 = €,AMA” + 6,447, 
where we have used the fact that €,; = ελ) = 0. Now, we also have that 
E12 = — €21 = 1, so we get 
Allg? 
— 412431 
which is the definition of the determinant of the matrix. The next exercise 
generalizes this to n X n matrixes. 
Exercise 4.12 
(a) Show that the determinant of an n x n matrix with elements A¥ 
@,j=1,...,n)is 
4 
det(A) = ει ,ANA™... A”. 
(4.39) 
(Hint: the determinant of an ή x n matrix is defined in terms of (ή — 1) 
x (n — 1) determinants by the cofactor rule. Use that rule to prove 
(4.39) by induction from the 2 x 2 case.) 
(b) Show that

## Page 142

Differential forms: algebra and integral calculus 
132 
1 
-- 
det(A) = τη] €ab...c€i...kAA™ / AM, 
Exercise 4.13 
If a manifold has a metric, let {ῶ1λ be an orthonormal basis for one- 
forms, and define @ to be the preferred volume-form 
LAG A...A CS”, 
O= @ 
Show that, if {FV is an arbitrary coordinate system, 
+ 
ὢ = lel? dx? Adx2 A... A dx” , 
(4.40) 
where g is the determinant of the matrix of components g;’;" of the 
metric tensor in these coordinates. 
Again it is interesting to look explicitly at the three-dimensional Euclidean case. 
The volume of a parallelepiped formed by the three vectors a, b, and ¢ is the 
determinant of the matrix whose rows are the components of those vectors. 
From (4.39), therefore, 
volume = €;jna'b'c® = a'(e;,b'c*) 
a'(b X@); = @-(6-0), 
another well-known expression for the volume. 
4.13 
Metric volume elements 
In exercise 4.13 we used the metric of a manifold to define a certain 
orthonormal basis {¢3'}, from which we constructed an n-form ὢ (equation 
(4.40)) which we called ‘the preferred volume-form’. Does this form deserve 
the name ‘preferred’: is it unique, or does it depend upon the particular ortho- 
normal basis (which certainly is not unique) used to define it? The answer is 
that it is unique, apart from a sign. To see this, note that the components of 
ὦὤ on the original basis are, by definition, ¢;; ,. If (ῶ] } 
is any other ortho- 
normal basis, then the components of @ on this basis are Je;’;’,_,', where J is 
the Jacobian of the transformation from {@/} to {@/ η. But, because the two 
bases are orthonormal, this Jacobian is + 1 (proved below). Therefore, the 
form @ differs from the ‘preferred’ form defined by {ῶ] } by at most a sign. 
If we adopt a convention for handedness, we can define @ by right-handed 
orthonormal bases, and it is unique. So a metric defines a unique volume-form 
for an oriented manifold. On intuitive grounds, of course, this is not at all 
surprising. 
To prove this result we used the fact that the Jacobian of a transformation 
from one orthonormal basis to another — which is just the detérminant of

## Page 143

4.13 Metric volume elements 
133 
the transformation matrix Ai, — has absolute value one. This is not hard to 
establish. We start from the general transformation law for the metric tensor’s 
components 
ει = Ny 
Ny 8p1, 
which can be written in matrix language as (cf. $2.29) 
(g') = (A)*@) (A). 
The determinant of this transformation law for g;; gives 
det(g’) = det(g) [det(A)]?. 
But in an orthonormal basis, g;; is a matrix which has + 1 on the diagonal and 
zero elsewhere. (Recall that if g;; is an indefinite metric not all diagonal elements 
will have the same sign.) So the determinant of g;; is + 1, and has the same sign 
in all orthonormal bases. Therefore we have for the Jacobian 
det(A) = J = £1. 
For indefinite metrics, the dual operation * can be defined in either of two 
ways, which arise because w--”, the inverse of the volume-form, has two 
‘natural’ definitions which may differ by a sign. The point of view we took 
earlier was that 
i.e. that 
ol" = (Wr nd, 
But if there is a metric one might like to define an n-vector ὢ by raising the 
indices of 63: 
ὤ λε κ = gilgim 
— gkroy 
κ. 
From equations (4.39) and (4.40) it follows that 
Gy te F _— |σ] 1/2 det(g!””) ele 
Now, since (g’”") is the matrix inverse to δη. its determinant is g ‘and we 
have 
απ. 
(ῶ }12:::1 — 
(4.41) 
δ 
whereas we had 
(0123 
—_ 
~ 
I 
—_— 
_ 
; 
(4.42) 
(ῶ)ι. η 
5 
If g is negative, these differ by a sign. It is conventional in relativity, where g is 
negative, to use @’ in the inverse-dual relations. This introduces an extra minus 
sign into equations like (4.27).

## Page 144

Differential forms: differential calculus 
134 
B The differential calculus of forms and its applications 
Where there is an integral calculus there is also a differential calculus, and so we 
shall introduce the exterior derivative, which operates on forms and produces 
forms which are their derivatives. The exact sense in which exterior differ- 
entiation is the inverse of integration is shown in Stokes’ theorem, proved below, 
which is the generalization of the fundamental theorem of calculus, 
b 
|, of = 10)-1@. 
(4.43) 
We will then go on to show the close relationship between differential forms and 
partial differential equations. 
4.14 
The exterior derivative 
We want to define a derivative operator on forms which preserves their 
character as forms and which is inverse to integration, in the sense of (4.43) 
above. Note that if M is a one-dimensional manifold, the operator d which takes 
a zero-form f to a one-form df does indeed satisfy (4.43) above. So what we 
want is to extend d to forms of higher degree. By analogy with the operation of 
d on zero-forms, it must raise the degree of a form. Thus, if @ is a p-form, then da 
is to be a (p + 1)-form. The appropriate way to extend d is as follows (where 
& is a p-form and β, ¥ are q-forms).: 
# 
(i) d@+¥) = (dB) + 7) 
@ 
(ii) ἁ(ᾶλβ) = dOanp+CE1Pan dB 
(iii) ἁ(άα) = 
Property (ii) is just the Leibniz rule apart from the (— 1)”, which comes about 
because one has to bring the operator d ‘through’ the p-form & in order to get at 
β, and this involves ‘exchanging’ it with p one-forms, each exchange contributing 
a factor of — 1. This property guarantees that d will preserve the rule (4.12). (A 
derivative with the property (ii) is called antiderivation.) Property (iii) is at first 
sight surprising, but on examination for the case where & is a function f proves 
sensible: the one-form df has components 0f/dx?. A second derivative would 
have components that were linear combinations of 07f/0x/0x'. But to be a two- 
form this second derivative would have to be antisymmetric in i and /, whereas 
07f/8x'dx! is symmetric (partial derivatives commute). Therefore it is sensible 
that it vanishes. The properties (i)-(iii) plus the definition of d on functions 
uniquely determine d. (This is a theorem whose rather long proof may be found 
in any of the standard references.)

## Page 145

4.15 Notation for derivatives 
155 
Exercise 4.14 
(a) Show that 
d(fdg) = dfa dg. 
(4.44) 
(b) Use (a) to show that if 
1 
~ 
~ 
&@ = —a, jdx'n...ndx’ 
p! 
is the expression for the p-form @in a coordinate basis, then 
v . 19 
Vk 
iyi 
dyed 
άᾶ = 
— >> (q@;..)dx* adx'an... ade’, 
p! ox 
and hence that 
- 
ὃ 
9 
(άᾶ). 1 = (Pt) Ὀχῖε ο." 
(4.45) 
4.15 
Notation for derivatives 
We shall have frequent occasion to use partial derivatives from now on. 
There is a standard and convient notation that for any function f on the mani- 
fold 
Of _ 
πα. Γι. 
(4.46) 
Notice that f might itself be the component of a tensor, in which case the 
comma follows all other indices: 
ον’ 
ak = Vien: 
(4.47) 
Second derivatives are denoted by more indices after the comma, but conven- 
tionally no extra commas are used: 
o7f 
ax® axt = Fir: 
(4.48) 
The indices are to be read left-to-right to find the order in which the derivatives 
are applied (the opposite to the 0/dx” convention). Note carefully that partial 
differentiation is not an allowed tensor operation on components as discussed in 
§2.27. That is, the functions fyi, μὲ do not in general equal the functions 
. 
b’ 
/ 
/ 
NA jA° k γα b’, ec? 
which are obtained by transforming the partial derivatives from another set of 
coordinates. (Recall the discussion in §3.4 of the problems involved in defining

## Page 146

Differential forms: differential calculus 
136 
differentiation of tensors on a manifold.) An exception to this rule is differ- 
entiation of a scalar function, where we have seen that { ; is the component 
of the one-form df. (Here it is worth recalling the distinction between scalar and 
function drawn in §2.28.) An example of our new notation is afforded by the 
Lie bracket: 
[U,V}i = UV' ,-viU' 
;. 
Although each term on the right separately does not transform as a tensor, 
together they do. Similarly, the partial derivatives in (4.45) appear in a com- 
bination which also transforms as a tensor. 
Exercise 4.15 
Show that ντι does not transform as a tensor under a general co- 
ordinate transformation, and then show that [U, V]' does transform 
as a vector. 
With the convention that the derivative index is placed after all the others, 
(4.45) becomes 
(d&); iz = C1P@t 1) os. αμ]. 
(4.49) 
4.16 
Familiar examples of exterior differentiation 
Just as the wedge product gave us the cross-product in three dimen- 
sions, so the exterior derivative (‘wedge-derivative’) gives us the curl. Consider a 
vector ἄ. The exterior derivative of its associated one-form is 
da = da, dx! +a,dx? + αἲ ἀχ3) 
= a, ;dx/ α dx! + a, ;dx? a dx? + a3; dx! a dx?, 
ο. 
Since dx! α dx! = 0 and similarly for indices 2 and 3, this becomes 
da = 
(αι 2 — az 1) dx? A dx! + (a2 3 — a3 2) dx? A dx? 
+ (a3 ι —a, 3) dx} A dx3, 
The curl is clearly involved here. To isolate it as a vector, we take the dual: 
*dz = (αι 2 — a1) *(dx? Adx!)+... 
ὃ 
= G12 
αλ) 
at... 
ὃ 
= 
— 
— Ht... 
(a2 4 
41,2) 53 
*da = Ψχᾶ. 
(4.50) 
~~ 
So the curl operator in three dimensions is *d.

## Page 147

4.17 Integrability conditions 
137 
Not only the curl, but also the divergence comes from exterior differen- 
tiation. In this case the appropriate operator is d*. That is, start with a vector ἄ 
and take its dual: 
* 
0 
0 
0 
(>) 
--- 
1 
+ 
2 
+ 
3 
(a) 
- 
x} 
a 
ax? 
a 
ax 1 
ba’ ει, dx! n dx* +... 
= a'(dx? ndx®)+.... 
Then the exterior derivative of this is 
~ 
d*a = αἱ dx! n dx? κ dx? +. 
= a’ ,dx! a dx? Ade+... 
(ai ϱ) dx! » dx? a de?. 
(4.51) 
(In going from the first line to the second only j = 1 survives in the wedge pro- 
duct.) We have therefore shown that 
+ 
d*a = (V-a)6, 
(4.52) 
where @ = dx! κ dx? a dx? is the Euclidean volume-element in Cartesian co- 
ordinates. We shall generalize this divergence formula to arbitrary manifolds and 
arbitrary p-vectors in 54.23. 
Exercise 4.16 
Use (4.50), (4.52), and property (iii) of $4.14 to show that (in three- 
dimensional Euclidean vector calculus) the divergence of a curl and the 
curl of a gradient both vanish. 
4.17 
Integrability conditions for partial differential equations 
Exterior differentiation, like forms themselves, is closely related to 
familiar concepts from calculus. As an example, consider the system of partial 
differential equations 
of 
of 
κ = 8@,y), 
το = Παιν). 
(4.53) 
Ox 
oy 
By letting (x, y) be coordinates of a manifold, this can be written as 
Γ. i ~ ᾱ. 
where a, = g anda, =h. This equation, in turn, has the coordinate-independent 
form

## Page 148

Differential forms: differential calculus 
138 
df = @, 
(4.54) 
where @ is a one-form with components g and h. Now, if f 
is a solution to this 
equation then we get a valid equation by operating with d upon it: 
d(df) = dz. 
But the left-hand side vanishes by property (iii) of the definition of d, so we 
have that a necessary condition for the solution to exist is that 
ω 4 da 
= 0. 
In component language this is 
a,j) = 9, 
which is really only one equation (a two-form on a two-dimensional manifold): 
ὃ 
ὃ 
og 
ὃ 
κ δν _ 5498 
Oh _ 4 
(4.55) 
Oy 
Ox 
Oy 
Ox 
These are, of course, the integrability conditions for the equations. Thus, the 
exterior calculus gives a geometric derivation of these conditions, and it is 
usually the easiest way to derive them because of the conciseness of its notation. 
The fact that the integrability conditions are sufficient conditions for the exist- 
ence of a solution is assured by Frobenius’ theorem, in the version described 
in §4.26. 
4.18 
Exact forms 
By definition of the exterior derivative d, the statement & = df implies 
d& = 0. It is natural to ask for the converse: if da = O, do we know there exists 
a β such that & = dg? A form & for which d& = 0 is said to be closed; a form & 
for which & = dg is said to be exact. Is a closed form exact? In the next section 
we will prove that the answer is yes in the following sense. Consider a neighbor- 
hood JY of a point P, in which & is everywhere defined and in which da = 0. 
Then there exists a sufficiently small neighborhood of P in which a form 8 is 
everywhere defined and for which & = df. Clearly, B is not unique: ᾖ + d¥ for 
any ¥ (of the right degree) also works. 
We only claim that a closed form is exact locally, because the statement is not 
always true globally. Given an arbitrary region G of a manifold in which @ is 
defined and closed, it may not be possible to find a single 8 defined everywhere 
in D for which & = df. 
We give the following example in R*. In figure 4.7, consider the annulus en- 
closed between the curves @, and 62, and consider Cartesian coordinates x and 
y, whose origin P is inside 62. The one-form 
. xdy —ydx 
— x Hy?

## Page 149

4.18 Exact forms 
139 
is defined everywhere between the curves and has the property d& = 0, as one 
can easily verify. Is there a function f such that & = df? If we introduce the 
usual polar coordinates r and @, then it is easy to see that & = dé, so we appar- 
ently have the answer ‘yes’. But there is a problem: ϐ is not a single-valued con- 
tinuous function everywhere in the region of interest, the region between @, 
and @,. Therefore, although @ is well-defined everywhere in this region, there is 
no function f such that & = df everywhere. The answer is ‘yes’ locally, but ‘no’ 
globally. This problem would go away if we ignored 4, and considered the 
whole interior of @; , since ἄ is not defined at x = y = 0. Similarly, if we con- 
sidered the region shown in figure 4.8, then again the problem goes away: in 
this case @ is defined everywhere inside @, and @ can be chosen single-valued and 
continuous inside @ as well. So in this simple example we have found that, 
whereas locally da = 0 > & = df, the global question (whether fis defined every- 
where) depends on the region being considered. 
It is clear that we are dealing with one aspect of the topology of a region or a 
manifold. The study of those topological properties which determine the rela- 
tion between closed and exact forms is called cohomology theory. After we have 
proved Stokes’ theorem we will have enough mathematical machinery to take at 
least a brief look at cohomology theory in 54.24. 
Fig. 4.7. An annular region of R*. The region does not include its 
boundaries. 
Fig. 4.8. A region of 
R? similar to that in figure 4.7 but whose bound- 
ary is a single connected curve. The discontinuity in ϐ (where ϐ jumps 
from 27 down to 0) on any circle r = const about P can be made to 
take place outside ¢.

## Page 150

Differential forms: differential calculus 
140 
4.19 
Proof of the local exactness of closed forms 
We shall prove the following theorem, known as the Poincaré lemma. 
Let & be a closed p-form (d& = 0) defined everywhere in a region U of M, and 
let U have a 1—1 differentiable map onto the unit open ball of κ”, i.e. the 
interior of the sphere S”"! defined by (x!)? +(x7)? 
+...+(")? = 1. Then 
in U there is (p — 1)-form @ for which & = ἀβ. 
Before proving this let us see what this map is. Clearly it means that U is 
covered by a single topologically Cartesian coordinate system. This is really a 
topological condition on U: the region shown in figure 4.7 does not have such 
a coordinate system while that in figure 4.8 does, as illustrated in figure 4.9. 
Other kinds of regions also have such a map. For instance R” itself can be 
mapped onto its unit open ball by the equations 
2 
; arctan r 
x! > = x! ———., 
(4.56) 
π 
r 
r= (ο) +?) +... 5)”, 
(4.57) 
because these imply 
2 
r->— arctan r. 
(4.58) 
π 
This is a C™ map even at the origin, as one can see by expanding arctan r in its 
Taylor series 
arctanr =r—4rt+ir—t.... 
To prove the theorem we use the coordinates x’ in U and construct the form 
B we seek. Suppose @ is 
Fig. 4.9. 
A map from the region in figure 4.8 onto the unit open ball 
of R* (the interior of the unit circle). Dotted lines map to dotted lines, 
dashed to dashed, and a few typical points are shown. Clearly such a 
map can be made C if the boundary curve ¢isC.

