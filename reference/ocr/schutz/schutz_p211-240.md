<!-- source-pdf: Bernard F. Schutz-Geometrical Methods in Mathematical Physics-Cambridge University Press (1980).pdf | pages 211-240 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 211–240

## Page 211

6 
CONNECTIONS FOR RIEMANNIAN MANIFOLDS 
AND GAUGE THEORIES 
6.1 
Introduction 
The subject of this chapter is outside the main theme of this book, 
which is the study of the differential structure of the manifold. The affine con- 
nection is an additional piece of structure which gives shape and curvature to a 
manifold; it does not arise naturally from the differential structure, nor is it even 
a tensor. For this reason, the chapter is marked as supplementary. Nevertheless, 
no treatment of differential geometry for physicists would be complete without 
this important and very topical subject. Connections are finding increasing popu- 
larity in physics, particularly in gauge theories in elementary particle physics. We 
shall mainly discuss affine connections (Riemannian manifolds), reserving an 
introductory section on gauge connections for the end. 
In earlier chapters we have occasionally added extra structure to a manifold, 
in that we have singled out a particular tensor field as special, either to serve as 
a volume-element or as a metric. Volume-elements are not far removed from the 
differential structure of the manifold. The metric, on the other hand, creates 
even more structure than the affine connection, as we shall see below. But we 
have been able to avoid all that in our applications, only using the metric in its 
role as a mapping between (4/) tensors and (γι) tensors. The affine connection 
cannot be fitted into the structures we have already developed. From the point 
of view of the differential structure, it is a radical new addition to the manifold, 
and it has correspondingly rich possibilities for physical application. 
6.2 
Parallelism on curved surfaces 
We have repeatedly emphasized that on a differentiable manifold there 
is no intrinsic notion of parallelism between vectors defined at different points. 
The affine connection is a rule whereby some notion of parallelism can be 
defined. To anticipate what kind of a rule may be possible, let us consider the 
notion of parallelism on an ordinary curved two-surface, the sphere. In figure 
6.1, the vector V is the tangent to the great circle ABC at the north pole, point 
A. Suppose we carry, or transport, V along ABC to the south pole, C. In order to 
be defineable in two-dimensional terms it must be Κερί tangent to the sphere, so

## Page 212

Connections: Riemmanian manifolds, gauge theories 
202 
if we do not rotate it as we carry it, it will simply remain tangent to the curve 
ABC. It winds up as V’ at C, pointing in what, to us three-dimensional beings, 
looks like the direction antiparallel to V. Should we assume that, at least with 
respect to the sphere’s geometry, V and V’ are parallel? Before jumping to a con- 
clusion, suppose we transport V from A to C on the path ADC shown in figure 
6.2, where ADC is another great circle intersecting ABC at right angles at both 
poles. Since V starts out perpendicular to ADC, the natural way to move it with- 
out twisting is to keep it perpendicular to ADC and tangent to the sphere. This 
produces the vector V" at C, which, to us, is in fact parallel to V. But V" and 
V',, both vectors at C, are antiparallel! Which is parallel to V2 Clearly, if we 
simply consider the intrinsic properties of the sphere, neither vector deserves to 
be called parallel to V. There is no global notion of parallelism. All one can do 
— and this is what we have done — is to define a notion of parallel transport, of 
moving the vector along a curve without changing its direction. The affine con- 
nection is a rule for parallel transport. 
Fig. 6.1. Parallel transport of a vector V along a great circle of the 
sphere. 
C 
Fig. 6.2. An alternative path for parallel transport, with a different 
result.

## Page 213

6.3 The covariant derivative 
203 
6.3 
The covariant derivative 
We shall for the moment view the affine connection in an abstract sense; 
it will become more concrete when we introduce components in the next section. 
For now, suppose we have a curve @ and a connection, a rule for parallel trans- 
port. Let the tangent to & be U = ἀ[ἀλ. At the point P, pick an arbitrary vector 
V from Tp. Then the connection allows us to define a vector field V along the 
curve &, which is obtained by parallel-transporting V (see figure 6.3). Since we 
can now say that V does not change along Y, we can define a derivative with 
respect to which V has zero rate of change. This is called the covariant derivative 
along U, Vg, and we write 
+ 
VaV = 0 © Vis parallel-transported along 6. 
(6.1) 
If W is a vector field defined everywhere on &, we can define its covariant deriv- 
ative along & in much the same way as we did for Lie derivatives (see figure 6.4). 
To define VW at P, it will be convenient to express all vectors as functions of λ. 
If P has parameter value Xo, then we define the field Wx, .-(A) to be that parallel- 
transported field (VgW* = 0) which equals W at λο + ε. The vector WX .<(Ao) is 
the vector W(Ao + ε) parallel-transported back to Xo. Then the derivative may be 
evaluated entirely in the vector space Tp: 
Wy +6(Ao) _ W(Ao) 
im σσ, 
E70 
€ 
(νο), = 
(6.2) 
Although this procedure resembles the one we used for defining the Lie deriv- 
ative, it is important to understand the significant difference: ‘dragging back’ a 
Fig. 6.3. The affine connection permits us to define V(Q) for any point 
O on © by parallel transport from P. 
€ 
Fig. 6.4. The vector field W on & is not parallel transported. Compari- 
son with one which is permits a definition of the covariant derivative of

## Page 214

Connections: Riemannian manifolds, gauge theories 
204 
vector for the Lie derivative required the entire congruence, so that U and W had 
to be defined in a neighborhood of the curve 6; parallel-transport, by contrast, 
requires only the curve @, the fields U and W on the curve, and of course the 
connection on the curve. 
It is clear from (6.2) that Vg is a differential operator: 
Va(fW) = fVoW+ Wor 
—_ 
_d 
= fVowWt+Ww of 
, 
(6.3a) 
dav 
where the last step is the obvious extension to scalars. The covariant derivative 
can also be extended to tensors of arbitrary type by the Leibniz rules 
+ 
Vo(A @B) = (VGA) OB +A 
(ΝΕ), 
(6.3b) 
+ 
νο(ῶ, 
4) = (Vp, 
A) + (8, Ve). 
(6.3c) 
Equations (6.3) guarantee compatibility of the connection with the differential 
structure. 
Suppose that we were to change the parameter along our curve from A to µ. 
Then the new tangent would be gU, where g = ἀλ/άμ. From (6.2) it is clear that 
the covariant derivative would also be multiplied by g, since ε would be replaced 
by du = εάμ/ἀλ while Wii +5 µ(μο) is the same as Wx κεζλο). (This is, strictly 
speaking, part of the definition of what we mean by a connection: the notion of 
parallel-transport along a curve must be independent of the parameter on the 
curve.) Therefore we conclude that for any function g 
VW = ενσή. 
(6.4a) 
We must also put another restriction on the affine connection, which is that at a 
point the covariant derivatives in different directions should have the additive 
property 
(VoW)p + (VoW)p = (Vou vW)p. 
(6.4b) 
This makes V behave like the ordinary V of Euclidean vector calculus. Together 
(6.4a, b) imply that for any vector fields U, V, W and functions f, g we have 
+ 
VegeevW = fVoW + ew. 
(6.4c) 
Exercise 6.1 
Show that (6.4c) and the fact that VW is a vector imply that VW is a 
(1) tensor field whose value on arguments U and @ is 
VW; U) = (ῶ, VgW). 
(6.5) 
This tensor is called the gradient of W.

## Page 215

