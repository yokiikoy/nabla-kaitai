<!-- source-pdf: Bernard F. Schutz-Geometrical Methods in Mathematical Physics-Cambridge University Press (1980).pdf | pages 91-120 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 91–120

## Page 91

3.7 Frobenius’ theorem (vector field version) 
§1 
The situation for one-forms at P is just the reverse. Let T*p be the dual of Tp, 
the set of one-forms at P which are functions defined on all of Tp. Similarly, let 
V* p> be the dual of Vp, the one-forms S itself has at P. Any one-form in T*p 
defines one in V*p: this only involves restricting its domain from all of Tp down 
to its subspace Vp. But there is no unique element of 7*p corresponding to a 
given element of Vp, since simply knowing the values of a one-form on Vp does 
not tell us what its value will be on a vector not in Vp. 
In summary, then, a vector defined on a submanifold S is also a vector on M, 
and a one-form on 
M is also a one-form on S. But neither statement is reversible. 
We will discuss one-forms and submanifolds again in chapter 4. Here we shall 
concentrate of vector fields. 
3.7 
Frobenius’ theorem (vector field version) 
In any coordinate patch of S there are coordinates {y*,a=1,...,m} 
and basis vectors {0/dy°} for vector fields on S. All these basis fields naturally 
commute: 
[/9γ5, a/ay?] = ο. 
(3.17) 
Exercise 3.5 
(a) Show that if V and W are linear combinations (not necessarily with con- 
stant coefficients) of m vector fields that all commute with one another, 
then the Lie bracket of V and W is a linear combination of the same m 
fields. 
(b) Prove the same result when the m vector fields have Lie brackets which 
are nonvanishing linear combinations of the m fields. 
From exercise 3.5(a) it follows that any two vector fields on S have a Lie bracket 
which is also tangent to S, since these fields are certainly linear combinations of 
the commuting fields {0/dy"}. The important statement is the converse: if a set 
of m C~ vector fields defined in a region U of M have Lie brackets with one 
another, all of which are linear combinations of the m vector fields, then the 
integral curves of the fields mesh to form a family of submanifolds. Each sub- 
manifold has dimension equal to the dimension of the vector space these fields 
define at any point, which is at most m, but which may be smaller (as in 53.9 
below). Each point of Uis on one and only one such submanifold, provided that 
the dimension of the vector space defined by the fields is the same everywhere in 
U. This family of submanifolds fills U in much the same way as a congruence of 
curves does (§2.12), and it is called a foliation of U. Each submanifold is a leaf 
of the foliation. Two foliations are illustrated in figure 3.6.

## Page 92

Lie derivatives and Lie groups 
82 
This result is called Frobenius’ theorem. The proof is sketched in the next 
section, but it is easy to see the central idea. If the integral curves of the various 
fields are to define a submanifold, they must remain tangent to it: no curve can 
start ‘sticking out’ off it. This tangency is guaranteed if all the Lie brackets are 
themselves tangent, since the Lie brackets are simply the derivatives of the vari- 
ous vector fields along one another. If no vector field has a derivative with a 
component off the hypersurface, then no integral curve can leave the hyper- 
surface. See figure 3.7 for some examples. When we come to the study of differ- 
ential forms, we shall encounter another version of Frobenius’ theorem, which 
will show us that it is the fundamental theorem giving conditions for the exist- 
ence of solutions to partial differential equations (‘integrability conditions’). 
Fig. 3.6. (a) A foliation of R? by parallel planes. Each point of 
R? is on 
one plane of the foliation. Only a few such planes are shown. (b) A 
foliation of R? by concentric spheres 53, The centre is a degenerate 
point of the foliation. 
(4) 
(0) 
Fig. 3.7. In R°, the vector field dx/dA = — sin A, dy/dA = cos A, dz/da 
= 1 spirals in the vertical direction with a spiral radius of 1. (a) The 
spiral field and the x-basis vector field form a family of surfaces, each 
point in R? being on one. One such surface is illustrated as a wavy (but 
not twisted) ribbon. In this view looking slightly down toward the x—y 
plane we sometimes see one side of the ribbon (horizontal striping) and 
sometimes the other (longitudinal striping). (b) Two vector fields which 
do not form a submanifold are the spiral one and the z-basis vector field. 
The plane defined by the two at any point is not tangent to the ‘next’ 
spiral curve above or below it. 
(a) 
(d)

## Page 93

3.8 Proof of Frobenius’ theorem 
8&3 
3.8 
Proof of Frobenius’ theorem 
Suppose in some open region U’ of M we are given m’ vector fields 
which at every point P of U’ spana 
subspace of Tp of dimension m <m’. (The 
set of all these subspaces is called an m-dimensional distribution on Μ. This has 
no relation to the delta-function distributions of §2.18.) At least in some neigh- 
borhood U of any point P in U' we can choose m of the fields as a linearly inde- 
pendent basis for the set, and these fields {(V,.,,a =1,..., m} will (by exercise 
3.5(b)) have the property 
[Vays χω] = 2 
Qabe Vio) 
(3.18) 
in U. So we never really need to consider the case where the fields are not linearly 
independent: such a set reduces locally to a linearly independent set of smaller 
dimension. Let the manifold M have dimension n. 
The theorem is trivial when there is only one vector field V (i.e. m = 1). The 
integral curves clearly exist in U if V(P) #0. Each curve is a one-dimensional 
manifold, a submanifold of M. 
The theorem for m 2 2 will be proved by induction. First we will establish a 
formula we will find useful in the proof. From equation (3.14) it is easy to prove 
that for any function f and vector field V, 
£y(df) = d(£¢/). 
(3.19) 
Moreover, equation (3.15) implies, for any vector field W, 
£Xdf,W) = (Leds, W)+ (df, £7). 
(3.20) 
Combining these two equations and remembering that £~W = [V, W], we find 
the result we shall need: 
(df, [V,W]) = £p(df, W) —(d(£<f), W). 
(3.21) 
Returning now to the main proof, we first note that if the m vector fields all 
actually commute (have zero Lie brackets with one another), then the construc- 
tion of §2.15 shows that they define a coordinate system for the points on their 
integral curves, hence the required family of submanifolds of M. We shall prove 
that the submanifolds exist in the general case (Lie brackets linearly dependent 
on the fields) by constructing m linearly independent linear combinations of the 
original fields which do commute. Thus, suppose we have m linearly independent 
vector fields Viz) whose Lie brackets are linearly dependent on the fields. We 
select any one, say Viny = d/dAgmy. Now the parameter Aqny along the Viny 
congruence is a number defined at every point, so it is a function on the region 
U of M we are looking at. Accordingly, its gradient dm) exists, and we use it as 
follows. We define (m — 1) vector fields X(4) which are linear combinations of all 
the original Y,)s and which satisfy

## Page 94

Lie derivatives and Lie groups 
84 
(ἁλμω. ἆω) = 0, a=1,...,m—1. 
(3.22) 
This determines the set {X,)} up to linear combinations of themselves. Now we 
write (again by exercise 3.5(b)) 
m-1 
[Χω, Χο] . 
» BabcX (c) + Yap Vim); 
(3.23) 
ee 
oe 
_ 
[Vimy X(a) | . » Map Xb) + να Επι): 
(3.24) 
b=1 
where βαρος, Yab> Map, and να are all functions on U. We contract these equations 
with daA,,, and use (3.21), (3.22), and the following simple identity 
ζάλη, Vimy? = Lv gqyh 
my = ἁλαμ/άλρω = 1=> d Lv ρλα) = 0. 
(3.25) 
The left-hand sides of both (3.23) and (3.24) contract to zero and the resulting 
equations imply y,, = Vz, 
0. So, in particular, the Lie brackets of the Χιωδ do 
not involve Von) at all. This was the purpose of imposing (3.22) on their con- 
struction. 
We now invoke the inductive hypothesis, that any set of (m — 1) vector fields 
having Lie brackets linearly dependent on them form an (m — 1)-dimensional 
submanifold. This applies to the set (χω, a=1,...,m-—1}, which is therefore 
assumed to form a family of (m — 1)-dimensional submanifolds filling U. Define 
a set of vector fields (χω. a=1,...,m-—1} which form a coordinate basis for 
one of the submanifolds, say S’, so that these fields commute on S'’. We shall 
define fields Ζω. a=1,...,m—1} off’ by Lie dragging along Vint): 
Ζω = Ya) 
ons’ 
[Viny, Ζω] = 0 
in U along any curve 
V,, passing through S’ 
(3.26) 
What we aim to prove is that the Ζ(ω5 commute among themselves every- 
where, as they do on S’. Then we will have constructed the fully commuting set 
{Vimy, Ziq), 4 = 1,...,m—1}and proved the theorem. But first we must 
establish that each Ζ(ω is still a linear combination of the Vqys. In fact we will 
prove that it is a linear combination of the Χ(ως alone, without ,,). Each field 
Za) is certainly unique, so let us see whether we can satisfy (3.26) with a linear 
combination 
Za) = > Wp Χρ). 
b 
fora=1,...,m-—1. 
Then we must have (all sums running from 1 to m — 1) 
0 = [Vins Z@] = £imyZ@ 
= a 
(£ Fy %ad) Χο) + daa L Mm» Xe]

