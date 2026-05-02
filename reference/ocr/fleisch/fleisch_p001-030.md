<!-- source-pdf: FleischVectorsAndTensors.pdf | pages 1-30 | tool: obsidian-ai-chat tools/ocr-pdf-to-md -->
# Pages 1–30

## Page 1

_(no text on this page)_


## Page 2

_(no text on this page)_


## Page 3

A Student’s Guide to Vectors and Tensors
Vectors and tensors are among the most powerful problem-solving tools available,
with applications ranging from mechanics and electromagnetics to general relativity.
Understanding the nature and application of vectors and tensors is critically important
to students of physics and engineering.
Adopting the same approach as in his highly popular A Student’s Guide to
Maxwell’s Equations, Fleisch explains vectors and tensors in plain language. Written
for undergraduate and beginning graduate students, the book provides a thorough
grounding in vectors and vector calculus before transitioning through contra and
covariant components to tensors and their applications. Matrices and their algebra are
reviewed on the book’s supporting website, which also features interactive solutions to
every problem in the text, where students can work through a series of hints or choose
to see the entire solution at once. Audio podcasts give students the opportunity to hear
important concepts in the book explained by the author.
DA N I E L FL E I S C H is a Professor in the Department of Physics at Wittenberg
University, where he specializes in electromagnetics and space physics. He is the
author of A Student’s Guide to Maxwell’s Equations (Cambridge University Press,
2008).

## Page 4

_(no text on this page)_


## Page 5

A Student’s Guide to Vectors
and Tensors
DANIEL A. FLEISCH

## Page 6

C AMBRIDGE UNIVERSITY PRESS
Cambridge, New York, Melbourne, Madrid, Cape Town,
Singapore, S˜ao Paulo, Delhi, Tokyo, Mexico City
Cambridge University Press
The Edinburgh Building, Cambridge CB2 8RU, UK
Published in the United States of America by Cambridge University Press, New York
www.cambridge.org
Information on this title: www.cambridge.org/9780521171908
c⃝D. Fleisch 2012
This publication is in copyright. Subject to statutory exception
and to the provisions of relevant collective licensing agreements,
no reproduction of any part may take place without the written
permission of Cambridge University Press.
First published 2012
Printed in the United Kingdom at the University Press, Cambridge
A catalog record for this publication is available from the British Library
ISBN 978-0-521-19369-6 Hardback
ISBN 978-0-521-17190-8 Paperback
Additional resources for this publication at www.cambridge.org/9780521171908
Cambridge University Press has no responsibility for the persistence or
accuracy of URLs for external or third-party internet websites referred to
in this publication, and does not guarantee that any content on such
websites is, or will remain, accurate or appropriate.

## Page 7

Contents
Preface
page vii
Acknowledgments
x
1
Vectors
1
1.1
Deﬁnitions (basic)
1
1.2
Cartesian unit vectors
5
1.3
Vector components
7
1.4
Vector addition and multiplication by a scalar
11
1.5
Non-Cartesian unit vectors
14
1.6
Basis vectors
20
1.7
Chapter 1 problems
23
2
Vector operations
25
2.1
Scalar product
25
2.2
Cross product
27
2.3
Triple scalar product
30
2.4
Triple vector product
32
2.5
Partial derivatives
35
2.6
Vectors as derivatives
41
2.7
Nabla – the del operator
43
2.8
Gradient
44
2.9
Divergence
46
2.10 Curl
50
2.11 Laplacian
54
2.12 Chapter 2 problems
60
3
Vector applications
62
3.1
Mass on an inclined plane
62
3.2
Curvilinear motion
72
v

## Page 8

vi
Contents
3.3
The electric ﬁeld
81
3.4
The magnetic ﬁeld
89
3.5
Chapter 3 problems
95
4
Covariant and contravariant vector components
97
4.1
Coordinate-system transformations
97
4.2
Basis-vector transformations
105
4.3
Basis-vector vs. component transformations
109
4.4
Non-orthogonal coordinate systems
110
4.5
Dual basis vectors
113
4.6
Finding covariant and contravariant components
117
4.7
Index notation
122
4.8
Quantities that transform contravariantly
124
4.9
Quantities that transform covariantly
127
4.10 Chapter 4 problems
130
5
Higher-rank tensors
132
5.1
Deﬁnitions (advanced)
132
5.2
Covariant, contravariant, and mixed tensors
134
5.3
Tensor addition and subtraction
135
5.4
Tensor multiplication
137
5.5
Metric tensor
140
5.6
Index raising and lowering
147
5.7
Tensor derivatives and Christoffel symbols
148
5.8
Covariant differentiation
153
5.9
Vectors and one-forms
156
5.10 Chapter 5 problems
157
6
Tensor applications
159
6.1
The inertia tensor
159
6.2
The electromagnetic ﬁeld tensor
171
6.3
The Riemann curvature tensor
183
6.4
Chapter 6 problems
192
Further reading
194
Index
195

## Page 9

Preface
This book has one purpose: to help you understand vectors and tensors so that
you can use them to solve problems. If you’re like most students, you ﬁrst
encountered vectors when you took a course dealing with mechanics in high
school or college. At that level, you almost certainly learned that vectors are
mathematical representations of quantities that have both magnitude and direc-
tion, such as velocity and force. You may also have learned how to add vectors
graphically and by using their components in the x-, y- and z-directions.
That’s a ﬁne place to start, but it turns out that such treatments only scratch
the surface of the power of vectors. You can harness that power and make it
work for you if you’re willing to delve a bit deeper – to see vectors not just
as objects with magnitude and direction, but rather as objects that behave in
very predictable ways when viewed from different reference frames. That’s
because vectors are a subset of a larger class of objects called “tensors,” which
most students encounter much later in their academic careers, and which have
been called “the facts of the Universe.” It is no exaggeration to say that our
understanding of the fundamental structure of the universe was changed for-
ever when Albert Einstein succeeded in expressing his theory of gravity in
terms of tensors.
I believe, and I hope you’ll agree, that tensors are far easier to understand
if you ﬁrst establish a stronger foundation in vectors, one that can help you
cross the bridge between the “magnitude and direction” level and the “facts of
the Universe” level. That’s why the ﬁrst three chapters of this book deal with
vectors, the fourth chapter discusses coordinate transformations, and the last
two chapters discuss higher-order tensors and some of their applications.
One reason you may ﬁnd this book helpful is that if you spend a few hours
looking through the published literature and on-line resources for vectors and
tensors in physics and engineering, you’re likely to come across statements
such as these:
vii

## Page 10

viii
Preface
“A vector is a mathematical representation of a physical entity characterized
by magnitude and direction.”
“A vector is an ordered sequence of values.”
“A vector is a mathematical object that transforms between coordinate
systems in certain ways.”
“A vector is a tensor of rank one.”
“A vector is an operator that turns a one-form into a scalar.”
You should understand that every one of these deﬁnitions is correct, but
whether it’s useful to you depends on the problem you’re trying to solve.
And being able to see the relationship between statements like these should
prove very helpful when you begin an in-depth study of subjects that use
advanced vector and tensor concepts. Those subjects include Mechanics,
Electromagnetism, General Relativity, and others.
As with most projects, a good ﬁrst step is to make sure you understand the
terminology that will be used to attack the problem. For that reason, Chapter 1
provides the basic deﬁnitions you’ll need to begin understanding vectors and
tensors. And if you’re ready for more-advanced deﬁnitions, you can ﬁnd those
at the beginning of Chapter 5.
You may be wondering how this book differs from other texts that deal with
vectors and/or tensors. Perhaps the most important difference is that approx-
imately equal weight is given to vector and tensor concepts, with one entire
chapter (Chapter 3) devoted to selected vector applications and another chapter
(Chapter 6) dedicated to example tensor applications.
You’ll also ﬁnd the presentation to be very different from that of other books.
The explanations in this book are written in an informal style in which math-
ematical rigor is maintained only insofar as it doesn’t obscure the underlying
physics. If you feel you already have a good understanding of vectors and
may need only a quick review, you should be able to skim through Chapters 1
through 3 very quickly. But if you’re a bit unclear on some aspects of vectors
and how to apply them to problems, you may ﬁnd these early chapters quite
helpful. And if you’ve already seen tensors but are unsure of exactly what they
are or how to apply them, then Chapters 4 through 6 may provide some insight.
As a student’s guide, this book comes with two additional resources
designed to help you understand and apply vectors and tensors: an interactive
website and a series of audio podcasts. On the website, you’ll ﬁnd the com-
plete solution to every problem presented in the text in interactive format –
that means you’ll be able to view the entire solution at once, or ask for a series
of helpful hints that will guide you to the ﬁnal answer. So when you see a state-
ment in the text saying that you can learn more about something by looking
at the end-of-chapter problems, remember that the full solution to every one

## Page 11

Preface
ix
of those problems is available to you. And if you’re the kind of learner who
beneﬁts from hearing spoken words rather than just reading text, the audio
podcasts are for you. These MP3 ﬁles walk you through each chapter of the
book, pointing out important details and providing further explanations of key
concepts.
Is this book right for you? It is if you’re a science or engineering student
and have encountered vectors or tensors in one of your classes, but you’re
not conﬁdent in your ability to apply them. In that case, you should read the
book, listen to the accompanying podcasts, and work through the examples
and problems before taking additional classes or a standardized exam in which
vectors or tensors may appear. Or perhaps you’re a graduate student struggling
to make the transition from undergraduate courses and textbooks to the more-
advanced material you’re seeing in graduate school – this book may help you
make that step.
And if you’re neither an undergraduate nor a graduate student, but a curi-
ous young person or a lifelong learner who wants to know more about vectors,
tensors, or their applications in Mechanics, Electromagnetics, and General Rel-
ativity, welcome aboard. I commend your initiative, and I hope this book helps
you in your journey.

## Page 12

Acknowledgments
It was a suggestion by Dr. John Fowler of Cambridge University Press that got
this book out of the starting gate, and it was his patient guidance and unﬂag-
ging support that pushed it across the ﬁnish line. I feel very privileged to have
worked with John on this project and on my Student’s Guide to Maxwell’s
Equations, and I acknowledge his many contributions to these books. A project
like this really does take a village, and many others should be recognized for
their efforts. While pursuing her doctorate in Physics at Notre Dame Univer-
sity, Laura Kinnaman took time to carefully read the entire manuscript and
made major contributions to the discussion of the Inertia tensor in Chapter 6.
Wittenberg graduate Joe Fritchman also read the manuscript and made helpful
suggestions, as did Carnegie-Mellon undergraduate Wyatt Bridgeman. Carrie
Miller provided the perspective of a Chemistry student, and her husband Jor-
dan Miller generously shared his LaTeX expertise. Professor Adam Parker of
Wittenberg University and Daniel Ross of the University of Wisconsin did their
best to steer me onto a mathematically solid foundation, and Professor Mark
Semon of Bates College has gone far beyond the role of reviewer and deserves
credit for rooting out numerous errors and for providing several of the better
explanations in this work. I alone bear the responsibility for any remaining
inconsistencies or errors.
I also wish to acknowledge all the students who have taken a class from
me during the two years it took me to write this book. I very much appreciate
their willingness to share their claim on my time with this project. The greatest
sacriﬁce has been made by the unfathomably understanding Jill Gianola, who
gracefully accommodated the expanding time and space requirements of my
writing.
x

## Page 13

1
Vectors
1.1 Deﬁnitions (basic)
There are many ways to deﬁne a vector. For starters, here’s the most basic:
A vector is the mathematical representation of a physical entity that may be
characterized by size (or “magnitude”) and direction.
In keeping with this deﬁnition, speed (how fast an object is going) is not rep-
resented by a vector, but velocity (how fast and in which direction an object is
going) does qualify as a vector quantity. Another example of a vector quantity
is force, which describes how strongly and in what direction something is being
pushed or pulled. But temperature, which has magnitude but no direction, is not
a vector quantity.
The word “vector” comes from the Latin vehere meaning “to carry;” it was
ﬁrst used by eighteenth-century astronomers investigating the mechanism by
which a planet is “carried” around the Sun.1 In text, the vector nature of an
object is often indicated by placing a small arrow over the variable representing
the object (such as ⃗F), or by using a bold font (such as F), or by underlining
(such as F or F∼). When you begin hand-writing equations involving vectors,
it’s very important that you get into the habit of denoting vectors using one of
these techniques (or another one of your choosing). The important thing is not
how you denote vectors, it’s that you don’t simply write them the same way
you write non-vector quantities.
A vector is most commonly depicted graphically as a directed line seg-
ment or an arrow, as shown in Figure 1.1(a). And as you’ll see later in this
section, a vector may also be represented by an ordered set of N numbers,
1 The Oxford English Dictionary. 2nd ed. 1989.
1

## Page 14

2
Vectors
(b)
(a)
Figure 1.1 Graphical depiction of a vector (a) and a vector ﬁeld (b).
where N is the number of dimensions in the space in which the vector
resides.
Of course, the true value of a vector comes from knowing what it represents.
The vector in Figure 1.1(a), for example, may represent the velocity of the wind
at some location, the acceleration of a rocket, the force on a football, or any of
the thousands of vector quantities that you encounter in the world every day.
Whatever else you may learn about vectors, you can be sure that every one of
them has two things: size and direction. The magnitude of a vector is usually
indicated by the length of the arrow, and it tells you the amount of the quantity
represented by the vector. The scale is up to you (or whoever’s drawing the
vector), but once the scale has been established, all other vectors should be
drawn to the same scale. Once you know that scale, you can determine the
magnitude of any vector just by ﬁnding its length. The direction of the vector
is usually given by indicating the angle between the arrow and one or more
speciﬁed directions (usually the “coordinate axes”), and it tells you which way
the vector is pointing.
So if vectors are characterized by their magnitude and direction, does that
mean that two equally long vectors pointing in the same direction could in fact
be considered to be the same vector? In other words, if you were to move the
vector shown in Figure 1.1(a) to a different location without varying its length
or its pointing direction, would it still be the same vector? In some applications,
the answer is “yes,” and those vectors are called free vectors. You can move
a free vector anywhere you’d like as long as you don’t change its length or
direction, and it remains the same vector. But in many physics and engineering
problems, you’ll be dealing with vectors that apply at a given location; such
vectors are called “bound” or “anchored” vectors, and you’re not allowed to

## Page 15

1.1 Deﬁnitions (basic)
3
relocate bound vectors as you can free vectors.2 You may see the term “sliding”
vectors used for vectors that are free to move along their length but are not free
to change length or direction; such vectors are useful for problems involving
torque and angular motion.
You can understand the usefulness of bound vectors if you think about an
application such as representing the velocity of the wind at various points in
the atmosphere. To do that, you could choose to draw a bound vector at each
point of interest, and each of those vectors would show the speed and direction
of the wind at that location (most people draw the vector with its tail – the end
without the arrow – at the point to which the vector is bound). A collection of
such vectors is called a vector ﬁeld; an example is shown in Figure 1.1(b).
If you think about the ways in which you might represent a bound vector,
you may realize that the vector can be deﬁned simply by specifying the start
and end points of the arrow. So in a three-dimensional Cartesian coordinate
system, you only need to know the values of x, y, and z for each end of the
vector, as shown in Figure 1.2(a) (you can read about vector representation in
non-Cartesian coordinate systems later in this chapter).
Now consider the special case in which the vector is anchored to the origin
of the coordinate system (that is, the end without the arrowhead is at the point
of intersection of the coordinate axes, as shown in Figure 1.2(b).3 Such vectors
may be completely speciﬁed simply by listing the three numbers that represent
the x-, y-, and z-coordinates of the vector’s end point. Hence a vector anchored
to the origin and stretching ﬁve units along the x-axis may be represented as
(a)
(b)
(0, 0, 0)
x
y
z
(xend – xstart,
yend – ystart,
zend – zstart)
(xend, yend, zend)
(xstart, ystart, zstart)
x
y
z
Figure 1.2 A vector in 3-D Cartesian coordinates.
2 Mathematicians don’t have much use for bound vectors, since the mathematical deﬁnition of a
vector deals with how it transforms rather than where it’s located.
3 The vector shown in Figure 1.2 (a) can be shifted to this location by subtracting xstart, ystart,
and zstart from the values at each end.

## Page 16

4
Vectors
(5,0,0). In this representation, the values that represent the vector are called the
“components” of the vector, and the number of components it takes to deﬁne
a vector is equal to the number of dimensions in the space in which the vector
exists. So in a two-dimensional space a vector may be represented by a pair
of numbers, and in four-dimensional spacetime vectors may appear as lists of
four numbers. This explains why a horizontal list of numbers is called a “row
vector” and a vertical list of numbers is called a “column vector” in computer
science. The number of values in such vectors tells you how many dimensions
there are in the space in which the vector resides.
To understand how vectors are different from other entities, it may help to
consider the nature of some things that are clearly not vectors. Think about the
temperature in the room in which you’re sitting – at each point in the room,
the temperature has a value, which you can represent by a single number. That
value may well be different from the value at other locations, but at any given
point the temperature can be represented by a single number, the magnitude.
Such magnitude-only quantities have been called “scalars” ever since W.R.
Hamilton referred to them as “all values contained on the one scale of progres-
sion of numbers from negative to positive inﬁnity.”4 Thus
A scalar is the mathematical representation of a physical entity that may be
characterized by magnitude only.
Other examples of scalar quantities include mass, charge, energy, and speed
(deﬁned as the magnitude of the velocity vector). It is worth noting that the
change in temperature over a region of space does have both magnitude and
direction and may therefore be represented by a vector, so it’s possible to pro-
duce vectors from groups of scalars. You can read about just such a vector
(called the “gradient” of a scalar ﬁeld) in Chapter 2.
Since scalars can be represented by magnitude only (single numbers)
and vectors by magnitude and direction (three numbers in three-dimensional
space), you might suspect that there are other entities involving magnitude and
directions that are more complex than vectors (that is, requiring more numbers
than the number of spatial dimensions). Indeed there are, and such entities are
called “tensors.”5 You can read about tensors in the last three chapters of this
book, but for now this simple deﬁnition will sufﬁce:
4 W.R. Hamilton, Phil. Mag. XXIX, 26.
5 As you can learn in the later portions of this book, scalars and vectors also belong to the class
of objects called tensors but have lower rank, so in this section the word “tensors” refers to
higher-rank tensors.

## Page 17

1.2 Cartesian unit vectors
5
A tensor is the mathematical representation of a physical entity that may be
characterized by magnitude and multiple directions.
An example of a tensor is the inertia that relates the angular velocity of a
rotating object to its angular momentum. Since the angular velocity vector
has a direction and the angular momentum vector has a (potentially different)
direction, the inertia tensor involves multiple directions.
And just as a scalar may be represented by a single number and a vector may
be represented by a sequence of three numbers in 3-dimensional space, a tensor
may be represented by an array of 3R numbers in 3-dimensional space. In this
expression, “R” represents the rank of the tensor. So in 3-dimensional space, a
second-rank tensor is represented by 32 = 9 numbers. In N-dimensional space,
scalars still require only one number, vectors require N numbers, and tensors
require NR numbers.
Recognizing scalars, vectors, and tensors is easy once you realize that a
scalar can be represented by a single number, a vector by an ordered set of
numbers, and a tensor by an array of numbers. So in three-dimensional space,
they look like this:
Scalar
Vector
Tensor (Rank 2)
(x)
(x1, x2, x3)
or
⎛
⎝
x1
x2
x3
⎞
⎠
⎛
⎝
x11
x12
x13
x21
x22
x23
x31
x32
x33
⎞
⎠
Note that scalars require no subscripts, vectors require a single subscript,
and tensors require two or more subscripts – the tensor shown here is a tensor
of rank 2, but you may also encounter higher-rank tensors, as discussed in
Chapter 5. A tensor of rank 3 may be represented by a three-dimensional array
of values.
With these basic deﬁnitions in hand, you’re ready to begin considering the
ways in which vectors can be put to use. Among the most useful of all vectors
are the Cartesian unit vectors, which you can read about in the next section.
1.2 Cartesian unit vectors
If you hope to use vectors to solve problems, it’s essential that you learn how to
handle situations involving more than one vector. The ﬁrst step in that process
is to understand the meaning of special vectors called “unit vectors” that often

## Page 18

6
Vectors
1
2
y
1
2
z
1
2
x
i
j
k
Figure 1.3 Unit vectors in 3-D Cartesian coordinates.
serve as markers for various directions of interest (unit vectors may also be
called “versors”).
The ﬁrst unit vectors you’re likely to encounter are the unit vectors ˆx, ˆy, ˆz
(also called ˆı, ˆj, ˆk) that point in the direction of the x-, y-, and z-axes of the
three-dimensional Cartesian coordinate system, as shown in Figure 1.3. These
vectors are called unit vectors because their length (or magnitude) is always
exactly equal to unity, which is another name for “one.” One what? One of
whatever units you’re using for that axis.
You should note that the Cartesian unit vectors ˆı, ˆj, ˆk can be drawn at any
location, not just at the origin of the coordinate system. This is illustrated in
Figure 1.4. As long as you draw a vector of unit length pointing in the same
direction as the direction of the (increasing) x-axis, you’ve drawn the ˆı unit
vector. So the Cartesian unit vectors show you the directions of the x, y, and z
axes, not the location of the origin.
As you’ll see in Chapter 2, unit vectors can be extremely helpful when doing
certain operations such as specifying the portion of a given vector pointing in
a certain direction. That’s because unit vectors don’t have their own magnitude
to throw into the mix (actually, they do have their own magnitude, but it is
always one).
So when you see an expression such as “5ˆı,” you should think “5 units along
the positive x-direction.” Likewise, −3 ˆj refers to 3 units along the negative
y-direction, and ˆk indicates one unit along the positive z-direction.
Of course, there are other coordinate systems in addition to the three perpen-
dicular axes of the Cartesian system, and unit vectors exist in those coordinate

## Page 19

1.3 Vector components
7
x
y
z
i
j
k
Figure 1.4 Cartesian unit vectors at an arbitrary point.
systems as well; you can see some examples in Section 1.5. One advantage
of the Cartesian unit vectors is that they point in the same direction no matter
where you go; the x-, y-, and z-axes run in straight lines all the way out to
inﬁnity, and the Cartesian unit vectors are parallel to the directions of those
lines everywhere.
To put unit vectors such as ˆı, ˆj, ˆk to work, you need to understand the
concept of vector components. The next section shows you how to represent
vectors using unit vectors and vector components.
1.3 Vector components
The unit vectors described in the previous section are especially useful when
they become part of the “components” of a vector. And what are the compo-
nents of a vector? Simply stated, they are the pieces that can be used to make
up the vector.
To understand vector components, think about the vector ⃗A shown in
Figure 1.5. This is a bound vector, anchored at the origin and extending to
the point (x = 0, y = 3, z = 3) in a three-dimensional Cartesian coordinate
system. So if you consider the coordinate axes as representing the corner of a
room, this vector is embedded in the back wall (the yz plane).
Imagine you’re trying to get from the beginning of vector ⃗A to the end – the
direct route would be simply to move in the direction of the vector. But if you
were constrained to move only in the directions of the axes, you could get from

## Page 20

8
Vectors
(a)
(b)
A
x
y
z
(0, 3, 3)
A
x
y
z
(0, 3, 3)
z-component (Az k)
y-component (Ayj)
Figure 1.5 Vector ⃗A and its components.
the origin to your destination by taking three (unit) steps along the y-axis, then
turning 90◦to your left, and then taking three more (unit) steps in the direction
of the z-axis.
What does this little journey have to do with the components of a vector?
Simply this: the lengths of the components of vector ⃗A are the distances you
traveled in the directions of the axes. Speciﬁcally, in this case the magnitude of
the y-component of vector ⃗A (written as Ay) is just the distance you traveled
in the direction of the y-axis (3 units), and the magnitude of the z-component
of vector ⃗A (written as Az) is the distance you traveled in the direction of the
z-axis (also 3 units). Since you didn’t move at all in the direction of the x-axis,
the magnitude of the x-component of vector ⃗A (written as Ax) is zero.
A very handy and compact way of writing a vector as a combination of
vector components is this:
⃗A = Axˆı + Ay ˆj + Az ˆk,
(1.1)
where the magnitudes of the vector components (Ax, Ay, and Az) tell you how
many unit steps to take in each direction (ˆı, ˆj, and ˆk) to get from the beginning
to the end of vector ⃗A.6
When you read about vectors and vector components, you’re likely to run
across statements such as “The components of a vector are the projections of
the vector onto the coordinate axes.” As you can see in Chapter 4, exactly
how those projections are made can have a signiﬁcant inﬂuence on the nature
of the components you get. But in Cartesian coordinate systems (and other
6 Some authors refer to the magnitudes Ax, Ay, and Az as the “components of ⃗A,” while others
consider the components to be Ax ˆı, Ay ˆj, and Az ˆk. Just remember that Ax, Ay, and Az are
scalars, but Ax ˆı, Ay ˆj, and Az ˆk are vectors.

## Page 21

1.3 Vector components
9
Light rays
perpendicular
to x-axis
Shadow cast
by vector A 
on y-axis
Light rays
perpendicular
to y-axis
(b)
(a)
Shadow cast
by vector A
on x-axis
x
θ
y
x
y
A
A
Figure 1.6 Vector components as projections onto x- and y-axes.
“orthogonal” systems in which the axes are perpendicular to one another), the
concept of projection onto the coordinate axes is unambiguous and may be
very helpful in picturing the components of a vector.
To understand how this works, take a look at vector ⃗A and the light sources
and shadows in Figure 1.6. As you can see in Figure 1.6(a), the direction of the
light that produces the shadow on the x-axis is parallel to the y-axis (actually
antiparallel since it’s moving in the negative y-direction), which in this case is
the same as saying that the direction of the light is perpendicular to the x-axis.
Likewise, in Figure 1.6(b), the direction of the light that produces the
shadow on the y-axis is antiparallel to the x-axis, which is of course perpendic-
ular to the y-axis. This may seem like a trivial point, but when you encounter
non-orthogonal coordinate systems, you’ll ﬁnd that the direction parallel to
one axis is not necessarily perpendicular to another axis, which gives rise to
an entirely different type of vector component. This simple fact has profound
implications for the behavior of vectors and tensors for observers in different
reference frames, as you’ll see in Chapters 4, 5, and 6.
No such issues arise in the two-dimensional Cartesian coordinate system
shown in Figure 1.6, and in this case the magnitudes of the components of
vector ⃗A are easy to determine. If the angle between vector ⃗A and the positive
x-axis is θ, as shown in Figure 1.6a, it’s clear that the length of ⃗A can be seen

## Page 22

10
Vectors
as the hypotenuse of a right triangle. The sides of that triangle along the x- and
y-axes are the components Ax and Ay. Hence by simple trigonometry you can
write:
Ax = | ⃗A| cos(θ),
Ay = | ⃗A| sin(θ),
(1.2)
where the vertical bars on each side of ⃗A signify the magnitude (length)
of vector ⃗A. Notice that so long as you measure the angle θ from the
positive x-axis in the direction toward the positive y-axis (that is, counter-
clockwise in this case), these equations will give the correct sign for the x- and
y-components no matter which quadrant the vector occupies.
For example, if vector ⃗A is a vector with a length of 7 meters pointing in a
direction 210◦counter-clockwise from the +x-axis, the x- and y-components
are given by Eq. 1.2 as
Ax = | ⃗A| cos(θ) = 7m cos 210◦= −6.1 m,
Ay = | ⃗A| sin(θ) = 7m sin 210◦= −3.5 m.
(1.3)
As expected for a vector pointing down and to the left from the origin, both
components are negative.
It’s equally straightforward to ﬁnd the length and direction of a vector if
you’re given the vector’s Cartesian components. Since the vector forms the
hypotenuse of a right triangle with sides Ax and Ay, the Pythagorean theorem
tells you that the length of ⃗A must be
| ⃗A| =

A2x + A2y,
(1.4)
and from trigonometry
θ = arctan
 Ay
Ax

,
(1.5)
where θ is measured counter-clockwise from the positive x-axis in a right-
handed coordinate system. If you try this with the components of vector ⃗A
from Eq. 1.3 and end up with a direction of 30◦rather than 210◦, remember
that unless you have a four-quadrant arctan function on your calculator, you
must add 180◦to the angle whenever the denominator of the expression (Ax in
this case) is negative.
Once you have a working understanding of unit vectors and vector compo-
nents, you’re ready to do basic vector operations. The entirety of Chapter 2 is
devoted to such operations, but two of them are needed for the remainder of this
chapter. For that reason, you can read about vector addition and multiplication
by a scalar in the next section.

## Page 23

1.4 Vector addition and multiplication by a scalar
11
1.4 Vector addition and multiplication by a scalar
If you’ve read the previous section on vector components, you’ve already seen
two vector operations in action. Those two operations are the addition of vec-
tors and multiplication of a vector by a scalar. Both of these operations are
used in the expansion of a vector in terms of vector components as in Eq. 1.1
from Section 1.3:
⃗A = Axˆı + Ay ˆj + Az ˆk.
In each of these terms, the unit vector (ˆı, ˆj, or ˆk) is being multiplied by a
scalar (Ax, Ay, or Az), and you already know the effect of that: it produces
a new vector, in the same direction as the unit vector, but longer than unity
by the value of the component (or shorter if the magnitude of the component
is between zero and one). So multiplying a vector by any positive scalar does
not change the direction of the vector, but only scales the length of the vector.
Hence, 5 ⃗A is a vector in exactly the same direction as ⃗A, but with length ﬁve
times that of ⃗A, as shown in Figure 1.7(a). Likewise, multiplying ⃗A by (1/2)
produces a vector that points in the same direction as ⃗A but is only half as long.
So the vector component Axˆı is a vector in the ˆı direction, but with length Ax
units (since ˆı has a length of one unit).
There is a caveat that goes with the “changes length, not direction” rule
when multiplying a vector by a scalar: if the scalar is negative, then the
vector is reversed in direction in addition to being scaled in length. Thus
multiplying vector ⃗B by −2 produces the new vector −2 ⃗B, and that vector
is twice as long as ⃗B and points in the opposite direction to ⃗B, as shown in
Figure 1.7(b).
The other operation going on in Eq. 1.1 is vector addition, and you already
have an idea of what that means if you recall Figure 1.5 and the process of
getting from the beginning of vector ⃗A to the end. In that process, the quantity
5A
(½)A
(a)
(b)
–2B
B
A
Figure 1.7 Multiplication of a vector by a scalar.

## Page 24

12
Vectors
Ay ˆj represented not only the number of steps you took, but also the direction
in which you took them. Likewise, the quantity Az ˆk represented the number
of steps you took in a different direction. The fact that these two quanti-
ties include directional information means that you cannot simply add them
together algebraically; you must add them “as vectors.”
To accomplish vector addition graphically, you simply imagine moving one
vector (without changing its length or direction) so that its tail is at the head
of the other vector. The sum is then determined by making a new vector that
begins at the start of the ﬁrst vector and terminates at the end of the second
vector. You can do this graphically, as in Figure 1.5(b), where the tail of vector
Az ˆk is placed at the head of vector Ay ˆj, and the sum is the vector from the
beginning of Ay ˆj to the end of Az ˆk.
This graphical “head-to-tail” approach to vector addition works for any vec-
tors (and any number of vectors), not just two vectors that are perpendicular to
one another (as Ay ˆj and Az ˆk were). An example of this is shown in Figure 1.8.
To graphically add the two vectors ⃗A and ⃗B in Figure 1.8(a), you simply imag-
ine moving one of the two vectors so that its tail is at the position of the other
vector’s head (it doesn’t matter which vector you choose to move; the result
will be the same). This is illustrated in Figure 1.8(b), in which vector ⃗B has
been displaced so that its tail is at the head of vector ⃗A. The sum of these two
vectors (called the “resultant” vector ⃗C = ⃗A + ⃗B) is the vector that extends
from the beginning of ⃗A to the end of ⃗B.
Knowing how to add vectors graphically means you can always determine
the sum of two or more vectors simply using a ruler and a protractor; just draw
the vectors head-to-tail (being careful to maintain each vector’s length and
(a)
(b)
B (displaced)
x
y
B
A
x
y
A
C
A + B
B
Figure 1.8 Graphical addition of vectors.

## Page 25

1.4 Vector addition and multiplication by a scalar
13
angle), sketch the resultant from the beginning of the ﬁrst to the end of the last,
and then measure the length (using the ruler) and angle (using the protractor)
of the resultant. This approach can be both tedious and inaccurate, so here’s
an alternative approach that uses the components of each vector: if vector ⃗C
is the sum of two vectors ⃗A and ⃗B, then the magnitude of the x-component of
vector ⃗C (which is just Cx) is the sum of the magnitudes of the x-components
of vectors ⃗A and ⃗B (that is, Ax + Bx), and the magnitude of the y-component
of vector ⃗C (called Cy) is the sum of the magnitudes of the y-components of
vectors ⃗A and ⃗B (that is, Ay + By). Thus
Cx = Ax + Bx,
Cy = Ay + By.
(1.6)
The rationale for this is shown in Figure 1.9.
Once you have the components Cx and Cy of the resultant vector ⃗C, you can
ﬁnd the magnitude and direction of ⃗C using
| ⃗C| =

C2x + C2y
(1.7)
and
θ = arctan
Cy
Cx

(1.8)
To see how this works in practice, imagine that vector ⃗A in Figure 1.9 is given
by ⃗A = 6ˆı + ˆj and vector ⃗B is given by ⃗B = −2ˆı + 8 ˆj. To add these two
vectors algebraically, you simply use Eqs. 1.6:
(a)
(b)
C = A + B
B
x
y
x
y
Ayj
Cyj = Ayj + Byj
Byj
A
Axi
Bxi
is negative
A
B
C
Cxi = Axi + Bxi
Figure 1.9 Component addition of vectors.

## Page 26

14
Vectors
Cx = Ax + Bx = 6 + (−2) = 4,
Cy = Ay + By = 1 + 8 = 9,
so ⃗C = 4ˆı + 9 ˆj. If you wish to know the magnitude of ⃗C, you can just plug
the components into Eq. 1.7 to get
| ⃗C| =

C2x + C2y =
	
42 + 92
=
√
16 + 81 = 9.85.
And the angle that ⃗C makes with the positive x-axis is given by Eq. 1.8:
θ = arctan
Cy
Cx

= arctan
9
4

= 66.0◦.
With the basic operations of vector addition and multiplication of a vector
by a scalar in hand, you’re ready to begin thinking about the more advanced
uses of vectors. But you’re also ready to attack a variety of problems involving
vectors, and you can ﬁnd a set of such problems at the end of this chapter.7
1.5 Non-Cartesian unit vectors
The three straight, mutually perpendicular axes of the Cartesian coordinate sys-
tem are immensely useful for a variety of problems in physics and engineering.
Some problems, however, are much easier to solve in other coordinate systems,
often because the axes of those systems more closely align with the directions
over which one or more of the parameters relevant to the problem remain con-
stant or vary in a predictable manner. The unit vectors of such non-Cartesian
coordinate systems are the subject of this section, and transformations between
coordinate systems are discussed in Chapter 4.
As described earlier, it takes exactly N numbers to unambiguously represent
any location in a space of N dimensions, which means you have to specify
three numbers (such as x, y, and z) to designate a location in our Universe
of three spatial dimensions. However, on the two-dimensional surface of the
Earth (ignoring height variation for the moment) it takes only two numbers
(latitude and longitude, for example) to designate a speciﬁc point. And one of
the few beneﬁts to living on a long, inﬁnitely thin island is that you can set
7 Remember that full solutions are available on the book’s website.

## Page 27

1.5 Non-Cartesian unit vectors
15
up a rendezvous using only a single number to describe the location (“I’ll be
waiting for you at 3.75 kilometers”).
Of course, numbers deﬁne locations only after you’ve deﬁned the coordi-
nate system that you’re using. For example, do you mean 3.75 kilometers from
the east end of the island or from the west end? In every space of 1, 2, 3, or
more dimensions, you can devise an inﬁnite number of coordinate systems to
specify locations in that space. In each of those coordinate systems, at each
location there’s one direction in which one of the coordinates is increasing
the fastest, and if you lay a vector with length of one unit in that direction,
you’ve deﬁned a coordinate unit vector for that system. So in the Cartesian
coordinate system, the ˆı unit vector shows you the direction in which the
x-coordinate increases, the ˆj unit vector shows you the direction in which the
y-coordinate increases, and the ˆk unit vector shows you the direction in which
the z-coordinate increases. Other coordinate systems have their own coordinate
unit vectors, as well.
Consider the two-dimensional coordinate systems shown in Figure 1.10. In
a two-dimensional space, you know that it takes two numbers to specify any
location, and those numbers could be x and y, deﬁned along two straight axes
that intersect at a right angle. The x value tells you how far you are to the right
of the y-axis (or to the left if the x value is negative), and the y value tells
you how far you are above the x-axis (or below if the y value is negative).
But you could equally well specify any location in this two-dimensional space
by noting how far and in what direction you’ve moved from the origin. In the
standard version of these “polar” coordinates, the distance from the origin is
x
y
r
x
y
y
x
(a)
(b)
θ
θ
j
r
i
Figure 1.10 2-D rectangular (a) and polar (b) coordinates.

## Page 28

16
Vectors
called r and the direction is speciﬁed by giving the angle θ measured counter-
clockwise from the positive x-axis.
It’s easy enough to ﬁgure out one set of coordinates if you know the others;
for example, if you know the values of x and y, you can ﬁnd r and θ using
r =

x2 + y2
θ = arctan

 y
x

.
(1.9)
Likewise, if you have the values of r and θ, you can ﬁnd x and y using
x = r cos(θ)
y = r sin(θ).
(1.10)
For the point shown in Figure 1.10, if the values of x and y are 4 cm and 9 cm,
then r has a value of approximately 9.85 cm and θ has a value of 66.0◦. Clearly,
whether you write (x, y) = (4 cm, 9 cm) or (r, θ) = (9.85 cm, 66.0◦), you’re
referring to the same location; it’s not the point that’s changed, it’s only the
point’s coordinates that are different.
And if you choose to use the polar coordinate system to represent the point,
do unit vectors exist that serve the same function as ˆı and ˆj in Cartesian coor-
dinates? They certainly do, and with a little logic you can ﬁgure out which
direction they must point. After all, you know that the unit vector ˆı shows you
the direction of increasing x and the unit vector ˆj shows you the direction of
increasing y, but now you’re using r and θ instead of x and y. So it seems
reasonable that the unit vector ˆr at any location should point in the direction of
increasing r, and the unit vector ˆθ should point in the direction of increasing θ.
For the point shown in Figure 1.10, that means that ˆr should point up and to the
right, in the direction of increasing r if θ is held constant. At that same point,
ˆθ should point up and to the left, in the direction of increasing θ if r is held
constant. These polar unit vectors are shown for one point in Figure 1.10(b).
An important consequence of this deﬁnition is that the directions of ˆr and ˆθ
will be different at different locations. They’ll always be perpendicular to one
another, but they will not point in the same directions as they do for the point
in Figure 1.10. The dependence of the polar unit vectors on position can be
seen in the following relations:
ˆr = cos(θ)ˆı + sin(θ) ˆj
ˆθ = −sin(θ)ˆı + cos(θ) ˆj.
(1.11)
So if θ = 0 (which means your location is on the +x-axis), then ˆr = ˆı and
ˆθ = ˆj. But if θ = 90◦(so your location is on the +y-axis), then ˆr = ˆj and
ˆθ = −ˆı.

## Page 29

1.5 Non-Cartesian unit vectors
17
Does this dependence on position mean that these unit vectors are not “real”
vectors? That depends on your deﬁnition of a real vector. If you deﬁne a vector
as a quantity with magnitude and direction, the polar unit vectors do meet
your deﬁnition. But they do not meet the deﬁnition of free vectors described in
Section 1.1, since they may not be moved without changing their direction.
This means that if you express a vector in polar coordinates and then
take the derivative of that vector, you’ll have to account for the change in
the unit vectors, as well. That’s one of the advantages offered by Cartesian
coordinates – the unit vectors do not change no matter where you go in the
space.
As you might expect, the situation is slightly more complicated for three-
dimensional coordinate systems. Whether you choose to use Cartesian or
non-Cartesian coordinates, you’re going to need three variables to represent all
the possible locations in a three-dimensional space, and each of the coordinates
is going to come with its own unit vector. The two most common three-
dimensional non-Cartesian coordinate systems are cylindrical and spherical
coordinates, which you can see in Figures 1.11 and 1.12.
In cylindrical coordinates a point P is speciﬁed by r, φ, z, where r (some-
times called ρ) is the perpendicular distance from the z-axis, φ is the angle
measured from the x-axis to the projection of r onto the xy plane, and z is the
same as the z in Cartesian coordinates. Here’s how you ﬁnd r, φ, and z if you
know x, y, and z:
Cylinder of
constant r
P(r,φ,z)
Plane of constant z
Plane of constant φ
z
x
y
φ
r
r
z
φ
Figure 1.11 Cylindrical coordinates.

## Page 30

18
Vectors
Plane of
constant φ
Sphere of
constant r
Cone of
constant θ
θ
φ
y
x
z
P(r,θ,φ)
r
θ
φ
ρ
Figure 1.12 Spherical coordinates.
r =

x2 + y2
φ = arctan

 y
x

z = z.
(1.12)
And if you have the values of r, φ, and z, you can ﬁnd x, y, and z using
x = r cos(φ)
y = r sin(φ)
z = z.
(1.13)
A vector at the point P is speciﬁed in cylindrical coordinates in terms of
three mutually perpendicular components with unit vectors perpendicular to
the cylinder of radius r, perpendicular to the plane through the z-axis at angle
φ, and perpendicular to the xy plane at distance z. As in the Cartesian case,
each cylindrical coordinate unit vector points in the direction in which that
parameter is increasing, so ˆr points in the direction of increasing r, ˆφ points
in the direction of increasing φ, and ˆz points in the direction of increasing z.
The unit vectors (ˆr, ˆφ, ˆz) form a right-handed set, so if you point the ﬁngers
of your right hand along ˆr and push it into ˆφ with your right palm, your right
thumb will show you the direction of ˆz.