6.4 Components: covariant derivatives of the basis 
205 
The fact that VW is a tensor field means that we have been able to remove the 
curve entirely from the definition of the covariant derivative. The tensor VW is 
defined only by W and the connection. One might be tempted to go further and 
say that Vis itself a ({) tensor field which is just the connection; but this would 
be wrong. While V may symbolize the connection, it is not a tensor field, since 
VW fW) #f VW (cf. (6.3a)). For this reason, the connection cannot be regarded 
as a tensor field. 
6.4 
Components: covariant derivatives of the basis 
Since any tensor can be expressed as a linear combination of basis 
tensors, and these basis tensors are all derivable from the vector basis {e,}, the 
connection can be completely described by giving the gradients of the basis 
vectors. So we define 
+ 
Vee; = yep. 
(6.6) 
The functions I, are called Christoffel symbols. For fixed (i, /) Γι is the kth 
component of the vector field Vz,e;. Note carefully the order of the indices on 
I’: the one associated with the derivative goes last. We shall often use the short- 
hand 
Ve, = νι. 
(6.7) 
In an n-dimensional manifold, the n° functions ρα, completely determine the 
affine connection, and this is often the most convenient way of describing the 
connection. Notice that arr is not a component of a tensor; under a basis trans- 
formation the indices Κ and i transform like tensor indices (by (6.5)) but the 
index j does not (by (6.3a)). 
Exercise 6.2 
Show that 
Dey = ARRAY AGT: + AY AWAY), 
where by V,A*; we mean dA*;/dA;, in which 6 = d/dd; and A", is 
treated as a function on the integral curves of e;. 
Exercise 6.3 
Show, by exercise 6.1, that 
[Γόμὲε 8 ὤ] 
is a collection of 
(1) tensors. (Here {G3'} is the one-form basis dual to 
(ej) 
Exercise 6.4 
On the unit sphere the usual spherical coordinates @ and ¢ define the

## Page 216

Connections: Riemannian manifolds, gauge theories 
206 
basis {@p = 0/00, €y = 0/0¢}. Extend the reasoning used in §6.2 to 
deduce that 
I” 49 = — sin ™ cos 0, 1 94 = r 46 = cot 6, 
and all other I's vanish. (Ν.Ο. this is a difficult problem. You should 
make maximum use of the symmetry of the sphere, and make intelligent 
guesses about how vectors behave under parallel transport.) 
Exercise 6.5 
From (6.6) and (6.3c) deduce that 
4 
Vo" = 
— Tj”. 
(6.8) 
Now that we have the derivatives of basis vectors, we can find the derivatives 
of arbitrary tensors. For example, if U = d/dd then 
VaV = U'Vs(V'é;) 
= U'(Vs,V)e; + U'V'Vs.@}. 
In the first term, V’ is simply a function, so U'V,(V’) = dV"/dX. Therefore we 
have 
. 
dvi. 
νο = D 4 + UV'T" 
€, 
Vv 
_ 
= κ. rar Gj. 
To get the final expression we had to redefine some summation indices in the 
final term. Since VV is itself a tensor, it has components 
(WY; = VV’) + DV". 
A word about the term V,(V’). If é; is the vector d/dy, then V,(V’) = dV4/du, 
with V/ simply a function along the curve whose parameter is µ. If δι is a coordi- 
nate basis vector then 6; = 0/dx' and we have 
VV? = ay 
= 
V i, 
using the comma notation introduced for differential forms. It is customary even 
where e; is not a coordinate basis vector to use the comma notation: 
Ve,f = &Lf] =f: 
(6.9) 
on any function f. When e; is a coordinate basis vector, this is the usual partial 
derivative; when e; is not, then this is simply the derivative of f along e;. We can 
thus write 
+ 
(Wy, = νετ = Vy. 
(6.10)

## Page 217

6.5 Torsion 
207 
We have here introduced the semicolon notation for the covariant derivative. 
Whereas neither V? ; nor Τζι V™ transforms like a tensor, their sum clearly 
does. 
Exercise 6.6 
Show that if @ is a one-form 
(V6); ξωιῃ = Wij I" ;wp. 
(6.11) 
Exercise 6.7 
Show that if T is a (47) tensor, 
ο... 
πο... 
_ ey 
νν κ. 
(6.12) 
6.5 
Torsion 
The two quantities [U, V] and Vo V — VoU are both vector fields and 
are both antisymmetric in U and V. A connection is said to be symmetric if they 
are equal: 
+ 
VoV—VoU = [U, V] & symmetric connection. 
(6.13) 
The name ‘symmetric’ is used because of the property proved in the following 
exercise. 
Exercise 6.8 
Show that in a coordinate basis, (6.13) implies that a connection is 
symmetric if and only if 
¢ 
,, = Γή 
(6.14) 
For a nonsymmetric connection we define the torsion T";;: 
-- 
- 
_- 
= 
- 
k 
- 
¢ 
Ve, — Νσιέι — [6]. 6ι] = Τ ji€kr- 
(6.1 5) 
μα 
Exercise 6.9 
Show that {7",;} are the components of a (2) tensor, which we call the 
torsion tensor T: 
Va V —VeU —-[U, V] = TC ;U,Y). 
The empty slot in T is for a one-form argument.

## Page 218

Connections: Riemannian manifolds, gauge theories 
208 
Exercise 6.10 
Suppose a manifold has two connections defined on it, with Christoffel 
symbols I™,; and I'’",,. Show that 
DY, = Γη Γη 
are the components of a (4) tensor. Show that the tensor D is sym- 
metric in its vector arguments if and only if both connections have the 
same torsion tensor. 
Exercises 6.9 and 6.10 show that we can always define the symmetric part Vs) 
of any connection V by defining the Christoffel symbols 
Γου = My — aT y- 
While torsion is in principle a useful part of the connection, it has not had as 
much popularity as the symmetric part in constructing mathematical models for 
physical laws. From now on we will deal with symmetric connections unless 
otherwise specified. One reason for this will be apparent in exercise 6.18 below. 
Notice that the definition (6.13) immediately guarantees the following. 
Exercise 6.11 
A manifold has a symmetric connection. Show that in any expression 
for the components of the Lie derivative of a tensor, all commas can be 
replaced by semicolons. An example: 
(£76); = 
ωι 0) + ωιῦ;; 
= «;.jU? + ωιῦ] α. 
(Naturally, all commas must be changed, not just some.) 
6.6 
Geodesics 
A geodesic curve is a curve that parallel-transports its own tangent 
vector. The geodesic equation is 
+ 
VaU = ο. 
(6.16a) 
If \ is the parameter of the curve and {x7} is any coordinate system, this becomes 
i 
at I;,U'U" = ο, 
(6.16b) 
or 
αχ 
ο dx! dx* 
otra 
a 7 
ore

## Page 219

