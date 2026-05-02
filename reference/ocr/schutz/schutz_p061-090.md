<!-- source-pdf: Bernard F. Schutz-Geometrical Methods in Mathematical Physics-Cambridge University Press (1980).pdf | pages 61-90 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 61–90

## Page 61

2.18 The Dirac delta function 
51 
That this function is linear is easily checked. 
(ii) In the Hilbert spaces used in quantum mechanics, the analogues of 
example (i) are Dirac kets |W) (vectors) and bras (| (one-forms), whose con- 
traction is (|), a complex number. (The generalization of vector and tensor 
algebra to algebras over the complex numbers rather than the reals is trivial: one 
just replaces the word ‘real’ by ‘complex’. In many ways, the generalization of 
our real manifolds to complex-analytic ones — where the maps are analytic maps 
to the space (z1, z”,...,2”) for complex rather than real z' — is also simple. 
But some features of complex manifolds, such as their global structure and 
curvature, present special problems, which we cannot treat in this book.) The 
notation (¢|W) is, not accidentally, similar to (2.18). 
In both examples (i) and (ii) one is used to switching between the vectors 
and one-forms, associating with a given vector its ‘conjugate’ or ‘transpose’, 
which is a one-form. We shall see in §2.29 below that this is equivalent to giving 
a metric or inner product to the vector space. This is a very important additional 
structure in a vector space, but the reader should bear in mind that there is no 
a priori, ‘natural’ way of associating a particular one-form with a particular 
vector. 
218 
The Dirac delta function 
In quantum mechanics one often deals with function spaces. Consider 
the set C[— 1, 1] ofall C™ real-valued functions defined on the interval — 1 <x 
<1 of κ. This set is a group under addition (the sum of any two C™ functions 
ἰδς , etc.) and a vector space under multiplication by real constants (if f is a 
C™ function, so is cf for any constant c). Its dual space of one-forms is called 
the distributions. An example of a distribution is the Dirac delta ‘function’ §(x), 
which is defined as that one-form whose value on aC” function f(x) is f(0): 
(6(x), f(x)) = f(0). 
(2.19) 
In one sense 6(x) is a true function: it is a mapping C[— 1, 1] > R. It is custom- 
ary to apply the word ‘distribution’ only to a continuous function of this sort. 
But any notion of continuity requires a topology, in this case a topology for 
C[- 1, 1]. This is an infinite-dimensional vector space (there are an infinite 
number of linearly independent C™ functions), and a discussion of its topology 
is well outside the scope of this book. The interested reader can consult 
Choquet-Bruhat et al. (1977). What is important for one to understand at 
present is that this sense of function is not what Dirac and his contemporaries 
meant when they called d(x) the delta function. To see what they had in mind 
we have to look again at a way of transforming a function in C[— 1, 1] into a 
one-form on C[— 1, 1].

## Page 62

Differentiable manifolds and tensors 
52 
For any function g in C[— 1, 1] it is possible to define a one-form % whose 
value on a function fin C[— 1, 1] is 
@ f= | gle) fe)ax. 
(2.20) 
This is indeed a linear function mapping f to the integral’s value. (Since g and f 
are continuous on— 1 <x <1, they are bounded there and the integral always 
exists.) The name ‘delta function’ was used as a loose way of turning this 
relation around: if 5() is a one-form, then one ought to be able to talk about it 
as a function of x in the ordinary sense whose integral with f(x) produced f(0): 
[ 52/0) & 
= £0) 
This idea caused great distress to mathematicians, some of whom even declared 
that Dirac was wrong despite the fact that he kept getting consistent and useful 
results. Wisely, the physicists rejected these extreme criticisms and followed 
their intuition. We can now see why they were ‘wrong’ and still succeeded. They 
were ‘wrong’ because they spoke of 5(x) as a function R' > R!, which it cannot 
be in any precise sense, and because they treated it as a function by integrating 
it and even differentiating it: 
μμ = -[ 5(x) f'(x) dx = —f'(0). 
But they were ‘right’ because they never used 5(x) outside integrals with 
sufficiently-differentiable functions f(x): they never used it except to map 
functions to real numbers. In this sense they employed the machinery but not 
the words of distribution theory, which was devised expressly in order to give 
delta functions a sound basis. Notice, however, that distribution theory has one 
big simplification over the older physicists’ view: it can define the delta function 
without referring to any mule like (2.20) for turning a function into a one-form. 
As remarked in example (ii) above, such a rule is an extra structure on a vector 
space, which we now see is unnecessary for understanding delta functions. 
We should remark in passing that we restricted the word ‘distribution’ to con- 
tinuous one-forms, in keeping with the usual practice in defining the dual of any 
vector space. However, we did not include the word ‘continuous’ in our defini- 
tion of one-forms in 952.16: have we been inconsistent? The answer is no, because 
on a finite-dimensional vector space a linear function is always continuous. (See 
Cho quet-Bruhat et αἰ. (1977) or Rudin (1964), in the bibliography of chapter 1.) 
2.19 
The gradient and the pictorial representation of a one-form 
A field of one-forms, by analogy with vector fields, is a rule giving a 
one-form at every point. The rules in equation (2.16) extend to fields; in this

## Page 63

2.19 The gradient and the pictorial representation of aone-form 
 οδ 
case, a is a function on M, not necessarily constant. Differentiability of one- 
form fields can be defined in terms of that of vector fields and functions. For 
example, on aC” 
manifold, a given one-form field @ defines, when supplied 
with a vector field V, a function G(V). If this function is ο 
for any C™ V then 
& is C™. (We will give an easier definition of differentiability after defining 
components of one-forms in 92.20.) As with vector fields, there is a fiber bundle 
called the cotangent bundle T*M with 
M as base and 7*p as the fiber over the 
point P. Cross-sections of 7*M are one-form fields. 
A most useful and instructive one-form field is the gradient of a function f, 
which we denote by df. Although elementary treatments of vector calculus call 
the gradient a vector, it is properly a one-form. Thus, the gradient df (not the 
‘infinitesimal’ df, which we rarely use)! is defined by 
ϕ 
df(d/da) = df/da, 
(2.21) 
where d/dA is an arbitrary tangent vector. That is, the gradient of f at any point 
P is that element of T*p whose value on an element V of Tp is the directional 
derivative of f along a curve whose tangent is V. We must check that this is a 
linear function on ΤΡ. in the sense of equation (2.15): 
/ 
ied +02) - ων]; 
dv 
du 
da 
du 
d 
d 
=a of 
+ b of 
dv 
du 
a df(d/dd) + b df(d/du). 
So it is indeed linear. At first thought it might seem that fitself should be the 
one-form, since f and ά4[ἀλ make df/dA, a number. But this is not right; the 
reader is reminded that both Tp and 7“ p are defined at a point P, so all the 
information needed to construct df/dA must be present there. The value of f at 
Pis irrelevant to df/dA. To compute df/dd at P one needs to know 0//0dx’ at P. 
These are, as we shall see, the components of the gradient of f. So it is the 
gradient which is the one-form. 
The gradient enables us to develop a picture of a one-form, complementary 
to the picture of a vector as an arrow. In figure 2.23 we have drawn part of a 
topographical map, showing contours of equal elevation. If h is the elevation, 
then the gradient dh is clearly largest in an area like A, where the lines are closest 
together, and smallest near B, where the lines are spaced far apart. Moreover, 
suppose one wanted to know how much elevation a (short) walk between two 
points would involve. One can lay out on the map a line (vector AX) between 
t For a nice discussion of the relation of af to the infinitesimal, see Spivak (1970), 
vol. 1.

## Page 64

Differentiable manifolds and tensors 
54 
the points. Then the number of contours the line crosses gives the change in 
elevation. For example, line 1 crosses 14 contours, while 2 crosses 2 contours. 
Line 3 starts near 2 but goes in a different direction, winding up only 4 a con- 
tour higher. But these numbers are just Ah, which is a linear function of dh and 
Ax: 
This is the value of dh on Ax (cf. equation (2.21) above and (2.27) below). 
Therefore, a one-form @ may be represented by a series of surfaces (figure 
2.24), and its contraction with a vector V is the number of surfaces V crosses. 
The closer the surfaces, the larger 6. Properly, just as a vector is straight, the 
one-form’s surfaces are straight and parallel. This is because we deal with one- 
forms at a point, not over an extended region: ‘tangent’ one-forms, in the same 
sense as tangent vectors. 
These pictures show why one in general cannot call a gradient a vector. One 
would like to identify the vector gradient as that vector pointing ‘up’ the slope, 
i.e. in such a way that it crosses the greatest number of contours per unit length. 
The key phrase is ‘per unit length’. If there is a measure of distance on the mani- 
fold, then a vector can be associated with a gradient. But if one does not know 
how to compare the lengths of vectors that point in different directions, one 
cannot define a direction of steepest ascent, and the gradient is fundamentally 
different from a vector. Since we shall not assume a length (or ‘metric’) in 
Fig. 2.23. A topographical map of a hilly region. Curves are contours 
of equal elevation above sea level. Arrows indicate possible paths for 
a walker. 
Fig. 2.24. A ‘tangent’ one-form @ represented pictorially as a series of 
parallel surfaces of dimension one less than that of the manifold. The 
number pierced by a vector V is the contraction (@, V).

## Page 65

2.20 Basis one-forms and components of one-forms 
55 
general, we must preserve the distinction between vectors and one-forms. We 
will return to this point in 52.29. 
2.20 
Basis one-forms and components of one-forms 
In the vector space of one-forms atP; T*p, any n linearly indepen- 
dent one-forms constitute a basis. However, once a basis {é;,i= 1,...,n}has 
been chosen for the vectors Tp at P, this induces a preferred basis for T*p, called 
the dual basis {G3',i=1,...,.n}. It is defined as follows. If V is any vector in Tp 
then ὤἱ produces the ith component of V 
aV) = V'. 
(2.22) 
It is easy to see that this is linear in the argument V, since the ith component of, 
say, V+ Wis V' + W'. So (2.22) indeed defines a linear function on ΤΡ. In 
particular, since the basis vector 6; has only a jth component, all others vanish- 
ing, we have 
+ 
ai) = 84. 
(2.23) 
This is the definition of @' found in most references. Note carefully that in 
order to define any G' all the vectors {é;} must be known. A change in any one 
é, generally changes al/ the basis one-forms @'. The correspondence we have 
established is between one basis and its dual, not between an individual vector 
and an associated one-form. 
We have not actually proved that the {@"} are linearly independent and there- 
fore do form a basis. This follows easily from (2.23), but we will use a more 
indirect approach. Consider any one-form @ acting on an arbitrary vector V, 
q(V) = ασ ve) 
», Via) 
> &(V)GE)). 
(2.24) 
j 
The numbers 
αι = F@;) 
(2.25) 
are called the components of ᾷ on the basis dual to {é;}. To see that this name 
is more than a mere analogy with (2.22), we rewrite (2.24) as 
q(V) = » q;@'(V). 
Since a one-form is defined by its values on vectors, it follows from this, equa- 
tion (2.16), and the fact that V is arbitrary, that

