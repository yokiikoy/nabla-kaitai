<!-- source-pdf: FleischVectorsAndTensors.pdf | pages 61-90 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 61–90

## Page 61

2.9 Divergence
49
Doing likewise for the y- and z-components and adding yields
⃗∇◦⃗A = 3(x2 + y2 + z2)1/2 + (x2 + y2 + z2)
	
x2 + y2 + z2 = 4(x2 + y2 + z2)1/2 = 4r.
Thus the divergence in the vector ﬁeld in Figure 2.13(a) is increasing linearly
with distance from the origin.
Finally, consider the vector ﬁeld in Figure 2.13(b), which is similar to the
previous case but with the amplitude of the vector ﬁeld decreasing as the
square of the distance from the origin. The ﬂow lines are spreading out as they
were in Figure 2.13(a), but in this case you might suspect that the decreas-
ing amplitude of the vector ﬁeld will affect the value of the divergence. Since
⃗A = (1/r2)ˆr,
⃗A =
1
(x2 + y2 + z2)
xˆı + y ˆj + z ˆk
	
x2 + y2 + z2 =
xˆı + y ˆj + z ˆk
(x2 + y2 + z2)(3/2) ,
and
∂Ax
∂x
=
1
(x2 + y2 + z2)3/2 −x
3
2

(x2 + y2 + z2)−5/2(2x).
Adding in the y- and z-derivatives gives
⃗∇◦⃗A =
3
(x2 + y2 + z2)3/2 −3(x2 + y2 + z2)
(x2 + y2 + z2)5/2 = 0.
This validates the suspicion that the reduced amplitude of the vector ﬁeld with
distance from the origin may compensate for the spreading out of the ﬂow
lines. Note that this is true only for the case in which the amplitude of the
vector ﬁeld falls off as 1/r2 (and only for points away from the origin).8
Therefore, you must consider two key factors in determining the divergence
at any point: the spacing and the relative amplitudes of the ﬁeld lines at that
point. These factors both contribute to the total ﬂow of ﬁeld lines into or out of
an inﬁnitesimally small volume around the point. If the outward ﬂow exceeds
the inward ﬂow, the divergence is positive at that point. If the outward ﬂow is
less than the inward ﬂow, the divergence is negative, and if the outward and
inward ﬂows are equal the divergence is zero at that point.
So far the divergence has been calculated for the Cartesian coordinate sys-
tem, but depending on the symmetries of the problem, it might be solved
8 At the origin, where r = 0, a (1/r2)-vector ﬁeld experiences a singularity, and the Dirac delta
function must be employed to determine the divergence.

## Page 62

50
Vector operations
more easily using non-Cartesian systems. The divergence may be calculated
in cylindrical and spherical coordinate systems using
⃗∇◦⃗A = 1
r
∂
∂r (r Ar) + 1
r
∂Aφ
∂φ + ∂Az
∂z ,
(cylindrical)
(2.36)
and
⃗∇◦⃗A = 1
r2
∂
∂r (r2Ar) +
1
r sin θ
∂
∂θ (Aθ sin θ) +
1
r sin θ
∂Aφ
∂φ .
(spherical)
(2.37)
If you doubt the efﬁcacy of choosing the proper coordinate system,
you should re-work the last two examples in this section using spherical
coordinates.
2.10 Curl
The del operator followed by a cross ( ⃗∇×) signiﬁes the differential operation
of curl. The curl of a vector ﬁeld is a measure of the ﬁeld’s tendency to circulate
about a point, much like the divergence is a measure of the tendency of the
ﬁeld to ﬂow away from a point. But unlike the divergence, which produces
a scalar result, the curl produces a vector. The magnitude of the curl vector
is proportional to the amount of circulation of the ﬁeld around the point of
interest, and the direction of the curl vector is perpendicular to the plane in
which the ﬁeld’s circulation is a maximum.
The curl at a point in a vector ﬁeld can be understood by considering the
vector ﬁelds shown in Figure 2.14. To ﬁnd the locations of large curl in each
of these ﬁelds, look for points at which the ﬂow vectors on one side of the
point are signiﬁcantly different (in magnitude, direction, or both) from the
1
3
(a)
(b)
(c)
5
4
7
2
6
Figure 2.14 Vector ﬁelds with various values of curl.

## Page 63

2.10 Curl
51
ﬂow vectors on the opposite side of the point. Once again a thought experi-
ment is helpful: imagine holding a tiny paddlewheel at each point in the ﬂow.
If the ﬂow would cause the paddlewheel to rotate, the center of the wheel
marks a point of non-zero curl. The direction of the curl is along the axis of the
paddlewheel. By convention, the positive-curl direction is determined by the
right-hand rule: if you curl the ﬁngers of your right hand along the circulation
direction, your thumb points in the direction of positive curl.
Using the paddlewheel test, you can see that points 1, 2, and 3 in
Figure 2.14(a) and point 5 in Figure 2.14(b) are high-curl locations, and some
curl also exists at point 4. The uniform ﬂow around point 6 and the diverging
ﬂow lines around Point 7 in Figure 2.14(c) would not cause a tiny paddlewheel
to rotate, meaning that these are points of low or zero curl.
To make this quantitative, you can use the differential form of the curl or
“del cross” ( ⃗∇×) operator in Cartesian coordinates:
⃗∇× ⃗A =

ˆı ∂
∂x + ˆj ∂
∂y + ˆk ∂
∂z

×

ˆı Ax + ˆj Ay + ˆk Az

.
(2.38)
Recall that the vector cross-product may be written as a determinant:
⃗∇× ⃗A =

ˆı
ˆj
ˆk
∂
∂x
∂
∂y
∂
∂z
Ax
Ay
Az

,
(2.39)
which expands to
⃗∇× ⃗A =
∂Az
∂y −∂Ay
∂z

ˆı +
∂Ax
∂z −∂Az
∂x

ˆj +
∂Ay
∂x −∂Ax
∂y

ˆk. (2.40)
Notice that each component of the curl of ⃗A indicates the tendency of the
ﬁeld to rotate in one of the coordinate planes. If the curl of the ﬁeld has a
large x-component, it means that the ﬁeld has signiﬁcant circulation about
that point in the yz plane. The overall direction of the curl represents the axis
about which the rotation is greatest, with the sense of the rotation given by the
right-hand rule.
If you’re wondering how the terms in this equation measure rotation,
consider the vector ﬁelds shown in Figure 2.15. Look ﬁrst at the ﬁeld in
Figure 2.15(a) and the x-component of the curl in the equation: this term
involves the change in Az with y and the change in Ay with z. Proceeding
in the positive y-direction from the left side of the point of interest to the right,
Az is clearly increasing (it’s pointing in the negative z-direction on the left side
of the point of interest and the positive z-direction on the right side), so the term
∂Az
∂y must be positive. Looking now at Ay, you can see that it is positive below

## Page 64

