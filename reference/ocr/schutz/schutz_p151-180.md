<!-- source-pdf: Bernard F. Schutz-Geometrical Methods in Mathematical Physics-Cambridge University Press (1980).pdf | pages 151-180 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 151–180

## Page 151

4.19 Proof of the local exactness of closed forms 
14] 
@ =a, ,(x',...,x™dxia...n dx®, 
(4.59) 
where each component a;_», has p indices. Contract & with the ‘radial vector’ 
7 whose components at any point on the coordinate basis are (x',...,x”), and 
call this (p — 1)-form fi. It is, by equation (4.13), 
f= QF) = ay px'dxi an... adx®. 
(4.60) 
Now we define the functions 
1 
β να. κ... αχ) = [ tP a νέα) 5 tx? , wey tx”) x'dr. 
(4.61) 
This integral is along the radial line in the coordinate system which {x'} happens 
to lie on. The functions define a (p — 1)-form B 
B= By ndxin...adx®, 
and the claim is that ¢ = dg. 
The proof of this claim is straightforward algebra. From (4.45) we have 
wm 
0 
(dB). = P μη Bj...) - 
(4.62) 
The derivative is easy: 
ὃ 
1 
πλ. = [ tP ays A (tx’ λ. 9.5 tx") dt 
1 
+ [ tPx'oy; κ (tx',..., ox”) dt. 
(4.63) 
In order to antisymmetrize this on [i ...k] we invoke (for the first time) the 
closure of @: 
O = απ. νη 
= αι]... μι] αι. 
ΕΠ 
απ)... i Ui...R], b> 
(4.64) 
where vertical bars separate out an index which is not included in the anti- 
symmetrization implied by | |. But the components of @ are already anti- 
symmetric on all indices, so the first p terms are equal, and we have 
O = pajrj...r,i) 
— fij...kI,1- 
(4.65) 
Putting this into the second integral of the antisymmetrized version of (4.63) and 
inserting this into (4.62) gives 
~~ Aw 
1 
_ 
(dB )ij...% =|. [ptP aj; 2(tx',..., x”) 
+ t?x'oy; κ (tx',..., x”)] de 
. 
d 
1 
n 
| Gp Lo iin κχ ,...,0x”)] dt 
0 
= Oyj p(X"... + 5X"). 
(4.66)

## Page 152