## Page 95

3.9 An example: the generators of S” 
85 
b 
to achieve which, we have used (3.24) with vy, = 0. Redefining the summation 
indices in the last sum (b > c and c > ϱ) gives 
da, 
— 
_ 
2 Χ(υ + 3 QabMpcX (ο) 
(3 27) 
dr 
be 
m 
o=> ο + Lost χι. 
b 
ο 
Since the Y. (ω» are linearly independent, this requires 
dans 
Drm 
which is a set of ordinary differential equations. The initial conditions (at S’), 
that a, give the appropriate combination of ἆμως to form Yq), determine a 
unique solution, which always exists. Therefore, at every point the Z(a)8 are 
linear combinations of the 
ως. 
The final step is to observe that the Lie dragging preserves the fact that they 
commute: 
[Ζω. Zo) | = 
0, 
α.δξ]1.....πι-- 1. 
(3.29) 
This can be proved by using the Jacobi identity, exercise 2.3, among the three 
fields Vimy, Zig), and Z(y). By construction we now have m fields {Vimy, Ζω. 
a=1,...,m-—1} which all commute and which therefore form a coordinate 
basis for a submanifold of dimension m. Since the original fields {Via} are 
linear combinations of these, we have proved the theorem. 
+) Wacken 
= 0, 
(3.28) 
6 
3.9 
An example: the generators of S? 
Readers familiar with angular momentum in quantum mechanics may 
have found many of the ideas presented so far familiar. Consider the (unnormal- 
ized) $-basis vector of spherical coordinates, sometimes called é: 
ey = 
— ye, + Xey, 
where e, and ἐν are the usual Cartesian basis vectors. In our notation this 
becomes 
ὃ 
ὃ 
ὃ 
πω 
τα 
eT) 
Ox 
oy 
which we shall call /,, the ‘angular momentum operator’ for the z-direction: 
7 
8 
(This differs from the usual definition in quantum mechanics by a factor h/i.) 
One can define ᾖ, and ly in analogous ways, and one finds the commutation 
relations (Lie brackets)

## Page 96

Lie derivatives and Lie groups 
86 
[1,1] = τς, 
[ῖψ. 1ε] . —I,, 
(3.30) 
[2,5 Le] στ —1,. 
Therefore the three vectors determine a submanifold. However, it would appear 
that this submanifold need only have dimension three — i.e. be all of the space — 
because there are three vectors. That it is really two-dimensional, we can see by 
realizing that if we define r = (x? + y? +z)”, then 1,(7) =1,(r) =1,(/) = 0. 
Put another way, 
dr(i,,) = dr(l,) = dr(i,) = 0. 
(3.31) 
From our picture of dr as a set of surfaces of constant r, and our interpretation 
of its contraction with, say, ᾖ, as the number of such surfaces 1, pierces, we see 
that (3.31) means that /,., ly, and 1, are all tangent to the sphere 7 = const. There- 
fore, at any point they are linearly dependent, and they generate a submanifold 
of dimension two: the sphere, of course. 
Exercise 3.6 
Show that exercise 3.3 is valid when W is replaced by any tensor field. 
Exercise 3.7 
Define the operator 
L* = £7, Si. + £7, fi, + £; whi, 
(3.32) 
Show that £;, and L? commute. By symmetry this also implies that L” 
commutes with £7, and fi, Show that if fis a scalar function, then 
1 
of 
1 ο 
Lf=—— 
θ 
+ 
τσ 
3.33 
Lif = sin ϐ 00 (i x) 
sin? 06?’ 
(3.33) 
where ϐ and ¢ are the usual spherical coordinates. That is, L?f is the 
angular part of V7f on the unit sphere. 
3.10 
Invariance 
One of the principal uses of Lie derivatives in physics is to express the 
notion that a tensor field is invariant under some transformation. We say that a 
tensor field T is invariant under a vector field V if 
£oT = 0. 
(3.34) 
If T has physical importance — e.g. it might be the metric tensor, or a scalar field 
describing the potential energy of a particle, or a vector field of force — then 
those special vector fields (if any) under which T is invariant will also be

## Page 97

