<!-- source-pdf: Bernard F. Schutz-Geometrical Methods in Mathematical Physics-Cambridge University Press (1980).pdf | pages 181-210 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 181–210

## Page 181

5.9 Linear dynamical systems 
171 
freedom, so there are more than one q and p. A particle in three dimensions has 
3 qs and 3 ps, so phase space is 6-dimensional. A system containing Ν such par- 
ticles has a 6.V-dimensional phase space. If we consider now a general system with 
n degrees of freedom, then phase space is 2n-dimensional, and all the above 
results still hold if we take the two-form ὦ to be 
4 
ὢ = 2 dq4 a dpa. 
(5.35) 
τι 
Such an @ is called a symplectic form, and then phase space is a symplectic 
manifold. 
5.9. 
(a) 
(b) 
Exercise 5.7 
Show that fis a constant of the motion if X;= (df ) is an invariant of 
Hie. 
τα. = 0. 
(5.36) 
(Refer to exercise 5.6.) 
Define a volume-form o for phase space by 
G = ὤλ...Λλῶ,. 
(5.37) 
Ne” 
n times 
where 27 is the dimension of the space, Show that o #0 and that a 
Hamiltonian vector field U is divergence-free in this volume measure. 
Said another way, this volume in phase space is preserved by the time- 
evolution of the system. This is known as Liouville’s theorem. 
Exercise 5.8 
We now prove the remarks made in 53.12 about the relation between 
Killing vectors and conserved quantities. For particle motion the 
coordinates of phase space are {g“, p, } = {x', p; = mv;}and the 
Hamiltonian is H = (1/ 2m)g" pp; + @(x'). Prove that if Vis a Killing 
vector and if ® is constant along U, then its conjugate momentum, 
g = U'p;, is a conserved quantity. Hint: using exercise 5.7, define X, 
as the vector field in phase space whose space components equal U and 
whose momentum components vanish. Show that 
Lx , = 0, 
and find f from equation (5.31). 
Linear dynamical systems: the symplectic inner product and conserved 
quantities 
Even more strikingly simple ways of formulating conservation laws are

## Page 182

Applications in physics: Hamiltonian mechanics 
172 
possible for linear systems, by which we mean dynamical systems whose Hamil- 
tonian has the form 
H= 
> (T4?pappt Vapqq?), 
(5.38) 
A,B=1 
where 
and V4, are independent of the p,s and q“s. This system is called 
linear because the equations of motion are linear in {q“, ρα }: 
TAB 
dpa 
9Η 
B 
στ agh Van 
(5.39) 
dg* 
9Η 
Α 
Notice that we can take Γ43 = T?4 and V4p = Vga, since the antisymmetric 
Τ48 would make no contribution to H when contracted with the 
part of, say, 
symmetric expression D4Pp.- 
The linearity of the system ensures that if {q@4), Paya} and {4%), Pra} are 
solutions then so is {αφ + Baty; OPA + Piya } for arbitrary constants a and 
8. Thus, this phase space is not just a manifold; it has a natural vector-space 
structure as well. A vector space is, of course, a kind of manifold, since it has a 
map into R”, but it is a manifold which can be identified with its tangent space 
at every point. That is, since a curve in a vector space is a sequence of vectors, 
the tangent to the curve is just the derivative of the vectors along the curve, 
which is another vector, i.e. another element of the vector space. A vector space 
is its own tangent space. More than this, all the tangent spaces Tp have a natural 
identification with each other: we are able to speak about vectors in different 
Tps as being equal or not, simply by whether or not their components are equal. 
(This means a vector space is a flat manifold: see chapter 6.) 
Since a point in phase space is a vector, we can use the symplectic form @ to 
define an inner product between elements of phase space. If Y,) is the vector 
whose components are {9(4), Paya, 4 =1,...,N}and if Y.) similarly has 
components {a6 , Paya }, then their symplectic inner product is defined as 
(Yay, Yay) = 2 (Pa — W)Paya): 
(5.41) 
If ¥,)(t) and Y;.)(t) are solution curves, then their symplectic inner product is 
independent of time {. To prove this, we simply substitute the equations of 
motion into the expression for d@(Y(4), Y2))/dt (sum on repeated indices here): 
do. 
=o 
d 
d 
dt ὤ(Υω. Yay) = dt (94) Pia + at) qr A 
d 
d 
— dt (96))Paya .. πο gp WA

## Page 183

5.9 Linear dynamical systems 
173 
= TA pypPaya + VaBdGy{@ — T?®payaPos 
_ VapUa dy: 
From the symmetry of 748 and V4, we conclude: 
d= 
= 
αγ Lay, ey) = 0 
(5.42) 
if Y4)(t) and Σ(1) are solutions. 
The symplectic inner produce enables us to define in an elegant way certain 
conserved quantities associated with solutions. At first sight this may not be 
obvious: although the symplectic inner product is conserved, the symplectic 
inner product of a solution with itself vanishes identically. The trick is to use 
an invariance of the system (1.9. of 
748 and V4,) to generate from one solution 
Y another closely related one. For example, suppose 74? and Υλη are indepen- 
dent of time. Then the equations of motion tell us that if Υ(1) is a solution, so 
is dY/dt. We define the canonical energy E, of the solution Y to be 
dt 
It is easy to verify that Ε(Υ) is just the value of the Hamiltonian on the 
solution Y. 
Other conserved quantities are just as easy to derive. It usually happens that 
Τ45 and V,p depend on the coordinates {x'} of the manifold in which the 
dynamical system is defined (Euclidean space for nonrelativistic dynamics). If, 
as in exercise 5.8, there is some vector field U for which 
£574? = 0 = £oV ap, 
(5.44) 
then there is a conserved quantity associated with U. (In computing £5777 it is 
important to distinguish between indices A, B which refer to coordinates in 
phase space and the tensorial character of 7“ on the original manifold. The 
quantities 74 may be scalars, or tensors on the original manifold, depending 
upon whether the quantities g“ are scalars or tensors of higher order. The 
indices A and B are labels; they do not imply that 74% should be treated as a 
tensor of type (4) when computing the Lie derivative with respect to U, because 
U is a vector field in the original manifold, not in phase space.) As before, if Y is 
a solution, then so is £;Y. (Again the same remark applies: this is a derivative in 
the original manifold, not in a phase space.) We therefore define the (conserved) 
canonical U-momentum 
+ 
PAY) = ὅ(αργ. Υ). 
(5.45) 
The reader is invited to try a simple example, such as the one given in exercise 
5.8, to verify that the usual conserved quantity does indeed appear. 
Although our discussion has been confined to systems with a finite number 
+ 
EA(Y) = a(t | 
(5.43)

## Page 184

Applications in physics: Hamiltonian mechanics 
174 
(V) of degrees of freedom, the formalism generalizes in a straightforward way to 
continuous systems, such as wave equations. Readers familiar with the Klein— 
Gordon equation may recognize the symplectic inner product: the integral of 
the conserved Klein-Gordon current density ψ ἵψ — Wy" is just (to within con- 
stant factors) @(W*, ψ). A discussion of the canonical conserved quantities for 
waves in fluids, with application to questions of stability, can be found in 
Friedman & Schutz (1978) (see bibliography). 
5.10 
Fiber bundle structure of the Hamiltonian equations 
Our original statement in §5.4 that we defined phase space to be the 
manifold whose coordinates are p and q, hid a lot of interesting and important 
structure. Suppose a dynamical system has the N coordinates {q'} corresponding 
to its Ν degrees of freedom. These define a manifold called configuration space 
M, and the evolution of the dynamical system in time is described by a curve 
q'(t) in M. The Lagrangian 7 is a function of g’ and dq'/dt, and so is a function 
on 7M, the tangent bundle of Μ. We now show that the momentum 
ρι = ὃσ]ο(ᾳ 
4), 
(5.46) 
is a one-form field on M, a cross-section of the cotangent bundle T*M. We show 
this by its transformation properties. Let us define new coordinates for M 
Q’ = οἳ(ᾳ). 
(5.47) 
Then the new momenta are 
af 
ο 
dq", 
P; = ani. — ο 
j' 
. 
9ο st 
og it 90 it 
Now, both αι and Q! , are elements of the fiber over any point P, and coordi- 
nates on this fiber undergo a natural change induced by (5.47). That is, if V is 
any vector at 
Pits components change by 
vi=N,vP, 
VR = Ate, 
This applies as well to the velocity vector q” 
wt 
oq” 
αι = MQ! επ 
at = ΛΑΟ. 
ag’ 
(5.48) 
Using this in (5.48) gives 
Ρ, = A*pp,, 
(5.49) 
so that the momentum is indeed a one-form. 
It follows that phase space, whose coordinates are {q’, p;}, is nothing but the 
cotangent bundle T*M, and the Hamiltonian is a function on this bundle. What 
is more, the symplectic form, 
= αφ) a dp;,

