<!-- source-pdf: FleischVectorsAndTensors.pdf | pages 91-120 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 91–120

## Page 91

3.2 Curvilinear motion
79
has changed). You can therefore set |⃗vinitial| = |⃗v f inal| = |⃗v|, where |⃗v| is the
speed of the object at both positions. Since the average speed of the object is
deﬁned as the distance covered divided by the time taken to cover that distance,
you can write
|⃗v| = r	θ
	t ,
(3.21)
which means that
	θ = |⃗v|	t
r
.
(3.22)
The reason that an expression such as Eq. 3.22 for 	θ is valuable is that this
angle change is directly related to the magnitude of the vector change in veloc-
ity, which you need to know if you want to ﬁnd the centripetal acceleration.
To see that, consider what happens if you form the vector 	⃗v by adding ⃗v f inal
to −⃗vinitial, as in Figure 3.14. The ﬁrst thing you should note is that the angle
between the vectors ⃗v f inal and −⃗vinitial is equal to 	θ (if you don’t see why
that’s true, go back to Figure 3.13 and imagine extending both vectors ⃗v f inal
and −⃗vinitial until they cross). Also note that the vector 	⃗v is drawn at the
location mid-way between the original location of ⃗vinitial and the original
location of ⃗v f inal, since that’s the location at which you’re ﬁnding the cen-
tripetal acceleration. The ﬁnal thing to note in this ﬁgure is that both ⃗v f inal
and −⃗vinitial have length equal to |⃗v|, which makes the arc length shown in the
ﬁgure equal to |⃗v|	θ.
Now imagine what will happen if you allow the angle 	θ to shrink toward
zero. As the angle decreases, the arc length |⃗v|	θ will get closer and closer to
the length of 	⃗v. Plugging in the value for 	θ from Eq. 3.22, you have in the
small-angle limit
|	⃗v| ≈|⃗v|	θ = |⃗v||⃗v|	t
r
= |⃗v|2	t
r
,
(3.23)
which means that the magnitude of the instantaneous centripetal acceleration is
|⃗ac| = |	⃗v|
	t
= |⃗v|2	t
r	t
= |⃗v|2
r .
(3.24)
So there you have it: the centripetal acceleration at any given point is simply
the square of the speed divided by the radius of curvature of the path at that
point. Hence doubling your speed means that your centripetal acceleration is

## Page 92

80
Vector applications
four times larger, which means that the centripetal force must be four times
stronger.
If you’re concerned that Eq. 3.24 may apply only in the case of uniform
circular motion, remember that by allowing 	θ to become arbitrarily small
you’ve ensured that neither the speed nor the radius of curvature has changed
during the time period under consideration.
What does Eq. 3.24 tell you about the amount of force needed to cause
an object to follow a speciﬁed curving path? Consider the hammer-thrower
discussed above and shown in Figure 3.12, and assume that she intends to
launch a 4 kg mass at the end of a 1.2 m cable with a speed of 20 m/s. Assuming
she achieves her maximum speed just before letting go of the cable, at that
point the centripetal accleration will be
|⃗ac| = |⃗v|2
r
= (20m/s)2
1.2m
= 333.3m/s2,
which means that the thrower must provide a centripetal force of
| ⃗Fc| = m|⃗ac| = 4kg

333.3m/s2
= 1333.3N
which is almost 300 pounds of force (and this doesn’t include the mass of the
cable).
With Eq. 3.24 to help you ﬁnd the magnitude of the centripetal accelera-
tion, and knowing that the tangential acceleration is just the change in speed
over time (⃗atang = 	⃗v/	t), the total acceleration can be found through
vector addition, as shown in Figure 3.15. Thus the magnitude of the total
acceleration is
atang
ac
aTotal
Figure 3.15 Total acceleration as the vector sum of centripetal and tangential
acceleration.

## Page 93

3.3 The electric ﬁeld
81
|⃗aT otal| =

(|⃗ac|)2 + (|⃗atang|)2
=
v2
r
2
+
|	⃗v|
	t
2
.
(3.25)
You’ll ﬁnd an example of combined tangential and centripetal acceleration
in the problems at the end of this chapter.
3.3 The electric ﬁeld
If the previous two sections convinced you that vectors are very helpful in
solving mechanics problems, the next two sections should help you under-
stand why vectors are absolutely essential in problems involving electric and
magnetic ﬁelds and their effect on charged particles. You’ll also see how the
vector operations of divergence, curl, gradient, and Laplacian are used in elec-
trostatics. Even if you’ve never taken an E&M course (and never hope to), the
examples in these sections should be sufﬁciently self-contained to allow you
to understand how vectors and vector operations can be used in E&M.
The natural way to begin a discussion of electric and magnetic ﬁelds is to
provide a clear, concise deﬁnition that states exactly what an electric or mag-
netic ﬁeld is. Such a deﬁnition would appear right here if I had one. But almost
two centuries after Michael Faraday ﬁrst used the words “ﬁeld of force” to
describe the region around electric charges, we still don’t have a standard way
of saying what such a ﬁeld is. The Oxford English Dictionary provides def-
initions for “ﬁeld” that include an “area or space” under the inﬂuence of an
agent, a “state or situation” in which force is exerted, and the “action” of a
force. According to James Clerk Maxwell, “The electric ﬁeld is the portion of
space in the neighbourhood of electriﬁed bodies.” In Halliday, Resnick, and
Walker you can learn to deﬁne the electric ﬁeld by placing a small positive test
charge q0 at some point and measuring the electrostatic force ⃗FE on that test
charge;10 the electric ﬁeld ⃗E is then deﬁned as ⃗E = ⃗FE/q0. In Grifﬁths’ Intro-
duction to Electrodynamics, he states that “. . . physically, ⃗E(P) is the force
per unit charge that would be exerted on a test charge placed at P.” The words
“would be” in that deﬁnition are important, because it is not necessary for the
test charge to be present in order for the ﬁeld to exist.
10 Why do physics and engineering texts always refer to a small test charge? For two reasons:
ﬁrstly, the amount of charge on the test charge must be small so that the electric ﬁeld produced
by the test charge is negligible when compared to the electric ﬁeld that you’re trying to
determine using the test charge. Secondly, the test charge must be physically small because
you’re using it to determine the ﬁeld at a speciﬁc position, so you don’t want your test charge
to extend over a large region of space.

## Page 94