3.10 Invariance 
87 
important. For example, in the preceding section we discussed the vector fields 
associated with rotations of the sphere. One knows that angular momentum will 
be important in a physical problem only if the problem is invariant under the 
rotations associated with at least one of the vector fields. For instance, if the sys- 
tem is invariant under rotations in some plane, it is said to be axially symmetric 
(or axisymmetric) and the angular momentum associated with the vector 
generating those rotations is conserved. How this comes about will be discussed 
in exercise 5.8. Here we shall look at invariance generally. 
The following theorem is of central importance to the whole theory of invari- 
ance. Suppose we have a set F = {T,, T2,... } of tensor fields whose invariance 
properties are being studied. Then the set of all vector fields V under which all 
fields in F are invariant is a Lie algebra, as defined in §2.14. The proof of this 
theorem has two steps. The first step is supplied by exercise 3.8, which shows 
that the set of fields is a vector space over the real numbers. 
Exercise 3.8 
Show that if a tensor T is invariant under both V and W then it is invari- 
ant under aV + bW, where a and ὃ are constants. 
The second step relies on the result of exercise 3.1(a), which applies as well to all 
tensor fields by (3.13) and (3.15). If V and W are vector fields in the set then for 
any tensor field Τι in F 
LoT; = {ῃΤι = O= (£7. £e]T; = 0Ξ 
fe HT; = 0. 
(9.35) 
Therefore [V, W] is in the set if V and W are. This proves the theorem. We will 
shortly see that Lie algebras are very closely related to Lie groups, and this 
theorem then explains some of the usefulness of Lie groups in physics. In the 
next sections we will study some examples of invariance. 
It is important to understand what sort of vector space this Lie algebra is. 
One usually thinks of a linear combination of vector fields V and W as another 
vector field aV + DW, where a and b are functions on the manifold. The linear 
combinations permitted by exercise 3.8, however, use only constants for a and 
b. The vector space we have constructed has the fields V and W as single 
elements; it is not a fiber bundle of which V and W are cross-sections. It is more 
like a finite-dimensional function space (see §2.3). This point may seem subtle, 
but it is important for understanding the dimension of the vector space. For 
example, the three vector fields 1, /,, and J, of the previous section are linearly 
dependent as vector fields on R®, since they are all tangent to S*. But to express 
one in terms of the other two one must use a linear combination with variable

## Page 98

Lie derivatives and Lie groups 
&8 
coefficients. Therefore the three fields are linearly independent elements of the 
Lie algebra: no linear combination of them with constant coefficients (not all 
zero) equals the zero element of the algebra, which is the zero vector field. We 
therefore say that these vector fields are a basis for a three-dimensional Lie 
algebra. The only other Lie algebra we have encountered so far is the algebra of 
all tangent vector fields to a manifold or submanifold. No finite number of such 
fields can be a basis for linear combinations using constant coefficients, so we 
say that this Lie algebra is infinite-dimensional. 
3.11 
Killing vector fields 
Many manifolds of interest in physics have metrics, and it is therefore 
of considerable interest whenever the metric is invariant with respect to some 
vector field. A Killing vector field is defined to be a vector field V such that 
4 
{Ρο = 0. 
(3.36) 
It can be deduced that the component form of this equation in a coordinate sys- 
tem is (cf. equation (3.14)) 
axl V® + gp; ne 
ve = 0. 
(3.37) 
It is often convenient to use a coordinate system in which the integral curves of 
V are one family of coordinate lines, say for the x! coordinate. Then, from 
exercise 3.6 we find 
ὃ 
(£79) = y* axk ὃν T Sip 
ὃ 
(£70) = axl ou = 0, 
(3.38) 
and so the metric components are independent of the coordinate x’. Conversely, 
if there exists a coordinate system in which the components of the metric are 
independent of a certain coordinate, then the basis vector for that coordinate is 
a Killing vector. This is often a convenient way of identifying Killing vectors. 
As an example, let us find the Killing vector fields of three-dimensional 
Euclidean space. The metric in Cartesian coordinates has components 
which is independent of x, y, and z. Therefore 0/0x, 0/dy, and 9/97 are Killing 
vectors. The same metric in spherical polar coordinates has components 
_~ 9,9 _ 
Srr 
Or ar 
0 
ὃ 
See = ο 
δρ r?, 
(3.40) 
ὃ 6 O 
Soo = arta = sin’ 
s. 
dd ὀφ

## Page 99

3.13 Axial symmetry 
δο 
Therefore 0/0¢ is a Killing vector: J, in fact. Clearly, J,, and 1, will also be Killing 
vectors. These six Killing vectors turn out to be a basis for the Lie algebra of 
Killing vector fields. We shall prove this in chapter 5, part E, where we undertake 
a more thorough study of spaces with high symmetry. 
3.12 
Killing vectors and conserved quantities in particle dynamics 
It is well-known in classical mechanics that if a force is the gradient of a 
potential which is axially symmetric, then the angular momentum of a particle 
about the axis of symmetry is constant on the particle’s trajectory. Similarly, if 
the potential is independent of one of the Cartesian coordinates, say x, then the 
x-component of momentum is conserved. However, it is not often remarked that 
if the potential has some other sort of symmetry (constant, say, on a family of 
similar ellipsoids) then there is not a conserved momentum associated with that 
symmetry. That is, conserved quantities in particle dynamics do not follow 
simply from invariance of the potential under some motion (circular, linear, or 
elliptical in our three examples), but also require that the motion be along a 
Killing vector field of the Euclidean space in which the dynamics takes place. 
Although we do not yet have quite enough mathematical machinery to prove 
this assertion (deferred to exercise 5.8), its reasonableness can be seen from the 
equation of motion. Written in ordinary vector calculus notation, this is 
mV = —V®,ormV' = —V'®. 
(3.41) 
But with our understanding that the vector gradient involves the metric, we 
know that this is really 
τῷ 
Ox? 
Any invariants derived from this equation clearly must involve not only the 
invariance of ® but also of ϱ|. 
mVi = —gi 
(3.42) 
3.13 
Axial symmetry 
To illustrate the natural way in which Lie derivatives enter problems 
with symmetry, we consider the case of axial symmetry. Axial symmetry is 
invariance under rotations about some fixed axis. (It should not be confused 
with cylindrical symmetry, which has the added assumption of invariance under 
translation along the axis of symmetry.) Let the angle about the axis be @. Situ- 
ations Often arise in which a problem has a certain ‘background’ axial symmetry. 
One may be dealing with a particle orbiting in an axially symmetric potential, or 
with small perturbations of an axially symmetric system. In such a case, one 
gets a linear equation for the unknown y, 
Ι{ν) = 0, 
(3.43)

## Page 100

Lie derivatives and Lie groups 
90 
where L is some operator which is independent of the coordinate transformation 
¢ > 
+ const. Solutions to (3.43) are not necessarily axially symmetric: the par- 
ticle is at one angle at one time and another angle a moment later, or the pertur- 
bation has nonaxisymmetric initial values. But scalar solutions do have the nice 
property that, when Fourier-analyzed in ϕ as 
VG.) = 
στ vmbeiyelr?, 
(3.44) 
m=-0 
the functions W,,(x’) (the index j runs over all coordinates but ϕ) satisfy the 
related differential equation 
0 = L, (Wm) = eU"PL(v ne”). 
(3.45) 
The operators L and L,,, are not usually identical because Z can contain deriva- 
tives with respect to ¢, but L,, must not. For example, consider the operator 
1a 
,20 
1 
0.9 
1 
0? 
Par” ὃν sind 260” 36 rin? 
6 96’ 
which is clearly unchanged by the transformation ¢@ > ¢ + const. Then when it 
im® 
Vv? = 
operates on a function f(r, ϐ) ο) ο it gives 
, 
10,0 
1 
oO 
ὃ 
V2 
6 
ΙΥΙΦΥ 
..αἰπφί - 
2. 
--«ἱῃθ-- 
(1G, Dem) 
=e 
ε 
ar ὃν 
γ2πθὸθ 
a0 
2 
τος 6). 
(3.46) 
The operator in curly brackets is V2,, as defined in (3.45). This Fourier decom- 
position of the function fis not usually useful in the case of particle motion, 
where the particle’s position is a delta function in ¢, but it is very helpful for 
continuous systems, like waves on an axially symmetric background. The key 
functions, οἱ". may be called scalar axial harmonics. 
We say that a solution ψ to (3.43) has axial eigenvalue m if 
4 
ἐοιν = imy, 
(3.47) 
where €g = 0/0¢ is the tangent to the circles of symmetry. None of this is diffi- 
cult if 
is a scalar function, but suppose one is dealing with a vector equation, 
such as the one for the vector potential of electromagnetism. It will again be use- 
ful to have axial harmonics here, but they must be vector axial harmonics. We 
proceed to construct these. 
Consider the submanifold ¢ = 0 (really a submanifold with boundary, this 
being on the axis of symmetry). At each point choose a basis {e;} for vectors 
tangent to the submanifold. Supplement this basis by eg so that {6ρ. 61) is a basis 
for all vectors tangent to the manifold at the points of the submanifold. Now 
generate a basis for the entire manifold by Lie dragging this basis along ég all the

## Page 101

3.13 Axial symmetry 
9] 
way around the axis of symmetry, as shown in figure 3.8. The resulting fields all 
satisfy 
£556) = Q, 
(3.48) 
i.e. they are all axially symmetric. Notice that in conventional Cartesian coordin- 
ates the components of e; change on going around the axis. Axial symmetry for 
a vector field does not mean that its Cartesian components are independent of ϕ, 
but rather that its components in a coordinate system that includes ¢ are 
independent of ¢. 
We now have a basis which has axial eigenvalue 0, by equation (3.48). Clearly, 
a basis which has axial eigenvalue m is 
Emi = GO", δω = Ep 1. 
(3.49) 
Any vector field satisfying 
£5 oY = imV 
can be expressed as a linear combination of the vector axial harmonics of eigen- 
value πι given in (3.49), which coefficients which are independent of ϕ. 
Exercise 3.9 
In Euclidean three-space, construct axial vector harmonics for rotations 
about the z-axis by choosing the basis in the plane ¢ = 0 to be {é,, δε}. 
Find the Cartesian components of the three vector harmonics for m = 2. 
In a similar way, find the basis one-form axial harmonics for m = 2, 
beginning with {dx, dz} in the plane ¢ = 0. If fis a scalar function of 
axial eigenvalue 2, show that the gradient, d f, is a one-form of axial 
eigenvalue 2. Show that ες + ie, has axial eigenvalue + 1. 
Although we have not yet exploited it, there is clearly a close relationship 
here with group theory. The existence of axial symmetry means that the 
Fig. 3.8. View down the axis of symmetry of a basis (δρ, δη) formed by 
Lie dragging along ég.

## Page 102