## Page 66

Differentiable manifolds and tensors 
56 
ϕ 
ἃ = > οῶ). 
(2.26) 
J 
This shows that the set {d/} is indeed a basis, since there are only n of them and 
any ᾷ is a linear combination of them. It also shows that the numbers {q;} are 
indeed the components of 7 on this basis in the ordinary sense. 
Most importantly, we now have a formula giving us the value of 9(V ) if we 
know the components of g and of V: 
q(V) = % αιγ’. 
(2.27) 
As remarked before, this is the contraction of V and g. 
Naturally, all these considerations extend directly to one-form fields. If the 
set of vector fields {61 is a basis at every point in some region U of M, then the 
fields {G!} defined by (2.23) are likewise a basis at all points of U. A coordinate 
system on U, {x}, defines a natural basis for vector fields {0/dx’?. It also defines 
a natural set of n one-forms, the gradients {dx'}. These one-forms are in fact the 
basis dual to the coordinate basis vectors: by equation (2.21) 
dx'(a/ax/) = dxi/ax! = δἱ,, 
(2.28) 
the second equality following from the ordinary properties of partial derivatives. 
In §2.19 we defined differentiability of one-form fields. It is now easy to 
prove that J is 
aC” one-form field if only if its components {q’} associated with 
aC basis for vector fields are C™ functions. 
2.21 
Index notation 
We adopt the following conventions for the use of indices. Components of 
vectors, e.g. V', have the index written as a superscript; components of one- 
forms, e.g. w,, have subscripted indices. Members of a vector basis are labelled 
with subscripts (2;), those of a one-form basis with superscripts (@/). (For 
coordinate bases, this rule means that the one-forms dx! have their index up, 
as they should, while the vectors 0 /ax! are considered to have their index down, 
since it appears in the denominator as a superscript.) These conventions are 
adopted for a good reason. Consider the contraction 
OV) 
= δ, Vio, 
j 
which is a sum of products in which one multiplier has a raised index and the 
other a lowered one. We shall adopt the Einstein summation convention: 
whenever an expression contains a repeated index, once as subscript and once 
as superscript, a summation over the index is understood. Thus, in the ex- 
pressions

## Page 67

2.22 Tensors and tensor fields 
57 
G=wud'i, 
P= vi, OV) = Vio, 
x 
summations are understood. In the expressions 
Viw®, 
γω, = VW), 
there are no summatiohs; in the first two there are no repeated indices, and in 
the last both are raised. Use of the summation convention greatly simplifies 
calculations in which components are used, and our rules for the placement of 
indices minimize the possibility that the convention will lead us into careless 
errors. 
We are now in a position to extend our treatment of vector algebra to tensors. 
2.22 
Tensors and tensor fields 
Tensors are a natural extension of the concepts we have already 
developed. Their algebra is straightforward and they have, as we shall see, many 
uses. The principal problem students have when they first encounter tensors is 
that they cannot ‘visualize’ them: they have no picture. We have earlier devel- 
oped pictorial ways of representing vectors and one-forms; this can to some 
extent be extended to tensors of higher type, but the pictures rapidly become 
very complicated. It is perhaps better to avoid picturing most tensors directly, 
and to think of them in terms of the definition we shall now give, as linear 
operators on vectors and one-forms. 
Consider a point P of M. A tensor of type (’) at P is defined to be a linear 
function which takes as arguments NV one-forms and NV’ vectors and whose value 
is a real number. This is a generalization of the way we defined one-forms. By 
‘linear’ we understand linearity on every argument (usually called multi- 
linearity). For example, if F is a (2) tensor then its value on the one-forms & 
and @ and the vectors V and W is 
F(,6;V, W). 
As a linear function it obeys (for arbitrary numbers a, b) 
9 
Ε(αῶ -Εδλ. δ: Ρ, W) = αξ(ῶ, δ: Ρ, W)+ DFO, 3 J, W), 
(2.29) 
and similarly for the other arguments. If we want to speak of F without naming 
its arguments, we may sometimes write 
F( , ; , ), in which empty spaces 
signify ‘slots’ into which any arguments of the appropriate type (one-forms 
before the semicolon, vectors after) may be placed. Naturally, the order of the 
arguments generally makes a difference, as is true of functions of real variables. 
(That is, the function f(x, y) = 3x + Sy has different values for f(1, 2) and 
(2, 1).) 
As with vectors and one-forms, a (9) tensor field is a rule giving a (9)

## Page 68

Differentiable manifolds and tensors 
58 
tensor at each point. Linearity extends to tensor fields, where the numbers a 
and b in equation (2.29) can have different values at each point: they are func- 
tions on M. Differentiability of the field is defined as for one-forms, $2.19. 
As a special case, note that vectors are tensors of type (0): they are linear 
functions of one-forms. Similarly, one-forms are tensors of type (°). By con- 
vention, a scalar function on the manifold is taken to be a tensor of type (0). 
(See §2.28 on ‘Functions and scalars’ below.) A (1) tensor T requires two 
arguments. Thus, Τ(ῶ: V) is a real number; for fixed ὤ, T(@; ) is a one-form, 
since it needs a vector argument to give a real number; T( ; V) isa vector. So, 
a (1) tensor in particular can be thought of as a linear vector-valued function of 
vectors, and also as a linear form-valued function of one-forms. This game can 
be played with any tensor. 
2.23. 
Examples of tensors 
Although our definition of a tensor may seem rather abstract, it is in 
fact quite often very directly applicable to common problems. We mention 
three examples immediately, and later (in 52.29) devote some time to a dis- 
cussion of a very important tensor, the metric tensor. 
(i) We take our first example from matrix algebra. If column vectors are 
vectors and row vectors are one-forms, then a matrix is a (1) tensor, since multi- 
plying it by a vector gives a vector, and letting it operate on both in the usual 
way gives a number. 
Exercise 2.4 
A linear (‘active’) transformation in matrix algebra (e.g. an orthogonal 
rotation) transforms one matrix into another. Show that it is therefore 
a (2) tensor when operating on matrices. 
(ii) The second example is from the function space C[— 1, 1] mentioned in 
§ 2.18. A linear differential operator (e.g. x? d/dx) converts functions (‘vectors’ 
in this space) into other functions (vectors). Being linear, it is therefore also a 
(1) tensor in the space. 
(iii) The third example is the stress tensor. Readers familiar with continuum 
mechanics will know the stress tensor. Given a stressed material, and given an 
imaginary plane passing through the material, the stress tensor gives the stress 
vector across that plane (the force per unit area exerted by the material on one 
side of the plane upon that on the other side). Now, a plane is a surface, and a 
surface is represented by a one-form. The stress tensor turns out to be a linear, 
vector-valued function of one-forms, or a (2) tensor.

## Page 69

225 Contraction 
59 
2.24 
Components of tensors and the outer product 
A simple (6) tensor is the following: given two vectors V and W, we 
form a tensor called V 6) Wwhose value on two one-forms ὗ and J is the product 
ΥΠ): 
9 
V @ Wd) = ΥΦΙ(Ω. 
(2.30) 
The operation © is called the ‘outer product’, ‘direct product , or ‘tensor prod- 
uct’. Its generalization to arbitrary numbers and types of tensors is obvious. 
The outer product of a (4y) tensor with a (Λη tensor is a tensor of type (4 ΑΝ. 
The components of a tensor are its values when it takes basis vectors and one- 
forms as arguments. If 5 is a (2) tensor, then it has components on a basis {e;} 
ϕ 
ου = ς(ῶ), &!, 
"3, δν). 
(2.31) 
If the order of the arguments of 5 matters, then so does the order of the indices 
of Sur . 
The extension to components of tensor fields and their differentiability is 
exactly as for one-forms in 52.20. 
Exercise 2.5 
(a) Prove that a general (0) tensor cannot be expressed as a simple outer 
product of two vectors. (Hint: count the number of components a 
(2) tensor may have.) 
(b) Prove that the (1) tensor V ® ὤ has components V'w,. 
Exercise 2.6 
Prove that the set of all (3) tensors at P is a vector space under addition 
defined by analogy with equation (2.160). Show that e; @ e; is a basis 
for that space. (Thus, although a general (2) tensor is not a simple outer 
product, it can be represented as a sum of such tensors.) This vector 
space is called Tp © ΤΡ. 
2.25 
Contraction 
In exercise 2.5, we point out that the set {V’w;} are components of a 
(1) tensor. Now, by summing on the index, one gets yi (oj, a number indepen- 
dent of the basis, the value of ὤ on V, which may be thought of as a (9) tensor. 
By analogy one can show that if Sip and P'™ are components, respectively, of 2 
(5) and (2) tensor, then S';,, P”” is a component of a (3) tensor, ο P’” of a 
({) tensor, Sip P" of a different ({) tensor, etc. By analogy with equation 
(2.27), this operation is called contraction, and produces new tensors. 
We can give a short proof of the fact that contraction is independent of the

## Page 70

Differentiable manifolds and tensors 
60 
basis used. Consider the (2) tensor A, the (2) tensor B, and their contraction 
(in some basis) 
A” B;,. We claim that these are the components of a (1) tensor 
C, such that for arbitrary vector V and one-form 
σ(σ; V) —= (x 
AB, ow 
= » AG; G)BG;, V). 
j 
j 
By linearity on A’s second argument we can write this as 
ο(σ. V) = ale 
> BE, ra), 
j 
since the quantities B(@;, V) are just numbers. But in §2.20 we proved in effect 
that, independent of the basis, 
», BE, V)a' = BC, 7), 
which is a one-form since (for fixed V) it requires a vector as an argument (in 
the empty slot). This one-form occupies one of the slots in A, so we have proved 
AB, = Ci, Φ C@;V) = AG,B( .7)), 
independent of any basis (cf. exercise 2.8). 
Exercise 2.7 
How many different (7) tensors may be made by contraction on pairs 
of indices of the (3) tensor ΟΥ 31113 How many (6) tensors by a second 
contraction? 
Exercise 2.8 
Let A and B be two (1) tensors, and regard them as vector-valued linear 
functions of vectors: if V is a vector then A(V) and B(V ) are vectors. 
Show that if we define C(V) to be 
c(V) = B(A(Y)), 
then C is a (1) tensor as well. Show that its components are 
ae 
Cc; κ. B',A 
j° 
Discuss the relation of this with the linear transformation defined in 
51.6. 
2.26 
Basis transformations 
The behavior of a tensor’s components under a change of basis is at the 
heart of the older definition of a tensor. It has been replaced more recently by 
the definition we have used here in terms of linear functions, and it is a measure

## Page 71

2.26 Basis transformations 
61 
of how conceptually different these two approaches are that we are only now 
getting around to looking at basis transformations. This is not to say that these 
transformations are unimportant. Most practical calculations involving tensors 
involve working with their components, and an understanding of their trans- 
formation properties is essential. 
We shall consider vectors and tensors defined at some point P of M. Suppose 
we begin with a vector basis {é;,/ = 1,...,}and wish instead to use a basis 
{é,7' =1,..., 2}. (We shall use primes on the indices as our only way of 
distinguishing references to one basis from references to the other.) Then in Tp 
there is a linear transformation A from the old basis to the new: 
er = Δε. 
(2.32) 
The matrix A’, is nonsingular (otherwise {2,'} would not be linearly indepen- 
dent) but otherwise arbitrary. It is not the collection of components of some 
tensor, since its indices refer to two different bases. It is simply called the trans- 
formation matrix. 
The old one-form basis satisfies (2.23): 
63'(é,) = 
δἳ, . 
Multiplying by ΛΑ j' and using (2.32) and linearity gives 
OE) = 5, A® = Abe. 
(2.33) 
Now the matrix Ai; has an inverse, which we will define to be AP: 
APA = 6, 
AP At = 64, 
(2.34) 
Multiplying (2.33) by A® , gives 
ΛΑ OG) = δὲ, 
By comparing this with (2.23) 
9 
ak = AF ey, 
(2.35) 
This is the counterpart of (2.32): basis one-forms transform oppositely to basis 
vectors (i.e. using the inverse transformation matrix) in order to satisfy (2.23) on 
both bases. 
It is now a simple matter of transform components: 
Vi = (VV) = N,V) = Αν], 
(2.36) 
αν’ = TEx) = UN ye) = VeIE) = Λόναι, 
(2.37) 
and similarly for tensors of higher type (cf. exercise 2.9 below). These trans- 
formation laws show that the components of vectors and the basis one-forms 
obey the same law, which is opposite (i.e. uses the matrix inverse) to the law 
obeyed by components of one-forms and the basis vectors. This is reasonable, 
in order to keep such sums as Ve, V'0,, etc. independent of basis. This illus- 
trates another convenience introduced by our positioning of indices and our 
|

## Page 72