Differential forms: differential calculus 
142 
This proves the theorem. 
Exercise 4.17 
Prove equations (4.64) and (4.65). 
Exercise 4.18 
Use the local exactness theorem to show that locally (in three- 
dimensional Euclidean vector calculus) a curl-free vector field is a 
gradient and a divergence-free vector field is a curl. 
There are two cautionary observations to be made here. The first is, as noted 
in §4.18, the (p — 1)-form 8 we constructed is not the only one for which 
dg = &. The second is that we have merely given a sufficient condition for a 
closed form to be exact. Cohomology theory reveals many more complicated 
manifolds on which a closed form is still exact. (See $4.24.) 
4.20 
Lie derivatives of forms 
We shall prove the following useful expression for the Lie derivative of 
a p-form & with respect to a vector field V: 
9 
εφῶ = d[a(V)] + (de) (V). 
(4.67) 
That is, the p-form £7 is the sum of two p-forms; the first is the exterior 
derivative of &(V), the contraction of @ on V; the second is the contraction 
of d@ on V. The proof is rather long and may be omitted on a first reading. 
The result, (4.67), has a nice naturalness: £7@ is a p-form involving V and 6; 
if it can be constructed using d at all (which we should expect, since both 
derivatives involve only the differential structure of the manifold), then it must 
involve the only two p-forms which one can construct from V, ὤ, and d. In fact, 
it is just their sum. 
The proof proceeds by induction. We shall drop tildes over the symbols in the 
rest of this section, for the sake of clarity. 
The first part of the proof is the case where w is a zero-form, a function f. 
Then its contraction on V is by definition zero, while its exterior derivative is df. 
If V = d/dd, then we know that df(V) = df/da, but this is also equal to £7f 
= V(f) = df/dix. This proves the expression in the simplest case. 
The next case is w, a one-form. Then we use component notation: 
WV) = wV'> d[a(V)] = (ωμ) 
| 
pdx? 
da = d(w;dx') = (dw,) 
a dx! 
ww, dx! 
n dx? = «3; (dx? 6 dx! — dx! ® dx’)

## Page 153

4.21 Lie derivatives and exterior derivatives commute 
143 
> (dw)(V) = ww, ;[dx4(V) 
dx? — dx'(V) dx] 
= 0; Vi dx! — ww; V' dx’. 
These expressions combine to give 
4[ω(γ)] + dex(V) = [ωμή + oV4 ἡ be’, 
which is the same as £7w from equation (3.14). 
The rest of the proof proceeds by induction. Since a general p-form can be 
represented as a sum of functions times wedge products of p one-forms, as 
| 
w= pf 
Cota 
A oe Nn dx®, 
it suffices to prove the theorem for a form which can be written as 
w = fanb, 
(4.68) 
where we assume the theorem has been established for a and b. Then we have 
Low = (fLpfpanb+ f(£ya)nb + 
fan (£7d) 
= dfV)anb+ f{d[a(V)] + (da) (V)ta b 
+ fan {d[b(V)] + (db) (V)}. 
But we also know that (if α is a p-form) 
d[w(V)] = d[faV)ab+C 1)?fand(V)] 
= df[@@ab)(V)] + fd[aV)] 
0b +G 1)? ta(V) κ db 
1 
+ (—1)?danb(V) Γαλ [db(V)]}, 
. 
(dw)(V) = [dfnanb+ 
fdanb + (— 1)?fan db] (1) 
dfVV)anb— dfn [an b)(V)| + f[daVV) a b 
+ (—1)P*! dan D(V) + (-- 1)?a(V) a db Γαλ db(V)]. 
Thus, adding these gives the same expression as for £7w above. This establishes 
the expression’s validity for general forms. 
4.21 
Lie derivatives and exterior derivatives commute 
A very important consequence of (4.67) is the fact that Lie and 
exterior differentiation commute: (4.69) below. To prove this, note that for any 
form w (again omitting tildes for clarity), 
fydw = d[(dw)(V)I, 
since ddw = 0. But, by using the Lie derivative formula once more we have 
(dw)(V) = ὄνω-- ἀ[ω(γ)]. 
So that (again because dd = 0) we get 
+ 
ἁφ(άω) = d(Lpw). 
(4.69)

## Page 154

Differential forms: differential calculus 
144 
Lie differentiation and exterior differentiation commute! This is actually a 
special case of a more fundamental property of d which is established in more 
complete treatments of the subject, namely that there is a sense in which d 
commutes with any differentiable mapping of the manifold. (This commutation 
property may make it easier for you to prove the second-to-last part of exercise 
3.9!) 
4.22 
Stokes’ theorem 
We are now in a position to show that exterior differentiation and 
integration are inverse to one another. Since integration of forms on an n- 
dimensional manifold is defined only for n-forms, the inverse property applies 
only to exterior derivatives of (n — 1)-forms. Moreover, since only definite inte- 
eration of n-forms is defined (i.e. the integral produces a number, not another 
form), the inverse relation analogous to equation (4.43) at the beginning of part 
B of this chapter will have to relate the integral of the n-form dé to another 
integral, that of ὤ. But the (n — 1)-form @ can be integrated only over (n — 1)- 
dimensional hypersurfaces, so we are led naturally to look for a theorem relating 
the integral of dé3 over a finite region to the integral of 6 over the region’s 
boundary, which is (n — 1)-dimensional. Our approach to this theorem (equation 
(4.75) below) will, however, be somewhat indirect, in order to avoid some of 
the lengthy calculations the usual proofs employ. We shall begin by looking at 
the change (to first order) in the value of an integral when the region of inte- 
gration is slightly changed. 
Accordingly, let us consider the integral of an n-form @ over a region U of 
an n-dimensional manifold Μ. Let U have a smooth orientable boundary called 
dU, by which we mean an orientable submanifold of Μ of dimension η — 1 
which divides M—dU into disjoint sets U and CU (the complement of U) in such 
a way that any continuous curve joining a point of U to a point of CU must 
contain a point of 0U. For simplicity we will assume 0U is connected, although 
this is not necessary. Examples are given in figure 4.10. Now let & be any vector 
field on M, and consider a change in the region of integration generated by Lie 
dragging the region (but not the form ὤ) along ἕ. Thus there is a family of 
regions U(e) and boundaries dU(e) obtained by moving along £ a parameter 
distance ε from the original ones, 
U = U(O) and 0U = 0U(O). This is illustrated 
in figure 4.11. 
The change in the integral of @ is simply the integral over 6U(e), the region 
between the boundaries: 
| ῶ-- | 
ῶ = | 
ὤ. 
(4.70) 
U(e) 
U(O) 
ὃ U(e) 
We will calculate this. Let V be a patch of dU covered by coordinates we shall call

## Page 155

4.22 Stokes’ theorem 
145 
{x7 x°,...,x}. By Lie dragging along £, we construct coordinates {x* = e, 
x?,x°,...,x”} for a neighborhood in M of any such patch V in which ἕ is 
not tangent to 90 (see figure 4.12). This defines and provides a coordinate 
system for the region 6 V(e) between 0U(0) and 0U(e) ‘above’ V = Υ{0). We 
will first calculate the integral of 4 over this region and then extend it to all of 
5 U(E). 
In our coordinates we write 
= fl,...,x")dxta...n 
dx”. 
If € is small, its integral is! 
Fig. 4.10. A manifold with a ‘handle’. Curves @, and @, are not 
boundaries since they do not divide M into an ‘inside’ and ‘outside’. 
The union, U @, is a boundary consisting of disconnected sub- 
manifolds. By contrast, @ 3 is a connected boundary. 
Fig. 4.11. The deformation of U = U(0) into U(e) by displacement a 
parameter distance € along the integral curves of ξ. Arrows represent 
the vector εξ (for small €). The region between 0U and 0U(e) is 6 U(e). 
0U(E) 
Ἐ The symbol ο(ε) stands for any function g(e) for which g(e)/e > 0 as e > 0.

## Page 156

Differential forms: differential calculus 
146 
| 
ῶ [ | 
[joe] eta 
6V(e) 
V(O) 
0 
ε| 
f(O,x7,...,x")dx?... dx” + ο(ε) 
ν(ο) 
ε | ὤ(ξ) 
+ ο(ε). 
(4.71) 
ν 
aU 
The last line follows from (4.13) and the fact that 9/9χ1 = &. 
Equation (4.71) is independent of the coordinate we constructed, but it does 
require that ἕ should not be tangent to dU in V. So it obviously applies to any 
region of 907 bounded by points where V 
is tangent to 0U. If these points form 
submanifolds of dU of lower dimensionality (as in figure 4.11), then they will 
not cause a problem. They will just divide dU into different regions V(;) in 
each of which (4.71) holds. If on the other hand ἕ is tangent to 0U in an open 
region in 0U then the Lie dragging simply maps that region into itself and does 
not change the integral of @ at all, so (4.71) still holds, both sides being zero. 
We can therefore apply (4.71) over all of 90 and combine it with (4.70) to get 
aU 
< { 
3 = 
lim. 
+ 
oe 
| 
= 
33(E) 
de J U(e) κ. e> 0 ε 
U(e) “ 
{eo oan low κα 
(4.72) 
Now, we can obtain another expression for (d/de) f @ from the very con- 
struction of the Lie dragging of the region along £; at any new point the inte- 
grand differs from the old one by e£¢@ + ο(ε). We therefore have 
A 
£ | 3 =| 
fee 
(4.73) 
de 
Jue” 
Jue 
** 
" 
But the expression (4.30) for £26 is particularly simple in this case, since dé) is 
an 
(nm + 1)-form and so vanishes identically: 
Fig. 4.12. A coordinate system for the neighborhood of a patch V of 
0 in which ἕ is never tangent to OU. The region 6 V(e) is all the points 
on those integral curves of ἕ that pass through V, and which are a para- 
meter distance Se 
from V.

## Page 157

4.23 Gauss’ theorem and the definition of divergence 
147 
[ εεῶ = | dte(é)]. 
U 
U 
Combining this with our previous expression for (d/de) fy @, we get the diver- 
gence theorem (the reason for whose name will become clear 
in the next section): 
+ 
ιο) = ο. 
(4.74) 
Now, since @ and & are arbitrary, @(£) is an arbitrary (nm — 1)-form. So we can 
rewrite this as 
Stokes’ theorem for an arbitrary (n — 1)-form & defined on M: 
+ 
| da = | a, 
4.75 
oe 
au ἃ 
(4.75) 
where on the right-hand side we must of course restrict & to dU. 
That this is what one knows as Stokes’ theorem in Euclidean vector calculus 
is easily seen by letting M be two-dimensional as in figure 4.11. Then let & be a 
one-form, & = a,;dx!, da = (a; ; αι) dx! ® dx!. The restriction of & to OU 
means allowing it to operate only on/ 
= d/dA, a vector tangent to the curve OU. 
Then we get 
. 
dx! 
; 
| 
(4,2 αι) de® dx? ~ > May OA ~ ϕ, αμάν. 
This is the usual Stokes’ theorem. 
4.23 
Gauss’ theorem and the definition of divergence 
Stokes’ theorem also embodies what is usually known as Gauss’ 
theorem in vector calculus. For example, return to (4.74) and consider co- 
ordinates in which @ = dx!a...A dx”, in some region W of M. Then its con- 
traction with £ is 
; 
ὤ(ξ) = ελλ... nde” — £2 dxtn dx? .. dx® +..., 
(4.76) 
. 
4 [ῶ(ε)] = Edyta dx?n...n dx” 
+ £7 sdet pn dx?ndxen...dx™ 4+... 
= #0. 
By analogy with Euclidean geometry we define the °a-divergence’ of a vector 
field &: 
7 
9 
(άϊνο  ἑ)ῶ = ἀ[ῶ(ξ)Ι. 
(4.77) 
If in the patch V of 0U defined in §4.22 we again use coordinates such that dU 
is a surface of constant x’, then the restriction of @(£) to OU is again 
Olay = Edx?n...nde” = dxl(E)dx?2n...n de”. 
More generally, if 7 is a one-form normal to OU (i.e. Π(η) = O on any vector 7 
tangent to 0U), and if @ is any (n — 1)-form such that

## Page 158

Differential forms: differential calculus 
148 
~ G=nadad, 
then we get 0()lay7 = A(E)@lay. This gives (4.74) in the form 
9 
[, (ἄνο ἐ)ῶ = i Ae, 
(4.78) 
where @ is restricted to 0U and fi n & = G3. If the coordinate system for (4.76) 
covers all of U, then this is 
| 
ο... f en,” x, 
(4.79) 
which is the usual version of Gauss’ theorem in R”. 
Exercise 4.19 
Show that, although @ as defined in (4.78) is not unique, the restriction 
ἄ]ου is unique once 7 is given. Show that 7 is fixed up to the scale 
transformation Π > fii, where fis any nowhere-zero function, and so 
show that ἄ]ου is unique up to ἄ]οι; > f | @lay. In this way conclude 
that 7(E) alr, is unique. 
The arbitrariness of @ in the definition we have used for the divergence of ἕ 
can be eliminated if there is a metric, by using the metric volume element 
(64.13). This is ambiguous up to a sign but (4.34) shows that diva is in fact 
independent of this sign. Equation (4.79) shows that the usual divergence in R” 
uses the form dx!a...A dx”, which is the metric volume element of the 
Euclidean metric. 
Exercise 4.20 
From (4.77) show that, if coordinates are chosen in which & 
= fdx'n...a dx”, then 
ἀνωξ = — (fe), : 
(4.80) 
Exercise 4.21 
In Euclidean three-space the preferred volume three-form is @ = dx 
A dy a dz. Show that in spherical polar coordinates this is @ = r? sin 6 
dra ἆθ κ ἀφ. Use (4.80) to show that the divergence of a vector ἕ 
= aa : 
9/96 + ἕν . 
is, 
0g? 
divé = 
ο. ET) + ο 
£9) + 
δώ