## Page 185

5.11 Rewriting Maxwell's equations 
175 
(summation convention employed) is independent of the coordinates in M. The 
transformation for it is 
Q' = ο) (q') == dg! = Μιά, 
P; = AM Dp —> dP; = 
A¥ 1η dq! + AP dpp. 
(Remember that this d operator acts in 7*M, not in M, and that the functions 
A*, are functions only of the coordinates of M). Then we find 
do? yn dP) = AP ;A® 
pp dq’ κ dq! + Mi jA* dq’ a ἆρν. 
(5.51) 
Now we also have 
AAR) = δν NAR) = — Ni A*y. 
So (5.51) becomes 
(5.50) 
dor Λ dP; = 
Ni, M py dqi Λ dq’ + dgi Λ ἄρι. 
The first term on the right-hand side vanishes because 
4 
of 
7 
_ Q 
i,l 
δα σα: 
is symmetric in 7 and / and is contracted with the antisymmetric form dq! A dq’ 
; 
Therefore @ is independent of the coordinates of M and is a natural structure on 
the cotangent bundle T*M. Moreover, T*M is always orientable, since the 
volume-form o defined in exercise 5.7(b) is nowhere zero. 
Clearly, although our examples treated the fiber structure as trivial (i.e. as a 
product of the q-space and p-space), it is possible to have nontrivial manifolds M 
and fiber bundles 7*M, in which all the coordinate-dependent formulae above 
are valid only in local coordinate patches. Even an example as simple as that of a 
bead constrained to move on the surface of a sphere has a nontrivial bundle 
structure for phase space, as we pointed out in §2.11. 
C Electromagnetism 
5.11 
Rewriting Maxwell’s equations using differential 
forms 
Maxwell’s equations, written in conventional form but with units where 
C= Up = €9 = 1. are 
VxB-<E = And, 
(5.52a) 
9 
VxEt ο. Ξ 0, 
(5.520) 
V-B = 0, 
(5.52c)

## Page 186

Applications in physics: electromagnetism 
176 
In writing these equations we have, of course, used the curl and divergence 
operations of ordinary flat three-space. 
What we shall show below is that there exists a way of writing these equations 
using only the concepts of the metric and the exterior derivative. First we rewrite 
the equations in their relativistically invariant form" by first defining the 
Faraday two-form F, whose components are 
O 
-ς 
-ν 
—E£, 
Ey 
0 
Bz, 
—By 
—B, 
0 
B,. 
E, 
Βν 
—B, 
0 
+ 
(Fuv) = 
(5.53) 
(Here, as in §2.31, Greek indices run over ft, x, y, Z.) 
Exercise 9.9 
Prove that under a spatial rotation F,,, transforms in such a way that 
both E and B transform as three-vectors. 
In terms of the Faraday tensor, Maxwell’s equations take a particularly simple 
form. For instance, the four equations (5.52b, c) are just 
Fryv.y = OS dF = 0, 
(5.54) 
where we have used the square-bracket notation to denote antisymmetrization. 
Exercise 5.10 
(a) Prove that (5.54) constitutes four linearly independent equations. 
(b) Evaluate (5.54) for the components of F given by (5.53) and prove 
their equality to (5.52b, ο). 
As for the rest of the equations, if we introduce the special-relativistic metric 
whose components in this coordinate system are 
-ι 
0 
ο 
0 
0 
1 
ο 
ο 
= 
5.55 
(Suv) 
ο 
0 
1 
ο 
(5.55) 
ο 
ο 
ο 
1 
T Ror readers to whom this is unfamiliar, recall that Maxwell’s equations are the 
correct theory for light and that special relativity was invented to explain certain 
properties of light, so the theory is already relativistically correct. All we do here 
is to find a convenient form for the equations.

## Page 187

5.11 Rewriting Maxwell’s equations 
177 
then we can define an antisymmetric (6) tensor F whose components are 
Fle = gle orb Fg, 
0 
E 
Ey 
Ε, 
(FRY) = 
(5.56) 
Exercise 5.11 
Prove equation (5.56). 
Then the remaining equations are 
FH = 4nd", 
(5.57) 
where we have defined the current four-vector to have components {J‘ = p, 
J' =(J)' fori=x,y, z}. 
Exercise 5.12 
Prove that the four equations (5.57) are just the same as (5.52a~—d). 
So far we have stuck to Lorentz coordinates because, while (5.54) is 
coordinate-independent, (5.57) is not a valid tensor equation in every coordinate 
system (recall exercise 4.15). On the other hand, we saw in exercise 4.23 how to 
define the divergence of an antisymmetric (2) tensor (two-vector) if we have a 
volume-form. Because we have a metric, and because { 9/9, 0/dx, 0/dy, 9/92} 
form an orthonormal basis in this metric, the preferred volume-form is 
6 = dtadxa dy a dz. 
The following exercise develops the argument. 
Exercise 5.13 
(a) Define the two-form *F to be the contraction 
*F = 13(F), 
(5.58) 
1.6. 
Puy — Wo purl? 
This is, of course, the dual of F introduced in chapter 4. Find the 
components ( Ε)ιν in terms of E and B.

## Page 188

Applications in physics: electromagnetism 
178 
(b) Define the three-form ΤΟΥ the contraction 
ΤΞξ OV), 
(5.59) 
and show that (5.57) is equivalent to 
dF) = 4n°J. 
(5.60) 
By exercise 4.23 this is also 
div.,F = ἀπ]. 
(5.61) 
Note the great formal similarity between the two halves of our new form for 
Maxwell’s equations: 
4 
dF = 0, 
(5.54) 
4 
d*F = 4n*J. 
(5.60) 
Note also that they now are completely coordinate-free, so they have this form 
in any manifold with metric (because the metric was needed to obtain *F from 
F). The similarity between (5.54) and (5.60) is deep in Maxwell’s equations. 
Note that the * operation on F’ simply results in an exchange of E and B (cf. 
exercise 5.13(a)), and recall also that J was the electrical current density. If there 
were magnetic monopoles we would have two current densities, J, and J,,, and 
Maxwell’s equations would take the symmetric form 
dF = απ, 
d*F = 4n*Jq. 
(5.62) 
Exercise 5.14 
(a) Prove (5.62). 
(b) Prove by exterior differentiation that equation (5.60) guarantees con- 
servation of charge, i.e. that 
divVJ) = 0. 
(5.63) 
Exercise 5.15 
Establish the integral theorem for charge in the following way. 
(a) Choose any oriented three-dimensional hypersurface & and restrict 
(5.60) to it. Prove that restriction commutes with exterior differen- 
tiation, i.e. that 
dl(“Plgl = (Ply. 
(b) Choose a region 
Hof #, with boundary 0 
Integrate the restriction 
of (5.60) over # and apply Stokes’ theorem to find (appropriate 
restrictions implied) 
[ F=—) 
F 
g 
Απ 
'ο6)

## Page 189

5.12 Charge and topology 
179 
(ο) In the case where & is a hypersurface t = const in Minkowski space- 
time and 0 
Dis a sphere, show that this gives the total charge in Das an 
integral of the normal component of the electric field over 9.5). 
5.12 
Charge and topology 
Since we can now formulate Maxwell’s equations on any manifold with 
a metric, we can mention two attempts which have been made to resolve the 
puzzling question ‘what is charge?’ by answering ‘charge is topology’. The first 
explanation, due to J. A. Wheeler (1962), is extremely simple. Consider figure 
5.2, in which a hypersurface t = const of some hypothetical spacetime is 
depicted. The lines drawn are integral curves of E. There is no charge density 
anywhere, and these integral curves are either closed (threading through the 
handle, out one hole, and down the other) or infinite (though they pass through 
the handle). Consider what an experimenter who measures E on the sphere S sur- 
rounding one hole will deduce: the integral {¢ F ς Will certainly not vanish (E is 
outward-pointing all over S), and he will say the hole has positive charge. Like- 
wise, a Sphere around the other hole would give it negative charge, of exactly the 
same magnitude. (The calculation of exercise 5.15 fails because S does not divide 
the manifold into an inside and outside, cf. figure 4.10.) So this is a model for 
‘charge without charge’, which has the bonus of explaining why negative charges 
equal positive charges. It has two drawbacks: first, no-one pretends to have a 
solution to, say, Einstein’s equations which gives a geometry for spacetime that 
looks like this; and second, it is perhaps philosphically displeasing to think of 
Fig. 5.2. A ‘wormhole’ or handle attached to a three-dimensional mani- 
fold with one dimension suppressed. Lines of force can thread through 
the handle, come out, and go backdown again to give each ‘mouth’ the 
appearance of charge in a charge-free space.

## Page 190

Applications in physics: electromagnetism 
180 
two charges, which may be separated by huge distances, linked together by their 
own special ‘handle’. 
The second explanation is more sophisticated, using a manifold made non- 
orientable by a special construction of the handle. This is due to Sorkin (1977) 
(reference in the bibliography of chapter 4). In this model, both holes have the 
same charge and so may be assumed to be close together, forming what to an out- 
side observer looks like a single charge of twice the strength of each hole. Here 
the breakdown in exercise 5.15 occurs because the manifold is nonorientable. 
This mode! overcomes the second objection to Wheeler’s picture, but not the 
first. And neither model explains why two unrelated charges should be equal. 
Nevertheless they illustrate a maxim which is becoming more convincing all the 
time: there is more to theoretical physics than just its local differential equations! 
5.13 
The vector potential 
The existence of a ‘vector potential’ for Maxwell’s equations follows 
naturally from (5.54). Since F is a closed two-form, there is a one-form A such 
that 
4 
F=dA 
(5.64) 
in some neighborhood of any point. This one-form can be mapped into a vector 
by the metric, and this is called the vector potential. 
A more natural concept is, 
of course, the one-form potential. Note that A is not uniquely defined: A =A 
+ df, for an arbitrary function f, also gives Fin (5.64). This is a gauge transfor- 
mation. Note also that if magnetic monopoles exist, then dF does not vanish 
everywhere. By our discussion of exact forms in chapter 4, it will be possible to 
define A only in simple regions which contain no magnetic monopoles. In par- 
ticular, in a region of spacetime containing the world-line of a magnetic 
monopole, the one-form potential cannot be consistently defined everywhere. 
Exercise 5.16 
(a) Show that, if a one-form potential A exists, then in nonrelativistic 
language it is related to the scalar potential @ and the vector potential 
A' by 6 = Ap, 
A! (vector potential) = 
— A, (one-form), where indices 
refer to the coordinates of (5.52). 
(b) Show how ¢ and A’ defined in (a) change under a gauge transformation. 
(c) To illustrate the problems caused to the one-form potential A by mag- 
netic monopoles, consider a situation with charges and no monopoles, 
but in which one defines a one-form potential a for *F by the equation 
"Fe = da. 
(By the duality between electric and magnetic fields under the

## Page 191

5.15 Role of Lie derivatives 
181 
*-operation, @ should have the same problems with electric charge as A 
has with magnetic.) Write down Maxwell’s equations in terms of a and 
show that @ exists in regions that contain no charge and that can 
be shrunk to zero. Show this by finding an explicit solution for α in 
the case of a single isolated static charge q. 
5.14 
Plane waves: a simple example 
Plane electromagnetic waves, as is well-known, travel at the speed of 
light. Consider a particular Faraday tensor ΓΔ, all of whose components are 
functions only of u = t — x (recall that we are using units in which ο = 1): 
Fe = Αἲβ(--κ) = A*B(y). 
(5.65) 
What are the conditions that this satisfy the empty-space equations dF =0, 
d*F = 0? From (5.65) we have 
dF 
ἄ(ξ Εμν dx! a dx’) = 5 d(Fy,y) A dx" a dx” 
4(dA,,,/du)du A dx” κ dx”. 
From (5.53) it is easy to deduce 
d 
.--- 
d 
-.,- 
dF = |— (8, —£,)dta dxa dy +—(@,,)dta dyn dz 
du 
du 
d 
~~ 
~~! 
~~ 
d 
ο. 
~ 
~ 
+ 
—(—B,,)dx a dy a dz + —(—B, —E£,)dta dx a dz{, 
du 
du 
the vanishing of which implies (ignoring any static fields) 
B,= Ey, 
By =—E,, 
B, =0. 
(5.66) 
Exercise 5.17 
Show that the equation {3-0 implies 
B,=Ey, 
By =—E,, 
 E, = 0. 
(5.67) 
By this exercise we see that a plane electromagnetic wave has transverse electric 
and magnetic fields (i.e. perpendicular to its direction of propagation), and that 
these are determined by two independent functions, £,,(u) and £,(u), corres- 
ponding to the two independent polarizations of the wave. 
D Dynamics of a perfect fluid 
5.15 
Role of Lie derivatives 
By a ‘perfect’ fluid we mean one which has no viscosity and moves

## Page 192

Applications in physics: fluid dynamics 
182 
adiabatically, i.e. with no heat conduction. It is well-known that such a fluid 
obeys certain local conservation laws: during its motion any fluid element has a 
constant mass, entropy, and — in some sense — vorticity. These conservation 
laws are usually derived using ordinary vector calculus, and can seem rather 
complicated. From the geometric point of view, the existence of a flow suggests 
immediately the use of the Lie derivative, and we now show that the local con- 
servation laws become much more transparent when framed with Lie derivatives. 
5.16 
The comoving time-derivative 
We have seen in exercise 4.22 that the equation of continuity, whose 
conventional form is 
0 
_ 
5. 
+ div(pV) = 
takes the form 
0 
+ 
. 
+ ον 
(ρῷ) - 0, 
(5.68) 
where 6 == dx a dy a dz is the volume three-form of Euclidean space. The 
operator (0/d¢ + £77) is a natural time-derivative operator following a particular 
fluid element. To see this, think not of space but of the four-dimensional mani- 
fold called Galilean spacetime, whose coordinates are (x, y, z, t) (see $2.10). 
Any hypersurface ¢ = const is in fact Euclidean space. Then the motion of a fluid 
element describes a curve on spacetime, called the world-line of the element. In 
figure 5.3, two such world-lines (4A’ and BB’) are drawn. For an infinitesimal 
change in time dt, a point on this curve moves from the point with coordinates 
(x, ¥,Z, t) to the one with coordinates (x + V*dt, y + V*dt,z + V7dt, t+ df). 
If we call U the tangent to the world line in the four-dimensional manifold, then 
it clearly has components (V*, V”, V*, 1). The time-derivative following a fluid 
element is simply £z, the natural derivative along the world-line of the element. 
Fig. 5.3. Two moments of Galilean time and the world lines AA’ and 
BB' of two particles. The vector U is the tangent to AA’ parameterized 
by time f.

## Page 193

5.17 Equation of motion 
183 
Exercise 5.18 
Using equation (2.7) show that 
_ 
0 
_ 
LgW = fa to 
W, 
(5.69) 
where W is any vector field in the hypersurface t = const, i.e. any 
purely spatial vector field (W‘ = 0). 
Equation (5.69) clearly holds if W is replaced by any (0) tensor which is entirely 
in the three-space t = const. It might seem that the notion of a tensor being 
purely spatial is not invariant under coordinate changes in the four-dimensional 
manifold, since it simply says that all the t-components of the tensor vanish. 
This is acceptable here, however, because of the rigid distinction made in non- 
relativistic physics between space and time. 
Exercise 5.19 
The most general kind of coordinate transformation which remains 
‘natural’ to the fiber-bundle structure of Galilean spacetime (§2.10) is 
t=); 
x! = fi’, d),7=1,2,3. 
(5.70) 
Show that under this transformation a (0) tensor A with no time- 
components (A(..., ὤ',.. .) Ξ 0) remains one with no time- 
components, and a (2) tensor B with no spatial components (i.e. only 
B, ,is nonzero) remains one with no spatial components. 
5.17 
Equation of motion 
The condition that the flow be adiabatic means that the total entropy 
of a fluid element must be conserved. It is convenient to work with S, the 
specific entropy (entropy per unit mass). This must clearly be constant during 
the flow: 
ὃ 
+ 
(24 te) 
= 0. 
(5.71) 
The Euler equation of motion for a fluid whose pressure is p and which 
moves in a gravitational field whose potential is ® can be written in Cartesian 
coordinates as 
9 pig γι 
? 54% 
© = 0, 
(5.72) 
Ot 
ox?

## Page 194

Applications in physics: fluid dynamics 
184 
There are two reasons that this equation is valid only in Cartesian coordinates: 
first, some indices 7 are up and some are down, and only in an orthonormal basis 
does this make no difference; second, the term 0V'/dx/’ transforms like a (1) 
tensor only if the transformation matrix A’ j 
is independent of position (exercise 
4.5), which is true for a transformation from one Cartesian frame to another. 
The usual way to adapt it to arbitrary coordinates is to introduce the covariant 
derivative, which is defined in the chapter on Riemannian geometry. Here we 
show that there is a different, and very instructive, approach. First, note that the 
first two terms of (5.72) can be written as 
OMG, yi hi 
ot 
Ox? ” 
since there is no difference between V' and V; in Cartesian coordinates. (We use 
here, of course, the fact that the three-dimensional space has a metric tensor.) 
Next, replace the derivative V/0/8x! with the Lie derivative (equation (3.14)) of 
the one-form V=g|(V,_): 
(Ly V); . | = | ~~ +- 
| κ. 
. 
O 
1 ὃ 
- Yi—y+--— 
ox? 
§ 
2 dx’! (VV), 
where in obtaining the final expression we again used the fact that V; = Vi 
Therefore we find 
. 
0 
ο 
ὃ 
νο νι 
(νι πάν. 
(5.73) 
Both terms on the right-hand side are tensors in any coordinate system! There- 
fore (5.72) becomes the frame-independent expression 
0 
~ 
1- 
~ 
+ 
(2 ὃν 
V+—dp+ d(@®—34V’) = 0. 
(5.74) 
ρ 
In this the role of the metric is crucial but hidden: it is required to form V from 
V,and hence to form V? = V(V). 
5.18 
Conservation of vorticity 
Now we are in a position to consider conservation of vorticity. In con- 
ventional terms, the vorticity is the curl of the velocity, V x V. As we saw in 
chapter 4, this is properly the exterior derivative dV. Now, exterior differen- 
tiation and Lie differentiation commute (and of course d and 3/dt commute 
since d only involves spatial derivatives), so we find from (5.74)

## Page 195

5.18 Conservation of vorticity 
165 
[e+ 
by Jay 
= + doa dp. 
(5.75) 
ot 
ρ 
(We have dropped tildes over symbols for clarity.) There are two cases to be con- 
sidered. The easier is when the fluid obeys an equation of state p = (0). Then 
dp a dp =0 and we find that the vorticity two-form dV obeys the local (or con- 
vective) conservation law 
ot 
This is the Helmholtz circulation theorem, written in its most natural form. A 
different result holds, however, if the more general equation of state p = p(p, S) 
obtains. Then the right-hand side of (5.75) does not vanish, but its wedge pro- 
duct with dS does: 
dSadpadp = 0. 
(5.77) 
5 
+ to 
dV = 0. 
. 
(5.76) 
Exercise 5.20 
Prove (5.77). 
The exterior derivative of (5.71) gives 
ot 
Therefore we can wedge dS with (5.75) to get 
ο ον 
dS = 0. 
(5.78) 
ὃ 
ἀδλ[-- £y| άν = 0, 
or 
ὂ 
9 
(> ο] 
dSadV = 0. 
(5.79) 
This equation is the most general vorticity conservation law. It is called Ertel’s 
theorem. 
The meaning of the three-form dS Λ dV may not be immediately apparent, 
but it is possible to convert (5.79) into a conservation law for a scalar. The 
reason is that there is another conserved three-form, pw, and any two three- 
forms in a three-dimensional space are proportional. Therefore there is a scalar 
function a such that 
dSa dV = apw, 
(5.80) 
and (5.68) and (5.79) then give the scalar equation

## Page 196

Applications in physics: cosmology 
186 
ὃ 
—+£e]a = 0. 
It can be shown that, in conventional vector notation, 
1 
a = -νςο  σχγ. 
(5.81) 
p 
Exercise 5.21 
Prove (5.81). (Hint: express both sides of (5.80) in terms of dx a dy 
A dz.) 
In the notation introduced in chapter 4 we have 
1. 
a = 
--εὖ 
το Vj. 
(5.82) 
p 
Therefore α is the dual of dS ~ dV with respect to pw. The conservation of a is 
then a natural consequence of the conservation of dS a dV: the fact that ρω is 
conserved means that forming duals with respect to it is an operation which is 
also conserved, i.e. which commutes with the operator 0/dt + £7. 
Exercise 5.22 
The shear of a velocity field V is defined in Cartesian coordinates by 
the equation 
συ = Vig + Vii — 5649, 
(5.83) 
where @ is the expansion 
θς ν.γν. 
(5.84) 
Show that in an arbitrary coordinate system 
0 = he" £u8;;, 
(5.85) 
ση = Leg — Ίθει. 
(5.86) 
E Cosmology 
5.19 
The cosmological principle 
Most physicists are aware that Einstein’s theory of general relativity has 
given modern physics a consistent and fruitful framework in which to study cos- 
mology, the large-scale structure of our universe. Most are also aware that, at 
least at the simplest level, there are only three basic cosmological models: the

## Page 197

5.19 The cosmological principle 
187 
‘closed’, ‘flat’, and. ‘open’ universes. What is probably less well known is that this 
simplicity of having only three models is not at all a prediction or consequence 
of Einstein’s equations. Rather, it is simply a consequence of assuming that the 
universe is homogeneous and isotropic in its large-scale properties. (Homogeneity 
and isotropy will be defined precisely below.) General relativity, like all the 
fundamental theories of physics, is a dynamical theory: given initial conditions, 
it will predict their future evolution and past history. The uniformity of the uni- 
verse is part of the initial conditions we put in to construct the simplest models. 
The important contribution of general relativity is that it permits us to choose 
the geometry of space — its metric tensor field — as a part of the initial con- 
ditions. This is not possible in Newtonian gravity, of course. Once we decide to 
choose the most uniform initial conditions, it is differential geometry that tells 
us that only three metric tensor fields are possible. Our aim in the next few 
sections is to find these metrics. We shall use the mathematics of symmetry and 
invariance developed in chapter 3, but we will not need to know anything about 
general relativity nor even about Riemannian geometry. 
We begin with the physical problem: the universe. On a small scale the uni- 
verse is certainly lumpy. On nearly any length scale from the nuclear (10:15 m) 
to the interstellar (10171), our world is characterized by clumping of matter 
into small regions with sharp demarcations between different kinds of matter or 
between matter and the vacuum. The stars themselves group into more or less 
isolated galaxies, galaxies congregate into clusters of several tens to thousands, 
and even clusters may associate in loose superclusters. But modern astronomy 
can see well beyond the supercluster length scale, and we find that in all direc- 
tions the tendency is for greater and greater homogeneity in the properties of 
the universe when they are averaged over larger and larger length scales. Since it 
is these large-scale averaged properties (particularly the mean density and 
Fig. 5.4. A slice of spacetime showing all the events labelled by coordi- 
nates ¢ (time) and x, with y = z = 0. Because electromagnetic radiation 
travels at a finite speed, distant objects are seen at an earlier time in 
their own histories than nearby objects. 
ver 
now 
observe 
recent 
past 
Nearby 
galaxy

## Page 198

Applications in physics: cosmology 
188 
velocity) that are important for the dynamics of the universe, the cosmologist 
would like to incorporate this homogeneity into at least the simplest models. 
But what does homogeneity really mean? After all, in a dynamical universe, the 
more distant regions should look different from those nearby if only because 
they are seen at an earlier time in their history, as illustrated in figure (5.4). 
Indeed this is the case: the number of quasars, for instance, is much higher in 
distant regions than locally. The homogeneity one ‘observes’ is really an extra- 
polation to the present time of the condition of distant regions. Yet in relativity 
even ‘the present time’ is not an absolute concept. We cannot give a full dis- 
cussion of these problems here, but we can say how they are resolved. 
The basic idea is to split spacetime up into a family of three-dimensional 
spacelike submanifolds filling it up (a foliation). These are called hypersurfaces 
of constant time (see figure 5.5). This really amounts just to a choice of time- 
coordinate. The metric tensor g| of spacetime has, like any (°) tensor, a natural 
restriction to each hypersurface, and the hypersurface is space-like if g| is 
positive-definite on all vectors tangent to it. The ‘uniformity’ of the cosmology 
depends on the Killing vectors or isometries of these hypersurfaces. 
Let G be the Lie group of isometries of some manifold S' with metric tensor 
field g|. The Lie algebra of G is that of the Killing vector fields of g|. Elements 
of G are mappings of S onto itself (diffeomorphisms). The action of G on S is 
said to be transitive on S if, for any two points P and Q of S, there is some 
element g of G for which g(P) = Q, i.e. which maps P to Q. The manifold S is 
said to be homogeneous if its isometry group acts transitively on it (see figure 
5.6). What this means is just that the geometry is the same everywhere in S. 
Suppose there are elements of G which leave some point P of S fixed. Then 
the product of any two also leaves P fixed, and since the identity e is one of 
them, they form a subgroup Hp of G called the isotropy group of P. These are, 
of course, the familiar rotations about an axis through P. The isotropy group of 
Fig. 5.5. Slicing spacetime into spaces of constant time 1.

## Page 199

5.19 The cosmological principle 
189 
P keeps P fixed and therefore maps any curve through P to another curve 
through P (see figure 5.7). It consequently induces a map of tangent vectors at P 
to others at P: a map Τρ > Tp. This group of mappings is the linear isotropy 
group of P. (Recall the similar discussion of the adjoint representation of a Lie 
group, 53.17.) A manifold S of dimension m is said to be isotropic about P if 
its isotropy group Hp is just SO(m), the group of rotations about arbitrary axes 
through P. If S is isotropic about every point P it is said to be isotropic. 
A cosmological model M is said to be a homogeneous cosmology if it has a 
foliation of space-like hypersurfaces, each of which is homogeneous; and 
similarly for an isotropic cosmology. As discussed above, the evidence is strong 
that our universe is homogeneous, at least on large scales in our observable neigh- 
borhood. We also see no systematic variations in its structure in different direc- 
tions in the sky. This suggests the universe is isotropic about us. But modern 
science does not like to assume that we live in a particularly favorable location in 
the universe. This is often elevated to the status of a principle, variously known 
as the cosmoiogical principle, the Copernican principle, or the principle of 
mediocrity: the properties of the universe we see near us would be seen, on aver- 
age, by any observer anywhere else in the universe. This principle enables cos- 
mologists, in the absence of information to the contrary, to extend our local 
Fig. 5.6. Some neighborhood U of P is mapped by g onto a neighbor- 
hood V of 0 = g(P) isometrically: there is no difference in the geometry 
near P from that near QO. 
Iz 
Fig. 5.7. The isotropy group of P maps Tp > 7p by mapping curves 
through P to other curves.

## Page 200

Applications in physics: cosmology 
190 
homogeneity and isotropy to the whole universe. Thisis not necessary, of course, 
and much current research is devoted to exploring inhomogeneous and/or aniso- 
tropic cosmologies. But the three basic models are the only three which have 
homogeneous, isotropic three-spaces. This is what we shall now prove. 
Exercise 5.23 
As we know from §3.9, the Killing vectors of the sphere S? are the 
vectors /,., ly, |... These form a basis for the Lie algebra of the group of 
isometries of S*, SO(3). Prove that S? is a homogeneous and isotropic 
manifold. 
5.20 
Lie algebra of maximal symmetry 
We shall begin by studying the Killing vector fields of a three- 
dimensional manifold S. If £ is a Killing vector, its components in any coordinate 
system satisfy the equations 
(£2); = fg + EF gn +" 
gi, = 0. 
(5.87) 
It will be more convenient to use the components of the one-form gi(é,_), 
ἐκ = Brit. 
(5.88) 
These satisfy the equivalent equations 
E+ 
77 261" = 0, 
(5.89) 
with the definition 
Γ, — ο (Si j + Emj,i — 8ij.m): 
(5.90) 
(The definition of I, including its factor of +, is conventional and would make 
more sense after a reading of chapter 6. For us equation (5.90) simply defines a 
convenient shorthand notation.) 
Equation (5.89) is symmetric under exchange of i and /, so it represents in n 
dimensions ΣΗ(ή + 1) independent differential equations, six for n = 3. Since 
there are only three components of E to solve for, the system is overdetermined: 
a general metric tensor Ο| has no Killing vectors. Our object is to find what form 
Q| must take in order that it allow the maximum number of Killing vectors. To 
see what this maximum number is, we differentiate (5.89) to get 
Evin + Ein = 2ET 
y) p- 
(5.91) 
By adding (5.91) to itself with the index permutation (i > k,j >i, k >/) and 
subtracting the permutation (i >j,j >k,k > i) we arrive at the equation 
Ei jr = Hijet, + Kijn’ £1, m: 
(5.92)

## Page 201

5.20 Lie algebra of maximal symmetry 
19] 
where Hijp is a complicated function of g;; and its first and second derivatives, 
and K wR” similarly depends on g;; and its first derivatives. The key point about 
(5.92) is that if we know é; and &; ; at any point P and if we know g;; every- 
where, then we can determine &; μι at P from (5.92), and similarly all its higher 
derivatives at P by successively differentiating (5.92). On an analytic manifold 
(which we shall assume) this suffices to determine the vector field ἕ everywhere. 
Moreover, we know that £; at P determines the symmetric part of &; ; at P by 
equation (5.89). If follows that every Killing vector field on ὁ is determined 
completely by giving the values of 
τι = &(P)and Ay  ἕμῃ(Ώ) 
(5.93) 
at any point P of S. It is important that a choice of {n;, A;;} at P does not necess- 
arily determine a Killing vector, because it may happen that (5.92) has no 
solutions: its right-hand side may not be symmetric under exchange of [ and k. 
But the argument does show that there cannot be more Killing vectors than the 
number of independent choices of {n;,A,;}, which in m dimensions is 
m+im(m—1) = $m(m + 1). 
(5.94) 
by virtue of (5.93). A manifold is said to be maximally symmetric if it has the 
maximum number of Killing vector fields. 
It is easy to show that a maximally symmetric connected manifold S is hom- 
ogeneous. At any point P we can choose a Killing vector field having any tangent 
at P. The one-parameter subgroups associated with these Killing vectors can 
therefore map P to any point Q in some neighborhood U of P (see figure 5.8). 
By a succession of such maps we can clearly map P to any point in S whatever. It 
follows that the isometry group maps P to any point, and S is homogeneous. 
Next we take a look at the isotropy group of P. Such transformations leave P 
fixed, so the associated Killing vector fields vanish at P. The Lie bracket of any 
two Killing fields V and W is 
i 
ei 
a τμ 
γὶ 
[V,w]|' = 
Vv" SW 
W' iV ; 
Fig. 5.8. By choosing the appropriate one-parameter subgroup of the 
isometry group one can map P to any point Q or Q’ in a neighborhood 
Ό.

## Page 202

Applications in physics: cosmology 
192 
~ 
[VW]; = Τι —Wi 
iV! — in, (V"W! — WED’). 
(5.95) 
If V and W both vanish at P, then so does [V, W]. But [V, W] is a linear combi- 
nation of Killing vector fields, so for it to vanish at P it must be a linear combi- 
nation only of those fields which also vanish at P. So these fields form a Lie sub- 
algebra, clearly the algebra of the isotropy group at P. The next exercise shows 
that the isotropy group is SO(m) if S is space-like, i.e. that a maximally sym- 
metric space-like manifold is isotropic. 
Exercise 5.24 
Choose at P the sort of coordinate system permitted by exercise 2.14, 
in which for a space-like manifold g;,(P) = 6,; and g;; ,(P) = 0. 
(a) Show that near P an isotropy Killing vector field is given by 
Vi = Aix! + O(x?), 
(5.96) 
where A‘, is an arbitrary antisymmetric matrix 
Ai, = —A’,. 
(5.97) 
(b) Let W be another isotropy Killing vector field, 
Wi = Bix! + O(x?), 
and show that 
[V,W]' = [A,B]',x’ + Ο(«2). 
(5.98) 
where [A, B]'; denotes the elements of the matrix commutator of A’; 
and B’;. This shows that the Lie algebra of the isotropy group is the 
same as the Lie algebra of SO(m). 
(c) Argue from this that the isotropy group of P is SO(m). 
(d) Show that if g| is not positive-definite (or negative-definite) then the 
isotropy group is not SO(m). In particular show that the isotropy group 
of a point P in four-dimensional Minkowski space is the Lorentz group 
L(4). 
5.21 
The metric of a spherically symmetric three-space 
Now we restrict our attention to space-like three-manifolds. The iso- 
tropy group is SO(3) and we say the manifold is spherically symmetric about 
any point. In this section we construct a convenient coordinate system for the 
rest of our calculation. We know that the Killing vectors of SO(3) define spheres 
S? by their integral curves. Since every point is on one such sphere, they must 
foliate the manifold S. We will adopt spherical coordinates, with the usual ϐ and 
@ on each sphere and a third ‘radial’ coordinate labelling spheres. There is a

## Page 203

5.21 The metric of a spherically symmetric three-space 
193 
particularly convenient choice for the radial coordinate. The metric of S induces 
a metric tensor on each sphere, which in turn defines a volume two-form and a 
total area (integral of the volume two-form). We define ihe radial coordinate r 
of a sphere by the equation 
area = 4nr’, 
r = (area/4n)"”. 
(5.99) 
This intrinsically defined coordinate need not be monotonically increasing every- 
where, as figure 5.9 shows. But at least in some neighborhood of P it is guaran- 
teed to be good by the local flatness theorem, exercise 2.14. (It is singular at 
r = 0, of course, but we know how to handle that.) 
In addition to the radial coordinate we have to define ϐ and ¢ more precisely. 
We have placed ϐ and ¢ on each sphere but we have not said how the pole 0 = 0 
of one sphere is related to that of another. That is, we are free to slide the 
coordinates of a sphere around as we move from one to another. We fix the pole 
in the following manner. At every point Ο there is a vector n orthogonal to the 
sphere at that point (g|(z, V) = 0 for any V in Tg(S*)), normalized to unity 
(α((π. 2) = 1), and pointing away from P (which is well defined near P and 
extends to all of S by continuity). This vector field is called the unit normal 
vector field, and is C® except at P. Choose the pole of any particular S* arbi- 
trarily and then fix the poles of all the others by demanding they lie on the 
integral curve of 7 through the original pole. This is illustrated in figure 5.10. 
This clearly will imply that any integral curve of n is a curve of constant ϐ and ¢, 
or in other words a coordinate line of the radial coordinate. Since 0/00 and 0/0¢ 
are tangent to the spheres this construction implies 
2-6 = g\(d/dr, 0/00) = 0. 
(5.100a) 
Fig. 5.9. A radial coordinate labelling circles on a sphere, defined as the 
circumference + 27. This is the two-dimensional analogue of the situ- 
ation described in the text. The radial coordinate increases away from P 
at first (say from A to B) but begins decreasing (from C to D) and 
becomes zero at P’.

## Page 204

Applications in physics: cosmology 
194 
δν = GI(0/dr, 9/9Φ) = 0. 
(5.100b) 
Moreover, on each sphere the metric is that of the unit sphere times r’, the 
appropriate factor to make the area be 4nr’: 
Soo = 1", 
Sep = 0, 
Sop = 1’ sin’. 
(5.100c) 
We therefore have only one unknown metric component, g,.. 
Exercise 5.25 
(a) Define the radial distance from P to a sphere with coordinate 7 to be 
the integral 
r [ αμ" ταν 
(5.101) 
0 
along a line ϐ = const, ¢ = const. Argue that g,, must be independent 
of 6 and ¢. 
(b) Show from exercise 2.14 that as one approaches P, 
lim g,, = 
1. 
(5.102) 
r—0 
By exercise 5.25(a) we write g,.,. = f(r) and have the metric 
fr) 
0 
0 
(gj) =| 
ο 
Fr’? 
0 
(5.103) 
0 
ο 
r?*sin?6 
As we have used only the isotropy group of P to get this, we should not expect 
to be able to determine f(r). For that we must use the rest of the isometries of S. 
Fig. 5.10. Establishing the pole of each circle of constant r in figure 5.9 
by requiring them all to lie on a single integral curve of the unit normal 
field Π.

## Page 205

5.22 Construction of the six Killing vectors 
195 
5.22 
Construction of the six Killing vectors 
There are a number of methods we could use to find the form of f(r) 
that guarantees the homogeneity of S. The method we shall use is to construct 
all the Killing vector fields of S by using the vector spherical harmonics of $4.29. 
Any vector field V on S can be written in the form 
_ 
ὃ 
—, 
.. 
V= Enm(1) Yim δν + Mm” Yim + Sim“) Σπα, 
(5.104) 
with an implied summation on / and m here and wherever they are repeated in 
the same term. We shall need the components of this equation. It is easy to 
deduce from equation (4.101) that 
(Yin) = ιο 
(Yin)? = πρ Limo: 
(5.105a) 
(Yin) = -- Yim,os (Yim)? 
πρ ἔιπιθ. 
(5.105b) 
sin 0 
sin 0 
° 
It follows that 
V" = Τμ. 
(5.106a) 
V? = 
mY imo + SimYimo/sin 4, 
(5.106b) 
V? = 
mY im,o/sin?@ — SimYim,o/sin θ. 
(5.106c) 
These components have to satisfy Killing’s equation 
Κυ = τει + V" Spi + V™ Sin = 0, 
(5.107) 
with ση from (5.103). 
The three equations {Kog = 0, Keg = 0, Κφφ = 0) do not involve derivatives 
Of Ems Nims Οἵ Sim, 50 we Shall tackle them first. First consider the combination 
(indices raised with (5.103)) 
4 
0 = K°*, +K%y = 7 slm¥im + 2nimL*(Y im), 
where 1, is the operator defined by equation (3.33). Using (3.33) we get 
[2/NEim . KI + 1)nim| Yim = 
0. 
By the linear independence of the spherical harmonics we have 
2 
> Em ~Kl+ 1ληιμι = 0. 
(5.108) 
Next consider the combinations 
ο = 3(K%s —K%) = Fimtim + GimSims 
(5.109a) 
1 
ο-- 
2 
Κρφ — — Gimtim + FimSim> 
(5.109b) 
r“ sin 8 
where F’,,, and G,,, are abbreviations for the expressions 
Fim = 
Yim,90 — cot 6 Yim,0 . μα φφ/ἱΠ76,

## Page 206

Applications in physics: cosmology 
196 
Gim = 2Yim.og/sin 8 — 2 cot OY}, 4/sin θ. 
Equations (5.109) have the solution [), = Nj = 0 unless the determinant of 
their coefficients vanishes. But this is (F;,,)* + (1η). 5ο it vanishes only if 
both F),, and G,,, vanish. It is easy to work out that this happens for / = 0 and 
= 1 (any m) but not for / > 2. Moreover, it is obvious from (5.106) that / = 0 
does not have a contribution from 7 or ¢ (the fixed-point theorem for S* again!) 
so that we can conclude 
1 = 1: Mim, Sim arbitrary; 
(5.110) 
1>2: 11m = Sim = 0. 
Then (5.108) gives us 
l= 0: & = 0, 
1= 1: ἔτι = 1m 
(5.111) 
| > 2: &,, = 0. 
Now we turn to the other three equations in (5.107). The first is a scalar with 
respect to rotations: 
0 = Kyy = (2féimr + f E1m)Yim: 
which implies 
fétmst tf réim = 0. 
(5.112) 
The remaining two equations, K,g = K,g = 0, transform as a vector under 
rotations. The divergence of this vector (with respect to the volume of S*) is 
1 
ο = (sin 0K,”) 9 + (sin6K,°) 4 = frm. 
+ “Fim sin6L*(Yim), 
r 
which again implies (for 1 > 0) 
] 
Πιτ 
+S E1m = 0. 
(5.113) 
The remaining equation can be taken to be the divergence of the dual of the 
vector in S?, 
0 = ἆγθφ — Kro,6 = 
η Simr sin OL7(Yim), 
which of course implies 
Sim, = 0. 
(5.114) 
We may conclude that {δημ 77 = — 1, 0, 1} are three arbitrary constants, the 
only contribution from Yj,,. The three equations (5.111) for the unknowns £,,,, 
Nim, and f have the following solution in terms of the arbitrary constants K and 
Vin: 
f = (—Kr’y’, 
(5.115) 
Eun, = V,,(1 —Kr*), 
(5.116)

## Page 207

5.23 Open, closed, and flat universes 
197 
1 
Tim = — m(l --Κνλ)"3. 
(5.117) 
Exercise 5.26 
Verify equations (5.105), (5.108), (5.109), (5.112}, (5.113), (5.114), 
and (5.115-17). 
Exercise 5.27 
Show that the Killing vectors with V,, = 0 are those corresponding to 
the isotropy group of the origin r = 0. 
Exercise 5.28 
Show that the apparent singularity in 7,,, as r > O isa coordinate effect: 
the vector field is well-behaved at the origin. 
Exercise 5.29 
Set K = 0 in (5.115-17) and show that S is just 
E*, Euclidean space. 
Find the constants V,,, that define the Killing vectors {0/d0x, d/dy, 9/97). 
where the Cartesian coordinates are obtained from our polars in the 
usual way. 
5.23 
Open, closed, and flat universes 
We now have a complete description of the geometry of the hom- 
ogeneous and isotropic spaces of the cosmological model: they have the metric 
tensor 
(1—Kr*y' 
0O 
0 
(6η) = 
0 
r? 
O 
|. 
(5.118) 
0 
0 
r?* εἰπ2θ 
It only remains to try to get a picture of this geometry. The following coordi- 
nate transformations are a help. 
Exercise 5.30 
Find a coordinate transformation from r to x which produces the 
following metric components 
for K >0: 
1 
0 
0 
(gi) = k 0 
sin?x 
0 
(5.119a) 
0 
0 
sin?y sin?

## Page 208

Applications in physics: cosmology 
198 
for 
K <0: 
| 
1 
0 
0 
(g;;) =i 0 
sinh*x 
0 
|. 
(5.119b) 
0 
0 
sinh?x sin? 
This shows that the geometry really depends only on the sign of K. Its magni- 
tude serves only as an overall scale factor. 
In the case K > 0, the sphere of radial coordinate χ has area 47 sin?y/K, which 
increases away from x = 0 toa maximum at y = 7/2 and then decreases to zero 
at x = 7. This is reminiscent of S* (figure 5.9). In fact, this is the metric of the 
sphere S° of radius K ~‘/?. Because the space is finite, the universe is said to be 
closed. 
Exercise 5.31 
Find a coordinate transformation of E* from Cartesian coordinates {x’} 
= {w, x,y, 2) to spherical coordinates fF} = tr, x, 9, ¢} in which the 
metric g;; = 6,; has the components g;';' given by (5.119a) when 
restricted to the sphere S°,w2 +x? + y? +27 =K7T. 
The case K = 0 has been considered in exercise 5.29. It is the flat universe. 
The case K < 0 is the open universe, and it is the hardest to visualize. The sur- 
face area of a sphere of radial coordinate y is 47 sinh?x/|K|, and increases ever 
more rapidly with y. This universe is unbounded. 
Exercise 5.32 
(a) By considering the relation between the areas of spheres y = const and 
the distance of the sphere from the origin y = 0, equation (5.101), 
prove that the metric (5.119b) is not the restriction of the Euclidean 
metric to any submanifold of any E”. 
(b) Find a submanifold of Minkowski space whose metric is that of 
(5.119b). 
When Einstein’s equations are supplied with initial data which are homo- 
geneous and isotropic (and this includes not only the geometry but the matter 
variables as well), then the subsequent evolution of the universe maintains the 
symmetry. It follows that the only aspect of the geometry which can change 
with time is the scale factor K: the universe gets ‘larger’ or ‘smaller’ as time goes

## Page 209

5.24 Bibliography 
199 
on. One must be careful, however, not to make coordinate-dependent state- 
ments. For the closed universe, whose total volume is finite, the change in K 
does cause a change in the total volume. But the flat and open universes are both 
infinite, so it is not meaningful to talk about their total volume. What general 
relativity tells us is that the coordinates of equation (5.119) are ‘comoving’: the 
local mean rest frame of the galaxies in any small region of the universe stays at 
constant {x, 0, ¢} as time evolves. It follows then that a change in K produces a 
change in the distance between galaxies, and this is what is meant by an expand- 
ing universe. In the ‘standard model’ of the universe, which assumes homogeneity 
and isotropy and a few other things, all three kinds of universe begin with zero 
‘volume’ (K = 9ο) and expand away from this ‘big bang’. The closed universe 
expands to a maximum and recollapses, the flat universe expands at a rate which 
goes asymptotically to zero, and the open universe expands at a rate which goes 
asymptotically to a nonzero limit. All of these things are consequences of 
Einstein’s equations. To understand these equations it is necessary to add one 
more level of structure to our manifolds: the affine connection. This is the 
subject of chapter 6. 
5.24 
Bibliography 
A concise and well-written introduction to thermodynamics is E. Fermi, 
Thermodynamics (Dover, New York 1956). Caratheodory’s theorem is 
discussed by S. Chandrasekhar, An Introduction to the Study of Stellar 
Structure (Dover, New York, 1958), and at a more advanced level in 
R. Hermann, Differential Geometry and the Calculus of Variations 
(Academic Press, New York, 1968). 
Our discussion of Hamiltonian mechanics follows the spirit of 
R. Abraham & J. E. Marsden, Foundations of Mechanics, 2nd edn. 
(Benjamin/Cummings, Reading, Mass., 1978). An introduction to the 
same ideas without the geometrical point of view may be found in 
H. Goldstein, Classical Mechanics (Addison-Wesley, Reading, Mass., 
1950) or L. D. Landau & E.M. Lifshitz, Mechanics (Pergamon Press, 
London, 1959). The use of the canonical conserved quantities makes 
certain fluid instabilities easier to understand; see J. L. Friedman & 
Β. F. Schutz, Astrophys. J. 221, 937-57 (1978), and 222, 281-96 
(1978). 
A number of useful articles on Hamiltonian mechanics from a 
geometrical viewpoint may be found in Topics in Nonlinear Dynamics 
— A Tribute to Sir Edward Bullard, ed. 5. Jorna (American Institute of 
Physics, 1978: Α.Ι.Ρ. Conference Proceeding no. 46). An interesting use 
of differential forms is the proof of the necessary and sufficient con- 
ditions that a set of dynamical equations possess a Hamiltonian (i.e. 
symplectic) structure, in R. M. Santilli, Foundations of Theoretical 
Mechanics I — The Inverse Problem in Newtonian Mechanics (Springer, 
Berlin, 1978).

## Page 210

Applications in physics: cosmology 
200 
For an introduction to electromagnetic theory which includes a dis- 
cussion of its relativistic version see J. D. Jackson, Classical Electro- 
dynamics (Wiley, New York, 1976). A discussion which extends our 
own is C. W. Misner, K. S. Thorne & J. A. Wheeler, Gravitation 
(Freeman, San Francisco, 1973). An advanced discussion of relativistic 
wave equations is F. G. Friedlander, The Wave Equation on a Curved 
Space-Time (Cambridge University Press, 1976). Wheeler’s ‘charge 
without charge’ is discussed in articles reprinted in 
J. A. Wheeler, Geo- 
metrodynamics (Academic Press, New York, 1962). Sorkin’s nonorient- 
able charge model is described in R. Sorkin, J. Phys. A. 12, 403-21, 
(1979). 
Introduction to fluid dynamics which include discussions of the 
Helmholtz theorem are Fluid Mechanics by L. D. Landau & E.M. 
Lifshitz (Pergamon Press, London, 1959) and Hydrodynamics by 
H. Lamb (Dover, New York, 1975). What we have called Ertel’s theorem 
is really a special case of a more general result derived by H. Ertel, 
Meteorologische Zeitschrift 59, 277 (1942). We touched on the proper- 
ties of the manifold called ‘Galilean spacetime’, which is the arena for 
pre-relativistic physics. Discussions of its structure involve the concept 
of an affine connection, developed in the next chapter. See C. W. 
Misner, K. S. Thorne & J. A. Wheeler, Gravitation (Freeman, San 
Francisco, 1973) for a lucid discussion, or R. Hermann, Topics in 
General Relativity (Math-Sci Press, Brookline, Mass., 1973) for a more 
technical treatment. The use of Lie derivatives in continuum mechanics 
is very fruitful in elasticity theory. Indeed, it is very difficult to formu- 
late the general-relativistic theory of elasticity without such techniques. 
See the treatment by B. Carter & H. Quintana, Proc. Roy. Soc. London, 
A331, 57 (1972), or B. Carter, Proc. Roy. Soc. London, A, to be pub- 
lished. 
Cosmology is treated in most textbooks on general relativity. Our 
approach draws elements from both S. Weinberg, Gravitation and Cos- 
mology (Wiley, New York, 1972), and Misner et al., op. cit. For an 
easier introduction see M. Berry, Principles of Cosmology and Gravi- 
tation (Cambridge University Press, 1977). The astrophysical and obser- 
vational sides of cosmology are dealt with in Weinberg and in P. J. E. 
Peebles, Physical Cosmology (Princeton University Press, 1971). Homo- 
geneous but not necessarily isotropic cosmologies are developed using 
the techniques of group theory in M. P. Ryan & L. C. Shepley, Homo- 
geneous Relativistic Cosmologies (Princeton University Press, 1975).

