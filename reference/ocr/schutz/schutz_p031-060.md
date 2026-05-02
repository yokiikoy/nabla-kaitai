<!-- source-pdf: Bernard F. Schutz-Geometrical Methods in Mathematical Physics-Cambridge University Press (1980).pdf | pages 31-60 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 31–60

## Page 31

1.7 Bibliography 
21 
There are some basic references for most of the material in later 
chapters. These books generally treat them in greater depth and more 
rigor. They will be listed here and referred to later by their authors’ 
names: 
Y. Choquet-Bruhat, C. DeWitt-Morette & M. Dillard-Bleick, Analysis, 
Manifolds, and Physics (North-Holland, Amsterdam, 1977). A compre- 
hensive book aimed at mathematically literate physicists. Especially 
strong on differential equation theory. 
R. Abraham & J. E. Marsden, Foundations of Mechanics, revised 2nd 
edn (Benjamin/Cummings, Reading, Mass., 1978). As its title indicates, 
a book with narrower scope than Choquet-Bruhat et al., but with conse- 
quently greater depth. Notable for its attention to global problems and 
its large bibliography. Considerably larger than the first edition. 
F. W. Warner, Foundations of Differentiable Manifolds and Lie Groups 
(Scott, Foresman, Glenview, ΠΠ. 1971). A readable introduction for 
mathematics undergraduates. Particularly strong on Lie groups and 
cohomology theory. 
M. Spivak, 
A Comprehensive Introduction to Differential Geometry, 
four volumes (Publish or Perish, Boston, 1970). Just what the title says, 
this work is aimed at undergraduate mathematicians. It has a relaxed, 
often humorous style, many good exercises, and lots of detail. 
There are many other books on differential geometry that are worth 
consulting. At an introductory level the reader may like N. J. Hicks, 
Notes on Differential Geometry (D. Van Nostrand, New York, 1965); 
or R. L. Bishop & S. I. Goldberg, Tensor Analysis on Manifolds 
(Macmillan, London, 1968). In the same ‘modern’ spirit as the present 
book is C. T. J. Dodson & T. Poston, Tensor Geometry (Pitman, 
London, 1977). This treats in a more leisurely manner many subjects 
we only touch on, but it does not deal with general Lie derivatives or 
the calculus of differential forms. Readers who find the leap from the 
present book to, say, Choquet-Bruhat et al. too great may find the first 
half of Dodson & Poston helpful. Authoritative works include 
S. Kobayashi & K. Nomizu, Foundations of Differential Geometry, two 
volumes (Interscience, New York, 1963 and 1969), which concentrates 
on positive-definite metric geometry; and J. A. Schouten, Ricci Calculus 
(Springer, Berlin, 1954), which is written in a rather old-fashioned 
notation. 
Not surprisingly, some of the best introductions to differential geometry 
for physicists are in textbooks on general relativity. I recommend 
C. W. Misner, Κ. S. Thorne & J. A. Wheeler, Gravitation (Freeman, San 
Francisco, 1973), which devotes several chapters to a development in the 
same spirit and similar notation as [ use here. More advanced and com- 
pact is the chapter on differential geometry in S. W. Hawking & 
G. Ε. R. Ellis, The Large Scale Structure of Space-Time (Cambridge 
University Press, 1973). An introduction with considerable range is the

## Page 32

Some basic mathematics 
22 
article Differential geometry, by C. W. Misner in Relativity, Groups, 
and Topology, ed. C. DeWitt & B. DeWitt (Gordon & Breach, New 
York, 1964). Another valuable introduction is the article Differential 
geometry from a modern standpoint, by B. Schmidt in Relativity, 
Astrophysics and Cosmology, ed. W. Israel (Reidel, Dordrecht, 1973). 
Also aimed at physicists are R. Hermann, Differential Geometry and 
the Calculus of Variations (Academic Press, New York, 1968); 
D. Lovelock & H. Rund, Tensors, Differential Forms and Variational 
Principles (Wiley, New York, 1975); H. Flanders, Differential Forms 
(Academic Press, New York, 1963); and Von Westenholz, Differential 
Forms in Mathematical Physics (North-Holland, Amsterdam, 1979).

## Page 33

2 
DIFFERENTIABLE MANIFOLDS AND TENSORS 
It is hard to imagine a physical problem which does not involve some sort of 
continuous space. It might be physical three-dimensional space, four-dimensional 
spacetime, phase space for a problem in classical or quantum mechanics, the 
space of all thermodynamic equilibrium states, or some still more abstract space. 
All these spaces have different geometrical properties, but they all share some- 
thing in common, something which has to do with their being continuous spaces 
rather than, say, lattices of discrete points. The key to differential geometry’s 
importance to modern physics is that it studies precisely those properties 
common to all such spaces. The most basic of these properties go into the defini- 
tion of the differentiable manifold, which is the mathematically precise substi- 
tute for the word ‘space’. 
2.1 
Definition of a manifold 
Asin §1.1, we denote by R” the set of all n-tuples of real numbers 
(X1,%X2,..-.,X,). A set (of ‘points’) M is defined to be a manifold if each point 
of Μ has an open neighborhood which has a continuous 1-1 map onto an open 
set of R” for some n. (The reader unsure of what a 1-1 map onto something 
means should look at § 1.2.) This simply means that M is locally ‘like’ κ”. The 
dimension of M is, of course, n. It is important that the definition involves only 
open sets and not the whole of M and R”, because we do not want to restrict 
the global topology of M. This will be clear in the example of the sphere in §2.2. 
Notice that the map is only required to be 1—1, not to preserve lengths or angles 
or any other geometrical notion. Length is not even defined at this level of geo- 
metry, and we shall encounter physical applications in which we will not want 
to introduce a notion of distance between points of our manifolds. At this 
elementary (‘primitive’) geometrical level we are only trying to ensure that the 
local topology of our space (as described in §1.1) is the same as that of R”. A 
manifold is a space with this topology. 
By definition, the map associates with a point P of M an n-tuple (x; (P),..-, 
x,,(P)). These numbers x, (P), ... ,x,(P) are called the coordinates of P under 
this map, as illustrated in figure 2.1. One way of thinking about an

## Page 34

Differentiable manifolds and tensors 
24 
n-dimensional manifold is that it is simply any set which can be given n indepen- 
dent coordinates in some neighborhood of any point, since these coordinates 
actually define the required map to R”. We shall adopt the standard notation of 
writing the index of the coordinate as a superscript: x' (P), x*(P),...,x"(P) are 
the n coordinates of P (not powers of x(P)!) under the map. 
| 
From the discussion so far, we ought now to have a general idea of what a 
manifold is, but to do any better than this we must examine the nature of these 
coordinate maps. Suppose fis a 1-1 map from a neighborhood U of a point P of 
M onto an open set f(U) of R”. As stressed above, the neighborhood U does not 
necessarily include all of M (we shall see in 52.2 that on the sphere it cannot 
include the whole sphere), so there will be other neighborhoods with their own 
maps, and each point of M must lie in at least one such neighborhood. The pair 
consisting of a neighborhood and its map is called a chart. It is easy to see that 
these open neighborhoods must have overlaps if all points of M are to be in- 
cluded in at least one, and it is these overlaps which enable us to give a further 
characterization of the manifold (refer to figure 2.2). Suppose V is a neighbor- 
hood overlapping U, and that V has a map g onto an open region of R”. This 
open region may be completely distinct from the one that f maps U onto. The 
intersection of V and U is open (by axiom (Ti) of §1.1) and is given two dif- 
ferent coordinate systems by the two maps. There is thus some equation relating 
these coordinate systems. To find it, pick a point in the image of the overlap 
under 
f (i.e. a point in R”), say the point (x', x”, ...,x”)in figure 2.3. The 
map f has an inverse f~', so there is a unique point S in the overlap which has 
these coordinates under f. Now let g take us from S to another point in R”, say 
Fig. 2.1. A region U of M has a 1-1 map 
f onto a region f(U) of R”. 
This map associates any point, say P, with a unique n-tuple of numbers 
(x1,X2,...,X,). In this way U acquires a coordinate system, illus- 
strated by drawing the dashed lines that are the images under f' of 
the usual coordinate lines of R”.

## Page 35

2.1 Definition of a manifold 
25 
(y!,y?,..., "). (What we have done is constructed the composite map of 
R” + R”, called go f.) In this way we obtain a functional relationship (a 
coordinate transformation) 
yi = γη) αλ. να”) 
γ2 = y*(x',x?,...,x") 
y” = y™(xl,x?,..., 
x”). 
If the partial derivatives of order k or less of all these functions { y'\ with respect 
to all the {x’! exist and are continuous, then the maps f and g (strictly, the 
charts (U, f) and (V, g)) are said to be C*-related. (This is the notation intro- 
duced in §1.2 for differentiability.) If it is possible to construct a whole system 
of charts (called, appropriately enough, an atlas) in such a way that every point 
Fig. 2.2. The neighborhoods U and V in M overlap (shaded area). Their 
respective maps to R”, f and g, give two different maps (hence two 
coordinate systems) to the overlap region. The relation between these 
coordinates characterizes the differentiability class of the manifold. 
Fig. 2.3. A magnification of figure 2.2, which shows how the overlap 
makes a map from R” to R”, which is f followed by g (called 
goof 
).

## Page 36

Differentiable manifolds and tensors 
26 
of M is in at least one neighborhood and every chart is C”-related to every other 
one it overlaps with, then the manifold 
M is said to be a cr manifold. A mani- 
fold of class C! (which includes C” for k > 1) is called a differentiable manifold. 
The differentiability of a manifold endows it with an enormous amount of 
structure: the possibility of defining tensors, differential forms, and Lie deriva- 
tives. This differential structure is our main subject. Remember, we have not 
introduced the concept of distance on M, and we have no notion of the ‘shape’ 
or ‘curvature’ of M. We only know that locally it is smooth, and that is all we 
need for what follows. 
In most applications we will assume a C™ manifold, but usually this is not 
strictly necessary. There will be times when we shall find it convenient to assume 
an analytic manifold (C“ : the functions { y"} are analytic functions of {x'}), but 
this will be in the physicist’s spirit of invoking analyticity where convenient, as 
mentioned in 51.3. We will take the view that in learning this subject for the 
first time it is better to make rather strong assumptions about the manifold in 
order to see what is going on in the differential geometry. After the student is 
more comfortable with the subject he can worry about relaxing his assumptions. 
Accordingly, the reader should assume throughout the book that any manifold 
is sufficiently differentiable for whatever argument we happen to be using. 
2.2 
The sphere as a manifold 
One of the simplest examples of a manifold, which illustrates the 
importance of allowing for more than one chart, is the sphere. (The word ‘sphere 
always means the surface of the sphere, not its interior.) Consider the two-sphere 
(called ιδ”), the set of points in R? for which (x' )* + (x?)? + («°)? = const. 
Any point has a sufficiently small neighborhood which as a 1-1 map onto a 
disc in R? (see figure 2.4). This shows that the map involved certainly will not 
preserve lengths or angles. As a specific example of a map, consider the usual 
spherical coordinates, with 6 =x' and ¢ =x*. Then the sphere appears to be 
mapped onto the rectangle 0 <x! <z,0<x? < 27, as shown in figure 2.5. But 
there are some funny features here. First, the map breaks down at the pole 
0 = 0, where one point is ‘mapped’ to the whole line x' = 0,0 <x* <27. So 
» 
Fig. 2.4. A small neighborhood of a point P on S? is mapped 1-1 onto 
a disc in κ".

## Page 37

2.2 The sphere as a manifold 
27 
at the pole there is not even a map. The second difficulty is that the points 
having @ = 0 are ‘mapped’ to two places, x? = 0 and x? = 2m: again, there is no 
map. To get around these problems we must restrict the map to the open region 
O<x' «πιο 
κ «2π. Then the two poles and the semicircle ¢ = 0 joining 
them are left out of the map. So here at least two maps are needed to cover 
the sphere completely. The second one could be another spherical coordinate 
system, this time with its line ¢ = 0 in the equator of the first system, say from 
o = 1/2 to @ = 3n/2. Then every point on the sphere is in at least one of these 
two charts. The overlap functions, expressing the second system’s coordinates 
in terms of the first one’s, will be complicated, but it should be clear that they 
will be analytic. So the sphere is an analytic manifold. 
A better map of S* onto a region of R?, which fails at only one point, is the 
so-called stereographic map of the sphere onto the plane, shown in figure 2.6 in 
a vertical cross-sectional view. The sphere is tangent to the plane, and a line is 
drawn from the point V on the sphere diametrically opposite the point of tan- 
gency. This line intersects the sphere at P, and R? at Q. This defines the map: 
Fig. 2.5. Ordinary spherical coordinates appear to give a map from S? 
to R? , which is good for ordinary points like P. But where is the image 
of the north pole? And which of two points is the image of Ο on the 
line 6 = 0? 
Fig. 2.6. The stereographic map of S* to R*. The set S? with the single 
point N removed is open, and this set is mapped onto all of R*. The 
map fails at 
N itself. 
N

## Page 38

Differentiable manifolds and tensors 
28 
P is mapped to Q, or in other words the coordinates of P in S* are just the 
coordinates of Q in R*. This map is 1-1 except at NV, for as the line from N 
becomes horizontal (P approaching /V), the point Q goes to infinity. But no 
matter in what direction in R* the point Q goes to infinity, the point P always 
approaches Ν. So Ν is mapped into all of ‘infinity’ and another coordinate 
patch must be used near NV. There is no mapping which is good on all of S*. 
Notice that this whole discussion really depends only on the global topology of 
S*: exactly the same remarks apply to the surface of, say a bowl or a wine glass, 
which are simply deformations of S?. On the other hand, the two-dimensional 
interior of the annulus bounded by two concentric circles in R* can be covered 
by a single coordinate patch. Try to find it! 
2.3 
Other examples of manifolds 
The usefulness of the concept of a manifold really comes from its 
generality, the fact that it embraces sets which one might not ordinarily regard 
as spaces. By definition, any set M that can be parameterized continuously is a 
manifold whose dimension is the number of independent parameters. For 
example: 
(i) The set of all rotations of a rigid object in three dimensions is a manifold, 
since it can be continuously parameterized by the three ‘Euler angles’ (cf. 
Goldstein, 1950). 
(ii) The set of all (pure boost) Lorentz transformations is likewise a three- 
dimensional manifold; the parameters are the three components of the velocity 
of the boost. 
(iii) For N particles, the numbers consisting of all their positions (3N num- 
bers) and velocities (3N numbers) define a point in a 6N-dimensional manifold, 
called phase space. 
(iv) Given an equation (algebraic or differential) for a dependent variable y in 
terms of an independent variable x, one can define the set of all (y, x) to be a 
manifold; any particular solution is a curve in this manifold. This concept is 
easily extended to arbitrary numbers of dependent and independent variables. 
(v) A particularly common manifold is a vector space, whose definition is 
given in 51.5. (Here we are dealing with vector spaces over the real numbers.) Το 
see that such a space is a manifold we will construct a map from it to some R”. 
Suppose the vector space V is n-dimensional, and choose any basis {@,,..., @,,}. 
Any vector y is then representable as a linear combination 
Ψ = aé,+...4+4,6é,. 
(2.1) 
But y is a point V, so this establishes a map from V to R”, p' (a,,...,4,,). In 
fact every point of R” corresponds to a unique vector in V under this map, so 
not only is V covered entirely by the single coordinate system we have just

## Page 39

2.4 Global considerations 
29 
constructed, but I’ is identical, as a manifold, with R”. In the language of group 
theory (51.4), V and R” are isomorphic. This is an important result. It means 
that every vector space may be thought of, when convenient, simply as R”. 
(vi) Example (i) above is an example of a Lie group, which we are now in a 
position to define. A Lie group G is a group which is also 
aC” manifold, with 
the restriction that the group operation induces aC” map of the manifold into 
itself. What this means is the following. Pick out any element a of the group. 
This element induces a map of G into itself, taking any element b of G into ba, 
b +> ba. This map must be C™ ; in concrete terms in whatever coordinates are 
used on G, the coordinates of ba must be C™ functions of those of b. The 
demand for such a map is really a compatibility requirement, to ensure that the 
manifold property is compatible with the group property. In example (i) above, 
then, the set of all rotations forms a group, and it is not hard to show that this 
group structure is indeed compatible with the three-dimensional manifold struc- 
ture. (This Lie group is called SO(3).) This definition of Lie groups may seem 
abstract and perhaps rather arid at first, but we shall become much more familiar 
with them in chapter 3. A simple example of a Lie group is R”. It is a vector 
space (see (v) above) and therefore a group, and it is also a manifold: R” is in 
fact the simplest Lie group. 
2.4 
Global considerations 
Because every manifold is locally the same as some R”, any two mani- 
folds of the same dimension (and same differentiability class) are locally indistin- 
guishable at this level of differential geometry. But this is certainly not the case 
when we consider their global structure, as the comparison of S? with R* in 
52.2 showed. Manifolds therefore divide up into classes according to their global 
properties. As an example, the sphere S* and the surface of a crayon have the 
same global structure. Although neither has a single map onto R*, each has a 
single perfectly good 1-1 map onto the other, as illustrated in figure 2.7. 
Fig. 2.7. 
A smooth (C~) crayon can be mapped 1-1 onto a sphere 52 
The map is global, not restricted to patches. It is a diffeomorphism, 
and so is its inverse.

## Page 40

Differentiable manifolds and tensors 
30 
(Strictly speaking, the crayon should have very smooth edges to be identical to 
S* asaC™ manifold.) Such a map directly from one C™ manifold M to another 
N, which is 1-1 and C™ (a map is C™ if the coordinates of a point in 
NV are 
infinitely differentiable functions of the coordinates of the inverse image of 
the point in M) and whose inverse is also C™, is called a diffeomorphism of M 
onto NV. The manifolds M and WN are said to be diffeomorphic if such a map 
exists. The surface of a teacup is diffeomorphic to the torus (doughnut) because 
each has just one hole: one can smoothly deform one into the other. 
Most of the geometry we will study in this book will be local, depending only 
on the differential structure. But there will be occasions, such as our studies of 
fiber bundles and of integration of functions, when the global properties of our 
manifolds will become very important. 
2.5 
Curves 
Curves in the manifold will be of great importance to us. One’s ordinary 
idea of a curve is that it is a continuous series of points in M. It is convenient 
here to make a somewhat different definition: a curve is a (differentiable) map- 
ping from an open set of 1 into M (see figure 2.8). Thus, one associates with 
each point of 
κ) (which is a real number, say A) a point in M, which is called the 
image point of X. The set of all image points is the ordinary notion of the curve, 
but our definition gives each point a value of A. Clearly we have a parameterized 
curve, with parameter λ. Thus, two curves are different even if they have the 
same image in M, provided they assign a different parameter value to the image 
points. Again, by a ‘differentiable’ mapping we simply mean that the coordinates 
of the image point, {x'(A), 
i= 1,..., n} are differentiable functions of X. 
2.6 
Functions on M 
A function on M is a rule that assigns a real number (the value of the 
function) to each point of M. When a region of M is mapped differentiably onto 
Fig. 2.8. A curve in M is a map from ΑΣ into M. The point Xin R! is 
mapped to P in M. The image of the open interval from a to b in R! 
is the line shown in M. 
( 
) 
R 1

## Page 41

2.7 Vectors and vector fields 
3] 
a region of R”, the function becomes a function on R” (see figure 2.9). If this 
function is differentiable in R", then it is said to be a differentiable function on 
M. We can say the same thing in another way: abstractly, the function may be 
written as f(P), where P is a point of M. But P has coordinates, so one can ex- 
press the value of the function by some algebraic expression f(x',x?,...,x”). 
Then if this expression is differentiable in its arguments, the function is differ- 
entiable. The coordinates themselves, of course, are continuous and infinitely- 
differentiable functions. 
For example, x° is the function such that x° (P) is the 
value of the third coordinate of the point P. 
From now on we shall avoid referring to the mapping from M to R” directly, 
although we shall occasionally refer to the coordinates (which describe the 
mapping). The purpose of discussing mappings up till now has been to establish 
the fundamental concepts in as precise a way as possible. From now on we shall 
be more interested in using these concepts to develop the differential structure 
of the manifold, so we will always assume that we can place coordinates {', 
i=1,...,n}on the manifold, and that any sufficiently-differentiable set of 
equations y’ = y'(x’) which is locally invertible (i.e. whose Jacobian is nonzero — 
see $1.2) constitutes an acceptable coordinate transformation to new coordin- 
ates {yi=1,..., Πλ. 
2.7 
Vectors and vector fields 
Consider a curve passing through the point P of M, described by the 
equations x’ = x'(A), 
i= 1,...,. Consider also a differentiable function 
f(x',...,x”) (abbreviated f(x’)) on M. At each point of the curve, 
f has a 
value. Therefore, along the curve there is a differentiable function g(A) which 
gives the value of fat the point whose parameter value is i: 
Fig. 2.9. The function fon M is a map from M to ΚΣ. The coordinate 
map g from a region U of 
M containing P onto a region g(U) of R” has 
an inverse. The composite map f © σα gives a map from R” toR’, 
which is a function on R”. This is just the expression of f(P) in terms of 
the coordinates of P.

## Page 42

Differentiable manifolds and tensors 
32 
g(r) = F&A), ....x"Q) = F&A). 
Differentiating and using the chain rule gives 
d 
dx? 9 
wily 
wo 
(2.2) 
dv 
; 
ἆλ Ox’ 
This is true for any function g, so we can write 
d 
dx’ ὃ 
¢ 
— = 
—_——, 
2.3 
dv 
; 
ἆλ Ox’ 
(2.3) 
Now, in the ordinary view of vectors in Euclidean space, one would say that 
the set of numbers {dx'/dA} are components of a vector tangent to the curve 
x'(A); one can see this by realizing that {dx’! are infinitesimal displacements 
along the curve, and that dividing them by dA only change the scale, not the 
direction, of this displacement. In fact, since a curve has a unique parameter, to 
every curve there is a unique set {dx’/dd}, which are then said to be components 
of the tangent to the curve. Thus, with our definition of a curve, every curve has 
a unique tangent vector. 
Of course, every vector is the tangent to an infinite number of different 
curves through P, for two different reasons. The first is that there are many 
curves which are tangent to one another and have the same tangent vector at P, 
and the second is that the same path may be re-parameterized in such a way as to 
give the same tangent at P. These are illustrated in figure 2.10. As an example of 
this, consider the simple curve x’(A) = Aa’, where the numbers {a'! are constants. 
Then if P is the point \ = 0, the tangent there is dx‘/d\ = a’. Another curve, 
Fig. 2.10. (α) Two curves having the same tangent vector. (b) Two 
curves having the same path but different parameterizations. If the maps 
are called hy and ᾖλ, then the map ἠ2 © h, gives a relation between 
the two parameters, Ay  λο(λι). If dA, /dA, = 1 at P the two tangent 
vectors will be the same at P. 
R} 
\ 
\ 
| / 
\ 
\ 
| 
| 
ee 
τε 
ὢ 
ahi 
Pot 
ot td, 
ια 
4 2 
! 
| 
| 
| 
| 
1 
Ι 
I

## Page 43

2.7 Vectors and vector fields 
33 
x'(u) = 2b! + pa’, also passes through P at up = 0 and has the same tangent 
vector there, dx’/du = a’. A re-parameterization of the first curve, καὶ = (w 
+ p)a', passes through all the same points and at P (u = 0) has the same tangent, 
dx'/du = a’. So each vector really characterizes a whole equivalence class of 
curves at that point. 
This use of the term ‘vector’ relies on familiar concepts from Euclidean 
space, where vectors are defined by analogy with displacements Ax’. However, 
since manifolds need have no distance relation between points, we shall need a 
definition of vector which relies only on infinitesimal neighborhoods of points 
of M. Suppose a and b are two numbers, and x’ = x'(y) is another curve through 
P. Then at P we have 
ο 
για =F 
det oe ο 
dv 
du 
; 
dav 
du 
Ox!” 
Now, the numbers {adx'/dA + bdx'/ du} are components of a new vector, which 
is certainly the tangent to some curve through P. So there must exist a curve 
with parameter, say, ϕ such that at P 
d 
dx? 
dx? \ a 
—_— = 
a—+b—|—. 
ἀφ 
= \" dy 
du } dx? 
Collecting these results, we get, at P, 
d 
d 
d 
a ar +b di = dp 
Therefore, the directional derivatives along curves, like d/dA, form a vector space 
at P.! There are in any coordinate system special curves, the coordinate lines 
themselves. The derivations along them are clearly 0/dx’, and equation (2.3) 
shows that any d/dA can be written as a linear combination of the particular 
derivatives 0/0x’. It follows that {0/dx"} are a basis for this vector space. Then 
(2.3) shows that d/dA has components {dx'/dd} on this basis. We therefore have 
the remarkable result that the space of all tangent vectors at P and the space of 
all derivatives along curves at P are in 1-1 correspondence. For this reason the 
mathematician says that d/dA is the tangent vector to the curve x'(A). We shall 
adopt this point of view, since it has three advantages. First, it is precise, since it 
does not involve displacements over finite separations. Second, it makes no 
t The derivatives must, of course, obey the other axioms of § 1.5 if they are to 
form a vector space, but closure under linear combinations is the only nontrivial 
one.

## Page 44

Differentiable manifolds and tensors 
34 
mention of coordinates; in particular, it does not rely on notions like “transforms 
the same way as... .’. Third, a derivative is a kind of ‘motion’ along the curve, 
which is what, conceptually, a tangent vector generates; this association of a con- 
cept from analysis — the derivative — with one from geometry — the vector — 
has very powerful consequences. 
One can still maintain the same ‘picture’ of a vector as an arrow tangent to 
the curve, since the components are just the same. Now, however, one must 
realize that only vectors at the same point P can be added together. Vectors at 
two different points have no relation with one another. The vectors lie, not in M, 
but in the tangent space to M at P, which is called Tp. For ordinary manifolds, 
like the surface of a sphere, this tangent space is easy enough to visualize as a 
plane tangent to the sphere at that point. 
For more abstract manifolds it may be 
harder. 
We shall use the term vector to refer to a vector at a given point P of M. The 
term vector field refers to a rule for defining a vector at each point of M. 
2.8 
Basis vectors and basis vector fields 
At any point P, the space ΤΡ is a vector space with the same dimension 
n as the manifold. Any collection of 
linearly independent vectors in Tp is a 
basis for Tp. By choosing a basis in each Τρ for all points P of M, we arrive at a 
basis for vector fields. If we have a coordinate system {x’! in a neighborhood U 
of P, then the coordinates define the coordinate basis {0/dx*} at all points in U. 
But one need not use the coordinate basis; one could refer vectors to some 
arbitrary basis {@;}. Here the subscript { is used as a label to distinguish one basis 
vector from another. It does not denote the component of anything. At a point 
P, an arbitrary vector V can be written as 
- 
. 0 
η 
V= ον σα τὸν) ει 
J 
The numbers {7/1} are the components of V on {0/0x'}. The numbers {V/ } are 
the components of V on {é;}, and are related to V' by the usual vector transfor- 
mation laws, which we will deal with later. If V and the bases {0/ax‘} and {,} 
are regarded as vector fields, then the components {V"} and {V! 4 of the field V 
are functions on M. A vector field is said to be differentiable if these functions 
are differentiable. 
We have implicitly assumed above that the vectors {0/0x'} of an arbitrary 
coordinate system are in fact all linearly independent at any point P of U. What 
justification do we have for this? We shall show that this is just the condition 
for the coordinates to be good coordinates at P, i.e. for them to provide a 1-1 
map of some neighborhood U of P onto a region V of κ”. Consider a set of

## Page 45

2.9 Fiber bundles 
35 
coordinates on U which are good, say {y',i=1,..., 7}. Then the map from 
(x',...,x”) to U can be expressed by the equations 
yl = γα... 
x"), f= 1...ν Π. 
By the inverse function theorem (§1.2) this map is 1—1 (has an inverse) in U if 
and only if the Jacobian matrix dy//dx' has a nonvanishing determinant. This 
means that at any point of U the vectors whose components are (dy'/dx’ , 
dy7/dx',..., oy"/dx"), (Oy'/dx?, dy?/dx?,..., ay"/ax?),..., (Oy fax”, 
dy7/dx",..., dy"/dx”) are linearly independent. But these are just the com- 
ponents of the vectors {0/0x', 
i= 1, ...,} on the coordinate basis of the {y'} 
system, because by the chain rule 
2 aya wa, 
ara 
1 
14,,1 
1 
312 0 "°° 
ly,,n? 
Ox 
ox oy 
Ox’ oy 
Ox” Oy 
and similarly for the other x's. So {x'} is in fact a good coordinate system in U 
if and only if {0/dx"} are a basis for vectors at each point of U. The reader may 
wish to look at the basis vectors of the spherical coordinates on the sphere to see 
how they go bad at the poles. 
2.9 
Fiber bundles 
A particularly interesting manifold is formed by combining a manifold 
M with all its tangent spaces ΤΡ. This is illustrated in figure (2.11) for the sim- 
plest case: a one-dimensional manifold M (a curve) and its tangent spaces (lines 
tangent to it at each point). In part (a) of figure 2.11 we draw the curve and a 
few tangent spaces; these are lines drawn tangent to the curve, and each must be 
thought of as extending infinitely far in both directions in order to allow for 
vectors of arbitrary length at each point. Now, when drawn this way the picture 
Fig. 2.11. (α) A one-dimensional manifold and some of its tangent 
spaces. (b) The same, with the tangent spaces drawn parallel to one 
another to avoid spurious intersections.

## Page 46

Differentiable manifolds and tensors 
36 
can be messy, since the various tangent spaces intersect one another and the 
curve M haphazardly: these spurious intersections have no meaning. A better 
way of drawing the picture is as in figure 2.11(b), where the tangent spaces are 
drawn parallel: they do not intersect each other, and they cross M only at the 
point where they are defined. This picture unfortunately does not show the fact 
that each Tp is ‘tangent’ to the curve, but that is the price to be paid for clarity. 
Each point on the vertical line Τρ represents a vector, having that ‘length’ and 
being tangent to M at P. Figure 2.11(b) also shows something else: every point 
in the figure (a two-dimensional manifold) is a point of one and only one tan- 
gent space for M, say Τη for point R of M. To each point in that figure there is 
one and only one vector at one and only one point at M. So one is led to define 
anew manifold 7M, consisting of all vectors at all points, which is thus two- 
dimensional. It is called a fiber bundle, and the fibers are the spaces Τρ for each 
P. The term ‘fiber’ comes from drawing pictures like figure 2.11(b) above. To 
see that ΤΗ is indeed a two-dimensional manifold, let us construct a coordinate 
system for a portion of it. Let the one-dimensional manifold M have coordinate 
x, and let us find coordinates for the tangent spaces to points of M in the region 
a<x <b for some a and b, assuming that the coordinate x itself is a good co- 
ordinate in this interval. (The reason for this assumption will be evident in §2.11 
below.) Any tangent vector V at any point P can be written as 
V = ya/ox, 
(2.4) 
so that the component y is a coordinate for Tp (cf. equation (2.1)). It clearly is 
a good coordinate over the whole fiber ΤΡ. Since each fiber has a fixed value of 
x, the coordinates (x, y) locate a particular vector (y) tangent to a particular 
point (x). Since every point of the fiber bundle must by definition lie in a region 
of this sort, we have proved that this 7M is a manifold. Clearly, the construction 
is easily generalized to tangent fiber bundles of higher-dimensional manifolds. A 
coordinate system of this sort, in which coordinates for Tp are determined by 
those on M at P by expressing a vector on the coordinate basis (2.4) is called a 
natural coordinate system for TM. 
Now, the curve in the fiber bundle drawn as a dashed line in figure 2.12 
identifies a particular vector at each point of M, and so the curve defines a vector 
field on M. Such a curve (i.e. one which is nowhere parallel to a fiber) is called a 
cross-section of TM. Clearly, it is not usually meaningful to ask for the ‘length’ 
of the curve, and so here we have an example of a manifold on which one 
usually would not bother to define a metric. 
A general fiber bundle consists of a base manifold, which in our case is the 
curve M, and one fiber attached to each point of the base space. If the base space 
is n-dimensional and each fiber is m-dimensional, then the bundle has m + n

## Page 47

2.10 Examples of fiber bundles 
37 
dimensions. It is a special kind of manifold, since it has the property of being 
decomposable into fibers: the points ofa single fiber are related to one another 
while points on different fibers are not. This is formalized by defining a pro- 
jection map m, which maps any point of a fiber to the point of the base manifold 
the fiber is attached to. A general manifold does not have such a projection 
defined on it. The following examples illustrate the wide variety of spaces de- 
scribable as fiber bundles. 
2.10 
Examples of fiber bundles 
(i) The fiber bundle TM we have illustrated consists of a manifold and 
its tangent spaces, and is called the tangent bundle. It is one of the most impor- 
tant abstract manifolds in physics. 
For an n-dimensional manifold, TM has 2n 
dimensions. 
(ii) Later in this chapter we will generalize from vector fields to tensor fields. 
There are corresponding bundles over any differentiable manifold for every type 
of tensor. 
(iii) The fibers need not be related to the differential structure of the base 
space. Consider the ‘internal’ variables describing the state of an elementary 
particle, such as isospin. A bundle whose fibers are isospin space and whose base 
space is spacetime is capable of describing both the position variables (x, y, Ζ, 1) 
of the particle and its internal (isospin) state. 
(iv) The view of spacetime taken by Newtonian physics has a natural fiber- 
bundle structure. To Newton and Galileo, time was absolute: everyone can agree 
what events are simultaneous, no matter where they occur. We can therefore 
construct a bundle whose base space is R! (time) and whose fibers are R° 
(space). This is illustrated in figure 2.13. There is no natural relation between 
points on different fibers (points of space at different times), because Newtonian 
physics has no ‘absolute space’: two different observers moving with respect to 
each other disagree as to what constitutes a fixed point of space. So there is no 
natural fiber structure with R? as a base, while there is with ΚΣ. One effect of 
Fig. 2.12. A cross-section (dashed line) of the fiber bundle TM of a one- 
dimensional manifold M (heavy line).

## Page 48

Differentiable manifolds and tensors 
3S 
Einstein’s relativity was to destroy this bundle structure and to substitute some- 
thing else, a metric structure (see §2.31 below). 
2.11 
A deeper look at fiber bundles 
There are two related aspects of fiber bundles which we should con- 
sider in order to appreciate the richness and usefulness of the bundle concept. 
These are their global properties and the importance of groups in their con- 
struction. 
To understand the interesting global properties fiber bundles can have, we 
must first define a simpler concept, the product space. Two spaces M and N have 
an associated (Cartesian) product space M x N consisting of all ordered pairs (a, 
b) with a in M and b in N. For example, R? is defined as the product R' x ΚΙ. If 
M and N are manifolds, M x N is also a manifold in an obvious way: the set of 
coordinates {x',i= 1,...,m} ofan open set U of M, taken together with 
{y!,i=1,...,n} of an open set V of N, form a set of m +n coordinates for the 
open set (U, V) of M x N. It is clear from our construction of fiber bundles 
above that they are, at least locally, product spaces, the product U x F of an 
open set U of the base manifold B with the space F representing a typical fiber 
(all fibers being identical to F’). This in fact forms part of the definition of a 
fiber bundle: it is Jocally trivial (it is a product space when we look at a local 
region of B). The interesting question is whether it is globally trivial: whether 
the whole fiber bundle can be represented as the product B x F. 
The answer is usually no, and we give two examples which illustrate what 
both the question and the answer mean. 
(i) Consider TS”, the tangent bundle of the two-sphere ιο”. If it were globally 
trivial, there would be a C™ 1-1 map (a diffeomorphism) of TS? onto S? x R?, 
since the typical fiber is R’ , the tangent plane. Consider the set of points in S” 
x R? of the form (P, V), where P is an arbitrary point of S? and V is a given 
fixed vector in κ. Then the inverse of the above map gives a nowhere-zero 
cross-section of TS”, i.e. a definition of a C™ vector field on S* which is 
Fig. 2.13. The natural bundle structure of Newtonian (Galilean) space- 
time, which is ‘sliced up’ into moments of constant universal time.

## Page 49

2.11 A deeper look at fiber bundles 
39 
nowhere zero. But in fact there is no C™ vector field on S* which is nowhere 
zero. This is a consequence of the famous but difficult fixed-point theorem of 
the sphere, that every 1-1 map (diffeomorphism) of S* onto itself leaves at least 
one point of S? fixed. A nowhere-zero vector field would generate such a map 
with no fixed point, as we explain in §3.1 below. Therefore TS? does not have 
a global product structure. This is an example in which the bundle is nontrivial 
because of the topology of the base manifold, S*. 
(ii) The second example shows that one can actually make a bundle nontrivial 
even if the base space allows a trivial bundle. Consider TS', the tangent bundle 
of the circle S'. Unlike S*, the circle does allow a continuous nowhere-vanishing 
vector field, and TS" is identical to the product space οἱ x R, as shown in figure 
2.14. This is just the global version of the local picture shown in figure 2.1 1(0). 
But suppose we ‘cut’ the circle at P in figure 2.14 and unwrap the bundle, lying 
it flat, as in figure 2.15. To reconstruct figure 2.14 from 2.15 we simply identify 
point a with a’, P with P’, b with b’, and so on. But we can reassemble the fiber 
bundle a different way by forming a Mobius band: identify α with b’, P with P’, 
b with a’, and so on. This gives the strip a twist so that it looks like figure 2.16 
when joined together. Locally it is still the same as figure 2.11(b); in fact the 
Fig. 2.14. The trivial way of constructing TS' as the product space of 
the circle S' and the typical fiber R! (drawn vertically). Cf. figure 
2.11(2). 
CLD» 
P 
Fig. 2.15. TS! cut along one fiber and laid flat. The fibers extend infi- 
nitely far in the vertical direction.

## Page 50

Differentiable manifolds and tensors 
40 
bundle over any connected open proper subset of S’ (‘proper’ means not iden- 
tical to S') has a 1-1 continuous map onto the same portion of figure 2.14. One 
has to go all the way around to see that there is no continuous 1-1 map of all of 
one bundle onto all of the other. Therefore, the M6bius band is not a product 
space, and the second bundle is nontrivial. Nontrivial constructions of bundles 
in analogous ways are used in modern particle physics to define the so-called 
‘instantons’. 
The Mobius example has a lesson for us: it is not sufficient simply to say 
what the base and fiber of a bundle are, because there may be more than one 
way to construct such a bundle. We need a better definition of a fiber bundle, 
and this is where groups come in. The difference between the two bundles over 
5) is in what is called the bundles’ structure group. To phrase the full definition 
of a fiber bundle more compactly, we need to define a homeomorphism, which 
is simply a 1-1 map from one space onto another, which is continuous and 
whose inverse is continuous.’ (For an explanation of the terminology of maps, 
see §1.2.) We define a fiber bundle as a space E for which the following are 
given: a base manifold B, a projection 7: E > B, a typical fiber F’, a structure 
group G of homeomorphisms of F onto itself, and a family {U;} of open sets 
covering B (i.e. open sets whose union is B), all of which satisfy the following 
restrictions. 
(i) Locally the bundle is trivial, which means that the bundle over any set U;, 
which is just 7"'(U;), has a homeomorphism onto the product space U; x F. We 
have noted this above. Part of this homeomorphism is a homeomorphism from 
each fiber, say 7 
'(x) where x is an element of B, onto F’. Let us call this map 
πα), labelled not only by the point x which defines the fiber but also by the 
index j which denotes the set U; containing x. 
(ii) When two sets U; and U;, overlap, a given point x in their intersection 
has two homeomorphisms h(x) and /;,(x) from its fiber onto ΜΕ. Since a 
Fig. 2.16. The Mobius-band version of this bundle: the fibers turn over 
once as one follows them around the circle. Locally it still has the same 
structure as figure 2.11(b). 
A homeomorphism is a diffeomorphism without the differentiability requirement. 
For most of the bundles of physical interest, one can read ‘diffeomorphisms’ for 
‘homeomorphisms’.

## Page 51

2.11 A deeper look at fiber bundles 
4] 
homeomorphism is invertible, the map h,(x) © hj' (x) is a homeomorphism of F 
onto F. This is required to be an element of the structure group G. 
The second restriction contains the information about the global structure of 
the fiber bundle. To see how this works, we first give the complete definition of 
TS' (which has a straightforward generalization to TM for any M). The bundle 
ΕΞ TS" has base B = S', typical fiber F = R*, and projection π: (x, 0) + x, 
where x is a point of S' and 0 is a vector in 7,,. Let the covering {U;} be the 
open sets of any atlas of S’. A typical family {U;} is illustrated in figure 2.17. 
Every U; has a coordinate ‘system’, i.e. a parameterization of S' , which we will 
call \;. The vector d/da; at x in U; is a basis for 7;,, so any vector 0 in 7;, has 
the representation a;)d/da, for any fixed/, where aj) isa real number. This is just 
equation (2.4) again. The homeomorphisms of 1, onto R which are part of the 
definition of TS" are defined to be h,(x): δ 
aj. If x is in two neighborhoods 
U; and U;, there are two such homeomorphisms from 7,, onto R, and since ); 
and d;, are unrelated, a,;) and αγ) can be any two nonzero real numbers. The 
homeomorphism h,(x) © hz, x): F > F maps αι 
ΓΣ αι) and is therefore just 
multiplication by the number 7;, = a(;)/a(,). Since 7;, is any real number other 
than zero, the structure group is R' — {0}, which is a group under multipli- 
cation, a Lie group in fact. We note in passing that for an n-dimensional mani- 
fold M, the structure group of TM is the set of all n x n matrices with nonzero 
determinant, which is called GZ(n, R). We will study this group in chapter 3. 
This defines TS‘. But what does it look like? It is possible to choose the co- 
ordinates A; in such a way that any two, say A; and A,, increase in the same 
direction in S’ in the region where U; and U;, overlap. (We say that S* is orient- 
able; see §4.7.) With such a choice of coordinates it is not hard to see that all 
the ‘overlap numbers’ r;, are positive, and the structure group reduces to R’, 
multiplication by the positive real numbers. In fact we can do even better by 
scaling the coordinates in such a way that ἆλι/ἆλι = 1 in every overlap region. 
Then the group reduces to 1, the identity element. The structure group is trivial, 
and so is the bundle structure. This is the bundle represented in figure 2.14. 
To characterize the structure of the Mobius band we must use different maps 
Fig. 2.17. A set of neighborhoods of S' which cover S!. The extent 
of each neighborhood is indicated by the parentheses. U, overlaps U2, 
U, overlaps U3, and so on until Ug overlaps U,.

## Page 52

Differentiable manifolds and tensors 
42 
h(x), and we must be careful not to try to interpret the bundle as a tangent 
bundle. The easiest procedure is to use the family {U;,7=1,..., 8} shown in 
figure 2.17 and to define Γι} = 1,723 = 1,...,773 = 1. But then the twist in 
the Mobius band forces us to use rg; = — 1. The structure group consists of the 
elements {1, — 1} with multiplication as the group operation. We could have 
made other choices for the 7;,8, but we could not have found a smaller structure 
group. 
The tangent bundle 7S* had structure group R' — {0}, which is nearly the 
same as its typical fiber. The frame bundle of any manifold M has the same 
structure group as TM, but its fiber is the set of all bases for the tangent space 
(equivalently, for R”). In the case of a one-dimensional manifold like ιδ, this is 
the set of all nonzero vectors, which is identical to R' — {0}. So the frame 
bundle of S' has fibers homeomorphic to its structure group, and this is true of 
all frame bundles. Such a bundle is called a principal fiber bundle. 
2.12 
Vector fields and integral curves 
As defined in §2.7, a vector field is a rule that gives a vector at every 
point of M. Each point has its own tangent vector space, so a vector field selects 
one vector from each space. Now, every curve has a tangent vector at every 
point, and the question arises of whether the converse is true: given an arbitrary 
vector field, is it possible to start at one point P and find a curve whose tangent 
vector is always the vector field at whatever point the curve passes through? The 
answer is yes, for C! vector fields, and such curves are called integral curves of 
the vector field. The proof is as follows. Let the components of the vector field 
be V'(P), functions of P. In some coordinate system {x!} we have V*(P) = v'(x’). 
The statement that this is a tangent vector to a curve with parameter λ is 
η 
ο 
= U(x’). 
(2.5) 
This is just a set of first-order ordinary differential equations for x'(A), and a 
unique solution always exists in some neighborhood of the initial point P. (This 
existence/uniqueness theorem for ordinary differential equations is proved in 
most textbooks on differential equations. A version may be found in Choquet- 
Bruhat, Dewitt-Morette & Dillard-Bleick (1977) in the bibliography.) Two 
particular vector fields are illustrated in figure 2.18. 
Notice that the paths of different integral curves can never cross except pos- 
sibly at a point where V* = 0 for all i, because of the uniqueness of solutions to 
(2.5). Since some integral curve passes through each point P (it is found by solv- 
ing (2.5) with initial conditions at P), the integral curves ‘fill’ M. For instance, if 
M is three-dimensional, then there is a two-dimensional family of integral curves 
for each vector field on M, and they cover all of M (except possibly isolated

## Page 53

2.14 Lie brackets and noncoordinate bases 
43 
points where V' = 0 for all 7). Such a manifold-filling set of curves is called a 
congruence. The set of curves, incidentally, can usually be regarded as a mani- 
fold itself. 
2.13 
Exponentiation of the operator d/dA 
We now introduce an idea that will prove to be a useful tool in several 
subsequent calculations. Suppose we have an analytic manifold (C™ 
), and the 
coordinate values x'(X) of points along the integral curves of Y = ά/ἀλ are 
analytic functions of A. Then the coordinates of two points with parameters po 
and A» + e€ are related by the Taylor series 
dx? 
1 
42 i 
x'(Ao + ε) = x'(Ag) + εν) rte x 
+ 
Xo 
° 
Ao 
dxf, 
21 
Vax 
d 
1,@ 
| 
= 
[l+e—+—e?—+...]x 
| an 2° an? 
|. 
' 
“| 
x! 
(2.6) 
= exple—|x'! 
, 
μπα. 
where the ‘exp’ notation is an obvious and convenient shorthand for the differ- 
ential operator which, when applied to x'(A) and evaluated at Ao, gives the 
Taylor series. It is called the exponentiation of the operator εά/ἀλ. Since ed/daA 
is an infinitesimal ‘motion’ along the integral curve, its exponentiation gives a 
finite motion. Other notations we will use include 
exp (ed/da) = οἑ αλ = ef”, 
2.14 
Lie brackets and noncoordinate bases 
Given a coordinate system x’, it is often convenient to adopt {0/dx"} as 
a basis for vector fields. However, any linearly independent set of vector fields 
Fig. 2.18. Integral curves of two vector fields on R’. (a) V = x0/0y 
— yd/dx;(b) V = (x + y/r)d/ay — (vy — x/r)d0/dx, withr = (x? + y?)'. 
(a) 
(ϱ)

## Page 54

Differentiable manifolds and tensors 
44 
can serve as a basis, and one can easily show that not all of them are derivable 
from coordinate systems. This is because the operators 0/dx’ and 0/ax/ 
commute for all i,j. Two arbitrary vector fields do not commute: if V = d/da 
and W = 4/άμ. then 
i,j 
ow! ὃ 
.ov' a 
+ 
pa 
YS 
py — 
ὃ Ox" Ox! 
π 
ox! dx" 
owi _ avila 
= 
vyi—--wi'— 
]—, 
2.7 
5 | 
Ox’ 
aa 
2.7) 
where the last line follows from relabelling the summation indices in the final 
sum of the middle quantity. Therefore, the commutator 
ἆ 
ἆ 
ποπ 
τπτ 
στ τπτ 
(2.8) 
ἀλ΄ du 
ἀλάμ 
ἂἆμ ἀλ 
is a vector field whose components do not vanish in general. If d/dA and d/dy are 
two elements of a basis, then they will not be expressible as derivatives with 
respect to any coordinates. Such a basis is a noncoordinate basis. 
It is important to realize that this distinction between coordinate and non- 
coordinate bases is one which can be made only over some region of the mani- 
fold, not at a single point. It depends on the derivatives of the components of 
the vectors, not just on their values at a point. The different properties of 
coordinate and noncoordinate bases therefore matter only over regions of a 
manifold, and are irrelevant in problems which involve only the tangent space 
Tp of a single point P. 
Exercise 2.1 
Show that the ‘unit’ basis vector fields for polar coordinates in the 
Euclidean plane, defined by 
f 
cos 0X 
+ sin 6Y, 
ϐ = —sin 
0% + cos OF, 
where x = 0/dx and y = 0/dy, are a noncoordinate basis.

## Page 55

2.14 Lie brackets and noncoordinate bases 
45 
The commutator [ά/άλ. d/du] is called the Lie bracket’ of V and W, and 
we now look at its geometrical interpretation. In figure 2.19 we have drawn a 
coordinate grid on a two-dimensional manifold. Notice that by definition x’ is 
constant along the lines of x*, which are the integral curves of 0/dx?. That is 
why 0/dx' and 0/dx* commute: each is a derivative along a line on which the 
other is fixed. Now consider two arbitrary vector fields, V = d/dA and W = d/du, 
whose integral curves are shown in figure 2.20. An integral curve of W is not 
necessarily a curve of constant A, and vice versa. The derivative d/dyu is not a 
derivative holding λ fixed, so d/dA and d/dy do not commute. Although the V 
and W curves look like coordinate curves, their parameterization is not that of a 
coordinate system. Even the fact that they look like coordinate curves is an 
artefact of two dimensions: in three dimensions it may happen that curve (1) 
intersects curves (a) and (8) but (2) intersects only (a). 
Fig. 2.19. Typical coordinate grid on a two-dimensional manifold. 
Fig. 2.20. Typical integral curves of two vector fields on a two- 
dimensional manifold. 
t The ‘Lie’ of Lie bracket is the same Lie as in Lie groups: Sophus Lie, the great 
mathematician of the late nineteenth century. The Lie bracket is, as we shall see, 
a special case of the Lie derivative. Readers who are familiar with Lie groups may 
recognize the Lie bracket as the commutator of the vector fields d/dA and d/du 
which generate a Lie group of mappings. We discuss these mappings in chapter 3.

## Page 56

Differentiable manifolds and tensors 
46 
We can obtain a picture of the vector [V, W] in the following manner. In 
figure 2.21, consider starting at P, moving Ad = e along the V curve through 
P, and then moving Ay = € along a W curve. One winds up at A. Starting again 
at P and going first Au = e and then AA = e¢, takes one to B #A. We shall show 
that the vector stretching from A to B is e? [V, W] , to lowest order in e. 
It is most convenient to use the exponentiation operator introduced earlier. 
It is clear that 
. 
d 
. 
i 
- 
i 
x'(R) 
exp ; 
a 
x 
? 
P 
and 
x'(A) = exp - 
η 
exp 
|é πι 
xt, 
(2.9) 
du 
dr 
P 
Similarly, the path to point B from P gives us 
x(B) = exp 9 
a 
exp 
|ε η 
x! 
(2.10) 
dr 
du 
Ρ 
Then the difference in the coordinates of A and B is 
x'(B)—x'(A) = [ο 9/44, ος HH] χὴν, 
(2.11) 
just the commutator of the exponentiation operators. Returning to the Taylor 
series, we can write 
; 
d 
1 
d 
[ος HAR, ge uy — ... +0), 
d 
d? 
bettie Soe 
µ 
μ 
x'(B)—x'(A) = e? [V, W] + Ο(εξ ). 
(2.12) 
Fig. 2.21. Geometric interpretation of the Lie bracket [V, W] as the 
open part of an incomplete parallelogram whose other sides are equal 
parameter increments along integral curves of V and W.

## Page 57

2.15 When is a basis a coordinate basis? 
47 
This is just the ith component of the Lie bracket, and (2.12) justifies the picture 
we have given for it. 
Exercise 2.2 
(a) Use (2.6) to prove (2.12). 
(b) Prove that 
exp [ad/dA + bd/du] 
= exp [αά/άλ] exp [bd/du] 
(2.13) 
for all a and b if and only if [d/da, d/du] = 0. 
Exercise 2.3 
Prove that any three twice-differentiable (1.9. (2) vector fields X, Y and 
Z satisfy the Jacobi identity 
[LX, Y],Z] + [[¥,Z], 
X] + [[Z,X], Y] = 0. 
(2.14) 
A Lie algebra of vector fields on a region U of M is aset A of vector fields on 
U which is a vector space under addition (which means any linear combination 
with constant coefficients of fields in A is a field in A) and which is closed under 
the Lie-bracket operation (the Lie bracket of any two fields in A is another field 
in A). Clearly, the set of all 6 vector fields on Uis a Lie algebra, but it is more 
interesting when a smaller set of vector fields singled out for some reason also 
forms a Lie algebra. These are closely related to the invariance properties of 
manifolds and to their associated invariance groups, which are usually Lie 
groups. We shall study this in greater detail in chapter 3, where we will also pre- 
sent a more general definition of a Lie algebra. 
2.15 
When ts a basis a coordinate basis? 
Suppose we are given two vector fields A = d/dA\ and B = d/du ona 
two-dimensional manifold M, and suppose that A and B are linearly independent 
at every point of some open neighborhood U of M, so that they form a basis for 
vector fields there. What condition would assure us that they are a coordinate 
basis, in other words that λ and w are coordinates for U? It is clearly necessary 
that they commute 
(4, Β] = 0. 
We shall show that this condition is sufficient as well. To do this we go right 
back to the basic definition of a manifold: we construct a 1-1 map from U onto 
a neighborhood in R*. Beginning at some point P in U, and using arbitrary co- 
ordinates (x!, x?) in U, we move a parameter distance A, from P along A toa 
point R whose coordinates are (by equation (2.6))

## Page 58

Differentiable manifolds and tensors 
48 
x(R) — ei d/dv x'|p. 
If we go first a distance λι along A, then µι along B, we get to a point Ο with 
coordinates 
x'(Q) -- elt Adu gd, d/dA yi) | 
This equation defines an exponential-type map from some neighborhood V of 
the origin of R* into U: a given element of V, the pair (A, , μι), is mapped to the 
point Q. This map is illustrated in figure 2.22. In order for this map to define a 
coordinate system, it must be 1-1: it must have an inverse. We show below that 
it does have an inverse everywhere in U, but first we shall show that A and B are 
the coordinate basis vectors of this coordinate system if they commute in this 
neighborhood. Let us rewrite the map as the coordinate transformation from 
ία, B} to {x*, x?}: 
xi(a, B) = Palau god/ar yi 
The basis vectors 0/da and 0/06 have components (in the {x'! coordinate 
system) dx'/da and dx'/dB, respectively. It is easy to show from (2.6) that 
do ead/dA _ ,ad/dr 4 
da 
dr’ 
and since d/du and d/dA commute, we obtain 
da 
ᾱλ 
ὃν ος balay goasan OX 
Op 
du 
But dx'/d) is just the component of d/d) in the {x"} coordinate system. Since 
this is an analytic function of M, operating on it with exp (βά/ἀμ) :« exp (αά/άλ) 
i 
i 
Ox 
— efd/du god/dr dx 
» 
Ρ 
Ρ 
Fig. 2.22. The map from Κ2 to M described in the téxt. This provides 
a coordinate system in some neighborhood of P.

## Page 59

2.16 One-forms 
49 
simply produces its value at the point whose coordinates are (a, 8). Therefore 
we have everywhere in U 
9/ὃα = d/dd and δ/9β = d/dy, 
and we have proved the sufficiency of [A, B] = 0 asa condition that A and B be 
coordinate basis vectors. 
We return now to the deferred proof that {a, 6} do form a coordinate system 
in U. We must prove that the map {a, 6} > {x'} has an inverse, and for this we 
use the inverse function theorem (see $1.2). This says that if the matrix 
ox! 
ax? 
da da 
ax' 
dx? 
06 8B 
has a nonzero determinant at some point {a, 8}, then the map has an inverse in 
some neighborhood of this point. The determinant will vanish if and only if the 
vectors 0x'/da, ax'/0B are linearly dependent, but from the above discussion it is 
clear that this will never happen because A and B are linearly independent in U. 
Therefore, everywhere in U the map is invertible and provides a coordinate 
system. 
It is interesting to ask where this argument breaks down if [A, B] #0. !n this 
case the expression dx'/dB is more complicated. It is still true that, at least in 
some neighborhood of a = 8 = 0, the map has an inverse. But because dx'/08 is 
no longer just dx’/dy at the point in question, the vectors 4 and B are not the 
basis vectors of the constructed coordinates. 
The whole argument extends to n dimensions: if n vector fields {Y;;y, 
j=1,...,n} onan n-dimensional manifold 
M are linearly independent and 
commute with one another in some open region U of M, then they are the co- 
ordinate basis vectors of the coordinate system {a;}, given in terms of an arbi- 
trary system {x/} by 
x'(Q1,...5,%,) = αν] 
» “Fay 
x; 
J 
centred at an arbitrary point P in U. 
2 
2.16 
One-forms 
Let us go back to Tp, the space of all tangent vectors at P. As a first 
step towards tensors, we define a one-form as a linear, real-valued function of 
vectors. This means the following: a one-form @ at P associates with a vector V 
at P a real number, which we call 6(V). This notation expresses the idea that ὢ 
is a function on vectors. (A tilde (~) over a letter always denotes a one-form, 
just as a bar (”) denotes a vector.) The linearity of this function means

## Page 60

Differentiable manifolds and tensors 
50 
S(aV + bW) = a&d(V) 
+ b&(W), 
(2.15) 
where a and b are real numbers. We can define addition of one-forms and their 
multiplication by real numbers in a straightforward way: ad) is the one-form 
such that 
(a&)(V) = α[ῶ(γ)] 
(2.16a) 
for all V, and & + @ is the one-form such that 
(O+G)V) = 6(V)+A(V) 
(2.16b) 
for all V. Thus one-forms at the point P satisfy the axioms of a vector space, 
which is called the dual vector to Tp, and is denoted by 7p. The reason 
it is ‘dual’ is that vectors can also be regarded as linear, real-valued functions of 
one-forms, in the following manner. Given a vector V, its value on any one-form 
ὤ is defined as 63(V 
). This is linear, since its value on αῶ + b@ is, by (2.16) 
above, 
(αῶ + b&)(V) = (αῶ) (1) + (&)(V) 
a(value of V on 6) + b(value of V on 6). 
(2.17) 
It is thus the linearity property which enables us to regard each as a function 
taking the other as argument and producing a real number; vectors and one- 
forms are thus said to be dual to each other. Their value on one another is often 
represented in many ways: 
o 
OV) = γ(ῶ) = (ῶ. 0), 
(2.18) 
where the last expression emphasizes their equal status. The formation of the 
number @(V) is often called the contraction of & with V. In older treatments 
of tensor algebra, vectors are often called ‘contravariant vectors’ and one-forms 
‘covariant vectors’. These names refer to the behavior of their components under 
a change of basis, which is something we will deal with in §2.26. 
2.17 
Examples of one-forms 
Before going further with the mathematical development, let us look at 
some familiar examples of one-forms. One of the most common is the gradient 
of a function, which will be discussed in §2.19. Other examples include the 
following: 
(i) In matrix algebra, if we call column vectors ‘vectors’, then row vectors are 
one-forms. This is because when multiplied (in the correct order) by the usual 
rules of matrix multiplication, they give a single real number. For example, in 
the two-dimensional case the row vector (— 1, 5) may be thought of as a func- 
tion which takes an arbitrary column vector into a real number: 
(— 1,5): κ... = —xt 5y. 
JY 
y