Lie derivatives and Lie groups 
92 
‘background’ physical situation is invariant under Lie draggings along 0/d¢. 
These draggings form a Lie group, as described in §3.1. The group involved, 
SO(2), is particularly simple. The more important example of the rotation group 
(whose associated symmetry is called spherical symmetry) is more complicated 
because the various Lie derivatives along ᾖ.. ly, and 1, do not commute. We can 
deal with this problem only by studying Lie groups themselves systematically, 
and that will occupy the rest of this chapter. 
3.14 
Abstract Lie groups 
We have touched on Lie groups or Lie algebras several times. Now we 
shall study them more systematically. The main reason they are interesting in 
physics is, as we have seen, that they express the invariance properties of 
important tensors. We will explore that aspect in later sections. Here our inten- 
tion is to study the group manifold itself. This is an important distinction which 
must not be blurred: the group manifold is quite separate from whatever mani- 
fold contains the tensor whose invariance properties the group expresses. The 
manifold of all rotations (SO(3)) is different from the manifold whose coordin- 
ate systems are rotated (Ε 2). 
Let us assume we have a finite-dimensional Lie group, i.e. a 
C™ manifold G 
of dimension n, which has the following C™ maps (diffeomorphisms): any 
element g of G maps h ΙΓ» gh (left translation by g) or h +> hg (right translation 
by g). We do not assume the group is Abelian (i.e. hg # gh in general), and we 
shall denote the identity element by e. Any neighborhood of e is mapped by left 
translation along a particular g onto a neighborhood of g, as shown in figure 3.9. 
Because the map carries curves into curves it maps tangent vectors at e (elements 
of Τε) to those at g. This is a map called Lz: Τε > Tg, which is also illustrated in 
figure 3.9. (The concept is the same as for the Lie dragging map, §3.3.) A vector 
Fig. 3.9. The left translation along g maps a neighborhood of e onto 
one of g. There is a natural map of a vector at e to one at g.

## Page 103

3.14 Abstract Lie groups 
93 
field V on G is said to be left-invariant if L, maps V at e to V at g (L,: Ve) 
+> V(g)) for all g. By the group composition law it follows that L, maps V(h) 
+> V(gh) for any hin G, so that what we have is a natural definition of a ‘con- 
stant’ vector field on G. It is also clear that each vector in T, defines a unique 
left-invariant vector field, so that the left-invariant vector fields form an n- 
dimensional vector space. (As in 53.10, linear combinations of these fields use 
constants, not functions on G.) In fact it is easy to see (figure 3.10) that if V and 
W are any two left-invariant vector fields, then L, maps [V, W] ateto [V, W] at 
g: the field [V, W] is also left-invariant. (The reader who is not convinced by the 
diagram is invited to use coordinates on G to prove the result.) This is important, 
because it means that the left-invariant vector fields form a Lie algebra. This is 
called the Lie algebra of G, denoted by &(G). (Some authors use g.) This Lie 
algebra is completely characterized by its structure constants ci,, defined as 
follows. Let {Vjy,i=1,...,n}bea 
basis for the Lie algebra, a linearly inde- 
pendent set of left-invariant vector fields. (If they are linearly independent at 
one point, say e, the map shows they are independent everywhere.) Then we 
can always write 
[Vinys Van) = chiViiy 
(3.50) 
(summation convention assumed). If all the structure constants vanish, the Lie 
algebra is said to be Abelian. We shall see that it implies G is also Abelian. 
Naturally the basis {Vy,)}is not unique, and under a change of basis the numbers 
cj.) transform as components of a (4) tensor. Every Lie group and algebra has a 
unique “structure tensor’ C. There is a limited converse to this, that a given set of 
structure constants ‘almost’ determines the Lie group whose Lie algebra they 
embody. This will be discussed in §3.16 below. 
Fig. 3.10. The mapping of figure 2.21 for left-invariant vector fields. 
Because they are left-invariant, translations by parameter distance ε 
near 6 map into the same ones near g, and so the ‘gap’ near e that repre- 
sents their Lie bracket is mapped to that near g, which is the bracket of 
the translated fields.

## Page 104