## Page 159

(a) 
(b) 
(c) 
(a) 
(b) 
4.23 Gauss’ theorem and the definition of divergence 
149 
Exercise 4.22 
In fluid dynamics (and in many other branches of physics) one deals 
with the equation of continuity, which is written in ordinary tensor- 
calculus form as 
0p 
Or 
Here p is the density of mass (or other conserved quantity) and V is its 
rate of flow. Defining @ = dx a dy a dz as in exercise 4.21 above, and 
using the comoving time-derivative operator (9/9: + £7) (which we will 
discuss in detail in chapter 5), show that the equation of continuity is 
+ div(oV) = 0. 
ο ἐν] 
(ρῶ) = 0. 
This permits one to regard ρῶ as a dynamically conserved volume 
three-form on the fluid. The ‘volume’ it assigns to any fluid element is 
that element’s mass. 
Exercise 4.23 
Show from (4.77) that another expression for the divergence of a 
vector & is 
divoé = *d*é, 
(4.81) 
where the *-operation is the dual with respect to @ introduced earlier. 
For any p-vector F define 
div,,F = (— 1"? *d*F. 
(4.82) 
Show that diva F is a (p — 1)}-vector. Show that if 6 has components 
€;,_; in some coordinate system, then 
(div. Fie ο pried b 
(4.83) 
in those coordinates. 
Generalize (4.80) to p-vectors, 
Exercise 4.24 
On the sphere S* use Stokes’ theorem to prove that a two-form ὤ is 
exact (is the exterior derivative of another form) only if 
[ 3 = ο. 
Js? 
(Hint: S* has no boundary.) 
Show that the two-form 
@ = x!dx7a dx?

## Page 160

Differential forms: differential calculus 
150 
defined on R® has the following value when integrated over the unit 
sphere S? as a submanifold of κ”: 
[ο 
4 
ω 
Ss? 
. = 37 
(Hint: what is d@ in Κ 33) Since any two-form on S? is closed (why?), 
this proves that not every closed two-form on S? is exact. 
(ο) Show that every closed one-form 8 on ο is exact. (Hint: integrate 
dg over a part of S? ) 
4.24 
A glance at cohomology theory 
Exercise 4.24 above illustrates how Stokes’ theorem may be used to 
study those global properties of a manifold which determine the relation 
between closed and exact forms. Let Z?(M/) be the set of all closed p-forms on 
M (all & such that d& = 0) and let B?(M) be the set of all exact p-forms on M (all 
a@ such that & = dg). Both sets are vector spaces over the real numbers: for 
example, if & and 6 are closed p-forms then a@ + bf is also closed for any real 
numbers a and D. In fact, B? is a subspace of Z”, since ddp = 0. We now show 
how Z?(M) can be split up into equivalence classes modulo the addition of 
elements of B?(M). Closed forms @, and @ are said to be equivalent (@, ~ &,) 
if their difference is an element of ΒΣ(Μ): 
ἂι 5 & 5ᾶι -& = dp. 
(4.84) 
The equivalence class of @, is the set of all closed forms equivalent to it. The set 
of all equivalence classes is called the pth de Rham cohomology vector space of 
M, H?(M). 
Exercise 4.25 
(a) A relation ~ is called an equivalence relation if it has the following 
properties: (i) for any ἄ, & © &; (ii) if @ 5” β then 5” &; and (iii) if 
& * Band 6  ¥ then & ~ ¥. Show that (4.84) does define an equiva- 
lence relation. 
(b) If Z? and B? were, respectively, any vector space and a subspace then 
the set of equivalence classes we have defined is called the quotient 
space of Z? by B”, denoted by Z°/B”.. Show that this is a vector space. 
(You must define addition of equivalence classes. Prove and then use 
the following result: if &@, and @ are in equivalence classes 
A, and A, 
respectively, then the sum of any element A, and any element of A, is 
in the equivalence class of @ + ἄ,.)

## Page 161

4.24 A glance at cohomology theory 
191 
(ο) Consider the vector space R” and its subspace Κ1.. consisting of all 
vectors of the form (a, 0) for arbitrary real a. Show that R?/R',. is the 
congruence of straight lines parallel to the x-axis. 
We can translate the result of §4.19 into the statement that for the open ball 
in n-dimensions or any region U diffeomorphic to it, H?(U) = 0 for p = 1, since 
all closed p-forms are equivalent to one another and hence to the zero p-form. 
It is also easy to compute H°(U), or in fact 
H°(M) for any connected manifold 
M. A zero-form is just a function, so Z°(M) is the space of functions f for which 
df = 0, i.e. the constant functions. This is simply R'. Moreover, since there is 
no such thing as a (— 1)-form, the space B°(M/) is just the zero-function. The 
equivalence relation © is therefore just the usual algebraic equality: constants f 
and g are equivalent (f ~ g) if and only if they are equal (f = g). Therefore 
H°(M) = Z°(M) = ΚΙ. If 
Mis not aconnected manifold then a function in 
Z°(M) need be constant only on each connected component of M, but may have 
different values on different components. Then H°(M) = Z°(M) = ΚΤΠ. where 
m is the number of components of M. 
Exercise 4.24 clearly can be generalized to any number of dimensions and 
shows that H”"(S”) # 0 (part (b)) and H” !(S") = 0 (part (c)). These are special 
cases of 
H"(S") — R', 
H®(S") = 0,0<p<n, 
(4.85) 
H(S") = R}, 
The proof of this plus many other interesting results can be found in Spivak 
(1970, volume 1). Among the many applications of cohomology theory in 
Spivak is the fixed-point theorem: for even n the sphere S” does not possess a 
nowhere-zero vector field. 
Exercise 4.26 
For odd n, find a nowhere-zero vector field on S”. (Hint: regard S?”"*? 
as a submanifold of R*™*? and consider the effect on S*”*! of the 
rotation corresponding to the following matrix of SO(2m + 2): T 
= diag(4,,A2,...,Am4+1), where each 
A; is the 2 x 2 matrix 
cos@ 
—siné 
A= 
sin 0 
cos 0 
independently of 7. Show that the vector field d/d@ on S?"*! which is 
tangent to the congruence generated by this one-parameter subgroup of 
mappings does not vanish anywhere.)

## Page 162

Differential forms: differential calculus 
152 
Exercise 4.27 
(a) Generalize exercise 4.24(b) to show that the (n — 1} form defined on 
κ” 
a = €i. px'dxi an -..A dx” 
(4.86) 
is nowhere zero when restricted to the sphere 8S"! defined by (x!) 
+(7?P+...4+@"P ξι. 
(b) Show that H""'(S""') = R' implies that if @ is any (n — 1)-form on 
S”’' then &@ — αῶ is exact, where a = fgn-1 G/f gn-1 ©. 
(c) By taking the dual of this relation show that if fis any function on 
οἩ 1 it can always be represented in the form f = c + divgV for some 
constant c and vector field V on S™?, 
(d) For the circle S' prove that H'(S'!) = ΚΙ by constructing a function f 
for which df = & — a6, as in (b) above. 
Exercise 4.28 
(a) Suppose a one-form @& on M has the property fz @ = 0 for any closed 
curve & in M. Show that @ is exact, i.e. that there is a function f such 
that ἃ-- df. 
(b) A connected manifold ή is simply connected if every closed curve can 
be smoothly contracted to a single point. Show that M is simply con- 
nected if and only if H'(M) = 0. 
Before leaving the subject of cohomology we must take two short remarks. 
First, the dimension of H?(M) is called the pth-Betti number b? of M. Second, 
although our definition of H?(M) relied on the differential structure of the 
manifold, it is one of the most fundamental theorems of cohomology (the de 
Rham theorem) that the cohomology groups depend only on the topological 
structure of M and not its differentiability. See Warner (1971) for further 
discussion. 
4.25 
Differential forms and differential equations 
The example mentioned in §4.17 of the way in which exterior differ- 
entiation has a natural relation to integrability conditions also illustrates that, 
at least for first-order partial differential equations, there is a natural way to 
write the equations as relations among forms. This is so important that we shall 
expand upon it here. 
Consider the equation 
dy 
dx . 1.2).

## Page 163

4.25 Differential forms and differential equations 
153 
rewritten as 
dy = f(x,y)d. 
(4.87) 
On a two-dimensional manifold M whose coordinates are x and y, we are 
tempted to write the one-form equation 
dy — fdx = 0, 
(4.88) 
where f is now a function on M. What meaning does this equation have? Surely 
on such a manifold the one-forms dy and dx are linearly independent, so (4.88) 
cannot really be true: it is not an identity. But we do not expect it to be an 
identity. It comes from (4.87), which is a relation between ‘increments’ dy and 
dx for solutions only. A solution of (4.87) is a relation of the form y = g(x), 
which defines a curve (or a path, at any rate) in Μ: a one-dimensional submani- 
fold of M. Vectors tangent to this submanifold have slope dy/dx equal to f(, y). 
Consider one such vector V at some point P, with components (1, f(P)). For 
such a vector, dy(V) = f(P) and dx(V) = 1. Therefore the one-form in (4.88) is 
zero on V: 
4 
(dy — fdx)(V) = 0. 
This is the meaning of (4.88): solutions to the original differential equation 
define submanifolds of M whose tangent vectors annul the form (4.88). Equa- 
tion (4.88) is true when restricted to this submanifold. Conversely, if there 
exist submanifolds whose tangent vectors annul (4.88), then these submanifolds 
are solutions of (4.87). Naturally there is not just one solution submanifold but 
a whole family of them, distinguished from one another by, say, the ‘initial 
value’ of the solution y at some fixed x = X9 (or equivalently by the arbitrary 
constant of integration in the solution to (4.87)). 
One can of course generalize this picture. Any given set of forms (not nec- 
essarily one-forms) {y;,i=1,...,N}$defines at any point P a subspace of Tp 
which annuls them. A solution to the forms (or to their associated differential 
equations) is the submanifold formed by the meshing together of these little 
tangent subspaces. The question of whether this meshing together is possible 
is clearly related to the theorem of Frobenius, proved in chapter 3. We reformu- 
late this theorem in the language of forms in the next section. 
The first question for the physicist, however, is usually to find the set (or a 
set) of forms which is equivalent to a given set of differential equations. An 
example of this is given in exercise 4.32, where the equations are first-order. 
A more complicated example is provided by the second-order harmonic oscilla- 
tor equation 
d*x 
a wx — 
0, 
(4.59)

## Page 164

Differential forms: differential calculus 
154 
where w is, for convenience, taken to be a constant. To put this in the language 
of forms, we write it as two first-order equations: 
ax 
Y = 
ory 
ας 
ο 
a 
Then it is clear that finding a submanifold that annulls the forms 
@=dx—ydt, 
B= dvtwxdrt, 
is equivalent to solving (4.89). The whole manifold is three-dimensional, with 
coordinates (x, y, {). A solution submanifold is one-dimensional, since annulling 
ἃ and 6 amounts to two restrictions on the vectors at any point of the manifold. 
Further instructive examples may be found in the papers by Estabrook (1976) 
and by Harrison & Estabrook (1971) in the bibliography. We now turn to the 
problem of the existence of solutions to these equations. 
4.26 
Frobenius’ theorem (differential forms version) 
We now return to one of the most important theorems of differential 
calculus on manifolds, whose Lie derivative version we gave in §3.7. In order to 
re-cast it in terms of differential forms we first need some definitions. A set of 
forms {@;} of any degree defines at each point P a subspace of vectors Xp of Tp, 
each of which annuls each B;- This is called the annihilator of the set of forms at 
Ρ. The complete ideal of the set at P is all the forms at P whose restriction to 
ΧΡ vanishes. (Notice that if ¥ is any form at P, ¥ a B; is zero when restricted to 
the annihilator of B;, and so is in the complete ideal.) Any such complete ideal 
has a set of linearly independent one-forms {a} which generates it, in the sense 
that the complete ideal of {@}is the same as that of {6;}. Exercise 4.29 con- 
structs such a set of generators. 
Exercise 4.29 
Let {@;,...,@,,}be a basis for Xp and augment it with any other set 
of vectors {@m+1,---,@,}to form a basis for ΤΡ. Show that the dual 
basis one-forms {@’"*', ... , 65"} generate the complete ideal. Show 
that any form in this ideal can be written as ΣΙ 44; ¥'A @' for some 
{7}. 
Exercise 4.30 
Let {0,7 =1,...,m}be aset of linearly independent one-forms. 
Show that any form Ύ is in their complete ideal if and only if 
YAQ, AG A...AQy, = 0. 
(4.90) 
The above algebra extends naturally to fields of forms. The complete ideal of

## Page 165

4.26 Frobenius’ theorem (differential forms version) 
155 
a set of fields {6;} is the set of fields which are annulled by the annihilator Xp 
of {B;3 at every point P. An ideal is said to be a differential ideal if, for every 
¥ in the ideal, 4 is also in it. A set of one-forms {1 15 said to be closed if each 
form da; is in the complete ideal generated by the as. 
Exercise 4.31 
(a) Show that a closed set of one-forms generates a differential ideal. 
(b) On an n-dimensional manifold, show that any linearly independent 
set of n or n — 1 one-forms is closed. 
The Frobenius theorem can now be stated: suppose {@;,i=1,...,m}area 
linearly independent set of one-form fields in an open region U of an n- 
dimensional manifold Μ. If and only if they are closed, there exist functions 
{P;;,Q;,i,7= 1,...,m}such that 
m 
+ 
a = >) Pz dQ;. 
(4.91) 
Before proving this in the next section, let us see what it means. We are 
looking for solutions of the differential equations {&; = 01, which are shown by 
(4.91) to be equivalent to (40, = 0}. But this latter set is easy to solve: {0; 
= const}. So the functions {Q;' are the solutions to the equations {δι = 0}. Each 
set of values {Q;} defines an m-dimensional submanifold of M. Its tangent 
vectors annul {dQ;} by definition and therefore annul {@;}. This is the link with 
our previous version of Frobenius’ theorem. The requirement that the set of 
one-forms be closed is the dual of the requirement that the set of vector fields 
annulling them be a Lie algebra, as discussed in more detail below. 
Forms {@;} satisfying (4.91) are said to be surface-forming. We can now 
establish the sufficiency of the integrability conditions discussed in $4.17. In 
that case the manifold had dimension two and the solution submanifold dimen- 
sion one. The equation 
a= df 
is of the form (4.91), so a function f exists if and only if da = 0. A more compli- 
cated example follows. 
Exercise 4.32 
Consider the set of coupled linear inhomogeneous differential equations 
for the functions f and g in the independent variables x and y

## Page 166

Differential forms: differential calculus 
of 
—+A,ft δισ 
Ox 
of 
oy 
dg 
—+Dyet kf 
Ox 
Ci, 
C2, 
Fy, 
8 4 
Det Eaf = 
wt 
Dog t 
Eof = Fa, 
ν 
156 
(4.92) 
where A;, δι, C;, D;, ΕΙ, F; @ = 1, 2) are functions of x and y. We wish 
to establish the integrability conditions for these equations. 
Neue’ 
(a 
we define two one-forms 
α 
~~ 
B 
ᾱ - df t+f4+eB—C, 
dg+eD+fE—F, 
with the one-form A being defined as 
A= Αι dx + 42 ἄν, 
and similarly for B,C,.... Show that finding a two-dimensional sub- 
manifold 
# in M on which Gly = Bly =0 
is equivalent to solving 
(4.92). 
In the four-dimensional manifold M whose coordinates are (x, y, f, g) 
(4.93) 
(4.94) 
(b) By Frobenius’ theorem, if (@, β) are closed, then there exist functions 
U,V,W,X, Y,Z of the four variables (x, y, f, g) such that 
@ = WdU+XdV, 
6 = YdU+Z dP. 
Show that 
U(x,y,f,g) = const, 
V(x,y,f,8) = const, 
defines a solution to (4.92). 
(c) By (b), a necessary and sufficient condition for a solution to exist is 
that the two-forms d@ and df be in the ideal of (ᾶ, 8). Show that this 
is true if and only if 
dA+BaE 
= dD+EaB 
dB+BaD+AnB = dC+BaFt+An 
dE+EAAt+DAE = dFtEaCtDa fF = 0. 
(Hint: the realization that by (4.94) dA is proportional to dx a dy helps 
simplify the algebra enormously.) 
(d) Show that the conditions in (c) lead to the integrability conditions for 
(4.92):

## Page 167

4.27 Equivalence of two versions of Frobenius’ theorem 
197 
ὃ4ι 
dA, 
πο ποπ 
+ Bok, —B,F, 
= 
0, 
Oy 
Ox 
0B, 
dB, 
oa 
t+ BLD, + 4.81 —B,D, —A,B, 
= 
0, 
oy 
Ox 
and so on. 
What does Frobenius’ theorem have to say about the existence of solutions 
to equation (4.89)? The answer is simple: since any two linearly independent 
one-forms in a three-dimensional manifold automatically have a closed ideal 
(cf. exercise 4.31(b)), there must exist functions f, g, h,1,m,n for which 
hdf + Idg, 
mdf + ndg. 
Then the one-dimensional submanifolds defined by f= const, g = const annul 
the forms a and B, and so are the solution submanifolds. 
Our version of Frobenius’ theorem does not directly deal with systems of 
differential equations described by sets of forms including two-forms or forms 
of higher degree. This case can be handled by finding a set of one-forms which 
generate the same complete ideal, as in exercise 4.29. It will not always be the 
Ὅοι 
ϱὶ 
| 
case that these one-forms are algebraically equivalent to the original set, i.e. they 
might not give differential equations equivalent to the original ones. If they do, 
Frobenius’ theorem applies directly. If not, then a more subtle approach is 
needed. See Choquet-Bruhat et al. (1977) for a discussion. 
4.27 
Proof of the equivalence of the two versions of Frobenius’ theorem 
Let us recall the geometrically more transparent version given in 
chapter 3: a given set of g vector fields (γω, i=1,...,q}, which at every 
point form a p-dimensional vector space, will mesh to form a p-dimensional 
hypersurface if and only if all the Lie brackets [V;,, Vj] (7 =1,..., 4) are 
linear combinations of the g vector fields. The version given in this chapter 
involves forms and the closure of their exterior derivatives; this is a picture 
‘dual’, or complementary, to one with vectors and the closure of their Lie 
brackets. The key element in the correspondence between the two pictures is 
that if the vector fields define an r-dimensional subspace of Tp at a point P, of 
an n-dimensional manifold, then they define in a natural way an (n — r)- 
dimensional subspace of ΤΡ, the space of one-forms at P, by the requirement 
that the forms be annulled by the vectors. Conversely, the same requirement 
allows a set of g one-forms to define an (n — q)-dimensional subspace of Tp. 
What we have, in effect, is that a submanifold can be described either by giving

## Page 168

Differential forms: differential calculus 
158 
at every point the r-dimensional subspace of Τρ which contains the vectors 
tangent to it, or by giving the (η — r)-dimensional subspace of one-forms 
annulled by those vectors. The proof of the equivalence between the two 
versions of Frobenius’ theorem has two steps. 
(1) Consider a submanifold of dimension p in a manifold of dimension n: 
there are n — p different functions Ομ which (locally) define the hypersurface 
by the n — p equations Q(z) = const. The forms dO ce are, by hypothesis, all 
linearly independent, and they are all anulled by any vector V tangent to the 
submanifold: (dQ, zy, V) = 0. On the other hand, the tangent space to the sub- 
manifold is a p-dimensional vector space, which therefore defines a (n — p)- 
dimensional subspace of one-forms, such that any one-form β in this subspace 
is annulled by all the V.;y: (8, Vij) = 0. Let @yy,k =1,...,n—p} be any 
basis for the subspace. It is clear that the forms dO, ϱ) are also a basis, so that 
any @,) can be written as a linear combination of all the dO anys, as in equation 
(4.40). So the equivalence proof must now show that the condition on the 
vector fields — closure of their Lie brackets — is equivalent to the closure con- 
dition on the forms {@,)}. 
(2) This is done by beginning with the equation 
(αμ. γώ) = OG = 1,...,n—-psj = 1,...,P), 
and taking its Lie derivative with respect to any V(,): 
0 = ἐνιδω. Vay? = (Lo gy Ven + (Kay, LF) Vp? 
By the rules for the Lie derivatives of forms we have 
(Loy Mays γώ) = (diy, Vewys Veg) + (dG n(Viny), Vin? - 
The first term vanishes because Qi) is by definition annulled by V(z), while 
the second one is just oes V (jy), the value of da; on two vectors in 
the original set. Now, if £7 (ke Vj) is a linear combination of some Vj, then it 
annuls ἄ(ῃ and we have that t day is annulled by the {V;;)}.as well. Therefore, 
deci is in the ideal, and closure of the Lie brackets implies closure of the forms. 
Conversely it is easy to see that closure of the forms (which implies dein (V, k)> 
Vy) = 0) implies closure of the Lie brackets. 
4.28 
Conservation laws 
A particularly nice approach to conservation laws for differential 
equations is afforded by forms. Suppose solving a system of equations is equi- 
valent to finding surfaces that annul a certain set of forms {&,}. Suppose further 
that there exists a form ¥, a linear combination of {@;}, 
Y= A a, +..., 
such that

## Page 169

4.28 Conservation laws 
159 
dy = Q. 
Then there exists another form 6 such that 
y= de, 
in a suitable region U of a solution surface H, and 
Ve = doly = 0. 
(4.95) 
Applying Stokes’ theorem to the integral of d& on the region U of H gives 
[ do = 
δ. 
U 
dU 
But by (4.95) this vanishes: 
bu Olu = 0 
on the boundary of the region of a solution surface. This is a kind of integral 
conservation law, as we now illustrate for the harmonic oscillator. 
The solution surfaces of (4.95) are one-dimensional curves, so the form 
do must be a one-form, and @ is in fact a zero-form (a function). Since d@ is 
the same as Ύ, consider the form (notation same as before (§4.25)) 
~~ 7 = w*x&+ γβῇ. 
It is easy to verify that 
dy = 0, 
(4.96) 
and in fact that 
y= dy? +4w?x?). 
(4.97) 
Then on a solution curve, for which & = 8 = 0 and hence ¥ = 0, we have that 
d@y? +3w°x?) = 0, 
0 =| ddy? +40?) 
= 
Gy? + 30° 
x? IP 
where p, and p, are the endpoints of the region of the curve we integrated 
over. This just expresses the constancy of the energy, 
$y* + 4w7’x’, along a 
solution curve. 
For an application of this point of view to equations having soliton solu- 
tions, the interested reader is referred to Estabrook & Wahlquist (1975) (see 
bibliography). 
Exercise 4.33 
Verify equations (4.96) and (4.97).