82
Vector applications
The common thread running through all these deﬁnitions is this: ﬁelds and
forces are closely related. So we’ll take the following as our deﬁnition of the
electric ﬁeld ⃗E:
⃗E ≡
⃗FE
q0
,
(3.26)
where ⃗E is the vector electric ﬁeld, q0 is a small test charge, and ⃗FE is the
electric force produced on the test charge by the electric ﬁeld. Deﬁning the
electric ﬁeld through this equation should help you remember that ⃗E is a
vector quantity with magnitude directly proportional to force and with direc-
tion given by the direction of the force on a positive test charge (because
if q0 is negative, there would be a minus sign on one side of the equation,
which would mean that vector ⃗E would be in the opposite direction from
vector ⃗FE).
This deﬁnition should also help you see that ⃗E has dimensions of force
divided by charge, for which the standard (SI) units are newtons per coulomb
(N/C). These units are equivalent to volts per meter (V/m), since volts have
dimensions of force times distance divided by charge (units of newtons times
meters/coulombs). So you’ll ﬁnd the units of electric ﬁeld given as N/C in
some texts and V/m in others, and you can rest assured that these mean exactly
the same thing.
There is, however, something important to be noticed in the units of the elec-
tric ﬁeld vector: the dimension of length (units of meters in this case) appears
in the denominator of the dimensions of the electric ﬁeld. And that means that
the vector that represents an electric ﬁeld has a fundamental difference from
the vectors that represent quantities such as position (which has dimension of
length), velocity (dimension of length over time), or acceleration (dimension
of length over time squared). As you can read in Chapter 4, that’s because vec-
tors whose dimensions contain length in the numerator transform oppositely to
vectors whose dimensions have length in the denominator when you perform
certain coordinate-system changes. If this seems unclear and you don’t plan to
venture into the tensor portion of this book, do not panic; none of this will pre-
vent you from using the concepts and operations described in Chapters 1 and 2
to solve problems involving vectors of this kind, exactly as you’re about to do
in the remainder of this section. But if you’ve run across objects called “one-
forms” or “covectors” (of which the electric ﬁeld is an example) and you’re
wondering how those objects are different from the things you’ve been call-
ing vectors, the appearance of length in the denominator of the dimension is
the beginning of the answer (you’ll ﬁnd the rest of the answer in Chapter 4 if
you’re interested).

## Page 95

3.3 The electric ﬁeld
83
You should also make sure you understand that if you know the electric ﬁeld
⃗E at a given location, placing any amount of charge q at that location will result
in an electric force ⃗FE given by
⃗FE = q ⃗E.
(3.27)
So while Eq. 3.26 uses the electric force on a positive test charge to deﬁne the
electric ﬁeld, Eq. 3.27 is a generally useful expression for ﬁnding the electric
force on any amount of charge at the location for which the electric ﬁeld is
known.
Deﬁning an electric ﬁeld is useful, but exactly how would you go about pro-
ducing an electric ﬁeld? One way is to gather up some electric charge, because
every bit of charge produces an electric ﬁeld, just as every bit of mass produces
a gravitational ﬁeld. Electric ﬁelds can also be produced by changing magnetic
ﬁelds, but it is the “electrostatic” ﬁeld produced by stationary electric charge
that will be used to demonstrate the application of vectors in this section.
It’s often helpful to be able to visualize the electric ﬁeld in the vicinity of
a charged object. The most common approaches to constructing a visual rep-
resentation of an electric ﬁeld are to use either arrows or “ﬁeld lines” which
point in the direction of the ﬁeld at each point in space. In the arrow approach,
the strength of the ﬁeld is indicated by the length of the arrow, while in the
ﬁeld-line approach, it’s the density of the lines that tells you the ﬁeld strength,
with closer lines signifying a stronger ﬁeld. When you look at a drawing of
electric ﬁeld lines or arrows, be sure to remember that the ﬁeld exists between
the lines as well.
The electric ﬁelds produced by positive and negative point charges are
shown using the arrow approach in Figure 3.16 and using the ﬁeld-line
approach in Figure 3.17. When you look at electric ﬁeld lines such as these,
+
(a)
_
(b)
Figure 3.16 The electric ﬁeld of positive and negative point charges drawn
using arrows.

## Page 96

84
Vector applications
+
(a)
–
(b)
Figure 3.17 The electric ﬁeld of positive and negative point charges drawn
using ﬁeld lines.
don’t forget that the ﬁeld arrows and lines always point in the direction of
the electric force on a positive test charge, and that electrostatic ﬁeld lines
always begin on positive charge and end on negative charge. And since the
ﬁeld lines show the direction of the electric ﬁeld at any given point, it’s impos-
sible for two ﬁelds lines to cross, since that would indicate that the electric
ﬁeld is pointing in more than one direction at the point of intersection (if two
electric ﬁelds are superimposed at a given point, they simply add as vectors to
give the total electric ﬁeld at that point, and that total ﬁeld can only point in a
single direction).
At this point, you should make sure that you understand that electric ﬁelds
can both be produced by electric charge as well as produce a force on another
electric charge. So you’re likely to face problems in which you ﬁrst have to
determine the total electric ﬁeld produced by charge at a certain location and
then ﬁgure out the effect of that ﬁeld on a completely different charge (not one
of the charges producing the ﬁeld). But doesn’t the charge that’s being affected
(let’s call that one the “subject charge”) also produce its own electric ﬁeld? Yes
it does, but as long as the electric ﬁeld produced by the subject charge isn’t
strong enough to cause the other charges to move around, you can approach
problems like this by ﬁnding the total electric ﬁeld produced by all the other
charges and then using that ﬁeld to determine the force on the subject charge.
This approach is very much like ﬁnding the Earth’s gravitational ﬁeld at some
point in space and then using that ﬁeld to ﬁgure out the gravitational force on
an object of known mass at that location, without considering what effect the
mass of the object might have on the Earth.
Problems like this are especially straightforward if the electric ﬁeld is being
produced by one or more discrete point charges. That’s because the electric
ﬁeld ⃗E of a point charge q is simply

## Page 97

3.3 The electric ﬁeld
85
⃗E = ke
q
r2 ˆr,
(3.28)
where ke is the Coulomb constant (8.99 × 109 Nm2/C2), r is the distance in
meters from the point charge to the location at which the electric ﬁeld is being
determined, and ˆr is a unit vector pointing radially outward from the point
charge.
Thus a single proton (electric charge of 1.6 × 10−19 C) at a distance of one
meter produces an electric ﬁeld given by
⃗E = (8.99 × 109 Nm2/C2)
1.6 × 10−19C
(1 m)2

ˆr
= 1.45 × 10−9(N/C) ˆr.
Note that the direction of that ﬁeld is radially away from the proton, since
the unit vector ˆr always points radially outward from the origin. An electron,
having negative charge, produces an electric ﬁeld of the same magnitude as
that of the proton, but the electron’s electric ﬁeld points toward the electron.
To see that, note that when you plug in a negative charge for q in Eq. 3.28, you
have
⃗E = (8.99 × 109 Nm2/C2)
−1.6 × 10−19 C
(1 m)2

ˆr
= −1.45 × 10−9(N/C) ˆr = 1.45 × 10−9(N/C)(−ˆr),
where the minus sign tells you that the direction of the electron’s electric ﬁeld
is in the negative ˆr direction, which is toward the source charge (since ˆr is
always radially outward, minus ˆr is always radially inward). This is consistent
with electric ﬁeld lines beginning on positive charge and ending on negative
charge.
To understand how to add the vector electric ﬁelds, consider the situation
shown in Figure 3.18. Note that q1 is positive, so its electric ﬁeld must point
radially outward from the location of q1, while q2 and q3 are negative, so their
q1 = +5 nC
q2 = –6 nC
q3 = –8 nC
electron
(–5, +4) cm
(–5, –4) cm
(+7, +2) cm
(0,0) cm
Figure 3.18 Example values for charges near an electron.