Lie derivatives and Lie groups 
94 
Consider the integral curve of a left-invariant vector field V which passes 
through e. It has a unique tangent vector V, at e and a unique parameter ¢ for 
which e corresponds to t = 0. As in 92.13, the points on the curve may be 
located by exponentiation of V, exp (tV). This just involves the diffeomorphism 
of G onto itself generated by V, as discussed in §3.1. Unlike an arbitrary vector 
field, V is determined completely by V,, so we can denote the points of G on 
this curve by 
εν, (ϐ) = exp(tV)|,. 
(3.51) 
Because exponentiation has, by definition, the property 
exp (t,V) exp (t;V)le = exp [(t1 + 42) V le; 
the points on these integral curves form a group: 
gv, 
(ti +t) = exp [(ti + t,V]le = exp(t,V) exp (ει Γιο 
= gv7,(t2)8v,(t1). 
(3.52) 
This is called a one-parameter subgroup of G. It is obviously always Abelian, 
gv(ti + t2)=8y,(t2 + 11), simply because the group operation corresponds to 
addition of parameter values. To each vector in Τε there corresponds a unique 
subgroup. Moreover, since every one-parameter subgroup must be a C™-curve in 
G which passes through e (a subgroup must always contain the identity element) 
there is a one-to-one correspondence between the one-parameter subgroups of G 
and the elements of the Lie algebra of G. 
Exercise 3.10 
Define right-invariant vector fields. Show that they form a Lie algebra. 
Show that their integral curves through e coincide with those of the left- 
invariant fields. Show that their integral curves through other elements 
do not coincide with those of the left-invariant fields in general unless 
the group is Abelian. 
Exercise 3.11 
Show any basis {V;(e),i=1,...,n}for Τε defines a linearly indepen- 
dent set of left-invariant vector fields, which we shall call {V;}. 
Consider the tangent bundle of the group, 7G. In some neighborhood U 
of e adopt coordinates for it as follows. Let X be a vector at point g of 
U, with X = Y;a;V;(g). The fiber at g is just R”, so take the coordinates 
of X to be {a;}. Let the coordinates of TG over U then be {{coordinates 
of g}, {a;}}. Show that this prescription extends to all of TG in such a 
way as to prove that Τζ has a 1-1 map onto G x R", i.e. that the 
tangent bundle of a Lie group is trivial. 
oN 
99 — 
(b eo

## Page 105

3.15 Examples of Lie groups 
95 
3.15 
Examples of Lie groups 
(i) The simplest example is R” , which is a manifold and a group under 
vector addition. This is an Abelian group. The one-paramenter subgroups are the 
‘rays’ (straight lines through the origin). The left-invariant vector fields are 
parallel to the rays, so they all commute. The Lie algebra is thus the vector space 
T, equipped with the trivial Abelian bracket: [V, W] = 0 for all Vand W in T,. 
(ii) For physics, one of the most important Lie groups is the group of all 
n Xn real matrices with nonvanishing determinant, called GL(n, R) or the 
General Linear group in” Real dimensions, which is a Lie group for the follow- 
ing reasons. First, it is a group with the operation of matrix multiplication, the 
unit matrix being the identity element. (The restriction to nonvanishing deter- 
minant is necessary to ensure the existence of an inverse element for any matrix.) 
Second, it is a Lie group because it is a manifold. Any matrix A in GL(n, R) with 
entries {a' ,, i,j =1,...,n}has a neighborhood of radius ε defined as those 
matrices B for which |b'; —a',| <¢ for all i andj, and ε can be chosen small 
enough so that every B has nonvanishing determinant. The numbers 
x', = b'; —a'; are coordinates for this neighborhood, and as there are n” of them, 
all independent, the dimension of GL(n, R) is ή”. In fact it is a submanifold of 
R”’, Since κ. like any R™, is identical with the tangent space of any of its 
points, the tangent space of the identity e of GL(n, R) is Α΄ and any tangent 
vector can be represented as a matrix. For instance, the curve in GL(n, R) com- 
prising the matrices diag (1 + exp (A), 1,1,..., 1), which has parameter A, has 
tangent diag (1,0,0,...,0) at A =0. This matrix has zero determinant, illus- 
trating the fact that any matrix is in T, and therefore any matrix generates a 
one-parameter subgroup, a left-invariant vector field,’ and an element of the Lie 
algebra. 
The one-parameter subgroup generated by any matrix A is the integral curve 
through e of the left-invariant vector field whose tangent at e is A. If we denote 
these matrices by g(t) with dg,(t)/dtl) =A (which simply means d(g,)';/dtlo 
= a', for all i, 7), then by (3.52) we have 
ga(t + At) = ga(tga(Ad) 
=> dg,(t)/dt = ga(t)A 
(3.53) 
=> g,(t) = exp (14) 
(3.54) 
] 
1 
= L+tA+ VA + PAT +... 
(3.55) 
Equation (3.55) is the definition of the exponential of a matrix, and with (3.54) 
gives concreteness of the formal expression (3.51). So the one-parameter 
υ The reader should bear in mind that a vector tangent to G is in fact a matrix, not 
to be confused with a ‘column vector’, which plays no role here.

## Page 106

Lie derivatives and Lie groups 
96 
subgroups of GL(n, R) are the exponentials of arbitrary n x n matrices. The 
matrix A is often called by physicists the infinitesimal generator of the subgroup 
g(t). Exercise 3.12 explores properties of exp (fA). 
Exercise 3.12 
(a) Show that (3.55) satisfies (3.53). 
(b) Show that (3.55) implies 
exp (B''AB) = B exp (A)B. 
(3.56) 
(c) It can be shown (see Hirsch & Smale, 1974) that for any real matrix A, 
a real matrix B can be chosen so that B™'AB has the following canonical 
form (called block-diagonal form, since the nonzero elements fall in 
square blocks along the main diagonal) 
P, 
0ο 
ο 
Ρ 148 Ξ{ 
0 
2 
0 
(3.57) 
ϱ 
O 
P3 
where each P; is a square matrix having one of the forms 
(i) P; isa 1 x1 matrix 
(1), 
(3.58a) 
or (ii) P; is a 2 x 2 nondiagonal matrix given by 
| 
a4 
| 
(3.580) 
SG 
or (iii) P; is an n; x nj nondiagonal matrix (η! = 2) given by 
uy 
1 
0 
ο 
0 
ο 
tl. 
0 
0 
ο 
ο 
wm. 
1 
ο 
(3.556) 
ο. 
ο 
ο 
. wl 
0 
ο 
ο 
| 
0 
µι 
Moreover, the numbers Aj, uj, and 7; + is; are the eigenvalues of A. 
Show from this and (3.55) that exp (18148) similarly has block- 
diagonal form with the corresponding blocks: 
(i) (3), 
(3.59a) 
il 
cos fs; 
sin ts; 
uD efi 
7 
7), 
(3.59b) 
— SIN tS; 
σος tS;

## Page 107

3.15 Examples of Lie groups 
97 
(iii) 
i, 1 
1 
t 
21 f 
31 t 
1, 
ο 
1 
t 
af 
ef Hj 
ο 
O 
1 
t 
(3.59c) 
0 
0 
1 
It follows from (a) that a matrix B which puts A into canonical form 
also puts exp (tA) into canonical form in cases (i) and (ii), but that the 
transformation to canonical form in (iii) is a function of 1. 
Note that not every element of GL(n, R) is a member of a one-parameter sub- 
group. One reason is that such a subgroup is a continuous curve in GL(n, R), on 
which the determinant must change continuously. Since the determinant is 1 at 
e and cannot be zero, there is no continuous curve linking e to a matrix with 
negative determinant. (The reader can easily see that (3.59) represents only 
matrices with positive determinants.) This is an example of a disconnected group 
and illustrates the interesting global properties Lie groups can have: one does 
not usually learn everything about a Lie group just by studying its one-parameter 
subgroups or even its Lie algebra. Those elements which can be joined to e by a 
continuous path (not necessarily a one-parameter subgroup) are called the 
component of the identity of the group. 
Exercise 3.13 
Show that the matrix 
—] 
1 
0 
—] 
is in the component of the identity of GL(2, R), but is not in any one- 
parameter subgroup. (Hint: construct a continuous path joining it to 
e=(9 1).) 
What is the Lie algebra of GL(n, R)? Given a tangent vector A, at e and its 
one-parameter subgroup g 4, (t), the left-translation fg Ae (8) of this curve by any 
matrix f of GL(n, R) produces a curve of the congruence of the left-invariant 
vector field corresponding to Ας, as in figure 3.11. This is how A, generates its 
left-invariant field, which we call simply A. If in fact fis on the curve 3,(¢)

## Page 108

Lie derivatives and Lie groups 
98 
through e generated by any matrix B, in T, then the Lie bracket of the two 
vector fields at e, [A, Β]|.. is by (2.12) just 
lim 2 
lea, (9)Ε5, (2) — 28,22, (01, 
which is easily evaluated using (3.55): 
[A, Bll. = A.B. —B,Ae.- 
(3.60) 
That is, the Lie bracket of any two left-invariant vector fields at e in GL(n, R) is 
just the ordinary matrix commutator of the two matrices which generate the 
fields. The left-invariant vector field generated by this commutator is the 
element of the Lie algebra &(GZ(n, R)) which is the bracket of the original fields. 
(iii) We have seen that the rotation group is a Lie group (§2.3(vi)). We will 
study it closely below, but here we examine it as a subgroup of GL(n, R). In 
§2.29 we saw that the matrices A for which 41 = A? are elements of the 
Euclidean symmetry group O(n). (The symbol O(n) means the Orthogonal group 
in n dimensions.) Since the determinant of any matrix obeys the rules ($1.6) 
det (4) = 1/det(A™'), 
det (A) = det (4%), 
(3.61) 
matrices in O(n) have determinant +1. Those with determinant +1 form a sub- 
group called SO(n) — the Special Orthogonal group — and we shall now demon- 
strate that this is the group of rotations. (The matrices in O(n) which have deter- 
minant —1 are not a subgroup since they do not include the identity matrix. 
Like GL(n, R), O(n) is disconnected.) 
Exercise 3.14 
(a) Show that if A is in O(n) its eigenvalues equal those of 4 1. (Use the 
fact that det B = det B’ for any B.) The reader not experienced with 
eigenvalues should look up their definition in 51.6. 
Fig. 3.11. Left-translation of £a,(t) by f.

## Page 109

3.15 Examples of Lie groups 
99 
(b) Show that for any nonsingular matrix A the eigenvalues of A are the 
reciprocals of those of 4-1. (Use the fact that det (AB) = det A det B.) 
Conclude that there are two types of eigenvalues (A,,...,A,,) of A 
in O(n): either (i) A; = +1 or (ii) AJA, = 1 for 7 #K. Show that case (ii) 
implies the eigenvalues come in pairs (e’”, e??) for real ϐ. 
(c) It can also be shown that the canonical form of a matrix A in O(n) can 
be achieved by a transformation B'AB, where B is a matrix in SO(n). 
Use this to conclude that a matrix in O() has canonical form consisting 
of blocks 
(i) (1), 
(3.624) 
or (ii) (-- 1), 
(3.62b) 
cos 
sin ϐ 
or (iii) | 
(3.62c) 
—sin@ 
cosé 
(d) Show that the Lie algebra of O(n) consists of all antisymmetric matrices. 
Show from this that O(n) has dimension $n(n — 1). 
Now, a matrix A in GL(n, R) may be regarded as an invertible (1) tensor on 
ΚΙ , 
mapping a column vector V of R” to AV, obtained by matrix multiplication. 
The transformation 8 148 is nothing more than the transformation of the com- 
ponents of this tensor (§2.26) when the basis {é;,..., κ} is transformed to 
{Bé,,...,B 'é,}. We can therefore take the view that any matrix of SO(n) is 
equivalent to successive rotations in independent two-dimensional planes, since 
the canonical form (3.62c) obviously does that, while the form (3.62b) must 
occur an even number of times (for the determinant to be positive), which direc- 
tions can be paired to give (3.62c) with 9 = 7. Thus SO(”) is indeed the rotation 
group. (Note that if n is odd, every matrix in SO(n) fixes at least one direction.) 
The remaining matrices of O(m) can be interpreted as inversions, transformations 
which change the ‘handedness’ of any set of n linearly independent vectors. This 
is shown in the next exercise. (‘Handedness’ of a basis will be discussed in detail 
in chapter 4.) 
Exercise 3.15 
Show that the canonical form of an element of O(n) not in SO(n) is the 
product of a matrix diag (1,...,1,—1,1,..., 1) (having only one 
— | onits diagonal) with the canonical form of a matrix in SO(n). 
From this prove that it is an inversion.

## Page 110

Lie derivatives and Lie groups 
100 
Exercise 3.16 
Prove that any matrix in SO(n) is in a one-parameter subgroup. Prove 
that any matrix in SO(3) is equivalent to a single rotation through a 
finite angle ϐ about some axis. 
Before leaving the rotation group we need to study its Lie algebra, at least for 
SO(3). The vector space 7, is that of all antisymmetric matrices, which has 
dimension three (see exercise 3.14(d)). A basis consists of the matrices 
ο 
ο 
ο 
0 
ο 
1 
ιξ- 
40 
0 
—-1] 
. 
L,= 
0 
ο 
OF 
, 
ο 
1 
0 
-ἱ 
0 
ο 
(3.63) 
ο 
-ι 
ο 
L3 = 
1 
0 
0 
0ο 
ο 
0 
Exercise 3.17 
Show that this Lie algebra basis has the brackets 
[L1,L2) = £3, 
1, 1] = Li, 
να, νι] = 11. 
(3.64) 
We will come back to this algebra shortly. 
(iv) Another matrix group of interest in physics is SU(”), which stands for 
Special Unitary group in n dimensions. This is a subgroup of GL(n, C), the group 
of all complex ή x n matrices of nonvanishing determinant (the General Linear 
group in nm Complex dimensions). Since each entry may be complex and each 
complex number is defined by two real ones, GL(n, C) has 2n? (real) dimensions. 
Its subgroup U(n) is the Unitary group, each element U obeying U' = 03, 
where * denotes the complex-conjugate transpose (Hermitian conjugate). By 
analogy with O(n), its Lie algebra consists of all n x n anti-Hermitian matrices. 
(A matrix A is anti-Hermitian if A* = — 
A.) This has η” real dimensions, since 
such a matrix can have $n(n — 1) arbitrary complex off-diagonal elements (given 
by (η — 1) real numbers) and n arbitrary pure-imaginary diagonal elements 
(contributing ή real dimensions, making n? in all). Its subgroup SU(n) is the set 
of all matrices in 01) with unit determinant. Since the determinant of any 
element of U(n) is real, this is one extra condition, so SU(n) has dimension 
n* — |, Its Lie algebra is the set of all anti-Hermitian matrices with zero trace. 
(The trace of A is the sum a';: see §1.6.)

## Page 111

(a) 
(b) 
(c) 
3.16 
3.16 Lie algebras and their groups 
101 
Exercise 3.18 
Show that the Lie algebra of SU(n) is that of all anti-Hermitian traceless 
matrices. You may use the fact that any element of U(n) has canonical 
form diag (οἱ δι, e!?2,.. . , etn) where the numbers {@,fj=1,...,n} 
are real. 
Exercise 3.19 
Show that the following matrices are a basis for T, of SU(2): 
yr ai(0 i) ,_4fo 
-ἡ 1 
ο 
6 65) 
στ ο 
OF 
ο 
οι 
ο) 
21ο 
i! 
Show that this is a three-dimensional real vector space: even though the 
matrices may contain imaginary numbers, only linear combinations of 
them with real coefficients remain in the vector space Τε of SU(2). 
Show that this Lie algebra basis has the brackets 
[J1,J2] = J3, 2. 19] -- Ji, [J3,J1] = 02. 
(3.66) 
These are formally identical to (3.64), and we shall see in the next 
section that this implies an intimate relation between SU(2) and SO(3). 
Exercise 3.20 
Let tr (A) =a’, denote the trace of any matrix A. Prove that tr (8148) 
= tr (A). 
Use this and (i) the fact that the determinants of matrices obey the rule 
det (AB) = det (A) det (B), (ii) the result (3.56), and (iii) the canonical 
forms (3.55-59) to prove that for any matrix A 
det (exp (A)) = exp (tr (A)). 
(3.67) 
Use this to give an easier proof of exercise 3.18. 
Lie algebras and their groups 
Every Lie group G has its Lie algebra (G). Since every element g of G is 
the image of e under the left-translation g generates, and since very vector in T, 
corresponds to a unique vector field in the Lie algebra, it follows that every 
point g of G is on one curve of each of the left-invariant congruences. Is it poss- 
ible, then, to construct the group G entirely from a knowledge of its Lie algebra? 
The answer is a partial yes, but to phrase it we must first give a better definition 
of a Lie algebra than we have so far been working with. 
A Lie algebra is a real vector space V upon which is defined a bilinear multi- 
plication rule called [ , ] which produces from any two vectors A and B 
another vector [A, B] satisfying:

## Page 112

Lie derivatives and Lie groups 
102 
(i) [4,8] = —[B, 4], 
(3.68) 
(ii) [A, [B, C]] + [B, [C, A]] + [C, [A, Β]] = ο. 
(3.69) 
The crucial difference between this definition and the one in §2.14 is that the 
Lie bracket is defined formaily, i.e. by its properties (i) and (ii), so that any rule 
for combining vectors in this manner is acceptable. The commutator of vector 
fields provides one such rule, and this was the only one used until now. But 
clearly another example is the vector space R® with the usual cross-product: 
ία, δ] 
=axb. 
(3.70) 
Exercise 3.21 
(a) Verify that (3.70) satisfies the Jacobi identity (3.69). 
(b) Show that the basis 6! = (1, 0, 0). e, = (0, 1, 0), e3 = (0. 0, 1) has the 
brackets 
[ει, 61] 
9. [1, 
63] = ἐι, [€3,é1] = 61. 
(3.71) 
Compare these to (3.64) and (3.66). 
We can now state but not prove a theorem which is of fundamental import- 
ance to physics, that behind every Lie algebra there is a group. Precisely, every 
Lie algebra is the Lie algebra of one and only one simply-connected Lie group. 
(A manifold is simply connected if every closed curve can be smoothly shrunk to 
a point. See Spivak (1970) or Warner (1971) for discussions and partial proofs of 
this theorem.) Moreover, any other Lie group with the same Lie algebra but not 
simply connected is covered by the simply-connected one. (A connected mani- 
fold M covers another N if there is a map 7 of M onto N such that the inverse 
image of some neighborhood V of any point P of N is a disjoint union of open 
neighborhoods of the points in 77'(P) in M. An example is given in figure 3.12.) 
The covering must be a homomorphism of the two groups. (See 81.4 for a defi- 
nition of a homomorphism.) 
The groups SO(3) and SU(2) illustrate this theorem nicely. First we shall 
show that SU(2) is simply connected. We do this by considering the set H of 
matrices of the form 
a 
b 
[*; | 
(3.72) 
for arbitrary complex a and b, bars denoting complex conjugation. 
Exercise 3.22 
(a) Show that H — {(@ 8)}, the subset of Η with non-zero determinant, is a 
group under multiplication, hence a Lie subgroup of GZ(2, C).

## Page 113

3.16 Lie algebras and their groups 
103 
(b) Show that Η is a real vector space (using matrix addition), has dimen- 
sion 4, and has a basis consisting of J;, /,, and J3 of exercise 3.19, plus 
the matrix J 
= (4 9). 
(ο) Let 4 be any matrix in H: 
A = 2a,J1 + 20,72 + 2444 + aal, 
with {a,} real. Show that A is in SU(2) if and only if 
at +02 +02 +02 = 1. 
(3.73) 
(d) Show from this that the group SU(2) has a 1-1 mapping onto the three- 
sphere S*, which is a simply connected manifold. (We say that S* and 
SU(2) are diffeomorphic.) 
We must next find a mapping 7: 
SU(2) > SO(3) which is a multiple covering. 
We can construct it easily by exponentiating the elements of the Lie algebra. In 
SU(2) the element J, has exponential 
C0 sae 3 
“GI. a) 
exp (6011) 
cos(t/2) 
isin (t/2) 
| 
(3.74) 
isin(t/2) 
cos (t/2) 
The element LZ, of SO(3) has the exponential 
1 
O 
QO 
0 
ο 
0 
exp(sL;) = 
[0 
1 
οἱ 
του 
-1 
0 
ο 
1 
ο 
ι 
ο 
| 
0 
0 
0 
| 
0 
0 
0 
+—sto0 
-ι 
ο 
+— 5} 
0 
Ι 1 
2! 
3! 
0 
0 
—] 
ο 
-1 
QO 
1 
0 
0 
= 
O 
ος 
-—sins] 
. 
(3.75) 
O 
sins 
 coss 