52
Vector operations
x
y
z
z
x
y
(b)
Ay
Ay
Ay
Ay
Az
Az
Az
Az
(a)
Figure 2.15 Effect of ∂Ay
∂z and ∂Az
∂y on the value of the curl.
the point of interest and negative above, so it is decreasing in the positive z-
direction. Thus ∂Ay
∂z is negative, which means that it increases the value of the
curl when it is subtracted from ∂Az
∂y . Thus the curl has a large value at the point
of interest, as expected in light of the circulation of ⃗A about this point.
The situation in Figure 2.15(b) is quite different. In this case, both ∂Ay
∂z and
∂Az
∂y are positive, and subtracting ∂Ay
∂z from ∂Az
∂y gives a small result. The value
of the x-component of the curl is therefore small in this case. Vector ﬁelds with
zero curl at all points are called “irrotational.”
Here are expressions for the curl in cylindrical and spherical coordinates:
⃗∇× ⃗A =
1
r
∂Az
∂φ −∂Aφ
∂z

ˆr +
∂Ar
∂z −∂Az
∂r

ˆφ+ 1
r
∂(r Aφ)
∂r
−∂Ar
∂φ

ˆz,
(cylindrical)
(2.41)
⃗∇× ⃗A =
1
r sin θ
∂(Aφ sin θ)
∂θ
−∂Aθ
∂φ

ˆr + 1
r

1
sin θ
∂Ar
∂φ −∂(r Aφ)
∂r

ˆθ
+ 1
r
∂(r Aθ)
∂r
−∂Ar
∂θ

ˆφ.
(spherical)
(2.42)
A common misconception is that the curl of a vector ﬁeld is non-zero wher-
ever the ﬁeld appears to curve. However, just as the divergence depended both
on the spreading out and the changing length of ﬁeld lines, the curl depends not
only on the curvature of the lines but also on the strength of the ﬁeld. Consider
a curving ﬁeld that points in the ˆφ direction and decreases as 1/r:

## Page 65

2.10 Curl
53
⃗A = k
r
ˆφ.
Finding the curl of this ﬁeld is particularly straightforward in cylindrical
coordinates:
⃗∇× ⃗A =
1
r
∂Az
∂φ −∂Aφ
∂z

ˆr +
∂Ar
∂z −∂Az
∂r

ˆφ + 1
r
∂(r Aφ)
∂r
−∂Ar
∂φ

ˆz.
Since Ar and Az are both zero, this is
⃗∇× ⃗A
=

−∂Aφ
∂z

ˆr + 1
r
∂(r Aφ)
∂r

ˆz =

−∂(k/r)
∂z

ˆr + 1
r
∂(rk/r)
∂r

ˆz = 0.
To understand the physical basis for this result, consider again the ﬂuid-ﬂow
and paddlewheel analogy. Imagine the forces on the paddlewheel placed in the
ﬁeld shown in Figure 2.16(a). The center of curvature is well below the bottom
of the ﬁgure, and the spacing of the arrows indicates that the ﬁeld is getting
weaker with distance from the center. At ﬁrst glance, it may seem that this
paddlewheel would rotate clockwise due to the curvature of the ﬁeld, since the
ﬂow lines are pointing slightly upward at the left paddle and slightly downward
at the right. But consider the effect of the weakening of the ﬁeld above the axis
of the paddlewheel: the top paddle receives a weaker push from the ﬁeld than
the bottom paddle, as shown in Figure 2.16(b). The stronger force on the bot-
tom paddle will attempt to cause the paddlewheel to rotate counter-clockwise.
Thus the downward curvature of the ﬁeld is offset by the weakening of the
ﬁeld with distance from the center of curvature. And if the ﬁeld diminishes
as 1/r, the upward-downward push on the left and right paddles is exactly
compensated by the weaker-stronger push on the top and bottom paddles. The
clockwise and counter-clockwise forces balance, and the paddlewheel does not
turn – the curl at this location is zero, even though the ﬁeld lines are curved.
Weaker field
Stronger field
(a)
(b)
Upward-
pointing
field
Downward-
pointing
field
Weaker push
to the right
Stronger push
to the right
Upward push
Downward push
Figure 2.16 Offsetting components of the curl of ⃗A.

## Page 66

54
Vector operations
For this 1/r ﬁeld, the curl is zero everywhere except at the center of curvature
(where a singularity exists and must be handled using the delta function).
2.11 Laplacian
Once you know that the gradient operates on a scalar function and produces a
vector and that the divergence operates on a vector and produces a scalar, it’s
natural to wonder whether these two operations can be combined in a mean-
ingful way. As it turns out, the divergence of the gradient of a scalar function
φ, written as ⃗∇◦( ⃗∇φ), is one of the most useful mathematical operations in
physics and engineering. This operation, usually written as ∇2φ (but some-
times as △φ), is called the “Laplacian” in honor of Pierre-Simon Laplace, the
great French mathematician and astronomer.
Before trying to understand why the Laplacian operator is so valuable,
you should begin by recalling the operations of gradient and divergence in
Cartesian coordinates:
Gradient:
⃗∇φ = ˆı ∂φ
∂x + ˆj ∂φ
∂y + ˆk ∂φ
∂z .
(2.43)
Divergence:
⃗∇◦⃗A = ∂Ax
∂x + ∂Ay
∂y + ∂Az
∂z .
(2.44)
Since the x-component of the gradient of φ is ∂φ
∂x , the y-component of the gra-
dient of φ is ∂φ
∂y , and the z-component of the gradient of φ is ∂φ
∂z , the divergence
of the vector produced by the gradient is
⃗∇◦⃗∇φ = ∇2φ = ∂2φ
∂x2 + ∂2φ
∂y2 + ∂2φ
∂z2 .
(2.45)
Just as the gradient ( ⃗∇), divergence ( ⃗∇◦), and curl ( ⃗∇×) represent
differential operators, so too the Laplacian (∇2) is an operator waiting to be
fed a function. As you may recall, the gradient operator tells you the direc-
tion of greatest increase of the function (and how steep the increase is), the
divergence tells you how strongly a vector function “ﬂows” away from a point
(or toward that point if the divergence is negative), and the curl tells you how
strongly a vector function tends to circulate around a point. So what does the
Laplacian, the divergence of the gradient, tell you?
If you write the Laplacian operator as ∇2 =
∂2
∂x2 +
∂2
∂y2 + ∂2
∂z2 , it should
help you see that this operator ﬁnds the change in the change of the function

## Page 67

2.11 Laplacian
55
(if you make a graph, the change in the slope) in all directions from the point
of interest. That may not seem very interesting, until you consider that accel-
eration is the change in the change of position with time, or that the maxima
and minima of functions (peaks and valleys) are regions in which the slope
changes signiﬁcantly, or that one way to ﬁnd blobs and edges in a digital
image is to look for points at which the gradient of the brightness suddenly
changes.
To understand why the Laplacian performs such a diverse set of useful tasks,
it helps to understand that at each point in space, the Laplacian of a function
represents the difference between the value of the function at that point and
the average of the values at surrounding points. How does it do that? Consider
the region around the point labeled (0, 0, 0) in Figure 2.17. The function φ
exists in all three dimensions around this region, and the cube is shown only
to illustrate the location of six points around the central point (0, 0, 0), where
the value of the function φ is φ0. Notice that there are points in front of and
behind the central point (along the x-axis), points to the left and right (along
the y-axis), and points above and below (along the z-axis). To see how the
change in the change in φ is related to φ0, consider for now the points along the
x-axis, as shown in Figure 2.18. Notice that the value of φ at the point in back
of the central point is labeled φBack and the value of φ in front of the central
point is labeled φFront. If each of these points is located a distance of 	x
x
y
z
(0, 0, 0)
Right
Top
Left
Front
Bottom
Back
Figure 2.17 Points surrounding (0, 0, 0) at which φ = φ0.

## Page 68

56
Vector operations
x
=
 ~ 
=~
A
B
at A
at B
=
∂x
∂φ
φ0 – φBack
Δx
Δx
φBack
φ0
Δx
Δx
φFront
–
φFront – φ0
Δx
φ0 – φBack
Δx
Δx
∂x
∂φ
∂x
∂φ
∂x
∂
φFront – φ0
Δx
Figure 2.18 Change in φ along x-axis.
from (0, 0, 0), then the partial derivative of φ at point B can be approximated
by (φ0 −φBack)/	x. Likewise, the partial derivative of φ at point A can be
approximated by (φFront −φ0)/	x.
But the Laplacian involves not just the change in φ, but the change in the
change of φ. For that, you can write
∂
∂x
∂φ
∂x

= (φFront −φ0)/	x −(φ0 −φBack)/	x
	x
,
∂2φ
∂x2 = φFront + φBack −2φ0
	x2
.
(2.46)
And although this might not look very helpful, good things happen when you
combine this expression with the expression for the two points to the right and
left of (0, 0, 0):
∂2φ
∂y2 = φRight + φLef t −2φ0
	y2
,
(2.47)
and the equation for the points on top and on the bottom of (0, 0, 0):
∂2φ
∂z2 = φT op + φBottom −2φ0
	z2
.
(2.48)
If you pick your locations symmetrically so that 	x = 	y = 	z, then these
three equations together give you the following:

## Page 69

2.11 Laplacian
57
∂2φ
∂x2 + ∂2φ
∂y2 + ∂2φ
∂z2
= φFront + φBack + φRight + φLef t + φT op + φBottom −6φ0
	x2
.
(2.49)
Using the del-squared notation for the Laplacian and a little rearranging makes
this
∇2φ = −6
	x2

φ0 −1
6(φFront + φBack + φRight + φLef t + φT op + φBottom)

= −6
	x2 (φ0 −φavg),
(2.50)
where the average value of the function φ over the six surrounding points is
φavg = 1
6(φFront + φBack + φRight + φLef t + φT op + φBottom).
Equation 2.50 tells you that the Laplacian of a function φ at any point is
proportional to the difference between the value of φ at that point and the aver-
age value of φ at the surrounding points. The negative sign in this equation
tells you that the Laplacian is negative if the value of the function at the point
of interest is greater than the average of the function’s value at the surround-
ing points, and the Laplacian is positive if the value at the point of interest is
smaller than the average of the value at the surrounding points.
And how does the difference between a function’s value at a point and the
average value at neighboring points relate to the divergence of the gradient of
that function? To understand that, think about a point at which the function’s
value is greater than the surrounding average – such a point represents a local
maximum of the function. Likewise, a point at which the function’s value is
less than the surrounding average represents a local minimum. This is the rea-
son you may ﬁnd the Laplacian described as a “concavity detector” or a “peak
ﬁnder” – it ﬁnds points at which the value of the function sticks above or falls
below the values at the surrounding points.
To better understand how peaks and valleys relate to the divergence of the
gradient of a function, recall that the gradient points in direction of steepest
incline (or decline if the gradient is negative), and divergence measures the
“ﬂow” of a vector ﬁeld out of a region (or into the region if the divergence
is negative). Now consider the peak of the function shown in Figure 2.19(a)
and the gradient of the function in the vicinity of that peak, shown in Fig-
ure 2.19(b). Near the peak, the gradient vectors “ﬂow” toward the peak from
all directions. Vector ﬁelds that converge upon a point have negative diver-
gence, so this means that the divergence of the gradient in the vicinity of a

## Page 70

58
Vector operations
(a)
–0.2
–0.1
0
0.1
0.2
–0.25
–0.2
–0.15
–0.1
–0.05
0
0.05
0.1
0.15
0.2
x
y
Top view
Side view
10
8
6
4
2
0
1
0.5
0
–0.5
–1 –1
–0.5
0
x
z
y
0.5
1
(b)
Figure 2.19 Function φ (varying as 1/r) and the gradient and contours of φ
near the peak.
Side view
z
0.5
1
–10
–9
–8
–7
–6
–5
–4
–3
–2
–1
0
0 –0.5
–1
y
–1
–0.5
0
x
0.5
1
–0.2
–0.1
0
0.1
0.2
–0.25
–0.2
–0.15
–0.1
–0.05
0
0.05
0.1
0.15
0.2
x
y
Top view
(b)
(a)
Figure 2.20 Function φ (varying as −1/r) and the gradient and contours of φ
near the bottom of the valley.
peak will be a large negative number. This is consistent with the conclusion
that the Laplacian is negative near a function’s maximum point.
The alternative case is shown in Figures 2.20(a) and 2.20(b). Near the bot-
tom of a valley, the gradient “ﬂows” outward in all directions, so the divergence
of the gradient is a large positive number in this case (again consistent with the
conclusion that the Laplacian of a minimum point is positive). And what is the
value of the Laplacian of a function away from a peak or valley? The answer to
that question depends on the shape of the function in the vicinity of the point in
question. As described in Section 2.9, the value of the divergence depends on
how strongly the function “ﬂows” away from a small volume surrounding the

## Page 71

2.11 Laplacian
59
point of interest. Since the Laplacian involves the divergence of the gradient,
the question is whether the gradient vectors “ﬂow” toward or away from the
point (in other words, whether the gradient vectors tend to concentrate toward
or disperse away from that point). If the inward ﬂow of gradient vectors equals
the outward ﬂow, then the Laplacian of the function is zero at that point. But if
the length and direction of the gradient vectors conspire to make the outward
ﬂow greater than the inward ﬂow at some point, then the Laplacian is positive
at that point.
For example, if you’re climbing out of a circularly symmetric valley with
constant slope, the gradient vectors are spreading apart without changing in
length, which means the divergence of the gradient (and hence the Laplacian)
will have a positive value at that point. But if a different valley has walls for
which the slope gets less steep (so the gradient vectors get shorter) as you move
away from the bottom of the valley, it’s possible for the reduced strength of the
gradient vectors to exactly compensate for the spreading apart of those vectors,
in which case the Laplacian will be zero.
To see how this works mathematically, consider a three-dimensional func-
tion φ whose value decreases in inverse proportion to the distance r from the
origin. This function may be written as φ = k/r, where k is just a constant of
proportionality and r is the distance from the origin. Thus r = (x2+y2+z2)1/2
and φ = k/(x2 + y2 + z2)1/2. You can ﬁnd the value of the Laplacian for this
case using Eq. 2.45; the ﬁrst step is to ﬁnd the partial derivative of φ with
respect to x
∂φ
∂x =
−k(2x)
2(x2 + y2 + z2)3/2 =
−kx
(x2 + y2 + z2)3/2 ,
after which you take another partial with respect to x:
∂2φ
∂x2 =
−k
(x2 + y2 + z2)3/2 +
3
2

kx(2x)
(x2 + y2 + z2)5/2
=
−k
(x2 + y2 + z2)3/2 +
3kx2
(x2 + y2 + z2)5/2 .
The same approach for the second-order partials with respect to y and z gives
∂2φ
∂y2 =
−k
(x2 + y2 + z2)3/2 +
3ky2
(x2 + y2 + z2)5/2 ,
and
∂2φ
∂z2 =
−k
(x2 + y2 + z2)3/2 +
3kz2
(x2 + y2 + z2)5/2 .

## Page 72

60
Vector operations
Now it’s just a matter of adding all three second-order partials:
∂2φ
∂x2 + ∂2φ
∂y2 + ∂2φ
∂z2 =
−3k
(x2 + y2 + z2)3/2 + 3k(x2 + y2 + z2)
(x2 + y2 + z2)5/2
=
−3k
(x2 + y2 + z2)3/2 +
3k
(x2 + y2 + z2)3/2 = 0.
So for a three-dimensional function with 1/r-dependence, the Laplacian of
the function is zero everywhere away from the origin. What about at the origin
itself? That point requires special treatment, since the 1/r-dependence of the
function becomes problematic at r = 0. That special treatment involves the
Dirac delta function and integral rather than differential techniques.
You may occasionally have need to calculate the Laplacian in non-Cartesian
coordinates. For function ψ, the Laplacian in cylindrical and spherical coordi-
nates is given by:
Cylindrical
∇2ψ = 1
r
∂
∂r

r ∂ψ
∂r

+ 1
r2
∂2ψ
∂φ2 + ∂2ψ
∂z2 ,
(2.51)
Spherical
∇2ψ = 1
r2
∂
∂r

r2 ∂ψ
∂r

+
1
r2 sin θ
∂
∂θ

sin θ ∂ψ
∂θ

+
1
r2 sin2 θ
∂2ψ
∂φ2 . (2.52)
2.12 Chapter 2 problems
2.1 For vectors ⃗A = 3ˆı + 2 ˆj −ˆk and ⃗B = ˆj + 4ˆk, ﬁnd the scalar product
⃗A ◦⃗B and the angle between ⃗A and ⃗B.
2.2 If vector ⃗J = 2ˆı −ˆj + 5ˆk and ⃗K = 3ˆı + 2 ˆj + ˆk, ﬁnd the vector ⃗L that
equals the cross product ⃗J × ⃗K. Also show that ⃗L is perpendicular to
both ⃗J and to ⃗K.
2.3 Show that ⃗A ◦⃗B = Ax Bx + Ay By + Az Bz = | ⃗A|| ⃗B/ cos(θ) and that
| ⃗A × ⃗B| = | ⃗A|| ⃗B/ sin(θ).
2.4 Using the vectors of the previous two problems, ﬁnd the triple product
⃗J ◦( ⃗A × ⃗B). Compare your answer to ( ⃗J × ⃗A) ◦⃗B.
2.5 Using the vectors of Problems 1 and 2, ﬁnd the triple vector product
⃗J × ( ⃗A × ⃗B). Compare your answer to ( ⃗J × ⃗A) × ⃗B and to ⃗B × ( ⃗J × ⃗A).
2.6 For the function f (x, y) = x2 + 3y2 + 2xy + 3x + 5, ﬁnd ∂f
∂x and ∂f
∂y .
2.7 If φ = x2 + y2, what is ⃗∇φ at the position (x, y) = (3 cm, −2 cm)?
2.8 Find the divergence of the vector ﬁeld given by ⃗C = 5xyˆı −3x ˆj + 5z2 ˆk.

## Page 73

2.12 Chapter 2 problems
61
2.9 What is the curl of the vector ﬁeld given in the previous problem?
2.10 Find the Laplacian of the function given in Problem 2.6.
2.11 In mechanics, the work (W) done by a force ( ⃗F) acting over a displace-
ment ( ⃗dr) is deﬁned as the scalar product between the force and the
displacement, so W = ⃗F ◦⃗dr. How much work is done by the vertically
downward force of Earth’s gravity (| ⃗F| = mg, where g is the acceler-
ation of gravity) on a car with a mass of 1200 kg as the car moves 50
meters down a hill whose surface makes an angle of 20 degrees below
the horizontal?
2.12 Imagine trying to turn the head of a bolt by pushing on the handle of a
wrench. The vector torque exerted by the force you apply ( ⃗F) is given by
the equation ⃗τ = ⃗r × ⃗F, where ⃗r is a vector from the point of rotation
to the point of application of the force. If you push on the handle of the
wrench with a force of 25 N at a distance of 12 cm from the point of
rotation, in what direction should you push to maximize the torque on
the bolt head? If you push in that direction, how much torque will you
exert on the bolt head?

## Page 74

3
Vector applications
The real value of understanding vectors and how to manipulate them becomes
clear when you realize that your knowledge allows you to solve a variety of
problems that would be much more difﬁcult without vectors. In this chapter,
you’ll ﬁnd detailed explanations of four such problems: a mass sliding down
an inclined plane, an object moving along a curved path, a charged particle
in an electric ﬁeld, and a charged particle in a magnetic ﬁeld. To solve these
problems, you’ll need many of the vector concepts and operations described in
Chapters 1 and 2.
3.1 Mass on an inclined plane
Consider the delivery woman pushing a heavy box up the ramp to her delivery
truck, as illustrated in Figure 3.1. In this situation, there are a number of forces
acting on the box, so if you want to determine how the box will move, you need
to know how to work with vectors. Speciﬁcally, to solve problems such as this,
you can use vector addition to ﬁnd the total force acting on the box, and then
you can use Newton’s Second Law to relate that total force to the acceleration
of the box.
To understand how this works, imagine that the delivery woman slips off the
side of the ramp, leaving the box free to slide down the ramp under the inﬂu-
ence of gravity. For starters, pretend that the ramp is so slippery that friction
between the bottom of the box and the ramp surface is negligible (so the coef-
ﬁcient of friction is effectively zero). How fast will the box be moving when it
reaches the bottom of the ramp? Perhaps more importantly, on what does that
speed depend?
Whenever you approach a problem like this, it’s a good idea to begin
by drawing a diagram that shows all the forces acting on the box. Such a
62

## Page 75

3.1 Mass on an inclined plane
63
Figure 3.1 The delivery-truck problem.
Fn
Fg
Figure 3.2 Free-body diagram for mass on frictionless ramp.
“free-body” diagram will help you determine the total force acting on the
object, from which you can easily determine the object’s acceleration using
Newton’s Second Law (⃗a =  ⃗F/m).1 And once you know the acceleration,
it’s an easy matter to ﬁnd the velocity. An example of the free-body diagram
for this (frictionless) case is shown in Figure 3.2.
By removing the delivery woman and friction from the problem, the only
remaining forces acting on the box are the force of gravity ⃗Fg, which points
vertically downward,2 and the normal force ⃗Fn, which is perpendicular (or
“normal”) to the surface of the ramp. The origin of these forces is easy to
understand; the gravitational force is produced by the mass of the Earth, and
the normal force is produced by the ramp as a reaction to the force produced by
the box on the ramp (if the ramp weren’t pushing upward on the box, gravity
would cause the box to accelerate straight downward).
1 You may be more accustomed to seeing this as ⃗F = m⃗a, but the form shown above is meant to
remind you that it’s the sum of the forces that produces acceleration, and the primary job of all
mass is to resist acceleration (which is why mass lives in the denominator – if the same force is
applied to a large mass and a small mass, the small mass experiences greater acceleration).
2 This ignores local gravitational anomalies, which is a very reasonable thing to do for problems
of this type.

## Page 76

64
Vector applications
Fn
Fg
y
x
Figure 3.3 Free-body diagram with coordinate axes.
Do these two forces really act only at a single point somewhere inside the
box, as implied by Figure 3.2? Clearly not, since every particle in the box
is being pulled downward by the Earth’s gravity, and the force of the ramp
on the box occurs along the entire underside of the box. But to determine
the acceleration of the box in this problem, you don’t need to worry about
the actual point of application of the forces, because you can treat the box
as a particle that exists at a single location. That’s not always the case; in
problems involving torque and angular acceleration, for example, the point of
application of the force may be critically important. But the box in this prob-
lem is sliding, not rolling, down the ramp, and you’re perfectly justiﬁed in
treating the box as a single particle and drawing the forces as though they
all act at the same point. Furthermore, you’re less likely to make a mistake
about the angles of the forces if you draw them as in Figure 3.2. This approach
can be justiﬁed using the concept of center of mass (CM), since for a rigid
object of mass m you can consider the entire object as a single point and write
⃗aC M = ⃗FC M/m.
Before doing the vector addition of the two forces acting on the box to deter-
mine the total force, it’s a good idea to draw a set of coordinate axes onto your
free-body diagram, as in Figure 3.3. Of course, you’re free to draw the axes in
any direction you choose, but when you’re faced with a problem of a mass on
an inclined plane, there are certain beneﬁts to drawing the x-axis pointing
down the ramp (and parallel to the ramp surface) and the y-axis pointing
upward (and perpendicular to the ramp surface). This approach has the advan-
tage that the normal force lies entirely along the positive y-axis, and the motion
of the block sliding down the ramp is entirely in the positive x-direction (as
long as the box stays on the ramp). To pay for that advantage, you’ll have
to use a bit of geometry to ﬁnd the x- and y-components of the gravitational

## Page 77

3.1 Mass on an inclined plane
65
θ
θ
θ
θ
θ
y
x
y
x
Parallel to ramp
surface (and to
x-axis)
(b)
(a)
Fn
Fg
Fg
Fn
90°–θ
90°–θ
Figure 3.4 Geometry to ﬁnd the angle of ⃗Fg.
force, since the vector ⃗Fg points straight downward and is therefore aligned
with neither the down-plane (x-) nor the perpendicular-to-plane (y-) axis.3
The key to ﬁnding the x-component ( ⃗Fg,x) and the y-component ( ⃗Fg,y) of
the gravitational force ( ⃗Fg) is to realize that the angle θ between the ramp
surface and the horizontal is also the angle between ⃗Fg and the negative y-axis,
as shown in Figure 3.4(a).
If you’re uncertain why the two angles shown as θ in Figure 3.4(a) must be
the same, take a look at Figure 3.4(b). Completing the two triangles shown in
Figure 3.4(b) should help you see that the angle between ⃗Fg and the negative
y-axis is indeed θ (you may also be able to see this by imagining the case in
which θ = 0◦or θ = 90◦).
Once you’re convinced that the angle between ⃗Fg and the negative y-
axis is θ, it’s quite straightforward to determine ⃗Fg,x and ⃗Fg,y, the x- and
y-components of the gravitational force vector
⃗Fg. As you can see in
Figure 3.5, the components of ⃗Fg are given by
⃗Fg,x = | ⃗Fg|sinθ(ˆı),
⃗Fg,y = | ⃗Fg|cosθ(−ˆj),
(3.1)
where the minus sign before the ˆj accounts for the fact that this component
points in the negative y-direction.
3 You may, of course, choose your axes to point exactly horizontally and vertically, in which case
⃗Fg would point entirely in the negative y-direction. In that case, the normal vector ⃗Fn would
have both x- and y-components. But since other forces (such as friction and the delivery
woman’s push) generally point along the ramp surface, tilting your coordinate axes may well
save you time later.

## Page 78

66
Vector applications
Length = |Fg|cos(θ)
Length = |Fg|sin(θ)
Fn
θ
θ
y
x
Fg
Figure 3.5 x- and y-components of ⃗Fg.
A note about notation: as mentioned in Chapter 1, it’s customary to write
Eqs. 3.1 as
Fg,x = | ⃗Fg|sinθ,
Fg,y = −| ⃗Fg|cosθ,
(3.2)
that is, as scalars rather than vectors. That’s because the direction of vector
components should be clear from the subscript: the x-component is always
in the ˆı direction (or −ˆı direction if it’s negative), and the y-component is
always in the ˆj direction (or −ˆj direction if it’s negative). So you can write
the components of a vector as scalars or vectors, as long as you remember that
each component points in a speciﬁc direction, which means you cannot simply
add the x- and y-components algebraically, even if they’re written as scalars.
You must add them as vectors.
Whether you write the components as vectors or scalars, having the x- and
y-components of ⃗Fg in hand and knowing that the normal force of the plane on
the box is entirely in the positive y-direction, you’re now in a position to use
vector addition to ﬁnd the total force acting on the box. Writing the magnitude
of the sum of the forces in the x-direction, you have
| ⃗Fx| = | ⃗Fg|sinθ,
(3.3)
and in the y-direction
| ⃗Fy| = (| ⃗Fn| −| ⃗Fg|cosθ).
(3.4)
Alternatively,
instead
of
writing
separate
equations
for
the
x-
and
y-components of the total force, you can write a vector equation incorporating
both:
 ⃗F = (| ⃗Fg|sinθ)ˆi + (| ⃗Fn| −| ⃗Fg|cosθ) ˆj,
(3.5)

## Page 79

3.1 Mass on an inclined plane
67
which contains exactly the same information as Eqs. 3.3 and 3.4.
Getting from the total force to the acceleration of the box is a simple step
thanks to Isaac Newton, whose Second Law tells you that the magnitudes of
the x- and y-components of the acceleration are
ax = | ⃗Fx|/m = (| ⃗Fg|sinθ/m),
(3.6)
and
ay = | ⃗Fy|/m = [(| ⃗Fn| −| ⃗Fg|cosθ)/m],
(3.7)
or, in full vector form,
⃗a =  ⃗F/m = (| ⃗Fg|sinθ/m)ˆi + [(| ⃗Fn| −| ⃗Fg|cosθ)/m] ˆj.
(3.8)
Whether you realize it or not, you almost certainly know two facts that will
allow you to simplify these equations considerably. The ﬁrst is that the magni-
tude of the force of gravity (| ⃗Fg|) on an object of mass “m” is simply equal to
mg, where “g” is the magnitude of the acceleration of gravity (9.8 m/s2 at the
Earth’s surface).4 So wherever you have the factor | ⃗Fg|, you can substitute the
expression mg.
The second simpliﬁcation is produced by the realization that as long as the
box stays on the ramp and doesn’t ﬂy off into the air or break through to the
ground, the y-component of the acceleration (ay) must remain zero (remember
that the y-axis is perpendicular to the surface of the ramp). Using the fact that
| ⃗Fg| = mg and that ay = 0 turns Eqs. 3.6 and 3.7 into the following:
ax = mg sin θ/m = g sin θ
(3.9)
and
ay = (| ⃗Fn| −mg cos θ)/m = 0.
(3.10)
When you’re working a physics problem, it’s a good idea to step back from
your calculations once in a while to look at your intermediate results to see
if they’re trying to tell you something – and that’s certainly the case at this
point. Equation 3.9 already has an important result for you: in the absence of
the upward-pushing delivery woman and with no friction, the box will accel-
erate down the ramp (that is, in the +x-direction) with an acceleration that
depends on only two things: which planet the delivery truck is on (that is, the
value of “g”) and the angle that the ramp makes with the horizontal (θ). In this
4 Remember that mass is a measure of the amount of material an object contains and weight is
the force of gravity on that mass. So mass is a scalar (magnitude only) and weight is a vector
(magnitude = mg and direction = straight down). Should you travel in space, your weight will
change as you leave the Earth’s gravity behind, but your mass will remain the same.

## Page 80

68
Vector applications
case, just as for a freely falling object, the mass of the box does not affect its
acceleration.5
Since the sine of the ramp angle can never be greater than one, Eq. 3.9 also
tells you that the magnitude of the acceleration of the object (g sin θ) can never
be greater than g, the accleration of gravity. It can, of course, be equal to g if
sin θ = 1. But this would mean that θ would have to be 90◦(since sin 90◦= 1),
in which case the ramp would be exactly vertical. In such cases, you no longer
have an object sliding down a ramp, you have an object falling next to a wall.
There’s also good information lurking in Eq. 3.10, but you have to think a bit
to see it. According to this equation, the y-component of the box’s acceleration
is equal to the difference between the magnitude of the normal force (| ⃗Fn|) and
the y-component of the gravitational force (mg cos θ). But since you know that
in this problem the box remains on the ramp and the y-acceleration is therefore
zero, you can use Eq. 3.10 to determine the magnitude of the normal force.
Since
ay = (| ⃗Fn| −mg cos θ)/m = 0,
then
| ⃗Fn| = mg cos θ.
(3.11)
So the normal force depends on the weight of the object (mg) and the cosine
of the ramp angle (θ). Understanding this will help you avoid a common pit-
fall for students who know that the normal force is the reaction force produced
on the object by the ramp, and who then mistakenly conclude that the normal
force must always equal the weight of the object (mg). That line of reason-
ing only works for horizontal surfaces, because for any inclined surface, it’s
only the component of the object’s weight that’s perpendicular to the surface
that produces the reaction force we call the normal force. That perpendicu-
lar component of the object’s weight is shown in Figure 3.5 to be mg cos θ,
which spans the range from mg (when θ = 0◦, meaning the ramp is horizontal
and bears the full weight of the object) to zero (when θ = 90◦, meaning the
ramp is vertical and bears none of the object’s weight). In all other cases, the
magnitude of the normal force will have a value between 0 and mg.
If you’re wondering why you should bother ﬁnding ⃗Fn if you’re only inter-
ested in the x-component of the acceleration, the answer is that you may not
5 But doesn’t the Earth pull harder on a more-massive object? Yes it does, but a more-massive
object also resists acceleration more than a less-massive object. Since gravitational mass
(which determines how strongly gravity pulls on an object) has the same value as inertial mass
(which determines how strongly the object resists acceleration), the result is that all objects fall
freely (or slide freely down frictionless ramps) with an acceleration that does not depend on
their mass.

## Page 81

3.1 Mass on an inclined plane
69
care about ⃗Fn for the frictionless case (unless you’re worried about your ramp
breaking), but you’ll deﬁnitely need ⃗Fn when friction exists between the ramp
surface and the bottom of the box.
With the magnitude of the down-ramp component of the acceleration (ax)
available from Eq. 3.9, all that remains is for you to ﬁnd the speed of the
box at the bottom of the ramp. Finding speed from acceleration turns out to
be quite straightforward, especially when the acceleration is constant (as it is
in this case), provided that you’re in possession of either one of two pieces
of information: the time the box takes to reach the bottom of the ramp, or
(more likely), the distance from the box’s starting point to the bottom of the
ramp. You’ll also need the initial speed, which you can generally discern from
the initial conditions, and which you can take to be zero in this case. As you
may remember from kinematics, the ﬁnal speed of an object moving in the
x-direction with initial speed vx,initial undergoing constant accleration ax over
time t is given by
vx, f inal = vx,initial + axt,
(3.12)
or, if you know d, the distance in the positive x-direction over which the
acceleration occurs,
(vx, f inal)2 = (vx,initial)2 + 2axd.
(3.13)
Using the expression for acceleration from Eq. 3.9, this becomes
(vx, f inal)2 = (0)2 + 2 (g sin θ) d
or
vx, f inal =
	
2 (g sin θ) d.
(3.14)
So, for example, a box sliding down a 2 m ramp with an angle of 30◦to the
horizontal on the surface of the Earth will be moving at a speed of
vx, f inal =

2

(9.8m/s2) sin 30◦
2m = 4.4m/s
(3.15)
when it reaches the bottom of the ramp. If you’re curious about how long it
takes the box to travel the 2 m down the ramp under these conditions, you can
plug this value for the ﬁnal speed into Eq. 3.12 and solve for t, which turns out
to be about 0.9 s in this case.
Stripping away effects such as friction is often a good way to learn the fun-
damentals of a problem, but if you’ve ever encountered a ramp outside of
physics texts, there’s a good chance you had to deal with friction. Happily,
once you understand how to use vectors, including friction in the “box on a

## Page 82

70
Vector applications
ramp” problem becomes a simple matter of adding another force into the mix
before solving for the acceleration.
As you may recall, friction operates in two regimes: “static” friction deter-
mines how hard you have to push on a stationary object to get it moving, but
once the object is moving, the frictional force that opposes the motion is pro-
duced by “kinetic” friction. So although both types of friction oppose motion,
the magnitude of the force produced by static friction depends on the applied
force (the harder you push, the stronger the opposing force of static friction,
until the object “breaks free” and begins moving), while the magnitude of the
kinetic-friction force depends only on the normal force and the coefﬁcient of
kinetic friction between the object and the surface.6 To determine the effect
of kinetic friction on the speed of the box at the bottom of the ramp, you can
modify your free-body diagram to include the frictional force ( ⃗F f ), as shown
in Figure 3.6.
Notice that the direction of the frictional force is chosen so as to oppose the
motion, and since the box is moving down the ramp in this case, the force of
kinetic friction points up the ramp (in the negative x-direction).
To determine the effect of friction on the acceleration of the box sliding
down the ramp, you simply have to include the frictional force ( ⃗F f ) in your
equation for the sum of the forces in the x-direction (Eq. 3.3), which becomes
| ⃗Fx| = | ⃗Fg|sinθ −| ⃗F f |.
(3.16)
This makes the acceleration
ax = Fx/m =

| ⃗Fg|sinθ −| ⃗F f |

/m.
(3.17)
Clearly, to determine the magnitude of the acceleration (ax), you’ll need to
ﬁnd an expression for | ⃗F f |, just as you used mg sin θ for |Fg,x| in Eq. 3.9.
y
x
Fn
Ff
Fg
Figure 3.6 Free-body diagram for object on ramp with friction.
6 You can read more about this in introductory physics texts such as Serway & Jewett or
Halliday, Resnick, & Walker.

## Page 83

3.1 Mass on an inclined plane
71
Fortunately, that’s easy to do, because the magnitude of the force of kinetic
friction is simply the product of the magnitude of the normal force (| ⃗Fn|) and
the coefﬁcient of kinetic friction (μk):
| ⃗F f | = μk| ⃗Fn|.
(3.18)
You also know from Eq. 3.11 that | ⃗Fn| = mg cos θ, so
ax = (mg sin θ −μk mg cos θ) /m
= (g sin θ −μk g cos θ) .
(3.19)
Comparing this expression for the acceleration of the box to the acceleration
in the frictionless case (Eq. 3.9), you’ll be happy to note that the term due to
gravity (g sin θ) is exactly the same in both cases, and the term due to friction
(μk g cos θ) is subtracted from the gravity term. This means that the acceler-
ation of the box will be made smaller by the frictional force. So in the case
considered previously of a box sliding down a 2 m ramp that makes an angle
of 30◦with the horizontal, if the coefﬁcient of kinetic friction between the box
and the ramp is 0.4, the speed of the box at the bottom of the ramp will be
reduced to
vx, f inal =

2

(9.8m/s2) sin 30◦−(0.4)(9.8m/s2) cos 30◦
2m
= 2.5m/s.
(3.20)
There is one aspect of Eq. 3.19 that may worry you: what if the second term
is larger than the ﬁrst? For any angle between 0◦and 45◦, the cosine is bigger
than the sine, so if the coefﬁcient of kinetic friction (μk) is sufﬁciently large,
this equation predicts that the acceleration will be in the negative x-direction,
meaning the box will acclerate up the ramp even if no one is pushing on it.
As physicists like to say, “That’s not physical,” meaning that this result contra-
dicts other well-established laws of physics (conservation of energy comes to
mind in this case). So where have we gone wrong in our analysis? We haven’t,
really, you just need to think carefully about the initial assumptions. One of
those assumptions was that the box is travelling down the ramp, which is why
we drew the frictional force pointing up the ramp in our free-body diagram
(Figure 3.6). But if the ramp isn’t very steep and the coefﬁcient of friction
between the box and the ramp is sufﬁciently large, the down-ramp component
of the force of gravity will not be strong enough to overcome the frictional
force, and the box will not slide down the ramp.7 So there’s nothing wrong
7 You can determine whether the box will move by comparing the maximum static frictional
force (which is just the product of the coefﬁcient of static friction and the normal force) to the
sum of the x-components of all the other forces.

## Page 84

72
Vector applications
with Eq. 3.19, it’s just that it only applies to the situation in which the box is
moving down the ramp under the inﬂuence of gravity, in which case the force
of kinetic friction points up the ramp.
So there you have it. You’ve used vectors to represent the forces of gravity
and friction, and knowing how to ﬁnd vector components and how to perform
vector addition has allowed you to ﬁnd the acceleration and speed of the box
under various conditions. And if a box sliding straight down a ramp is a bit too
mundane for your taste, you may want to take a look at the next three appli-
cation examples. In them, you’ll see how vectors can be helpful in analyzing
motion on a curved path and how vector operations can be used to understand
the behavior of electric and magnetic ﬁelds.
3.2 Curvilinear motion
In everyday language, the word “acceleration” is used as a synonym for
“increasing speed.” Hence the “accelerator” in an automobile usually refers
to the gas pedal. But in physics and engineering, acceleration is deﬁned as any
change in velocity, and velocity is a vector quantity with both magnitude and
direction. So changing the direction of the velocity is also a form of accelera-
tion, meaning that most cars have three accelerators: the gas pedal, the brake,
and the steering wheel. “Stepping on the gas” produces an acceleration in the
same direction as the velocity vector (causing the speed to increase), press-
ing on the brake produces an acceleration directly opposite to the direction of
the velocity vector (causing the speed to decrease), and turning the steering
wheel produces an acceleration perpendicular to the velocity vector (causing
the car’s direction to change but not affecting the speed).8 Acceleration in the
direction parallel (or antiparallel) to the velocity vector is called “tangential”
and acceleration perpendicular to the velocity is called “radial.” Any time an
object experiences radial acceleration, it does not move in a straight line, and
its motion is called “curvilinear.” An example of curvilinear motion is shown
in Figure 3.7, in which a car is going around a curve.
Note that at any instant, the velocity vector points directly along the path
the car is following. For a curving path, that means the instantaneous veloc-
ity vector is tangent to the path, as you can see when the car is at position B
in Figure 3.7. If you wish to determine the acceleration at points such as A,
B, and C along the car’s path, it’s not enough to know the velocity at those
points; you have to know how the velocity is changing with time at those
locations.
8 In reality, turning the steering wheel produces frictional forces that also slow the car down, but
it’s the perpendicular component of the acceleration that causes the car to turn.

## Page 85

3.2 Curvilinear motion
73
A
B
C
Velocity
vector is tangent
to path
Figure 3.7 Velocity vectors for a car following a curved path.
A good way to visualize the acceleration vector is to graphically represent
the velocity vector at the instants of time just before and just after the car is at
positions A, B, and C. This is illustrated in Figure 3.8 for the following case:
the car is slowing down at Position A as it approaches the turn, maintaining
constant speed while turning at Position B, and then speeding up as it exits the
turn at Position C.
You can get a sense of the acceleration just by examining the change in the
velocity vectors at each position. Comparing the velocity vectors just before
and just after Position A, you can see that the magnitude (length) of the vector
is getting smaller but the direction remains the same. This means that the speed
of the car is decreasing but the car is not yet turning. Now look at the velocity
vectors just before and after Position B: the direction of the vector is changing
but its length is not, so the car is turning while maintaining constant speed.
Finally, by examining the velocity vectors before and after Position C, you can
see that the length is increasing, meaning the car is speeding up after leaving
the turn.
The direction of the acceleration is easily found by remembering that the
average acceleration is given by the equation ⃗a = 	⃗v/	t, where 	⃗v is the
change in velocity over time 	t. That change in velocity is just ⃗v f inal−⃗vinitial,
which you can determine by subtracting the earlier velocity vector from the
later one at each position in Figure 3.8. To make that easier, the vectors are
reproduced in Figure 3.9.

## Page 86

74
Vector applications
A
B
C
Figure 3.8 Change in car’s velocity vectors at Positions A, B, and C.
A
B
C
vfinal
–vinitial
vfinal
vfinal
vinitial
vinitial
vinitial
–vinitial
–vinitial
Figure 3.9 Velocity vectors before and after Positions A, B, and C.
Note that the vectors shown in Figure 3.9 include not only ⃗v f inal and ⃗vinitial,
but also the negative of ⃗vinitial. That’s because you’ll need to know −⃗vinitial
to compute the change in velocity, since 	⃗v = ⃗v f inal −⃗vinitial, which is the
same as ⃗v f inal + (−⃗vinitial). Remember that to add two vectors graphically
you simply move the tail of one to the head of the other and then draw the
resultant from the start of the ﬁrst to the end of the second vector. The results
of adding vectors ⃗v f inal and −⃗vinitial are shown in Figure 3.10.
In Figure 3.10, the velocity vectors −⃗vinitial and ⃗v f inal for Positions A and
C are shown slightly offset since they would overlay one another if they were
drawn truly head-to-tail. If you look at the direction of the vector representing
the change in velocity (	⃗v) at each position, you’ll see that while the car is

## Page 87

3.2 Curvilinear motion
75
vfinal
vfinal
vfinal
–vinitial
–vinitial
Δv = vfinal– vinitial
A
B
C
–vinitial
Δv = vfinal– vinitial
Δv = vfinal– vinitial
Figure 3.10 Change in velocity vectors at Positions A, B, and C.
slowing down at Position A, the change in velocity is in the opposite direction
from the velocity at this point. Since the acceleration (⃗a) is deﬁned as the vector
change in velocity (	⃗v) divided by the scalar time period (	t) over which that
change occurs, the direction of ⃗a must be the same as the direction of 	⃗v.
Hence the acceleration direction at Position A is opposite to the direction of
the velocity vector, as you’d expect when the car is slowing down. This is an
example of negative tangential acceleration.
Now consider the direction of the vector change in velocity 	⃗v at Position B,
where the car is going around the turn at constant speed. In this case, subtract-
ing ⃗vinitial from ⃗v f inal gives a vector 	⃗v that is perpendicular to the velocity
vector. This shows that the acceleration vector for an object moving along a
curve at constant speed points toward the center of curvature (to help you visu-
alize this direction, the 	⃗v vectors are shown on the car’s path in Figure 3.11).
At position B, this is an example of radial acceleration.9
Finally, as the car speeds up at Position C, you can see that the direction
of the vector change in velocity 	⃗v is the same as the direction of the veloc-
ity vector, meaning that the accleration in this case is parallel to the velocity.
Hence this is an example of positive tangential acceleration.
For Position B, a careful analysis of the length of the vector change in veloc-
ity reveals that the magnitude of the radial acceleration depends on the square
of the speed and on the radius of curvature of the path. Before getting into
that, it’s worth a few minutes of your time to make sure you understand the
terminology commonly used to describe acceleration and force in curvilinear
motion. Acceleration toward the center of curvature (such as the acceleration at
Position B in Figure 3.11) is called “centripetal” (for “center-seeking”) accel-
eration, and the force producing that acceleration is often called centripetal
force. It’s important for you to understand that a centripetal force is not a new
9 As described later in this section, most texts deﬁne the positive direction for radial acceleration
to be outward from the center of curvature, in which case the acceleration at Point B would be
considered negative radial acceleration.

## Page 88

76
Vector applications
A
B
C
Δv = vfinal–vinitial
Δv = vfinal–vinitial
Δv = vfinal–vinitial
vfinal
vfinal
–vinitial
–vinitial
–vinitial
vfinal
Figure 3.11 Acceleration vectors at Positions A, B, and C.
kind of force that is somehow different from mechanical, electrical, magnetic,
or other kinds of force. The word “centripetal” simply describes the direction
of the force, but the force itself is provided by the same old kinds of forces to
which you’re accustomed. So for a car going around a curve, the centripetal
force is simply the frictional force of the tires on the ground. If you tie a rock
to a rope and twirl the rope in a circle, the centripetal force on the rock is
produced by the tension of the rope. And if you ﬁll a bucket with water and
swing it over your head, the centripetal force on the bucket (and via the bucket
on the water) comes from the muscles in your arm. So the centripetal force is
whatever force is producing the centripetal acceleration that causes the object
to follow a curved path.
As footnoted earlier, it’s conventional to consider radial acceleration (⃗ar)
as positive outward (away from the center of curvature), and since centripetal
acceleration (⃗ac) is deﬁned as positive toward the center of curvature, you may
run across an equation such as ⃗ar = −⃗ac. This is simply a statement that the
radial acceleration and centripetal acceleration are commonly deﬁned to have
the same magnitude but opposite directions.
You should note that in the case of the car on the curving road, the rock being
twirled in a circle on a rope, and the bucket of water being swung over your
head, the centripetal acceleration (and hence the centripetal force) is toward the
center of curvature, and there is no acceleration (and no force) pointing radially
outward. But what about the “centrifugal” force that the occupants of the car
feel toward the outside of the curve (that is, toward the left door if the car is
turning to the right)? What they’re feeling is the force of the left door on their

## Page 89

3.2 Curvilinear motion
77
bodies as they attempt to obey Newton’s First Law and continue moving in a
straight line while the car is accelerating to the right. So centrifugal force is the
apparent force experienced by observers in the reference frame that is rotating
with the object (physicists refer to acclerating reference frames such as this
as “non-inertial”). Hence if you’re riding in a right-turning car, as you slide
across the seat and up against the left door, in your (rotating) reference frame
you’re accelerating to your left, which causes you to conclude that there’s a
force in that direction (outward from the center of curvature). But for those
of us not riding in the car, we don’t see any such force; we simply observe
the centripetal acceleration of the car as the friction of the tires on the road
provides a centripetal (rightward) force.
The concept of centripetal and centrifugal force can be understood by con-
sidering an Olympic hammer-thrower as she spins a heavy mass on the end
of cable, as illustrated from above in Figure 3.12. For the thrower, it feels
like the object is pulling directly outward (away from her). Once again, in
the non-rotating reference frame of the stadium, that’s just because the object
is attempting to obey Newton’s First Law and continue moving in a straight
line. So from our vantage point in the viewing stand, we see that the hammer-
thrower is having to produce a centripetal (radially inward) force to make the
object follow a curved path.
So is the hammer-thrower wrong in her assessment? Absolutely not. In her
reference frame, which is rotating along with the mass, her conclusion that
a radially outward (centrifugal) force exists is perfectly valid. After all, she
knows that she has to exert a very strong inward force on the cable to keep the
mass at the same distance from her (because in her reference frame the mass
Thrower
Cable
Mass
Figure 3.12 Top view of hammer-thrower.

## Page 90

78
Vector applications
has zero acceleration until she releases it). Hence she is correct in concluding
that in her reference frame there must be a force in the radially outward direc-
tion to balance her inward pull. So if you hear someone say that the centrifugal
force is “ﬁctitious,” they generally mean that centrifugal force is an apparent
force to an observer in a rotating (non-inertial) reference frame.
Once you understand the concepts of centripetal acceleration and force, it’s
reasonable to ask how strong the centripetal force must be to cause an object to
follow a given path. It’s simple to determine the centripetal force using New-
ton’s Second Law ( ⃗F = m⃗a) if you know the object’s mass and have some
way of ﬁnding the centripetal acceleration. Happily, the centripetal accelera-
tion turns out to depend only on the object’s speed and the radius of curvature
of the path, as you can see by considering Figures 3.13 and 3.14.
In Figure 3.13 you can see the velocity vectors at two locations for an object
in uniform circular motion (meaning that the object’s speed and the radius of
curvature are both constant over the time period under consideration). Note
that the two positions are separated by angle 	θ at the center of curvature,
which makes the arc length between the initial and ﬁnal positions equal to
r	θ, where r is the radius of curvature and 	θ is in radians. Since the speed
of the object is constant over this distance, you know that |⃗vinitial| must equal
|⃗v f inal| (in other words, the direction but not the length of the velocity vector
r
r
rΔθ
Δθ
vfinal
vinitial
Figure 3.13 Geometry of changing direction of velocity.
length =  vfinal  = |v|
length = |Δv|
length =  vinitial  = |v|
length = |v|Δθ
Δθ
Figure 3.14 Geometry for determining length of 	⃗v.