## Page 170

Differential forms: differential calculus 
160 
4.20 
Vector spherical harmonics 
We resume here our discussion of spherical harmonics in §3.18. In that 
section we noted that a finite-dimensional representation of SO(3) in the space 
of functions on S?, L?(S”), had the basis {Y,,,,m =—1,..., 1}. How do we 
create a related basis for vector fields on S”? The space of all vector fields can be 
given a natural norm in terms of the metric g| of S?, whose components are 
(σρο = 1, S49 = sin? 
6, Zog = 0} in the usual spherical coordinates. If we let & 
be the metric-induced volume form on S? (§4.13) then the space 11 9(S”) is 
the vector space of all vector fields V on S* whose norm 
WIP = {o GV, V) @ 
(4.98) 
is finite. What we want are vector fields in Li 6 (52) which are eigenfunctions of 
|, and L?. 
We use two facts: first, Οἱ and hence @ are invariant under /, and L? ; and 
second, exterior differentiation and Lie differentiation commute. From the 
function Y,,, we construct the one-form dY im, and from it the vector VY), 
with components (indices A, B run over 1 and 2) 
(WYim)* . g°? (Yim) ,B: 
(4.99) 
Evidently this is also an eigenfunction of J, and L?: 
τσι = im VYim, 
(4.100a) 
L?(VYim) = —1d+1)VYim- 
(4.100b) 
But we cannot stop with one sort of vector harmonic, since we need to span a 
two-dimensional vector space. Here we take advantage of the fact that there is 
another way (on a two-dimensional manifold) to construct a vector from a one- 
form: the dual operation. So we also have *dY,,,, which is of course also an 
eigenfunction. 
Exercise 4.34 
Show that VY;,, and *dYj,, are in general linearly independent vectors 
at each point. 
It follows from the completeness theorem quoted in $3.18 that the two sets of 
vector spherical harmonics 
4 
Yin 
ση. 
(41014) 
+ 
Yim = *dYim 
(4.101b) 
form a complete set for representing vectors on the two-sphere. 
It is possible to follow this procedure further and define second-rank tensor