## Page 98

86
Vector applications
_
+
-
q1
field
q2
field
q3
field
You want to determine
the total electric field
at this point
Figure 3.19 The electric ﬁelds produced by charges q1, q2, and q3.
electric ﬁelds must point radially inward toward their locations. To ﬁnd the
total electric ﬁeld at the position of the electron, it may help you to picture the
ﬁelds produced by q1, q2, and q3 as shown in Figure 3.19.
If you read the discussion of ﬁeld lines earlier in this section, you should
realize that the electric ﬁeld exists between the lines as well as at the locations
of the lines themselves. But just to help you visualize the direction of the ﬁelds
from each of the three charges, the ﬁeld lines in Figure 3.19 have been drawn
on a tilt so that they are directly in line with the location at which you’re trying
to ﬁnd the total ﬁeld (the origin in this case). You should also remember that
just because the lines have grown too small to see does not mean that the ﬁeld
has gone to zero. Hence the electric ﬁeld produced by q1 points down and to
the right at the location of the electron, the ﬁeld from q2 points down and to
the left, and the ﬁeld from q3 points up and to the right. It is these three vector
ﬁelds that you will have to add together to determine the total electric ﬁeld at
the point of interest.
Using Eq. 3.28, the electric ﬁelds due to the three point charges q1, q2, and
q3 may be written as
⃗E1 = ke
q1
r2
1
ˆr1,
⃗E2 = ke
q2
r2
2
ˆr2,
⃗E3 = ke
q3
r2
3
ˆr3.
(3.29)

## Page 99

3.3 The electric ﬁeld
87
Of course, you know from Figure 3.19 that these three electric ﬁelds do not
point in the same direction. That’s because the unit vector ˆr1 points radially
outward from the location of charge q1, and ˆr2 and ˆr3 point radially outward
from q2 and q3, respectively. This means you can’t add the three electric ﬁelds
algebraically; to ﬁnd the total ﬁeld you must use vector addition. You’ll ﬁnd
an example of the vector addition of electric ﬁelds in the problems at the end
of this chapter and the on-line solutions.
As you might suspect, it’s not just the simple operations of vector addition
and multiplication by a scalar that ﬁnd use in electrostatics. If you followed
the discussion of the divergence operation in Chapter 2, you may be wonder-
ing about the divergence of the electrostatic ﬁelds produced by a point charge
(Figures 3.16 and 3.17). In fact, one of the fundamental laws of electrostatics
is Gauss’s Law for electric ﬁelds, the differential form of which is
⃗∇◦⃗E = ρ/ϵ0,
(3.30)
where ρ represents the volume electric charge density (coulombs per cubic
meter) and ϵ0 is the vacuum permittivity of free space (8.85×10−12 Nm2/C2).
Gauss’s Law for electric ﬁelds tells you that electric ﬁeld lines diverge from
any location at which positive charge exists (positive ρ) and converge upon
any location at which negative charge is present (negative ρ). This explains the
analogy between the “ﬂow” of electrostatic ﬁeld lines and the ﬂow of a ﬂuid.
In this analogy, positive charge acts as the “source” of electrostatic ﬁeld lines
in the same sense as a faucet acts as the source of ﬂuid, and negative charge
acts as a “sink” of electrostatic ﬁeld lines just as a drain does for ﬂuid.
Note what happens when you take the divergence of the electric ﬁeld of a
point charge (this is most easily done in spherical coordinates):
⃗∇◦⃗E = 1
r2
∂
∂r (r2Er) = 1
r2
∂
∂r

r2ke
q
r2

= 1
r2
∂
∂r (keq) = 0.
This is consistent with the worked example in Chapter 2 showing that the
divergence of any radial vector ﬁeld is zero if the amplitude of the ﬁeld falls
off as 1/r2. Zero, that is, at all locations except where r = 0, the location of
the source of the ﬁeld. Thus Gauss’s Law tells you that electrostatic ﬁeld lines
diverge only from those locations at which positive electric charge exists, and
converge only on those locations at which negative charge exists.
You can gain additional understanding of the behavior of the electrostatic
ﬁeld by considering the curl of ⃗E for a point charge. Since Eθ and Eφ are both
zero, the curl in spherical coordinates becomes

## Page 100

88
Vector applications
⃗∇× ⃗E = 1
r
1
sin θ
∂Er
∂φ
ˆθ + 1
r

−∂Er
∂θ

ˆφ
= 1
r
1
sin θ
∂
∂φ
keq
r

ˆθ + 1
r

−∂
∂θ
keq
r

ˆφ
= 0.
This is not a surprising result in light of the radial nature of the electrostatic
ﬁeld of a point charge.
As mentioned in Chapter 2, vector ﬁelds with zero curl are called irro-
tational, and such ﬁelds have several important properties. One of those
properties arises from the fact that the curl of a gradient is always zero: an
irrotational vector ﬁeld may always be written as the gradient of a scalar ﬁeld.
In the case of electrostatic ﬁelds, the electric ﬁeld may be written as the gra-
dient of the scalar electric potential (usually written as φ or V ). By convention,
the electric ﬁeld is written as the negative gradient of the scalar potential, so
you’re likely to see this relationship written as
⃗E = −⃗∇V,
(3.31)
where V is the scalar electric potential with units of Nm/C (equivalent to joules
per coulomb or volts).
Since the electric ﬁeld is the negative of the change in electric potential
with distance, moving along an electric ﬁeld line in the direction it’s pointing
means that you’re moving toward a region of lower electric potential. Likewise,
moving in the opposite direction (opposite to the direction of the ﬁeld) takes
you into a region of higher potential, and moving perpendicular to the ﬁeld
lines results in no change in potential. Hence the “equipotential” surfaces are
always perpendicular to the electric ﬁeld lines.
Another differential vector operation useful in electrostatics is the Laplacian
(∇2). Recall that the Laplacian involves the second spatial derivative, specif-
ically the divergence of the gradient. Since the electrostatic ﬁeld ⃗E may be
written as the negative of the gradient of the scalar potential V , taking the
divergence of the electric ﬁeld gives:
⃗∇◦⃗E = ⃗∇◦(−⃗∇V ) = −∇2V.
(3.32)
Since Gauss’s Law says that the divergence of the electrostatic ﬁeld must equal
ρ/ϵ0, this means
∇2V = −ρ/ϵ0.
(3.33)
This is known as Poisson’s Equation. Since the Laplacian ﬁnds peaks and val-
leys of a function (locations at which the value of the function differs from the

## Page 101

3.4 The magnetic ﬁeld
89
average value at surrounding locations), Poisson’s Equation tells you that the
electric potential can have local maxima and minima only at locations at which
charge is present (that is, where ρ ̸= 0). And if you recall that the Laplacian
is negative at peaks and positive at valleys, you can see that positive charge
produces a peak in electric potential while negative charge produces a valley.
This is one reason that the electric ﬁeld is taken as the negative gradient of the
electric potential.
In regions in which the electric charge density (ρ) is zero, Poisson’s
Equation becomes Laplace’s Equation:
∇2V = 0,
(3.34)
so there are no maxima or minima in electric potential for locations with zero
charge density.
3.4 The magnetic ﬁeld
In this section, you can read about the behavior of the magnetic ﬁeld ( ⃗B) and
the magnetic force on a moving charged particle. You’ll also ﬁnd a discus-
sion of the application of the vector operations of divergence and curl to the
magnetostatic ﬁeld.
Unlike electrostatic ﬁeld lines, which diverge from positive charge and con-
verge on negative charge, magnetic ﬁeld lines form circles around the electric
current (ﬂowing charge) that is producing the magnetic ﬁeld. And just as
stationary source charges produce electrostatic ﬁelds, stationary currents (in
which the charge ﬂow is constant) produce magnetic ﬁelds that are called
“magnetostatic.” An example of such a ﬁeld is shown in Figure 3.20. The
direction of those ﬁeld lines is determined using the right-hand rule: if you
put the thumb of your right hand along the direction of current ﬂow and curl
I
B
Current-carrying
straight wire
(out of page
   on this side)