Differentiable manifolds and tensors 
62 
summation convention: the position of an index automatically gives its trans- 
formation law. For example, V‘ and &/ obey the same law, which is 
vi = AV 
It could not use the matrix Ati, because the summation must be on unprimed 
indices and must involve one index which is up and one which is down. 
These opposing transformation laws gave rise to the old names, ‘contra- 
variant’ and ‘covariant’. What we call a vector was called contravariant because 
its components obey the law opposite (‘contra’) to the law governing the basis 
vectors. Similarly, one-forms were “covariant vectors’ because their components 
go with the basis vectors. The modern viewpoint emphasizes the fact that neither 
the vector nor the one-form is in fact changed by a basis transformation: they 
are coordinate-independent geometrical objects. Therefore, modern terminology 
has dropped the old names because they over-emphasize the coordinate- 
dependent descriptions of these objects. 
Exercise 2.9 
Show that a (2) tensor’s components transform as two vectors, i.e. 
Tit = Ai, Ai 7, 
(2.38) 
Generalize this to type (4). 
Exercise 2.10 
Show that if a tensor’s components are all zero in one basis, they are 
zero in all bases. (We then say the tensor is zero. It follows that if two 
tensors have equal components in one basis they are equal in all, and 
the tensors are said to be equal.) 
Exercise 2.11 
Associated with a particular basis {@;} of a vector space of dimension 
n, we are given some set of numbers (41, i,j=1,...,n}. We define 
another set of numbers Ai, = At Al, A! | and call them the compo- 
nents of the ‘tensor’ A on the new basis {é;' 1. Show that this ‘tensor’ 
is indeed a tensor as we have defined it. This shows that one can take 
the point of view that a tensor is the collection {4111 transforming in 
the given way. This is an alternative definition to the one we have 
used. 
It is of particular interest to look at these basis transformations when they 
result from coordinate transformations, which were mentioned briefly at the 
end of §2.6. Suppose a region U of the manifold M has a coordinate system

## Page 73

2.27 Tensor operations on components 
63 
fx i=1,...,m}, and that we introduce new functions (νε, i=1,...,n} 
given by the equations 
yi = fi@l,...,x”), i = 1,...,n, 
(2.39) 
which can be summarized as yi =f U(x) ). These equations constitute a coordi- 
nate transformation if the Jacobian matrix of partial derivatives ay! / 
dx! has 
a nonvanishing determinant in U. A given point P in U can be described by two 
different sets of numbers, {x'} or {γή }. At P we likewise have two different 
coordinate vector bases, {0/ Ox! hand, by the chain rule of calculus, 
0 
ax’ 
ὃ 
—~_ 
= TT TY. 
2.40 
dy' 
ὃὂγ' ax? 
2.49) 
By comparing this with (2.32) we learn 
. 
Ox! 
Ain = a 
(2.41) 
M 
Similarly, the inverse matrix is 
’ 
ὃν 
ΛΑ; = πα 
(2.42) 
which is easily proved using the chain rule for partial derivatives: 
ax! ay? -- δα. _— δὲ, 
dy? ax® ~— ax? 
It is important to understand that (2.42) defines only a restricted class of 
transformation fields AF, in U. At any one point Pin U one can choose all 
n* elements of AF, arbitrarily (apart from the requirement that its determinant 
should not vanish), but not so in the neighborhood of P, because (2.42) implies 
AF (ax! = aA® ax, 
(2.43) 
a symmetry that an arbitrary field AF, certainly would not need to satisfy. This 
is another illustration that not every field of basis vectors is a coordinate basis. 
2.27 
Tensor operations on components 
Given a tensor T and its components {7 a j...} on some basis, suppose 
one multiplies each component by the number a, thereby obtaining {aT . i...) 
These are clearly components of the tensor aT, and this means that the oper- 
ation of multiplying all the components of T by a is basis-invariant: had we 
begun in coordinates fy we would have obtained the components of aT in these 
new coordinates. (One could not say the same had we multiplied only some of 
{T'--;_ \by a.) Thus, the operation «Τί, 
}> {aT*;_ } 
uniquely corresponds 
to the basis-independent statement T > aT. Similarly, the outer product of two 
tensors,

## Page 74

Differentiable manifolds and tensors 
64 
A,B>A®B, 
has the unique component analogue (cf. exercise 2.4) 
αμ. 
independently of what coordinate or noncoordinate bases are used. In general, 
an operation on components that produces components of the same tensor 
independently of the basis is called a tensor operation, and we will deal exclu- 
sively with them. The following list is a summary of the algebraic tensor oper- 
ations (we shall consider ones involving differentiation later): 
(i) Addition (and subtraction) of components of tensors of the same type. 
(ii) Multiplication of all components by a number gives a tensor of the 
same type. 
(iii) Multiplication of components of two tensors gives a tensor whose type 
is the sum of the two. 
(iv) Contraction on pairs of indices, one of which is up and the other down. 
An equation that involves components combined using only these operations is 
called a ‘tensor equation’. It follows from exercise 2.10 that if a series of oper- 
ations performed in a certain basis gives a tensor equation, then that equation is 
true in all bases. This often permits a convenient choice of basis for a particular 
calculation. 
2.28 
Functions and scalars 
A scalar is defined as a (9) tensor, ie. a function on the manifold whose 
definition does not depend upon the choice of any particular basis. 
For example, 
the contraction V‘w; is a scalar, since its value is independent of the particular 
basis in which the components are computed. On the other hand, the compo- 
nent V' is also a function on the manifold, having a numerical value at every 
point; it is not a scalar because its value depends on the basis. Put another way, 
there is some (scalar) function f(P) such that Υ (9) = ΓΡ) when the index ‘1’ 
refers to some particular basis; when that basis is changed, the new V'(P) will 
not equal f(P). So f(P) is a scalar, whose value happens to equal that of the one- 
component of V in some basis. But V! is not a scalar since its value changes with 
a change in basis. You see, therefore, that whether a thing is a ‘scalar’ or simply 
a ‘function’ depends on its interpretation when the basis is changed, rather than 
on its actual value. 
2.29 
The metric tensor on a vector space 
Most familiar vector algebras involve an inner product between vectors, 
asin §1.5. This is a rule which associates a number (the ‘dot product’) with two

## Page 75

2.29 The metric tensor on a vector space 
65 
vectors. It is a linear function of both vectors. Therefore it is a (9) tensor, which 
is called the metric tensor, ΟΙ. Thus we define 
+ 
g(V, U) = g\(U,V) = U-vV. 
(2.44) 
The first equality above is a demand that U- V should not depend on the order 
of U and V. We say that gj is a symmetric tensor. Its components on a basis 
{é;} are 
Si = ONG, 2) = 2° &. 
(2.45) 
These components form ann x n symmetric matrix. For reasons explained later, 
we also demand that this matrix have an inverse. If it happens that the matrix is 
the unit matrix, i.e. if 
δη = 
δι), 
we say the metric tensor is the Euclidean metric, and the vector space is called 
Euclidean space. But what can we say if g;; is not this simple? Well, we are 
always free to try to choose a new basis {é,;}in which the new metric com- 
ponents, 
δι 1’ = AP My Spi, 
(2.46) 
are simpler. Consider this equation as a matrix equation. It is helpful to rewrite 
it as 
, 
δι 1’ = 
A SEA j' . 
From the discussion in $1.6 it is easy to see that this is the matrix equation 
g = A'gA, 
(2.47) 
where ΛΣ is the transpose of the matrix A whose entries are A" ,'. We will now 
see that a clever choice of A will reduce the matrix g’ to a very simple form. 
Since A is arbitrary, we will take it to be the product of two matrices 
A = OD, 
(2.48) 
where O is an orthogonal matrix (O' = 071) and D is a diagonal matrix (so in 
particular D? = D). Then we have, from equation (1.41), 
AT = (OD)' = ΡΤΟΣ = DO" 
and 
g = DO'gOD. 
(2.49) 
It is well known that any symmetric matrix, such as g, can be reduced to diag- 
onal form, gg, by a similarity transformation using an orthogonal matrix, so let 
us choose O to do this: 
δα > 
Oo” gO, 
g = Dg,D. 
If gq is the matrix diag(g,,22,...,8,) and our as yet undetermined matrix D is 
diag(d,,d,,...,d,,), then g’ is

## Page 76

Differentiable manifolds and tensors 
66 
g’ = diag(g,d;’,g2d2",...,8ndy’). 
(2.50) 
We now choose d; = (|g;|)””, so that each element on the diagonal of g’ is 
either + 1 or — 1. We cannot use d; to change the sign of g;, only its magnitude. 
Now, the diagonal elements of gg are the eigenvalues of g, and are unique apart 
from the order in which they appear. Moreover, since g has an inverse, none of 
the eigenvalues is zero. If we choose O to make all the negative ones appear first, 
then we have proved the theorem that any vector space with a metric tensor has 
a basis on which the metric tensor has the canonical form diag(— 1,...,—1, 
1,..., 1). Such a basis is said to be orthonormal. The sum of these diagonal 
elements — the trace of the canonical form — is called the signature of the 
metric. 
Exercise 2.12 
Find the matrices A which cast the following matrices into their unit 
diagonal form: 
2 
1 
ο 
1 
4 
0 
ω [ ]. ) ί η, ©) : η. 
This theorem is very important. It means that there are only a few different 
kinds of metric tensors on a vector space. If the metric is positive-definite, then 
its canonical form must have all + 1s, and the space is Euclidean. If the metric 
is negative-definite it is also said to be Euclidean, since what is important for the 
space is whether the signs are all the same or not. If the metric is not of definite 
sign, it is called indefinite. An important case is the canonical form (— 1, 
1,..., 1), whose metric is usually called a Minkowski metric; special relativity 
has such a metric for n = 4, which we will discuss at length shortly. 
Another consequence of this canonical form is that it picks out a preferred 
set of bases for the vector space, the orthonormal bases. In Euclidean space E”,, 
such a basis is called Cartesian. In it the metric tensor has the components 
δι = δῃ, or in matrix form g = J. A transformation matrix Λο from one such 
basis to another satisfies 
T= AéIAg = AG = Λά. 
(2.51) 
So the orthogonal matrices are the transformations between Cartesian bases. 
These matrices form a group (the product of two orthogonal matrices is ortho- 
gonal), which is called the Euclidean symmetry group O(n). A Minkowski metric 
likewise singles out its preferred Lorentz bases in which the metric components 
form the matrix 
η = diag(—1,1,..., 1). 
(2.52)

## Page 77

2.29 The metric tensor on a vector space 
67 
A transformation matrix A;, from one Lorentz basis to another satisfies 
n = AL nAy. 
(2.53) 
Such a matrix is called a Lorentz transformation. It is not hard to show that 
these too form a group, called the Lorentz group L(n) or O(n — 1, 1). 
From the point of view of tensor algebra, the metric tensor’s most important 
role is one we have not yet mentioned: it maps vectors into one-forms in a 1-1 
manner. Consider a vector V. Then g|(V,_) is, for fixed V, a linear function of 
vectors into real numbers: a one-form. We denote this by 
V= αι”, ). 
(2.54) 
The fact that we demanded that the matrix g,; have an inverse is what makes 
this map 1-1: there is only one vector V mapped to V. To see how this works, 
let us look at the component version of this equation. Denote the component 
of V by V;: 
Vg, 2) = Via = ευ”, 
where the last equality follows from the symmetry of g|. Now, the inverse 
matrix to g;; will be called οὐ: 
¢ 
ος], = 
S54. 
(2.55) 
Then we have 
gty, = εσυ) = 6*,Vi = Vv", 
(2.56) 
which shows that the map is invertible: the metric provides a unique pairing 
II 
| 
between one-forms and vectors. This pairing can be summarized: 
9 
Vi = ευ, 
(2.57) 
+ 
Vi= giky,. 
(2.58) 
Notice that we have denoted the elements of the inverse matrix by οὗ, and this 
permits (2.58) to obey the usual index conventions for a tensor equation. But 
for consistency one must show that the numbers g” are in fact components of a 
(2) tensor. This is the object of the next exercise. 
Exercise 2.13 
(a) Show that {g"} are the components of a (6) tensor ϱ| 
1, either by 
showing that they transform properly, or that they define a bilinear 
function on one-forms. 
(b) Show that if a vector basis {6/3 is orthonormal, so is its dual one-form 
basis {G5'}, in the sense that g/'(@', @/) = + 5".

## Page 78

Differentiable manifolds and tensors 
68 
In the same way, the metric can map a (2) tensor A into a (1) tensor: 
Al, = 9A’. 
(2.59) 
In turn this can be mapped into a (2) tensor 
Ay = 81mA™; = &im&jnA™, 
(2.60) 
which can be mapped back into the original tensor 
Al = gilgkm 4 
(2.61) 
These maps are called index raising and lowering, and it is conventional to give 
all these tensors the same name (e.g. A), distinguishing them only by the posi- 
tions of their indices. It is sometimes unimportant in vector spaces with metrics 
to say whether a tensor is of type (43) or of types (> 1), (4 *}), etc. and then 
one speaks only of the order of a tensor, which is 
N+ N’. 
In a Euclidean vector space a Cartesian basis has g;; = 6 ;, so that g” = 6”, 
and U' = U;: there is no difference between the components of a vector and of 
its associated one-form in this case. This is the reason that elementary dis- 
cussions of Euclidean vector algebra fail to distinguish between vectors and 
one-forms, and also why they confine themselves to orthonormal bases. But 
in a nonorthonormal basis for Euclidean space and in any basis in an indefinite 
metric space, the components of a one-form can be very different from those of 
its vector. We will see an interesting example of this in the section on special 
relativity, $2.31 below. 
2.30 
The metric tensor field on a manifold 
A metric tensor field Οἱ on a manifold is a (8) symmetric tensor field 
which must have an inverse at every point. At every point P it serves as a metric 
on the tangent space ΤΡ, and all the properties discussed in the previous section 
carry over directly. But there is much more. 
The definition of a certain (9) tensor on a manifold M as the metric of the 
manifold endows M with a very rich structure. It immediately becomes ‘rigid’: 
one can define such notions as distance (see below) and curvature (see chapter 
6). These notions are so important in many applications, particularly in general 
relativity, that it is this sort of geometry that a physicist is most likely to be 
familiar with. But this is, from the point of view of differential geometry, a 
‘higher level’ structure: one goes beyond the notion of a simple differentiable 
manifold by picking out a certain tensor field as special. In doing this one may 
overlook the rich geometrical structure of the ordinary manifold itself. Such 
important tools as Lie derivatives and differential forms have nothing to do 
with metrics. Accordingly we shall put the metric tensor very much in the back- 
ground in this book, even in applications to manifolds on which one is defined.

## Page 79

2.30 The metric tensor field on a manifold 
69 
In this section we take a brief look at its simplest properties. Further develop- 
ment of metric geometry itself is deferred to chapter 6. 
The metric tensor may be as differentiable as one requires, but it must at 
least be continuous. This implies that its canonical form must be a constant 
everywhere, since it is composed only of integers, and integers cannot change 
continuously. So we speak of the signature of the field g}. As long as one can 
choose the basis transformation matrix A freely at each point, one can trans- 
form from any given basis field to a globally orthonormal basis in which the 
components of ϱ| are its canonical ones. But this transformation field A is 
usually not a coordinate transformation (i.e. it does not satisfy (2.43)), and in 
fact it is generally impossible to find a coordinate basis which is also ortho- 
normal in any open region U of a manifold M (see exercise 2.14). The obvious 
exception is R” considered as a manifold with the Euclidean metric 5,; at 
every point. But even here only the Cartesian coordinates generate an ortho- 
normal basis. An example of this is given in exercise 2.1 for polar coordinates 
in R?. The coordinate basis is orthogonal but not normalized. The rescaled 
orthonormal basis is not a coordinate basis. 
Exercise 2.14 
Show that aC™ metric tensor field ϱ| is locally flat, in the sense that 
any point P has a neighborhood in which there exists a coordinate 
system on whose basis the components g;; have the following proper- 
ties: 
(i) g,(P) = + 6;; (orthonormal form at P) 
(ii) 
(iii) 
(a) 
(b) 
ὃς.. 
oe = 0 
(orthonormal form a good approximation near P) 
Ρ 
07g 
i of ;| 
not necessarily all zero 
(no truly orthonormal 
Ox" 0x" | 
p 
coordinate system) 
Exercise 2.15 
In polar coordinates in the Euclidean plane, find the components of 
the metric on 
the basis {0/dr, 0/00}; 
the basis t, @ of exercise 2.1. Express ἓ, @ in terms of 0/dr and 9/90. 
Exercise 2.16 
Find the components of df and the vector df on both bases of exercise 
2.15.

## Page 80

Differentiable manifolds and tensors 
70 
Here a word of caution is in order. Most treatments of vector calculus in 
curvilinear coordinates in Euclidean space use the components of a vector on 
this kind of orthonormal basis. This permits them to avoid distinguishing 
between vectors and one-forms. But when one compares the expressions we 
obtain below for, say, the divergence of a vector field in terms of its compo- 
nents with expressions given in other treatments, one must allow for possible 
differences of basis. 
An important property of the metric is that it permits a definition of length 
on the manifold. If a curve has tangent V = dx/dA, then a displacement dd has 
squared length 
αἱ = de : αχ 
(Vdd) - (Vda) = V- Vdd)? 
g\(V, V) da’. 
(2.62) 
(Here the symbol ‘d’ is the infinitesimal, not the gradient.) If a metric is positive- 
definite, then g|(V, V) > 0 for all V 
#0. In such a case d/? is positive and we 
have 
II 
di = (g/(V, V))? da 
(2.63) 
as the length of an element of the curve. In an indefinite metric, however, the 
squared length is not of definite sign. Curves are distinguished by having d/? 
positive (‘space-like’) or negative (‘time-like’). Then one defines the real number 
dl = |g\(V, Vy"? da 
(2.64) 
to be ‘proper distance’ for space-like curves and ‘proper time’ for time-like 
curves. It is zero for ‘null’ curves. When one has an indefinite metric one must 
be careful to distinguish a vector of zero norm from a vector which is truly zero 
(all its components vanishing). 
2.31 
Special relativity 
The vector space R* equipped with a metric of signature + 2 and con- 
sidered as a manifold is one of the most important manifolds in physics: it is 
Minkowski spacetime, the spacetime of special relativity. Elementary treatments 
of special relativity often do not introduce the metric tensor explicitly, but they 
do provide us with all we need to see what the metric must be. In particular, we 
know that there exists a preferred set of coordinate systems for spacetime, called 
Lorentz frames, and that if two events are separated by coordinate intervals 
(At, Ax, Ay, Az) in such a frame, the number 
As* = —c?(At)* + (Ax)? + (Ay)? + (Azy’ 
(2.65) 
is independent of the Lorentz frame. (Here c is the speed of light.) Let us rescale 
our coordinates by defining x° = ct,x'! =x,x? =y,x? =z. (It isa common 
convention to use numerical indices beginning with O rather than 1 in relativity.)

## Page 81

2.32 Bibliography 
71 
Let us also follow the convention of letting Greek letters represent spacetime 
indices. This will help us distinguish discussions applicable only to relativity 
from those of more general scope. Then equation (2.65) has the form 
As? — 
— (Ax°)? + (Ax!) + (Ax?) + (Ax?)* 
= Nogdx*Ax®, 
(2.66) 
where Ώαρ is the matrix 
Nog = diag(— 1, 1, 1, 1). 
(2.67) 
We now interpret (2.66) as defining the pseudo-norm (§1.5) of a vector Ax 
whose components are (Ax°, Ax', Ax’, Ax*). It is easy to see that this pseudo- 
norm satisfies axioms (Nii) and (Niv) of §1.5, which are required for an inner 
product to be defined. This is clearly 
VW = nogV°V®, 
(2.68) 
and so we see that Ώαρ is in fact the metric tensor in canonical form and the 
Lorentz frame is the associated orthonormal basis. 
This metric gives a good illustration of the difference between the com- 
ponents of a vector and its associated one-form. In a Lorentz frame 
Uy = πού. = —U°*, 
(2.69a) 
U, = U*,U, = U*,U,z = U*. 
(2.69b) 
Consider the vector gradient of a function f, which is the vector mapped from 
the one-form df. The gradient df has components (df/0x° , of/dx',...) while 
the vector df has (— df/dx°, af/ax!,...). Many treatments of special relativity 
introduce the gradient as a vector operator with components (— 0/dx°, 
d/dx',...). This odd sign is a clumsiness forced by the fact that the gradient 
is really a one-form. 
A manifold M with a metric g| is called Minkowski spacetime only if there 
exists a single coordinate system covering all of M in which g| has components 
Nag. This coordinate system is a good one to work in, but it is not the only one 
possible on M. One can perfectly well choose others, such as those associated 
with accelerated observers. Provided one follows the general rules of differential 
geometry one will get the correct physical results. 
2.32 Bibliography 
For a more precise and rigorous discussion of what is meant by a 
manifold, and particularly of the rich and useful structure of fiber 
bundles, see Y. Choquet-Bruhat, C. DeWitt-Morette & M. Dillard-Bleick, 
Analysis, Manifolds, and Physics (North-Holland, Amsterdam, 1977). 
See M. Spivak, A Comprehensive Introduction to Differential Geometry 
(Publish or Perish, Boston, 1970) vol. 1, pp. 8—54, for a proof of the 
fixed-point theorem using cohomology theory (after studying $4.24

## Page 82

Differentiable manifolds and tensors 
72 
below!). The tangent bundle and related structures are also discussed 
in R. Hermann, Vector Bundles in Mathematical Physics, two volumes 
(Benjamin, Reading, Mass., 1970); and in R. Abraham & J. E. Marsden, 
Foundations of Mechanics, 2nd edn (Benjamin/Cummings, Reading, 
Mass., 1978). A discussion of fiber bundles in the context of modern 
research in quantum field theory and gravitation is B. Carter, Under- 
lying mathematical structures of classical gravitation theory, in Recent 
Developments in Gravitation, ed. M. Levy & S. Deser (Plenum, New 
York, 1979). See also the article by A. Trautman, Rep. Math. Phys. 10, 
297 (1976). 
Function spaces are discussed in Choquet-Bruhat et al. and in any 
textbook on functional analysis, such as F. Riesz & B. Sz.-Nagy, 
Functional Analysis (Ungar, New York, 1955). The theory of distri- 
butions (the Dirac delta function) is discussed in Choquet-Bruhat et al. 
(1977), and in G. Friedlander, The Wave Equation on a Curved Space— 
Time (Cambridge University Press, 1976). 
The matrix algebra needed to reduce the metric tensor to canonical 
form may be found in the references quoted in chapter 1. A good 
reference for vector calculus in Euclidean three-space in curvilinear 
coordinates is Functions of Mathematical Physics, by W. Magnus & 
ΓΕ, Oberhettinger, chapter 9 (Chelsea, New York, 1949). The metric 
structure of the manifold used in special relativity (Minkowski space) 
is introduced at an elementary level in Spacetime Physics, by E. F. 
Taylor & J. A. Wheeler (Freeman, San Francisco, 1963). Minkowski’s 
own exposition of the subject is reprinted in The Principle of Relativity, 
edited and translated by W. Perrett & G. B. Jeffery (Dover, New York, 
1924). As an example of a discussion of the vector gradient in special 
relativity without benefit of one-forms, see The Feynman Lectures on 
Physics, R. P. Feynman, R. B. Leighton & M. Sands, vol. 2, $25-3 
(Addison-Wesley, Reading, Mass., 1964). 
The Euler angles and other parameterizations of the rotation group 
are discussed at length in H. Goldstein, Classical Mechanics (Addison- 
Wesley, Reading, Mass., 1950). The student may find it helpful to read 
Goldstein’s treatment in conjunction with our discussion of the rota- 
tion group in chapter 3 below.

## Page 83

3 
LIE DERIVATIVES AND LIE GROUPS 
3.1 
Introduction: how a vector field maps a manifold into itself 
In the previous sections we have developed certain aspects of index 
notation. This notation is often essential for dealing with actual numerical 
computations; but it is just as often a hindrance in developing a sound geometri- 
cal idea of what the mathematics means. We begin by defining vectors and 
tensors in a manner independent of any basis, and we now continue in this spirit 
to develop what is one of the most useful analytic tools in geometry: the Lie 
derivative along the congruence defined by a vector field. 
We have mentioned the idea of a ‘congruence’ in §2.12: a set of curves that 
fill the manifold, or some part of it, without intersecting. Each point in the 
region of the manifold M is on one and only one curve. Since each curve is a one- 
dimensional set of points, the set of curves is (n — 1)-dimensional. (With some 
suitable parameterization, the set of curves is itself a manifold.) The key point 
from which everything else follows is that the congruence provides a natural 
mapping of the manifold into itself. If the parameter on the curves is A, then any 
sufficiently small number AA defines a mapping in which each point is mapped 
into the one, a parameter distance AA further along the same curve of the 
congruence (see figure 3.1). This is a 1~1 mapping, at least in any region in 
which the vector field is sufficiently well-behaved (a C’ field will do). If the 
vector field is 
C”, the mapping is a diffeomorphism (see §2.4.). If the map exists 
Fig. 3.1. The mapping of M to itself defined by mapping each point to 
the point on the same curve of the congruence whose parameter is some 
fixed number AA larger.

## Page 84

Lie derivatives and Lie groups 
74 
for all AX, there is a one-dimensional differentiable family of such mappings (a 
one-parameter Lie group, in fact, with composition law AA, + Δλ2). Such a 
mapping is called a ‘dragging’ along the congruence, or a Lie dragging. 
3.2 
Lie dragging a function 
If a function fis defined on the manifold, then the mapping defines a 
new function fA, by ‘carrying’ f along the congruence in an obvious manner: if a 
point P on a certain curve in figure 3.1 is mapped to the point Q, a parameter 
distance Δλ further along the same curve, then the new field fA has the same 
value at Ο as fhad at P, 
¢ 
FP) = far). 
(Here the asterisk on fA, simply means ‘new’.) If it happens that the value 
FAn(Q) in fact equals the old value at the point Q, f(Q), for all Q, 
f = faa, 
then the function is invariant under the mapping. If the function is invariant for 
all AX then it is said to be Lie dragged. Clearly, a function that is Lie dragged 
must be constant along any curve of the congruence: df/dA = 0. 
3.3 
Lie dragging a vector field 
To see the effect this map has on vector fields, recall that any vector 
field is defined by the congruence of curves for which it is the tangent field. In 
Fig. 3.2. How a new vector field d/duA is defined by Lie dragging its 
path and its parameter µ. Curves (1)—(4) are members of the A- 
congruence. Curve (A) is a u-curve passing through P and is mapped to 
curve (4) by being Lie dragged a parameter distance AA. Curve (B) is a 
µ-ουτνε of the old congruence also passing through Q. The image of (B) 
under the dragging is not shown. In general (B) and (4) will be different 
curves. If they are the same the u-congruence is said to be Lie dragged. 
(1) 
(2) 
(3) 
(4)

## Page 85

3.3 Lie dragging a vector field 
75 
figure 3.2, we show two congruences: one, for d/dA, generates a map of the 
manifold; the other, which defines the arbitrary field d/dy, will be acted on by 
the map. This action is very simple: any curve of the u-congruence is mapped 
into a new curve which runs through the images under the Lie dragging of the 
points it used to run through, and the parameter values µ are carried along to the 
new points as well. This defines a new congruence with parameter μἈλ. This new 
congruence has a tangent vector field d/du’,,, which is called the image of d/du 
under the Lie dragging. 
In general the uw ,-congruence is different from the u-congruence. If it is the 
same, then d/du’, = d/du everywhere and we say the vector field and congru- 
ence are invariant under the map. If they are invariant for all AX then we say 
they are Lie dragged by the vector field ά/ἀλ. 
A Lie dragged vector field has a simple geometric interpretation, illustrated 
by figure 3.3. It is clear that (in the limit of infinitesimal Ad and infinitesimal 
separation between curves (2) and (3)) if d/du at P ‘stretches’ exactly from P to 
R on curve (A), then ἆ/[άμἈλ stretches exactly from Q to S on (4’). If d/dy is Lie 
dragged, then curve (B) of figure 3.2 coincides with (A’) and (d/duAy eg 
= (d/du)g, 5ο d/dy also stretches from Q to S. Referring to our discussion of Lie 
brackets in §2.14, we find that this implies [d/dA, d/du] = 0: a vector field is 
Lie dragged if its Lie bracket with the dragging field vanishes: 
[ά/άλ, d/du] = 0. 
(3.1) 
There is another way to see the same thing. Suppose we look at figure 3.3 dif- 
ferently, as if we were given only a single curve (A) with parameter yu, not a 
whole congruence. Then we can generate from this curve a whole congruence by 
Lie dragging it for all possible values of AX. One such curve is (A’). Let us call 
this field d/du;, with parameter pyz,. By this construction, the derivative d/da” is 
Fig. 3.3. The central section of figure 3.2, with curve (B) omitted and 
the tangent vectors to (A) and (A’) at P and Q respectively drawn in.

## Page 86

Lie derivatives and Lie groups 
76 
always on a curve of fixed µ and the derivative d/duz, is always on a curve of 
fixed λ. Therefore they must commute. 
3.4 
Lie derivatives 
The concept of dragging permits the definition of a derivative along the 
congruence. There is a difficulty inherent in any attempt to define derivatives of 
vector and tensor fields. Consider trying to define a vector field’s derivative as 
the limit of the difference between the vectors at different points divided by the 
distance between the points. One problem is defining “distance’ between points; 
if one has a curve between the points, one can take this to be the difference 
between the parameter values at the points. (This gives a derivative with respect 
to the parameter, and on manifolds without metrics this is all one can hope for.) 
A more serious problem is the comparison of vectors at different points: are two 
vectors at different points ‘parallel’ or not? In the Euclidean plane this is a 
simple question to answer. On a curved surface it may not have a unique answer. 
On a simple differentiable manifold the question of parallelism at different 
points does not even make sense, since there are no ‘markers’ or rules for moving 
vectors around in a parallel manner. One must add more structure — called an 
‘affine connection’ — to the manifold in order to define an absolute parallelism. 
This is treated in chapter 6 on Riemannian geometry. What we shall consider 
here is an alternative that one should expect to find useful in any problem in 
which a congruence plays a central role. The congruence itself can provide a sub- 
stitute for the concept of parallelism at different points. That is, when compar- 
ing vectors at points A and A + Δλ on a certain curve, one can Lie drag the 
vector at λ + Ad back to the point A. This defines a new vector at A, which can 
be subtracted from the old one to define the difference between them. Notice 
that this is a unique difference, and hence a unique derivative, given the congru- 
ence. But it does depend on the congruence. 
Let us derive analytic expressions for this. First consider a scalar function. 
Evaluate the scalar at the point Ag + AA, drag it back to Ag, subtract the value of 
the scalar at Ao, divide by AA and take the limit AA > 0. Its value at Ag + AA” is 
f(\o + AA). By dragging one defines a new scalar field 
f*, whose value is defined 
by the rule df*/dd = 0. Therefore its value at Ag is the same as at Ag + AX: 
f*(Xo) =f(Ao + AA). The derivative so defined is 
km 
{ ο) FO), {ο 
AN =SQo) _ Ee 
im ———-- = odin = 
|--- 
Δλ-»0 
Δλ 
Δλ-»0 
Δλ 
The result for the Lie derivative of fis not, of course, surprising. There is a 
special notation for the Lie-derivative operator: £5, where V is the vector field 
generating the mappings (d/dA in our case). We have proved that for functions

## Page 87

3.4 Lie derivatives 
77 
+ 
£of = Vif) = ἁ[άλ. 
(3.3) 
Now we do the same for a vector field U = d/du. Since a vector is defined by 
its effect on functions, we use an arbitrary function fin what follows. At λρ the 
field U gives the derivative (df/du),,, while at Ag + Δλ it gives (df/du), 4 
an. By 
dragging U(Ay + AA) in the sense of §3.3, one gets a new field U* = d/dy*, 
defined by (U*, V] = Oand by ὃ (λο + AA) = (Xo + Ad). The vanishing of 
the commutator implies 
d d 
d d 
and 
= du* da? 
(3.4) 
everywhere. Therefore we have (for analytic vector fields) 
d 
d 
d/d 
fl 
[ης 
—~arj—{(—<f]| 
+ o(ar 
a 
Ro 
ή, 
Entra] Xo 
(An) 
a f 
— Ar Pas ὴ + Ο(Δλ2) 
duo 
y+ aa 
du"\dr" } |x, 
=~ 
{2 rl +ari2(o 
ld η 
dn au! r, 
-- 
d 
d 
2 
on) {e 
i). 
+ O(AX). 
We define the Lie derivative £>U as the vector field which operates on f to give 
[Foo Ma) 
eee 
Cb 
(3.5) 
— 
j—ae 
[£7U](S) 
dd 
dd 
lim 
μα —f- Par —f 
. 
Δλ-ο 
\dA du 
du* ἆλ 
Now, the difference between μ” and µ is clearly a term of first order in AA, 
which means we can replace μ΄ by µ in the last equation above. Since this 
equation is true for all f, we have 
— 
d-—~ 
de 
— 
4 
£{£pU = —U—-—V 
= 
[V,U}. 
3.6 
ντ 
[0-7 v= 10,0) 
6.9 
This is again a sensible result. By definition of the Lie derivative along V, a 
vector field has a zero Lie derivative if it is Lie dragged, i.e. if it has zero Lie 
bracket with V. Therefore it makes sense that its derivative is in fact its Lie 
bracket. By the antisymmetry of the Lie bracket we find 
£oU = --4Ργ. 
(3.7)

## Page 88

3.5 
(a) 
(b) 
(a) 
(b) 
Lie derivatives and Lie groups 
78 
Exercise 3.1 
Show that, on functions and fields, 
fv, £0] = fry 
(3.8) 
for any two twice-differentiable vector fields V and W. 
Prove the Jacobi identity for Lie derivatives on functions and vector 
fields: 
[[£z, εν]. fz] + ([£y, £2], £z] + [[£z, £z], £e] = 0, 
(3.9) 
where X, Y, Z are any three-times-differentiable vector fields. 
(Hint: for (a) on vectors, show that (3.8) is equivalent to (2.14). For 
(b) on vectors, use (3.8) and the fact that, as is obvious from its defi- 
nition, £4 + £— = £4.35.) 
Exercise 3.2 
Deduce the Leibniz rule 
LAfU) = (E~f)U 
+ fioU 
(3.10) 
from the definitions of £7 on functions and vector fields. 
From (2.7) we know that the components of £7U on a coordinate basis 
are 
_ 
. 
0 
9 
(fpUy = V η U'—U! Si V'. 
(2.7) 
Given an arbitrary basis {e;} for vector fields, show from (a) that 
(£pU) = V'e(U') — σεν) + VU" (£5.24), 
(3.11) 
where e;(U*) means the derivative of the function U’ with respect to 
the vector field e;. 
Exercise 3.3 
Show that if one chooses a coordinate system in which V 
is a coordi- 
nate basis vector, say 0/dx', then for any vector field W 
(Εν)! = ow'/ax!. 
(3.12) 
That is, the Lie derivative is the coordinate-independent form of the 
partial derivative. 
Lie derivative of a one-form 
Since fields of one-forms and tensors of higher rank are defined in terms 
of vector fields and scalar functions, one can deduce the Lie derivatives of one- 
forms from the Lie derivatives of vectors and scalars. Conceptually, the definition 
is the same: a one-form field is said to be Lie dragged if its value on any Lie

## Page 89

3.6 Submanifolds 
79 
dragged vector field is constant. The Lie derivative is found by dragging the one- 
form at Ag + AA back to Ag and taking the difference. The result is that if @ is a 
one-form, then £7 is the one-form field which is the Lie derivative of ὢ along 
V defined by the product rule (just the Leibniz rule for first-order derivatives): 
£7[G(W)] = (£pS)(W) + BLpw) 
(3.13) 
for all vector fields W. Since G(W) is simply a function, this defines £7 in 
terms of known operations, the Lie derivative of functions and vector fields. 
Exercise 3.4 
From (3.13) and the expression (2.7) for the components of 
£7W =[V, W], deduce that £>@ has components, on a coordinate 
basis, 
. 
O 
0 
; 
Sy) ωι + wa VV!” 
(3.14) 
1 Ox! 
The natural extension of (3.13) to tensors of higher type gives the Lie deriva- 
tive the properties. 
£7(A Φ8Β) = (£7A)©B+A 
® (£7B) 
(3.15) 
εφ(τ(ῶ.... 
0... .)) = (£¢T)\(@,...5U,...) 
+ T(£p@,...3;U,...)4+... 
+1(@,...3£7U,...)+..., 
(3.16) 
where A, B, T are arbitrary tensors and @ and U arbitrary one-form and vector, 
respectively. 
an 
3.6 
Submanifolds 
A submanifold of a manifold Μ is a manifold which is a smooth subset 
of M. If M is ordinary three-dimensional Euclidean space, then ordinary smooth 
surfaces and curves are submanifolds. In four-dimensional Minkowski spacetime 
(§2.31), the three-dimensional space of events simultaneous to a given event in 
the view of a particular observer (same time coordinate {) is a submanifold, and 
so is the hyperboloid of all events at constant interval As” from a given event. 
The word ‘hypersurface’ is sometimes used instead of ‘submanifold’, but some 
textbooks use ‘hypersurface’ only to describe a submanifold whose dimension is 
one less than that of M. 
Although the idea of a submanifold is easy enough to visualize in simple 
cases, the word ‘smooth’ in the definition given above needs to be made more 
precise, and different textbooks give different (and inequivalent) definitions. We

## Page 90

Lie derivatives and Lie groups 
80 
shall use the one which guarantees the greatest smoothness and is closest to our 
definition of a manifold. An m-dimensional submanifold S of an n-dimensional 
manifold M is a set of points of M which have the following property: in some 
open neighborhood in M of any point P of S there exists a coordinate system 
for M in which the points of S in that neighborhood are the points characterized 
by xt =x? =...=x""™ = 0 (see figure 3.4). A one-dimensional submanifold is 
a kind of curve, and its smoothness requirement is illustrated in figure 3.5. It is 
clear that the definition of S guarantees it is itself a manifold, since it has the 
requisite coordinate patches (charts). A special case is m =n: any open set of M 
is a submanifold of M. 
Our interest in submanifolds stems mostly from the fact that solutions of 
differential equations are usually relations, say {y; =f,(x',...,x™),i=1, 
. 
,p}, which can be thought of as submanifolds with coordinates {x',... , x} 
of a larger manifold whose coordinates are {y;,... Vp» X', ...,x}, We shall 
begin our investigation of submanifolds from a different perspective, however, 
and the tie-in with differential equations will not come until chapter 4. 
Suppose P is a point of a submanifold S (dimension m) of M (dimension n). A 
curve in S through P is also a curve in M through P, so naturally a tangent vector 
to such a curve at P is an element of both ΤΡ, the tangent space to 
M at P, and 
Vp, the tangent space to S at P. In fact, Vp is a vector subspace of Tp of dimen- 
sion m. On the other hand, an arbitrary vector of Tp not in Vp has no unique 
‘projection’ onto Vp (recall there is no notion of orthogonality in general). 
Fig. 3.4. A two-dimensional submanifold S of a three-dimensional mani- 
fold M is shown, along with coordinates near a point P which satisfy the 
definition given in the text. The coordinate line of x! intersects S only 
at P. 
Fig. 3.5. A candidate for a one-dimensional submanifold of a two- 
dimensional manifold, which fails because it crosses itself at P. At P one 
cannot construct the necessary coordinates. Only some curves, there- 
fore, are submanifolds.