## Page 171

4.30 Bibliography 
161 
spherical harmonics. This would, however, involve us with the covariant deriv- 
ative on the sphere, which we have not yet discussed (see chapter 6). Interested 
readers may consult the paper by Regge & Wheeler (1957) listed in the biblio- 
graphy. 
Note that we have discussed only scalars and vectors on the sphere. Most 
applications involve larger manifolds with spherical symmetry, in which the 
spheres are submanifolds. As a simple example, consider three-dimensional 
Euclidean space E°. A function on £° can be expanded in a series 5 fj, (1) 
X Yim» where its r-dependence is entirely contained in {f,,, }. A vector field V on 
E? can be split into two fields 
V=V,+V,, 
where V, is perpendicular to the spheres (parallel to @,) and V, is tangent to 
the spheres. If we write V, as vé,, where v is a function, then under a rotation 
v transforms as a scalar function on the sphere while V; transforms as a vector 
on the sphere. So V, must be expanded in terms of vector spherical harmonics 
while v is expanded in scalar spherical harmonics. (Many authors multiply these 
scalars by 6, and call the resulting set a third kind of vector spherical harmonic.) 
We shall employ these in our examination of cosmological models in chapter 5 
part E. 
There are other equivalent formulations of vector spherical harmonics which, 
at first sight, seem to have very little to do with the ones defined here. These are 
defined by the algebraic methods of group theory (cf. Edmonds, 1957). The set 
presented here are convenient to use in differential equations, where the deriv- 
atives we have used occur naturally. 
4.30 
Bibliography 
E. Cartan’s own point of view on differential forms is very lucidly set 
out in E. Cartan, Les Systemes Differentials Exterieurs et Leurs Appli- 
cations Geometriques (Hermann, Paris, 1945). An excellent intro- 
duction with more detail than we have room for, and with many 
applications in physics and engineering, is H. Flanders, Differential 
Forms with Applications to the Physical Sciences (Academic Press, 
New York, 1963). A recent and modern discussion which presupposes 
very little mathematical background is M. Schreiber, Differential 
Forms: a Heuristic Introduction (Springer, Berlin, 1977). A rigorous 
and advanced discussion of forms can be found in Y. Choquet-Bruhat, 
ο. Dewitt-Morette & Μ. Dillard-Bleick, Analysis, Manifolds, and Physics 
(North-Holland, Amsterdam, 1977). 
For a discussion of Stokes’ theorem on nonorientable manifolds, 
with an application to the problem of the apparent nonexistence of 
magnetic monopoles, see R. Sorkin, J. Phys. A 10, 717 (1977). 
For further discussion of cohomology theory, see M. Spivak, A