(into page
      on this side)
B
Figure 3.20 Magnetic ﬁeld of a long, straight wire.

## Page 102

90
Vector applications
your ﬁngers (like you’re grabbing the current), the magnetic ﬁeld points in the
direction of your curled ﬁngers. So if you were to reverse the direction of that
current ﬂow, the magnetic ﬁeld lines would still form circles around the cur-
rent, but the magnetic ﬁeld lines would point in the opposite direction (as you
can tell by observing the direction of your curled ﬁngers when your thumb
points in the opposite direction).
You can tell by the spacing of the ﬁeld lines in Figure 3.20 that the strength
of the magnetic ﬁeld is decreasing as the distance from the current increases.
For a thin wire of inﬁnite length carrying current I, the vector magnetic ﬁeld
is given by the equation
⃗B = μ0I
2πr
ˆφ,
(3.35)
where μ0 is a constant called the magnetic permeability of free space, r is
the distance from the wire to the point at which the magnetic ﬁeld is being
determined, and ˆφ is the cylindrical-coordinate unit vector that points in the
direction circulating around the wire. The standard (SI) unit of magnetic ﬁeld
is the tesla (T).
Comparing the magnetic ﬁeld lines around an electric current to the vector
ﬁelds with various values of divergence and curl discussed in Chapter 2, you
may have already guessed that magnetic ﬁelds ﬁt into the “low divergence,
high curl” category. Recall that electric ﬁeld lines originate on positive charge
and terminate on negative charge, and it is only at the location of those charges
that the divergence of the electrostatic ﬁeld is non-zero. And since magnetic
ﬁeld lines circulate back onto themselves rather than diverging from and con-
verging upon speciﬁc locations, it’s reasonable to expect small values for the
divergence of the magnetic ﬁeld. In fact, the divergence of the magnetic ﬁeld
( ⃗B) is exactly zero, as indicated by Gauss’s Law for magnetic ﬁelds:
⃗∇◦⃗B = 0.
(3.36)
You can verify this for the magnetic ﬁeld of a long, straight wire by taking the
divergence of the ﬁeld in Eq. 3.35:
⃗∇◦⃗B =
1
r sin θ
∂Bφ
∂φ =
1
r sin θ
∂
∂φ
μ0I
2πr

= 0.
As you might expect from the discussion of curl in Chapter 2, the magnetic
ﬁeld around a current-carrying wire has zero curl:

## Page 103

3.4 The magnetic ﬁeld
91
⃗∇× ⃗B =

−∂Bφ
∂z

ˆr + 1
r
∂(r Bφ)
∂r

ˆz
=

−∂
∂z
μ0I
2πr

ˆr + 1
r
 ∂
∂r

r μ0I
2πr

ˆz
= 0.
As in the case of the divergence of the electric ﬁeld, which has a non-zero value
only at locations at which charge exists, the only locations at which the curl of
the magnetic ﬁeld is non-zero are locations at which current exists (that is, at
the singularity point r = 0).
Other uses of vectors and vector operations come about when you consider
the force ( ⃗FB) produced by a magnetic ﬁeld ( ⃗B) on a moving electric charge
(q). This force is given by the vector equation
⃗FB = q⃗v × ⃗B,
(3.37)
where ⃗v is the velocity of the charged particle with respect to the magnetic
ﬁeld. The magnitude of the force is readily found using the deﬁnition of the
magnitude of the vector cross product (| ⃗A × ⃗B| = | ⃗A|| ⃗B| sin θ):
| ⃗FB| = q|⃗v|| ⃗B| sin θ,
(3.38)
where θ is the angle between vector ⃗v and vector ⃗B.
Examined carefully, Eqs. 3.37 and 3.38 can tell you a great deal about how
magnetic ﬁelds affect charged particles. Compare these equations to Eq. 3.27
( ⃗FE = q ⃗E), and note that there are similarities and differences between
electric and magnetic forces:
• Similarity: Both are directly proportional to the amount of charge (q);
• Similarity: Both are directly proportional to the ﬁeld strength ( ⃗E or ⃗B);
• Difference: The velocity (⃗v) of the particle appears in the magnetic
equation;
• Difference: The magnetic force depends on the angle between the velocity
and the magnetic ﬁeld;
• Difference: The magnetic force is perpendicular to both the velocity and the
magnetic ﬁeld.
The similarities seem reasonable: both electric and magnetic forces are
stronger if the ﬁelds are stronger and if the amount of charge is greater. Also,
charges with opposite signs feel forces in opposite directions. The ﬁrst listed
difference (the fact that the magnetic force depends on the velocity of the parti-
cle) has the interesting consequence that a charged particle at rest with respect

## Page 104

92
Vector applications
to the magnetic ﬁeld (⃗v = 0) feels no force whatsoever from that ﬁeld. And
for particles moving with respect to the magnetic ﬁeld, the faster the particle
moves, the stronger the magnetic force becomes.
The presence of the vector cross product in the magnetic force equation
also has some important consequences. One of those consequences is that
charged particles moving in a direction parallel or antiparallel to the magnetic
ﬁeld feel zero magnetic force. That’s because in both the parallel (θ = 0◦)
and antiparallel (θ = 180◦) cases, the sine term in Eq. 3.38 is zero. So
the closer the angle θ between ⃗v and ⃗B is to 90◦, the stronger the magnetic
force.
Another consequence of the vector cross product in Eq. 3.37 is that the mag-
netic force ( ⃗FB) can never point in the direction of the magnetic ﬁeld, since the
vector result of the cross product is by deﬁnition perpendicular to both vectors
forming the product (⃗v and ⃗B in this case). For this same reason, the magnetic
force can never point in the direction of the particle’s velocity vector, and must
in fact be perpendicular to that vector. So if you imagine the ﬂat plane formed
by the velocity vector and the magnetic ﬁeld, you can be sure that the magnetic
force (if any) must be perpendicular to that plane.
If you’ve read the discussion of radial and tangential acceleration in Sec-
tion 3.2, you should understand that this means that magnetic ﬁelds can
provide radial but never tangential acceleration to a charged particle (since
tangential acceleration requires a component of force that’s either parallel
or antiparallel to the velocity vector). And since ⃗v × ⃗B always points per-
pendicular to ⃗v, magnetic ﬁelds can provide only radial acceleration. Thus
magnetic ﬁelds may change the direction but never the speed of charged
particles.
An example of the geometry involved in magnetic force is shown in
Figure 3.21. In this ﬁgure, the direction of the magnetic ﬁeld is into the page, as
B
v
q
Figure 3.21 Charged particle moving to right; magnetic ﬁeld into page.