If we simply establish the natural correspondence suggested by the algebra, 
1 
0 
0 
QO 
cost 
—sinf] 
, 
st 
isin4t 
π: SU(2)>SO(3), 7: oad psi | 
1σίπΣί 
οοςΣί 
0 
sint 
cost 
(3.76)

## Page 114

Lie derivatives and Lie groups 
104 
then it is clear that this is a homomorphism of the two one-parameter subgroups, 
and it is also clear that the two elements { and t + 27 of SU(2) have the same 
image in SO(3). Moreover, { + 4nz for any integer n is the same point of SU(2) 
as t, so we have proved that exp (t/,) is a double covering of exp (sL,). We can 
generalize this to the whole group: the map 
tr exp (t,J, + thJ, + t3J3) 
exp (¢,L, + t,L, + t3L3) 
(3.77) 
is a double covering of SO(3) by SU(2). 
Since we know that SU(2) has the global topology of the three-sphere, this 
double covering enables us to discover the topology of SO(3). The one-parameter 
subgroup exp (tJ,) of SU(2) begins at e with t = 0 and returns to e at t = ἀπ. In 
figure 3.13 this is shown as a great circle around ιδ”. (But bear in mind that we 
have not put a metric on SU(2). Only the global topology is relevant, not the 
actual distance relations.) The points labelled { and { + 27 are diametrically 
opposite one another. In order to make them the same point of SO(3), we simply 
Fig. 3.12. The unit circle S' is covered by the real line R! an infinite 
number of times by the map 7: R' > S' which takes x to the point on 
S' whose coordinates in the plane R* are m(x) = (cos x, sin x). The set 
na 
‘(V) is the union of all the open intervals shown on R. 
s} 
by 
R} 
-4π -2π 
0 
2xn 
4x 
ὄπ 
Fig. 3.13. A two-dimensional slice of S$? containing the one-parameter 
subgroup exp (t/,) of SU(2). The group SO(3) is the top half of the 
sphere, with points on opposite ends of diameters identified with each 
other.

## Page 115

3.17 Realizations and representations 
105 
identify SO(3) as the top half οἱ’, with points on opposite ends of a diameter 
through the equator (e.g. t = 7 and t = 3π) identified. This half of S° with these 
identifications is no longer simply connected. A curve such as @ can be shrunk 
smoothly to a point, but the curve of the subgroup exp (tZ,) cannot be, since 
the two ends of the diameter of the equator cannot be brought together: they 
are always diametrically opposite one another. This construction also makes 
clear the fact that SO(3) and SU(2) are identical in some neighborhood of e. It is 
for this reason that their Lie algebras are the same. This happens for any two 
groups with the same Lie algebras. 
To what group does the Lie algebra of equation (3.70) correspond? This is 
entirely a matter of interpretation. As an abstract algebra it corresponds to both 
groups. As a relation among vectors in R® it is most common to associate it with 
SO(3) by saying that to the subgroup exp (01.1) (rotation by an angle 6 about 
the x-axis) there corresponds the ‘curve’ in R® , exp (02,) (a vector along the 
x-axis of length 0). This association of a rotation with a vector is very familiar to 
physicists, even more so in its time-differentiated version associating a rate of 
rotation with an angular velocity vector. This convenient identification is an 
accident of three dimensions: the group SO(4) has dimension 6 while the vector 
space R* in which it acts has dimension 4, so no such identification is possible. 
But to return to R*, we can equally well identify κ with SU(2) in a similar 
fashion. In §3.18 we will see that this permits us to associate the spin of a par- 
ticle with a vector in R* even though the spin is not an element of T,, for any P 
in R?. 
Before leaving Lie algebras, we must remark that we can now show that an 
Abelian Lie algebra is the Lie algebra of an Abelian group. An n-dimensional 
Abelian algebra is simply a vector space, and it is the algebra of the Lie group 
R" , 
as discussed in §3.15. Since R” is simply connected, any other Lie group 
having this algebra must be covered by R” and must be identical to it in a neigh- 
borhood of the origin e. Since R” is Abelian (V + W = W + V), so is any other 
Lie group with an Abelian Lie algebra. 
3.17 
Realizations and representations 
It is usually best to regard any group as an abstract group, defined 
entirely by the group operation and, for Lie groups, by the manifold structure. 
Thus, 
SO(3) as an abstract group is simply a certain three-dimensional manifold 
with a rule associating a product point gh with any two points g and h, the rule 
obeying the usual group axioms. To a physicist this abstract structure is not the 
aspect of group theory that is of most interest. More important is what the 
group acts upon and how it affects it. Again, SO(3) is important because we 
associate with each point of it a rotation of our three-dimensional space. Such an

## Page 116

Lie derivatives and Lie groups 
106 
association is called a realization. A realization of a group G is an association 
(map) between any element g of G and a transformation Τ(6) of some space M 
in such a way that the group properties are preserved: (i) T(e) = J, the identity 
transformation (no change of M);(ii) T(g™*) = [T(g)]" ; Gili) T(g) ο T(h) = T(gh). 
The realization is faithful if the association is 1-1: T(g) # T(h) if g #h. If 
Misa 
vector space and every 7(g) is a linear transformation (a (1) tensor on that vector 
space) then the realization is called a representation. A few examples may help 
to make these ideas clear. 
(i) Consider the effect of a rotation on the unit sphere S” given by the 
equation x” + y? +z? = 1 in ΚΣ. Suppose we rotate by an angle 6 about the 
x-axis. This consists of mapping any point on the sphere whose coordinates are 
(x,y,z) to one whose coordinates are (x’, y’, z') as follows 
/ 
x =X, 
y' = ycosé —zsiné, 
(3.78) 
z = ysind +zcos@, 
which is still on the sphere since (x’)* +(y')* + (z')? = 1. This transformation 
is associated with the group element exp (6L,) of SO(3), in the notation of 
(3.63). To any element of the group there corresponds some transformation of 
S* into itself. Since S? is a manifold but not a vector space, this is a realization 
of SO(3). On the other hand, the same transformation (3.78) can be regarded as 
a map of R® into itself, not just of S? into itself. Since R? is a vector space, this 
is a representation of SO(3) in terms of matrices which transform vectors of R° 
into other vectors. These matrices are nothing more than the matrices we used to 
define the group SO(3) in the first place. This illustrates a subtle but useful point 
of view. It is typical for a group to be defined in the first place by a (faithful) 
realization or representation, because this enables one to study all its properties 
concretely. Afterwards, however, it is more useful to regard the group as abstract 
because there may be other useful representations or realizations that one had 
not been aware of at first. We will illustrate these for the rotation group separ- 
ately in the next section. 
(ii) Every group has at least two faithful realizations: the left and right trans- 
lations of itself. Any group element g defines a transformation of G which maps 
any h to gh (the progressive or principal realization) and one which maps h to 
hg” (the retrograde realization). 
(iii)" The matrix groups that we have studied — GL(n, R), O(n), SO(n), GL(n, 
C), U(n), 
SU(n) — have all been studied through their faithful representations as 
n Xn matrix transformations of n-dimensional real or complex vector spaces. But 
T This example may be regarded as supplementary material.

## Page 117

3.17 Realizations and representations 
107 
each Lie group G has another representation as linear transformations on its own 
Lie algebra. This is called the adjoint representation, and is defined as follows. 
Consider first the map of G into itself given by J,:h t> ghg™'. This is the group 
adjoint realization of G consisting of left-translation by g and right-translation 
by g -. (It is not necessarily faithful: if G is Abelian then J g is the identity map 
h +h 
for all g.) This realization is called the inner automorphisms of G. Notice 
that each J, maps the identity e into itself, so that every curve through e is 
mapped into a (possibly different) curve through e, as shown in figure 3.14. 
Therefore J, induces a map of any tangent vector in T, to another one in Τε. 
This map is called Ad,, the adjoint transformation of T, induced by g. Now, if 
the solid curve in figure 3.14 is a one-parameter subgroup, say exp (tX) where 
X is in Το, then so is its image under J,, since g( fh)g' = (gfg™')(ghg™'). It 
follows that the dashed curve in figure 3.14 is the one-parameter subgroup gener- 
ated by Ad,(X), 
I,[exp (tX)] = exp [tAd,(X)]. 
(3.79) 
Now if g itself is a member of a one-parameter subgroup g(s) = exp (sY) there 
should be a natural expression for Ad,(X) in terms of Y. This is provided by the 
next exercise. 
Exercise 3.23 
Show that 
Adgs)(X) = exp (s£s)X. 
(3.80) 
Fig. 3.14. What happens to curves through e under the map h b> ohg Ἱ. 
shown first as the map 
gh followed by the map gh b> ghg!. The 
identity e is mapped into itself but points 4 and f near it are generally 
changed, so that a tangent vector at e is mapped into another one.

## Page 118

Lie derivatives and Lie groups 
108 
3.18 | Spherical symmetry, spherical harmonics and representations of the 
rotation group 
We have discussed Killing vectors and their relation to symmetries of 
Euclidean space. We can now make all of these notions precise by concentrating 
on the example of spherical symmetry. A manifold M with a metric tensor ϱ| is 
said to be spherically symmetric if the Lie algebra of its Killing vector fields has 
a subalgebra (i.e. a subspace whose brackets remain in the subspace) which is 
the Lie algebra of SO(3). We have to speak of a subalgebra because g| might have 
more symmetries, and here we will only consider those having to do with its 
spherical nature. The reader should note that it may be wrong to say M is spherical 
‘about some point’, because the ‘centers’ of the spheres may not be in M (see 
figure 3.15). Our definition is intrinsic: the Lie subalgebra concerns vector fields 
of M itself. In §3.9 we saw what the Lie algebra of the vector fields {/,., 1,, 1,} 
was, equation (3.30). By defining V; =—/,, V. =— ly, and V3 =—J, we see 
that the Lie algebra of the vector fields {V;} is identical to that of SO(3), 
equation (3.64). This shows that our present definition of spherical symmetry 
implies the existence of a foliation of M into surfaces with the geometry of 
spheres. (Foliations were defined in 53.7.) 
Suppose we concentrate now on functions defined on the two-sphere S*. Any 
function on 
M defines such a function on any of its spheres of symmetry. We 
define the space of functions 1, (53) to be the Hilbert space of all complex-valued 
functions on S* which are square-integrable: the norm 
1/2 
Thal -|f wu sin ϐ d0 a4 
(3.81) 
exists, where the integral is over the usual area element of the sphere. (Our defi- 
nition of this space is a little sloppy, but accurate enough for our purposes here.) 
The space L?(S”) is a vector space of infinite dimension. Its elements are func- 
tions, linear combinations of which are made with constants, and no finite 
number of functions is a basis. The realization of an element g of SO(3) asa 
Fig. 3.15. The cylinder is axially symmetric, but the centers of its 
circles of symmetry are not in the manifold.

## Page 119

3.18 Spherical symmetry 
109 
mapping R(g) of S? into itself causes any function f(x’) on the sphere to be 
mapped into another one, simply by being carried along by the mapping. There- 
fore R(g) can also be identified as a representation of SO(3) in the vector space 
L*(S*), an infinite-dimensional representation since 1, (53) is of infinite dimen- 
sion. The question arises whether there are finite-dimensional subspaces of 
L*(S*) which provide representations of SO(3). Such a subspace would have to 
be invariant under SO(3), in the sense that R(g)[ f | for any g in SO(3) and for 
any f in the subspace must also be in the subspace. Suppose such a subspace 
exists and {f,,i=1,...,N}isa basis for it. Then it is invariant if and only if 
for any numbers {a’} there exist {211 such that 
R(g)la’f] = οἱ. 
(3.82) 
Because the map is linear there is a relation 
bi = gia’, 
(3.83) 
which defines a matrix g'; corresponding to the element g of SO(3). This matrix 
is called the representation of g in the subspace. A representation of SO(3) in 
any vector space V 
is said to be irreducible if V contains no finite-dimensional 
subspaces invariant under SO(3). 
The construction of the irreducible representation of SO(3) in L?(S7) is 
treated in many books (see Gel’Fand, Minlos & Shapiro, 1963). All physicists 
know the basis functions of the irreducible subspaces as the spherical harmonics, 
Υμῃ. Rather than go through their construction, let us simply try to understand 
them in terms of the present discussion. The claim is this. Every irreducible sub- 
space of L?(S*) is characterized by an integer / > 0 and has dimension 2/ + 1. 
The functions {Y},,,m =—l,...,/}are basis functions for this subspace, called 
V,. Moreover, the union of all these bases for all / is a basis for L?(S”) itself, 
which means that the spherical harmonics are complete. Since any map R(g) of 
S? into itself is the exponentiation of a linear combination of the vectors {L.., ly, 
|}, V, is invariant under SO(3) if and only if it is invariant under J,, 1, and J,. 
A trivial example is 7 = 0, where the basis function Yoo = 1 has Lie derivatives 
L,.(Yoo) = ly (Yoo) = L(Yoo) = 0, 
all of which are certainly linearly dependent on Yo9- A better example is /= 1, 
where the three basis functions are 
42 
112 
41142 
Y,-. = 
|—] 
 siné e?? γιο 
[1] 
cos6,¥,, = 
|— 
sine? . 
δπ 
4π 
δπ 
(3.84) 
Exercise 3.24 
(a) Show that if x,y,z are Cartesian coordinates of R*, then on the sphere 
S* given by x? + y? + z* = 1 the following hold

## Page 120

Lie derivatives and Lie groups 
110 
3 1/2 
3 1/2 
3 1/2 
Y,-1 
=) (x 
—iyv), 
Yio 
(=) 2,411 
(= (x + iy) 
(b) Construct all the derivatives 111 κ. ¢.g. 
L(Y, 1) = —iY; ο/(2)3, L(Y, 1) = iVia, 
(3.86) 
and show that the space V, is invariant under SO(3). 
Why is this particular basis for V; chosen? This is largely a matter of conveni- 
ence. It is convenient that the basis should consist of eigenfunctions of relevant 
operators, i.e. functions which satisfy 
Af = af 
(3.87) 
for some operator A and constant a. The spherical harmonics are chosen because 
they are eigenfunctions of both J, and {2 = (£3)? + (£7,)° + (£;,)’, which was 
defined in exercise 3.7. The following exercise shows that this is the best one can 
hope to do: one cannot find nontrivial eigenfunctions of any two of {ς, ly, ο}. 
Exercise 3.25 
Assume that a function fhas the properties 
L.(f) = af, lL, 
(f) = Bf 
for constants a and β. Show from the Lie bracket relations (3.30) that 
a=B=1,(f)=0. 
Incidentally, the completeness of the basis functions comes from the fact that il, 
and L? are commuting operators (cf. exercise 3.7) which are (or extend to) self- 
adjoint operators on L?($7). The spectral theorem of functional analysis (cf. 
Riesz & Sz.-Nagy, 1955) guarantees completeness of their eigenfunctions. 
Actually, the representations of SO(3) may be studied much more abstract- 
ly than is apparent in the above discussion. In particular one does not need to 
say what the vector space V is in order to develop most of the algebra. For 
example, our original representation of SO(3) as matrices transforming vectors 
of R® is certainly irreducible, since no subspace of R* except the trivial one {0} 
is left invariant by all rotations. It turns out to be formally identical to the repre- 
sentation / = 1 of the spherical harmonics, which also has dimension three 
(= 21+ 1). In fact, equation (3.85) is simply a coordinate transformation of R? 
from (x,y, 2) to (Y, -;, Yio, Y1,). The transformation involves complex 
numbers, but if these are just treated algebraically then the matrices ο, of (3.83) 
expressed on the spherical-harmonic basis may be transformed into matrices 
expressed on the usual Cartesian basis, and these matrices turn out to be nothing 
more than the matrices we used to define SO(3) in the first place.