## Page 172

Differential forms: differential calculus 
162 
Comprehensive Introduction to Differential Geometry (Publish or 
Perish, Boston, 1970) vol. 1; or F. W. Warner, Foundations of Differ- 
entiable Manifolds and Lie Groups (Scott, Foresman, Glenview, II. 
1971). 
The usefulness of forms in exploring the structure of differential 
equations is illustrated by F. B. Estabrook & H. D. Wahlquist, Pro- 
longation structure of nonlinear evolution equations, J. Math. Phys. 16, 
1 (1975), and The geometric approach to sets of ordinary differential 
equations and Hamiltonian dynamics, SIAM Review 17, 201 (1975). 
See also B. K. Harrison & F. B. Estabrook, Geometric approach to 
invariance groups and solutions of partial differential systems, J. Math. 
Phys. 12, 653 (1971); and F. B. Estabrook, Some old and new tech- 
niques for the practical use of exterior differential forms, in Backlund 
Transformation ed. R. N. Miura, Lecture notes in mathematics, no. 
515 (Springer-Verlag, Heidelberg, 1976). 
There are many formulations of vector spherical harmonics. A stan- 
dard reference is A. R. Edmonds, Angular Momentum in Quantum 
Mechanics (Princeton University Press, 1957). For the extension of our 
methods to tensors, see T. Regge & J. A. Wheeler, Phys. Rev. 108, 1063 
(1957). Other definitions of tensor spherical harmonics may be found 
in D. A. Akyeampong, J. Math. Phys. 20, 505-8 (1979); and E. T. 
Newman & R. Penrose, J. Math. Phys. 7, 863 (1966).

## Page 173

5 
APPLICATIONS IN PHYSICS 
A Thermodynamics 
5.1 
Simple systems 
We confine our attention at first to a one-component fluid, for which 
the equation of conservation of energy is 
δο = PdV+dU, 
(5.1) 
where U is the internal energy of the fluid and δΟ is the heat absorbed as the 
fluid does work PdV and changes its energy. We shall interpret this equation as a 
relation among various one-forms in the two-dimensional manifold whose 
coordinates are (V, U), on which the function P(V, U) is defined (called the 
equation of state). Then since dV and dU are one-forms, so is 50. But is 50 an 
exact one-form? That is, can one find a function Q(V, U) such that 50 = do? If 
this were true, then one would have ddQ = 0, which would mean 
OP\ 
w~ 
OP\ 
~ 
στι 
dV+ 
(—] 
dU 
OP\ 
~ 
~ 
—| 
ἀλλά’. 
νι 
(Subscripts on derivatives indicate which variable is fixed during differentiation.) 
Thus, a function Q can exist only if (0P/dU)y vanishes everywhere: this would 
be a strange fluid indeed! 
Since 50 is a one-form in a two-space, its ideal is automatically closed, so by 
Frobenius’ theorem ($4.26) there must exist functions T(U, V) and S(U, V) 
such that δΟ = TdS. Thus, we define the temperature and entropy functions 
for the single-component gas in thermodynamic equilibrium simply as a repre- 
sentation of the one-form in equation (5.1): 
9 
TdS = PdV + du. 
(5.2) 
It is important to understand that this is a purely mathematical definition of T 
and S, and it has no relation to the second law of thermodynamics, which we 
will consider in a moment. No mathematical identity of this sort would hold for 
0 = ἀρλάν = 
a dV

## Page 174

Applications in physics: thermodynamcis 
164 
a multi-component fluid. (We shall see that the second law of thermodynamics is 
equivalent to requiring 50 = TdS for composite systems. Because this is not an 
automatic identity, the second law is a physical law: it restricts the possible 
mathematical nature of physical systems.) 
5.2 
Maxwell and other mathematical identities 
Taking the exterior derivative of (5.2) gives 
ἄΤλ dS = dPa dV. 
(5.3) 
Suppose we write T = T(S, V), 
P= P(S, V). Then (5.3) gives (since dSadS =0, 
dVa dV=0O): 
aT\ ~~ 
[aP\ 
ς 
ορ)... 
- 
—) dvads = (=| 
dsadv 
= —|<] 
ava 
ds. 
2 
) * 
I, * 
2) * 
From this we conclude 
oT 
oP 
(27) 
= — e). 
(5.4) 
which is known as one of the Maxwell identities. Similarly, by writing S = S(T, 
V),P =P(T, V), we can deduce 
95 
oP 
LB 
. 
another Maxwell identity. By dividing (5.2) by Τ and then taking the exterior 
derivative we get 
1 ~ 
~ 
Pex 
~ 
1 ~ 
~ 
γη Λ πο aE a VV — 73 OT A dU = 0. 
By writing U= U(T, V), 
P= PCT, V), we get 
1 
[οἱ 
~~ 
Pri 
w~ 
1 
/0U\ ~~ 
ποστ 
dTa ava APA γ΄ --τ-ς 
ἀΤλάΞ 0, 
ν 
T 19Τ 
Τ21ὸΥ// 
. 
oP 
ου 
ΤΙ 
—-P={=—|]. 
5.6 
η, 
(4) 
| 
ο 
Exercise 5.1 
Derive the identity 
oP 
oP 
ου 
δΡι 
{dU 
ο] .. (=) (22) -(%) (24) 
6 
by multiplying (5.2) by 1/P and differentiating.

## Page 175

5.3 Composite thermodynamic systems 
165 
Another important relation which follows easily from the use of forms is 
ΟΤΙ] 
(951 
{oP 
rl ler),las), =~ 
aa 
which is equally true of any set of three of (P, V, U, T, 5). We prove this by 
writing 
T = T(P,S),S = S(T,P),P = P(T,S), 
(5.9) 
which is possible since the manifold is two-dimensional. Then we have the 
successive identities: 
oT \ ~ 
~ 
ar] 
dPa dS 
ΟΡ Js 
or Os dP 
a dT 
ΟΡ /g\ OT |p 
aT\ 
(951 
(ορ. 
~ 
- 
(“| 
(2) 
[| 
as, 
ar 
bakeanegl ou 
from which follows (5.8). Notice that the derivation here relies only on the 
ability to write (5.9), so that it is really an identity among any three functions 
on a two-dimensional manifold. 
The ease with which the Maxwell identities and (5.8) can be derived using 
forms is an illustration of the natural way in which they fit into thermodynamics: 
the one-forms dP, ds , etc. are the mathematically precise substitutes for the 
physicists’ rather fuzzier concept of the infinitesimals dP, dS, etc. 
dT a ds 
5.3 
Composite thermodynamic systems: Caratheodory’s theorem 
We now consider composite thermodynamic systems, the parts of 
which may exchange energy with each other and with the outside world. In this 
case the law of conservation of energy is (for a system with Ν parts) 
δο = P,dV,+ dU, +P,dV,+ dU, +... 
N 
= ) (P,dV, + dU,). 
(5.10) 
i=1 
We regard this as a relation among one-forms on a 2N-dimensional manifold 
whose coordinates are (V;, U;;i=1,...,N), and we assume that each P; can be 
expressed as a function of these coordinates. The question arises of whether one 
can define an entropy and temperature for the system as a whole, i.e. whether 7 
and S exist such that 
+ 
δο = TdS. 
(5.11) 
This equation is just the statement that 50 is integrable (in the sense of the 
Frobenius theorem). Now the Frobenius theorem tells us that the necessary and

## Page 176

Applications in physics: thermodynamics 
166 
sufficient condition for this to be true is d5Q a 5Q = 0. It is easy to see from 
(5.6) that this will not generally be true, so we can conclude that for a general 
interacting system there is no global temperature or entropy function. But the 
situation can be different for an equilibrium system, because the conditions for 
mechanical and thermodynamic equilibrium among the constituent parts restrict 
the problem (we assume) to a submanifold of the 2V-dimensional one. We shall 
from now on let the world ‘manifold’ refer to this equilibrium submanifold, and 
examine the possibility that 5Q is integrable in it from the point of view of 
Caratheodory. 
If 50 is integrable, then every point of the manifold is on one and only one 
integral submanifold; these submanifolds are defined by S = const. None of these 
surfaces intersect. Therefore, starting at one point, it is not possible to reach an 
arbitrary point of the manifold along a curve on which δΟ is everywhere zero. In 
other words, if an entropy function exists it is not possible to reach every equi- 
librium state of the system along an adiabatic path of equilibria. The physically 
interesting question is whether the converse is true: if we know that not every 
state is reachable along a path for which δΟ = 0, can we say that δΟ is inte- 
erable? This is interesting because one version of the second law of thermo- 
dynamics asserts that it is impossible in a closed system to transfer heat from a 
colder to a hotter body without making other changes as well. By a closed sys- 
tem we mean one for which δΟ = 0, so that the second law tells us that not 
every state can be achieved with 6Q = 0. So does the second law imply the exist- 
ence of an entropy function? Caratheodory’s theorem says it does. 
What we shall prove is that if 5Q is not integrable then all points in the neigh- 
borhood of some initial point P are reachable from P on a curve which annuls 
5Q. Since δΟ is not integrable, the version of Frobenius’ theorem given in $4.26 
shows us that there are at least two vector fields V and W for which 5Q(V) 
= 5Q(W) = 0 in a neighborhood of any point P, but 
5O([V, W]) #0 at P. That 
is, the one-form δΟ defines at each point Ρα subspace K p of Tp, the vectors of 
which annul 50; the nonintegrability of 50 means that vector fields everywhere 
in Kp do not form a hypersurface: at least one of their Lie brackets does not lie 
in Kp (see figure 5.1). Because annulling 50 is only one equation, K p has 
Fig. 5.1. The tangent hyperplane K p contains the vectors annulling 50 
but not all of their Lie brackets at P. 
[V, 
W]

## Page 177

5.4 Hamiltonian vector fields 
167 
dimension n — 1, where n is the dimension of the equilibrium manifold. Now, 
recall the exponentiation notation for the Taylor series introduced in §2.13. If 
we take any vector field U which is in Kp at all points P, and we move along it a 
parameter distance ε from P, we reach the point whose coordinates are 
* = exp (eUV)x'|p, where we use U as a derivative operator on the function x’ 
along the curve. The set of all points in a small neighborhood of P reachable in 
this way may be called exp (€K p): it is the representation in the manifold of the 
vector space K p. This set of points is locally like a piece of an (n — 1)-dimensional 
hypersurface. We shall show that, by following the curves of V and W defined 
above, we can reach points ‘above’ or ‘below’ this ‘hypersurface’ — i.e. that we 
can reach all points near P. The trip we make is the following: we move first a 
distance ε along V, then ε along W, then — € along V, and finally — € along W. 
This takes us to (cf. equation (2.6)) 
i 
x 
~eW 
eV .eW EV, i 
=e 
lp 
= (1+ €?[W, V] + O(e?))x'lp. 
(5.12) 
This means that we wind up almost back at P, but a parameter distance εὖ away 
from it along [V, W]. This point is not in exp (eK p), since [V, W] is not in Kp. 
It is on one side of exp (€K p); to finish on the other side we would have trav- 
elled first on W, then on V. Now, our path was along V or W everywhere, so it 
was adiabatic: δΟ = 0 everywhere. It is clear, therefore, that if 50 is not integ- 
rable, all states of the system will be reachable along adiabatic paths. This proves 
that the second law requires integrability of 5Q in the equilibrium manifold and 
the existence of an entropy function for composite systems in equilibrium. 
B Hamiltonian mechanics 
5.4 
Hamiltonian vector fields 
The Hamiltonian version of a dynamical system of equations begins 
with the Lagrangian στα, ᾳ |) for some dynamical variable g(t). The momentum 
p is defined as 
p = ὃσ]δ(ᾳϱ, 
(5.13) 
and the Hamiltonian Η as 
H = pqi-—L = H(p,4q). 
(5.14) 
The dynamical equation 
ά ὃσ of 
—>—_ —-~— = 0, 
(5.15) 
dt og; 
 0q 
and the definition of p can be written, respectively, as

## Page 178

Applications in physics: Hamiltonian mechanics 
168 
oH 
op 
an 
off = 4 ; 
0g 
dt ’ 
dp 
 ἀί 
We now make a geometric picture of Hamiltonian dynamics by defining a mani- 
fold 
M called ‘phase space’, whose coordinates are p and 4. On M we define the 
two-form 
+ 
6} = dqa dp. 
(5.17) 
Consider a curve {q = f(t), p = g(t)} on M which is a solution of (5.16). Its tan- 
gent vector, 
U = d/dt =f, 0/dq +g; 0/dp, has the property 
(5.16) 
ϕ 
{.πῶ = 0, 
(5.18) 
as we shall now prove. Since da = 0, we have from (4.67) 
£50 = d[a(0)]. 
(5.19) 
But since @ = dq ® dp — dp ® dq, we have 
6(U) = (dq, U) dp — (dp, U) dq 
= — dp—— dq. 
5.20 
ae 
ay 
(5.20) 
On the other hand, since fand g satisfy (5.16), we have 
ο 
9Η. 
9Η. 
~ 
@(U) = —dp+—dq = dH. 
(5.21) 
Op 
oq 
Therefore d[(U/)] vanishes, establishing (5.18). A vector field U that satisfies 
(5.18) is called a Hamiltonian vector field. 
Exercise 5.2 
(a) Prove that if U is a Hamiltonian vector field, there exists some A(p, q) 
such that equations (5.16) are satisfied along the integral curves of U. 
(b) Prove that Hamiltonian vector fields form a Lie algebra. 
By exercise 5.2(a), we interpret U as a tangent to the solution curves in phase 
space if U is Hamiltonian. Notice that the system is conservative, since (5.16) 
implies 
dH 
£7H = — = 
0. 
2 
U 
dy 
0 
(5.22) 
5.5 
Canonical transformation 
Now the coordinates p and q are not unique. We define a canonical 
transformation as one which leaves G in the same form. That is, new coordinates 
P = P(q, p) and O = O(q, p) are called canonical if

## Page 179

5.6 Map between vectors and one-forms provided by 3 
169 
dg a dp. = dQ a dP. 
(5.23) 
The necessary and sufficient condition for this is 
90 0P 
90 οΡ 
09 of ο 
= 
1. 
(5.24) 
dq op 
ορ oq 
One such transformation is Q = p, 
P= —q. A less trivial one is found if we 
follow a procedure similar to the one we used to deduce the Maxwell identities 
in thermodynamics: we write p = p(q, Q), P = P(q, Q) and find from (5.23) that 
9ρΡ/90 = — doP/dq. 
(5.25) 
So if we take an arbitrary function F(q, Q) and define 
p = 9Ε/9ᾳ. 
P = 
— 0F/0Q, 
then (5.25) is satisfied identically. Thus, F(q, Q) is said to generate a canonical 
transformation. Since we could have chosen, instead of (ᾳ. Q), the pairs (q, P), 
(p,Q), or (p, P) to be independent in (5.23), there are clearly four types of such 
generating functions for canonical transformations. They are explored more 
fully in Goldstein (1950) (see bibliography). 
5.6 
Map between vectors and one-forms provided by 3 
One of the most important features of this geometrical point of view on 
Hamiltonian dynamics is that @ can be cast in a role similar to that which a 
metric plays on Riemannian manifolds: it provides an invertible 1-1 mapping 
between vectors and one-forms. If V is a vector field on M, we define a one-form 
field 
~~ 
V = GV), 
(5.26) 
with components 
(V); = wyV!. 
(5.27) 
Similarly, given a one-form field &@ we define a vector field a as the (unique) 
vector such that 
ᾱ-- ὤ(α). 
(528) 
Exercise 5.3 
Prove that (V, V) = 0, so that ὤ is not suitable as a metric. 
Exercise 5.4 
Prove that if a = fdq + gdp, then 
αξρ---- Γτ-. 
(5.29)

## Page 180

Applications in physics: Hamiltonian mechanics 
170 
Exercise 5.5 
Prove that ¥ is a Hamiltonian vector field on M if and only if Χ is an 
exact one-form, i.e. if and only if there exists some function H such 
that Y= dH, or 
X = dH. 
5.7 
Poisson bracket 
Suppose there are two functions f and g on the manifold, and we define 
the vector fields X; = df and X, = dg. Then consider the scalar 
{fg} = OX, χε = (df, XQ). 
(5.30) 
Since ὦ = dq &) dp — dp &) dq, we have 
— 
og 0 
og ὃ 
Xg 
= TTD ; 
5.31 
& 
0g 0p 
ὃρ ag 
( 
) 
which can be established by verifying that @(X,) = dg. Therefore we have 
Og Of 
ορ of 
0q 0p 
dp dq 
This is what is usually called the Poisson bracket of the functions f and g. The 
definition (5.30) gives it a geometrical significance, and shows that the Poisson 
bracket is actually independent of the coordinates. It depends only on 6. 
Exercise 5.6 
(a) Defining X,, = dH, show that for any function K, 
{K,H} = X,(K) = dK/dt, 
(5.32) 
where ¢ is the parameter such that Y;,; = d/dt. Thus, the Poisson 
bracket of a function with the Hamiltonian gives the time-derivative of 
that function along a solution curve. In particular, constants of the 
motion have vanishing Poisson bracket with H. 
(b) Show that the Poisson brackets satisfy the Jacobi identity 
fig, us + tg, th, £55 + th, (hast = 0 
(5.33) 
for any C” functions f, g, h. 
(c) Show from this that 
[Χ,, χο] = 
— Xf g}, 
(5.34) 
so that the Hamiltonian vector fields form a Lie algebra. 
5.8 
Many-particle systems: symplectic forms 
In general one deals with systems which have more than one degree of