## Page 105

3.4 The magnetic ﬁeld
93
B
v
q
Force in same direction as v × B if q positive
Force in opposite direction from v × B if q negative
Push v into B (into page)
with right hand; thumb
shows direction of v × B 
FB
FB
Figure 3.22 Magnetic force for positive and negative charges.
indicated by the crosses inside circles,11 and the charged particle (q) is moving
to the right.
To determine the direction of the magnetic force in this case, you simply
have to imagine forming the vector cross product ⃗v × ⃗B using the right-hand
rule, as shown in Figure 3.22. Once you know the direction of ⃗v × ⃗B, it’s
very important to remember (but easy to forget) that you must then reverse
the direction if the charge q is negative (since by Eq. 3.37, ⃗FB = q⃗v × ⃗B,
meaning that the magnetic force is opposite to the direction of ⃗v × ⃗B if
q is negative). This explains why two directions for the magnetic force ⃗FB
are shown in Figure 3.22: upward if q is positive and downward if q is
negative.
Once you understand the direction of the magnetic force relative to the
velocity of the charged particle, it should help explain why you may have
heard or read about charged particles “circling around magnetic ﬁeld lines” or
perhaps “spiralling along the magnetic ﬁeld.” Consider the positively charged
particle q in Figure 3.23. If this particle is initially at the leftmost position in
the ﬁgure, travelling with velocity ⃗v straight up the page, and the magnetic ﬁeld
⃗B points directly out of the page, the direction of the magnetic force q⃗v × ⃗B is
initally to the right (as you can determine using the right-hand rule). This force
causes the particle to travel on the dashed path to the topmost position in the
ﬁgure. At that point, the magnetic force ⃗FB points straight down the page. Just
as at the previous position, since q is positively charged, the magnetic force
points in the same direction as ⃗v × ⃗B. This now-downward force causes the
particle to travel to the rightmost position, at which point the velocity is straight
11 This is common notation in physics and engineering; you can remember it by thinking of a
hunter’s feathered arrow. Seen from the back, you can see the back edges of the feathers, so it
looks like this: ⊗. But seen from the front, you can see the arrow’s point, so it looks like
this: ⊙.

## Page 106

94
Vector applications
FB
v
Use right hand
to push v out of
page (into the
direction of B)
Right hand
Right hand
Right hand
q
q
q
q
B
FB
FB
FB
v
v
v
Figure 3.23 Magnetic force on positive charge.
down the page and the magnetic force ⃗FB points directly to the left. This force
causes the particle to reach the bottom position in Figure 3.23, at which point
the velocity is to the left and the magnetic force points straight up the page.
Under the inﬂuence of this force, the particle will travel back to the starting
(leftmost) position, and the entire cycle will repeat. So this positively charged
particle makes a clockwise circle around the outward-pointing magnetic
ﬁeld.
Applying the same reasoning to a negatively charged particle, you should
be able to determine that it will make counter-clockwise circles around the
same outward-pointing magnetic ﬁeld. And if the ﬁeld direction is reversed,
so that ⃗B points into the page rather than outward, the sense of the parti-
cle’s rotation will be reversed (so that a positively charged particle will circle
counter-clockwise and a negatively charged particle will circle in the clockwise
direction).
The particles in these examples retrace the same path over and over, so what
makes some particles “spiral around” the lines of the magnetic ﬁeld? Simply
this: the particle’s velocity must have a component parallel (or antiparallel) to
the direction of the magnetic ﬁeld. Note that the particle shown in Figure 3.23
is moving entirely in the plane of the page, and the magnetic ﬁeld is perpen-
dicular to the page. Hence the particle’s velocity vector has no component
along the magnetic ﬁeld (into or out of the page). If such a component were
present, the particle would have a component of its motion along the ﬁeld

## Page 107

3.5 Chapter 3 problems
95
lines while also circling around them. In that case, the circular path shown in
Figure 3.23 would move into or out of the paper over time, and the circle would
become a spiral. The magnetic ﬁeld has no effect on the velocity component
(v||) parallel or antiparallel to the ﬁeld (since there’s no magnetic force in that
direction), so the speed with which the particle moves along the ﬁeld line is
constant as long as no other forces are acting.
3.5 Chapter 3 problems
3.1 Solve the box-on-a-ramp problem (that is, ﬁnd the acceleration of
the box) for the frictionless case using a Cartesian coordinate system
for which the y-axis points vertically upward and the x-axis points
horizontally to the right.
3.2 The maximum force of static friction is μs ⃗Fn, where μs is the coefﬁcient
of static friction and ⃗Fn is the normal force. How big must the coefﬁcient
of static friction μs be to prevent a box of mass m from sliding down a
ramp inclined 20 degrees from the horizontal?
3.3 If a delivery woman pushes a box of mass m up a 2 m ramp with a force
of 10 N, how fast is the box moving at the top of the ramp if the ramp
angle to the horizontal is 25 degrees and the coefﬁcient of kinetic friction
is 0.33?
3.4 If the hammer-thrower shown on the cover of this book wishes to
launch a hammer of mass 7.26 kg on a cable of length 1.22 m with a
speed of 22 m/s, what is the magnitude of the centripetal force he must
supply?
3.5 Imagine a Formula 1 car going around a curve with radius of 10 m while
slowing from a speed of 180 mph to 120 mph in 2 s. What are the magni-
tude and direction of the car’s acceleration at the instant the car’s speed
is 150 mph?
3.6 If three electric charges q1, q2, and q3 have the values and locations
shown in Figure 3.18, ﬁnd the electric ﬁeld they produce at the origin
(x = 0, y = 0), then use your value of the ﬁeld to determine the electric
force on an electron at that location.
3.7 If the vector electric ﬁeld ⃗E in some region is given in spherical coordi-
nates by 5
r ˆr + 2
r sin θ cos φ ˆθ −1
r sin θ cos φ ˆφ (N/C), what is the volume
charge density ρ in that region?
3.8 If the scalar electric potential V in some region is given in cylindrical
coordinates by V (r, φ, z) = r2sinφ e−3/z, what is the electric ﬁeld ⃗E in
that region?

## Page 108