6.6 Geodesics 
209 
The last equation is a quasi-linear system of differential equations for x'(A), the 
equation of the curve. 
Exercise 6.12 
Recall that our definition of a curve includes its parameter. If λ is a 
parameter for which (6.16c) is true, show that a change of parameter to 
w= artd, 
(6.17) 
where a and b are constants, also gives a solution to (6.16c). The param- 
eter of a geodesic curve is called an affine parameter. 
Notice that only the symmetric part of a connection contributes to the geodesic 
equation. This provides a way of displaying the geometrical effect of torsion. 
Take a geodesic through a point P with tangent vector U. In Τρ choose a linear 
subspace δρ of dimension n — 1 (the manifold’s dimension being n) which is 
linearly independent of U. Pick a vector ἔ in Rp and construct a geodesic 
through P tangent to £. Using the symmetric part of the connection, parallel- 
transport U along £ a small affine parameter distance e. Construct a new geodesic 
through this new point tangent to U there (see figure 6.5). This geodesic will be 
roughly parallel to the first one. In this manner, any point in the neighborhood 
of P can be given a geodesic ‘parallel’ to U. Along this congruence of geodesics 
we can transport the original ‘linking’ vector £ in two ways, either by parallel- 
transport or by Lie dragging. Let £ be parallel-transported. Then by (6.15) we 
have 
(Lg) = —(VgU)'— ΤΕ”. 
The initial vector £, however, had the property that VigyzU = 0, so that (Vz Uy 
= ΣΤΙΣ initially. Therefore we have the initial value 
(458)! = —2T',8U". 
Fig. 6.5. Two parallel geodesics U and U’ and the vector ἕ which con- 
nects them in the plane Ap and is parallel-transported along U. If there 
is torsion it rotates away from U’.

## Page 220

Connections: Riemannian manifolds, gauge theories 
210 
What this means is that a vector ἕ parallel-transported by a symmetric connection 
would stay ‘attached’ to the parallel congruence of geodesics we have con- 
structed. But if the connection is not symmetric, the vector does not remain 
fixed in this congruence. Speaking loosely, it is ‘rotated’ relative to nearby geo- 
desics by the action of torsion. Conversely, if we regard the parallel-transported 
vector ἕ as defining a ‘fixed’ direction as it moves along, then the congruence of 
‘parallel’ geodesics twists around the one carrying £. (One cannot, however, 
define precisely the notions of ‘rotation’ and ‘twist’ without a metric.) 
6.7 
Normal coordinates 
It will be helpful below to use a coordinate system based on geodesics. 
To construct this, we note that the geodesic curves through a point P give a 1-1 
mapping of a neighborhood of P onto a neighborhood of the origin of Tp. This 
map arises because each element of Tp defines a unique geodesic curve through 
P,so we can associate the vector in Tp with the point an affine parameter dis- 
tance Ad = 1 along the curve from P. (Recall that if two elements of Tp are 
parallel, their geodesic curves have the same path but different parameters, and 
so the map picks out different points along the path.) Using this map and choos- 
ing an arbitrary basis for Tp, one defines the normal coordinates of a point Q to 
be the components of the vector in Tp it is associated with. This map will 
generally be 1-1 only in some neighborhood of P, since geodesics may cross on a 
curved manifold. For some connections, such as that of flat space, the map is 
1-1 over the entire manifold. (The map from Tp to the manifold is well-defined 
even if geodesics cross. It is called the exponential map. If it is defined for all 
elements of Tp at all points P then the manifold is said to be geodesically com- 
plete.) For our purposes the principal interest in the normal coordinates is that 
I"; = 0 at P (but not elsewhere in the neighborhood of P). To see this, note 
that if a vector U with components U'(P) defines a geodesic curve, then the 
coordinates of the point with affine parameter λ along that curve are simply 
x' = \U'(P), with the convention that \ = 0 at P. Therefore d2x'/d? vanishes, 
and (6.16c) tells us that I’,,U (P)U'(P) must vanish along the whole curve. At 
P, however, U’ had an arbitrary direction, which means that I’;,,(P) = 0. 
The fact that it is always possible to choose a coordinate system to make Γι, 
vanish at a point will be of great help in proving several theorems below. Since it 
is not necessary for ly to vanish anywhere else, the derivatives of in at 
Pdo 
not vanish. 
6.8 
Riemann tensor 
One might expect that the commutator of two convariant derivatives, 
[Va, νν] = VaVo — WVa.

## Page 221

6.8 Riemann tensor 
211 
should be a differential operator. In fact, however, it has the following remark- 
able property: the operator R, defined by 
¢ 
[νο. Vel — Viea,71 = RU, V), 
(6.18) 
is a multiplicative operator. Even more remarkably, R does not depend on deriv- 
atives of U and V either. These properties are explained and proved in the 
following exercise. 
Exercise 6.13 
Prove, for an arbitrary function f, that 
(a) 
R(U, V)fW = fR(U, VW, 
(b) 
R(fU, V)W = fR(U, ΤΙ’. 
Because of these properties, (6.18) actually defines a tensor, which is called the 
Riemann tensor. Given vectors U, V, (6.18) shows that R(U, V) is a (1) tensor, 
since the left-hand side operates on a vector to give a new vector. With U and V 
also regarded as variable arguments, the Riemann tensor becomes a (4) tensor. 
(N.b. the conventions used for defining the Riemann tensor, (6.18) and (6.19), 
are by no means universal. Other definitions may differ in sign and the ordering 
of arguments. When consulting other books, make sure you find what conven- 
tion is being used. We follow Misner, Thorne & Wheeler (1973).) 
Exercise 6.14 
The components of the Riemann tensor, R' ip); are defined by 
[νι, Vile — Viz,.e1@r = R'nijer- 
(6.19) 
(a) Show that in a coordinate basis 
4 
Reg 
Τι ΠΕ Τί ΤΠ ην. 
(6.20) 
(b) In a noncoordinate basis define the commutation coefficients Clin by 
le;, e,| — C' ip 
ej. 
(6.21) 
Show that 
Reg 
Τρι 
nig TOM Γι 
my — Cy em: 
(6.22) 
where 
f ; 
=e;[f]. 
(c) Show that 
Κι = (δη +R 
ei) = 0, 
(6.23a) 
and 
Κιμ = 0. 
(6.230)

## Page 222

Connections: Riemannian manifolds, gauge theories 
212 
(Hint: for (6.23b), use normal coordinates. The result, of course, is 
independent of the basis.) 
(d) Using (c) show that in an n-dimensional manifold, the number of 
linearly independent components of R' nij is 
7” πα τι) 
μα 
1-2) _ 
4 
5 
n 
31 
$n?*(n? — 1). 
(6.24) 
Exercise 6.15 
Show that 
R' 
etijzmy = 0. 
(6.25) 
These are called the Bianchi identities. (Hint: again work in normal 
coordinates.) Show that this result is equivalent in a coordinate basis to 
the Jacobi identity for covariant derivatives 
[νι [νι] + (Vj. νε Vil] + (Ve. [Vis Vil] = 0. 
Cf. equations (2.14) and (3.9). 
6.9 
Geometric interpretation of the Riemann tensor 
Like the interpretation of the other commutator we have studied, 
[U, V], this involves a closed or almost-closed loop. Our approach will be based 
upon the exponentiation of the covariant derivative, and so will closely parallel 
that for the Lie bracket. If a vector field A is defined along a curve whose tangent 
is U, then parallel-transport permits us to bring A from any point Q on the curve 
to any other point P. The vector so produced, A(Q > P) in Tp (not in general 
equal to A{P)) is called the image at P of A(Q), and it depends of course on the 
curve. In fact, if A and U are analytic we can write the Taylor series 
4(0 -») = A(P)+AVGA(P) + HE VGVGA(P) +... 
exp [AVg]Alp, 
(6.26) 
where λ is the curve’s parameter (U = d/d)) and the ‘exp’ notation is again just a 
shorthand for the line above it. 
Now consider two congruences with tangents U = d/dd and V = d/du, for 
which [U, V] = 0. Their intersections therefore form closed loops, as shown in 
figure 6.6. If we parallel-transport a vector from some point R to Q along a curve 
V as shown, we thereby define a vector at 0 
A(R >Q) = εχρ[μνν]ά!ο. 
where µ is the parameter distance from Ο to R. If we then parallel-transport the 
resulting vector from Q to P, we get at Pa vector we call 
A(R >Q>P) = exp [AVa] exp [μνν]41,, 
|

## Page 223

6.9 Geometric interpretation of the Riemann tensor 
213 
where λ is the parameter distance from P to Q. We could have done the trans- 
porting another way, namely by first going to S (a distance λ along a U-curve) 
and then to P (a distance µ along a V-curve). The values of \ and ware the same 
as above because U and V commute. The second method would produce 
A(R >S->P) = exp [uVy] exp [AVgJAlp. 
Their difference, which we shall call &4, can be found for small λ and µ by using 
the Taylor expansion: 
6A = [εἣ" Ὁ HY] A 
= [1 Ελνς ΓΣλ2νονς. 
1LtuVe + ou°WWIlA + OG), 
where O(3) means terms in ”\”", where n + m 2 3. Evaluating this gives 
5A = du[Vo. WIA + Ο(3), 
(6.27) 
which is of course just the Riemann tensor, and does not involve derivatives of 
A. Viewed another way, this is the change in A that would be produced if we 
were to parallel-transport it around the loop PORSP. This change is just the 
Riemann tensor times the ‘area’ of the loop, Au: 
SA! = wR ip, AlUPV!. 
Another important geometrical aspect of the Riemann tensor involves geo- 
desic deviation, the fact that geodesics begun parallel do not stay parallel. To 
measure this precisely, we consider a congruence of geodesics with tangent U 
(νο 
ῦ = 0), and a connecting vector £ which is Lie dragged by the congruence 
(£& = 0) (see figure 6.7). The manner in which ἕ changes along U will be our 
measure of geodesic deviation. Its first derivative, Vg, depends upon initial con- 
ditions, upon whether the geodesics are set up initially parallel or not. The geom- 
etry enters into the second derivative Vi Va£, which tells how the initial rate of 
separation of the geodesics changes. So we have 
Fig. 6.6. Parallel transport around a closed loop generally does not 
return the same vector as it began with.

## Page 224

Connections: Riemannian manifolds, gauge theories 
214 
νονσξ = Vo(faé + νεῦ) 
= VaVeU 
[νο. Ve]JU + νενσῦ. 
The first step used exercise 6.11. The last term in the last line vanishes because 
U is a geodesic, so we have 
νρνσξὲ = R(U, 2)U, 
(6.28a) 
or in component form 
(&.jU).U" = Rij U'U"E'. 
Notice that the left-hand side can be simplified because U’ ,,U" = 0, and so we 
get 
εἰ UU" —_ κι". 
(6.250) 
Equation (6.28) is called the equation of geodesic deviation. 
6.10 
Flat spaces 
Euclid’s axiom that parallel lines when extended never meet is the 
defining axiom for a flat space. From (6.28) it is clear that this means that a 
space is flat if and only if the Riemann tensor vanishes. Thus, the Riemann 
tensor is the measure of the curvature of a manifold with a connection. A flat 
space, by (6.27), has a global notion of parallelism: a vector at point R can be 
said to be parallel to one at P, because it can be parallel-transported to Pina 
manner independent of the path. Thus in a flat space all tangent spaces Tp may 
be identified with each other. Moreover, the exponential map is extendible 
indefinitely (provided the manifold’s global topology is not artificially compli- 
cated by ‘cutting and pasting’) and the entire manifold may be identified with its 
tangent space. Notice that none of this requires a metric tensor. Minkowski 
space is just as flat as Euclidean space. 
Fig. 6.7. A connecting vector ἕ Lie dragged along a geodesic congruence.

## Page 225

6.11 Compatibility of connection with volume-measure 
215 
Exercise 6.16 
Consider a two-dimensional flat space with Cartesian coordinates x, y 
and polar coordinates r, 0. 
(a) Use the fact that e, and e, are globally parallel vector fields (e,.(P) is 
parallel to é,.(Q) for arbitrary P, Q) to show that 
Mog = —7, 
Ing = Τζο = Ir, 
and all other I's are zero in polar coordinates. 
(b) For an arbitrary vector field V, evaluate V;V’ and V;V' for polar coordi- 
nates in terms of the components V" and V®. 
(ο) For the basis f = 0/dr, θΞ (1/9)9/9θ find all the Christoffel symbols. 
(d) Same as (b) for the basis in (c). 
This exercise makes the important point that, although on a flat manifold 
coordinates exist in which a = 0 everywhere, it is possible to choose coordi- 
nates in which they do not vanish. 
6.11 
Compatibility of the connection with the volume-measure or the metric 
If a manifold has not only a connection but also a volume form or a 
metric, one usually makes certain compatibility demands. For example, both the 
connection and the volume-form can define the divergence of a vector field V. 
The covariant divergence is 
V- V=V;V’. The volume-form divergence is defined 
by 
. 
{ὀφῶ = (ἀναογ)ῷ. 
We say that V and ὤ are compatible if divs V = V~ 
V 
for all V. 
Exercise 6.17 
(a) Show that V and 
are compatible if and only if νῶ = 0. (Hint: use 
exercise 6.11 to evaluate £7.) 
(b) In coordinates (x',...,x”) suppose w4._, =f. Show that Vand & 
are compatible if and only if for all k 
(Inf), = ip: 
In a similar way, there is a natural compatibility demand if the manifold has a 
metric tensor g]. Two vectors A and B have the inner product g|(A,B) at a point 
P.We say that V and Οἱ are compatible if this inner product is preserved by 
parallel-transport of A and B along any curve, for any vectors A and B.

## Page 226

(a) 
(b) 
Connections: Riemannian manifolds, gauge theories 
216 
Exercise 6.18 
Show that V and gj are compatible if and only if 
Vg| = 0. 
(6.29) 
In coordinates (x’,...,x”} show that V and gj are compatible if and 
only if 
Γι = ΣΕ (ευ Έξι) — Sin,v- 
(6.30) 
Here g” are the elements of the matrix inverse to the matrix of compo- 
nents g;,, (cf. equation 2.55)). (Hint: use the symmetry lip = Γι.) 
Exercise 6.19 
Recall that exercise 4.13 enables one to define a preferred volume-form 
if one has a metric. (This is another compatibility, that of the metric 
and volume-form). Show that if the metric and connection are com- 
patible, then the preferred volume-form and the connection are com- 
patible. (Hint: you will have to show that g;, = gi 'g:; ,. Use equation 
(4.39) for this purpose.) 
Equation (6.30) shows the remarkable fact that a metric actually determines 
the compatible symmetric connection uniquely. Such a connection is called a 
metric connection. 
6.12 
Exercise 6.20 
Show that for an arbitrary vector V 
(L790) = ViVi+ ViVi. 
Therefore a Killing vector (cf. 53.11) obeys Killing’s equation 
ViV; + Vj V; =(. 
Cf. equation (5.89). 
Metric connections 
Because (6.30) is such a strong constraint on the connection, metric 
connections have additional properties that general symmetric connections do 
not. To derive some of them it is easiest to work in a normal coordinate system. 
Notice that (6.29) and (6.30) imply 
i, = OatP>8imn = OatP. 
(6.31)

## Page 227

6.12 Metric connections 
217 
Exercise 6.21 
Show that (6.20), (6.30), and (6.31) imply that in normal coordinates 
at a point P 
Κυ = δι 
in = 2 (Bit, 
jx — Bir, jt δι δν). 
(6.32) 
Exercise 6.22 
(a) Show that (6.32) implies the identity 
Άι = Reniy- 
(6.33) 
(b) Show that (6.33) and (6.23) imply that in an n-dimensional manifold 
the number of linearly independent components of Κυ is 
gn(n — 1)\(n? —n + 2) -- n(n —1)(n—2)n—-3) = τη (12 -- 1). 
Exercise 6.23 
(a) Define the tensor R,,, called the Ricci tensor, by 
Re = R' ni, 
(6.34) 
and the Ricci scalar R by 
κ = ο κι. 
(6.35) 
Show that R;; is symmetric. 
(b) Show that the contracted Bianchi identities 
Ειναι = 0 
and 
ϱ) ην = 0 
imply 
(R" —43Re")., = 0. 
(6.36) 
(Raising indices on R” is accomplished by the metric: RY = ο 
σκι) 
Define the Weyl tensor: 
C8 = Ry, — 25 Ry + 56h, OR. 
(637) 
Show that every contraction between indices of (μι gives zero: it is a 
‘pure’ fourth rank tensor. 
oo 
Ωω — 
Equation (6.36) plays a fundamental role in Einstein’s theory of gravitation 
(general relativity). Spacetime is represented as a four-dimensional manifold with 
metric, a generalization of flat Minkowski spacetime. The empty-space (source- 
free) gravitational field (i.e. metric) is found by solving the differential equations 
GY = R¥—iRg" = 0, 
(6.38) 
where G¥ is called the Einstein tensor. The identities (6.36) reduce the number 
of independent equations in (6.38) from 10 (=4n(n + 1) because G” is sym- 
metric) to 6. This guarantees that the solution, g;;, which also has 10 independent

## Page 228

Connections: Riemannian manifolds, gauge theories 
218 
components, is determined only up to the four functional degrees of freedom 
represented by the coordinate transformations of g;;. 
Exercise 6.24 
Show that a geodesic joining points P and Q is a curve of extremal 
length among all curves joining P and Q. Do this by showing that 
Q 
1/2 
|, | 
is unchanged to first order by changes in χ(λ) away from a geodesic 
curve. (Bear in mind that any curve has a unique parameter; a geodesic 
curve’s parameter must be affine.) Discuss the need for the absolute 
value signs above if the metric is indefinite, and in particular discuss 
separately the case of a null geodesic (length zero). 
6.13 
The affine connection and the equivalence principle 
We all learned our basic geometry and physics by studying flat mani- 
folds: Euclidean three-space, Galilean spacetime (though it probably was not 
given that name) and later (if at all), Minkowski spacetime. General relativity, on 
the other hand, uses a curved spacetime. It seems natural to think of a flat space 
as the simplest kind of space. But from the point of view of manifold theory, 
even a flat space is by no means simple: it has far more structure than the ordin- 
ary differentiable manifold, for it has an affine connection. The existence of this 
connection does not intrude into elementary geometry and physics, because one 
usually adopts rectangular coordinates, in which the Christoffel symbols vanish. 
But if the physical laws are framed in flat space using curvilinear coordinates, 
then the Christoffel symbols must be used, and the connection becomes visible. 
It may seem that this is a complication to be avoided, but consider its potential 
for generalization. Most physical laws written in this way involve the Christoffel 
symbols but not the Riemann tensor, so their equations are meaningful — 
identical — whether the manifold is flat or curved. It is therefore natural to 
postulate that in the curved spacetime of general relativity the laws of physics 
have exactly the same mathematical form as they have in a curved coordinate 
system in the flat spacetime of Minkowski space. This is called the principle of 
minimal coupling (of physical fields to the curvature of spacetime), or the strong 
principle of equivalence. It is a postulate, widely adopted, which is consistent 
with experiment. A full discussion of it can be found in Misner et al. (1973). The 
point that needs to be exphasized here is the rather remarkable circumstance 
that, by expressing the flat-space laws of physics in a curved coordinate system,

## Page 229

6.14 Connections and gauge theories 
219 
one obtains the curved-space form of the laws. This circumstance can be traced 
to the fact that flat space, though having zero curvature, has a perfectly definite 
connection and is therefore only a special kind of ‘curved’ space. 
6.14 
Connections and gauge theories: the example of electromagnetism 
‘Gauge theories’ is the collective name for a large variety of theories of 
elementary particle interactions, all of which share one feature: invariance of 
their physical predictions under a group of transformations of the basic variables 
of the field theory. Electromagnetism is the best-known example: if the basic 
variable is taken to be the one-form (‘vector’) potential A, then the physical pre- 
dictions of the theory are invariant under the gauge transformation A>xAt df. 
The word ‘gauge’ is applied by analogy to the transformations of all these 
theories. A general discussion of gauge theories is beyond our scope (see the 
lectures by Trautman (1973) in the bibliography). We will confine our remarks 
to electromagnetism, illustrated with the equation for a charged particle of mass 
m and zero spin. We will see that a connection different from but in the same 
spirit as the affine connection arises in a natural way and in particular leads us to 
‘invent’ the electromagnetic field! 
Consider first the neutral scalar particle of mass m whose wave-function ψ 
obeys the Klein—Gordon equation and the (conserved) normalization condition 
(V, 
V4 —m)y = 0, | 
d3x(y*y —yw*) = 1, 
(6.39) 
where Greek indices run over (t,x, y, Z), and where we assume for simplicity the 
metric of Minkowski spacetime. Clearly, if ψ is a solution then so is We'®, where 
ϕ is any real constant. This is a gauge transformation: 
> We!?. We shall now 
make an analogy which will carry through our whole discussion. The gauge trans- 
formations are of a very restricted sort, since ¢ cannot depend on position. This 
is analogous to the coordinate-freedom in the description of some (any) physical 
system in rectangular coordinates in special relativity. The permissible coordinate 
transformations are the rotations, Lorentz boosts, and translations, and these 
are all rigid: one cannot make one transformation at one point and a different 
one somewhere else. Relaxing this restriction in special relativity in order to per- 
mit arbitrary coordinates forces one, as we have seen in the last section, to intro- 
duce the affine connection in order to preserve a coordinate-independent deriv- 
ative, the covariant derivative. Once the equations of motion of the physical sys- 
tem are written down with a connection in them, it is natural to use them when 
the connection is not flat. These turn out to be the appropriate equations for 
that system in general relativity. This procedure of generalizing the coordinate 
freedom thus leads to a theory of the way the system interacts with a

## Page 230

Connections: Riemannian manifolds, gauge theories 
220 
gravitational field. In a similar manner, we will now generalize the gauge freedom 
of the field y and find, automatically, a theory for how the field interacts with 
electromagnetism. 
The generalization is obvious: we would like a general gauge transformation 
y> per | 
(6.40) 
where now ¢ is an arbitrary real function of position X in Minkowski spacetime. 
But because the field equations involve derivatives, this produces a change 
dy > (dw +ivddjei?™, 
(6.41) 
To see how to eliminate this extra term, let us look at the situation more geo- 
metrically. The factor e'® is a complex number on the unit circle; the gauge 
transformation is a representation of the action of the group U(1) (unitary group 
in one complex dimension) on wW. So the transformation y > wei? can be 
thought of as picking out an element of U(1) at each ¥ and allowing it to act on 
y. The natural geometrical structure here is the fiber bundle, whose base manifold 
is Minkowski spacetime and whose fibers are the group U(1) (which can be visual- 
ized as the unit circle in the complex plane). A gauge transformation (6.40) is 
then a cross-section of the fiber bundle. We shall call this bundle the U(1 )-bundle. 
Now, the thing we want to look at is not y itself but V,,W, which at any point 
P is an element of 7” p, the vector space of one-forms at P. Consider a curve & 
with parameter A in the base manifold. As we move along the curve we encounter 
a sequence of one-forms dy, one at each point. If ψ satisfies the Klein-Gordon 
equation, (6.39), we will say that dy changes along @ in the ‘correct’ manner. 
There is a restricted set of gauge transformations (¢ = const) for which the new 
dy is also ‘correct’. Suppose we make an arbitrary gauge transformation. Then 
to the curve @ in the base manifold there corresponds a curve #* in the U(1)- 
bundle which passes through each fiber above a point of @ at the point on the 
fiber (element of U(1)) which corresponds to the gauge transformation at that 
point of @. If this transformation is not constant (if 
* is not ‘parallel’ to ¥) 
then the gradient of the transformed wy will not be ‘correct’: it will not equal, to 
within a phase, that of the original ψΨ. So we will define a connection one-form 
A on the base manifold, which will depend upon the curve 
* in such a way as 
to correct the derivative of y. The definition is: 
(i) If ψ solves (6.39) then A = 0. 
(ii) Under a transformation y > we’? the connection one-form trans- 
forms as 
4-4 + do. 
(6.42) 
(iii) The gauge-covariant derivative of w is 
Dy = dy —iWA. 
(6.43)

## Page 231

6.14 Connections and gauge theories 
221 
Properties (ii) and, (iii) mean that 
DW changes, under a gauge transformation, to 
el © Dy - property (i) guarantees that Dw is ‘correct’ on &. 
Let us now understand why A is called a connection. The affine connection is 
represented by the Christoffel symbols, which are added to the ordinary partial 
derivative in order to give a ‘correct’ derivative: one which gives parallel trans- 
port (cf. (6.43) with (6.10)). In order to preserve the ‘correctness’ of the deriv- 
ative, the Christoffel symbols must transform under a coordinate change in a 
manner which depends on the coordinate change (exercise 6.2) in a way very 
similar to the way A changes under a gauge transformation (6.42). The differ- 
ence between the connections is what they set out to preserve: an affine con- 
nection preserves parallelism; our one-form connection preserves the gradient 
under a gauge transformation. 
We can now write the gauge-covariant form of the Klein—Gordon equation: 
D,D*y—m>y = (Vz —iA, (V4 —iA*)y —m? yp = 0. 
(6.44) 
This equation reduces to the usual Klein-Gordon equation if the phase of ψ is 
‘correct’; and any ψ obtained by an arbitrary gauge transformation of a ‘correct’ 
W solves (6.44). 
The curvature tensor of an affine connection can be defined in a coordinate 
system by an equation like (6.18): 
[Vu WIV* = κιν”. 
The analogue here is 
μμ. Ὀν]ψ = Fury. 
(6.45) 
It is a straightforward calculation to show that the gauge-curvature two-form F 
whose components are ἔμν is simply 
F = —idA. 
(6.46) 
Clearly F is gauge-invariant (cf. (ii) above). (The Riemann tensor was coordinate- 
invariant.) The Klein—Gordon equation is gauge-flat (F = 0) because there exists 
a gauge in which A = 0. But because of the obvious analogy with electromagnet- 
ism (A = one-form potential, if’ = Faraday tensor: see chapter 5), it is clearly 
tempting to regard (6.44) as a generalization of the Klein-Gordon equation to 
the case where the particle has charge and interacts with an external electromag- 
netic field F. This is in fact correct, and (6.44) can be derived more directly 
from the fact that the canonical momentum of a classical particle in an external 
electromagnetic field is ῥ. = p + (q/c)A, where ῥ is the ‘true’ four-momentum 
of the particle. By the correspondence principle the equation p -p επι = 0 
becomes (in units where A = c = 1) 
(—iV, Αμ iV" —qA*")+m’*y = 0. 
This shows us that (6.44) is the wave equation for such a particle with charge

## Page 232

Connections: Riemannian manifolds, gauge theories 
222 
4 = 1. We can summarize what we have learned in the following way: a scalar 
particle of mass m and charge q in the presence of an external electromagnetic 
field with one-form potential A obeys the equation 
(V, —igA,(V" —igA")y —m’?yp = 0. 
(6.47) 
A gauge-transformation consists of the following: 
A>A+ 
dg, 
(6.48a) 
Wy > peiela, 
(6.48b) 
We can regard A as a connection on the U(1)-bundle and F as its curvature. 
Exercise 6.25 
(a) Verify that 
Dy > e®™ 
Dy under a gauge transformation. 
(b) Verify (6.46). 
6.15 
Bibliography 
A very complete reference for Riemannian geometry is S. Kobayashi & 
K. Nomizu, Foundations of Differential Geometry, two volumes (Inter- 
science, New York, 1963 and 1969). 
Good modern introductions to pseudo-Riemannian geometry (a 
metric connection with an indefinite metric) are in Gravitation by C. W. 
Misner, K. S. Thorne & J. A. Wheeler (Freeman, San Francisco, 1973); 
The Large-Scale Structure of Space-Time, by ο. W. Hawking & σα. F. R. 
Ellis (Cambridge University Press, 1973); and Gravitation and Cos- 
mology, by S. Weinberg (Wiley, New York, 1972). 
A more complete exposition on the role of connections in gauge 
theories is A. Trautman, Infinitesimal connections in physics, in the 
Proceedings of the International Symposium on New Mathematical 
Methods in Physics, ed. K. Bleuler & A. Reetz (Bonn, 1973). See also 
R. Hermann, Vector Bundles in Mathematical Physics, two volumes 
(Benjamin, Reading, Mass., 1970). For a ‘physicist’s’ description of 
gauge theories see J. 
C. Taylor, Gauge Theories of the Weak Inter- 
actions (Cambridge University Press, 1976). 
A mathematical discussion 
of connections in their wider meaning can be found in Y. Choquet- 
Bruhat, C. Dewitt-Morette & M. Dillard-Bleick, Analysis, Manifolds, and 
Physics (North-Holland, Amsterdam, 1977). Connections on fiber 
bundles are reviewed in B. Carter, Underlying mathematical structures 
of classical gravitation theory, in Recent Developments in Gravitation, 
ed. M. Levy & S. Deser (Plenum, New York, 1979). 
There are many other topics one can study once one has introduced 
the affine connection. For example, Lie groups have a natural affine 
connection which makes the one-parameter subgroups into geodesics in 
the group manifold. This construction is explored in a step-by-step 
fashion in a number of exercises in Misner et al., op. cit.

## Page 233

6.15 Bibliography 
223 
Torsion may play a role in gravitation, a suggestion first made by 
Cartan. The Einstein—Cartan theory of gravitation has received con- 
siderable attention lately: see A. Trautman, Bull. de l’Academie 
Polonaises des Sciences (math., astr., phys.) 20, 185-90 (1972). 
The Riemann tensor is not an easy tensor to calculate from a know- 
ledge of the metric tensor’s components. The task is made somewhat 
easier by Cartan’s method of moving frames, which makes use of the 
calculus of differential forms. See Misner et al., op. cit. 
Although we have not considered it, the differential geometry of 
complex manifolds is interesting and may play a large role in future 
physical applications. For an introduction aimed at physicists, see Ε. J. 
Flahery, Hermitian and Kahlerian Geometry in Relativity (Springer, 
Berlin, 1976). A standard mathematical reference is S. S. Chern, Com- 
plex Manifolds Without Potential Theory (D. Van Nostrand, New York, 
1967).

## Page 234

2.1 
2.2(b) 
2.3 
2.4 
2.5(a) 
2.6 
2.7 
2.8 
APPENDIX: SOLUTIONS AND HINTS FOR 
SELECTED EXERCISES 
[7,6] = —6/r#0. 
Since ad/dA + bd/du = bd/du + ad/dd, equation (2.13) implies 
exp [ad/dA] exp [bd/du] = exp [2ά/άμ] exp [ad/dA], which certainly 
implies [d/dA, d/du] = 0. Conversely, if the order of d/dA and d/du on 
the right-hand side of (2.13) does not matter, then they may be mani- 
pulated exactly as real numbers, for which (2.13) is true. 
Expand out each term, e.g. [[X¥, Y], Z] =X YZ — YXZ — ZXY 
+ ZYX. Each such term is to be interpreted as a differential operator 
on functions. The 67 requirement guarantees each term exists. When all 
three terms in (2.14) are so expanded, the result follows. 
Each matrix is a (}) tensor requiring one vector and one one-form to 
give a real number. Since there are two matrices involved, transfor- 
mation can produce a number when supplied with two vectors and two 
one-forms. Linearity is easy to check. 
In n dimensions a (2) tensor has n? independent components, while 
two vectors have between them only 2n components. In general this is 
inadequate. 
A linear combination of two (0) tensors is defined in terms of their 
values on arbitrary one-forms ῥ and J: (ah + Br) (5. J) = ah (5, J) 
+ Br (B, ᾷ). This is still a linear function of pf and ἆ, and so is a (4) 
tensor. The zero tensor has value zero on any pf and q, and the other 
axioms are also obvious. The space has n? dimensions because each 
tensor his completely defined by its n? components h(&', @/) = h", 
The n? tensors {ξι ® é;} are a basis because they are linearly indepen- 
dent: the linear combination βὗ δι ® é; vanishes if and only if all BY 
vanish, as can be seen by allowing the tensor to operate on all pairs of 
basis one-forms. In fact it is easy to verify that h = μη €; QE}. 
Six. Six. 
Linearity: C(aV + DW) = B(A(@V + DW)) = B@A(V) + DA(W)), 
aB(A(V )) + DBB(A(W)) = aC(V) + bC(W). 
Components: if A(é;) = A*.é, then C(é;) = B(A*.é,) = B(é, λα”, 
= B',A®, é;, from which the result follows.

## Page 235

2.9 
2.10 
2.11 
2.12 
2.13 
2.14 
2.15 
2.16 
3.1 
Appendix: Solutions and hints 
225 
Each (1) tensor is a linear transformation of Tp. Our result shows that 
linear transformations form a group under the operation of composi- 
tion (by which C was produced from A and B). 
τ(ῶ", a 
d= TAS 
20" JN, 6) = A! Nw 17 (@*", &!). This generalizes 
to Ti 
=A 
ΔΙ ‘My AMY T™ Fs, , where 
(ii... nhs 
are 5 N indices and α a 1 are N’ indices. 
True of any vector space: the zero element is unique. 
The value of the tensor (in the original basis) on a one- form p and a 
vector V is A?,V'p;. In the new basis it is At, ye p;' = (A',AS;'A’,) 
δι, V®) (A!.:p)), where we have used the transformed components 
of everything. Doing the sums oni’ andj’ first and using (2.34) gives 
that the new value is the same as the old, i.e. that the rule gives a real 
number associated with the vector and one-form, independent of the 
basis. 
@) A= εν 12 
1 
produces the canonical form 
0 
6 
ΙΝ2 
i): 
_{ 
IN2 
12 
| 
-1 
0 
(b)A = [_ 
67 
va produces the canonical form | 
0 η 
(ο A= 
° M2 
produces the canonical form Γ a 
a 
(a) The transformation law 
can be deduced from equation (2.55). As 
function of one-forms, | :(δ, 7) = 9\(P, J) leads to (2.55) and 
clearly shows the linearity property. 
(b) In such a basis, the metric has components + 6,;, so ϐϱἱ ' has compo- 
nents + 5” as well, being just the inverse matrix. 
Make a Taylor expansion of 6η and ΛΙ, about P. Try to satisfy (i) and 
(ii) by choosing the coefficients of the ΔΙ, expansion appropriately for 
arbitrary coefficients of the g;; expansion. Show, by counting the 
number of coefficients, that (i}-(iii) hold. Remember that not all OAt,/ 
ax” at P are independent, since Ai = 
= dx!/ax/ implies dA‘ /οχ 
= ΛΙ, fax? 
(a) Sr = 1,879 =0, 299 =r’. 
(0) orthonormal. # = 0/dr, ΘΞ 1 9/90. 
(a) df has components (0f/0r, 0f/30); df has components (9//97, r°? 
of/00@). 
(b) On the orthonormal basis, both df and df have components (9//9Υ, 
r‘of/de). 
(a) On functions, equation (3.3) shows that each side of (3.8) reduces 
to the operator [V, W]. On a vector field U, equation (3.6) gives

## Page 236

3.2(b) 
3.3 
3.4 
3.5 
3.6 
3.7 
3.8 
3.9 
Appendix: Solutions and hints 
226 
the left-hand side as [V, [W, U]] — [W, [V, U]] and the right- 
hand side as [[V, W], U]. The Jacobi identity (exercise 2.3) and 
the antisymmetry of the Lie bracket establish the result. 
(b) On functions, we have the Jacobi identity (2.14) again. On vectors, 
equation (3.8) converts (3.9) into the Lie derivative with respect to 
(LY, ¥],Z] + ([¥,Z], 
Χ] + [[Z, X], Y], which vanishes. 
£5U = εν(ύῖε) = (£pU')e, + U' Eve; = [Vi2,(U)) 2, 
εν) = [V2(U!) — Ul2,V]é;— U"V' £5, 
2; 
The last step required relabelling of indices. Use of (3.7) in the last term 
produces the desired result. 
Follows from (2.7) with V? = 6',. 
From (3.13) we have 
~ 
3 
| 
8, 
δ., 
ανν) Va 
eo( Mw wor 
[v2 
9 wrt ωμτν] wi 
ax! 
J Ox! 
2 
where indices have been relabelled in the second term. The arbitrariness 
of W' gives the result. 
(a) 
_ 
_ 
. 
_ 
ΣαωωιΣ βω4(ω | = 2, [αω δω, βω)Α)] 
a 
a, 
= Σ, {αωβω[άω. Ae] + ew [4@Bey)] 
Ae 
a,b 
— By [A@@@)] 4@} - 
oo 
ὂ 
. 
(LoT) Rn 
= VG ΤΙ" ορ 
wed Tg, wd aoe 
, 
ὃ 
a 
ὃ 
” 
ὃ 
-. Τε 1 πο 
Vy? + Tees 1 axF yr +, - + Trev, 
ay! VT. 
Set V' = 6', and get (ΕΡΤ), ι-- AT* 4, ,/dx!. 
[L*, ἐπ] = ἐπ 
£7] + [τσ ἐπ] £5, + &, 1 4,. £7] 
+ [£i, £7 | £7, = fF £7, + £7, £5, — fF, fr — £7 £7, = 0. 
The second step used equation (3.8). To prove (3.33), derive the 
following relations: 1,, = — sin ϕ 9/90 — cos ¢ cot ϐ 0/09; 1, =— cos ϕ 
0/06 + sin ϕ cot 6 9/φ: 
1. = /d¢. 
Follows trivially from £,7 = a£7 if a is constant. (This is not true if a is 
a general function.) 
When Lie dragged along ¢ from ¢ = 0, 8, is unchanged but @, becomes

## Page 237

Appendix: Solutions and hints 
227 
é, = cos ϕ é, + sin ϕ ἔγ. The third basis vector, é,, has Cartesian 
representation — sin ¢ é, + cos ¢ ἔψ. The three vector harmonics are 
exp (2i¢) 8., exp (2id) (cos ¢ é,, + sin  @,), exp (2id) (— sin ¢ ἐς 
+ cos ¢ ἔν). It might be more useful to use the more compact linear 
combinations exp (2ip) é,, exp (id) (€,. + i@,), exp Bid) (6. — ié,). It 
is obvious from these that 6, + ié,, has eigenvalue + 1 and ες — ié, 
eigenvalue — 1, but these are easy to verify directly. The one-form dz 
is unchanged by Lie dragging, and dx becomes dr = cos ¢ dx + sin ϕ 
dy. The third basis one-form, dg, has Cartesian representation — sin ϕ 
dx + cos @ dy. The three one-form harmonics are, then, exp (2ib) 
dz, 
exp (id) (dx + idy), exp (3i¢) (dx — idy). Since ἐς of = 2if, d (£5 ot) 
= 2idf. But it is easy to show (using cylindrical coordinates) that 
d(£5 AN=£5 (df), which completes the proof. This is a special case of 
a general theorem proved in §4.21 below. 
A right-invariant vector field is invariant under the map Rg, generated 
by right translations analogously to L,. Figure 3.10 applies here, too, 
so they form a Lie algebra. The integral curves through e of a right- 
invariant vector field are one-parameter subgroups for the same reason 
as for left-invariant integral curves. But the subgroups are in 1-1 corre- 
spondence with the two sets of integral curves, so the curves are the 
same. The integral curves of a left-invariant field not passing through e 
are obtained by left-translation of those which do, i.e. of the one- 
parameter subgroups. The curve of V through, say, h is μεν, (1). The 
right-invariant curve through A is g7_,(t)h. This is not the same unless 
hand g7,(t) commute. 
(a) Because left-translation by h' is a 1-1 map of neighborhoods of h 
on to neighborhoods of 6, the vector-field map 1, is also 1-1 and 
invertible. It follows that if {V;(e)} is linearly independent then so is 
{L,V;(e) = V,(h)} for any h. 
(b) The point is that the fields {V;} are globally a basis, so any vector 
field is defined by giving {a,(g)} for all g. This maps 
TG onto G x R”. 
(b) The key step is that (8 14)” =B''ABB'AB...B'AB 
= B'A"B. 
(c) Block-diagonal matrices are easy to exponentiate, since 
P, 
ο 
ο 
(51): 
0 
0 
0 
2, 
0 
0 
(P,)” 
ϱ

## Page 238

Appendix: Solutions and hints 
228 
In case (i), exp (fA;) is the usual exponential function. In (ii), 
κο 
L(t πείς 
0 
1 
(1 ] 
| i, a 0 κα τι 
po 8 | 
|; 1) 
0 
r; — 1s; 
—] 
al) | 
expen) (O° 
ο | 
V2\i 
-ἶ 
0 
cos tr; — isin ts; 
πα - 
al, .. 
from which the answer follows. For (iii), some experimentation will 
verify that 
x 
1 
0 
0 
“ 
ο 
x 
1 
ο 
ο 0x 
1 
d 
1 d? 
1 dad 
πι 
- 
n 
_ 
οι 
__ 
πι 
eae 
212 
31 
d 
1 d? 
n 
μαμα. 
_ 
— 
Φα 
0 
x 
dx 
ο] de? 
7 
d 
0 
0 
x” 
— x” 
When multiplied by t” and put into the exponentiation sum, this gives 
(3.59c). 
3.13 
The sequence of matrices 
cost 
sin (t/ . 
—sint 
cost 
is a continuous path containing e (for t = 0) and 
vs 
ο -ιί 
(for t = π). The matrix is not in a one-parameter subgroup because it is 
not the exponential of any matrix. This follows from exercise 3.12. It

## Page 239

3.14 
3.15 
3.16 
3.17 
Appendix: Solutions and hints 
229 
is easy to verify that none of the forms (3.59) can be transformed as in 
(3.56) to give the desired matrix, because of the negative elements on 
the main diagonal. 
(a) An eigenvalue A of A satisfies the equation det(A — AJ) = 0 
= det(A — AJ)" = det(At — AJ) = det(A7! — AJ) and so is an eigen- 
value of 41. The converse also holds. 
(b) det(A — AJ) = 0 > 0 = det(A!)det(A — AJ) = det(— AA) 
= det(— AJ) det(A“' — XZ). None of the eigenvalues is zero since 
det(A) # 0, so we conclude det(A~! --λ 1) = 0. Thus, if A is in 
O(n) and λ is an eigenvalue of A, so is 1/A. But the equation det(A 
— AI) = Ois real, so its solutions come in complex-conjugate pairs. 
In order for these pairs to be inverse they must have the form (e’? , 
ei9) 
(c) These forms are just (3.58a, b) for the given eigenvalues, with 
(3.62b) being a special case of (3.62c). The only case to exclude is 
(3.58c) when µι = + 1. This form is impossible because B"' 
AB is in 
O(n) while (3.58c) is easily seen not to be. 
(d) The Lie algebra can be found by looking at the tangent space of any 
element, in particular of e, and so we can restrict attention to the 
generators of the one-dimensional subgroups of SO(n). The problem 
may be solved by examining canonical forms, but the following 
method is quicker, Consider the element exp(tA ), where A is in the 
Lie algebra of O(n). Then [exp(tA)]"! = exp(— fA) and [exp(tA)]* 
= exp(tA’). These are equal for any t, so A’ = — A. The converse 
is proved in the same way. The dimension of O(n) is the maximum 
number of linearly independent antisymmetric n xX n matrices, 
4n(n — 1). 
A matrix A is in SO(n) if and only if its canonical form (3.62) has an 
even number of blocks (— 1). An element of O(m) not in SO(7) has an 
odd number of blocks (— 1), and may obviously be obtained from one 
in SO(n) by the given transformation. 
As in the previous problem, the canonical form of A in SO(n) has an 
even number of blocks (— 1), which may be ordered to be a special case 
of (3.62c) with @ = 7. Any canonical form (3.62a) or (3.62c) is a 
special case of the exponentials (3.59a) or (3.59b). For SO(3), the 
canonical form must be one block (3.62a) and another (3.62c). The 
eigenvector for (3.62a) is the axis of rotation. 
Use equation (3.60). 
3.18 The matrix diag[exp(ia,t), exp(ia,t), ...] is the exponential of diag 
(ia,t, ia,t,...). The first matrix has determinant exp(it 2,a;), and if

## Page 240

Appendix: Solutions and hints 
230 
this equals 1 the second matrix is traceless. Let us establish a corre- 
spondence between complex numbers and real 2 x 2 matrices, defined 
byat+ib@ (_% 2). Then multiplication preserves this: (a + ib) (ο + id) 
+ (_¢°)(_$ 2). There is thus a group isomorphism between the com- 
plex numbers and matrices of this special form. (It is in fact an algebra 
isomorphism, since it is preserved by addition as well.) This generalizes 
to a group isomorphism between GL(n, C) and the subgroup of GL(2n, 
R) consisting of matrices built of 2 x 2 blocks of the form ( 5 9). 
Hermitian conjugation in GL(n, C) is simply the transpose operation in 
GL(2n, R). Thus we may regard U(n) as a subgroup of O(2n). Since 
O(2n) is generated by antisymmetric 2n x 2n matrices, U(n) is gener- 
ated by anti-Hermitian matrices. These must be trace-free by our first 
observation and by exercise 3.20(a). 
3.20 (a) (BAB), = (B') A,B” ,. But (B')',B™; = 6)", so tr(B LAB) 
= tr(A). 
(b) Since ἀθί(Β 
1) = 1/det(B), we have det(exp(A)) = det(B™' exp (A)B) 
= det(exp(B' AB)); moreover, exp(tr(A)) = exp(B ‘(tr A)B) 
= exp(tr(B 'AB)). Thus, we need only prove (3.67) for the various 
canonical forms. The form (3.58a) is trivial. For (3.58b), inspection 
of (3.59b) proves the result. The same is true of (3.58c), for the 
matrix written in (3.59c) has unit determinant. 
3.21 (a) Use the identity @ x b) x 
C= (@-@)b — (b «δ)ᾶ. 
3.22 (a) Note that det (_¢ 2) = |a|? + |b/? only vanishes for the zero matrix. 
(b) The dimension is 4 because there are 4 real numbers freely chosen 
to define an element of H. 
(d) Equation (3.73) is the equation for S°, so the 1-1 mapping is estab- 
lished by associating the point (αι, αλ. 3, αι) of S? in R* with the 
matrix A. 
3.23 Since [g(s)]"' = exp (— sY) we can write (3.79) as 
exp (sY) exp(tX) exp(—sY) = exp [tAdy(X)]. 
Differentiating both sides with respect to { at t = 0 gives 
exp(sY)X exp(—sY) = Ady (X). 
Expanding the left-hand side in powers of s gives 
¥+s(¥,X] +487 (¥, (V7) +497, [ΣΤ +.... 
proving the result. 
3.24 (b) Ικ(Υ1 1) =iY1 0 V2: ly(¥, 1) = Yio /V2;1.%1-1 )=i¥i-4; 
L(Y J=i1%14 -N i WMV231,(Y10) (νι + Y; 1 V2; 
l.(Y10) = ο: (Σι 1) Ξ —iYy0/V2;1,(1%1 1) Ξ Y10/V2312(¥ 1) 
= iY, 1°