96
Vector applications
3.9 For the scalar electric potential V of Problem 3.8, use Poisson’s Equation
to ﬁnd volume charge density ρ in that region.
3.10 Find the magnitude and direction of the magnetic force on a charged
particle with charge −4 nC and velocity ⃗v = 2.5 × 104 ˆı + 1.1 × 104 ˆj
(m/s) if the magnetic ﬁeld in the region is given by ⃗B = 1.2 × 10−3 ˆı +
5.6 × 10−3 ˆj −3.2 × 10−3 ˆk (T).

## Page 109

4
Covariant and contravariant
vector components
The vector concepts and techniques described in the previous chapters are
important for two reasons: they allow you to solve a wide range of problems
in physics and engineering, and they provide a foundation on which you can
build an understanding of tensors (the “facts of the universe”). To achieve that
understanding, you’ll have to move beyond the simple deﬁnition of vectors as
objects with magnitude and direction. Instead, you’ll have to think of vectors
as objects with components that transform between coordinate systems in spe-
ciﬁc and predictable ways. It’s also important for you to realize that vectors
can have more than one kind of component, and that those different types of
component are deﬁned by their behavior under coordinate transformations.
So this chapter is largely about the different types of vector component,
and those components will be a lot easier to understand if you have a solid
foundation in the mathematics of coordinate-system transformation.
4.1 Coordinate-system transformations
In taking the step from vectors to tensors, a good place to begin is to con-
sider this question: “What happens to a vector when you change the coordinate
system in which you’re representing that vector?” The short answer is that
nothing at all happens to the vector itself, but the vector’s components may be
different in the new coordinate system. The purpose of this section is to help
you understand how those components change.
Before getting to that, you should spend a few minutes considering the
statement that the vector itself doesn’t change if you change the coordinate
system. This may seem obvious in the case of scalars – after all, whether you
measure temperature in Celsius or Fahrenheit doesn’t make a room feel hot-
ter or colder. Now remember that vectors are mathematical representations of
97

## Page 110

98
Covariant and contravariant vector components
physical entities, and those entities don’t change just because you change the
coordinate system in which you’re representing them. Think about it: does the
size of a room change if you tilt your head to one side? Clearly not. But if you
use your tilted head to deﬁne up and down, then the points you designate as
the top and bottom of the room may change, and this will change what you
call the “height” and “width” of the room. The important idea is that the room
itself doesn’t change (it “remains invariant”) under such a change of coordinate
system. And if you deﬁne the center of your head to be the origin of your coor-
dinate system, then walking toward one wall will “offset” the room (that is, the
x, y, and z values of locations within the room may change), but once again
the room itself is unchanged. Likewise, specifying dimensions of the room in
inches rather than meters will allow you to put larger numbers in the real-estate
ad, but that doesn’t mean your room will hold a bigger sofa.
So if coordinate-system transformations such as rotation, translation, and
scaling leave physical quantities unchanged, what exactly does happen to a
vector when you transform coordinates? To understand that, consider the sim-
ple rotation of the two-dimensional Cartesian coordinate system shown in
Figure 4.1. In this transformation, the location of the origin has not changed,
but both the x- and y-axis have been tilted counter-clockwise by an angle θ.
The rotated axes are labeled x′ and y′ and are drawn using dashed lines to
distinguish them from the original axes.
What impact does this rotation have on a vector in this space? Take a look
at vector ⃗A and its components in Figure 4.2(a) and (b). Note that the rotation
has no effect on the length or direction of ⃗A (at ﬁrst glance, ⃗A may look a
bit different in Figure 4.2(a) and 4.2(b), but you can verify using a ruler and
protractor that the vector itself is exactly the same). But the rotation has clearly
caused the components of ⃗A to change: A′
x (the x′-component of A in the
tilted coordinate system) is longer than Ax, and A′
y is shorter than Ay. If you
y′
y
x
x′
θ
θ
Figure 4.1 Rotation of 2-D coordinate system.

## Page 111

4.1 Coordinate-system transformations
99
y′
y
x
x′
y′
y
x
x′
A′
A′
A
(a)
(b)
A
Ay
Ax
y
x
Figure 4.2 Change in vector components due to rotation of coordinate
system.
were to continue rotating your axes in the same direction, you’d eventually
reach an angle at which ⃗A lies entirely along the x′-axis, at which point the
y′-component of ⃗A would vanish (that is, A′
y = 0) and the x′-component would
equal the length of ⃗A (A′
x = | ⃗A|).
Finding the change in the components of a vector due to rotation of the
coordinate axes can be done both graphically using simple geometry and
analytically using the dot product. You’ll ﬁnd the graphical approach in this
section; the analytical approach is the subject of one of the problems at the end
of this chapter.
If you think about the changes to Ax and Ay in Figure 4.2, you might come
to realize that the vector component A′
x in the rotated coordinate system cannot
depend entirely on the component Ax in the original system. After all, Ax
contains some but not all of the information about vector ⃗A; the rest is in Ay.
And as the axes rotate, the axis that had pointed exclusively in the x-direction
now points partially in the (former) y-direction. So it seems reasonable that
the portion of ⃗A that had previously pointed in the original y-direction (and
so contributed only to Ay) now points partially in the x′-direction, and hence
contributes to the x′-component as well as the y′-component.
You can see how this works in Figure 4.3. The (a) portion of this ﬁgure
shows how the vector component Ax in the original (non-rotated) coordinate
system contributes to A′
x in the rotated system, and the (b) portion shows how
the vector component Ay in the original system contributes to A′
x in the rotated
system.
As you can see in both portions of the ﬁgure, A′
x can be considered to be
made up of two segments, labeled ℓ1 and ℓ2. So
A′
x = ℓ1 + ℓ2,
(4.1)

## Page 112

100
Covariant and contravariant vector components
y′
y
x
x′
A
Ax
Ax
A
x′
x
(a)
y′
y
x
x′
A
Ay
Ay
Ax
1
A′
y
y′
x
x′
A
(b)
x
A′x
A′x
A′x
α11
α12
α12
1
2
2
Figure 4.3 Dependence of A′x on Ax and Ay.

## Page 113

4.1 Coordinate-system transformations
101
and to determine how these segments depend on Ax and Ay, consider the right
triangles shown in Figure 4.3. In the (a) portion of the ﬁgure, you can see that
Ax is the hypotenuse of a right triangle formed by drawing a perpendicular
from the end of Ax to the x′-axis. Call the angle between the x-axis and the
x′-axis α11 (the reason for using double subscripts will become clear when
rotations are written in matrix notation). Then the length of ℓ1 (the projection
of Ax onto the x′-axis) is Ax cos(α11). Hence
ℓ1 = Ax cos(α11).
(4.2)
To ﬁnd the length of ℓ2, consider the right triangle shown in Figure 4.3(b).
In this case, the triangle is formed by sliding A′
x upward along the y′-axis
and then drawing a perpendicular from the tip of A′
x to the x-axis. From this
triangle, you should be able to see that
ℓ2 = Ay cos(α12),
(4.3)
where α12 is the angle formed by the tips of A′
x and Ay (which is also the angle
between the x′-axis and the y-axis, as you can see from the parallelogram in
Figure 4.3(b).
Adding the expressions for ℓ1 and ℓ2, you can write A′
x as
A′
x = Ax cos(α11) + Ay cos(α12),
(4.4)
where Ax and Ay are the components of vector ⃗A in the non-rotated coordinate
system, α11 is the angle between the x′-axis and the x-axis, and α12 is the angle
between the x′-axis and the y-axis. You should note that the new component
(A′
x) is a weighted linear combination of the original components (Ax and
Ay). “Weighted” because the cosine factors determine how heavily each of the
original components contributes to the new one, “linear” because the original
components appear to the ﬁrst power only, and “combination” because both
Ax and Ay contribute to A′
x.
A similar analysis for A′
y, the y-component of vector ⃗A in the rotated
coordinate system, gives
A′
y = Ax cos(α21) + Ay cos(α22),
(4.5)
where α21 is the angle between the y′-axis and the x-axis, and α22 is the angle
between the y′-axis and the y-axis.
The relationship between the components of vector ⃗A in the rotated and
non-rotated systems is conveniently expressed using vector/matrix notation1 as
1 Remember, there’s a review of matrix notation and algebra on the book’s website.

## Page 114

102
Covariant and contravariant vector components
 A′
x
A′
y

=
 cos (α11)
cos (α12)
cos (α21)
cos (α22)
  Ax
Ay

.
(4.6)
This is called a “transformation equation” for the components of vector ⃗A, and
the two-column matrix is called a “transformation matrix.” The elements of
that matrix are called the “direction cosines.” Note that for a rigid rotation of
the Cartesian axes through angle θ, the angles α11 and α22 are both equal to θ,
while α12 = 90◦−θ and α21 = 90◦+ θ. The transformation matrix in this
case is

cos (θ)
cos (90◦−θ)
cos (90◦+ θ)
cos (θ)

=

cos (θ)
sin (θ)
−sin (θ)
cos (θ)

,
(4.7)
since cos(90◦−θ) = sin(θ) and cos(90◦+ θ) = −sin(θ).
To understand how this works in practice, consider vector ⃗A given as
⃗A = 5ˆı + 3 ˆj
(4.8)
in a two-dimensional Cartesian coordinate system. Now imagine that the
x- and y-axes of that coordinate system are rotated counter-clockwise by 150◦,
as shown in Figure 4.4.
Before jumping to the equations to ﬁnd the components A′
x and A′
y in the
rotated coordinate system, it’s worth a few minutes to take a look at the diagram
to estimate what the effect of the rotation on the components will be. From
Figure 4.4(b), it’s pretty clear that both the A′
x and A′
y components will be
negative, and the A′
y component appears to be somewhat larger than the A′
x
component.
y′
y
x′
Ay
Ax
A
x
y′
y
x′
A′
A′
A
x
(b)
(a)
y
x
Figure 4.4 2-D Cartesian axes rotated by 150◦.

## Page 115

4.1 Coordinate-system transformations
103
y′
α22
α21
α12
α11
y
x′
x
Figure 4.5 Angles between original and rotated axes.
Now that you have an idea of what to expect, you can insert the relevant
values into Eq. 4.6. You know that Ax = 5 and Ay = 3, and using the angles
shown in Figure 4.5, you should be able to see that α11 = 150◦, α12 = 60◦,
α21 = 240◦, and α22 = 150◦.
So you have
 A′
x
A′
y

=
 cos (150◦)
cos (60◦)
cos (240◦)
cos (150◦)
  Ax
Ay

,
(4.9)
or
A′
x = 5 cos(150◦) + 3 cos(60◦) = −2.8,
(4.10)
and
A′
y = 5 cos(240◦) + 3 cos(150◦) = −5.1.
(4.11)
As a quick visual analysis suggested, both components are negative and the
y′-component is larger than the x′-component in the rotated system.
It is very important for you to understand that the transformation equation
(4.6) does not rotate or change the vector ⃗A in any way; it determines the values
of the components of vector ⃗A in a new coordinate system. This distinction is
important because you may be tempted to apply this transformation matrix to
basis vectors such as ˆı (1, 0) and ˆj (0, 1), which for a counter-clockwise 150◦
rotation gives for ˆı

## Page 116

104
Covariant and contravariant vector components
 cos (150◦)
cos (60◦)
cos (240◦)
cos (150◦)
  1
0

=
 1 cos (150◦) + 0 cos (60◦)
1 cos (240◦) + 0 cos (150◦)

=
 −0.866
−0.5

,
(4.12)
and for ˆj
 cos (150◦)
cos (60◦)
cos (240◦)
cos (150◦)
  0
1

=
 0 cos (150◦) + 1 cos (60◦)
0 cos (240◦) + 1 cos (150◦)

=

0.5
−0.866

.
(4.13)
There’s nothing inherently wrong with doing this, as long as you remember
what the results mean: these are the components of the original unit vectors
ˆı and ˆj (that is, the ones in the non-rotated coordinate system) expressed in
terms of the rotated coordinate axes, as you can see in Figure 4.6. These are
not the unit vectors ˆı′ and ˆj′ which point in the direction of the x′ and y′-axes
(remember that in the primed coordinate system, the unit vectors ˆı′ and ˆj′,
pointing along the rotated coordinate axes, must have components (1, 0) and
(0, 1), respectively).
Rigid rotation of Cartesian axes is only one type of the myriad coordinate
transformations that can change the components of a vector. But as long as the
new components can be written as weighted sums of the original components,
the transformation is linear and can be represented by a matrix equation. For
y′
x′
x
y′
y
x′
(b)
(a)
i
–0.5
–0.866
+0.5
–0.866
j
y′-component
of i in rotated
coordinate system
y′-component
of j in rotated
coordinate system
x′-component
of j in rotated
coordinate system
x′-component
of i in rotated
coordinate system
Figure 4.6 Components of ˆı and ˆj in rotated coordinate system.

## Page 117

4.2 Basis-vector transformations
105
reasons that will become clear when you read Section 4.3 of this chapter, such
transformations of vector components are called “inverse” or “passive” trans-
formations, which means the matrix equation of such a transformation will
look like this:
⎛
⎝
Components of
same vector
in new system
⎞
⎠=
⎛
⎝
Inverse
transformation
matrix
⎞
⎠
⎛
⎝
Components of
vector in
original system
⎞
⎠.
(4.14)
At this point, you may be wondering how you might go about transform-
ing the unit vectors of the original (non-rotated) system (that is, ˆı and ˆj) into
the unit vectors of the primed (rotated) system (ˆı′ and ˆj′). That’s a different
question, because you’re no longer asking, “Given the components of a vector
in one coordinate system, how do I ﬁnd the components of that same vector
in a different coordinate system?” Instead, you’re asking, “How do I change a
given vector (in this case, a unit vector in one coordinate system) into a differ-
ent vector (the unit vector in a different coordinate system)?” That question is
addressed in the next section.
4.2 Basis-vector transformations
The previous section illustrated what happens to the components of a vector
when the two-dimensional Cartesian axes are rotated, and the results are not
surprising: the components of the vector referenced to the new (rotated) axes
are different from the components referenced to the original (non-rotated) axes.
More speciﬁcally, the new components are weighted linear combinations of the
original components.
Now here’s a very important point: as your studies carry you along the
path from vectors to tensors, you will undoubtedly run across discussions of
“covariant” and “contravariant” vector components.2 In those discussions, you
may see words to the effect that covariant components transform in the same
way as basis vectors (“co” ≈“with”), and contravariant components trans-
form in the opposite way to basis vectors (“contra” ≈“against”). As you’ll
see later in this chapter, there’s plenty of truth in that description, but there’s
also a major pitfall. That’s because the “transformation” of basis vectors usu-
ally refers to the conversion of the basis vectors in the original (non-rotated)
coordinate system to the different basis vectors which point along the coordi-
nate axes in the new (rotated) system, whereas the “transformation” of vector
2 These components are identical in the Cartesian coordinate systems considered so far.

## Page 118

106
Covariant and contravariant vector components
components refers to the change in the components of the same vector referred
to two different sets of coordinate axes. The potential for confusion here is suf-
ﬁciently great to cause Schutz to write that “the reason that ‘co’ and ‘contra’
have been abandoned is that they mix up two very different things.”3 Schutz
wrote that in 1983, and for better or worse, the “covariant/contravariant” ter-
minology is still with us – that’s why in this book you’ll ﬁnd those words as
well as more modern terminology.
Why did the “covariant/contravariant” terminology take hold in the ﬁrst
place? Probably because the process of changing a vector into a different vec-
tor has much in common with the process of transforming the components of
a vector from one coordinate system to another. This section shows you how
to make a new vector using rotation (speciﬁcally, how to rotate basis vectors).
To understand the process of rotating a vector, consider vector
⃗A in
Figure 4.7(a). The rotation shown in Figure 4.7(b) causes vector ⃗A to point
in a different direction, which means it is no longer the same vector (which
is why it’s labeled ⃗A′ after the rotation). The relationship between the com-
ponents of the original (non-rotated) vector and the new (rotated) vector can
be found rather easily through geometric constructions such as those shown in
Figure 4.8. In this example, the rotation angle is α. The x- and y-components
of vectors ⃗A and ⃗A′ are
Ax = | ⃗A| cos(θ),
A′
x = | ⃗A′| cos(θ′),
Ay = | ⃗A| sin(θ),
A′
y = | ⃗A′| sin(θ′).
But θ′ = α + θ, so the components A′
x and A′
y are
A′
x = | ⃗A′| cos(α + θ) = | ⃗A′| [cos(α) cos(θ) −sin(α) sin(θ)] ,
A′
y = | ⃗A′| sin(α + θ) = | ⃗A′| [sin(α) cos(θ) + cos(α) sin(θ)] .
Since the length of ⃗A must be the same as the length of ⃗A′ (the vector rotated
but did not change length), you can write | ⃗A| = | ⃗A′|, which means that
y
x
A
y
x
(b)
(a)
A
A′
Figure 4.7 Rotation of a vector.
3 Schutz, B., A First Course in General Relativity, p. 64. See further reading.

## Page 119

4.2 Basis-vector transformations
107
y
x
A
A′
θ′
θ
α
Figure 4.8 Angles involved in the rotation of a vector.
A′
x = | ⃗A′| [cos(α) cos(θ) −sin(α) sin(θ)]
= | ⃗A| cos(α) cos(θ) −| ⃗A| sin(α) sin(θ),
A′
y = | ⃗A′| [sin(α) cos(θ) + cos(α) sin(θ)]
= | ⃗A| sin(α) cos(θ) + | ⃗A| cos(α) sin(θ).
But | ⃗A| cos(θ) is just Ax and | ⃗A| sin(θ) is Ay, so you can write
A′
x = Ax cos(α) −Ay sin(α),
A′
y = Ax sin(α) + Ay cos(α),
or, as a matrix equation,
 A′
x
A′
y

=
 cos(α)
−sin(α)
sin(α)
cos(α)
  Ax
Ay

,
(4.15)
which tells you how to ﬁnd the components A′
x and A′
y of the new vector ( ⃗A′)
in the original coordinate system.
To see how this works in practice, consider a rotation such as the one shown
in Figure 4.7, but through a larger rotation angle of α = 150◦. If the original
vector is given by ⃗A = Axˆı + Ay ˆj = 5ˆı + 3 ˆj, then
 A′
x
A′
y

=
 cos(150◦)
−sin(150◦)
sin(150◦)
cos(150◦)
  5
3

=
 −5.83
−0.10

,
(4.16)
so the new vector ⃗A′ = −5.83ˆı −0.10 ˆj. This means that by rotating vector
⃗A through 150◦, you’ve produced a new vector that lies almost entirely along
the negative x-axis (you can see this by noting that the x-component is neg-
ative and much larger than the y-component). Remember that this is a new
vector expressed using the same basis (ˆı and ˆj) and is not the same vector
expressed using a new basis (because in this case you rotated the vector, not
the coordinate system).

## Page 120

108
Covariant and contravariant vector components
x′
x
y′
y
(b)
(a)
i
0.5
–0.866
–0.5
–0.866
j
x-component
of i′ in original
coordinate system
x-component
of j′ in original
coordinate system
y-component
of j′ in original
coordinate system
y
i′
x
j′
y-component
of i′ in original
coordinate system
Figure 4.9 Components of ˆı′ and ˆj′ in original (unrotated) coordinate system.
You can, of course, rotate the basis vectors ˆı and ˆj using this same approach.
This can be helpful if you’re faced with a problem involving a rotated coordi-
nate system and you wish to express the basis vectors pointing along the axes
of the rotated system in terms of the basis vectors in the original (non-rotated)
system. For example, to rotate the ˆı unit vector by 150◦counter-clockwise, you
can use
 ˆı′
x
ˆı′
y

=
 cos(150◦)
−sin(150◦)
sin(150◦)
cos(150◦)
  1
0

=
 −0.866
0.5

,
(4.17)
where ˆı′
x represents the x-component of the 150◦-rotated ˆı vector and ˆı′
y repre-
sents the y-component of the rotated ˆı vector, as shown in Figure 4.9(a). You
can also rotate the ˆj unit vector by the same angle using
 ˆj′
x
ˆj′
y

=
 cos(150◦)
−sin(150◦)
sin(150◦)
cos(150◦)
  0
1

=

−0.5
−0.866

,
(4.18)
where ˆj′
x represents the x-component of the 150◦-rotated ˆj vector and ˆj′
y
represents the y-component of the rotated ˆj vector, as shown in Figure 4.9(b).
Just as in Eq. 4.15, the new components of the ˆı′ and ˆj′ vectors are expressed
in the same coordinate system as the original ˆı and ˆj. As pointed out in the
previous section, the components of ˆı′ and ˆj′ in the rotated coordinate system
must be (1, 0) and (0, 1).
So if you wish to transform a set of basis vectors into new basis vec-
tors (pointing along different coordinate axes), you use a “direct” or “active”
transformation matrix, and the matrix equation looks like this:

