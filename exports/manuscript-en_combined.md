# Preface: A Gift to My Former Self, or a Line of Defense in the Age of Social Media

I wrote this book to answer the questions I had as an undergraduate. It assumes, roughly, the background I had at the time.

The book also needs a few lines of defense. Once you publish something mathematical-looking on the internet, you cannot avoid them. In several places, a more advanced textbook would immediately abstract everything away. I deliberately begin instead with matrix representations and computations on finite cells.

That is not a rejection of the more advanced point of view. Quite the opposite. My aim is to give the reader concrete tools, intuition, and a feel for “rigor” that will remain useful when they eventually face the world beyond this book.

The detailed problem setting comes in the next section, “Introduction.”

Now, to the matter at hand.

Can you explain what $dx$ is?

> <strong>Note</strong> (on notes)
> This book contains many notes. Some readers may find them unkind, since they interrupt the flow of the main text.
>
> Here, however, the notes have three jobs.
>
> First, they are lines of defense for me. They leave a small record, beside the main text, of where something is being omitted, where two things are being identified, and what kind of rigorous formulation lies further ahead.
>
> Second, they help train the reader’s nose. Even if you do not understand everything yet, it helps to sense that “something is going on here” or that “this way of speaking has its limits.” That sense will help later.
>
> Third, they are meant to work a little like flashbacks in a mystery novel. At first, a note may look like a fragment. As you read on, it gradually acquires meaning, until later you realize, “Ah, so that was what this was for.” I am aiming for a little of that reading experience as well.
>
> The notes are not there so that you understand everything on the spot. Pick up the parts you can read, and feel free to pass over the parts you cannot.

> <strong>Note</strong> (historical order and understandable order)
> Modern readers can learn matrices, linear algebra, differential forms, and vector analysis as already-organized tools. At least in the education I received, matrices first appeared in high school as algebraic tools one could compute by hand. Historically, however, these tools seem to have developed in a much less linear way, influencing one another along the way. I suspect that some confusion born of that history still remains in education. This book is not an attempt to reconstruct the history of mathematical physics. It is an attempt to unwind multivariable calculus and vector analysis in a different order, using the matrix algebra that modern readers already have.

> <strong>Remark</strong> (this book contains anger)
> This is not anger at any particular person. It is anger at the fact that a problem that should have been visible was not sufficiently solved when I was a student, and has still not been sufficiently solved even now. Vector analysis implicitly contains the metric, orientation, duality, and the exterior derivative, yet it is taught as a collection of formulas while hiding them. Meanwhile, differential forms have been placed up in the heights of manifold theory, instead of being brought down as tools for beginners trying to understand vector analysis. This book is an attack on that gap, and at the same time, a proposed alternative.

# Introduction: What Is $dx$? What Is Nabla?

## Prerequisites

You should be able to read this book if you are comfortable with the following basic material.

- <strong>Calculus</strong>: You should be able to differentiate and integrate one-variable functions. It is even better if substitution in integrals does not bother you.
- <strong>Linear algebra</strong>: You should not be allergic to multiplying matrices. You should also have an image of moving back and forth between “vectors as arrows” and “vectors as lists of numbers.”

You do not need to know determinants in advance. We will discover them along the way.

When I say that a high-school student could read this book, I do not mean that it will be effortless. But I wrote it so that, at least, the twenty-year-old version of myself could have read it through.

## What Is $dx$?

Every integral sign has a $dx$ at its tail. In high-school mathematics, it is treated almost like a marker saying “integrate with respect to $x$.” We are also taught that $\frac{dy}{dx}$ is not a fraction, even though substitution in integrals effectively lets us manipulate it as if it were one.

In first-year university calculus, $dx$ appears as part of the total differential. But in many cases, we still do not go very deeply into what it actually is.

In physics and engineering courses, the situation becomes even stranger. Infinitesimals such as $dx$ and $\delta x$ are manipulated as if they were perfectly ordinary objects.

When I was a first-year master’s student, I once asked a mathematics friend what $dx$ was. I remember getting an explanation that was both understandable and not understandable: “$dx$ is a linear functional on the tangent vector space, or an element of the cotangent space.”

So what is $dx$, in the end? Unless we are already in an advanced course, must we either avoid the question or treat $dx$ as an infinitesimal?

From a more advanced mathematical point of view, my friend was overwhelmingly right. It is better if one can understand $dx$ that way. But it is hard.

So this book asks a more practical question: what would it take to lead a high-school student toward that understanding? The foothold I use is matrix algebra, which, at least in my case, had already been drilled into me in high school.

In this book, we first read $dx$ as “a measuring device that extracts the $x$-component from a displacement vector.” In matrix representation, symbolically,

$$
dx=\begin{pmatrix}1&0&0\end{pmatrix}
$$

The question is what the $dx$ at the tail of the integral sign is actually doing. This book begins by making that operation visible.

$dx$ eats a displacement and returns its $x$-component. $dx\wedge dy$ measures the oriented area spanned by two displacements. $dx\wedge dy\wedge dz$ measures the oriented volume spanned by three displacements.

Instead of immediately placing abstract terminology between the $dx$ of high-school mathematics and the $dx$ of differential forms, we first place matrices and measuring devices there. That is the starting point of this book.

## What Is Nabla?

The other symbol this book wants to confront is $\nabla$.

In English, $\nabla$ is usually called **del**; it is also called **nabla**. Japanese textbooks often use the name *nabla*. This book is not really about the name of the symbol. It is about what div, grad, and curl are actually doing.

When you study vector analysis, the whole subject may suddenly start to look like a collection of formulas. At least that was my experience. In Cartesian coordinates, things may still look manageable. But once cylindrical or spherical coordinates enter the stage, $r$ and $\sin\theta$ appear, and one has to memorize coefficients whose origin is not clear.

For example, in two dimensions, one encounters

$$
\frac{\partial F_y}{\partial x}-\frac{\partial F_x}{\partial y}
\qquad=\qquad
\frac{1}{r}\frac{\partial (r F_\theta)}{\partial r}-\frac{1}{r}\frac{\partial F_r}{\partial \theta}
$$

The left-hand side is written in Cartesian coordinates. The right-hand side is the same quantity written in polar coordinates. With a midterm tomorrow, it is not especially easy to feel convinced that this deserves to be called “curl.”

Of course, this point is explained in supplementary books on mathematical physics and in careful recent books as well. But as far as I know, books in Japanese that build this up heuristically within the structure of a textbook are still rare.

This book does not begin with nabla. Since we are going to think about the matrix representation of $dx$, we use that representation first.

From $dx$, we rethink what area is and what volume is. Then we move on to integration, changes of variables, the exterior derivative, and the Hodge star. Only after that do we return to nabla.

It will not help you in time for tomorrow’s midterm. But perhaps it will make it in time for the final.


# Portal Site and a Small Experiment

The PDF version of this book, errata, revision history, GitHub repository, and links to related notes are collected on the following portal site.

### Portal Site

[https://covectorspace.xyz/en/](https://covectorspace.xyz/en/)

### GitHub Pages (English)

[https://yokiikoy.github.io/nabla-kaitai/en/](https://yokiikoy.github.io/nabla-kaitai/en/) · [Japanese edition](https://yokiikoy.github.io/nabla-kaitai/)

This book is available for free. Obvious typo-level corrections are also accepted through GitHub Issues.

> <strong>Note</strong> (on the name)  
> Incidentally, the term *covector space*, or *Co-Vector Space*, is not especially common. In mathematics, it is more usual to say *dual space* and related terms.

### Discord Server

As a small experiment, I have opened a Discord server as a slightly more private place for unorganized ideas and elementary questions that are hard to post on public social media.

The plan is to develop it gradually. At present, it is honestly close to an “empty room.” I hope it can become a place where people interested in science and engineering can gather at a comfortable distance, whether or not the topic is directly related to this book.

If you are interested, please visit the portal site.
The invitation link is here.

[https://discord.gg/NCffyR9gj](https://discord.gg/NCffyR9gj)

# Chapter 1: What Is $dx$? — A Measuring Device That Eats Vectors, or a Row Vector

# Chapter 1: What Is $dx$? — A Measuring Device That Eats Vectors, or a Row Vector

### §1.0 The Mathematician’s One Dimension, the Physicist’s One Dimension

When we first learn the one-dimensional integral $\int f(x)\,dx$ in high school, the textbook places before us a single line: the $x$-axis. For a mathematics textbook, that is perfectly reasonable. A <strong>mathematician</strong> assumes a self-contained abstract world called one-dimensional space $\mathbb{R}^1$, and builds the logic there. A point is a real number $x$, a displacement is a real number $\Delta x$, and an integral is defined as the limit of “function times tiny width.” Everything is self-contained.

<strong>But here, we are physicists.</strong>

> <strong>Note</strong> (I am not a physicist)  
> Of course, this is rhetoric. My degree is not in physics but in chemistry, and I am not currently in academia.
>
> What I mean is that the viewpoint of this book may be useful not only to readers in physics, but also to readers in information science, mechanical engineering, electrical engineering, other areas of science and engineering, or simply anyone who has gotten lost in the notation of vector analysis or calculus.
>
> “Physicist” here is not an institutional affiliation. It means a way of looking at things mathematically, as one often does in physical mathematics. I do not mean to put down mathematicians or mathematics books.
>
> I still wrote it a little grandly because I simply wanted to say it.

The <strong>actual physical space</strong> we deal with is always three-dimensional. Even when a point mass appears to move along a straight line, it is not living in some “fictional one-dimensional space.” Rather, we are looking at a slice of three-dimensional space $\mathbb{R}^3$ in which displacement in the $y$ and $z$ directions happens not to be observed, or can be neglected.

For example, consider a cart sliding on a frictionless straight rail. We say, “This is one-dimensional motion in the $x$ direction,” but in reality:

* the rail is installed in three-dimensional space;
* the cart may be vibrating slightly up and down;
* there may also be tiny lateral fluctuations due to air resistance.

What a physicist calls “one-dimensional motion” is a situation in which, <strong>in three-dimensional space, displacement in one particular direction dominates, while displacement in the other directions is either negligibly small or constrained to be exactly zero by the symmetry of the system.</strong>

> <strong>Note</strong> (the embedding point of view)  
> The “physicist’s one dimension” here means viewing a one-dimensional parameter space as being mapped into three-dimensional space as a curve. In mathematics, such a map is first treated as a <strong>parametrization</strong> of a curve; under good conditions, such as no self-intersection and nonzero velocity, it is called an <strong>embedding</strong>.
>
> This book is not denying abstract one-dimensional spaces themselves. Rather, here we first understand the “motion along a curve in space” that often appears in physical mathematics as a mapping into three-dimensional space.

Therefore, what a physicist calls a “one-dimensional infinitesimal displacement” is not really just a scalar $\Delta x$. It is more appropriately represented as the following <strong>column vector</strong>:

$$
\mathbf{v} :=
\begin{pmatrix}
\Delta x \\
0 \\
0
\end{pmatrix}
$$

We call a three-component expression of displacement from a point in three-dimensional space a <strong>displacement vector</strong>. Following the usual convention, the <strong>first component</strong> corresponds to displacement in the $x$-axis direction, the <strong>second component</strong> to displacement in the $y$-axis direction, and the <strong>third component</strong> to displacement in the $z$-axis direction.

The zeros in the second and third components should not be read as saying that those components are merely “being ignored” or “do not exist.” They are the result of a positive choice: <strong>we are currently focusing only on motion in the $x$-axis direction and intentionally excluding the other components from what we measure.</strong>

This physicist’s three-dimensional point of view lets us see that $dx$ is not a mere extra symbol hanging off the end of an integral sign. In the next section, from this perspective, we will reread $dx$ <strong>not as an infinitesimal quantity, but as a matrix, or as an operator.</strong>

> <strong>Note</strong> (the standpoint of this book)  
> This book is, above all, a book for unwinding elementary calculus and vector analysis. It is not a systematic development of differential forms in arbitrary dimensions.
>
> Therefore, until the end, we basically stay fixed in three-dimensional Cartesian coordinates $(x,y,z)$ and adopt the most straightforward expression from linear algebra: matrix representation. The $dx,dy,dz$ used in this book are defined, in this coordinate system, as concrete matrices that extract components.
>
> The aim is to let vector analysis sink in first as concrete symbols and operations—without leaning on infinitesimals—within the plain setting of three dimensions, Cartesian coordinates, and matrices.

> <strong>Note</strong> (on the name “Cartesian coordinates”)  
> In this book, “Cartesian coordinates” means an <strong>orthonormal coordinate system</strong>: a coordinate system whose axes meet at a common origin, are mutually orthogonal, and have equal spacing. In mathematics and in other books, this may also be called a rectangular coordinate system on Euclidean space, a Cartesian coordinate system, and so on. In this book, I will simply call it “Cartesian coordinates.”

> <strong>Note</strong> (extensions in Part III)  
> In Part III, however, we will touch on curvilinear coordinates and extensions to higher dimensions as needed.


> <strong>Checkpoint so far</strong>
> - An infinitesimal displacement is a column vector $\mathbf{v}$. The symbol $\Delta x$ is a scalar width, while a standalone $dx$ is an operator, a row vector or $1$-form.
> - The Cartesian $dy$ and $dz$ will be introduced in <strong>the next section, §1.2.3</strong>. They are $1$-forms based on <strong>the same idea</strong> as $dx$ in §1.1.6. Their distinction from $\Delta y$, $\Delta z$, and from $dy(\mathbf{v})$, $dz(\mathbf{v})$, follows the <strong>notational contract</strong> in §1.1.6.
> - Each term of the Riemann sum has the form $(f\,dx)(\mathbf{v}_i)$, and the integral can be understood as the limit of such sums.
> - The $dx$ at the end of the integral sign $\int_a^b f(x)\,dx$ is conventional notation. The displacement itself is written as $\Delta x$ or $dx(\mathbf{v})$, according to the contract in §1.1.6.

---

### §1.2 The Total Differential $df$ — An Operator That Packs Rates of Change into a Matrix

In the previous section, we dismantled the Riemann integral as “the limit of sums of the action of the matrix $f(x)\,dx$ on displacement vectors.” In this section, we extend that idea to the differential of the function itself and <strong>define the total differential $df$ as a row vector, or matrix</strong>. A “differential” is not merely a numerical rate of change. We treat it as an <strong>operator that produces the linear part of the change only after it is multiplied by a displacement vector</strong>.

#### 1.2.1 Matrix Representation of Differentiability

A function $f(x)$ is differentiable at a point $x$ if the following linear approximation holds:

$$
\Delta f = f(x+\Delta x)-f(x)=f'(x)\Delta x+o(|\Delta x|)\quad(|\Delta x|\to0).
$$

> <strong>Note</strong> (Landau order notation)  
> The term $o(|\Delta x|)$ is <strong>Landau order notation</strong>. As $\Delta x\to0$, the quantity written as $o(|\Delta x|)$ is a remainder whose ratio to $|\Delta x|$ tends to $0$. In other words, it is <strong>small enough to ignore</strong> compared with the main term $f'(x)\Delta x$. This notation often appears in science and engineering texts, though some readers may be seeing it for the first time.

Here $\Delta x$ is a scalar, but as in the previous section, we represent the corresponding displacement as the three-dimensional vector:

$$
\mathbf{v}=\begin{pmatrix}\Delta x\\0\\0\end{pmatrix}.
$$

Then the change $\Delta f$ of the function can be regarded as the effect caused by this $\mathbf{v}$.

#### 1.2.2 Defining $df$ as a Matrix and Reading $df(\mathbf{v})$

At the point $x$, define the <strong>total differential</strong> $df$ of the function $f$ as the following $1\times3$ row vector:

$$
df:=f'(x)\,dx=\begin{pmatrix}f'(x)&0&0\end{pmatrix}.
$$

As in the previous section, we write the result of letting this $df$ act on the displacement $\mathbf{v}$ as $df(\mathbf{v})$:

$$
df(\mathbf{v})=
\begin{pmatrix}f'(x)&0&0\end{pmatrix}
\begin{pmatrix}\Delta x\\0\\0\end{pmatrix}
=f'(x)\,\Delta x.
$$

Here is the <strong>important change in viewpoint</strong>. <strong>Always read it as follows</strong>:

* The expression $df=f'(x)\,dx$ is the familiar notation for the <strong>total differential</strong>, but in this book both $df$ and $dx$ are <strong>row-vector operators</strong>. By themselves, they are <strong>not infinitesimal changes</strong>.
* When we write $df(\mathbf{v})$, we mean the <strong>linear part of the change</strong> for a finite, though sufficiently small, displacement $\mathbf{v}$.

The object $df$ itself is not a change. It is a <strong>measuring device for the linear part of the change</strong>.

> <strong>Note</strong> ($df$ is an operator; $df(\mathbf{v})$ is the linear part of the change)
> This is the same distinction as the notational contract in §1.1.6, stated once again. It may feel repetitive, but <strong>if you misread this point, everything that follows will shift out of alignment</strong>. The repetition is worth it.

#### 1.2.3 The Measuring Devices $dy$ and $dz$ in the $y$ and $z$ Directions

The strength of this viewpoint shows up when we return to the mechanics example from §1.1.5: it extends naturally to the general case where the force has a component in the $y$ direction as well. With the $dy$ we now define, two-dimensional work can be treated uniformly in the form $F_x\,dx+F_y\,dy$.

Just as $dx$ extracts the $x$-component, we define $dy$ in physical space as the row vector, or $1$-form, that extracts the $y$-component, and $dz$ as the one that extracts the $z$-component. Their matrix representations are

$$
dy:=\begin{pmatrix}0&1&0\end{pmatrix},\qquad
dz:=\begin{pmatrix}0&0&1\end{pmatrix}.
$$

For a displacement

$$
\mathbf{v}=\begin{pmatrix}\Delta x\\\Delta y\\\Delta z\end{pmatrix},
$$

we have $dy(\mathbf{v})=\Delta y$ and $dz(\mathbf{v})=\Delta z$.

> <strong>Note</strong> (the contract for $dy$ and $dz$)  
> A standalone $dy$ or $dz$ is an operator. When we speak of infinitesimal widths in the $y$ or $z$ direction, we write $\Delta y$, $\Delta z$, or $dy(\mathbf{v})$, $dz(\mathbf{v})$. The $dy$ and $dz$ appearing at the tail of an integral sign should be read in the same way as $dx$, as conventional notation inherited from elementary calculus. The detailed convention is the <strong>same idea</strong> as the notational contract for $dx$ in §1.1.6.

Now we have all <strong>three measuring devices</strong> for three-dimensional space. In the main line of this chapter, we have focused on the $x$-direction slice, but you should think of the coordinates $y,z$ and the measuring devices $dy,dz$ as being available from the beginning.

We have now supplemented the one-variable expression $df=f'(x)\,dx$ with $dy$ and $dz$ as measuring devices of the same type. In the concrete example below and in the extension to three dimensions in §1.2.6, we will see how all three devices come into play.

#### 1.2.4 Example: $f(x)=x^2$

Let $f(x)=x^2$. Then $f'(x)=2x$.

For example, at $x=3$, the total differential is written explicitly as a row vector. Placing the row vector and column vector side by side,

$$
df=6\,dx=\begin{pmatrix}6&0&0\end{pmatrix},\qquad
\mathbf{v}=\begin{pmatrix}0.1\\0\\0\end{pmatrix}.
$$

Therefore the matrix product is

$$
df(\mathbf{v})=
\begin{pmatrix}6&0&0\end{pmatrix}
\begin{pmatrix}0.1\\0\\0\end{pmatrix}
=6\cdot0.1+0\cdot0+0\cdot0=0.6.
$$

Indeed, $f(3.1)-f(3)=9.61-9=0.61$, so the linear approximation $0.6$ agrees well.

#### 1.2.5 Substitution in Integrals and Rebuilding Measuring Devices

So far, we have read $dx$ as a measuring device for displacement.

That is, $dx$ is not a standalone infinitesimal quantity. It is a row vector that eats a displacement vector and returns its $x$-component. This reading is the basic convention of this book.

Once we have this reading, the substitution rule familiar from high school begins to look a little different.

Suppose a variable $x$ is expressed in terms of another variable $t$ by

$$
x=\gamma(t).
$$

In substitution, one often writes

$$
dx=\gamma'(t)\,dt.
$$

In ordinary calculus, this formula is explained by differentiating a composite function. For example, if $F'(x)=f(x)$, then differentiating $F(\gamma(t))$ with respect to $t$ gives

$$
\frac{d}{dt}F(\gamma(t))=f(\gamma(t))\gamma'(t).
$$

Therefore,

$$
\int_{t_0}^{t_1}f(\gamma(t))\gamma'(t)\,dt
=F(\gamma(t_1))-F(\gamma(t_0)).
$$

If we write the endpoints as

$$
x_0=\gamma(t_0),\qquad x_1=\gamma(t_1),
$$

then the right-hand side is

$$
F(x_1)-F(x_0)=\int_{x_0}^{x_1}f(x)\,dx.
$$

Thus we obtain

$$
\int_{x_0}^{x_1}f(x)\,dx
=
\int_{t_0}^{t_1}f(\gamma(t))\gamma'(t)\,dt.
$$

Up to this point, this is the standard explanation of substitution.

But in this book, we look at the formula with slightly different eyes. The expression

$$
dx=\gamma'(t)\,dt
$$

is not merely a computational symbol. It can be read as the result of rebuilding the measuring device $dx$ on the $x$ axis into a measuring device on the $t$ axis, using $dt$.

When $t$ changes a little, $x=\gamma(t)$ changes by $\gamma'(t)$ times that amount. Therefore, to build a measuring device that eats a small interval on the $t$ side and returns the same value as the displacement on the $x$ side, we need to multiply $dt$ by $\gamma'(t)$.

Chapter 4 will treat this viewpoint seriously as the pullback.

There, we will not use the formula as a mysterious given. We will rediscover the same coefficient $\gamma'(t)$ by mapping finite intervals and measuring their images. Then we will extend the same structure to finite cells and finite boxes.

For now, we have walked through the standard substitution calculation once. Later, in the main line of this book, we will reread it as “making measuring devices consistent.”

> <strong>Note</strong> ($dx=\gamma'(t)\,dt$)  
> In ordinary calculus, for the substitution $x=\gamma(t)$, this relation is written as $dx=\gamma'(t)\,dt$.
>
> From the standpoint of this book, however, this does not mean that the measuring device $dx$ itself on the $x$ side has moved to the $t$ side. It should be read as pulling back the $1$-form $dx$ on the target side along the map $\gamma:I\to\mathbb{R}$ to the domain side.
>
> More precisely, using the pullback notation introduced in Chapter 4, it is safer to write $\gamma^\ast(dx)=\gamma'(t)\,dt$. In other words, the $dx$ on the left originally measures displacement on the $x$ side, while $\gamma'(t)\,dt$ on the right is the device rebuilt to measure displacement on the $t$ side and return the same first-order change.
>
> At least from the standpoint of this book, hiding this distinction is one reason explanations of $dx$ in substitution can become confusing.

#### 1.2.6 Extension to Three Dimensions

A function $f$ that assigns a scalar, or real number, to each point $(x,y,z)$ in space may be treated simply as a <strong>real-valued function</strong> on physical space.

> <strong>Note</strong> (scalar fields)  
> In physics, such a function is often called a <strong>scalar field</strong>.

To say that $f(x,y,z)$ is <strong>totally differentiable</strong> at the point $(x,y,z)$ means that, for a displacement

$$
\mathbf{v}=\begin{pmatrix}\Delta x\\\Delta y\\\Delta z\end{pmatrix},
$$

the following relation holds:

$$
\begin{aligned}
\Delta f
&=f(x+\Delta x,\,y+\Delta y,\,z+\Delta z)-f(x,y,z)\\
&=\frac{\partial f}{\partial x}\,\Delta x
{}+\frac{\partial f}{\partial y}\,\Delta y
{}+\frac{\partial f}{\partial z}\,\Delta z
{}+o(\|\mathbf{v}\|)\quad(\|\mathbf{v}\|\to0).
\end{aligned}
$$

This has the same form as the one-variable definition in §1.2.1. The term $o(\|\mathbf{v}\|)$ is the same kind of remainder notation as $o(|\Delta x|)$. We will not go deeply into it here, but it should not obstruct the discussion.

Using the measuring devices $dx,dy,dz$ from §1.2.3, define the same type of operator as in §1.2.2 by

$$
df:=\frac{\partial f}{\partial x}\,dx+
\frac{\partial f}{\partial y}\,dy+
\frac{\partial f}{\partial z}\,dz
=
\begin{pmatrix}
\frac{\partial f}{\partial x}&
\frac{\partial f}{\partial y}&
\frac{\partial f}{\partial z}
\end{pmatrix}.
$$

For the next few lines, we drop the $o(\|\mathbf{v}\|)$ term and follow only the <strong>skeleton of the notation</strong>. By definition of differentiability, for $\mathbf{v}=\begin{pmatrix}\Delta x\\\Delta y\\\Delta z\end{pmatrix}$ we have $\Delta f=df(\mathbf{v})+o(\|\mathbf{v}\|)$. So <strong>$df(\mathbf{v})$ is not the exact change $\Delta f$, but its linear principal part once the remainder is stripped away</strong>. Writing that principal part as a matrix product gives

$$
\begin{aligned}
df(\mathbf{v})
&=\frac{\partial f}{\partial x}
\begin{pmatrix}1&0&0\end{pmatrix}
\begin{pmatrix}\Delta x\\\Delta y\\\Delta z\end{pmatrix}
+\frac{\partial f}{\partial y}
\begin{pmatrix}0&1&0\end{pmatrix}
\begin{pmatrix}\Delta x\\\Delta y\\\Delta z\end{pmatrix}\\
&\quad+\frac{\partial f}{\partial z}
\begin{pmatrix}0&0&1\end{pmatrix}
\begin{pmatrix}\Delta x\\\Delta y\\\Delta z\end{pmatrix}\\
&=\frac{\partial f}{\partial x}\,\Delta x+
\frac{\partial f}{\partial y}\,\Delta y+
\frac{\partial f}{\partial z}\,\Delta z.
\end{aligned}
$$

The first line shows, as a <strong>matrix product</strong>, how the measuring devices $dx,dy,dz$ from §1.2.3 extract the $x,y,z$ components from $\mathbf{v}$ as row vectors, with the partial derivatives attached as coefficients. The second line is the evaluated result, which has the same form as the <strong>linear principal term</strong> in the definition of $\Delta f$ above. The reading from §1.2.2 remains unchanged in three dimensions: <strong>row vector, or operator, times column vector, or displacement, gives a scalar</strong>.

If a function $f(x,y)$ involves only two coordinates, we can include it in the same framework by regarding it as independent of $z$, so that $\partial f/\partial z=0$. This three-dimensional framework contains the two-dimensional case naturally.

Compare the cases.

For one variable:

$$
df:=f'(x)\,dx=\begin{pmatrix}f'(x)&0&0\end{pmatrix}.
$$

For a two-variable function $f(x,y)$, using $dy$ from §1.2.3:

$$
df:=\frac{\partial f}{\partial x}\,dx+
\frac{\partial f}{\partial y}\,dy
=
\begin{pmatrix}
\frac{\partial f}{\partial x}&
\frac{\partial f}{\partial y}&0
\end{pmatrix}.
$$

For three variables $f(x,y,z)$, we simply have all three components of the row vector, as in §1.2.6.

Thus <strong>the form is the same; only the number of components increases</strong>. This is the advantage of the three-dimensional matrix representation. By viewing $df$ as a matrix, we can treat differentiation uniformly as an operator that gives the linear approximation with respect to a displacement.

#### 1.2.7 A Preview of Line Integrals

Suppose a curve in space is parametrized by

$$
\mathbf{r}(t)=\begin{pmatrix}x(t)\\y(t)\\z(t)\end{pmatrix},
$$

and write the displacement of each small step as $\Delta\mathbf{r}$. The limit of the operation of summing $(df)(\Delta\mathbf{r})$ over each step is written symbolically as

$$
\int_\gamma df
$$

where $\gamma$ is the curve. Just as with $\int f'(x)\,dx$ in §1.2.5, the skeleton is the limit of a Riemann sum in which the <strong>$1$-form $df$ acts on the displacement of each step</strong>. The precise treatment of closed curves, orientation, changes of parameter, and so on is left to later chapters.

---

> <strong>Checkpoint so far</strong>
> - Differentiability is understood as a linear approximation of the form $\Delta f=f'(x)\Delta x+o(|\Delta x|)$, where $o$ is Landau order notation.
> - $df=f'(x)\,dx$ is a row vector. Its action on a displacement, $df(\mathbf{v})$, gives the linear part of the change.
> - We look once at the standard starting point for substitution in integrals, but in this book we later reread it as “making measuring devices consistent” (§1.2.5).

---

### §1.3 Leibniz Notation and Algebraic Intuition

When Leibniz introduced the symbols $dx$ and $dy$, he treated them intuitively as “infinitesimals.”

> <strong>Note</strong> (Leibniz and notation)  
> <strong>Gottfried Wilhelm Leibniz</strong> (1646–1716) was the mathematician who organized the notation of calculus, including symbols such as $dx$ and $dy$. We will not go into the historical details here. I mention him only as the person who introduced the notation. Many readers are already used to the symbol $dx$ itself; if the name is unfamiliar, this one sentence is enough.

We have relocated that intuition into the language of <strong>linear algebra</strong>. Leibniz’s notation

$$
df=f'(x)\,dx
$$

is not merely a formal equality:

* $dx$: Leibniz’s infinitesimal intuition → in this book, extraction of the $x$-component as an <strong>operator</strong>. When we speak of the infinitesimal displacement itself, we write $\Delta x$ or $dx(\mathbf{v})$. The symbols $dy$ and $dz$ are defined in the same way as $dx$ in §1.2.3.
* $df$: Leibniz’s intuition of an infinitesimal change → in this book, the total differential as an <strong>operator</strong>. Its action on a displacement, $df(\mathbf{v})$, gives the linear part of the change.

<strong>Leibniz’s genius was to treat differentiation and integration as essentially algebraic operations.</strong> This book gives that intuition a concrete skeleton: matrices.

In the next section, we make explicit the hidden assumption behind this framework: the “convenience” of Cartesian coordinates. That also points toward more general coordinates.

---

> <strong>Checkpoint so far</strong>
> - In this book, the Leibnizian intuitions behind $dx$ and $df$ are row vectors, or operators, acting on displacements.
> - When discussing displacement widths, we write $\Delta x$; when discussing the linear part of a function’s change, we write $df(\mathbf{v})$.

---

### §1.4 Coordinate Transformations — Rebuilding Measuring Devices in New Coordinates

> <strong>Note</strong> (how to read this section)  
> It is all right if you do not fully understand this section on the first reading. What matters here is not the formula for cylindrical coordinates itself, but the feeling that, once we view $dx$ as a matrix, we can still compute when coordinates change.
>
> To repeat: for now, atmosphere is enough. In Chapter 4, we will spend much more space on the same idea. There, we will start by actually mapping finite intervals and finite cells and measuring their images. That will let us explain the rebuilding of measuring devices in a more organized way, without relying on the assumption that something is “sufficiently small.” What follows here is an explanation closer to the approximate viewpoint often used in ordinary calculus and mathematical physics: we assume that the change in parameter space is sufficiently small and extract only the first-order term.

Throughout this chapter, we have discussed the matrix representation of $dx$ by setting

$$
dx:=\begin{pmatrix}1&0&0\end{pmatrix}.
$$

As long as we view physical space in Cartesian coordinates $(x,y,z)$, this is the measuring device that extracts the $x$-component.

But physical problems are not always rectangular. In problems such as flow inside a circular pipe or the magnetic field around a straight current, it is often easier to use cylindrical coordinates, where a point is specified by the triple $(r,\theta,z)$.

So what does the measuring device $dx$ in physical space look like when viewed through cylindrical coordinates?

The important point is not to memorize a coordinate-transformation formula. The point is to rebuild a measuring device in physical space into one expressed in another set of variables, so that it returns the same first-order value.

> <strong>Note</strong> (locality of cylindrical coordinates)  
> Here we do not deal with the periodicity of $\theta$ or the singularity at $r=0$. We treat cylindrical coordinates only as a local parametrization.
>
> In actual computations in mathematical physics using cylindrical or spherical coordinates, one can often avoid coordinate singularities by choosing the integration range or the target region appropriately.
>
> However, in problems involving the origin, an axis, or the periodicity of the angle in an essential way, this local representation is not enough. In such cases, one must handle coordinate patches and boundary conditions more carefully.

#### 1.4.1 The Transformation from Cylindrical Coordinates to Physical Space

Write the transformation from the parameter space of cylindrical coordinates to physical space as

$$
\Phi(r,\theta,z)
=
\begin{pmatrix}
r\cos\theta\\
r\sin\theta\\
z
\end{pmatrix}.
$$

This transformation sends the point $(r,\theta,z)$ in parameter space to the point $(x,y,z)$ in physical space. In other words,

$$
x=r\cos\theta,\qquad
y=r\sin\theta,\qquad
z=z.
$$

The question is: what kind of measuring device does the physical-space $dx$ become on the parameter-space side?

#### 1.4.2 Map a Small Step and Measure It with $dx$

Consider a small step

$$
\mathbf h
=
\begin{pmatrix}
\Delta r\\
\Delta\theta\\
\Delta z
\end{pmatrix}
$$

from the point

$$
p=(r,\theta,z)
$$

in parameter space.

After the move, the point is

$$
p+\mathbf h
=
(r+\Delta r,\theta+\Delta\theta,z+\Delta z).
$$

But this $\mathbf h$ is not a displacement vector in physical space. It lists the changes in the parameter space of cylindrical coordinates.

Now send this small step into physical space by the transformation $\Phi$. The displacement in physical space is

$$
\Phi(p+\mathbf h)-\Phi(p).
$$

Written componentwise, this is

$$
\Phi(r+\Delta r,\theta+\Delta\theta,z+\Delta z)
-
\Phi(r,\theta,z)
=
\begin{pmatrix}
(r+\Delta r)\cos(\theta+\Delta\theta)-r\cos\theta\\
(r+\Delta r)\sin(\theta+\Delta\theta)-r\sin\theta\\
\Delta z
\end{pmatrix}.
$$

This vector is the true displacement in physical space.

The physical-space measuring device $dx$ extracts only the $x$-component from a physical-space displacement vector. Therefore, applying $dx$ to the displacement above gives

$$
dx\bigl(\Phi(p+\mathbf h)-\Phi(p)\bigr)
=
(r+\Delta r)\cos(\theta+\Delta\theta)-r\cos\theta.
$$

This value measures how much the $x$-component in physical space changes when we move by $\mathbf h$ in parameter space.

#### 1.4.3 Build a Measuring Device from the First-Order Term

Now assume that $\Delta r,\Delta\theta,\Delta z$ are small, and look only at the first-order terms.

First,

$$
\Delta x
=
(r+\Delta r)\cos(\theta+\Delta\theta)-r\cos\theta.
$$

Using the first-order approximation

$$
\cos(\theta+\Delta\theta)
=
\cos\theta-\sin\theta\,\Delta\theta
+
\text{higher-order terms},
$$

we get

$$
\begin{aligned}
\Delta x
&=
(r+\Delta r)\cos(\theta+\Delta\theta)-r\cos\theta\\
&=
(r+\Delta r)(\cos\theta-\sin\theta\,\Delta\theta+\text{higher-order terms})-r\cos\theta\\
&=
r\cos\theta
+\cos\theta\,\Delta r
-r\sin\theta\,\Delta\theta
+\text{higher-order terms}
-r\cos\theta\\
&=
\cos\theta\,\Delta r
-r\sin\theta\,\Delta\theta
+\text{higher-order terms}.
\end{aligned}
$$

Since $\Delta z$ does not affect the $x$-component, we can write

$$
\Delta x
=
\cos\theta\,\Delta r
-r\sin\theta\,\Delta\theta
+0\cdot\Delta z
+
\text{higher-order terms}.
$$

The first-order term we have obtained is

$$
\cos\theta\,\Delta r
-r\sin\theta\,\Delta\theta
+0\cdot\Delta z.
$$

This is equal to the value obtained by applying the following row vector to the small step in parameter space,

$$
\mathbf h
=
\begin{pmatrix}
\Delta r\\
\Delta\theta\\
\Delta z
\end{pmatrix}:
$$

$$
\begin{pmatrix}
\cos\theta & -r\sin\theta & 0
\end{pmatrix}
\begin{pmatrix}
\Delta r\\
\Delta\theta\\
\Delta z
\end{pmatrix}
=
\cos\theta\,\Delta r
-r\sin\theta\,\Delta\theta
+0\cdot\Delta z.
$$

Therefore, if we rewrite the physical-space measuring device $dx$ as a measuring device on the cylindrical-coordinate parameter space that returns the same first-order value, we get

$$
\begin{pmatrix}
\cos\theta & -r\sin\theta & 0
\end{pmatrix}.
$$

This is what $dx$ looks like when viewed through cylindrical coordinates.

> <strong>Note</strong> (splitting large geometry into small geometry)  
> Many textbooks draw a curved $(r,\theta)$ grid in physical space and explain geometrically that “the arc length in the $\theta$ direction is approximately $r\Delta\theta$.” That intuition itself is correct.
>
> In this book, however, we first prioritize an algebraic procedure: map a small step in parameter space into physical space, and then measure its image.
>
> The coefficient $-r\sin\theta$ carries the information of how much a step in the $\theta$ direction contributes to the $x$ direction in physical space. Similarly, $\cos\theta$ tells us how much the $r$ direction contributes to the $x$ direction, and $0$ tells us that the $z$ direction does not contribute to the $x$ direction.
>
> In other words, the single row $\begin{pmatrix}\cos\theta & -r\sin\theta & 0\end{pmatrix}$ is the geometry of the change in the $x$-component split into three small components.

#### 1.4.4 Reading It as a Pulled-Back Measuring Device

Read the computation above this way.

The physical-space measuring device $dx$ eats a displacement in physical space and returns its $x$-component. But when we want to compute in cylindrical coordinates, the input is not the physical-space displacement itself. The input is a small step in parameter space,

$$
\begin{pmatrix}
\Delta r\\
\Delta\theta\\
\Delta z
\end{pmatrix}.
$$

So we build a measuring device that, when it eats a small step in parameter space, returns the same first-order value that $dx$ would have measured in physical space.

That measuring device was

$$
\begin{pmatrix}
\cos\theta & -r\sin\theta & 0
\end{pmatrix}.
$$

In the mathematics of measuring devices, this operation is called a <strong>pullback</strong>. Symbolically,

$$
\Phi^*(dx)
=
\cos\theta\,dr-r\sin\theta\,d\theta.
$$

Here $dr,d\theta,dz$ are the measuring devices that extract, respectively, the first, second, and third components from a displacement in parameter space,

$$
\begin{pmatrix}
\Delta r\\
\Delta\theta\\
\Delta z
\end{pmatrix}.
$$

Therefore,

$$
\cos\theta\,dr-r\sin\theta\,d\theta
$$

is simply the parameter-space row vector

$$
\begin{pmatrix}
\cos\theta & -r\sin\theta & 0
\end{pmatrix}
$$

written in measuring-device notation.

In other words, it is safe here to read

$$
\Phi^*(dx)
=
\begin{pmatrix}
\cos\theta & -r\sin\theta & 0
\end{pmatrix}.
$$

The right-hand side, however, is a row vector that eats displacements in the parameter space of cylindrical coordinates:

$$
\begin{pmatrix}
\Delta r\\
\Delta\theta\\
\Delta z
\end{pmatrix}.
$$

> <strong>Note</strong> (we built it from a finite step here)  
> Here we did not start by using the known formula
> $$
> dx=\frac{\partial x}{\partial r}dr+\frac{\partial x}{\partial\theta}d\theta+\frac{\partial x}{\partial z}dz.
> $$
>
> First, we mapped a small step in parameter space into physical space and measured its image using the physical-space $dx$. Then we built a measuring device on the parameter-space side that returns the same first-order value.
>
> In Chapter 4, we will extend this same idea to finite intervals, finite cells, and finite boxes. There, we will see how measuring devices must be rebuilt in order to preserve lengths of intervals, areas, and volumes.

#### 1.4.5 Two Cartesian Coordinate Systems

Let us now make clear the relation between the two triples of numbers we are using: $(x,y,z)$ in physical space and $(r,\theta,z)$ in the parameter space of cylindrical coordinates.

The physical-space $(x,y,z)$ is the usual Cartesian coordinate system. On the other hand, $(r,\theta,z)$ is also a coordinate system consisting of three numbers on the calculation page. Physically, $\theta$ is an angle, but in parameter space it is treated as one coordinate axis.

Thus both physical space and parameter space have “straight components” for purposes of calculation. What is curved is the transformation $\Phi$ connecting the two spaces. That curvature appears as coefficients such as $\cos\theta$ and $-r\sin\theta$.

One can think of curved coordinate axes as growing inside physical space. But in this book, I try not to think that way. Instead, I think as follows:

<strong>There are two places: physical space and parameter space. Between them is a translation rule </strong>$\Phi$<strong>.</strong>

From this point of view, rebuilding measuring devices becomes fairly simple. We pull the measuring device in physical space back to the parameter-space side through the transformation $\Phi$. Then we can read, directly from a displacement in parameter space, the same first-order value that would have been measured in physical space.

> <strong>Note</strong> (matrix representations of $dr$, $d\theta$, and $dz$)  
> Parameter space is also, for purposes of calculation, a space with three components. Thus $dr$ is the measuring device that extracts the first component in parameter space, $d\theta$ extracts the second, and $dz$ extracts the third.
>
> In matrix representation,
> $$
> dr=\begin{pmatrix}1&0&0\end{pmatrix},\qquad
> d\theta=\begin{pmatrix}0&1&0\end{pmatrix},\qquad
> dz=\begin{pmatrix}0&0&1\end{pmatrix}.
> $$
> But these are measuring devices acting on displacements in parameter space. They live on a different space from the $dx,dy,dz$ that act on physical-space $(x,y,z)$.

#### 1.4.6 Foreshadowing Chapter 4

In this way, the pullback is the operation of rebuilding a measuring device from physical space so that it returns the same value on the parameter-space side.

In Chapter 1, we have only seen one example, using the smallest measuring device, $dx$. In Chapter 4, however, we will extend the same idea to area and volume.

There, we will pull back area-measuring devices such as

$$
dx\wedge dy
$$

and volume-measuring devices such as

$$
dx\wedge dy\wedge dz
$$

to other variable systems.

The coefficients that appear then are the familiar $r$ in cylindrical coordinates, or the Jacobian $J$ that appears in general changes of variables.

In other words, the Chapter 4 formulas

$$
\Phi^*(dx\wedge dy)=r\,dr\wedge d\theta
$$

and

$$
\Phi^*(dx\wedge dy\wedge dz)=J\,du\wedge dv\wedge dw
$$

have the same structure as the formula we have just seen:

$$
\Phi^*(dx)
=
\cos\theta\,dr-r\sin\theta\,d\theta.
$$

> <strong>Note</strong> (the philosophy of delaying the metric)  
> The $\cos\theta$ and $-r\sin\theta$ that appeared here will later be organized in relation to the metric $g$ in Chapter 6. For now, however, it is enough to read them as the components of a measuring device rebuilt by the transformation $\Phi$.
>
> It is also important to draw curved figures in physical space and estimate arc length as $r\Delta\theta$. But in this book, we first prioritize the algebraic procedure of mapping a small step in parameter space and measuring its image. That procedure will become important later when we compute areas and volumes.

---

> <strong>Checkpoint so far</strong>
>
> - The measuring device $dx$ itself extracts the $x$-component in physical space.
> - When we want to compute in cylindrical coordinates, we rebuild the physical-space measuring device $dx$ as a measuring device on the parameter-space side.
> - By mapping a small step in parameter space into physical space and measuring its image with $dx$, we can determine the components of the parameter-space measuring device.
> - In cylindrical coordinates, $\Phi^*(dx)=\cos\theta\,dr-r\sin\theta\,d\theta$.
> - In Chapter 4, we will extend the same idea to area-measuring devices and volume-measuring devices.

---

### §1.5 Writing in Another Coordinate System — Exercises

Near the end of this chapter, we want you to work through, by hand, what it means to “write in another coordinate system.” We have not yet defined coordinate changes as a general theory, but in §1.4.3 we already saw that **the same** $dx$ **gets a different matrix representation when coordinates change**. This exercise lets you confirm that by calculation. **Why do it before the full vocabulary of coordinate change is in place?** So that when later chapters get busy, you already feel that changing components is only natural.

#### 1.5.1 Exercise: Measurement in Cylindrical Coordinates

<strong>Problem setup</strong>  
As in the previous section, the matrix representation of $dx$ in cylindrical coordinates $(r,\theta,z)$ is

$$
dx = \begin{pmatrix} \cos\theta & -r\sin\theta & 0 \end{pmatrix}
$$

(The row above is the row vector that acts on displacements in parameter space, constructed in §1.4.3. It is **not** obtained by taking the Cartesian row $\begin{pmatrix}1&0&0\end{pmatrix}$ from §1.1.3 and simply turning it into a column vector.)

Answer the following questions.

<strong>Question 1</strong>  
Suppose a particle is at the point $P(r=2,\theta=\pi/6,z=0)$ in the parameter space of cylindrical coordinates. The particle undergoes a small displacement of $0.1$ in the $r$ direction. **In this section, we denote by** $\mathbf{v}$ **the vector** $\begin{pmatrix}\Delta r\\\Delta\theta\\\Delta z\end{pmatrix}$ **listing the changes in the parameters** $r,\theta,z$ (this ordering is different from the Cartesian column $\begin{pmatrix}\Delta x\\\Delta y\\\Delta z\end{pmatrix}$ in §1.0–§1.2). Write this displacement vector $\mathbf{v}$ in terms of its components.

<strong>Question 2</strong>  
Apply the matrix $dx$ at the point $P$ to the displacement vector $\mathbf{v}$ from Question 1. (Use $\cos(\pi/6)=\sqrt{3}/2$.)

<strong>Question 3</strong>  
Explain what the result $dx(\mathbf{v})$ from Question 2 means physically.

#### 1.5.2 Solutions and Commentary

<strong>Answer to Question 1</strong>  
The displacement is $0.1$ in the $r$ direction and zero in the $\theta$ and $z$ directions, so as a column vector listing **changes in the cylindrical parameters**, we write

$$
\mathbf{v} = \begin{pmatrix} 0.1 \\ 0 \\ 0 \end{pmatrix}
$$

<strong>Answer to Question 2</strong>  
At the point $P$, the matrix $dx$ is the $1\times 3$ row vector obtained by substituting $\theta=\pi/6$ and $r=2$:

$$
dx
=
\begin{pmatrix}
\cos(\frac{\pi}{6}) & -2\sin(\frac{\pi}{6}) & 0
\end{pmatrix}
=
\begin{pmatrix}
\frac{\sqrt{3}}{2} & -2 \times \frac{1}{2} & 0
\end{pmatrix}
=
\begin{pmatrix}
\frac{\sqrt{3}}{2} & -1 & 0
\end{pmatrix}
$$

(In cylindrical coordinates, the components of $dx$ depend on $r$ and $\theta$, so what we mean here is the row evaluated at the coordinates of the point $P$. The notation $dx(\mathbf{v})$ matches §1.1.3.)

What matters is that the second entry of the row vector is generally the coefficient $-r\sin\theta$, and thanks to $r$ it **carries a length dimension**. Substituting $r=2$ and $\theta=\pi/6$ gives the numerical value $-1$ for that coefficient, but **the number** $-1$ **by itself does not carry a dimension**. The correct reading is that the matrix entry $-r\sin\theta$ carries the length dimension. This is the key to dimensional analysis.

Applying this to the displacement vector $\mathbf{v}$ gives

$$
dx(\mathbf{v})
=
\begin{pmatrix}
\frac{\sqrt{3}}{2} & -1 & 0
\end{pmatrix}
\begin{pmatrix}
0.1\\
0\\
0
\end{pmatrix}
=
0.1 \times \frac{\sqrt{3}}{2}
\approx 0.0866
$$

<strong>Answer to Question 3 (physical meaning)</strong>  
This result expresses the physical fact that **a motion of $0.1$ outward in the $r$ direction in cylindrical coordinates corresponds, when viewed along the $x$ axis in physical space, to a forward displacement of about $0.0866$.**

> <strong>Note</strong> (“about” versus exact agreement)  
> For this displacement we have $\Delta\theta=\Delta z=0$, so from $x=r\cos\theta$ we get $\Delta x=(\Delta r)\cos\theta$ **exactly**. We wrote “about” only because the decimal display $0.0866$ is rounded.

#### 1.5.3 Motion in the Angular Direction

At the same point $P(r=2,\theta=\pi/6,z=0)$, let us also consider motion by $0.1$ in the $\theta$ direction.

Then the displacement in the parameter space of cylindrical coordinates is

$$
\mathbf{v}
=
\begin{pmatrix}
0\\
0.1\\
0
\end{pmatrix}
$$

At the point $P$, $dx$ is again

$$
dx
=
\begin{pmatrix}
\frac{\sqrt{3}}{2} & -1 & 0
\end{pmatrix}
$$

so

$$
dx(\mathbf{v})
=
\begin{pmatrix}
\frac{\sqrt{3}}{2} & -1 & 0
\end{pmatrix}
\begin{pmatrix}
0\\
0.1\\
0
\end{pmatrix}
=
-0.1
$$

Here, the second component of the input vector, $0.1$, is an angle and therefore dimensionless. But the second entry of the row vector, $-r\sin\theta$, carries a length dimension. Therefore the output $-0.1$ has the dimension of length.

This is an important property of **linear forms**. The matrix entries of $dx$ themselves are functions that include $r$, and even when the input is given in coordinate components (with mismatched dimensions), the output is always automatically adjusted to have the correct physical dimension, namely “length in the $x$ direction.” **A linear form is a measuring device that absorbs the distortion of the coordinate system and outputs a physically meaningful measured value.**

---

### §1.6 Summary of This Chapter and Outlook Toward the Next

> <strong>Checkpoint — Chapter 1 as a whole</strong>
> - Chapter 1 centers on reading $dx$ as a matrix / linear form and reading $\int f\,dx$ as the limit of actions. The main exposition leaned on the $x$ direction, but the Cartesian measuring devices $dy$ and $dz$ were defined in the same way as $dx$ in §1.2.3.
> - $df$ is also unified as a row vector; the extension to several dimensions is simply an increase in the number of components.
> - From the next chapter onward, we extend these measuring devices to the <strong>wedge product</strong>, exterior derivative, and Hodge star.

In this chapter we leaned on the $x$ direction for concrete examples of integrals and $df$, and often treated $y$ and $z$ as fixed “slices.” Even so, the linear forms in physical space are the full trio $dx$, $dy$, and $dz$ (§1.2.3).

In the next chapter we combine these three to introduce the **wedge product**, also called the **exterior product** $\wedge$. This constructs **area-measuring devices** and **volume-measuring devices** ($2$-forms and $3$-forms), and leads to **higher differential forms** that are not limited to objects that act on vectors and return scalars. Aggregation along curves, surfaces, and regions (line integrals, surface integrals, volume integrals) will be treated in later chapters, after these measuring devices are in place.

<!-- role: roadmap -->
In later parts we proceed to the <strong>exterior derivative</strong> $\mathrm{d}$, the <strong>Hodge star operator</strong> $\ast$, and the vector-analysis operators $\mathrm{grad}$ ($\nabla$), $\mathrm{curl}$ ($\nabla\times$), and $\mathrm{div}$ ($\nabla\cdot$), followed by Stokes’s theorem, Maxwell’s equations, and the basic equations of fluid mechanics. The correspondence between differential forms and vector fields in three dimensions can be organized using the Hodge star.

Let us gradually unravel how three-dimensional Euclidean space looks.

# Chapter 2: What Is Area? — The Sign Rule Hidden in Parallelepipeds

# Chapter 2: What Is Area? — The Sign Rule Hidden in Parallelepipeds

### §2.0 Measuring Devices, Area, Volume, and Length

In Chapter 1, we defined $dx$, $dy$, and $dz$ as row vectors ($1$-forms) that eat one vector and return a scalar, and we reread $\int f\,dx$ as the limit of matrix actions. In this chapter we extend that framework and <strong>discover area-measuring devices</strong> ($2$-forms), which eat two vectors, and <strong>volume-measuring devices</strong> ($3$-forms), which eat three. Both are built from the same parts: $dx$, $dy$, and $dz$.


### §2.2 The Three Rules an Area-Measuring Device Must Satisfy

As a first step in the design, we do not rely only on “$1\times 1$ squares.” We take as our base the <strong>parallelogram spanned by two vectors</strong>.

> <strong>Note</strong> (why start with a parallelogram)  
> For readers used to “area = tiling with squares,” the motivation for suddenly starting with a parallelogram may not be obvious. Taking a parallelogram as the base relaxes the requirement that the sides be orthogonal, and the rules we are about to build become cleaner. A square appears naturally as a <strong>special case</strong>. When <strong>extending integrals to higher dimensions</strong>, this approach is also easier to handle.

What we want is a magic black box $S(\mathbf{v}_1,\mathbf{v}_2)$ that eats two vectors as input and spits out the area $S$ of the parallelogram they span.

This is somewhat sweeping, but for this black box to function properly as an “area-measuring device,” it is enough for it to satisfy the following three rules. Picture a parallelogram whose adjacent sides are two arrows emanating from the origin, and check each rule.

#### 2.2.1 Rule 1: If one side stretches, the area stretches too (proportionality)

If one side vector $\mathbf{v}_1$ is doubled, the area of the parallelogram should naturally double:

$$S(2\mathbf{v}_1,\mathbf{v}_2)=2S(\mathbf{v}_1,\mathbf{v}_2).$$

Similarly, if we feed in the sum of two vectors, the area should split additively:

$$S(\mathbf{v}_1+\mathbf{u},\mathbf{v}_2)=S(\mathbf{v}_1,\mathbf{v}_2)+S(\mathbf{u},\mathbf{v}_2).$$

Together, these two properties are called <strong>linearity</strong>. The same “scalar multiple” and “additivity over sums” hold for the second argument $\mathbf{v}_2$ as well — in other words, $S$ is <strong>linear in both arguments</strong> (<strong>bilinear</strong>).

#### 2.2.2 Rule 2: Overlap gives zero (alternation)

This is the most important rule. What if $\mathbf{v}_1$ and $\mathbf{v}_2$ are exactly the same vector? The parallelogram collapses to a line and the area is zero:

$$S(\mathbf{v}_1,\mathbf{v}_1)=0.$$

In fact, from this “same input gives zero” rule, a very strange property follows. Using Rule 1 (linearity), put $\mathbf{v}_1+\mathbf{v}_2$ into both arguments. By “same gives zero,”

$$S(\mathbf{v}_1+\mathbf{v}_2,\;\mathbf{v}_1+\mathbf{v}_2)=0.$$

Expanding the left-hand side by linearity gives

$$S(\mathbf{v}_1,\mathbf{v}_1)+S(\mathbf{v}_1,\mathbf{v}_2)+S(\mathbf{v}_2,\mathbf{v}_1)+S(\mathbf{v}_2,\mathbf{v}_2)=0.$$

The first and fourth terms vanish by Rule 2, so what remains is $S(\mathbf{v}_1,\mathbf{v}_2)+S(\mathbf{v}_2,\mathbf{v}_1)=0$. Thus

$$S(\mathbf{v}_1,\mathbf{v}_2)=-S(\mathbf{v}_2,\mathbf{v}_1).$$

If we swap the order of the input vectors, <strong>the sign of the area flips</strong>.

> <strong>Note</strong> (signed area 1)  
> “Negative area? That sounds wrong.” Perhaps — but physicists do not ignore the “orientation” of nature. The direction of a current, the direction of a magnetic field — in all of these, a vector’s orientation is essential. So the idea that “area, too, has an orientation (signed area)” is rather natural for us physicists. This concept will later be indispensable when we distinguish the two sides of a surface, or compute magnetic flux or fluid flow through space. For now, do not worry too much; just keep moving.

> <strong>Note</strong> (signed area 2)  
> Even in one variable, when $f(x)<0$ on an interval we can have $\displaystyle\int_a^b f(x)\,dx<0$ — signed “area” is already there. Signed area is that idea lifted to two dimensions.

#### 2.2.3 Rule 3: Fixing the standard (normalization)

Finally, we must decide “what size counts as $1$.” Here we simply declare that the square formed by the <strong>basis vectors</strong> (standard basis vectors) $\hat{e}_x$ in the $x$ direction and $\hat{e}_y$ in the $y$ direction has area $1$. In this book’s convention, written as <strong>column vectors</strong>,

$$\hat{e}_x=\begin{pmatrix}1\\0\\0\end{pmatrix},\qquad
\hat{e}_y=\begin{pmatrix}0\\1\\0\end{pmatrix}.$$

$$S(\hat{e}_x,\hat{e}_y)=1.$$

> <strong>Note</strong> (basis vectors / standard basis)  
> One can think of the basis vectors (standard basis) as unit vectors along the axes of Cartesian coordinates. A more advanced definition is left to linear algebra.

---

> <strong>Checkpoint so far</strong>
> - An area-measuring device is a gadget that eats two vectors and returns a scalar. It must satisfy three rules: linearity, alternation, and normalization.
> - From alternation (same vector twice gives zero) we get $S(\mathbf{v}_1,\mathbf{v}_2)=-S(\mathbf{v}_2,\mathbf{v}_1)$, so area becomes <strong>signed</strong>.
> - In the next section we search concretely for an algebraic device that satisfies these three rules.

---

### §2.3 An Area-Measuring Device Is an "Antisymmetric Matrix"

We have now set three rules while picturing in our minds the <strong>image of a figure</strong> called a “parallelogram.” However, once the rules are fixed, we no longer need to visualize the figure. <strong>“If we find an algebraic formula that satisfies these three rules, that becomes the definition of area.”</strong>

For simplicity, let us first consider two vectors whose $z$ component is always zero—that is, two vectors lying in the $xy$ plane.

$$
\mathbf{v}_1 = \begin{pmatrix} x_1 \\ y_1 \\ 0 \end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix} x_2 \\ y_2 \\ 0 \end{pmatrix}
$$

Stating the conclusion first: <strong>under the constraint that the vectors lie in the $xy$ plane</strong>, the measuring device that outputs a quantity perfectly satisfying the three rules above settles into exactly one natural form in the world of linear algebra.

That is a computation of the form “<strong>row vector</strong> $\times$ <strong>matrix</strong> $\times$ <strong>column vector</strong>” with a certain $3 \times 3$ <strong>matrix</strong> sandwiched in the middle:

$$
\begin{pmatrix} x_1 & y_1 & 0 \end{pmatrix}
\begin{pmatrix}
  0 & 1 & 0 \\
  -1 & 0 & 0 \\
  0 & 0 & 0
\end{pmatrix}
\begin{pmatrix} x_2 \\ y_2 \\ 0 \end{pmatrix}
$$

Let us actually substitute $\mathbf{v}_1$ and $\mathbf{v}_2$ and compute:

$$
\begin{pmatrix} x_1 & y_1 & 0 \end{pmatrix}
\begin{pmatrix}
  0 & 1 & 0 \\
  -1 & 0 & 0 \\
  0 & 0 & 0
\end{pmatrix}
\begin{pmatrix} x_2 \\ y_2 \\ 0 \end{pmatrix}
= \begin{pmatrix} -y_1 & x_1 & 0 \end{pmatrix}
\begin{pmatrix} x_2 \\ y_2 \\ 0 \end{pmatrix}
= x_1 y_2 - x_2 y_1
$$

The quantity $x_1 y_2 - x_2 y_1$ we obtain here is precisely the content of the “two-dimensional area formula.”

> <strong>Note</strong> (antisymmetric matrix and metric)  
> We have written $\mathbf{v}_1^T M \mathbf{v}_2$ (row vector $\times$ matrix $\times$ column vector). From a more advanced standpoint—that of general tensor analysis or general manifold theory—this way of laying vectors on their side without making the metric explicit is slightly bad manners. However, this book will proceed for the time being with standard Cartesian coordinates fixed. Within that scope there is no problem, so we will push forward with this notation here. After introducing the metric in Chapter 6, we will revisit this point.

#### 2.3.1 Higher-Dimensional Extension of the Measuring Device

To repeat, we make the following standpoint clear here.
Rather than putting first the naive intuition of **the number of tiles** we counted in elementary school, we now define the quantity obtained by feeding two vectors into this $3 \times 3$ antisymmetric matrix as **the area component returned by this measuring device**—the area-measuring device specialized to the $xy$ plane, or the reading along $dx \wedge dy$. It does not exhaust all the <strong>information</strong> about oriented area in three-dimensional space in a single number; it is merely <strong>a scalar cut out by one pair of glasses</strong>. The full picture will be given in §2.4.6 when we align all three kinds of measuring devices.

The $1$-form from the previous chapter was a “$1 \times 3$ matrix” that captures one vector.
The matrix before us now has evolved into a “$3 \times 3$ antisymmetric matrix” that **receives two vectors at once and computes area**.

We will call this matrix (or operator) a $2$-form.

> <strong>Note</strong> (quadratic form and $2$-form)  
> In linear algebra, “quadratic form” often refers to a quadratic polynomial. The $2$-form here is terminology from differential forms and is a different object.

Now the reader must be thinking:
“I see, I understand that area comes out from a matrix. But this matrix has zeros in the third row and third column, so it completely ignores the $z$ component. This doesn’t solve that ‘painful three-dimensional calculation,’ does it?”

<strong>Exactly right.</strong>
The matrix $\begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ we now have in our hands is nothing more than one of the three basic measuring devices in three-dimensional space—the <strong>area-measuring device specialized to the $xy$ plane</strong>.
This is like <strong>a “biased pair of glasses” that looks only at the $xy$ plane</strong>. In space, there also exist glasses that look at the $yz$ plane and glasses that look at the $zx$ plane.

---

> <strong>Checkpoint so far</strong>
> - An area-measuring device ($2$-form) is an algebraic device that measures the “pairing of two vectors,” not the parallelogram itself that is being measured.
> - The true identity of an area-measuring device is an “antisymmetric matrix,” and the physical rules completely determine the form of the matrix.
> - In three-dimensional space there exist three kinds of “biased glasses” (basis $2$-forms).

---

### §2.4 Internal Structure of the Area-Measuring Device

#### 2.4.1 Determining the Form of a "Device That Handles Two Inputs"

In §2.3, we said that the true identity of an area-measuring device ($2$-form) is the $3 \times 3$ antisymmetric matrix sandwiched in the middle. However, that matrix had been handed down from on high by the author.

Our next goal is this:
**“Can we combine the simple measuring devices $dx, dy, dz$ introduced in Chapter 1 as parts, and systematically build that complicated matrix?”**
If we can do this, then although we currently have only an area-measuring device specialized to the $xy$ plane, we will also be able to mass-produce area-measuring devices for the $yz$ plane and the $zx$ plane from the same parts by the same procedure.

To achieve this, let us first think about what the overall form of a “device that eats two vectors and spits out a scalar” ought to look like.

In Chapter 1, we saw that a device that eats one vector ($1$-form) can be represented as a "row vector" (row $\times$ column $=$ scalar).
So how can we write a device that eats two vectors, $\mathbf{v}_1$ and $\mathbf{v}_2$, at the same time, and moreover preserves the Rule 1 from §2.2 (proportionality and linearity) with respect to both?

The natural form is one in which a square table (matrix) is sandwiched between the two vectors—that is, the form **“row $\times$ matrix $\times$ column”** ($\mathbf{v}_1^T M \mathbf{v}_2$). Let us accept this as a requirement of linear algebra. What we must find is the contents of the matrix $M$ sandwiched in the middle.

#### 2.4.2 Contraction—An Operation That Eliminates the Matrix

Here, let us give a name to the form "row $\times$ matrix $\times$ column" that we derived earlier.

Writing $\mathbf{v}_1^T M \mathbf{v}_2$ in components,

$$
\mathbf{v}_1^T M \mathbf{v}_2 = \sum_{i=1}^3 \sum_{j=1}^3 v_{1i}\, M_{ij}\, v_{2j}
$$

On the left-hand side we had the matrix $M$ ($3 \times 3 = 9$ numbers) and two vectors ($3+3=6$ numbers), but the right-hand side is just a single scalar. The indices $i$ and $j$ are "eliminated" by the sums, and 15 numbers collapse into 1. This is an example of an operation called <strong>contraction</strong>.

<strong>Contraction in the narrow sense</strong> is the operation of "taking a sum over one pair of matching indices." The simplest example is the $1$-form from Chapter 1. $dx(\mathbf{v}) = \sum_i (dx)_i v_i$ obtains a scalar by contracting once over the index $i$. Likewise, the matrix–vector product $\sum_j M_{ij} v_j$ is an operation that contracts once over the index $j$ to obtain a vector (the index $i$ remains).

<strong>Contraction in the broad sense</strong> is what you get by stacking this several times. The expression $\mathbf{v}_1^T M \mathbf{v}_2 = \sum_i \sum_j v_{1i} M_{ij} v_{2j}$ that we just saw creates a scalar from a matrix and two vectors by contracting over <strong>both</strong> indices $i$ and $j$—this is a <strong>double contraction</strong>. In the second half of this chapter (§2.5), the determinant appears as a contraction of three vectors with the Levi-Civita symbol $\epsilon_{ijk}$. Appendix A follows the entire process.

> <strong>Note</strong> (the feel of contraction)  
> Indices disappear—this is the feel of contraction. A $3 \times 3$ matrix has two indices (row and column), and a vector has one index. In contraction, we make the index of the vector and an index of the matrix "the same letter" and take a sum, so that index vanishes from the expression. If two indices disappear, the number of remaining indices is zero—that is, we get a scalar. This operation of "eliminating indices" underlies every calculation in this book.

#### 2.4.3 Filling in the Entries from the Desired Result

There is no need to search blindly. We already know the <strong>"answer"</strong> that ought to be output: the area formula for the $xy$ plane.

$$\text{Desired output} = x_1 y_2 - x_2 y_1$$

To produce this output, what numbers should we place in the entries of the matrix $M$? I want the reader to join in and solve the puzzle of filling in the entries while imagining the expansion of $\mathbf{v}_1^T M \mathbf{v}_2$.

$$
\begin{pmatrix} x_1 & y_1 & z_1 \end{pmatrix}
\begin{pmatrix}
  ? & ? & ? \\
  ? & ? & ? \\
  ? & ? & ?
\end{pmatrix}
\begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}
$$

1. **To produce $x_1 y_2$:** place $+1$ in the entry where the $x$ component of $\mathbf{v}_1$ ($x_1$) and the $y$ component of $\mathbf{v}_2$ ($y_2$) are multiplied—that is, row 1, column 2.
2. **To produce $-x_2 y_1$:** place $-1$ in the entry where the $y$ component of $\mathbf{v}_1$ ($y_1$) and the $x$ component of $\mathbf{v}_2$ ($x_2$) are multiplied—that is, row 2, column 1.
3. <strong>Everything else:</strong> terms like $x_1 x_2$ and $z$ components never appear in the area formula. Therefore all remaining entries are $0$.

In this way, that antisymmetric matrix that appeared from on high in §2.3 is uniquely determined in the following form:

$$
M = \begin{pmatrix}
  0 & 1 & 0 \\
  -1 & 0 & 0 \\
  0 & 0 & 0
\end{pmatrix}
$$


#### 2.4.4 Introduction of the Tensor Product

Now, if we look closely at the matrix $M$ of this area-measuring device, we see that it is built from the "subtraction" of two parts.

$$
\begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
= \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
- \begin{pmatrix} 0 & 0 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
$$

The first term on the right-hand side is "the matrix whose only nonzero entry is row 1, column 2," and it represents the operation of extracting the $x$ component from $\mathbf{v}_1$ and the $y$ component from $\mathbf{v}_2$ and multiplying them ($x_1 y_2$).

Let us recall the measuring devices from Chapter 1. The measuring device that extracts the $x$ component was $dx$, and the one that extracts the $y$ component was $dy$.
Let us combine these two measuring devices into a new operator: it measures $\mathbf{v}_1$ with $dx$, measures $\mathbf{v}_2$ with $dy$, and multiplies the results. We call this the <strong>tensor product</strong> and write it as $dx \otimes dy$.

$$(dx \otimes dy)(\mathbf{v}_1, \mathbf{v}_2) := dx(\mathbf{v}_1)\,dy(\mathbf{v}_2) = x_1 y_2$$

The tensor product $dx \otimes dy$ may sound intimidating, but there is nothing to fear. In the world of matrix representations, this is nothing more than the operation of **“turning on the switch that sets only the entry in row 1, column 2 to $1$.”**

> <strong>Note</strong> (matrix representation of the tensor product)  
> For readers who like formulas: with $dx = \begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$ and $dy = \begin{pmatrix} 0 & 1 & 0 \end{pmatrix}$, the matrix representation of $dx \otimes dy$ is obtained as the outer product $dx^T dy$: turn the first row vector into a column, place it next to the second row vector, and multiply each column entry by each row entry to fill the matrix. You will probably find this construction in your linear algebra textbook as well.

#### 2.4.5 Completion of the Wedge Product

The preparation is now complete.
The area-measuring device matrix for the $xy$ plane that we derived was obtained by subtracting the "switch for $y_1 x_2$" from the "switch for $x_1 y_2$."

Translating this into the language of measuring devices ($1$-forms), we naturally arrive at a new operator: the **wedge product** $dx \wedge dy$.

$$
dx \wedge dy := dx \otimes dy - dy \otimes dx
$$

The symbol $\wedge$ means "wedge" in English. Applying this definition to vectors gives:

$$
(dx \wedge dy)(\mathbf{v}_1, \mathbf{v}_2) = dx(\mathbf{v}_1)\,dy(\mathbf{v}_2) - dy(\mathbf{v}_1)\,dx(\mathbf{v}_2) = x_1 y_2 - x_2 y_1
$$

Splendid — from combinations of the measuring devices ($1$-forms) of Chapter 1, we have constructed an area-measuring device ($2$-form) systematically.
Because it is built from the subtraction of tensor products, please also notice that <strong>swapping the arguments flips the sign (alternating property)</strong>—Rule 2 from §2.2 is automatically "built in."

#### 2.4.6 The Three Basis $2$-Forms

By the same method, we can also construct the remaining two "biased pairs of glasses."

**Glasses that look at the $yz$ plane:** $dy \wedge dz$

$$
dy \otimes dz - dz \otimes dy = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} - \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}
$$

**Glasses that look at the $zx$ plane:** $dz \wedge dx$

$$
dz \otimes dx - dx \otimes dz = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} - \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}
$$


<strong>That is everything!</strong>

Now let us apply each of the three pairs of glasses one by one to general vectors and see what each one measures.

For general three-dimensional vectors $\mathbf{v}_1 = \begin{pmatrix} x_1 \\ y_1 \\ z_1 \end{pmatrix}$, $\mathbf{v}_2 = \begin{pmatrix} x_2 \\ y_2 \\ z_2 \end{pmatrix}$, we compute according to the definition in §2.4.5 (putting $\mathbf{v}_1$ in the first argument and $\mathbf{v}_2$ in the second):

$$
(dy \wedge dz)(\mathbf{v}_1, \mathbf{v}_2) = y_1 z_2 - z_1 y_2
$$

$$
(dz \wedge dx)(\mathbf{v}_1, \mathbf{v}_2) = z_1 x_2 - x_1 z_2
$$

$$
(dx \wedge dy)(\mathbf{v}_1, \mathbf{v}_2) = x_1 y_2 - x_2 y_1
$$

Each computation is a single subtraction. Whatever the orientation of the vectors, the definition of the wedge product automatically returns the signed value measured by that pair of glasses.

#### 2.4.7 The Meaning of the Three Numbers—Orthogonal Projection onto Each Coordinate Plane

Now, the reader surely expected the following: “If we feed in two vectors and add up the three readings from the three pairs of glasses, we get the area we learned in elementary school, right?”

That is,

$$
\text{Elementary-school area} \stackrel{?}{=} (dy \wedge dz)(\mathbf{v}_1, \mathbf{v}_2) + (dz \wedge dx)(\mathbf{v}_1, \mathbf{v}_2) + (dx \wedge dy)(\mathbf{v}_1, \mathbf{v}_2)
$$

However, <strong>it is not actually that simple</strong>.

When we designed the area-measuring device in §2.2, in the story confined to the $xy$ plane, a <strong>single number</strong> was indeed enough. But for a general parallelogram in three-dimensional space, orientation is not a simple $+/-$ choice. The readings obtained through the three basis $2$-forms (pairs of glasses),
$$A_{yz} = (dy \wedge dz)(\mathbf{v}_1,\mathbf{v}_2),\quad A_{zx} = (dz \wedge dx)(\mathbf{v}_1,\mathbf{v}_2),\quad A_{xy} = (dx \wedge dy)(\mathbf{v}_1,\mathbf{v}_2)$$
do not represent the area of the parallelogram in space itself, but rather the signed areas obtained when it is orthogonally projected onto each coordinate plane.

<strong>Orthogonal projection onto each coordinate plane</strong>—this is the geometric meaning of the three readings. $A_{yz}$ is the signed area of the orthogonal projection of the parallelogram onto the $yz$ plane; $A_{zx}$ is the projection onto the $zx$ plane; and $A_{xy}$ is the projection onto the $xy$ plane.

> <strong>Note</strong> (orthogonal projection)  
> Orthogonal projection means the "shadow" you get when you crush a figure flat onto a plane at right angles. It helps to picture a light source shining straight down onto the plane. For example, under orthogonal projection onto the $xy$ plane, you ignore the $z$ coordinate of the figure and take only the $x,y$ coordinates. From Chapter 3 onward, this book will sometimes call orthogonal projection simply a <strong>shadow</strong>.

So how do we extract the scalar area $S$ of the parallelogram itself from these projected areas? The answer has the same structure as the length of a vector.

The reader probably knows that to extract the "length (scalar)" from a vector $\mathbf{v} = x\hat{e}_x + y\hat{e}_y + z\hat{e}_z$, you compute the square root of the sum of squares of the components, $\sqrt{x^2+y^2+z^2}$. The operation that extracts the scalar area of a parallelogram from the three projected areas has exactly the same form.

$$S = \sqrt{A_{yz}^2 + A_{zx}^2 + A_{xy}^2} = \sqrt{(y_1 z_2 - z_1 y_2)^2 + (z_1 x_2 - x_1 z_2)^2 + (x_1 y_2 - x_2 y_1)^2}$$

This matches exactly the high-school area formula that we called "a painful calculation" in §2.1. We have at last returned safely from the design of an algebraic measuring device all the way to the "number of tiles" from elementary school.

> <strong>Note</strong> (a general $2$-form)  
> The simple sum of the three readings, $(dy \wedge dz + dz \wedge dx + dx \wedge dy)(\mathbf{v}_1,\mathbf{v}_2)$, is also a perfectly good $2$-form that returns a single scalar. However, this value does not agree with the Euclidean area (the area we learned in elementary school). To obtain that, the nonlinear operation of "square root of the sum of squares" is required, and this nonlinearity foreshadows the appearance of the <strong>metric (inner product)</strong> that we will introduce in Chapter 6. It is a structure completely parallel to the fact that the length of a vector, $\sqrt{x^2+y^2+z^2}$, is the square root of the inner product $\mathbf{v}\cdot\mathbf{v}$.

#### 2.4.8 One-Dimensional "Area" (Length) and Zero-Dimensional "Area" (a Point)

Let us lower our viewpoint a little. I said that the operation "square root of the sum of squares of the components" should look familiar—and in fact we already know the same pattern for **one-dimensional figures (line segments)**.

The $1$-forms ($dx, dy, dz$) treated in Chapter 1 were measuring devices that "eat only one vector."
The figure being measured is the vector itself ($\mathbf{v} = x\hat{e}_x + y\hat{e}_y + z\hat{e}_z$), which is data for a one-dimensional oriented measure—an oriented length. The operation that extracts the "scalar length" from this was $\sqrt{x^2+y^2+z^2}$.

So what is a $0$-form?
Since a measuring device that eats $k$ vectors is a $k$-form, a $0$-form is a <strong>"measuring device that eats no vectors at all"</strong>. It needs no input direction (no arrow); you simply place it on the spot and it returns a single scalar (temperature, density, and so on)—in other words, it is just a <strong>"scalar field (function)"</strong>.
The “zero-dimensional figure” in this analogy is simply a point; the value assigned there has only one component, and its magnitude is obtained by taking the absolute value. In standard mathematical language, a $0$-form is a function itself, but when this book says it "measures a point," that is a metaphor for lining up dimensions in a series: it returns a value when placed at that point without needing an input direction.

Point (0-dimensional), line segment (1-dimensional), parallelogram (2-dimensional). All of them were repetitions of the same structure: "eat $k$ vectors and return a scalar."

In §2.5 we will raise this one step further and apply the same structure to a three-dimensional parallelepiped (volume). To summarize:
- $k=0$: a $0$-form measures a point. One component; magnitude is absolute value
- $k=1$: a $1$-form measures a vector (<strong>oriented length</strong>). Three components; magnitude is $\sqrt{x^2+y^2+z^2}$
- $k=2$: a $2$-form measures the parallelogram spanned by two vectors (<strong>oriented area</strong>). Three components; magnitude is $\sqrt{A_{yz}^2+A_{zx}^2+A_{xy}^2}$
- $k=3$: a $3$-form measures the parallelepiped spanned by three vectors (<strong>oriented volume</strong>). One component; magnitude is absolute value

Because the stage of this book is three-dimensional space, we stop at $k=0,1,2,3$, but the principle that "a $k$-form eats $k$ vectors and returns a scalar" does not depend on $k$. This pattern carries forward into integration in Chapter 3 and the exterior derivative in Chapter 5.

#### 2.4.9 Agreement with the Cross Product

Readers who learned the "vector cross product" in university linear algebra will recognize the following three components.

$$\mathbf{v}_1 \times \mathbf{v}_2 = (y_1 z_2 - z_1 y_2)\,\hat{e}_x + (z_1 x_2 - x_1 z_2)\,\hat{e}_y + (x_1 y_2 - x_2 y_1)\,\hat{e}_z = \begin{pmatrix} y_1 z_2 - z_1 y_2 \\ z_1 x_2 - x_1 z_2 \\ x_1 y_2 - x_2 y_1 \end{pmatrix}$$

This is nothing other than the values of $dy \wedge dz$, $dz \wedge dx$, and $dx \wedge dy$ on $(\mathbf{v}_1,\mathbf{v}_2)$, listed in this order.

> <strong>Note</strong> (for uneasy readers)  
> Even if this looks unfamiliar, there is no obstacle to understanding what follows. In this book we simply discovered the wedge product before the cross product.

> <strong>Note</strong> ($2$-forms and the cross product)  
> Area as a $2$-form and the cross product as a three-component vector are related by what we will later call the <strong>Hodge dual</strong>. We will make clear in Chapter 6 why, in Cartesian coordinates, these must inevitably carry the same components; here we will leave it at "different ways of carrying information about oriented area."

---

> <strong>Checkpoint so far</strong>
> - The wedge product $dx \wedge dy := dx \otimes dy - dy \otimes dx$ automatically generates an antisymmetric matrix from the subtraction of tensor products. $dy \wedge dz$ and $dz \wedge dx$ are constructed similarly, and any area-measuring device can be assembled as a linear combination of the three basis $2$-forms.
> - Feeding two vectors $\mathbf{v}_1,\mathbf{v}_2$ into the three basis $2$-forms yields the signed projected areas $A_{yz},A_{zx},A_{xy}$ onto the coordinate planes ($yz$, $zx$, $xy$).
> - The scalar area (the positive magnitude corresponding to the number of tiles) is recovered by the square root of the sum of squares of the projected areas, $\sqrt{A_{yz}^2 + A_{zx}^2 + A_{xy}^2}$, returning to the formula of §2.1 (Lagrange's identity). It is the same kind of operation as the formula for the length of a vector. This nonlinearity foreshadows the metric we will introduce in Chapter 6.

---

### §2.5 Volume-Measuring Devices and Determinants

In the previous section we combined two $1$-forms (measuring devices) $dx, dy$ via the wedge product and assembled the area-measuring device ($2$-form) $dx \wedge dy$. The area-measuring device was a device that “eats two vectors and returns the signed area of the parallelogram they span.”

Now at last we come to <strong>volume</strong>, and here the stance is the same. First we assign volume $1$ to the <strong>standard basis </strong>$\hat{e}_x,\hat{e}_y,\hat{e}_z$<strong> lined up to form a unit cube</strong> (Rule 3), and we define the measuring device by alternativity and linearity. To return to the **positive volume** of elementary school—“how many unit cubes fit inside?”—we take the magnitude of the signed output. In three dimensions this will reduce to an absolute value, the one-component version of the same “square root of a sum of squares” structure we saw for area.

A natural question arises.
**“Can the device that measures the volume of the parallelepiped spanned by three vectors—the volume-measuring device ($3$-form)—also be assembled in the same way?”**

#### 2.5.1 Rules a Volume-Measuring Device Must Satisfy

Let us take exactly the same strategy as when we designed the area-measuring device in §2.2. First we decide “the rules that a volume-measuring device $V$ must satisfy,” and then we uniquely derive the form of the device from those rules.

A volume-measuring device $V(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3)$ is a function that eats three vectors and returns one scalar. The rules we impose on it are obtained by <strong>extending the three rules for the area-measuring device directly to three arguments</strong>:

<strong>Rule 1 (linear in each argument)</strong>
If one vector doubles, the volume doubles; if one input is a sum of vectors, the output splits additively.
$$V(a\mathbf{v}_1 + b\mathbf{u},\; \mathbf{v}_2,\; \mathbf{v}_3) = a\,V(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) + b\,V(\mathbf{u}, \mathbf{v}_2, \mathbf{v}_3)$$
The same holds for the second and third arguments.

<strong>Rule 2 (alternativity — swapping any two arguments flips the sign)</strong>
$$V(\mathbf{v}_2, \mathbf{v}_1, \mathbf{v}_3) = -V(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3)$$
The same for the other pairs. By the same argument as in §2.2, <strong>putting the same vector into two slots always gives zero</strong>—if $\mathbf{v}_1 = \mathbf{v}_2$, then $V(\mathbf{v}_1,\mathbf{v}_1,\mathbf{v}_3) = -V(\mathbf{v}_1,\mathbf{v}_1,\mathbf{v}_3)$, so $V=0$. Geometrically the parallelepiped collapses, but <strong>algebraically alternativity alone forces “collapse to zero.”</strong> This is the same structure as Rule 2 for the two-dimensional area-measuring device.

<strong>Rule 3 (normalization — the unit cube has volume 1)</strong>
$$V(\hat{e}_x, \hat{e}_y, \hat{e}_z) = 1$$

#### 2.5.2 Determining the Form from the Rules — Basis Expansion and Elimination

Let us follow the same procedure as when we derived the matrix for the area-measuring device in §2.3. Expand the three vectors in the basis:
$$\mathbf{v}_1 = x_1 \hat{e}_x + y_1 \hat{e}_y + z_1 \hat{e}_z, \quad \mathbf{v}_2 = x_2 \hat{e}_x + y_2 \hat{e}_y + z_2 \hat{e}_z, \quad \mathbf{v}_3 = x_3 \hat{e}_x + y_3 \hat{e}_y + z_3 \hat{e}_z$$

By Rule 1 (multilinearity), $V(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3)$ expands into $3 \times 3 \times 3 = 27$ terms:
$$V(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) = \sum_i\sum_j\sum_k v_{1i}\,v_{2j}\,v_{3k}\; V(\hat{e}_i, \hat{e}_j, \hat{e}_k)$$

Twenty-seven terms is a lot, but Rule 2 (alternativity) eliminates most of them:
- Every term with a <strong>repeated index is zero</strong> (e.g., $V(\hat{e}_x, \hat{e}_x, \hat{e}_z) = 0$)
- Combinations without repetition are exactly those where $i, j, k$ are all distinct—that is, <strong>permutations</strong> of $(x,y,z)$

There are $3! = 6$ permutations of $(x, y, z)$ in all. By alternativity, even permutations have the same sign as $V(\hat{e}_x, \hat{e}_y, \hat{e}_z)$, and odd permutations have the opposite sign. Rule 3 fixed $V(\hat{e}_x, \hat{e}_y, \hat{e}_z) = 1$, so:

| Permutation | even/odd | value |
|------|-------|----|
| $(x,y,z)$ | even (0 swaps) | $+1$ |
| $(y,z,x)$ | even (2 swaps) | $+1$ |
| $(z,x,y)$ | even (2 swaps) | $+1$ |
| $(y,x,z)$ | odd (1 swap) | $-1$ |
| $(x,z,y)$ | odd (1 swap) | $-1$ |
| $(z,y,x)$ | odd (1 swap) | $-1$ |

Therefore:
$$V(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) = x_1 y_2 z_3 + y_1 z_2 x_3 + z_1 x_2 y_3 - y_1 x_2 z_3 - x_1 z_2 y_3 - z_1 y_2 x_3$$

Readers who have studied linear algebra should recognize this as the <strong>determinant</strong> of the matrix formed by lining up the three vectors as columns:
$$\begin{pmatrix} x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3 \\ z_1 & z_2 & z_3 \end{pmatrix}$$
Readers who do not know it yet may simply <strong>decide to call this six-term sum “the determinant”</strong> and move on—the essential fact is that it fell out of the rules above.

Here is the one point to keep in mind. The determinant is not merely a “procedure of multiplying and subtracting components”; it can also be read as an operator that returns <strong>a single number—the “signed volume” when three column vectors are fed into it in that order</strong>. The $1$-form of Chapter 1 is “one vector → scalar,” the $2$-form of §2.3 is “two vectors → scalar”—the determinant is “three vectors → scalar,” linking this series.

For the area-measuring device an antisymmetric matrix appeared; for the volume-measuring device the determinant appeared—but <strong>in both cases the rules we imposed first determined the algebraic form</strong>.

> <strong>Note</strong> (the order of the six terms of the determinant) Some textbooks simply declare upfront that “the definition of the determinant is these six terms.” In the flow of this book, the order is <strong>rules of the measuring device → six terms</strong>.

#### 2.5.3 Reinterpreting the $2$-form as a Determinant

In fact, a determinant was hiding in the wedge product of the $2$-form defined in §2.4 as well. Let us recall the definition:
$$(dx \wedge dy)(\mathbf{v}_1, \mathbf{v}_2) = dx(\mathbf{v}_1)\,dy(\mathbf{v}_2) - dy(\mathbf{v}_1)\,dx(\mathbf{v}_2)$$

The right-hand side is nothing other than the following $2 \times 2$ determinant:
$$(dx \wedge dy)(\mathbf{v}_1, \mathbf{v}_2) = \det\begin{pmatrix} dx(\mathbf{v}_1) & dx(\mathbf{v}_2) \\ dy(\mathbf{v}_1) & dy(\mathbf{v}_2) \end{pmatrix}$$

In other words, the value of the wedge product is the determinant of the matrix with “which measuring device” across the rows and “which vector” down the columns.

#### 2.5.4 Definition of $dx \wedge dy \wedge dz$ — Completing the Determinant Pattern

Extending this “determinant pattern” straightforwardly to $3 \times 3$ gives us the volume-measuring device.

<strong>Definition:</strong> For three vectors $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$,
$$(dx \wedge dy \wedge dz)(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) := \det\begin{pmatrix} dx(\mathbf{v}_1) & dx(\mathbf{v}_2) & dx(\mathbf{v}_3) \\ dy(\mathbf{v}_1) & dy(\mathbf{v}_2) & dy(\mathbf{v}_3) \\ dz(\mathbf{v}_1) & dz(\mathbf{v}_2) & dz(\mathbf{v}_3) \end{pmatrix}$$

Each entry on the right-hand side is “the coordinate component that one of the $1$-forms $dx$, $dy$, or $dz$ extracts from vector $\mathbf{v}_i$,” so this is exactly:
$$= \det\begin{pmatrix} x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3 \\ z_1 & z_2 & z_3 \end{pmatrix}$$

This agrees completely with the $V$ derived in §2.5.2. **The volume-measuring device can be constructed as the wedge product of the three measuring devices $dx$, $dy$, and $dz$.**

Readers who learned determinants in linear algebra will easily see that this definition satisfies the three rules of §2.5.1:
- <strong>Multilinearity</strong>: the determinant is linear in each column, so this is automatic.
- <strong>Alternativity</strong>: swapping two columns of the determinant flips the sign.
- <strong>Normalization</strong>: inserting $\hat{e}_x, \hat{e}_y, \hat{e}_z$ gives the identity matrix, and $\det(I) = 1$.

#### 2.5.5 Tensor-Product Representation of the Volume-Measuring Device — An Array of Three $3 \times 3$ Blocks Side by Side

In §2.4.4–2.4.5 we saw that the area-measuring device $dx \wedge dy$ can be built as the difference of tensor products $dx \otimes dy - dy \otimes dx$, and that the result is a $3 \times 3$ antisymmetric matrix. Can the same trick be applied to the volume-measuring device $dx \wedge dy \wedge dz$?

Why bring out a tensor array here at all? Because we want to show that <strong>the operation of eating three vectors and returning a determinant can be written with exactly the same idea of “contraction” as for the area-measuring device</strong>. As defined in §2.4.2, contraction is the operation of summing over a shared index and eliminating that index. $1$-forms, $2$-forms, and $3$-forms all run on this single principle.

The answer is yes. However, while tensor products of two measuring devices fit into $3 \times 3$ matrices, with three measuring devices one more index appears and we get a <strong>three-dimensional array</strong> of $3 \times 3 \times 3 = 27$ components. Such a multidimensional array with three indices is called a <strong>tensor</strong> in both mathematics and physics. A matrix (two indices) is a special case of a tensor; what appears here is a <strong>third-order tensor</strong> with three indices.

By the way, for tensors of third order and above, writing out every component makes the page explode, so even physicists rarely use array displays. Instead the usual practice is to write using an indexed representative such as the Levi-Civita epsilon component $\epsilon_{ijk}$, and leave the rest of the calculation to contraction. In this section too we follow that convention and, as needed, pull out individual components to carry the discussion forward.

> <strong>Note</strong> (tensor notation) In tensor algebra, the <strong>notation itself</strong> $\epsilon_{ijk}$ often denotes “the entire third-order tensor” (the Levi-Civita epsilon). To avoid confusion, this book writes the <strong>entire third-order tensor</strong> as $\widehat{\epsilon}$ and a <strong>single component</strong> as $\epsilon_{ijk}$. That is, we distinguish matrix display (the $3\times3$ of §2.3) from “one component” in our notation. Keep this in mind when reading other books.

> <strong>Note</strong> (upper and lower indices) An apology to detailed readers who are peeking ahead. In more advanced differential geometry and tensor analysis, the convention of distinguishing vectors from covectors and bases from dual bases by the <strong>position of upper vs. lower indices</strong> is often used. This book fixes the discussion to <strong>standard Cartesian coordinates</strong>, where the distinction between covector components and vector components does not surface, so we write everything with <strong>lower indices</strong>, as in $\epsilon_{ijk}$.

Now, antisymmetrizing this 27-component array (adding the six permutations with signs) produces an array where only 6 of the 27 entries are $\pm 1$ and the rest are zero. It is exactly the table of permutations derived in §2.5.2—the components are taken as follows (the $(i,j,k)$ component of $\widehat{\epsilon}$):

$$
\epsilon_{ijk} = \begin{cases} +1 & (i,j,k) \text{ is an even permutation of } (x,y,z) \\ -1 & (i,j,k) \text{ is an odd permutation of } (x,y,z) \\ 0 & \text{repeated indices} \end{cases}
$$

How to display these 27 numbers—there is a good way. Think of <strong>three $3 \times 3$ matrices lined up in a row</strong>:

$$
\widehat{\epsilon} \;{=}\;
\begin{pmatrix}
\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix} &
\begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} &
\begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
\end{pmatrix}
$$

The first index $i$ specifies “which slice from the left,” and inside each slice the contents are a $3 \times 3$ block indexed by $j,k$.

<strong>Eating three vectors and collapsing to a scalar — triple contraction</strong>

In formulas it is one line:

$$
V(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) = \sum_i\sum_j\sum_k \epsilon_{ijk}\, v_{1i}\, v_{2j}\, v_{3k}
$$

This is a <strong>triple contraction</strong>. We sum over all three indices $i, j, k$ and build a single scalar from the 27-component array and three vectors. It is the natural extension of $\mathbf{v}_1^T M \mathbf{v}_2$ (double contraction) from §2.4.2.

Viewing this triple contraction in two stages makes the structure even clearer:

- <strong>Step 1 (contract over index $i$ → matrix):</strong> Contract $\mathbf{v}_1$ and $\widehat{\epsilon}$ over index $i$. $\displaystyle M = \sum_{i=1}^3 v_{1i}\,\epsilon_{i,\cdot,\cdot}$ ($\epsilon_{i,\cdot,\cdot}$ is the $i$th $3 \times 3$ block of $\widehat{\epsilon}$ from the left). The result drops down to a single $3 \times 3$ matrix $M$. This $M$ is precisely the matrix of the area-measuring device constructed in §2.4.5–2.4.6:

| $i$th slice from the left | identity |
|:---:|:---:|
| $i=1$ | $dy \wedge dz$ (area-measuring device for the $yz$ plane) |
| $i=2$ | $dz \wedge dx$ (area-measuring device for the $zx$ plane) |
| $i=3$ | $dx \wedge dy$ (area-measuring device for the $xy$ plane) |

- <strong>Step 2 (contract over indices $j,k$ → scalar):</strong> Sandwich the resulting matrix $M$ with $\mathbf{v}_2, \mathbf{v}_3$ and contract— $V = \mathbf{v}_2^T M \mathbf{v}_3$. An operation we are already familiar with from §2.4.

In Appendix A, we write out every component and confirm that this two-stage contraction reproduces all six terms of the determinant from §2.5.2.


#### 2.5.6 Example: Signed Volume of a Parallelepiped

Let us verify by hand. Add a third vector to the two whose area we measured in §2.4.6:

$$\mathbf{v}_1 = \begin{pmatrix}1\\0\\1\end{pmatrix}, \quad \mathbf{v}_2 = \begin{pmatrix}0\\1\\1\end{pmatrix}, \quad \mathbf{v}_3 = \begin{pmatrix}1\\1\\0\end{pmatrix}$$

Feed them into the volume-measuring device:
$$(dx \wedge dy \wedge dz)(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3) = \det\begin{pmatrix}1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0\end{pmatrix}$$

Computing according to the definition:
$$= 1\cdot1\cdot0 + 0\cdot1\cdot1 + 1\cdot0\cdot1 - 1\cdot1\cdot1 - 0\cdot0\cdot0 - 1\cdot1\cdot1 = 0 + 0 + 0 - 1 - 0 - 1 = -2$$

> <strong>Note</strong> (negative volume?)
> As with oriented area in §2.2, <strong>the order</strong> can yield a minus sign.

Let us try swapping $\mathbf{v}_1$ and $\mathbf{v}_2$:
$$(dx \wedge dy \wedge dz)(\mathbf{v}_2, \mathbf{v}_1, \mathbf{v}_3) = -(-2) = +2$$

#### 2.5.7 Agreement with the Scalar Triple Product

Readers who learned the “scalar triple product” in vector analysis may know the following identity:
$$\mathbf{v}_1 \cdot (\mathbf{v}_2 \times \mathbf{v}_3) = \det\begin{pmatrix}x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3 \\ z_1 & z_2 & z_3\end{pmatrix}$$

The right-hand side is exactly the $(dx \wedge dy \wedge dz)(\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3)$ we defined.

> <strong>Note</strong> (borrowing the dot product symbol early) The “$\cdot$” on the left is the symbol for the <strong>dot product</strong>; here we use it in the familiar coordinate-calculation sense of “sum of products of corresponding components.” In Chapter 6 we will give a formal definition using the metric $g$.

#### 2.5.8 Output of the Volume-Measuring Device — Only One Independent Component

The $dx \wedge dy \wedge dz$ we assembled is a **volume-measuring device ($3$-form)** waiting for three vectors. Unlike the area-measuring device that eats two vectors, feeding three vectors into the volume-measuring device yields a single signed scalar $V$ (because, as we will see in §2.5.9, a $3$-form has only one independent component).

If we want the positive elementary-school volume—the scalar volume “how many unit cubes fit inside?”—we take the magnitude of the signed output. Since a $3$-form in three-dimensional space has only one independent component, this is simply $|V|=\sqrt{V^2}$. As with area, this nonlinear operation requires a metric; we will treat it again in Chapter 6.

#### 2.5.9 The “Size” of a $3$-form — Why Is There Only One Independent Component?

An area-measuring device ($2$-form) could be represented by a $3 \times 3$ antisymmetric matrix, with 3 independent components (the coefficients of $dy \wedge dz$, $dz \wedge dx$, $dx \wedge dy$).

How many independent components does a volume-measuring device ($3$-form) have? Consider the candidates we can build as basis $3$-forms. The number of ways to choose three measuring devices $dx, dy, dz$ <strong>without repetition</strong> is … only one. Just $dx \wedge dy \wedge dz$ (changing the order only changes the sign; it does not produce a new basis).

> <strong>Note</strong> (foreshadowing the Hodge dual) For area, feeding two vectors into the three basis $2$-forms gave three numbers, and obtaining scalar area required a nonlinear operation (square root of a sum of squares). By contrast, the output of the volume-measuring device $dx \wedge dy \wedge dz$ is a single scalar $V$ from the start. And this is no accident. A $0$-form (scalar field) also has 1 independent component, a $1$-form has 3, and a $2$-form has 3—that is, $1, 3, 3, 1$, mirrored from both ends. This sequence is a foreshadowing of the symmetry called the <strong>Hodge dual</strong>. We will go into detail in a later chapter.

#### 2.5.10 Hierarchy of Measuring Devices — Organizing the Weapons Gained in Chapter 2

Here let us survey the overall picture of the “measuring devices” we have built up since Chapter 1.

From §2.4.8 onward, and especially through §2.5.8 and §2.5.9 (the number of independent components), we have seen that <strong>for each dimension $k$, the same pattern repeats: “a $k$-form eats $k$ vectors and returns a scalar.”</strong> Collecting the number of data components and the operation that extracts the ordinary scalar magnitude, we get:

| dimension ($k$) | measuring device ($k$-form) | what it measures | number of components | how to extract scalar magnitude |
| :--- | :--- | :--- | :--- | :--- |
| <strong>0-dimensional</strong> | $0$-form (scalar field $f$) | point | 1 component ($f$) | $\sqrt{f^2}$  |
| <strong>1-dimensional</strong> | $1$-form ($dx, dy, dz$) | vector (line segment) | 3 components ($x, y, z$) | $\sqrt{x^2 + y^2 + z^2}$ |
| <strong>2-dimensional</strong> | $2$-form ($dy \wedge dz$, etc.) | parallelogram | 3 components | $\sqrt{A_{yz}^2 + A_{zx}^2 + A_{xy}^2}$ |
| <strong>3-dimensional</strong> | $3$-form ($dx \wedge dy \wedge dz$) | parallelepiped spanned by three vectors | 1 component ($V$) | $\sqrt{V^2}$ |

> <strong>Checkpoint so far</strong>
> - The volume-measuring device $dx \wedge dy \wedge dz$ ($3$-form) is the wedge product of three measuring devices, and its value equals a $3 \times 3$ determinant.
> - There is a $1, 3, 3, 1$ symmetry: $0$-form (1 component) → $1$-form (3 components) → $2$-form (3 components) → $3$-form (1 component).
> - No matter the dimension, the principle is the same: a $k$-form eats $k$ vectors and returns a scalar. When we want the ordinary positive magnitude, we extract it by the appropriate “square root of a sum of squares” operation; in the one-component cases this reduces to an absolute value.


---

### §2.6 Summary of This Chapter and Outlook Toward Chapter 3

> <strong>Checkpoint so far — Chapter 2 as a whole</strong>
> - Area is a $2$-form, an antisymmetric matrix that measures the “pairing of two vectors”; the physical rules completely determine the form of the matrix.
> - The wedge product $\wedge$ is the operation that builds an antisymmetric matrix by “subtracting tensor products.” By attaching field coefficients to the three basis $2$-forms, we assemble a general $2$-form (the meaning of the coefficients comes in later chapters).
> - The volume-measuring device $dx \wedge dy \wedge dz$ ($3$-form) is the wedge product of three measuring devices, and its value equals a $3 \times 3$ determinant. It can also be expressed by contraction with the antisymmetrized $\widehat{\epsilon}$ (components $\epsilon_{ijk}$, the Levi-Civita symbol) (verify all components in Appendix A).

In this chapter, starting from the measuring devices $dx$, $dy$, and $dz$ set up in Chapter 1, we have reached the point of **building area ($2$-forms) and volume ($3$-forms) algebraically**. The wedge product is not a tool for “drawing geometry directly”; it is a tool for <strong>mechanically generating formulas that satisfy the rules of measuring devices</strong>.

In the next chapter (Chapter 3), we will <strong>aggregate these forms over curves, surfaces, and regions</strong>—that is, rewrite line integrals, surface integrals, and volume integrals in a unified language of $1$-forms / $2$-forms / $3$-forms. Variable changes and <strong>pullback</strong> will also appear, and the Jacobian will arise naturally as the “calculation of shadows.”

---

## Appendix A: Tensor-Product Representation of the Volume-Measuring Device — Full Component Calculation

In §2.5.5 we stated that contraction of $\widehat{\epsilon}$ (components $\epsilon_{ijk}$) with three vectors agrees with the determinant. Here we follow that entire process by hand calculation and verify it term by term.

#### A.1 Extension of the Tensor Product to Three Arguments

Let us review. The $(i,j)$ component of $dx \otimes dy$ was the product of the $i$th component of $dx$ and the $j$th component of $dy$:
$$(dx \otimes dy)_{ij} = (dx)_i\,(dy)_j$$

Extension to three measuring devices is natural—we merely add one more index:
$$(dx \otimes dy \otimes dz)_{ijk} = (dx)_i\,(dy)_j\,(dz)_k$$

After substituting $dx=(1\ 0\ 0)$, $dy=(0\ 1\ 0)$, and $dz=(0\ 0\ 1)$, only one of the $3^3=27$ cells is nonzero: the entry at $(i,j,k)=(1,2,3)$ is $1$. The remaining 26 cells are $0$. Each of the other five permutations ($dx \otimes dz \otimes dy$, and so on) is likewise nonzero in exactly one place—for $dy \otimes dx \otimes dz$ the $1$ sits at $(2,1,3)$, and for $dz \otimes dy \otimes dx$ at $(3,2,1)$.

#### A.2 Antisymmetrization — Superposing Six Permutations with Signs

In §2.4.5, for area we had $dx \wedge dy = dx \otimes dy - dy \otimes dx$ (a signed sum of two terms). The three measuring devices are $dx, dy, dz$ in Cartesian coordinates. There are $3! = 6$ permutations, For each permutation $\sigma$, we arrange $(dx,dy,dz)$ in the permuted order, join them with tensor products $\otimes$, attach the sign $\mathrm{sgn}(\sigma)$, and sum over $S_3$—that is, the following six-line sum written in one line in the language of permutations.

> <strong>Note</strong> (symmetric group and sign of a permutation)
> $S_3$ is the symmetric group of degree 3 (the set of permutations). $\mathrm{sgn}(\sigma)$ is defined to be <strong>$+1$ for an even permutation</strong> and <strong>$-1$ for an odd permutation</strong>.

Written out:

$$\underbrace{dx \otimes dy \otimes dz}_{(1,2,3)\text{ with }+1} - \underbrace{dx \otimes dz \otimes dy}_{(1,3,2)\text{ with }-1} + \underbrace{dy \otimes dz \otimes dx}_{(2,3,1)\text{ with }+1}$$
$$- \underbrace{dy \otimes dx \otimes dz}_{(2,1,3)\text{ with }-1} + \underbrace{dz \otimes dx \otimes dy}_{(3,1,2)\text{ with }+1} - \underbrace{dz \otimes dy \otimes dx}_{(3,2,1)\text{ with }-1}$$

Superposing these six “arrays with only one nonzero entry” with signs leaves only 6 of the 27 components at $\pm 1$; the other 21 are zero. Compare with the permutation table in §2.5.2—this is the construction principle that yields each component $\epsilon_{ijk}$ of $\widehat{\epsilon}$.

#### A.3 Writing Down the Matrix for Each Component

Let us verify cell by cell the three component matrices shown in §2.5.5.

**Component 1 ($i=1$, $x$):** among the six terms, those with $i = 1$ are $+1$ at $(1,2,3)$ and $-1$ at $(1,3,2)$.

$$\epsilon_{1,\cdot,\cdot} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}$$

**Component 2 ($i=2$, $y$):** $+1$ at $(2,3,1)$ and $-1$ at $(2,1,3)$.

$$\epsilon_{2,\cdot,\cdot} = \begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$$

**Component 3 ($i=3$, $z$):** $+1$ at $(3,1,2)$ and $-1$ at $(3,2,1)$.

$$\epsilon_{3,\cdot,\cdot} = \begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

To repeat: these are exactly the matrices of $dy \wedge dz$, $dz \wedge dx$, and $dx \wedge dy$, respectively.

#### A.4 Feeding Three Vectors — The Full Contraction Process

**Step 1: weighted sum over index $i$ using the components of $\mathbf{v}_1$ (collapse index $i$)**

Add the three area-measuring-device matrices, weighted by the components of $\mathbf{v}_1$. One vector is fed in and the $3$-dimensional array drops to a $3 \times 3$ matrix:

$$M := \sum_i v_{1i}\, \epsilon_{i,\cdot,\cdot} = x_1 \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix} + y_1 \begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} + z_1 \begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

Adding component by component gives:

$$M = \begin{pmatrix} 0 & z_1 & -y_1 \\ -z_1 & 0 & x_1 \\ y_1 & -x_1 & 0 \end{pmatrix}$$

An area-measuring device specialized to $\mathbf{v}_1$ has appeared, built from the three area-measuring devices weighted by the components of $\mathbf{v}_1$. Note that it is an antisymmetric matrix—the antisymmetry in the indices of $\widehat{\epsilon}$ is inherited.

**Step 2: sandwich the matrix with the remaining two vectors (collapse indices $j,k$)**

What remains is the familiar “row $\times$ matrix $\times$ column” from §2.4:

$$V = \mathbf{v}_2^T\, M\, \mathbf{v}_3 = \begin{pmatrix} x_2 & y_2 & z_2 \end{pmatrix} \begin{pmatrix} 0 & z_1 & -y_1 \\ -z_1 & 0 & x_1 \\ y_1 & -x_1 & 0 \end{pmatrix} \begin{pmatrix} x_3 \\ y_3 \\ z_3 \end{pmatrix}$$

First compute $\mathbf{v}_2^T \times M$ (row $\times$ matrix → row):

$$= \begin{pmatrix} y_1 z_2 - z_1 y_2, & z_1 x_2 - x_1 z_2, & x_1 y_2 - x_2 y_1 \end{pmatrix}$$

Finally, the sum of products of corresponding components of the resulting row vector and $\mathbf{v}_3$ (row $\times$ column → scalar):

$$V = (y_1 z_2 - z_1 y_2)\,x_3 + (z_1 x_2 - x_1 z_2)\,y_3 + (x_1 y_2 - x_2 y_1)\,z_3$$

Expanding and collecting terms gives:

$$= x_1 y_2 z_3 + y_1 z_2 x_3 + z_1 x_2 y_3 - y_1 x_2 z_3 - x_1 z_2 y_3 - z_1 y_2 x_3$$

This **matches the determinant in §2.5.2 term for term—all six terms agree.**

# Chapter 3: What Does It Mean to Integrate? — Count Finite Masses, Then Take the Limit

# Chapter 3: What Does It Mean to Integrate? — Count Finite Masses, Then Take the Limit

### §3.0 Measuring Curved Things — Paying Back a Debt from Elementary School

In Chapter 2, we defined how to measure <strong>flat figures</strong> such as the area of a parallelogram and the volume of a parallelepiped.

If we feed two vectors to the area-measuring device $dx \wedge dy$, we get a signed area; if we feed three vectors to the volume-measuring device $dx \wedge dy \wedge dz$, we get a signed volume. We redesigned the elementary-school intuition of “how many $1\times 1$ squares fit inside” as algebraic measuring devices.

However, a debt from elementary school still remains.

We have used the circumference $2\pi r$, the surface area of a sphere $4\pi r^2$, and the volume of a sphere $\frac{4}{3}\pi r^3$ for a long time as “formulas of that kind.” But where do they actually come from?

There is only one answer.

<strong>Chop into finite small pieces, measure each one, add them up, and finally make the mesh infinitely fine.</strong>

That is integration.

The purpose of this chapter is not to memorize the formulas for a sphere again. Rather, using the familiar sphere as our example, we confirm at the level of Riemann sums what it means to “integrate.”

Therefore, we deliberately do not escape immediately into polar or spherical coordinates. We count small pieces in $x,y,z$, decide which pieces belong to the target, and organize the sum. It is messy — but this messiness is the substance of integration.

Now, on our desk we have the measuring devices built in Chapters 1 and 2: $0$-forms, $1$-forms, $2$-forms, and $3$-forms. The job of this chapter is to <strong>apply them to curves, surfaces, and regions and aggregate the results</strong>.

The principle is the same at every degree. We begin with the case where a volume-measuring device with coefficient $1$ returns the volume of a region directly, then step down in dimension and check “what does the form measure, and what does it not measure?”

> <strong>Note</strong> (ground rules)  
> We state this up front as a promise. Below, we treat curves and surfaces as sufficiently smooth, and cases where chopping into small pieces and adding converges in a straightforward way. Details such as orientation reversal and self-intersection are kept at the level of “they do not cause trouble in situations commonly used in physics.” A rigorous theory of integrability is outside the scope of this book.


> <strong>Checkpoint so far</strong>
> - The integral of $dx \wedge dy \wedge dz$ is the limit of a Riemann sum that chops a region into small boxes and adds the values obtained by feeding each volume element to the volume-measuring device. $\iiint_V$ is the symbol this book gives to that limit.
> - With coefficient $1$, volume is measured directly. The sphere volume $\frac{4}{3}\pi R^3$ is obtained by organizing the Riemann sum in the order $x \to y \to z$. No special coordinate system is needed.
> - In the next section we drop one dimension and measure the area of a surface.

---

### §3.2 Surface Area — The Limit of Two Dimensions, Coefficient 1

#### 3.2.1 From Parallelograms to Surfaces

In Chapter 2 §2.4, we assembled the area-measuring device $dx \wedge dy$. If we feed it two vectors $\mathbf{v}_1, \mathbf{v}_2$, we get the signed area of the shadow they cast onto the $xy$ plane. Likewise, $dy \wedge dz$ measures the shadow onto the $yz$ plane, and $dz \wedge dx$ measures the shadow onto the $zx$ plane.

So how do we measure the area of a surface? Let us first check the flat case. Take a unit square lying in the $xy$ plane and chop it into fine small squares. The two edges of one small square are

$$\Delta\mathbf{x}=\begin{pmatrix}\Delta x\\0\\0\end{pmatrix},\qquad
\Delta\mathbf{y}=\begin{pmatrix}0\\\Delta y\\0\end{pmatrix}.$$

Feed these to $dx \wedge dy$:

$$(dx \wedge dy)(\Delta\mathbf{x},\Delta\mathbf{y})=\Delta x\,\Delta y.$$

Adding over all small squares gives area $1$. This is nothing more than the extension of the flat parallelogram from Chapter 2. What we are confirming here is that the $2$-form $dx\wedge dy$ returns the signed area of a small piece on the $xy$ plane directly.

What if the surface is curved? Chop the surface into sufficiently fine small pieces. On each piece, write the displacement vectors in two adjacent directions as $\Delta\mathbf{a},\Delta\mathbf{b}$. In this chapter we call these two displacement vectors, or the oriented infinitesimal parallelogram they span, a <strong>surface element</strong> of the surface. The finer we chop the surface, the more closely the aggregate of these surface elements approximates the surface itself.

Feed the two displacement vectors $\Delta\mathbf{a},\Delta\mathbf{b}$ that span this small piece of surface to the area-measuring device $dx \wedge dy$. From the definition in Chapter 2 §2.4.4, if

$$\Delta\mathbf{a}=\begin{pmatrix}\Delta a_x\\\Delta a_y\\\Delta a_z\end{pmatrix},\qquad
\Delta\mathbf{b}=\begin{pmatrix}\Delta b_x\\\Delta b_y\\\Delta b_z\end{pmatrix},$$

then

$$(dx \wedge dy)(\Delta\mathbf{a},\Delta\mathbf{b})
=\Delta a_x\Delta b_y-\Delta a_y\Delta b_x.$$

This is the signed area of the shadow that small piece casts onto the $xy$ plane.

We <strong>write</strong> the limit as the mesh becomes infinitely fine as

$$\iint_S dx \wedge dy.$$

This is the definition of integration of a $2$-form — a surface integral. The structure is the same type as the volume integral in §3.1; only the number of vectors fed in has dropped from three to two.

#### 3.2.2 What $dx \wedge dy$ Measures — A Test on the Sphere

Let us actually compute on a sphere. Consider the upper half of a sphere of radius $R$ ($z \ge 0$). A point $(x,y,z)$ on the sphere satisfies

$$x^2+y^2+z^2=R^2,\qquad z=\sqrt{R^2-x^2-y^2}.$$

Here we use the total differential defined in Chapter 1. The total differential of the function

$$F(x,y,z)=x^2+y^2+z^2$$

is

$$dF=2x\,dx+2y\,dy+2z\,dz.$$

As promised in Chapter 1, this is a row vector that eats a displacement vector and reads off the first-order change in $F$. If the displacement vector is tangent to the sphere, then to first order it does not change the value of $F=x^2+y^2+z^2$. Therefore that displacement vector $\mathbf{v}$ satisfies $dF(\mathbf{v})=0$. We choose the two displacement vectors that span a small piece of the sphere to satisfy this condition as well.

For example, take the displacement vector that holds $y$ fixed and advances a small amount $\Delta x$ in the $x$ direction:

$$\Delta\mathbf{x}_S=\begin{pmatrix}\Delta x\\[2pt]0\\[2pt]\Delta z\end{pmatrix}.$$

Feed this to $dF$:

$$dF(\Delta\mathbf{x}_S)=2x\,\Delta x+2z\,\Delta z.$$

Choosing this as a tangent displacement along the sphere, so that $dF(\Delta\mathbf{x}_S)=0$, gives $\Delta z=-(x/z)\Delta x$. Likewise, for the displacement vector that holds $x$ fixed and advances a small amount $\Delta y$ in the $y$ direction, we get $\Delta z=-(y/z)\Delta y$.

Therefore the two displacement vectors that span a small piece of the sphere can be written as

$$\Delta\mathbf{x}_S=\begin{pmatrix}\Delta x\\[2pt]0\\[2pt]-\dfrac{x}{z}\Delta x\end{pmatrix},\qquad
\Delta\mathbf{y}_S=\begin{pmatrix}0\\[2pt]\Delta y\\[2pt]-\dfrac{y}{z}\Delta y\end{pmatrix}.$$

If we chop the surface sufficiently finely, the aggregation of the parallelograms spanned by these two vectors approaches the aggregation of the sphere itself.

Let us first feed only $dx \wedge dy$ to the surface:

$$(dx \wedge dy)(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S)=\Delta x\,\Delta y.$$

Therefore the integral over the upper hemisphere,

$$
\iint_{S_{\text{upper}}} dx \wedge dy,
$$

can be computed by the same method as the $y$ integral in §3.1.2, and the result is $\pi R^2$. This is nothing other than the area of the shadow cast by the upper hemisphere onto the $xy$ plane — a disk of radius $R$.

The same calculation works for the lower hemisphere ($z = -\sqrt{R^2 - x^2 - y^2}$). However, if we measure the entire sphere with outward orientation, the orientation of the surface flips on the lower hemisphere and the sign reverses, so the integral becomes $-\pi R^2$.

Therefore the integral of $dx \wedge dy$ over the entire sphere is $\pi R^2 + (-\pi R^2) = 0$. The shadow of the upper hemisphere and the shadow of the lower hemisphere cancel each other. This tells us exactly what $dx \wedge dy$ measures: <strong>the signed area of the shadow onto the $xy$ plane, not the scalar area of the surface.</strong> Likewise, $dy \wedge dz$ measures the shadow onto the $yz$ plane, and $dz \wedge dx$ measures the shadow onto the $zx$ plane.

#### 3.2.3 From Three Shadows to Scalar Area

So how do we measure the scalar area of a surface (the area we learned in elementary school)? On each small patch, feed the two displacement vectors that form the surface element to all three area-measuring devices, and combine the results.

Let us compute the remaining two on the upper hemisphere as well. Feeding the two displacement vectors from above,

$$\Delta\mathbf{x}_S=\begin{pmatrix}\Delta x\\0\\-\dfrac{x}{z}\Delta x\end{pmatrix},\qquad
\Delta\mathbf{y}_S=\begin{pmatrix}0\\\Delta y\\-\dfrac{y}{z}\Delta y\end{pmatrix},$$

to the three area-measuring devices gives:

$$\begin{aligned}
(dy \wedge dz)(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S) &= \frac{x}{z}\,\Delta x\,\Delta y
= \frac{x}{\sqrt{R^2-x^2-y^2}}\,\Delta x\,\Delta y \\[4pt]
(dz \wedge dx)(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S) &= \frac{y}{z}\,\Delta x\,\Delta y
= \frac{y}{\sqrt{R^2-x^2-y^2}}\,\Delta x\,\Delta y \\[4pt]
(dx \wedge dy)(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S) &= \Delta x\,\Delta y
\end{aligned}$$

The three readings $A_{yz},A_{zx},A_{xy}$ are the signed projected areas of the surface element onto the three coordinate planes. Taken together, these three components record the information of the oriented infinitesimal area. This is the surface version of the story from Chapter 2 §2.4.6, where we read the oriented area of a parallelogram as three projected areas.

From here we want to extract the positive area with orientation discarded. So in this chapter we call

$$
dS(\Delta\mathbf{a},\Delta\mathbf{b})
= \sqrt{A_{yz}^2+A_{zx}^2+A_{xy}^2}
$$

the <strong>scalar surface element</strong> of that small patch.

This is not a $2$-form. Whereas $dx\wedge dy$ eats the two displacement vectors that form a surface element and returns a single projected area, $dS$ is notation that combines the three projected areas by the familiar square root of a sum of squares in orthogonal Cartesian coordinates and returns a positive area with orientation discarded.

However, before we simply add up $dS$, let us see what happens if we integrate each of the three area-measuring devices separately over the entire upper hemisphere. Writing the disk $D=\{(x,y)\mid x^2+y^2\le R^2\}$ that is the shadow of the upper hemisphere onto the $xy$ plane, the three signed shadow areas become the following three integrals:

$$\begin{aligned}
\iint_{S_{\text{upper}}} dy\wedge dz
&= \int_{-R}^{R}\int_{-\sqrt{R^2-x^2}}^{\sqrt{R^2-x^2}}
\frac{x}{\sqrt{R^2-x^2-y^2}}\,dy\,dx, \\[4pt]
\iint_{S_{\text{upper}}} dz\wedge dx
&= \int_{-R}^{R}\int_{-\sqrt{R^2-x^2}}^{\sqrt{R^2-x^2}}
\frac{y}{\sqrt{R^2-x^2-y^2}}\,dy\,dx, \\[4pt]
\iint_{S_{\text{upper}}} dx\wedge dy
&= \int_{-R}^{R}\int_{-\sqrt{R^2-x^2}}^{\sqrt{R^2-x^2}}
1\,dy\,dx.
\end{aligned}$$

These three integrals measure the signed shadow areas onto the $yz$ plane, the $zx$ plane, and the $xy$ plane, respectively. In fact, by symmetry the first two are $0$ and the last is $\pi R^2$:

$$
\iint_{S_{\text{upper}}} dy\wedge dz=0,\qquad
\iint_{S_{\text{upper}}} dz\wedge dx=0,\qquad
\iint_{S_{\text{upper}}} dx\wedge dy=\pi R^2.
$$

Note: taking the square root of the sum of squares of these three integral values afterward does <strong>not</strong> give the area of the upper hemisphere. We must combine the three shadows <strong>on each small patch</strong> before adding them up; otherwise the information about the tilt of the surface is lost along the way.

Therefore, to obtain surface area, on each small patch we find the three projected areas, build the scalar surface element $dS$ from them, and add those up. Writing the three projected areas from above as

$$\begin{aligned}
A_{yz} &= (dy \wedge dz)(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S) \\
A_{zx} &= (dz \wedge dx)(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S) \\
A_{xy} &= (dx \wedge dy)(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S)
\end{aligned}$$

the scalar surface element is

$$
dS(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S)
= \sqrt{A_{yz}^2+A_{zx}^2+A_{xy}^2}.
$$

Substituting the three outputs we computed above,

$$\begin{aligned}
dS(\Delta\mathbf{x}_S,\Delta\mathbf{y}_S)
&= \sqrt{
\Bigl(\frac{x}{\sqrt{R^2-x^2-y^2}}\Delta x\,\Delta y\Bigr)^2
{}+ \Bigl(\frac{y}{\sqrt{R^2-x^2-y^2}}\Delta x\,\Delta y\Bigr)^2
{}+ (\Delta x\,\Delta y)^2} \\[4pt]
&= \sqrt{\frac{x^2+y^2}{R^2-x^2-y^2}+1}\;\Delta x\,\Delta y \\[4pt]
&= \frac{R}{\sqrt{R^2-x^2-y^2}}\,\Delta x\,\Delta y
\end{aligned}$$

That is, if we chop the disk $x^2+y^2 \le R^2$ — the shadow of the upper hemisphere onto the $xy$ plane — into small patches, the Riemann sum for the area becomes

$$\sum_i\sum_j
\frac{R}{\sqrt{R^2-x_i^2-y_j^2}}\,
\Delta x_i\,\Delta y_j.$$

In other words, we are simply adding up the scalar surface element on each small patch in the form

$$\sum_i\sum_j dS(\Delta\mathbf{x}_{S,ij},\Delta\mathbf{y}_{S,ij}).$$

In the limit as the mesh becomes fine:

$$
\operatorname{Area}(S_{\text{upper}})
= R\int_{-R}^{R}\biggl(\int_{-\sqrt{R^2-x^2}}^{\sqrt{R^2-x^2}}
\frac{dy}{\sqrt{R^2 - x^2 - y^2}}\biggr)\;dx.
$$

The inner $y$ integral. Set $a = \sqrt{R^2 - x^2}$:

$$\int_{-a}^{a} \frac{dy}{\sqrt{a^2 - y^2}}.$$

Use the substitution $y = a\sin t$ (the same procedure as in §3.1.2). We have $dy = a\cos t\,dt$, $\sqrt{a^2 - y^2} = a\cos t$, and as $y$ goes from $-a$ to $a$, $t$ goes from $-\pi/2$ to $\pi/2$:

$$\int_{-a}^{a} \frac{dy}{\sqrt{a^2 - y^2}} = \int_{-\pi/2}^{\pi/2} \frac{a\cos t}{a\cos t}\,dt = \int_{-\pi/2}^{\pi/2} dt = \pi.$$

The integral is $\pi$ regardless of $a$. Therefore:

$$R\int_{-R}^{R} \pi\,dx = R \cdot \pi \cdot 2R = 2\pi R^2.$$

This is the area of the upper hemisphere. On the lower hemisphere as well, some projected-area signs flip under the outward orientation, but the sum of squares is the same, so again we get $2\pi R^2$. Therefore the area of the entire sphere is:

$$2\pi R^2 + 2\pi R^2 = 4\pi R^2.$$

Splendid — $4\pi R^2$ appears. It is <strong>exactly the same pattern</strong> as when we recovered the area of a parallelogram from three shadows in Chapter 2 §2.4.7.

#### 3.2.4 What We Have Learned So Far

A basis $2$-form with coefficient $1$ does not, by itself, directly return the scalar area of a surface. $dx \wedge dy$ measures the signed projected area of a small piece of surface onto the $xy$ plane. To obtain the scalar area of a surface, we must combine the three projected components on each small piece to build the scalar surface element $dS$, and then add those up. This is exactly the same situation as for the area of a parallelogram in Chapter 2.

However, in physics we often want to control “which shadow to emphasize, and by how much, at each point.” For example, when measuring fluid flow through a surface, if the flow is strong in the $x$ direction we want to put a large weight on $dy \wedge dz$ (the shadow onto the $yz$ plane). The need for such <strong>weights that vary from place to place</strong> — coefficients — naturally appears here. This is foreshadowing for §3.4.

> <strong>Checkpoint so far</strong>
> - A surface integral is the operation of feeding the two displacement vectors that form a surface element on each small patch to an area-measuring device and aggregating the scalars obtained.
> - $dx \wedge dy$ by itself measures the signed area of the shadow onto the $xy$ plane. Over the entire sphere the net result is zero (the shadows of the upper and lower hemispheres cancel).
> - Combining the readings of the three basis $2$-forms by the square root of a sum of squares on each small piece gives the scalar surface element $dS$. Adding these up yields the scalar area of the surface. For a sphere, $4\pi R^2$.
> - In the next section we drop the dimension further and measure the length of a curve. There the limit of coefficient $1$ appears most clearly.

---

### §3.3 Curves — The Limit of One Dimension, Coefficient 1, Revealed

#### 3.3.1 From Straight Lines to Curves — Defined by Riemann Sums

In Chapter 1, we defined $dx, dy, dz$ as $1$-forms (measuring devices) that eat a vector and return each component. When $dx = \begin{pmatrix}1&0&0\end{pmatrix}$ and $\mathbf{v} = \begin{pmatrix}\Delta x\\\Delta y\\\Delta z\end{pmatrix}$, we have $dx(\mathbf{v}) = \Delta x$. The same holds for $dy$ and $dz$.

So what do we get if we apply these along a curve and aggregate the results?

First, chop the curve into small subintervals. To each subinterval there corresponds a displacement vector from start to end,

$$
\Delta\mathbf{r}_i=(\Delta x_i,\Delta y_i,\Delta z_i)
$$

At this stage we do not yet need to write the curve as a formula. On each subinterval, if we feed $dx$ this displacement vector,

$$dx(\Delta\mathbf{r}_i)=\Delta x_i$$

Similarly, $dy(\Delta\mathbf{r}_i)=\Delta y_i$ and $dz(\Delta\mathbf{r}_i)=\Delta z_i$.

Summing over all subintervals gives

$$
\sum_i dx(\Delta\mathbf{r}_i)=\sum_i \Delta x_i
$$

This is nothing but the straightforward sum of the $x$-direction displacements of each small piece along the curve. We <strong>write</strong> the limit as the mesh is made infinitely fine as

$$\int_\gamma dx$$

This is the definition of integration of a $1$-form — a line integral.

So the definition is in place. How do we actually compute this sum?

Introducing $t$ here is not abandoning our policy so far. In §3.1 we organized small rectangular boxes inside a sphere in the order $z,y,x$; in §3.2 we organized small pieces on a sphere by projection onto the $xy$ plane. Likewise, on a curve we need a label to arrange the small pieces in order from start to end. We simply call that label $t$.

So we assign a continuous index $t$ to each small piece along the curve and write

$$\gamma(t) = \bigl(x(t),\, y(t),\, z(t)\bigr),\qquad t \in [t_0, t_1]$$

Here $t$ is not a new spatial coordinate. It is a label for arranging the small pieces along the curve from start to end. With this label, the displacement on the $i$th subinterval can be written as

$$
\Delta\mathbf{r}_i = \gamma(t_i+\Delta t)-\gamma(t_i)
$$

On each subinterval, <strong>apply the matrix $dx$ to the displacement vector $\Delta\mathbf{r}_i$</strong>:

$$dx(\Delta\mathbf{r}_i) = \begin{pmatrix}1&0&0\end{pmatrix} \begin{pmatrix}\Delta x_i \\ \Delta y_i \\ \Delta z_i\end{pmatrix} = \Delta x_i = \frac{\Delta x_i}{\Delta t}\,\Delta t$$

The equality here means that applying the fixed $1$-form $dx$ to the displacement vector $\Delta\mathbf{r}_i$ returns the component $\Delta x_i$ exactly. On the other hand, the integral over the whole curve is defined as the limit of a Riemann sum in which the measuring device is evaluated at a representative point on each subinterval and the results are added.

$$\sum_i dx(\Delta\mathbf{r}_i) = \sum_i \frac{\Delta x_i}{\Delta t}\,\Delta t$$

The substitution integrals treated in Chapter 1 were precisely this kind of reorganization of a sum. We do the same here. Number the small pieces along the curve by $t$, and organize the change in each component as “rate of change $\times$ subinterval width.” As the mesh is made infinitely fine, the conversion factor converges to the ordinary derivative of the coordinate function: $\Delta x_i/\Delta t \to x'(t)$.

This computation has exactly the same form as the substitution integral in Chapter 1 §1.2.5:

$$\int_\gamma dx = \int_{t_0}^{t_1} x'(t)\,dt = x(t_1)-x(t_0).$$

Similarly, $\int_\gamma dy = y(t_1) - y(t_0)$ and $\int_\gamma dz = z(t_1) - z(t_0)$. In other words, <strong>the line integrals of the $1$-forms $dx, dy, dz$ return the net displacement of the curve — the difference between the coordinates at the end point and those at the start point.</strong>

#### 3.3.2 Trying It on a Circle — Arc Length Does Not Appear

Let us check. For a circle too, what we have in mind first is the operation of chopping the circle into fine arcs and summing the displacements of each small piece. To compute the sum over one full revolution, however, we need a label that arranges the small pieces in order. Here we use the angle $t$ as that label. A circle of radius $R$ is represented as

$$\gamma(t) = (R\cos t,\; R\sin t,\; 0),\qquad t \in [0, 2\pi]$$

Since $\gamma'(t) = (-R\sin t,\; R\cos t,\; 0)$:

$$\begin{aligned}
\int_\gamma dx &= \int_0^{2\pi} dx(\gamma'(t))\,dt = \int_0^{2\pi} (-R\sin t)\,dt = R\bigl[\cos t\bigr]_0^{2\pi} = 0 \\[4pt]
\int_\gamma dy &= \int_0^{2\pi} dy(\gamma'(t))\,dt = \int_0^{2\pi} (R\cos t)\,dt = R\bigl[\sin t\bigr]_0^{2\pi} = 0
\end{aligned}$$

Both are zero. It is a closed curve, so the start and end points coincide and the component displacements cancel over one full turn — a natural result.

However, we also know that the arc length of this circle is $2\pi R$. With coefficient-$1$ $dx$ and $dy$ alone we get zero — so <strong>how do we obtain arc length?</strong>

At each label $t$, the values measured by $dx$ and $dy$ are already at hand:

$$
dx(\gamma'(t)) = -R\sin t,\qquad dy(\gamma'(t)) = R\cos t
$$

These are scalars, so we can square them and add:

$$dx(\gamma'(t))^2 + dy(\gamma'(t))^2 = R^2\sin^2 t + R^2\cos^2 t = R^2$$

Taking the square root gives the conversion factor for length per small piece, $|\gamma'(t)| = R$. Integrating over the whole interval:

$$\int_0^{2\pi} \!\sqrt{dx(\gamma'(t))^2 + dy(\gamma'(t))^2}\;dt = \int_0^{2\pi} \!R\,dt = 2\pi R$$

Arc length $2\pi R$ has appeared. What is happening here is important — $dx$ and $dy$ each gave zero on the closed curve by themselves, yet when we take the square root of the sum of their squares and integrate, the correct arc length emerges. The “power to measure length” that coefficient-$1$ $1$-forms lacked was recovered by the algebraic rearrangement called the sum of squares.

Let us organize what is happening here. At each label $t$ we obtain two scalars, $dx(\gamma'(t))$ and $dy(\gamma'(t))$, take the square root of their sum of squares, $\sqrt{dx(\gamma'(t))^2 + dy(\gamma'(t))^2}$, and integrate with respect to $t$. This is nothing other than integrating length measurement in Cartesian coordinates along the curve. In three dimensions, we write this line element as

$$ds(\mathbf{v}) = \sqrt{dx(\mathbf{v})^2 + dy(\mathbf{v})^2 + dz(\mathbf{v})^2}$$

The circle we are considering now lies in the plane $z=0$, so $dz(\gamma'(t))=0$, and only the two components $dx, dy$ remain in the calculation above.

> <strong>Note</strong> (on notation) By the convention of Chapter 1 §1.1.6, a standalone $dx$ is a row vector (operator), and it cannot be squared by itself. $dx(\mathbf{v})^2$ means the square of the <strong>scalar obtained by applying the $1$-form $dx$ to the vector $\mathbf{v}$</strong>. Preserving this distinction is what keeps the notation of this book consistent.

This $ds$ is a convenient notation for measuring arc length, but it is not itself a $1$-form in the sense of this book. A $1$-form is a measuring device that acts linearly on a displacement $\mathbf{v}$, whereas $ds(\mathbf{v})$ contains a square root of a sum of squares, so in general $ds(\mathbf{v}+\mathbf{w}) = ds(\mathbf{v})+ds(\mathbf{w})$ does not hold. Therefore $ds$ cannot be written as a linear combination of $dx, dy, dz$ — in the form $P\,dx+Q\,dy+R\,dz$.

#### 3.3.3 What Can a $1$-Form Measure?

Arc length could be measured by integrating the line element $ds(\mathbf{v}) = \sqrt{dx(\mathbf{v})^2 + dy(\mathbf{v})^2 + dz(\mathbf{v})^2}$. However, this $ds$ cannot be written as a linear combination of $dx, dy, dz$; it requires a square root of a sum of squares. Here we first ask: what does a $1$-form that does not use such a square root of a sum of squares — that is, a $1$-form that can be written as a linear combination of $dx, dy, dz$ — actually measure?

Suppose a force field $\mathbf{F}(x,y,z) = (F_x, F_y, F_z)$ acts at each point in space. When we move a particle along a curve, the infinitesimal work done by the force on each subinterval is the product of the component of the force in the direction of displacement and the magnitude of the displacement — namely, $F_x\,\Delta x + F_y\,\Delta y + F_z\,\Delta z$. Summing this over the whole interval gives the work $W = \int_\gamma \mathbf{F}\cdot d\mathbf{r}$.

What matters here is that the components $F_x, F_y, F_z$ of the force <strong>vary from place to place</strong>. For the geometric examples in §3.1 and §3.2, coefficient $1$ carried much of the story; to measure work, coefficients that vary from place to place are indispensable. This is what most vividly shows the necessity of coefficients.

This is the motivation for introducing coefficients in the next section.

> <strong>Checkpoint so far</strong>
> - Line integrals of $dx, dy, dz$ return “net displacement.” On a closed curve they are zero.
> - Arc length can be computed by integrating the line element $ds(\mathbf{v}) = \sqrt{dx(\mathbf{v})^2 + dy(\mathbf{v})^2 + dz(\mathbf{v})^2}$. $ds$ is not a $1$-form and cannot be written as a linear combination of $dx, dy, dz$ (it requires a square root of a sum of squares).
> - What a $1$-form that can be written as a linear combination of $dx, dy, dz$ measures is a quantity such as “work.” → §3.4.

---

### §3.4 Adding Coefficients — Density Times Geometry

#### 3.4.0 Why Coefficients? — Physics Demands Them

In §3.1–§3.3, we measured curved shapes using forms with coefficient $1$. But in real physics, there are countless situations where we want to multiply a measuring device by a <strong>weight that varies from place to place</strong>:

- <strong>Force field</strong> (varying with location) $\times$ <strong>displacement</strong> $=$ <strong>work</strong>
- <strong>Velocity field</strong> (varying with location) $\times$ <strong>oriented cross-section</strong> $=$ <strong>flux</strong>
- <strong>Density field</strong> (varying with location) $\times$ <strong>volume</strong> $=$ <strong>mass</strong>

The common structure is obvious. The product of <strong>"a weight that varies from place to place ($0$-form $=$ scalar field)"</strong> and <strong>"a geometric way of measuring ($k$-form)"</strong> gives a general $k$-form. In Chapter 2 §2.4.8 we said that "$0$-form is a measuring device that eats zero vectors, namely a scalar field" — precisely this setup.

Below, we define the integrals of forms with coefficients, in order from one to two to three dimensions.

#### 3.4.1 Line Integral of a General $1$-Form (Work)

In real space, take three scalar fields $P, Q, R$ that depend on the point $(x,y,z)$, and call

$$\omega = P(x,y,z)\,dx + Q(x,y,z)\,dy + R(x,y,z)\,dz$$

the <strong>general form of a $1$-form</strong>. Each $dx, dy, dz$ is, as in Chapter 1, a row vector that reads off components from a column vector. The coefficients $P,Q,R$ are weights that vary from place to place — $0$-forms. If $P=\partial f/\partial x,\;Q=\partial f/\partial y,\;R=\partial f/\partial z$ come from a single function $f$, we get the special case $\omega=df$; in general, this need not be so.

The integral along a curve $\gamma(t)$ is simply the Riemann sum from §3.3.1 with coefficients multiplied in. Take the representative point of each small segment to be $\gamma(t_i)$, evaluate the coefficients there to get $\omega_{\gamma(t_i)}$, and feed it the displacement $\Delta\mathbf{r}_i$. At the fixed point $\gamma(t_i)$, $\omega_{\gamma(t_i)}$ is a row vector and $\Delta\mathbf{r}_i$ is a column vector, and their contraction can be written as

$$\omega_{\gamma(t_i)}(\Delta\mathbf{r}_i) = P(\gamma(t_i))\,\Delta x_i + Q(\gamma(t_i))\,\Delta y_i + R(\gamma(t_i))\,\Delta z_i$$

Here "equals" means the contraction of the row vector $\omega_{\gamma(t_i)}$ fixed at one point and the displacement vector $\Delta\mathbf{r}_i$. As the contribution of the whole small segment, this is one term of a Riemann sum with coefficients frozen at the representative point; in the limit as the mesh becomes fine, it becomes a line integral.

Organize the change in each component in the form "finite ratio $\times \Delta t$":

$$
\omega_{\gamma(t_i)}(\Delta\mathbf{r}_i)
= \bigl(P(\gamma(t_i))\frac{\Delta x_i}{\Delta t}
+ Q(\gamma(t_i))\frac{\Delta y_i}{\Delta t}
+ R(\gamma(t_i))\frac{\Delta z_i}{\Delta t}\bigr)\,\Delta t.
$$

Sum over the whole interval and take the limit. Since $\Delta x_i/\Delta t \to x'(t)$, $\Delta y_i/\Delta t \to y'(t)$, and $\Delta z_i/\Delta t \to z'(t)$:

$$
\sum_i \omega_{\gamma(t_i)}(\Delta\mathbf{r}_i)
\;\xrightarrow{\Delta t \to 0}\;
\int_{t_0}^{t_1}
\bigl(P(\gamma(t))x'(t)+Q(\gamma(t))y'(t)+R(\gamma(t))z'(t)\bigr)\,dt
$$

We write this limit as

$$\int_\gamma \omega$$

Exactly the same pattern as the coefficient-$1$ case in §3.3.1: at each instant, a <strong>row vector (coefficient-weighted $1$-form)</strong> eats a <strong>column vector ($\gamma'(t)$)</strong>, returns a scalar, and we aggregate. This is nothing but the natural three-dimensional extension of $F(x)\,dx$ from Chapter 1 §1.2.5.

> <strong>Note</strong> (correspondence with vector analysis)  
> In vector analysis, this quantity is written $\int_\gamma \mathbf{F}\cdot d\mathbf{r}$. Our $\int_\gamma \omega$ is the same thing, yet <strong>the field $\omega$</strong> and <strong>the path $\gamma$</strong> are clearly separated in the notation.

Let us look at a concrete example. Compute the work done by the force field $\mathbf{F} = (y,\; x,\; 0)$ along the unit circle $\gamma(t) = (\cos t,\; \sin t,\; 0),\; t \in [0, 2\pi]$.

Since $\omega = y\,dx + x\,dy$, the coefficients are $P=y,\;Q=x,\;R=0$. On the curve, $P=\sin t,\;Q=\cos t$. Also, $x'(t)=-\sin t$ and $y'(t)=\cos t$:

$$\omega(\gamma'(t)) = (\sin t)(-\sin t) + (\cos t)(\cos t) = -\sin^2\!t + \cos^2\!t = \cos 2t$$

Therefore:

$$\int_\gamma \omega = \int_0^{2\pi} \cos 2t\,dt = \Bigl[\frac{1}{2}\sin 2t\Bigr]_0^{2\pi} = 0$$

The work is zero. This force field does no net work along the unit circle.

#### 3.4.2 Surface Integral of a General $2$-Form (Flux)

Similarly, with three scalar fields $P,Q,R$ as coefficients,

$$
\eta = P\,dy \wedge dz + Q\,dz \wedge dx + R\,dx \wedge dy
$$

we call $\eta$ a general $2$-form.

The integral over a surface is again just the Riemann sum from §3.2.1 with coefficients multiplied in. At the representative point of each small patch, evaluate the coefficients and feed $\eta$ the two displacement vectors $\Delta\mathbf{a},\Delta\mathbf{b}$ that span the patch:

$$\eta(\Delta\mathbf{a},\Delta\mathbf{b})
= P\,(dy \wedge dz)(\Delta\mathbf{a},\Delta\mathbf{b})
{}+ Q\,(dz \wedge dx)(\Delta\mathbf{a},\Delta\mathbf{b})
{}+ R\,(dx \wedge dy)(\Delta\mathbf{a},\Delta\mathbf{b})$$

Sum over all patches and take the limit. We denote this limit by

$$\iint_S \eta$$

At each point, the area-measuring device $\eta$ eats the two displacement vectors that form a surface element and returns a scalar; we aggregate over the whole surface — the same point as in §3.2.

That $dy \wedge dz,\; dz \wedge dx,\; dx \wedge dy$ each measure the "shadow area" onto the corresponding plane was seen in §3.2. The coefficients $P, Q, R$ attach a <strong>weight that varies from place to place</strong> to those shadows. Physically, $(P, Q, R)$ are the components of a velocity field, and $\iint_S \eta$ corresponds to the flux through the surface — but translating this rigorously into the language of vector analysis requires additional correspondence relations. We will do that in a later chapter.

> <strong>Note</strong> (correspondence with vector analysis is only a guidepost here)
> The connection with flux is nothing more than a bridge for readers who already know vector analysis. The main line of this book remains the operation of "feeding a $2$-form and aggregating." Lack of vector-analysis background will not hinder the discussion from here on.

#### 3.4.3 Volume Integral of a General $3$-Form (Total Mass)

The general form of a $3$-form, with scalar field $\rho(x,y,z)$ as coefficient, is

$$\Omega = \rho(x,y,z)\,dx \wedge dy \wedge dz$$

We need only multiply the Riemann sum from §3.1.1 by the density $\rho$. At the representative point of each small box, evaluate $\rho$ and feed the volume element to $\Omega$:

$$\Omega(\Delta x_i\,\hat{e}_x,\; \Delta y_i\,\hat{e}_y,\; \Delta z_i\,\hat{e}_z) = \rho(x_i,y_i,z_i)\,\Delta x_i\,\Delta y_i\,\Delta z_i$$

Sum over the whole region and take the limit. We write this limit as

$$\iiint_V \Omega$$

If $\rho=1$, we return to the coefficient-$1$ case from §3.1. If $\rho$ is mass density, we get total mass; if charge density, total charge. A $3$-form has only one independent component, $dx \wedge dy \wedge dz$, so <strong>"density ($\rho$)" and "the way of measuring volume ($dx \wedge dy \wedge dz$)" separate cleanly</strong> and the picture is clear.

#### 3.4.4 A Unified Picture of Line, Surface, and Volume

Let us look back at what we have done.

| Object | Form | Integral notation | Example physical meaning |
|:---:|:---|:---|:---|
| Curve $\gamma$ | $1$-form $\omega$ | $\displaystyle\int_\gamma \omega$ | Work |
| Surface $S$ | $2$-form $\eta$ | $\displaystyle\iint_S \eta$ | Flux |
| Region $V$ | $3$-form $\Omega$ | $\displaystyle\iiint_V \Omega$ | Total mass |

Written as Riemann sums, they are

$$
\int_\gamma \omega
= \lim_{\text{mesh}\to 0}
\sum_i \omega(\Delta\mathbf{r}_i),
$$

$$
\iint_S \eta
= \lim_{\text{mesh}\to 0}
\sum_i\sum_j\eta(\Delta\mathbf{a}_{ij},\Delta\mathbf{b}_{ij}),
$$

$$
\iiint_V \Omega
= \lim_{\text{mesh}\to 0}
\sum_i\sum_j\sum_k
\Omega(\Delta\mathbf{a}_{ijk},\Delta\mathbf{b}_{ijk},\Delta\mathbf{c}_{ijk})
$$

Here "mesh $\to 0$" means making the size of the coarsest small piece that makes up the curve, surface, or region approach $0$.

All follow the same pattern: a <strong>$k$-form (measuring device) eats $k$ displacement vectors — that is, a $k$-dimensional small piece — returns a scalar, and we aggregate over the whole domain</strong>. As the degree rises, the number of vectors fed in increases, and antisymmetry governs the orientation of area and volume. Only the degree differs; the principle is the same throughout.

> <strong>Checkpoint so far</strong>
> - A general $k$-form is a linear combination of "basis $k$-forms" with "weights that vary from place to place ($0$-form)."
> - The line integral $\int_\gamma \omega$ corresponds to work, the surface integral $\iint_S \eta$ to flux, and the volume integral $\iiint_V \Omega$ to total mass.
> - All follow the same principle: "contraction of measuring device and figure → aggregation." In the next chapter we introduce pullback — the method of recomputing these integrals in different coordinates.

#### 3.4.5 The General Form of Integration

The line, surface, and volume integrals defined separately in §3.1–§3.3 actually fit one pattern. The operation of integrating a $k$-form $\omega$ over a $k$-dimensional region $M$ is written, regardless of dimension, as

$$\int_M \omega$$

If $M$ is a curve ($k=1$), we write $\int_\gamma$; if a surface ($k=2$), $\iint_S$; if a solid ($k=3$), $\iiint_V$ — the number of integral signs is determined only by the dimension of $M$. The content is always "chop into small pieces → feed $k$ displacement vectors to the $k$-form → sum $\sum$ → limit."

The stage of this book is three-dimensional space, so $k=1,2,3$ suffices; but it does no harm to keep in the back of your mind that this formula holds regardless of $k$. When we introduce the exterior derivative $d$ in Chapter 5, this unified viewpoint will bear fruit in the general form of Stokes's theorem, $\int_{\partial M} \omega = \int_M d\omega$.

---

### §3.5 Summary of This Chapter and Outlook Toward the Next

Over the past three chapters, we have assembled the following three things:

1. <strong>Chapter 1</strong>: View $dx$ as a matrix ($1$-form), and read integration as the limit of matrix action
2. <strong>Chapter 2</strong>: Construct $2$-forms and $3$-forms via the wedge product $\wedge$, and measure area and volume algebraically
3. <strong>Chapter 3 (this chapter)</strong>: Apply forms to curves, surfaces, and regions, and establish the operation of aggregating their output

What this chapter established is the following unified principle:

<strong>A $k$-form (measuring device) eats $k$ displacement vectors—that is, a $k$-dimensional small piece—and returns a scalar, which is then aggregated over the entire region.</strong> Across degrees $0,1,2,3$, the picture remains the same. Work along a curve, flux across a surface, total mass in a region—all can be written in the same language.

> <strong>Checkpoint so far — Chapter 3</strong>
> - The integral $\int_M \omega$ of a $k$-form $\omega$ is defined by “chop into small pieces → feed $k$ displacement vectors to the $k$-form → sum → limit.”
> - The line integral $\int_\gamma \omega$ of a $1$-form is the operation of feeding each small curve segment’s displacement vector to $\omega$ and aggregating. Work is written as $\int_\gamma \omega$, corresponding to the vector-analysis notation $\int_\gamma \mathbf{F}\cdot d\mathbf{r}$.
> - The surface integral $\iint_S \eta$ of a $2$-form $\eta$ is the operation of feeding the two displacement vectors that span each small piece to $\eta$ and aggregating. With coefficient $1$, it measures the “shadow” onto each plane; adding up scalar area elements $dS$ built from the three shadows gives scalar area.
> - The volume integral $\iiint_V \Omega$ of a $3$-form $\Omega$ is the operation of feeding the three displacement vectors that span each small rectangular box to $\Omega$ and aggregating. With coefficient $1$ this is volume directly; with coefficient $\rho$ it is total mass or total charge.
> - A general $k$-form can be written as a combination of coefficients ($0$-forms) that vary from point to point and basis $k$-forms.

However, an important problem remains.

Up to here, we counted small pieces while keeping the measuring devices of standard Cartesian coordinates $x, y, z$ as much as possible. But in actual calculations, counting in other variables is often overwhelmingly easier. Trace a circle by angle. View a sphere by radius and angles. In physics problems, you cannot get away without such variable changes.

Then what should we change, and what should we keep?

In the next chapter (Chapter 4), we reread variable change not as a matter of “moving points,” but as an <strong>operation that rebuilds measuring devices</strong>. This is the <strong>pullback</strong>.

# Chapter 4: What Is a Change of Variables? — The Pullback $\Phi^*$: Making Measuring Devices Consistent

# Chapter 4: What Is a Change of Variables? — The Pullback $\Phi^*$: Making Measuring Devices Consistent

### §4.0 Physics Curves; Computation Uses Boxes

The quantities we truly want to measure in physics do not depend on the names of coordinates.

Work done on a particle must be the same whether we write the trajectory in $x$ or in time $t$. The area swept out by a planet must be the same whether we measure it in Cartesian coordinates or polar coordinates. The mass of an object must be the same whether we integrate in Cartesian coordinates or cylindrical coordinates.

Yet physics is usually curved.
Trajectories curve, surfaces curve, and the boundaries of regions curve.

Computation, on the other hand, is boxy.
We mark off intervals, divide into grids, and slice into boxes. Integration is the technique of tallying curved physical quantities using boxy computation.

Here a problem arises.
If we change the variables used for computation, we cannot use the measuring devices as they stand.

$dx$ is a measuring device that reads displacement in the $x$ direction; swapping it for $dt$ alone does not measure work correctly.
$dx \wedge dy$ is an area-measuring device in the $xy$ plane; swapping it for $dr \wedge d\theta$ alone does not measure area correctly.
$dx \wedge dy \wedge dz$ likewise does not measure volume correctly if we swap it for $dr \wedge d\theta \wedge dz$ alone.

Physical quantities must not change.
But the boxes used for computation do change.

Then how should we rebuild the measuring devices?

In this chapter we pursue this question through three examples.

First, on a finite interval, we see what must be multiplied on the time side so that a piece of work agrees. Next, on a finite grid, we find the factor that makes area agree. Finally, on finite boxes, we find the factor that makes volume agree.

As the partition is refined, a finite ratio becomes a derivative, and a finite determinant becomes the determinant of the matrix built from partial derivatives. The rebuild of measuring devices obtained in that limit is called the pullback, written $\Phi^*$.

So the order of this chapter is as follows.

> - Find it on a finite interval.
> - Do the same on a finite grid.
> - Do the same on finite boxes.
> - Finally, $\Phi^*$ appears as the limit $h\to0$.

In this chapter we do not memorize formulas; we make things consistent.
Through three physical quantities—work, area, and volume—we see how $dx$, $dx \wedge dy$, and $dx \wedge dy \wedge dz$ are each rebuilt.

### §4.1 Pullback of a 1-Form — Work and the Work-Energy Theorem

> <strong>Note</strong> (for readers without a physics background) All we use here is that position can be written as $x=\gamma(t)$. Read $F(x)$ as a function of position and $v(t)$ as a function of time.

<strong>① Start from a physical quantity.</strong> We do not jump straight to general theory. Let us begin from a familiar fact of mechanics.

Suppose a force $F$ acts on a particle moving along the $x$ axis. Work is given by

$$W = \int F\,dx$$

On the other hand, the equation of motion is

$$F = m\frac{dv}{dt}$$

From these two, the familiar work-energy theorem

$$W = \frac{1}{2}mv^2\,\Big|_{t_0}^{t_1}$$

follows. In this section we reread this derivation through the lens of "how must we rebuild the measuring device so that the same work comes out?" We begin by finding the coefficient needed on the time-side measuring device, interval by interval on a finite partition.

<strong>② Naive substitution—it does not match.</strong> Write the particle's position as $x = \gamma(t)$. The velocity is $v(t)=\gamma'(t)$. The measuring device for work is $F\,dx$—a $1$-form that eats displacement in physical space and returns a piece of work.

But the motion is given by time $t$. So we want to compute work in time.

First on the physical-space side, take uniformly accelerated motion $x(t) = \frac{1}{2}at^2$ and constant force $F = ma$. With endpoint $X = \frac{1}{2}aT^2$,

$$W_{\text{phys}} = \int_0^X ma\,dx = ma\,X = \frac{1}{2}ma^2T^2$$

On the other hand, if we integrate naively on the time side—that is, replace $dx$ by $dt$ as-is—

$$W_{\text{naive}} = \int_0^T ma\,dt = ma\,T$$

We have $\frac{1}{2}ma^2T^2 \neq ma\,T$, so they clearly do not agree. With $dt$ alone, the value of work changes.

<strong>③ See the cause on a finite interval.</strong> Consider a small time interval $[t_i, t_{i+1}]$. Let its width be $\Delta t_i = t_{i+1} - t_i$ and the corresponding change in position $\Delta x_i = \gamma(t_{i+1}) - \gamma(t_i)$. One term of work on the physical-space side is $F_i\,\Delta x_i$. One term built naively on the time side is $F_i\,\Delta t_i$. These do not agree because we ignored the consistency factor between $\Delta t_i$ and $\Delta x_i$.

So multiply the time-side term by a coefficient $c_i$ and try $F_i\,c_i\,\Delta t_i$. For this to agree with $F_i\,\Delta x_i$, we need $c_i\,\Delta t_i = \Delta x_i$. Therefore

$$c_i = \frac{\Delta x_i}{\Delta t_i}$$

Up to here it is just division. Yet this division has meaning. We were asking: what measuring device must eat the time-side interval $\Delta t_i$ so that the same value as the physical-space displacement $\Delta x_i$ comes out? The answer is

$$\frac{\Delta x_i}{\Delta t_i}\,dt$$

Indeed, if we feed $\Delta t_i$ to this measuring device,

$$\left(\frac{\Delta x_i}{\Delta t_i}\,dt\right)(\Delta t_i)=\Delta x_i$$

So on a finite time interval we can read the same displacement as on the physical-space side.

Write this provisional measuring device on a finite interval as

$$\gamma_h^\square(dx):=\frac{\Delta x_i}{\Delta t_i}\,dt$$

where $h$ denotes the maximum width of the partition. Feeding this measuring device to a finite interval gives

$$\gamma_h^\square(dx)\bigl(\Delta t_i\bigr)=\Delta x_i$$

As the partition is refined, the finite ratio approaches the velocity

$$\frac{\Delta x_i}{\Delta t_i}\to \gamma'(t)$$

So in the limit we obtain

$$
\gamma_h^\square(dx)
\xrightarrow{h\to0}
\gamma^*(dx)
=
\gamma'(t)\,dt
$$

After the limit we write this measuring device as $\gamma^*(dx)=\gamma'(t)\,dt$. The coefficient $\Delta x_i/\Delta t_i$ found on finite intervals has become the velocity $\gamma'(t)$ in the limit.

Henceforth we write the same rebuild for finite grids and boxes collectively as $\Phi_h^\square$.

> <strong>Note</strong> ($\Phi_h^\square$ and $\Phi^*$)
>
> $\gamma_h^\square$ and $\Phi_h^\square$ are provisional measuring devices used in this book on finite intervals and finite cells. They are distinguished from $\Phi^*$ after $h\to0$.
>
> In the finite cell version, the coefficient is obtained by dividing the measured value of the figure spanned by finite displacement vectors by the cell width on the computation side. Therefore, feeding this measuring device to a finite cell recovers the original measured value.
>
> This coefficient is determined cell by cell. To keep the notation light, dependence on the cell index is not written into $\Phi_h^\square$.
>
> What we measure here is not the image of a finite cell under the map itself, but the figure spanned by the chosen displacement vectors: displacement in one dimension, a parallelogram in two dimensions, a parallelepiped in three dimensions. For example, the image of a finite polar grid cell is a curved sector, but what we measure here is not that sector itself but the parallelogram spanned by the two chosen displacement vectors.
>
> In the limit of partition width $h\to0$, the coefficients of $\gamma_h^\square$ and $\Phi_h^\square$ converge to the coefficients of the pullback $\Phi^*$ after the limit.

<strong>④ Write the pullback of the concrete example.</strong> After taking the limit, the measuring device on the time axis (the pulled-back result) is

$$\gamma^*(F\,dx) = F(\gamma(t))\,v(t)\,dt$$

By this we can recast the measuring device $F\,dx$ for work in physical space into one for the time axis.

<strong>⑤ Pullback of a $1$-form with a coefficient.</strong> For an arbitrary coefficient $F(x)$, the same structure holds. When position is given by $x = \gamma(t)$,

$$
\gamma^*(F(x)\,dx)
=
F(\gamma(t))\,\gamma'(t)\,dt
$$

<strong>⑥ Define it through this transformation.</strong> By now the route from the finite-interval version to the standard version is visible. So for a smooth curve $\gamma: t \mapsto x$, we define the rebuild of the $1$-form $\omega = F(x)\,dx$ by

$$
\gamma^*(F(x)\,dx)
=
F(\gamma(t))\,\gamma'(t)\,dt
$$

This formula is the pullback of the physical-space $1$-form to the time side. The velocity $\gamma'(t)$ is the limit of $\Delta x_i/\Delta t_i$ found on finite intervals and serves as the consistency factor for "recasting the physical-space measuring device $dx$ into the time-axis measuring device $dt$."

Next we repeat the same procedure for the two-dimensional area-measuring device $dx\wedge dy$. In one dimension we mapped a finite interval and measured the displacement of its image. In two dimensions we will map a finite rectangle and measure the area spanned by two displacement vectors of its image.

<strong>⑦ Return to the physical quantity.</strong> Here, using the equation of motion $F = m\,dv/dt$,

$$\gamma^*(F\,dx) = m\frac{dv}{dt}\,v\,dt = m v\,dv$$

Here $\frac{dv}{dt}\,dt$ can be read as $\gamma^*(dv)$: the velocity-axis measuring device $dv$ pulled back to the time axis. Therefore

$$W = \int F\,dx = \int_{\gamma} F\,dx = \int_{t_0}^{t_1} \gamma^*(F\,dx) = \int_{v(t_0)}^{v(t_1)} m v\,dv = \frac{1}{2}mv^2\,\Big|_{t_0}^{t_1}$$

—work equals the change in kinetic energy.

> <strong>Aside</strong> (why the name "pullback") If we are "sending" a measuring device that lives in physical space into parameter space, is that not a "push forward"?—that is how it feels to me. For me, physical space is "reality" and parameter space is a "tool for computation." But the mathematical map $\gamma$ is always defined in the direction “parameter space $\to$ physical space.” In the mathematical world, parameter space is the departure point. So the movement of a measuring device that goes against the direction of the map, from physical space back to parameter space, is called a pullback. I have made peace with calling it that by convention.

> <strong>Note</strong> ($dx$ is a row vector, $dt$ is too) In the calculations of §4.1, $dx$, $dt$, and $dv$ all keep the same type: "eat displacement and return a scalar." The principle "row vector × column vector → scalar" from Chapter 1 §1.1.3 does not break even in the middle of a pullback. The result $\gamma^*(F\,dx)$ is again a $1$-form (row vector) on the time axis; feeding it the time-side displacement $\Delta t$ yields a scalar (a piece of work)—this consistency is what supports understanding of the pullback.


### §4.3 Pullback of a 3-Form — Conservation of Mass and Volume Integrals

<strong>① Start from a physical quantity.</strong> The end point is a volume integral. This time we map a three-dimensional finite box and measure it.

Consider the mass of a cylinder of uniform density $\rho$ (radius $C$, height $H$). Computing directly in $(x,y,z)$ space,

$$M = \rho \cdot (\text{volume}) = \rho \cdot \pi C^2 H$$

This $M$ must not change no matter which coordinates we use to compute it.

<strong>② Naive substitution — it does not work as-is.</strong> We want to write the integral in cylindrical coordinates $(r,\theta,z)$. The cylinder ranges over $r \in [0, C],\; \theta \in [0, 2\pi],\; z \in [0, H]$, so if we replace $dx \wedge dy \wedge dz$ outright by $dr \wedge d\theta \wedge dz$:

$$
M_{\text{naive}}
=
\rho \iiint dr\wedge d\theta\wedge dz
=
\rho
\int_0^H
\biggl(
  \int_0^{2\pi}
  \biggl(
    \int_0^C dr
  \biggr)
  d\theta
\biggr)
dz
=
2\pi\rho C H
$$

Comparing this with the correct value $\rho \pi C^2 H$, we have $2\pi\rho C H \neq \rho \pi C^2 H$. They clearly do not agree.

<strong>③ Find the cause on a finite mesh.</strong> In three dimensions, we ask what must be fed to a finite box on the $(r,\theta,z)$ side so that we get the same value as the volume on the $(x,y,z)$ side.

Cut a grid of finite size $\Delta r \times \Delta\theta \times \Delta z$ in $(r,\theta,z)$ space. The transformation is $x = r\cos\theta,\; y = r\sin\theta,\; z = z$. The $z$ direction is unchanged by the transformation, so the volume is “mesh-cell area in the $xy$ plane” $\times \Delta z$. The area in the $xy$ plane follows exactly the procedure of §4.2:

$$\det = r\Delta r\,\sin\Delta\theta$$

Therefore, the volume of one cell is

$$\text{volume} = \bigl(r\Delta r\,\sin\Delta\theta\bigr) \times \Delta z$$

The finite cell in cylindrical coordinates itself is curved in the $\theta$ direction, but what we are measuring here is the signed volume of the parallelepiped spanned by three difference vectors.

Dividing this measured value by the cell widths $\Delta r_i\,\Delta\theta_j\,\Delta z_k$ on the $(r,\theta,z)$ side gives the coefficient of a provisional measuring device used on a finite cell. That is,

$$
\Phi_h^\square(dx\wedge dy\wedge dz)
:=
r_i\frac{\sin\Delta\theta_j}{\Delta\theta_j}\,dr\wedge d\theta\wedge dz
$$

Feed this measuring device to a finite box and we get

$$
\begin{aligned}
&\Phi_h^\square(dx\wedge dy\wedge dz)
(\Delta r_i,\Delta\theta_j,\Delta z_k)\\
&\qquad =
r_i\frac{\sin\Delta\theta_j}{\Delta\theta_j}
\Delta r_i\Delta\theta_j\Delta z_k \\
&\qquad =
r_i\Delta r_i\sin\Delta\theta_j\Delta z_k
\end{aligned}
$$

The right-hand side is the signed volume of the parallelepiped spanned by three finite difference vectors.

Writing the total mass sum in the finite-cell version as $M_h^\square$, we have

$$
M_h^\square
:=
\sum_i\sum_j\sum_k
\rho\,
\Phi_h^\square(dx\wedge dy\wedge dz)(\Delta r_i,\Delta\theta_j,\Delta z_k)
=
\sum_i\sum_j\sum_k
\rho\,r_i\,\Delta r_i\,\sin\Delta\theta_j\,\Delta z_k
$$

In the final stage, when we take the limit of the sum,

$$
\frac{\sin\Delta\theta_j}{\Delta\theta_j}\to 1
$$

Therefore the true mass $M$ is obtained as

$$
M
=
\lim_{h\to0} M_h^\square
=
\rho\iiint_{V'} r\,dr\wedge d\theta\wedge dz
=
\rho
\int_0^H
\biggl(
  \int_0^{2\pi}
  \biggl(
    \int_0^C r\,dr
  \biggr)
  d\theta
\biggr)
dz
=
\rho\cdot\pi C^2H
$$

The coefficient of the measuring device on a finite cell is $r_i\frac{\sin\Delta\theta_j}{\Delta\theta_j}$. As $h\to0$, this coefficient again approaches $r$.

<strong>④ Write the standard form obtained in the limit.</strong> For the transformation to cylindrical coordinates $\Phi(r,\theta,z) = (r\cos\theta,\; r\sin\theta,\; z)$:

$$
\Phi_h^\square(dx\wedge dy\wedge dz)
\xrightarrow{h\to0}
\Phi^*(dx \wedge dy \wedge dz)
=
r\,dr \wedge d\theta \wedge dz
$$

This is the limiting rebuild of the $3$-form obtained from the finite-cell version $\Phi_h^\square$. We denote this limiting rebuild by $\Phi^*$. The same consistency coefficient $r$ from §4.2 carries over unchanged.

<strong>⑤ Pullback of a weighted $3$-form.</strong> For a $3$-form $\rho\,dx \wedge dy \wedge dz$ with arbitrary density $\rho(x,y,z)$, the same structure holds:

$$\Phi^*\bigl(\rho(x,y,z)\,dx \wedge dy \wedge dz\bigr) = \rho(r\cos\theta,\, r\sin\theta,\, z)\; r\,dr \wedge d\theta \wedge dz$$

The coefficient $\rho$ is only re-expressed in new coordinates (pullback of a $0$-form); only the part $dx \wedge dy \wedge dz$ changes to $r\,dr \wedge d\theta \wedge dz$.

<strong>⑥ Transfer the same discovery to a general transformation.</strong> More generally, consider a transformation of space $\Phi(u,v,w) = (x(u,v,w), y(u,v,w), z(u,v,w))$. Mapping a finite box on the $(u,v,w)$ side produces three difference vectors. Measuring them with $dx\wedge dy\wedge dz$ gives the oriented volume of the mapped parallelepiped.

Dividing that volume value by $\Delta u\,\Delta v\,\Delta w$ and refining the partition, the difference ratios converge to partial derivatives and a $3\times3$ determinant appears. Therefore, after $h\to0$, the pullback is:

$$
\begin{aligned}
&\Phi^*\bigl(\rho(x,y,z)\,dx \wedge dy \wedge dz\bigr) \\
&= \rho(x(u,v,w), y(u,v,w), z(u,v,w))\,
\det\!\begin{pmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\[6pt]
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\[6pt]
\frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w}
\end{pmatrix}
\,du \wedge dv \wedge dw
\end{aligned}
$$

Writing this $3 \times 3$ determinant as $J(u,v,w)$, we obtain

$$\Phi^*(\rho\,dx \wedge dy \wedge dz) = \rho(\Phi(u,v,w))\,J\,du \wedge dv \wedge dw$$

This $3\times3$ determinant $J(u,v,w)$ is the consistency coefficient of the $3$-form.

Arranging three difference vectors on a finite mesh gives

$$\det\!\begin{pmatrix}
\Delta x_u & \Delta x_v & \Delta x_w \\[2pt]
\Delta y_u & \Delta y_v & \Delta y_w \\[2pt]
\Delta z_u & \Delta z_v & \Delta z_w
\end{pmatrix}$$

This is the measured value assigned to the finite box by the provisional measuring device. For the parallelepiped spanned by the difference vectors, it is an equality. As the partition width $h$ is taken toward $0$, the coefficient obtained by dividing this finite determinant by $\Delta u\,\Delta v\,\Delta w$ converges to the Jacobian $J$ built from partial derivatives.

If $J$ is negative, orientation is reversed. In the formal pullback, we use this signed $J$ as-is. On the other hand, when we are computing ordinary positive volume or mass density as a non-oriented scalar quantity, we need the magnitude with orientation forgotten, so $|J|$ appears. It is important not to confuse $J$ and $|J|$ here.

For a $1$-form we have a $1 \times 1$ determinant (the velocity $\gamma'(t)$), for a $2$-form a $2 \times 2$ determinant, for a $3$-form a $3 \times 3$ determinant ($J$) — as the degree rises, the size of the determinant governing the consistency coefficient grows by one each time. The partial-derivative determinant formula above is precisely <strong>the general definition of the pullback of a $3$-form</strong>.

> <strong>Note</strong> (for readers who have studied vector analysis) When you learned in a change of variables that “in polar coordinates, $r\,dr\,d\theta$ appears,” many textbooks give a geometric explanation: “consider the arc length $r\Delta\theta$ in the $\theta$ direction and $\Delta V \approx \Delta r \cdot r\Delta\theta \cdot \Delta z$.” That explanation is not wrong. But in the computation of this book we never consider arc length at all. Only the transformation formulas, trigonometric identities, and the determinant corresponding to $\wedge$ produce the consistency coefficient $r$.

<strong>⑦ Return to the physical quantity.</strong> Integrating with the pulled-back measuring device,

$$
M
=
\rho\iiint_V dx\wedge dy\wedge dz
=
\rho\iiint_{V'} r\,dr\wedge d\theta\wedge dz
$$

$$
=
\rho
\int_0^H
\biggl(
  \int_0^{2\pi}
  \biggl(
    \int_0^C r\,dr
  \biggr)
  d\theta
\biggr)
dz
=
\rho\cdot\pi C^2H
$$

This agrees with the correct value. To preserve the integral value, the measuring device $dx \wedge dy \wedge dz$ had to be rebuilt as $r\,dr \wedge d\theta \wedge dz$ in $(r,\theta,z)$ space. The same pattern repeats across the chapter: in §4.1 the consistency factor $\gamma'(t)$ describes conservation of energy; in §4.2 the factor $r$ describes conservation of angular momentum; and here, the factor $r$—more generally, $J$—describes conservation of mass.

---

### §4.4 Properties of the Pullback — What We Have Established So Far

In §4.1–§4.3 we constructed pullbacks through three concrete examples. Here we organize the algebraic properties common to all of them. At the same time, we define the $3 \times 3$ determinant $J$ that appeared in §4.3 as the <strong>Jacobian determinant</strong>. The matrix

$$\begin{pmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\[4pt]
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\[4pt]
\frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w}
\end{pmatrix}$$

is called the <strong>Jacobian matrix</strong>, and its determinant is the Jacobian $J$.

<strong>① Pullback of a $0$-form (scalar field).</strong> To pull back a scalar field $f(x,y,z)$ by a transformation $\Phi$ is simply to rewrite the coordinates into a parametric representation:

$$\Phi^*(f) = f(\Phi(u,v,w))$$

For example, the operation in §4.1 that rewrote $F(x)$ in $F(x)\,dx$ as $F(\gamma(t))$ is nothing but the pullback of the $0$-form $F$.

<strong>② Linearity.</strong> For two $k$-forms $\omega, \eta$ and scalars $a,b$,

$$\Phi^*(a\omega + b\eta) = a\,\Phi^*(\omega) + b\,\Phi^*(\eta)$$

holds. This guarantees that sums and scalar multiples of measuring devices stay consistent before and after pullback.

<strong>③ Compatibility with the wedge product.</strong> For a $k$-form $\omega$ and an $\ell$-form $\eta$,

$$\Phi^*(\omega \wedge \eta) = \Phi^*(\omega) \wedge \Phi^*(\eta)$$

holds. In other words, “assemble then pull back” and “pull back then assemble” give the same result. The operation in §4.2 of expanding $dx$ and $dy$ separately and then assembling with $\wedge$ was exactly an instance of this property.

<strong>④ Consistency factors by degree.</strong> For the pullback $\Phi^*$ after taking the limit $h\to0$ from finite cells, we take the Jacobian matrix assembled from the partial derivatives of $\Phi$, pick out the $k$ directions needed, and the $k \times k$ determinant of those entries becomes the consistency factor. Within the scope of this book, it appears in the following forms.

- $k=1$ ($1$-form): a $1 \times 1$ determinant

$$
\det
\begin{pmatrix}
\gamma'(t)
\end{pmatrix}
=
\gamma'(t)
$$

- $k=2$ ($2$-form): a $2 \times 2$ determinant

$$
\det
\begin{pmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v}\\[4pt]
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{pmatrix}
=
\frac{\partial x}{\partial u}\frac{\partial y}{\partial v}
-
\frac{\partial x}{\partial v}\frac{\partial y}{\partial u}
$$

- $k=3$ ($3$-form): a $3 \times 3$ determinant

$$
J
=
\det
\begin{pmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w}\\[4pt]
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w}\\[4pt]
\frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w}
\end{pmatrix}
$$

Thus a $1 \times 1$ determinant appears for $1$-forms, a $2 \times 2$ determinant for $2$-forms, and a $3 \times 3$ determinant for $3$-forms. As the degree increases, the size of the determinant that fixes the consistency factor of the measuring device grows by one step at a time. This structure is the same for $k$-forms in higher dimensions as well. Arrange the coefficients obtained by differentiating the transformation formulas, pick out the $k$ directions needed, and form the determinant. That determinant is the consistency factor for rewriting a $k$-dimensional measuring device into a form usable in the variables on the parameter-space side.

> <strong>Note</strong> (The name “Jacobian”) In general, the matrix assembled from the partial derivatives of a change of variables is called the Jacobian matrix, and its determinant is called the Jacobian. In one dimension this is the $1\times1$ determinant $\gamma'(t)$; in two dimensions it is the $2\times2$ determinant above; in three dimensions it is $J$.
>
> In this book, we often write the $3\times3$ determinant that appears especially as a volume conversion factor as $J$ and call it the Jacobian.

<strong>⑤ Relation between the finite-cell version and the pullback after the limit.</strong> In the derivations of this chapter, we did not write partial derivatives right away. First in §4.1, we wrote the rebuilding of the measuring device on a finite interval as $\gamma_h^\square$. There, the finite ratio $\Delta x/\Delta t$ served as the coefficient on each interval, and in the limit $h\to0$ we moved to $\gamma^*$.

In §4.2 and §4.3, we extended this idea to two and three dimensions. The finite-cell version $\Phi_h^\square$ is a provisional measuring device used on finite cells. Its coefficients are fixed by “measurement of the figure spanned by finite-difference vectors, divided by the cell width on the parameter-space side.” When we feed this measuring device to a finite cell, the original measurement comes back.

For example, for a $2$-form, the coefficient is the area of the parallelogram spanned by two difference vectors, divided by $\Delta u\,\Delta v$. For a $3$-form, it is the volume of the parallelepiped spanned by three difference vectors, divided by $\Delta u\,\Delta v\,\Delta w$.

In the limit as the partition width $h\to0$, these coefficients converge to determinants built from partial derivatives. These are the coefficients of the pullback $\Phi^*$ after the limit. Thus the flow of this chapter is a two-stage process: “build a provisional measuring device on finite cells → obtain $\Phi^*$ in the limit $h\to0$.”

> <strong>Note</strong> (Commutation with the exterior derivative $d$ — foreshadowing Chapter 5) In addition to these, there is an important relation between pullback and the exterior derivative $d$:
> $$\Phi^*(d\omega) = d(\Phi^*\omega)$$
> In other words, “exterior differentiate then pull back” and “pull back then exterior differentiate” give the same result. We will take up this property again in §5.9 after we formally introduce $d$ in Chapter 5.

We will not go any deeper here. In later chapters we will move on to language for dealing with curved space itself. Even then, the experience with finite cells and determinants that we saw in this chapter will serve as a foothold.

---

### §4.5 Summary of This Chapter and Outlook Toward Chapter 5, the Exterior Derivative

Over the past four chapters, we have assembled the following four things:

1. <strong>Chapter 1</strong>: View $dx$ as a matrix ($1$-form), and read integration as the limit of matrix action
2. <strong>Chapter 2</strong>: Construct $2$-forms and $3$-forms via the wedge product $\wedge$, and measure area and volume algebraically
3. <strong>Chapter 3</strong>: Apply forms to curves, surfaces, and regions, and establish the operation of aggregating their output
4. <strong>Chapter 4 (this chapter)</strong>: Through three concrete examples—the work–energy theorem, conservation of angular momentum, and conservation of mass—establish the unified principle that pullback rebuilds measuring devices so that integral values are preserved

What this chapter established is the following unified principle:

<strong>When counting in different variables, rebuild the measuring devices so that the integral value does not change.</strong> This is the pullback. Whether it is work along a curve, area or flux on a surface, or total mass in a region—all can be handled by the same idea.

The pullback is the technique of rebuilding measuring devices so that integral values are preserved, and its core lies in the discovery-based derivations we saw in §4.1–§4.3. That is, the flow: “the naive attempt does not match → build a provisional measuring device on finite cells → obtain the general form in the limit $h\to0$.” In the finite-cell version $\Phi_h^\square$, the coefficient is the determinant of finite-difference vectors divided by the cell width; in $\Phi^*$, its limit appears as partial-derivative coefficients and the Jacobian. For $1$-forms the velocity $\gamma'(t)$, for $2$-forms $r$, and for $3$-forms the $3\times3$ determinant $J$ all emerged from measuring finite cells.

> <strong>Checkpoint so far — Chapter 4</strong>
> - The pullback $\Phi^*$ is the operation of rewriting measuring devices on the physical-space side into a form usable in the variables on the parameter-space side, so that the integral value does not change.
> - For a $1$-form, the physical-space measuring device $F(x)\,dx$ is rebuilt on the time side as $\gamma^*(F(x)\,dx)=F(\gamma(t))\,\gamma'(t)\,dt$. On finite intervals the consistency factor is $\Delta x/\Delta t$; in the limit, it becomes the velocity $\gamma'(t)$.
> - For a $2$-form, $dx\wedge dy$ is rebuilt on the polar-coordinate side as $\Phi^*(dx\wedge dy)=r\,dr\wedge d\theta$. On a finite grid, $r\Delta r\sin\Delta\theta$ appears, and in the limit $h\to0$ the coefficient $r$ remains.
> - For a $3$-form, $dx\wedge dy\wedge dz$ is rebuilt on the cylindrical-coordinate side as $\Phi^*(dx\wedge dy\wedge dz)=r\,dr\wedge d\theta\wedge dz$. For a general transformation, $\Phi^*(dx\wedge dy\wedge dz)=J\,du\wedge dv\wedge dw$.
> - The finite-cell version $\Phi_h^\square$ is a provisional measuring device used on finite cells. Its coefficient is fixed by “measurement of the figure spanned by finite-difference vectors, divided by the cell width on the parameter-space side.” When we feed this measuring device to a finite cell, the original measurement comes back. In the limit $h\to0$, this coefficient becomes the coefficient of $\Phi^*$.
> - For $1$-forms a $1\times1$ determinant, for $2$-forms a $2\times2$ determinant, and for $3$-forms a $3\times3$ determinant serve as the consistency factors for rebuilding measuring devices.
> - Chapter 1 §1.4’s $dx = \cos\theta\,dr - r\sin\theta\,d\theta$ was already a prototype of $1$-form pullback.

---

In the next chapter, we finally introduce the <strong>exterior derivative $d$</strong>. We have reached the point of building measuring devices, integrating them, and rebuilding them to suit the variables. What we look at next is change in the measuring devices themselves. The operation that records how a form changes from place to place, producing a form one degree higher, is the exterior derivative $d$.

# Chapter 5: What Does It Mean to Differentiate? — The Exterior Derivative $d$: Integral Quantities and Local Laws

# Chapter 5: What Does It Mean to Differentiate? — The Exterior Derivative $d$: Integral Quantities and Local Laws

### §5.0 The Bridge to Differentiation — Observation Is Integral, Law Is Differential

In Chapter 3 we defined integration over curves, surfaces, and regions in the language of $k$-forms. Work along a curve $\gamma$ is $\int_\gamma \omega$, flux through a surface $S$ is $\iint_S \eta$, and the total mass of a region $V$ is $\iiint_V \Omega$. Each followed the same principle: feed $k$ displacement vectors to a $k$-form (measuring device), obtain a scalar, and aggregate over the entire region.

In Chapter 4 we introduced the operation that rebuilds measuring devices to compute the same integral in different variables—the pullback $\Phi^*$. With that, we also gained a tool for changing the variables of computation while preserving the integral value.

The integrals we now have in hand are all quantities that span an <strong>entire region</strong> (below we call such quantities <strong>global</strong>). Work is the total sum over an entire curve, flux is the total amount crossing an entire surface, and mass is the grand total over an entire region. They depend on how the measuring device is applied and on the choice of region.

But this alone is not what physicists ultimately want. Behind the laws observed as integral quantities, they want to see local relations that hold at each point. Whether Maxwell's equations or the Navier–Stokes equations, the fundamental laws of nature are written as <strong>local</strong> relations—differential equations—that describe <strong>what holds at each point in space and each instant in time</strong>. Global integral quantities depend on the region, but local laws have a universality that does not depend on the region.

> <strong>Note</strong> (the terms global / local) Other books sometimes call a similar contrast <strong>macro / micro</strong>. In this chapter, however, we use global / local to mean the contrast between a quantity integrated over an entire region and a relation that holds at each point—not so much a difference of scale.

Here a fundamental question arises.

> <strong>How do we extract a local law from an integrated quantity?</strong>

The subject of this chapter—the <strong>exterior derivative $d$</strong>—answers this question. $d$ is an operator that acts on a $k$-form and returns a $(k+1)$-form; combined with the integrals defined in Chapter 3, it translates a "global integral measured on the boundary" into "an accumulation of local changes in the interior." In short, <strong>$d$ is the device that converts integral laws into differential laws</strong>.

The structure of this chapter is as follows. First we recall the $df$ introduced in Chapter 1 and build $d\omega$ from the mismatch that remains when a general $1$-form is measured on a closed loop. Next we extend the same idea to $2$-forms and unify Stokes' theorem and Gauss' theorem into a single form. Finally we look at the structure $d^2=0$ and at how the exterior derivative localizes physical laws, connecting to the Hodge star in the next chapter.


### §5.2 The "Mismatch" Revealed by a Closed Loop

#### 5.2.1 What About a General $1$-Form?

What about a general $1$-form

$$\omega = P(x,y,z)\,dx + Q(x,y,z)\,dy + R(x,y,z)\,dz$$

? Here $P, Q, R$ are coefficients that vary from place to place (scalar fields)—the "general $1$-form" introduced in Chapter 3 §3.4.1.

> <strong>Note</strong> (what "general" means) The $df$ treated in §5.1 had coefficients of the special combination $\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}$—a triple derived from partial derivatives of a single function $f$. By contrast, the "general" $\omega$ here has $P, Q, R$ as <strong>three arbitrary scalar fields unrelated to one another</strong>. In other words, we call a $1$-form "general" when it cannot necessarily be written as $\omega = df$. The $y\,dx + x\,dy$ of §5.1.3 happened to be an exact form writable as $d(xy)$, but forms that are not of that kind are rather the norm.

$\omega$ need not represent a force; it can be any measuring device applied along a line.

For this $\omega$, there is no guarantee that the same telescoping sum as in §5.1 works. The most concise way to decide is to integrate on a <strong>closed loop</strong>—a curve whose start and end coincide. If $\int_\gamma \omega$ could be written only as the difference of endpoint values, then on a closed loop we would have to get $f(A)-f(A)=0$.

We write the line integral along a closed loop as $\oint_\gamma \omega$. In general:

$$\oint_\gamma \omega \neq 0$$

If you drag an object once around against friction, the work is not zero; if you go once around a swirling current, you receive net work. This <strong>fact that "closing the loop still does not balance the books" is evidence of local structure such as circulation or vorticity</strong>.

> <strong>Note</strong> (no physics background needed) Readers who have not yet treated friction or water flow in physics need not stop here. What matters now is not the specific physical phenomenon but only the sense that "if the integral on a closed loop is not zero, there is local structure like circulation in that field." The detailed physical correspondences will be touched on in later chapters.

#### 5.2.2 Where Does the Local Information Live?

Then where does this "mismatch left after one circuit" come from? If we think of the closed loop only at a global scale all at once, we cannot tell which points inside contributed how much to the mismatch. Recall how we found $f'(x)$ in Chapter 1—we extracted a rate of change <strong>at a single point</strong> by taking the limit $\Delta x \to 0$ of $\Delta f / \Delta x$.

We use the same idea here. As we shrink the loop more and more, what happens to the value of the integral $\oint \omega$ around one circuit? If the leading term of $\oint \omega$ shrinks in proportion to the <strong>area enclosed</strong> by the loop, then the mismatch per unit area—how much the books fail to balance per unit area—should be determined as a value intrinsic to that point.

Conversely, if it does not scale that way (for example, if it scales with the perimeter of the loop), it cannot be fixed as a per-area quantity, and we cannot call it "a property at that point." So the question is:

> <strong>When a tiny loop is traversed once, does the leading term of $\oint \omega$ scale with the enclosed area? If so, what is the proportionality constant?</strong>

In the next section we actually answer this question with a tiny rectangle placed in the $xy$ plane.

---

### §5.3 Dismantling an Infinitesimal Loop — The Mismatch Is Proportional to Area

#### 5.3.1 A Tiny Rectangle in the $xy$ Plane

Consider a tiny rectangle parallel to the $xy$ plane, with the point $(x, y, z)$ as its lower-left vertex. Let the width in the $x$ direction be $\Delta x$ and the width in the $y$ direction be $\Delta y$. Traverse the four edges of this rectangle once in the <strong>counterclockwise (right-handed) direction</strong>, and integrate $\omega = P\,dx + Q\,dy + R\,dz$.

Let us evaluate the integral on each edge using a first-order Taylor approximation (with $\Delta x, \Delta y$ sufficiently small).

> <strong>Note</strong> (on Taylor expansion) There is no need to be intimidated by the words "Taylor expansion." What we use here is the first-order approximation of a multivariable function—the same thing as $\Delta f \approx f'(x)\,\Delta x$ in Chapter 1 §1.2.1. For example, the value of $Q(x+\Delta x, y)$ shifted by $\Delta x$ in the $x$ direction can be approximated as $Q + \frac{\partial Q}{\partial x}\,\Delta x$ using the partial derivative of $Q$ with respect to $x$. When $\Delta x$ is sufficiently small, terms of order $(\Delta x)^2$ and higher are overwhelmingly smaller than $\Delta x$ and may be ignored—that is what first-order approximation means.

$z$ is fixed, so $dz=0$ and the $R$ term contributes nothing.

<strong>Edge 1 (bottom edge, rightward)</strong>: from $(x, y)$ to $(x+\Delta x, y)$. With $y$ fixed, $dy=0$. $P$ is approximately $P(x, y, z)$. Contribution: $P(x, y, z)\,\Delta x$.

<strong>Edge 2 (right edge, upward)</strong>: from $(x+\Delta x, y)$ to $(x+\Delta x, y+\Delta y)$. $dx=0$. Evaluate $Q$ at the position shifted by $\Delta x$ in the $x$ direction:
$$Q(x+\Delta x, y, z) \approx Q(x, y, z) + \frac{\partial Q}{\partial x}\Delta x$$
Contribution: $\bigl(Q + \frac{\partial Q}{\partial x}\Delta x\bigr)\,\Delta y$.

<strong>Edge 3 (top edge, leftward)</strong>: from $(x+\Delta x, y+\Delta y)$ to $(x, y+\Delta y)$. The direction is negative, so the sign flips. Evaluate $P$ at the position shifted by $\Delta y$ in the $y$ direction:
$$P(x, y+\Delta y, z) \approx P(x, y, z) + \frac{\partial P}{\partial y}\Delta y$$
Contribution: $-\bigl(P + \frac{\partial P}{\partial y}\Delta y\bigr)\,\Delta x$.

<strong>Edge 4 (left edge, downward)</strong>: from $(x, y+\Delta y)$ back to $(x, y)$. Contribution: $-Q(x, y, z)\,\Delta y$.

Summing the contributions from all four edges:

$$\begin{aligned}
\oint \omega &\approx P\Delta x + (Q + \frac{\partial Q}{\partial x}\Delta x)\Delta y - (P + \frac{\partial P}{\partial y}\Delta y)\Delta x - Q\Delta y \\
&= P\Delta x + Q\Delta y + \frac{\partial Q}{\partial x}\Delta x\Delta y - P\Delta x - \frac{\partial P}{\partial y}\Delta x\Delta y - Q\Delta y \\
&= (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,\Delta x\,\Delta y
\end{aligned}$$

The omitted terms are higher order in $\Delta x$ and $\Delta y$.

The terms $P\Delta x$ and $Q\Delta y$ cancel beautifully, leaving only $(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,\Delta x\,\Delta y$ as the leading term.

#### 5.3.2 The Decisive Fact

This result tells us just one thing:

> <strong>The leading term of the mismatch left after one circuit is proportional to the enclosed area $\Delta x\,\Delta y$.</strong>

And the proportionality constant $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$ is precisely the <strong>mismatch per unit area</strong> at the point $(x,y,z)$—a local quantity representing the "strength of vorticity" at that point. More precisely, for the tiny rectangle $R_{\Delta x,\Delta y}$,

$$\lim_{\Delta x,\Delta y\to 0}\frac{1}{\Delta x\,\Delta y}\oint_{\partial R_{\Delta x,\Delta y}}\omega = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$$

is the quantity extracted by this limit.

This is "differentiation" in the same spirit as $f'(x) = \lim_{\Delta x\to 0} \frac{\Delta f}{\Delta x}$ in Chapter 1. Only the denominator has changed—from "distance moved" to "area enclosed"—but the spirit of <strong>extracting a rate of change locally</strong> is unchanged.

> <strong>Note</strong> (why only $\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}$ survives) $\frac{\partial P}{\partial x}$ and $\frac{\partial Q}{\partial y}$ do not appear. The change of $P$ in the $x$ direction ($\frac{\partial P}{\partial x}$) acts in the same direction on the bottom and top edges and cancels; the change of $Q$ in the $y$ direction ($\frac{\partial Q}{\partial y}$) likewise cancels on the right and left edges. What survives is only "the change of $P$ in the $y$ direction" and "the change of $Q$ in the $x$ direction"—the difference of <strong>partial derivatives in mutually orthogonal directions</strong>. This crosswise structure is the key to everything from the next section onward.

---

### §5.4 The Birth of $d$ — A New Measuring Device for Mismatch per Unit Area

#### 5.4.1 Revisiting the Wedge Product

Let us restate the $(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,\Delta x\,\Delta y$ obtained in §5.3 in the language of Chapter 2. In Chapter 2 §2.4.4 we defined the area-measuring device $dx \wedge dy$. This was a device that, when fed two vectors $\mathbf{v}_1, \mathbf{v}_2$, returns the signed area of the shadow they cast onto the $xy$ plane:

$$(dx \wedge dy)(\mathbf{v}_1, \mathbf{v}_2) = \det\begin{pmatrix} dx(\mathbf{v}_1) & dx(\mathbf{v}_2) \\ dy(\mathbf{v}_1) & dy(\mathbf{v}_2) \end{pmatrix}$$

In particular, if we feed the displacement $\Delta x\,\hat{e}_x$ in the $x$ direction and the displacement $\Delta y\,\hat{e}_y$ in the $y$ direction, we get $(dx \wedge dy)(\Delta x\,\hat{e}_x,\; \Delta y\,\hat{e}_y) = \Delta x\,\Delta y$.

#### 5.4.2 Definition of $d\omega$

Written in this language, the result of §5.3 says that for the two edges $\Delta x\,\hat{e}_x,\; \Delta y\,\hat{e}_y$ of an infinitesimal rectangle, some <strong>new $2$-form</strong> returned the leading term $(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,\Delta x\,\Delta y$. We call this $2$-form the <strong>exterior derivative</strong> of $\omega$, and write it $d\omega$:

$$d\omega := (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy$$

$d\omega$ is a $2$-form—it eats two vectors and returns a scalar. Its value represents the mismatch per unit area of a closed loop over the infinitesimal parallelogram spanned by the two vectors fed to it.

Let us organize what is happening here:

- <strong>Input</strong>: $\omega = P\,dx + Q\,dy + R\,dz$ ($1$-form, a line measuring device that eats one vector)
- <strong>Output</strong>: $d\omega = (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy$ ($2$-form, a surface measuring device that eats two vectors)
- <strong>Operation</strong>: $d$ <strong>raises the degree by one</strong>, from 1 to 2

This is exactly the same structure as the $df$ we saw in §5.1. $d$ acts on a $0$-form $f$ and returns the $1$-form $df$; it acts on a $1$-form $\omega$ and returns the $2$-form $d\omega$. <strong>One of the great roles of $d$ is to raise the degree by one.</strong>

> <strong>Checkpoint</strong>
> - $df$ was the exterior derivative from $0$-form to $1$-form. $\int_\gamma df = f(B)-f(A)$ (depends only on the endpoints).
> - For a general $\omega$, $\oint \omega \neq 0$ on a closed loop. To investigate this mismatch, we shrink the loop.
> - On an infinitesimal rectangle in the $xy$ plane, $\oint \omega = (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,\Delta x\,\Delta y +$ higher-order terms. The leading term of the mismatch is proportional to area.
> - We define the $2$-form that measures this proportionality coefficient as $d\omega := (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy$. $d$ is the operator that raises the degree.

---

### §5.5 The Exterior Derivative of a General $1$-Form — Extension to Three Dimensions

#### 5.5.1 The $yz$ Plane and the $zx$ Plane

In §5.3–§5.4 we considered loops only in the $xy$ plane. But in three-dimensional space there are three orientations of surface. On an infinitesimal rectangle in the $yz$ plane, a similar calculation gives $(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z})\,\Delta y\,\Delta z$; on the $zx$ plane we get $(\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,\Delta z\,\Delta x$. These correspond to $dy \wedge dz$ and $dz \wedge dx$, respectively.

The complete formula that follows from this intuition is:

$$d\omega = (\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z})\,dy \wedge dz + (\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,dz \wedge dx + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy$$

> <strong>Note</strong> ($2$-forms measure tilted parallelograms) This $d\omega$ is a $2$-form—a <strong>measuring device that eats two vectors</strong>. The two vectors fed to it need not be parallel to the $xy$ plane. If we feed the two edges $\mathbf{v}_1, \mathbf{v}_2$ of an infinitesimal parallelogram floating obliquely in three-dimensional space, it returns the mismatch per unit area of a closed loop over that surface. It is exactly the same thing we did in §5.3—the only difference is that the surface being measured need not be parallel to a coordinate plane. The mechanism for extracting the area (and orientation) of a parallelogram from two vectors was already verified in Chapter 2 §2.4, when we constructed $dy \wedge dz$ and the like as antisymmetric matrices.

#### 5.5.2 Algebraic Derivation — Leibniz Rule and $d(dx)=0$

The formula above can of course be derived by doing separate loop calculations on each plane. But drawing a loop and adding four edges every time is tedious. What we do here is recast the exterior derivative introduced geometrically in §5.3 as computational algebraic rules, and confirm that these rules do indeed reproduce the exterior derivative. In other words, using the intuition from the $xy$-plane example, we move to a form that can be computed mechanically.

> <strong>Note</strong> (Relation to the axiomatic definition) Many mathematics books take Leibniz's rule and $d(dx)=0$ as the <strong>definition</strong> of $d$. That definition is concise, but it is hard to see why those rules should hold. In this book we start from the dissection of an infinitesimal loop. What we are about to verify is that this geometric $d$ and the algebraic computational rules are consistent. The rules are for computational convenience; <strong>the meaning is in §5.3</strong>. Still, when one looks ahead to higher dimensions, this algebraic definition is indeed very concise.

First, for $\omega = P\,dx + Q\,dy + R\,dz$, we take $d$ to act linearly: $d\omega = d(P\,dx) + d(Q\,dy) + d(R\,dz)$. This is the same as considering loops around tilted parallelograms. The question is $d(P\,dx)$—how does $d$ act on the $1$-form $dx$ with coefficient $P$?

Here, the geometric $d$ obtained in §5.3–§5.4 has already taught us something. For $\omega = P\,dx$ ($Q=R=0$), if we carry out the infinitesimal loop calculation of §5.3 not only in the $xy$ plane but also in the $zx$ plane, $d(P\,dx)$ should have no component on the $yz$ face, and

$$d(P\,dx) = \frac{\partial P}{\partial z}\,(dz \wedge dx) - \frac{\partial P}{\partial y}\,(dx \wedge dy)$$

(the loop on the $xy$ face gives $(0 - \frac{\partial P}{\partial y}) = -\frac{\partial P}{\partial y}$; the loop on the $zx$ face gives $(\frac{\partial P}{\partial z} - 0) = \frac{\partial P}{\partial z}$).

Now recall $dP = \frac{\partial P}{\partial x}\,dx + \frac{\partial P}{\partial y}\,dy + \frac{\partial P}{\partial z}\,dz$ (§5.1). Taking its wedge product with $dx$:

$$dP \wedge dx = (\frac{\partial P}{\partial x}\,dx + \frac{\partial P}{\partial y}\,dy + \frac{\partial P}{\partial z}\,dz) \wedge dx = \frac{\partial P}{\partial z}\,(dz \wedge dx) - \frac{\partial P}{\partial y}\,(dx \wedge dy)$$

(the term with $\frac{\partial P}{\partial x}$ vanishes because $dx \wedge dx = 0$)

This <strong>agrees completely</strong> with the geometric calculation. That is, at least for a term of the form $P\,dx$:

$$d(P\,dx) = dP \wedge dx$$

So only the variation of the coefficient $P$ from place to place attaches to the measuring device in the $dx$ direction as a new area-measuring device.

Comparing the geometric result with Leibniz's rule $d(P\,dx) = dP \wedge dx + P\,d(dx)$, the extra term $P\,d(dx)$ must be zero. Since $P$ is an arbitrary function, this can hold in general only if $d(dx)=0$—that is, $d(dx) = 0$ is required.

Generalizing this observation, we arrive at the following <strong>graded Leibniz rule</strong>. $P$ is a $0$-form and $dx$ is a $1$-form; the behavior of $d$ on the “product” of a $0$-form and a $1$-form is:

$$d(P\,dx) = (dP) \wedge dx + P\,d(dx)$$

$dP$ is known—from §5.1, $dP = \frac{\partial P}{\partial x}\,dx + \frac{\partial P}{\partial y}\,dy + \frac{\partial P}{\partial z}\,dz$. The question is the value of $d(dx)$.

Here, the exterior derivative of the coordinate function $x$ is $dx$ ($d(x) = dx$). The $dx$ of Cartesian coordinates is a reference measuring device whose coefficients do not change from place to place. So even if we send $dx$ itself once around an infinitesimal loop, no mismatch per unit area appears. The same holds for $dy$ and $dz$. Therefore, for the coordinate basis, we adopt the following computational rule:

$$d(dx) = d(dy) = d(dz) = 0$$

Then:

$$d(P\,dx) = (\frac{\partial P}{\partial x}\,dx + \frac{\partial P}{\partial y}\,dy + \frac{\partial P}{\partial z}\,dz) \wedge dx + P\,0$$

Using the antisymmetry of $\wedge$ ($dx \wedge dx = 0$, $dy \wedge dx = -dx \wedge dy$):

$$d(P\,dx) = \frac{\partial P}{\partial x}\,(dx \wedge dx) + \frac{\partial P}{\partial y}\,(dy \wedge dx) + \frac{\partial P}{\partial z}\,(dz \wedge dx) = \frac{\partial P}{\partial z}\,(dz \wedge dx) - \frac{\partial P}{\partial y}\,(dx \wedge dy)$$

Similarly:

$$\begin{aligned}
d(Q\,dy) &= (\frac{\partial Q}{\partial x}\,dx + \frac{\partial Q}{\partial y}\,dy + \frac{\partial Q}{\partial z}\,dz) \wedge dy = \frac{\partial Q}{\partial x}\,(dx \wedge dy) - \frac{\partial Q}{\partial z}\,(dy \wedge dz) \\
d(R\,dz) &= (\frac{\partial R}{\partial x}\,dx + \frac{\partial R}{\partial y}\,dy + \frac{\partial R}{\partial z}\,dz) \wedge dz = -\frac{\partial R}{\partial x}\,(dz \wedge dx) + \frac{\partial R}{\partial y}\,(dy \wedge dz)
\end{aligned}$$

Adding the three and collecting in the order of the basis $dy \wedge dz,\; dz \wedge dx,\; dx \wedge dy$ (this cyclic order is foreshadowing for consistency with the right-handed system in the next chapter):

$$\begin{aligned}
d\omega &= (-\frac{\partial Q}{\partial z} + \frac{\partial R}{\partial y})\,dy \wedge dz + (\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,dz \wedge dx + (-\frac{\partial P}{\partial y} + \frac{\partial Q}{\partial x})\,dx \wedge dy \\
&= (\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z})\,dy \wedge dz + (\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,dz \wedge dx + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy
\end{aligned}$$

This includes the $xy$ component $(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})$ derived geometrically in §5.3, and the $yz$ and $zx$ components follow the same cross pattern.

#### 5.5.3 The Pattern of the Coefficients

Notice how the coefficients are arranged. $(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z},\; \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x},\; \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})$ are obtained by taking partial derivatives of $(P, Q, R)$ <strong>with respect to axes other than their own, crossing them, and taking differences</strong>. There is a cyclic symmetry:

$$\begin{aligned}
dy \wedge dz &\longleftrightarrow \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \\
dz \wedge dx &\longleftrightarrow \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \\
dx \wedge dy &\longleftrightarrow \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}
\end{aligned}$$

> <strong>Note</strong> (A guidepost for experienced readers) Readers who already know vector analysis will find these three coefficients familiar. In this book we do not rely on their names; we first build the operation $d$ itself. The correspondence will be organized in later chapters.

> <strong>Checkpoint</strong>
> - The exterior derivative $d\omega$ of a general $1$-form $\omega$ is a $2$-form whose coefficients are the cross differences of partial derivatives $(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},\; \frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},\; \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})$.
> - The computational rules are threefold: (1) linearity, (2) Leibniz rule $d(P\,dx) = dP \wedge dx + P\,d(dx)$, (3) $d(dx)=d(dy)=d(dz)=0$.
> - The result is fully consistent with the infinitesimal loop calculation of §5.3.

---

### §5.6 Accumulate It, and Only the Boundary Remains — Stokes' Theorem

#### 5.6.1 Tiling a Surface

In §5.3 we computed $\oint \omega$ around <strong>a single</strong> infinitesimal rectangle and saw that its leading term is the product of $d\omega$ and area. What happens if we <strong>tile an entire surface</strong> with these infinitesimal rectangles and add everything up?

Divide a surface $S$ into small coordinate patches and cut each into infinitesimal rectangles on its parameter plane (this is exactly the idea of a surface element from Chapter 3 §3.2). For each infinitesimal rectangle, the integral of $\omega$ around the boundary in the orientation matching the surface has, as its leading term, the value obtained by feeding the surface element to $d\omega$.

Here we consider the case where the surface can be smoothly parameterized and a natural orientation is induced on the boundary as well. Reversing the orientation of the surface simultaneously reverses the direction in which the boundary is traced. Only after fixing this “pairing of surface orientation and boundary orientation” do the signs on the two sides agree.

#### 5.6.2 Interior Edges Cancel

Here is the decisive geometric observation. Focus on <strong>the edge shared by two adjacent rectangles</strong>. For the rectangle on the left, that edge is traced “upward”; for the rectangle on the right, it is traced “downward.” Because the paths run in opposite directions, the line integral of $\omega$ <strong>cancels completely</strong> on this edge.

This cancellation occurs on <strong>every shared edge</strong> in the interior of the surface $S$. No matter how finely we partition and add, the contributions from interior edges vanish in plus-minus pairs.

#### 5.6.3 Only the Boundary Survives

Then which edges survive without cancellation—<strong>edges for which no adjacent rectangle exists</strong>, that is, edges along the <strong>boundary $\partial S$</strong> of the surface $S$.

In other words:

$$\oint_{\partial S} \omega = \iint_S d\omega$$

The left-hand side is “the line integral of $\omega$ along the one-dimensional closed curve that is the boundary of the surface”; the right-hand side is “the sum of mismatch densities from the countless infinitesimal loops tiled in the interior of the surface.” In the limit of a finer and finer partition, only the cancellation of interior edges remains, and the two sides agree.

This is the <strong>Kelvin–Stokes theorem</strong> (also called simply Stokes' theorem).

Writing out the components for $\omega = P\,dx + Q\,dy + R\,dz$ explicitly:

$$\oint_{\partial S} \bigl(P\,dx + Q\,dy + R\,dz\bigr) = \iint_S \Bigl( (\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z})\,dy \wedge dz + (\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,dz \wedge dx + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy \Bigr)$$

In the matrix language we have used since Chapter 2, the $2$-form on the right-hand side is represented by the antisymmetric matrix $\mathbf{J}^T - \mathbf{J}$, where $\mathbf{J}$ is the Jacobian matrix of the coefficient vector $(P,Q,R)$. If $\mathbf{v}_1, \mathbf{v}_2$ are the two edges of a surface element, then $(d\omega)(\mathbf{v}_1, \mathbf{v}_2) = \mathbf{v}_1^T(\mathbf{J}^T - \mathbf{J})\mathbf{v}_2$. All components are written out in Appendix B.3; consult it as needed.

The structure of this theorem is remarkably simple. <strong>Integral measured on the global boundary</strong> $=$ <strong>accumulation of local mismatch ($d\omega$) in the interior</strong>. $d$ is the device that <strong>translates</strong> information about $\omega$ on the boundary $\partial S$ into information about $d\omega$ in the interior $S$.

> <strong>Note</strong> (Assumptions used in localization) The tiling explanation here assumes a sufficiently smooth surface and field that can be divided into sufficiently fine coordinate patches. When there are cusps on the boundary, self-intersections, singular points, and the like, patch decomposition and orientation must be handled separately. In this book we treat the smooth cases ordinarily used in physics.

> <strong>Note</strong> (Correspondence with Chapter 3) When we defined surface integrals in Chapter 3 §3.2.1, we fed $dx \wedge dy$ to the surface element $(\mathbf{r}_u\Delta u,\;\mathbf{r}_v\Delta v)$. Here too, we divide the surface into small surface elements, act with the measuring device on each element, and organize the contributions that cancel in the interior.

> <strong>Checkpoint</strong>
> - If we tile a surface $S$ with infinitesimal loops, interior edges cancel and only the contribution from the boundary $\partial S$ remains.
> - $\oint_{\partial S} \omega = \iint_S d\omega$. A global boundary integral equals an integral of the local exterior derivative.
> - As with surface integrals in Chapter 3, we divide the surface into small patches, act with the measuring device on each patch, and aggregate.

---

### §5.7 The Same Thing One Degree Higher — Exterior Derivative of a $2$-Form and Divergence

#### 5.7.1 A $2$-Form Is a Measuring Device for Surfaces

In Chapter 3 §3.4.2 we wrote a general $2$-form in the form

$$\eta = A\,dy \wedge dz + B\,dz \wedge dx + C\,dx \wedge dy$$

This is a measuring device for flux through a surface. As we saw in Chapter 2 §2.4.5, the three basis $2$-forms each measure the area of the projection onto the $yz$, $zx$, and $xy$ planes, respectively.

#### 5.7.2 Measuring on the Faces of a Tiny Rectangular Box

In the same spirit as §5.3, we now integrate $\eta$ over <strong>all six faces</strong> of a tiny rectangular box in space, $[x, x+\Delta x] \times [y, y+\Delta y] \times [z, z+\Delta z]$. We align the orientations outward.

For the term $C\,dx \wedge dy$, consider only the bottom and top faces perpendicular to $z$:

- <strong>Bottom face</strong> ($z$, outward direction is $-z$): evaluate $C(x,y,z)$ with the orientation of $-dx \wedge dy$ → approximately $-C(x,y,z)\,\Delta x\,\Delta y$
- <strong>Top face</strong> ($z+\Delta z$, outward direction is $+z$): $C(x,y,z+\Delta z) \approx C + \frac{\partial C}{\partial z}\Delta z$ → approximately $(C + \frac{\partial C}{\partial z}\Delta z)\,\Delta x\,\Delta y$

Summing, the $C\Delta x\Delta y$ terms cancel and $\frac{\partial C}{\partial z}\,\Delta x\,\Delta y\,\Delta z$ remains. The term $A\,dy \wedge dz$ contributes $\frac{\partial A}{\partial x}\,\Delta x\,\Delta y\,\Delta z$ from the faces perpendicular to $x$, and the term $B\,dz \wedge dx$ contributes $\frac{\partial B}{\partial y}\,\Delta x\,\Delta y\,\Delta z$ from the faces perpendicular to $y$.

The total over all six faces is:

$$\iint_{\partial (\text{box})} \eta \approx (\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z})\,\Delta x\,\Delta y\,\Delta z$$

Here too the structure is the same—<strong>the leading term of the mismatch measured on the surface is proportional to the enclosed volume</strong>. The proportionality constant $\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z}$ represents the "outflow per unit volume."

#### 5.7.3 Definition of $d\eta$ and Algebraic Derivation

As a $3$-form that eats the three edges $\Delta x\,\hat{e}_x,\; \Delta y\,\hat{e}_y,\; \Delta z\,\hat{e}_z$ of the box:

$$d\eta := (\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z})\,dx \wedge dy \wedge dz$$

This formula can also be derived from the algebraic rules of §5.5.2. First, as we did in §5.5.2, let us confirm for the term $A\,dy \wedge dz$ that the geometric result is consistent with the Leibniz rule.

According to the geometric calculation in §5.7.2, the contribution of $A\,dy \wedge dz$ was $\frac{\partial A}{\partial x}\,\Delta x\,\Delta y\,\Delta z$. In the language of $dx \wedge dy \wedge dz$, this is $\frac{\partial A}{\partial x}\,dx \wedge dy \wedge dz$.

On the other hand, applying the Leibniz rule to $d(A\,dy \wedge dz)$ gives:

$$d(A\,dy \wedge dz) = dA \wedge dy \wedge dz + A\,d(dy \wedge dz)$$

Here, as in §5.5.2, using $d(dy)=d(dz)=0$:

$$d(dy \wedge dz) = d(dy) \wedge dz - dy \wedge d(dz) = 0 \wedge dz - dy \wedge 0 = 0$$

so the second term vanishes and only the first remains:

$$dA \wedge dy \wedge dz = (\frac{\partial A}{\partial x}\,dx + \frac{\partial A}{\partial y}\,dy + \frac{\partial A}{\partial z}\,dz) \wedge dy \wedge dz$$

By antisymmetry of $\wedge$ ($dy \wedge dy = 0$, $dz \wedge dz = 0$), the terms with $\frac{\partial A}{\partial y}$ and $\frac{\partial A}{\partial z}$ vanish, leaving only $\frac{\partial A}{\partial x}\,dx \wedge dy \wedge dz$. This <strong>agrees completely</strong> with the geometric calculation in §5.7.2.

The terms $B\,dz \wedge dx$ and $C\,dx \wedge dy$ are similar; adding the three yields:

$$d\eta = (\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z})\,dx \wedge dy \wedge dz$$

$d$ has accomplished the promotion $2$-form $\to$ $3$-form.

#### 5.7.4 Gauss' Theorem

By the same tiling argument as in §5.6—this time filling the solid $V$ with tiny rectangular boxes—internal faces cancel and only the outer surface $\partial V$ remains:

$$\iint_{\partial V} \eta = \iiint_V d\eta$$

This is <strong>Gauss' theorem</strong>. It has <strong>exactly the same form</strong> as Stokes' theorem, only with the dimension shifted by one. Placed side by side, the parallel is obvious: $\omega$ ($1$-form) $\to$ $d\omega$ ($2$-form) $\to$ surface $S$, $\eta$ ($2$-form) $\to$ $d\eta$ ($3$-form) $\to$ solid $V$.

Writing out the components explicitly for $\eta = A\,dy \wedge dz + B\,dz \wedge dx + C\,dx \wedge dy$:

$$\iint_{\partial V} \bigl(A\,dy \wedge dz + B\,dz \wedge dx + C\,dx \wedge dy\bigr) = \iiint_V (\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z})\,dx \wedge dy \wedge dz$$

> <strong>Note</strong> (a guide for readers already familiar with vector calculus) Readers who already know vector analysis may recognize $\frac{\partial A}{\partial x}+\frac{\partial B}{\partial y}+\frac{\partial C}{\partial z}$. In this book we first obtain this quantity as the exterior derivative of a $2$-form, and we keep that order of presentation. The correspondence with names will be organized in a later chapter.

> <strong>Checkpoint so far</strong>
> - The exterior derivative $d\eta$ of a $2$-form $\eta$ is a $3$-form whose coefficient is $\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z}$.
> - The derivation can be done mechanically with the same algebraic rules as §5.5 (Leibniz rule $+$ $d(dx)=0$).
> - $\iint_{\partial V} \eta = \iiint_V d\eta$. Stokes ($1$-form $\to$ surface) and Gauss ($2$-form $\to$ solid) differ only in degree; the structure is the same.

---

### §5.8 $d^2 = 0$ — The Mismatch of a Mismatch Leaves Nothing Behind

Before unifying Stokes' theorem and Gauss' theorem in the next section, let us confirm one more basic structure of the exterior derivative. $d$ raises the degree by one, but applying it twice in succession leaves no new mismatch. This fact is also connected to the geometric structure we will see later: "the boundary of a boundary cancels as an oriented sum."

#### 5.8.1 $d(df) = 0$

In §5.1 we defined $df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy + \frac{\partial f}{\partial z}\,dz$. Let us apply the exterior derivative once more. Using the formula from §5.5 with $P = \frac{\partial f}{\partial x},\; Q = \frac{\partial f}{\partial y},\; R = \frac{\partial f}{\partial z}$:

$$d(df) = \left(\frac{\partial^2 f}{\partial y \partial z} - \frac{\partial^2 f}{\partial z \partial y}\right) dy \wedge dz + \left(\frac{\partial^2 f}{\partial z \partial x} - \frac{\partial^2 f}{\partial x \partial z}\right) dz \wedge dx + \left(\frac{\partial^2 f}{\partial x \partial y} - \frac{\partial^2 f}{\partial y \partial x}\right) dx \wedge dy$$

By symmetry of mixed partial derivatives (if $f$ is $C^2$ (twice continuously differentiable), then $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$, etc.; see Chapter 1 §1.2), every coefficient vanishes:

$$d(df) = 0$$

> <strong>Note</strong> ($d^2=0$ in the axiomatic viewpoint and the $C^2$ condition) When we compute concretely in coordinates, we see that $d^2=0$ is inevitable from symmetry of mixed partial derivatives and antisymmetry of the wedge product. From the axiomatic standpoint of differential forms, one may instead read things the other way around: requiring $d^2=0$ (as part of the definition) means we are implicitly working with a class of functions for which symmetry of mixed partial derivatives holds ($C^2$ functions). In this book we first understand it through concrete calculation, as the mechanism that prevents contradictions in the hierarchy of physical laws.

#### 5.8.2 $d(d\omega) = 0$

Apply the formula of §5.7 to the $d\omega$ of §5.5. With $A = \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z},\; B = \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x},\; C = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$:

$$d(d\omega) = \left(\frac{\partial^2 R}{\partial x \partial y} - \frac{\partial^2 Q}{\partial x \partial z} + \frac{\partial^2 P}{\partial y \partial z} - \frac{\partial^2 R}{\partial y \partial x} + \frac{\partial^2 Q}{\partial z \partial x} - \frac{\partial^2 P}{\partial z \partial y}\right) dx \wedge dy \wedge dz$$

Expanding and rearranging the expression in parentheses:

$$\left(\frac{\partial^2 R}{\partial x \partial y} - \frac{\partial^2 Q}{\partial x \partial z}\right) + \left(\frac{\partial^2 P}{\partial y \partial z} - \frac{\partial^2 R}{\partial y \partial x}\right) + \left(\frac{\partial^2 Q}{\partial z \partial x} - \frac{\partial^2 P}{\partial z \partial y}\right)$$

By symmetry of mixed partial derivatives ($\frac{\partial^2 R}{\partial y \partial x}=\frac{\partial^2 R}{\partial x \partial y}$, etc.), the six terms cancel in three pairs and the sum is zero:

$$d(d\omega) = 0$$

> <strong>Checkpoint so far</strong>
> - $d^2 = 0$: applying the exterior derivative twice always gives zero. Symmetry of mixed partial derivatives and antisymmetry of the wedge produce the cancellation.
> - Several identities familiar to readers who already know vector calculus—"it vanishes when you differentiate twice"—will be organized in a later chapter as other expressions of this $d^2=0$.

---

### §5.9 Unifying the Exterior Derivative — One Formula, One Rule

#### 5.9.1 Stokes and Gauss Were the Same Formula

Place Stokes' theorem $\oint_{\partial S}\omega = \iint_S d\omega$ from §5.6 and Gauss' theorem $\iint_{\partial V}\eta = \iiint_V d\eta$ from §5.7 side by side. Only the number of integral signs differs—$\oint$, $\iint$, $\iiint$—yet the structure is identical. If $M$ is a curve, we write $\int$ (1-dimensional); if a surface, $\iint$ (2-dimensional); if a solid, $\iiint$ (3-dimensional)—the number of integral signs is determined only by the dimension of $M$.

So, regardless of dimension, we write uniformly:

$$\int_{\partial M} \omega = \int_M d\omega$$

Here $\omega$ is a $k$-form, $M$ is a $(k+1)$-dimensional region, and $\partial M$ is its $k$-dimensional boundary. For $k=0$, with the oriented boundary $\partial M=\{B\}-\{A\}$, this is the fundamental theorem of calculus: $\int_{\partial M} f=f(B)-f(A)=\int_M df$; for $k=1$ it is Stokes' theorem; for $k=2$ it is Gauss' theorem. All fit into this single line.

The power of this unified form stands out even more in combination with $d^2=0$ from §5.8. Replacing $\omega$ by $d\omega$ in $\int_{\partial M} \omega = \int_M d\omega$:

$$\int_{\partial(\partial M)} \omega = \int_{\partial M} d\omega = \int_M d(d\omega) = 0$$

That is, <strong>"the boundary of a boundary is zero as an oriented sum"</strong> ($\partial^2 M = 0$) and <strong>$d^2=0$</strong> correspond to each other. This does not mean that the second boundary is always empty as a set. For example, if we subdivide the boundary of a polygon further into boundary pieces, vertices appear—but counted with orientation, contributions from adjacent edges cancel. $d^2=0$ is the algebraic portrait of this topological cancellation.

> <strong>Note</strong> (three dimensions suffice) Because the stage of this book is three-dimensional space, the dimension of $M$ is 1, 2, or 3, and $\omega$ is a $0$-form, $1$-form, or $2$-form. We do not enter $k=3$ ($M$ four-dimensional). Still, it does no harm to keep in the back of your mind that this formula holds regardless of $k$.

#### 5.9.2 Exterior Derivative of a General $k$-Form

Likewise, the action of $d$ collapses into one pattern regardless of degree. When an arbitrary $k$-form $\omega$ is written as a sum of coefficients $a_{i_1\cdots i_k}$ and basis elements $dx_{i_1}\wedge\cdots\wedge dx_{i_k}$:

$$d\omega = \sum \Bigl( \sum_j \frac{\partial a_{i_1\cdots i_k}}{\partial x_j}\,dx_j \Bigr) \wedge dx_{i_1}\wedge\cdots\wedge dx_{i_k}$$

For this book we need only the three cases $k=0,1,2$, written out concretely in §5.1 ($df$), §5.5 ($d\omega$), and §5.7 ($d\eta$). The general form above is only confirmation that "at every degree, take the total differential of the coefficients and attach with the wedge"—a single principle.

#### 5.9.3 Summary of Computational Rules

All computations of the exterior derivative $d$ built in this chapter are summarized in the following four rules:

1. <strong>Action on a $0$-form</strong>: $df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy + \frac{\partial f}{\partial z}\,dz$ (the definition since Chapter 1 §1.2)
2. <strong>Linearity</strong>: $d(\omega_1 + \omega_2) = d\omega_1 + d\omega_2$
3. <strong>Graded Leibniz rule</strong>: $d(f\,\omega) = df \wedge \omega + f\,d\omega$
4. <strong>Exterior derivative of coordinate bases is zero</strong>: $d(dx) = d(dy) = d(dz) = 0$

Rule 4 reflects the geometric fact that the coordinate bases $dx, dy, dz$ themselves have no coefficients that vary with position, so measuring them on a tiny loop produces no local mismatch. It is also consistent with $d^2=0$ in §5.8.

With only these four rules, the exterior derivative of any form from $0$-form to $3$-form can be computed mechanically. In fact, every calculation treated in this chapter is nothing but a combination of these rules.

> <strong>Note</strong> (commutativity with pullback—payoff of a Chapter 4 foreshadowing) As foreshadowed in Chapter 4, between pullback $\Phi^*$ and exterior derivative $d$ there holds the commutation relation
> $$\Phi^*(d\omega) = d(\Phi^*\omega)$$
> "differentiate then pull back" and "pull back then differentiate" give the same result. This property cannot be derived directly from the four rules above, but if we recall that $d$ is the operation that "measures local mismatch" and $\Phi^*$ is the operation that "relabels coordinates," it is natural—the structure of local mismatch does not depend on how coordinates are chosen. This fact will be an important footing when we consider differential forms on general manifolds in Chapter 11.

> <strong>Checkpoint so far</strong>
> - A single line $\int_{\partial M} \omega = \int_M d\omega$ unifies the fundamental theorem of calculus, Stokes' theorem, and Gauss' theorem.
> - Computation of $d$ is summarized in four rules ($df$, linearity, Leibniz rule, $d(dx)=0$).
> - $d^2=0$ and $\partial^2 M=0$ echo each other as algebraic truth and geometric truth.

---

### §5.10 From Integrals to Differential Equations — Localizing Physical Laws

#### 5.10.1 Turning Integral Laws into Differential Laws

Let us return to the question posed at the opening of this chapter.

> <strong>How do we extract a local law from an integrated quantity?</strong>

The answer lies in the two tools we have developed—<strong>Stokes' theorem</strong> and the <strong>exterior derivative $d$</strong>.

Many fundamental laws of physics are discovered first in <strong>integral form</strong>. They take the shape: a quantity measured on the boundary of a region equals the total of sources inside:

$$\int_{\partial M} \omega = \int_M \eta$$

The left-hand side is the integral measured on the boundary (a global observable); the right-hand side is the integral of sources in the interior (a global total). $\omega$ and $\eta$ are differential forms of the appropriate degrees.

Apply Stokes' theorem to the left-hand side. Since $\int_{\partial M} \omega = \int_M d\omega$:

$$\int_M d\omega = \int_M \eta$$

Rearranging:

$$\int_M (d\omega - \eta) = 0$$

This is the decisive moment. If this equality holds for <strong>every smooth region $M$</strong>, including sufficiently small ones, the integrand form must vanish identically at each point. For if there were a point where $d\omega - \eta \neq 0$, the integral over a tiny region around that point would not be zero—a contradiction. Here too we are considering the case where the fields are sufficiently smooth and contain no singular concentrated sources.

Therefore:

$$d\omega = \eta$$

This is the <strong>local differential law extracted from the integral law</strong>. $d$ has functioned precisely as the operator that converts an integral equation into a differential equation.

In other words, the exterior derivative $d$ is not merely a symbol that raises the degree of a form. It is the operator that translates a law observed on the boundary into a law that holds at each point in the interior.

#### 5.10.2 Examples from Physics

A typical instance of this pattern is the fundamental laws of electromagnetism.

> <strong>Note</strong> (for readers who have not yet studied electromagnetism) In this section we are not after the detailed content of electromagnetism, but after the mechanism by which an integral law becomes a local one. Think of $E,D,B,H,J,\rho$ not so much as names of physical quantities as symbols standing for "quantities measured along a line," "quantities measured through a surface," and "quantities measured over a volume."

> <strong>Note</strong> (for readers who learned electromagnetism through vector calculus) Here we choose the degree of each form according to the dimension of the object over which we integrate, rather than treating the fields as ordinary three-component vectors. Because $E$ and $H$ are integrated along lines, they are $1$-forms; because $D,B,J$ are integrated through surfaces, they are $2$-forms; because $\rho$ is integrated over volume, it is a $3$-form. The correspondence with the usual vector-calculus notation will be organized after we introduce the Hodge star.

In electromagnetism, the object of integration depends on the kind of quantity: some are measured along lines, some through surfaces, some over volume. Schematically, we can read the situation as follows.

| Quantity | What is measured | Form |
| --- | --- | --- |
| $E,H$ | along a line | $1$-form |
| $D,B,J$ | through a surface | $2$-form |
| $\rho$ | over a volume | $3$-form |

For example, Gauss's law for charge takes the form

$$
\int_{\partial V}D=\int_V\rho
$$

The left-hand side is the total flux of $D$ passing outward through the closed surface $\partial V$; the right-hand side is the total charge contained in the interior $V$. By Stokes' theorem,

$$
\int_{\partial V}D=\int_V dD
$$

so

$$
\int_V dD=\int_V\rho
$$

If this holds for every region $V$, then

$$
dD=\rho
$$

Similarly, the law that the net magnetic flux through a closed surface is zero can be written

$$
\int_{\partial V}B=0
$$

By Stokes' theorem,

$$
\int_V dB=0
$$

and if this holds for every $V$, then

$$
dB=0
$$

Laws that include time variation have the same type. For a surface $S$,

$$
\int_{\partial S}E
=
-\frac{\partial}{\partial t}\int_S B
$$

implies

$$
dE=-\frac{\partial B}{\partial t}
$$

and

$$
\int_{\partial S}H
=
\int_S J+\frac{\partial}{\partial t}\int_S D
$$

implies

$$
dH=J+\frac{\partial D}{\partial t}
$$

Here $d$ is the exterior derivative in the spatial directions, and time variation is represented by $\partial/\partial t$.

Thus the fundamental equations of electromagnetism appear, in the language of this chapter, as expressions of the same type:

$$
dD=\rho,\qquad
dB=0,\qquad
dE=-\frac{\partial B}{\partial t},\qquad
dH=J+\frac{\partial D}{\partial t}
$$

What matters here is not to memorize these as new formulas of electromagnetism. The single point is that an integral law measured on the boundary passes, via the exterior derivative $d$, to a local law in the interior.

On the other hand, relating $E$ to $D$, or $B$ to $H$, requires a convention for how space and the medium are measured. Likewise, matching quantities measured along lines to quantities measured through surfaces requires additional rules for how length, area, and volume are measured. The Hodge star, which we introduce in the next chapter, is the tool that supplies this correspondence.

A detailed development including component formulas is deferred to Appendix C, "Integral Forms of Electromagnetism and Differential Forms."

> <strong>Checkpoint so far</strong>
> - Physical laws are often given in the form $\int_{\partial M} \omega = \int_M \eta$.
> - By Stokes' theorem, rewrite $\int_{\partial M} \omega = \int_M d\omega$; since the equality holds for every $M$, we obtain $d\omega = \eta$ (the local law).
> - This localization, however, is an argument in regions where the fields are sufficiently smooth and contain no singular concentrated sources.
> - $d$ is the operator that converts integral laws into differential laws.

---

### §5.11 Outlook Toward Part II — Foreshadowing the Hodge Star

In this chapter we have acquired the powerful operator called the exterior derivative $d$. $d$ maps:

- $0$-form $\to$ $1$-form: $df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy + \frac{\partial f}{\partial z}\,dz$
- $1$-form $\to$ $2$-form: $d\omega = (\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z})\,dy\wedge dz + (\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x})\,dz\wedge dx + (\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y})\,dx\wedge dy$
- $2$-form $\to$ $3$-form: $d\eta = (\frac{\partial A}{\partial x}+\frac{\partial B}{\partial y}+\frac{\partial C}{\partial z})\,dx\wedge dy\wedge dz$

Each time the degree rises by one step, the coefficients rearrange in a different pattern. And $d^2=0$ guarantees that no contradiction can slip in among these levels.

Yet one asymmetry stands out. A $0$-form and a $3$-form each have 1 independent component; a $1$-form and a $2$-form each have 3—symmetry in the pattern $1, 3, 3, 1$ (as we saw in Chapter 2 §2.5.9–§2.5.10). This symmetry is no accident. In three-dimensional space with Cartesian coordinates, once we add rules for measuring length, area, and volume, a "dictionary" appears that links forms of the same information content.

That dictionary is the <strong>Hodge star</strong> $\ast$, which we introduce in the next chapter. But $\ast$ is not a mere relabeling of symbols. It depends on which direction corresponds to which face, how area and volume are measured, and how orientation is fixed. For that reason we do not yet use concrete correspondence formulas in this chapter.

What we have built so far is, after all, only $d$. $d$ raises the degree by one, extracts local mismatch, and converts integral laws into local laws. Yet $d$ alone cannot yet reconstruct the familiar operations of vector analysis. To match $1$-forms with $2$-forms, we need the additional rules for how length, area, and volume are measured in space—the <strong>metric</strong>.

In the next chapter we define those rules of "measurement" as the Hodge star $\ast$. To the $d$ constructed in Chapter 5 we add $\ast$ in Chapter 6, and use the two together to rebuild the familiar operations of vector analysis in later chapters. From here we move into the core of Part II—unmasking div, grad, and curl.

---

> <strong>Checkpoint so far — Chapter 5</strong>
> - The exterior derivative $d$ is the operator that maps a $k$-form to a $(k+1)$-form: $0$-form $\to$ $1$-form ($df$), $1$-form $\to$ $2$-form, $2$-form $\to$ $3$-form.
> - There are four computational rules: the definition of $df$, linearity, the Leibniz rule $d(f\omega) = df\wedge\omega + f\,d\omega$, and $d(dx)=d(dy)=d(dz)=0$.
> - The geometric origin is §5.3's dissection of a tiny loop: the mismatch around a closed loop scales with area, and the proportionality constant is $d\omega$.
> - Stokes' theorem $\int_{\partial M} \omega = \int_M d\omega$ is the universal bridge linking boundary and interior.
> - $d^2 = 0$ comes from the symmetry of mixed partial derivatives and the antisymmetry of the wedge product; geometrically it corresponds to "the boundary of a boundary is zero as an oriented sum."
> - $d$ is the operator that converts integral laws into local differential laws—an indispensable role in the formulation of physics.
> - In the next chapter we add rules for measuring length, area, and volume, and organize the correspondence between $d$ and the operations of vector analysis through the Hodge star $\ast$.

---

## Appendix B: Matrix Representation of the Exterior Derivative

The main text of this chapter proceeded with the basis $dx, dy, dz$ and the algebra of the wedge product. Here we rewrite the exterior derivative in the language of matrix representations, following the book's convention since Chapter 2 — <strong>arranging every component without exception into matrices</strong>.

### B.1 $0$-form: the $1 \times 3$ row vector of $df$

For $f = f(x,y,z)$, as defined in Chapter 1 §1.2:

$$df = \frac{\partial f}{\partial x}\,dx + \frac{\partial f}{\partial y}\,dy + \frac{\partial f}{\partial z}\,dz$$

As a row vector ($1 \times 3$ matrix):

$$df = \begin{pmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} & \frac{\partial f}{\partial z} \end{pmatrix}$$

### B.2 $1$-form: the Jacobian matrix $\mathbf{J}$ of the coefficients

For $\omega = P\,dx + Q\,dy + R\,dz$, the $3 \times 3$ matrix that arranges <strong>all</strong> partial derivatives of the coefficients $(P,Q,R)$ is:

$$\mathbf{J} := \begin{pmatrix}
\frac{\partial P}{\partial x} & \frac{\partial P}{\partial y} & \frac{\partial P}{\partial z} \\
\frac{\partial Q}{\partial x} & \frac{\partial Q}{\partial y} & \frac{\partial Q}{\partial z} \\
\frac{\partial R}{\partial x} & \frac{\partial R}{\partial y} & \frac{\partial R}{\partial z}
\end{pmatrix}$$

This is the Jacobian matrix of the vector field obtained by stacking $(P,Q,R)$ as a column. The reason §5.1 said that "a mere matrix of partial derivatives is not enough" is precisely that this $\mathbf{J}$ is not antisymmetric.

### B.3 $d\omega = \mathbf{J}^T - \mathbf{J}$

The result of §5.5 is:

$$d\omega = (\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z})\,dy \wedge dz + (\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,dz \wedge dx + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy$$

Following the convention of Chapter 2 §2.4.4, we seek the antisymmetric matrix $\mathbf{M}$ such that $(d\omega)(\mathbf{v}_1, \mathbf{v}_2) = \mathbf{v}_1^T \mathbf{M} \mathbf{v}_2$ for arbitrary column vectors $\mathbf{v}_1, \mathbf{v}_2$.

Writing out the entries of $\mathbf{J}^T - \mathbf{J}$:

$$\mathbf{J}^T - \mathbf{J} = \begin{pmatrix}
0 & \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} & \frac{\partial R}{\partial x} - \frac{\partial P}{\partial z} \\
\frac{\partial P}{\partial y} - \frac{\partial Q}{\partial x} & 0 & \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \\
\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} & \frac{\partial Q}{\partial z} - \frac{\partial R}{\partial y} & 0
\end{pmatrix}$$

With the Chapter 2 convention for representing a $2$-form by an antisymmetric matrix, this gives:

$$d\omega = \mathbf{J}^T - \mathbf{J}$$

Thus, <strong>the matrix representation of the exterior derivative $d\omega$ is the antisymmetric matrix obtained by subtracting the Jacobian matrix of the coefficients from its transpose.</strong>

### B.4 $2$-form: $d\eta$ and the trace of the Jacobian matrix

For $\eta = A\,dy \wedge dz + B\,dz \wedge dx + C\,dx \wedge dy$, let the Jacobian matrix of the coefficients $(A,B,C)$ be:

$$\mathbf{J}_\eta := \begin{pmatrix}
\frac{\partial A}{\partial x} & \frac{\partial A}{\partial y} & \frac{\partial A}{\partial z} \\
\frac{\partial B}{\partial x} & \frac{\partial B}{\partial y} & \frac{\partial B}{\partial z} \\
\frac{\partial C}{\partial x} & \frac{\partial C}{\partial y} & \frac{\partial C}{\partial z}
\end{pmatrix}$$

Then the coefficient in the result of §5.7, $d\eta = (\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z})\,dx \wedge dy \wedge dz$, agrees with the <strong>trace</strong> (sum of diagonal entries) of $\mathbf{J}_\eta$:

$$\frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z} = \operatorname{tr}(\mathbf{J}_\eta)$$

#### B.4.1 The 27 components of $d\eta$ — expanded into three matrices

The antisymmetric components of $\eta$ are $\eta_{yz}=A,\; \eta_{zx}=B,\; \eta_{xy}=C$ (the others are sign reversals or $0$). To see where all entries go, first arrange the raw derivative components $\partial_a\eta_{bc}$, where $\partial_x=\frac{\partial}{\partial x}$, $\partial_y=\frac{\partial}{\partial y}$, $\partial_z=\frac{\partial}{\partial z}$, and $a,b,c\in\{x,y,z\}$, so there are $3^3=27$ entries before antisymmetrization. Arranging them into three $3 \times 3$ matrices with $a$ fixed gives:

$$
\begin{aligned}
d\eta_{x,\cdot,\cdot}
&= \begin{pmatrix}
0 & \frac{\partial C}{\partial x} & -\frac{\partial B}{\partial x} \\
-\frac{\partial C}{\partial x} & 0 & \frac{\partial A}{\partial x} \\
\frac{\partial B}{\partial x} & -\frac{\partial A}{\partial x} & 0
\end{pmatrix}, \\
d\eta_{y,\cdot,\cdot}
&= \begin{pmatrix}
0 & \frac{\partial C}{\partial y} & -\frac{\partial B}{\partial y} \\
-\frac{\partial C}{\partial y} & 0 & \frac{\partial A}{\partial y} \\
\frac{\partial B}{\partial y} & -\frac{\partial A}{\partial y} & 0
\end{pmatrix}, \\
d\eta_{z,\cdot,\cdot}
&= \begin{pmatrix}
0 & \frac{\partial C}{\partial z} & -\frac{\partial B}{\partial z} \\
-\frac{\partial C}{\partial z} & 0 & \frac{\partial A}{\partial z} \\
\frac{\partial B}{\partial z} & -\frac{\partial A}{\partial z} & 0
\end{pmatrix}
\end{aligned}
$$

When these $27$ components are contracted with the corresponding basis wedge products of $1$-forms (for example, if $a=x,\;b=y,\;c=z$, then $dx \wedge dy \wedge dz$), terms with repeated indices (diagonal entries, $b=c$, and so on) vanish because $dx \wedge dx = 0$, and only the $6$ terms with all of $a,b,c$ distinct (permutations of $3!$) survive. Each is summed with its sign. The factor convention is the same as in Chapter 2 §2.4.4: the matrix stores each antisymmetric pair twice, while the form stores it once. With that convention, the six surviving signed terms combine to

$$d\eta = \left( \frac{\partial A}{\partial x} + \frac{\partial B}{\partial y} + \frac{\partial C}{\partial z} \right) dx \wedge dy \wedge dz$$

In other words, of the $27$ components of $d\eta$, $6$ survive and pair up and combine into the trace of $\mathbf{J}_\eta$.

A $3$-form has only the single basis element $dx \wedge dy \wedge dz$, so in this representation it reduces to a scalar coefficient.

### B.5 $d^2 f = 0$ and the Hessian

The Hessian of a $0$-form $f$:

$$\mathbf{H}_f := \begin{pmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} & \frac{\partial^2 f}{\partial x \partial z} \\
\frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} & \frac{\partial^2 f}{\partial y \partial z} \\
\frac{\partial^2 f}{\partial z \partial x} & \frac{\partial^2 f}{\partial z \partial y} & \frac{\partial^2 f}{\partial z^2}
\end{pmatrix}$$

arranges the second partial derivatives of $f$. If $f$ is $C^2$, then $\mathbf{H}_f$ is a symmetric matrix ($\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$, and so on).

$d(df) = 0$ is the §5.5 formula for $d\omega$ with $(P,Q,R) = (\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z})$. We have $\mathbf{J} = \mathbf{H}_f$, and because $\mathbf{H}_f$ is symmetric, $\mathbf{J}^T - \mathbf{J} = 0$; hence $d(df) = 0$. In the language of matrices, this is rephrased as "the antisymmetric part of the Hessian is zero."

## Appendix C: Integral Forms of Electromagnetism and Differential Forms

This appendix verifies, in component form, the passage from the integral forms of the four fundamental equations of electromagnetism to their local forms. What we use here are the exterior derivative $d$ and the degree of a differential form. The metric of space does not appear in this localization itself.

### C.1 Degrees of physical quantities

Quantities measured along a line are placed as $1$-forms, quantities measured through a surface as $2$-forms, and quantities measured over a volume as $3$-forms. In components:

$$
E = E_x\,dx+E_y\,dy+E_z\,dz,
\qquad
H = H_x\,dx+H_y\,dy+H_z\,dz
$$

$$D = D_x\,dy\wedge dz + D_y\,dz\wedge dx + D_z\,dx\wedge dy$$

$$B = B_x\,dy\wedge dz + B_y\,dz\wedge dx + B_z\,dx\wedge dy$$

$$J = J_x\,dy\wedge dz + J_y\,dz\wedge dx + J_z\,dx\wedge dy$$

$$
\rho = \rho\,dx\wedge dy\wedge dz
$$

To keep the notation simple, we write both the coefficient representing charge density and the $3$-form obtained by multiplying it by the volume form with the same symbol $\rho$.

$E$ and $H$ are $1$-forms measured along a line; $D$, $B$, and $J$ are $2$-forms measured through a surface; $\rho$ is a $3$-form measured over a volume.

### C.2 Gauss's law for charge

The integral form is:

$$
\int_{\partial V}D=\int_V\rho
$$

Applying the generalized Stokes' theorem to the left-hand side:

$$
\int_{\partial V}D=\int_V dD
$$

Therefore, if

$$
\int_V dD=\int_V\rho
$$

holds for every region $V$, the local form is:

$$
dD=\rho
$$

Expanding in components:

$$
dD
=
\left(\frac{\partial D_x}{\partial x}
{}+\frac{\partial D_y}{\partial y}
{}+\frac{\partial D_z}{\partial z}\right)
dx\wedge dy\wedge dz
$$

Hence:

$$
\frac{\partial D_x}{\partial x}
{}+\frac{\partial D_y}{\partial y}
{}+\frac{\partial D_z}{\partial z}
=\rho
$$

### C.3 The law of magnetic flux

The integral form stating that the net magnetic flux through a closed surface is zero is:

$$
\int_{\partial V}B=0
$$

By the generalized Stokes' theorem:

$$
\int_V dB=0
$$

If this holds for every region $V$, the local form is:

$$
dB=0
$$

Expanding in components:

$$
dB
=
\left(\frac{\partial B_x}{\partial x}
{}+\frac{\partial B_y}{\partial y}
{}+\frac{\partial B_z}{\partial z}\right)
dx\wedge dy\wedge dz
$$

Therefore:

$$
\frac{\partial B_x}{\partial x}
{}+\frac{\partial B_y}{\partial y}
{}+\frac{\partial B_z}{\partial z}
=0
$$

### C.4 Faraday's law

The integral form is:

$$
\int_{\partial S}E
=
-\frac{\partial}{\partial t}\int_S B
$$

Applying the generalized Stokes' theorem to the left-hand side:

$$
\int_S dE
=
-\frac{\partial}{\partial t}\int_S B
$$

If this holds for every surface $S$, the local form is:

$$
dE=-\frac{\partial B}{\partial t}
$$

Expanding in components:

$$dE = \left(\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z}\right)dy\wedge dz + \left(\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x}\right)dz\wedge dx + \left(\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial y}\right)dx\wedge dy$$

On the other hand,

$$
-\frac{\partial B}{\partial t}
=
-\frac{\partial B_x}{\partial t}\,dy\wedge dz
-\frac{\partial B_y}{\partial t}\,dz\wedge dx
-\frac{\partial B_z}{\partial t}\,dx\wedge dy
$$

so the components are:

$$
\frac{\partial E_z}{\partial y}
-
\frac{\partial E_y}{\partial z}
=
-\frac{\partial B_x}{\partial t}
$$

$$
\frac{\partial E_x}{\partial z}
-
\frac{\partial E_z}{\partial x}
=
-\frac{\partial B_y}{\partial t}
$$

$$
\frac{\partial E_y}{\partial x}
-
\frac{\partial E_x}{\partial y}
=
-\frac{\partial B_z}{\partial t}
$$

### C.5 Ampère–Maxwell's law

The integral form is:

$$
\int_{\partial S}H
=
\int_S J+\frac{\partial}{\partial t}\int_S D
$$

Applying the generalized Stokes' theorem to the left-hand side:

$$
\int_S dH
=
\int_S J+\frac{\partial}{\partial t}\int_S D
$$

If this holds for every surface $S$, the local form is:

$$
dH=J+\frac{\partial D}{\partial t}
$$

Expanding in components:

$$dH = \left(\frac{\partial H_z}{\partial y}-\frac{\partial H_y}{\partial z}\right)dy\wedge dz + \left(\frac{\partial H_x}{\partial z}-\frac{\partial H_z}{\partial x}\right)dz\wedge dx + \left(\frac{\partial H_y}{\partial x}-\frac{\partial H_x}{\partial y}\right)dx\wedge dy$$

Also,

$$J+\frac{\partial D}{\partial t} = \left(J_x+\frac{\partial D_x}{\partial t}\right)dy\wedge dz + \left(J_y+\frac{\partial D_y}{\partial t}\right)dz\wedge dx + \left(J_z+\frac{\partial D_z}{\partial t}\right)dx\wedge dy$$

so the components are:

$$
\frac{\partial H_z}{\partial y}
-
\frac{\partial H_y}{\partial z}
=
J_x+\frac{\partial D_x}{\partial t}
$$

$$
\frac{\partial H_x}{\partial z}
-
\frac{\partial H_z}{\partial x}
=
J_y+\frac{\partial D_y}{\partial t}
$$

$$
\frac{\partial H_y}{\partial x}
-
\frac{\partial H_x}{\partial y}
=
J_z+\frac{\partial D_z}{\partial t}
$$

### C.6 Where a metric is needed

The four local forms above can be written using only the exterior derivative $d$ and the degree of differential forms. At this stage, no metric for measuring lengths or angles is used.

A metric becomes necessary when relating $E$ to $D$ and $B$ to $H$. It is also needed when pairing $1$-forms with $2$-forms so that the usual three-component fields can be treated as objects of the same kind.

The Hodge star, introduced in the next chapter, is the tool that provides this correspondence.

# Chapter 6: The Metric $g$ and the Hodge Star $\ast$ — Summoning the Inner Product and Reversing Degree

# Chapter 6: The Metric $g$ and the Hodge Star $\ast$ — Summoning the Inner Product and Reversing Degree

### §6.0 The End of Excuses — Releasing the Inner Product

When, in Chapter 2, we restored the scalar area of a parallelogram as the square root of the sum of squares of three projected areas, and when, in Chapter 3, we measured the surface area $4\pi R^2$ of a sphere and the arc length $2\pi R$ of a circle by the same idea—here we have repeatedly hedged, each time we computed a length or an area, with “we have not yet formally introduced the metric (inner product).”

The reader has probably begun to find this tedious by now. To be honest, I have too.

After all, we are computing on real space $(x,y,z)$—orthogonal Cartesian coordinates. In this space the Pythagorean theorem holds. Let us stop being shy and start using the <strong>inner product</strong>.

What is the inner product? We have already met it many times. In Chapter 2, when we obtained an oriented area, we said that if you take the square root of the sum of squares of the three shadow components $A_{yz}, A_{zx}, A_{xy}$, you recover the elementary-school area—that “sum of squares” is precisely the inner product with itself (or its square root). More generally, for column vectors among themselves, or for $1$-forms written as row vectors, the scalar quantity obtained by multiplying corresponding components and adding is what we call the <strong>inner product</strong> here.

...<strong>That is all</strong>. Most readers probably learned the inner product in high-school mathematics and are thinking, “Why state the obvious?” Yet in this book we have, uncomfortably, avoided defining the inner product head-on until now. There is a reason.

The reason is that if we bring out the inner product too soon, the distinctions we have cared about until now will collapse.

From a more advanced standpoint, “vector addition and subtraction” and the “inner product” are not inseparable; they can be thought of separately. On that view one distinguishes “spaces with an inner product” from “spaces without one,” and calls the matrix that defines the inner product the “metric tensor.” I respect that distinction too. That is precisely why we have repeatedly hedged that we have not yet formally introduced the metric or the inner product.

What we really want to distinguish here is the operation “row vector × column vector gives a scalar” from the operation “take the inner product between vectors of the same kind.”

> <strong>Note</strong> (Why separate row and column so insistently) There is a standpoint that says one can describe physics quite powerfully even without putting the metric or inner product front and center—for example, elementary integration of $n$-forms and much undergraduate-level physics calculation work well on that view. I respect that standpoint too. On the other hand, the metric viewpoint that uses length, angle, inner product, and the Hodge star $\ast$ is of course also powerful. Personally, I think the ideal is to move back and forth between these two views as the problem demands. And to move back and forth, we must first not confuse “the operation measured by row vector × column vector” with “the operation that takes the inner product between vectors of the same kind.” That is why this book has been so insistent about separating row vectors and column vectors.

Since Chapter 1 we have done mountains of calculations that obtain a scalar from row vector × column vector. So how is that different from the inner product?

The conclusion: <strong>they are completely different things</strong>. Row vector times column vector is a calculation between <strong>vectors of different kinds</strong>—row and column. The inner product, by contrast, is a calculation between <strong>vectors of the same kind</strong>—“row with row” or “column with column.”

Yes—the matter is deeper than the reader may have thought. On the special stage of real space, these two often happen to return the same number, which has encouraged their confusion—and on top of that confusion a vast edifice called vector analysis has been built. The goal of this chapter is to make this distinction clear, then introduce the metric $g$ as the natural generalization of the inner product, and from there expose what the Hodge star $\ast$ really is.


### §6.2 Converting Between Column Vectors and Row Vectors Using $g$

#### 6.2.1 $\mathbf{v}^T \mathbf{g}$ Is a Row Vector

Look once more at the inner-product formula from §6.1, $\mathbf{v}_1^T \mathbf{g} \,\mathbf{v}_2$. Matrix products can be executed from the left in order, so this expression can be read as “first compute $\mathbf{v}_1^T \mathbf{g}$, then multiply the result by $\mathbf{v}_2$.”

$\mathbf{v}_1$ is a column vector, but transposed $\mathbf{v}_1^T$ is a row vector. Multiplying a row vector by a square matrix again yields a row vector. So if we extract only the part $\mathbf{v}_1^T \mathbf{g}$,

$$\omega = \mathbf{v}^T \mathbf{g}$$

this is a <strong>row vector</strong> of size $1 \times 3$. The metric $g$ is, arising naturally from the matrix form of the inner product, a <strong>device that converts column vectors into row vectors</strong>.

Let us also write the reverse direction. Suppose a $1$-form given as a row vector

$$
\omega =
\begin{pmatrix}
\omega_1 & \omega_2 & \omega_3
\end{pmatrix}
$$

is given. The corresponding column vector $\mathbf{v}_\omega$ is

$$
\mathbf{v}_\omega = \mathbf{g}^{-1}\omega^T
$$

> <strong>Note</strong> (Inverse matrix) For a square matrix $A$, the matrix $A^{-1}$ satisfying
> $$
> A^{-1}A = AA^{-1} = I
> $$
> is called the inverse of $A$. Intuitively, it is the matrix that undoes the transformation by $A$. Here we use $\mathbf{g}^{-1}$ to return a row vector built with $\mathbf{g}$ to the original column vector.

In fact, if $\omega = \mathbf{v}^T\mathbf{g}$, transposing gives

$$
\omega^T = \mathbf{g}^T\mathbf{v}
$$

Since $\mathbf{g}$ is symmetric, $\mathbf{g}^T = \mathbf{g}$. Therefore

$$
\mathbf{v} = \mathbf{g}^{-1}\omega^T
$$

returns us to the start.

In orthogonal Cartesian coordinates on real space, $\mathbf{g}=I$, so this reverse conversion too looks like mere transpose. In a general coordinate system, however, $\mathbf{g}^{-1}$ is needed to return a row vector to a column vector.

> <strong>Note</strong> (What we smuggled in Chapter 2) When we sought a matrix representation of a $2$-form in Chapter 2, we already used the form $\mathbf{v}_1^T M \mathbf{v}_2$. At that time we only said that “laying a column vector on its side is mathematically ill-behaved” and pushed on without going deeper. The $\mathbf{v}^T\mathbf{g}$ we are looking at now is the true nature of the operation we smuggled in then. In real space $\mathbf{g}=I$, so transpose alone makes a column vector look like a row vector. In parameter space, however, to convert a column vector into a row measuring device that reproduces the inner product in real space, we must pass explicitly through the metric $\mathbf{g}$.

Consider the meaning of this conversion. Since Chapter 1 we have distinguished “the figure being measured (column vector $\mathbf{v}$)” from “the measuring device (row vector $\omega$).” They were inhabitants of different worlds. But via $g$, a column vector that lived on the figure side changes form to the scale side—the row vector. Even for the same arrow, the “sensitivity as a scale” changes from place to place because $\mathbf{g}$ absorbs all the differences in calibration at each location.

In real space ($\mathbf{g}=I$) we have $\omega = \mathbf{v}^T$, and the components of the column vector become the components of the row vector as-is. In parameter space $\mathbf{g} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & r^2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, so $\omega = \begin{pmatrix} \Delta r & r^2\Delta\theta & \Delta z \end{pmatrix}$. Only the $\theta$ component is multiplied by $r^2$, reflecting that the $\theta$ direction’s scale is stretched by a factor of $r$.

Without $g$, we cannot convert between “the figure being measured” and “the measuring device” without strain. $g$ is the standard go-between that ties the two together.

#### 6.2.2 What the Metric Gives — Geometric Size of Parallel $k$-Parallelepipeds

The most basic role of the metric $g$ is to define the <strong>actual geometric size</strong> (length, area, volume) of the <strong>parallel $k$-parallelepiped</strong> spanned by $k$ vectors.

In the chapters until now we performed “oriented counting” by feeding $k$ vectors to a $k$-form. $dx(\mathbf{v})$ is the number of the $x$ component of $\mathbf{v}$; $dx \wedge dy(\mathbf{v}_1, \mathbf{v}_2)$ is the oriented area of the parallelogram spanned by $\mathbf{v}_1, \mathbf{v}_2$. But these are measurements of shadows after all; how many meters of segment the vectors span, how many square meters of parallelogram they span under that metric, is determined only once the metric $g$ is given.

For $k=1$ (the segment spanned by one vector $\mathbf{v}$), the square of its length is defined by the inner product with itself, as we already derived in §6.1:

$$|\mathbf{v}|^2 = \mathbf{v}^T \mathbf{g} \,\mathbf{v}$$

In real space ($\mathbf{g}=I$), $|\mathbf{v}|^2 = \Delta x^2 + \Delta y^2 + \Delta z^2$. In the parameter space of cylindrical coordinates, $|\mathbf{v}|^2 = \Delta r^2 + r^2\Delta\theta^2 + \Delta z^2$.

For $k=0$, no displacement vector is fed in; the corresponding size is simply the absolute value of the scalar coefficient $|f|$.

The same holds for $k=2$ (area of the parallelogram spanned by two vectors) and $k=3$ (volume of the parallelepiped spanned by three vectors). As we saw in Chapter 2 §2.4.7, the square root of the sum of squares of the coefficients $A_{xy}, A_{yz}, A_{zx}$ of the three basis $2$-forms $dx \wedge dy, dy \wedge dz, dz \wedge dx$, namely $\sqrt{A_{yz}^2 + A_{zx}^2 + A_{xy}^2}$, gives the unsigned area of the parallelogram. In $xyz$ coordinates this calculation needs only the coefficients of the basis $2$-forms; no other information is required.

> <strong>Note</strong> (Why we do not write $k=2$ in vector form) For $k=1$ we wrote length as the inner product $\mathbf{v}^T\mathbf{g}\,\mathbf{v}$ of the column vector $\mathbf{v}$. The analogous inner product for $k=2$—inner product between matrices (the Frobenius product in Appendix D)—we have not yet defined. Moreover, to display the coefficients of a $2$-form as a $3$-component vector requires the Hodge star $\ast$, which changes degree. Here we still treat a face as a face—that is, as coefficients of a $2$-form.

The role of the metric $g$ is to generalize this “computation in $xyz$” to coordinate systems with distorted scales, such as parameter space. In every case, <strong>once $g$ is fixed, a consistent geometric size is defined for parallel $k$-parallelepipeds of every degree</strong>—that is the most fundamental role of the metric.

#### 6.2.3 Properties of the Inner Product

Just as in Chapter 5 we summarized the properties of the exterior derivative $d$ (linearity, raising degree, $d^2=0$, Leibniz rule), let us organize here the properties of the inner product that emerge from the calculations so far. These do not depend on a particular coordinate system.

1. <strong>Symmetry</strong>: $\mathbf{v}_1 \cdot \mathbf{v}_2 = \mathbf{v}_2 \cdot \mathbf{v}_1$. Apply this to the matrix form derived in §6.1, $\mathbf{v}_1^T \mathbf{g} \,\mathbf{v}_2$. We have $\mathbf{v}_2 \cdot \mathbf{v}_1 = \mathbf{v}_2^T \mathbf{g} \,\mathbf{v}_1$, but a scalar is unchanged under transpose, so $\mathbf{v}_2^T \mathbf{g} \,\mathbf{v}_1 = (\mathbf{v}_2^T \mathbf{g} \,\mathbf{v}_1)^T = \mathbf{v}_1^T \mathbf{g}^T \mathbf{v}_2$. For this to equal $\mathbf{v}_1^T \mathbf{g} \,\mathbf{v}_2$ we must have $\mathbf{g} = \mathbf{g}^T$. That is, from symmetry of the inner product it follows that $\mathbf{g}$ must be a <strong>symmetric matrix</strong>.

2. <strong>Linearity</strong> (bilinearity): $(a\mathbf{v}_1 + b\mathbf{v}_2) \cdot \mathbf{v}_3 = a(\mathbf{v}_1 \cdot \mathbf{v}_3) + b(\mathbf{v}_2 \cdot \mathbf{v}_3)$. Linear in each argument. This is nothing but the distributive law for matrix products, $(a\mathbf{v}_1 + b\mathbf{v}_2)^T \mathbf{g} \,\mathbf{v}_3 = a\mathbf{v}_1^T \mathbf{g} \,\mathbf{v}_3 + b\mathbf{v}_2^T \mathbf{g} \,\mathbf{v}_3$.

3. <strong>Positive definiteness</strong>: $\mathbf{v} \cdot \mathbf{v} > 0$ ($\mathbf{v} \neq \mathbf{0}$). This guarantees that “square of length” is positive. In special relativity, where signs are mixed, this need not hold; but on the three-dimensional real space that is the stage of this book it always does.

> <strong>Note</strong> (Symmetric vs antisymmetric matrices)
> The fact that the area-measuring device in Chapter 2 required an antisymmetric matrix ($M = -M^T$) and that the inner product here requires a symmetric matrix ($\mathbf{g} = \mathbf{g}^T$) are exactly paired. Antisymmetry governs oriented counting; the symmetric metric governs length and angle, and from there the unsigned area and volume induced.

#### 6.2.4 Letting the Geometry of the Metric Matrix Live in Its Components

The diagonal entries of $\mathbf{g}$ express “how much a step along that axis contributes to length”; the off-diagonal entries express “how much steps along different axes interfere with each other.” That $\mathbf{g}$ in cylindrical coordinates was diagonal is because the axes $r,\theta,z$ are mutually orthogonal. In any case, the single matrix $\mathbf{g}$ carries in its components all the “ruler properties” at that location.

> <strong>Note</strong> (Axiomatic inner product—reversed order of axioms and matrix) In a standard linear-algebra textbook one first defines the three properties above as axioms, then derives the theorem that any operation satisfying them can be written, in some basis, in the form $\mathbf{v}^T \mathbf{g} \mathbf{w}$ with a symmetric matrix $\mathbf{g}$. The logical order is the reverse of ours. On the axiomatic side the matrix representation is only one representation; on the measuring-device reading of this book, <strong>this matrix $\mathbf{g}$ is the scale of space itself</strong>, the starting point of all measurement. Neither is “correct” in preference to the other. One enters from abstract properties; one enters from concrete symbolic operations of measurement. Only the direction that suits you differs.

> <strong>Checkpoint so far — §6.0–§6.2</strong>
> - The inner product is the operation of taking the sum of products of components between vectors of the same kind (row × row, or column × column). It is a different thing from row × column.
> - The inner product in parameter space is computed by pulling back to real space first. In that process $J^T J$ appears naturally. That is the true nature of the metric $g$.
> - $g$ converts column vectors to row vectors. Concretely, from a column vector $\mathbf{v}$ the corresponding $1$-form is built by $\omega_{\mathbf{v}} = \mathbf{v}^T\mathbf{g}$.
> - Conversely, from a $1$-form $\omega$ given as a row vector, the corresponding column vector is $\mathbf{v}_\omega = \mathbf{g}^{-1}\omega^T$. In Cartesian coordinates $\mathbf{g}=I$, so both look like almost nothing but transpose.
> - With $g$ as mediator, geometric size is defined for parallel $k$-parallelepipeds of every degree.
> - From the properties of the inner product (symmetry, linearity, positive definiteness) the symmetry of $g$ follows. This pairs with the antisymmetry of the area-measuring device $\wedge$.

---

### §6.3 The Hodge Star $\ast$ — The Correspondence Connecting Two Routes

#### 6.3.1 Two Ways to Obtain a Scalar

By now the true nature of $g = J^T J$ has been revealed, and we can compute inner products in any coordinate system. Let us step back and look at the larger picture.

When we survey the formulas of physics, we notice that there is more than one way to produce a scalar quantity. When we integrate a field along a line or over a surface, a natural notation appears: something that measures acts on something that is measured and returns a number. On the other hand, quantities such as power and energy density are often written as inner products of the same kind of arrow, as in $\mathbf{E}\cdot\mathbf{J}$ or $\mathbf{A}\cdot(\nabla\times\mathbf{A})$.

In other words, at least on the surface, two conventions for obtaining scalars coexist in the notation of physics. In the language of this book, they are the following two:

- <strong>Route ① (differential-forms route / $d$ route)</strong>: Prepare a measuring device (row vector: a $1$-form, and so on) and a figure to be measured (column vector: a vector field, and so on), and obtain a scalar by a row $\times$ column computation. What this computation uses is the logic of action and evaluation—a form eats a vector and returns a scalar.
- <strong>Route ② (vector-calculus route / $\nabla$ route)</strong>: Unify all quantities as "arrows of the same kind," and obtain a scalar by an inner product between like vectors (column $\times$ column, or row $\times$ row). In this computation, the metric $g$ is inserted so that like vectors can be compared. Many readers will be familiar with this method from school education.

> <strong>Note</strong> (What to call the two methods—the author's dilemma) The author long wondered what to call these two conventions in a textbook. Calling Route ① the "differential forms method" is natural, but in this book we also write "d method" alongside it. For readers who do not yet know differential forms, the symbol $d$ is more familiar. The author personally also calls it the "topology method." For readers raised in topology or geometry, that name may feel more natural. Likewise, calling Route ② the "vector calculus method" is natural, but in this book we also write "$\nabla$ method" alongside it. The symbol $\nabla$ (nabla) is the most familiar symbol for readers who have studied physics. The author personally also calls it the "inner product method," using that name when emphasizing that the structure of the inner product sits at the core. All of these names refer to the same two conventions.

> <strong>Note</strong> (Genealogy of the two notations) Route ① lies close to Grassmann's exterior algebra and Élie Cartan's line of development; Route ② lies close to the vector calculus systematized by Gibbs and Heaviside. This is not a matter of one being correct and the other wrong.

In fact, whichever method we adopt, the physical result we obtain in the end is the same. This is merely a difference of expression.

Yet a practical problem arises here. In the framework of Route ②, quantities that ought to be measured through a "surface" ($2$-forms) and quantities measured along a "line" ($1$-forms) are all treated as the same kind of "three-component arrow." To handle the notions of area and volume from Route ① within the framework of Route ②'s "inner product of arrows," we need a correspondence that links forms of different degrees.

The number of independent components of a $k$-form had a characteristic symmetry. As we saw in Chapter 2 §2.5.9, in three-dimensional space a $0$-form has $1$ component, a $1$-form has $3$, a $2$-form also has $3$, and a $3$-form has $1$—folded at the middle, the pattern $1, 3, 3, 1$ is symmetric left and right. Between a $1$-form and a $2$-form with the same number of independent components, and between a $0$-form and a $3$-form, some correspondence ought to exist. The device that supplies that correspondence is the <strong>Hodge star $\ast$</strong>.

$\ast$ uses the information of the inner product (that is, $g$) to assign to each form the partner that combines with it to make a volume. In the main text we first build this correspondence in the basis of physical space; verification in components is deferred to Appendix D.

> <strong>Note</strong> (Between the two methods) We need not use only one of Route ① and Route ②. The author's ideal is to move freely between both. This book starts from Route ① (differential forms) in order to build a solid foundation that does not depend on distortion of space. On top of that, we want to be able to read the same quantities in the language of Route ② when needed—and $\ast$ is what bridges the two.

> <strong>Note</strong> (For readers who know vector calculus) Many operations that in ordinary vector calculus are treated as face orientations or cross products can be read anew as the correspondence given by this $\ast$. In this chapter, however, we do not use those as known formulas; we rebuild them from $g$ and the basis $2$-forms of Chapter 2.

#### 6.3.2 The $\ast$ Dictionary in Physical Space—Choosing the Partner That Makes a Volume

So how is $\ast$ determined?

Here we first consider orthogonal Cartesian coordinates in physical space $(x,y,z)$. In this space, $dx, dy, dz$ are mutually orthogonal reference measuring devices of length $1$. We also fix the orientation of space so that

$$
dx \wedge dy \wedge dz
$$

is the positive volume form.

We may think of $\ast$ as the operation that, given a form, returns the partner which combines with it to yield a volume form.

For example, what $2$-form combines with $dx$ to produce the positive volume form? It is $dy \wedge dz$. Indeed,

$$
dx \wedge dy \wedge dz
$$

is obtained. Therefore it is natural to set

$$
\ast dx = dy \wedge dz.
$$

Likewise,

$$
dy \wedge dz \wedge dx = dx \wedge dy \wedge dz,
$$

so

$$
\ast dy = dz \wedge dx,
$$

and

$$
dz \wedge dx \wedge dy = dx \wedge dy \wedge dz,
$$

so

$$
\ast dz = dx \wedge dy.
$$

In other words, $\ast$ assigns to each line measuring device the surface measuring device that combines with it to give the positive volume form. By the same idea, the scalar $1$ corresponds to the volume form $dx \wedge dy \wedge dz$, and the volume form corresponds to the scalar $1$.

Therefore the $\ast$ dictionary in physical space is as follows.

$$\begin{aligned}
\ast(1) &= dx \wedge dy \wedge dz, \qquad &\ast(dx \wedge dy \wedge dz) &= 1 \\
\ast(dx) &= dy \wedge dz, \qquad &\ast(dy \wedge dz) &= dx \\
\ast(dy) &= dz \wedge dx, \qquad &\ast(dz \wedge dx) &= dy \\
\ast(dz) &= dx \wedge dy, \qquad &\ast(dx \wedge dy) &= dz
\end{aligned}$$

At this stage it is enough to read $\ast$ as a "dictionary." However, this correspondence is not a mere memorization table. Once a basis is chosen, $\ast$ can be written as an array representation of a linear transformation that rearranges coefficients. The array representation over all degrees is confirmed in Appendix D.

The meaning of this dictionary is simple. What corresponds to a line segment in the $x$ direction ($dx$) is the face perpendicular to the $x$ axis ($dy \wedge dz$). Likewise $y \leftrightarrow dz \wedge dx$, $z \leftrightarrow dx \wedge dy$. And the scalar $1$ ($0$-form) and the volume $dx \wedge dy \wedge dz$ ($3$-form) correspond to each other. This is precisely the manifestation of the symmetry $1, 3, 3, 1$ of independent component counts that we saw in Chapter 2.

> <strong>Note</strong> (Why this dictionary is the right one) That $\ast dx = dy \wedge dz$ holds is because $dx, dy, dz$ form an orthonormal basis (mutually orthogonal, length $1$) and because we have taken the orientation of space so that $dx \wedge dy \wedge dz$ is positive in a right-handed system. Under these conditions, the dictionary above is determined uniquely. Once parameter space is taken into account, the $\ast$ dictionary depends on the metric $g$ and on how orientation is chosen—in other words, if $g$ is not $I$, the coefficients in the dictionary become more complicated.

#### 6.3.3 $\ast\ast = \mathrm{id}$

As the dictionary above shows immediately, applying $\ast$ twice returns the original:

$$\ast(\ast(dx)) = \ast(dy \wedge dz) = dx.$$

In general, in three-dimensional Cartesian physical space, $\ast\ast = \mathrm{id}$ (the identity operator) holds. One application of $\ast$ reverses the degree of a form; two applications return it to the original.

> <strong>Checkpoint so far — §6.3</strong>
> - There are two ways to obtain a scalar. Route ① obtains a scalar by row $\times$ column action. Route ② reads it as an inner product of like vectors, and the metric $g$ appears there.
> - The symmetry $1, 3, 3, 1$ seen in Chapter 2 suggests that a correspondence can be set up between $1$-forms and $2$-forms with the same number of independent components.
> - The Hodge star $\ast$ returns, for a given form, the partner which combines with it to give the positive volume form. The dictionary in physical space includes $\ast dx = dy \wedge dz$, and so on.
> - This dictionary is not a mere memorization table; once a basis is chosen, it can be written as an array representation of a linear transformation. Details of the array representation are confirmed in Appendix D.
> - $\ast\ast = \mathrm{id}$ follows immediately from this dictionary.

#### 6.3.4 Properties of $\ast$

Following the pattern of §6.2.3, where we summarized the properties of the inner product, and of Chapter 5, where we summarized the properties of the exterior derivative $d$, let us organize the properties of $\ast$ that emerge from the construction so far.

1. <strong>Reversal of degree</strong>: In three-dimensional space, $\ast$ pairs $0$-forms with $3$-forms and $1$-forms with $2$-forms. In general it sends a $k$-form to a $(3-k)$-form.

2. <strong>Linearity</strong>: $\ast(\omega_1 + \omega_2) = \ast\omega_1 + \ast\omega_2$. $\ast$ is the operation that extends the dictionary on the basis linearly with coefficients; linearity is immediate. Details of the array representation are confirmed in Appendix D.

3. <strong>Correspondence with the inner product</strong>: For forms $\alpha, \beta$ of the same degree, combining $\alpha$ and $\ast\beta$ by the wedge product yields a $3$-form whose coefficient is the inner product of $\alpha$ and $\beta$. In Cartesian coordinates,

$$
\alpha \wedge \ast\beta
=
(\alpha\cdot\beta)\,dx\wedge dy\wedge dz
$$

Here $\alpha\cdot\beta$ denotes the metric-induced inner product of forms of the same degree. For two $1$-forms it is the sum of products of components; for two $2$-forms it is the Frobenius product seen in Appendix D. This formula expresses that $\ast$ links the "scalar obtained by the inner product" with the "$3$-form obtained by the wedge product."

> <strong>Note</strong> (Relation to more advanced definitions) In more advanced textbooks, $\alpha\wedge\ast\beta=(\alpha\cdot\beta)\,dx\wedge dy\wedge dz$ is often adopted as the definition of $\ast$. In this book we first built the dictionary on each basis element and its array representation; that is a concrete realization of this definition in Cartesian coordinates.

4. <strong>$\ast\ast = \mathrm{id}$</strong>: Applying it twice returns the original (§6.3.3). This holds under the conditions of an orthonormal basis and a right-handed system; in Appendix D it can also be verified algebraically through antisymmetric matrices and the Frobenius product.

5. <strong>Dependence on the metric $g$</strong>: The $\ast$ dictionary is determined by the metric $g$ of space. In Cartesian coordinates ($g=I$), the concise dictionary of §6.3.2 suffices; in a general coordinate system, the coefficients of $\ast$ become functions of position. We treat the general case in detail in Chapter 9.

These properties show that $\ast$ is not a mere "dictionary" but the very <strong>degree-reversal structure</strong> of a space equipped with a metric and an orientation.

---

### §6.4 Examples of the Correspondence — Differential Forms and Vector Analysis

#### 6.4.1 Joule Heating $P=VI$ — Two Routes

Let us verify in actual computation how $\ast$ concretely links differential forms with dot-product representations of like-kind vectors. The purpose of this section is not to learn formulas from electromagnetism or vector analysis. It is to survey, in two examples, how quantities that arise naturally in the language of differential forms can be read in the notation of scalar products and vector analysis.

> <strong>Note</strong> (you need not know electromagnetism or vector analysis) From here on, for the sake of explanation we will use a few symbols from electromagnetism and vector analysis a little ahead of their formal introduction. You need not understand right now what $E$ or $J$ represent, or what $\mathbf{A}\cdot(\nabla\times\mathbf{A})$ means. What we want to see here is a single point: a $3$-form that appears naturally in the language of differential forms can be read, through the Hodge star $\ast$, as a scalar or an inner product. The relation to vector-analytic notation will peek through a little later, but a full systematic treatment is deferred to later chapters.

Revisit the high-school physics formula "electric power = voltage × current ($P=VI$)" as a phenomenon that occurs at each point in space.

- The <strong>electric field $E$</strong>, which is the origin of voltage, is a <strong>$1$-form</strong> that counts along line segments.
- The <strong>current density $J$</strong>, which is the origin of current, is a <strong>$2$-form</strong> that counts charge crossing a surface.

First, let us compute by <strong>Route ① (differential forms)</strong>. Take the wedge product of the $1$-form $E$ and the $2$-form $J$:

$$E \wedge J$$

The wedge product of a $1$-form and a $2$-form is a $3$-form (a volume density). This means "power per unit volume (W/m³)." Integrating this over a spatial region ($\int_V E \wedge J$) yields the total power consumed in the region (watts). This route uses only the operation of wedging a $1$-form and a $2$-form into a $3$-form.

Next, see how the same calculation is carried out by <strong>Route ② (dot product of like-kind vectors)</strong>. To take an inner product treating both $E$ and $J$ as if they were $1$-forms, convert $J$, which measures surfaces, into a form that measures lines via $\ast$:

$$\text{Route ② display of }J \longleftrightarrow \ast J$$

Now we have two $1$-forms, $E$ and $\ast J$. Take their inner product (dot product). Here $E\cdot J$ is the Route ② display after $J$ has been read through $\ast$ as a like-kind object. To write the inner product of $1$-forms in the language of differential forms, apply $\ast$ to one side to obtain a $2$-form, wedge to a $3$-form, then apply $\ast$ overall to drop to a $0$-form:

$$\text{Route ② display }E\cdot J \longleftrightarrow \ast(E \wedge \ast(\ast J))$$

Here $\ast\ast = \mathrm{id}$, so the inner $\ast(\ast J) = J$:

$$\ast(E \wedge J)$$

The bracketed quantity $E \wedge J$ is exactly the same $3$-form obtained in Route ①. The outer $\ast$ strips the volume $dx \wedge dy \wedge dz$ from the $3$-form and extracts a scalar value. The way of writing that multiplies the scalar $E \cdot J$ by a small volume $dV$ and integrates again can be read as restoring afterward the volume that this $3$-form already carried.

<strong>In short, $\ast$ links the $3$-form of Route ① and the scalar display of Route ② without contradiction.</strong> Because $\ast\ast = \mathrm{id}$, either route leads to the same result.

#### 6.4.2 Helicity $A \cdot (\nabla \times A)$ — The Round Trip of $\ast$

In one more example, let us see further how $\ast$ works. Consider the following $3$-form built from a $1$-form $\alpha$ and its exterior derivative $d\alpha$:

$$\alpha \wedge d\alpha$$

In the language of Route ②, this quantity appears as the inner product of a vector field $\mathbf{A}$ with its curl:

$$\mathbf{A} \cdot (\nabla \times \mathbf{A})$$

Write the $1$-form corresponding to $\mathbf{A}$ as $\alpha$. The $d\alpha$ is first obtained as a $2$-form; in the language of Route ② it corresponds to the $1$-form $\ast d\alpha$.

First compute by <strong>Route ①</strong>. The wedge product of the $1$-form $\alpha$ and the $2$-form $d\alpha$:

$$\alpha \wedge d\alpha$$

The wedge of a $1$-form and a $2$-form is a $3$-form. On this route, $\alpha$ and $d\alpha$ are combined directly by the wedge product.

Next look at the internal structure of the same calculation on <strong>Route ②</strong>. To read it as a dot product of like-kind vectors, we cannot leave the $2$-form $d\alpha$ as it is; we assign the corresponding $1$-form $\ast d\alpha$:

$$\nabla \times \mathbf{A} \longleftrightarrow \ast d\alpha$$

Now we have two $1$-forms, $\alpha$ and $\ast d\alpha$. Take their inner product:

$$\mathbf{A} \cdot (\nabla \times \mathbf{A}) \longleftrightarrow \ast(\alpha \wedge \ast(\ast d\alpha))$$

By $\ast\ast = \mathrm{id}$, the inner $\ast(\ast d\alpha) = d\alpha$. Therefore,

$$\ast(\alpha \wedge d\alpha)$$

The bracketed quantity is the same as the $3$-form $\alpha \wedge d\alpha$ from Route ①. The outer $\ast$ strips the volume and extracts a scalar value.

<strong>What deserves attention here is that $\ast$ appears twice and cancels via $\ast\ast = \mathrm{id}$.</strong> Inside Route ② we use $\ast d\alpha$ as the $1$-form corresponding to $d\alpha$ (a $2$-form), and call on $\ast$ again to take the inner product. This round trip is canceled by $\ast\ast = \mathrm{id}$.

> <strong>Note</strong> (why the round trip of $\ast$ occurs) Vector analysis has no concept of the degree of a form and treats everything uniformly as "a three-component arrow." To read a $2$-form as an arrow, one must build the corresponding $1$-form with $\ast$; to take an inner product one must again use $\ast$ to return to the original degree. The Hodge star $\ast$ is the single correspondence that links these two representations.

> <strong>Checkpoint so far — §6.4</strong>
> - In the Joule-heating calculation, Route ① ($E \wedge J$) and Route ② ($E \cdot J = \ast(E \wedge J)$) agree via $\ast$.
> - In the helicity calculation, $\ast$ is used twice and cancels by $\ast\ast = \mathrm{id}$. Route ① ($\alpha \wedge d\alpha$) and Route ② ($\mathbf{A} \cdot (\nabla \times \mathbf{A})$) give the same result.
> - $\ast$ is the correspondence linking differential forms and vector analysis; $\ast\ast = \mathrm{id}$ guarantees consistency of the round trip.

---

### §6.5 The Types of the Three Operations — grad, curl, div

By now we have the two operators $d$ (Chapter 5) and $\ast$ (this chapter). Combining them yields operations that move the degree of a form in various ways.

Among these, three types are especially named in three-dimensional vector analysis:

$$
0 \to 1,\qquad
1 \to 2 \to 1,\qquad
1 \to 2 \to 3 \to 0
$$

In this book we call them, respectively,

$$
\mathrm{grad},\qquad
\mathrm{curl},\qquad
\mathrm{div}
$$

This chapter stops at naming these three types. The correspondence with the usual $\nabla f$, $\nabla\times\mathbf F$, and $\nabla\cdot\mathbf F$ is treated again in later chapters.

> <strong>Note</strong> (for readers who know vector analysis) By this point you may already see the usual $\nabla f$, $\nabla\times\mathbf F$, and $\nabla\cdot\mathbf F$ in the background. This chapter, however, does not formally develop the usual vector-analytic notation. Here we confirm the path: "from combinations of $d$ and $\ast$, extract the three types corresponding to grad, curl, and div." The usual nabla notation, the correspondence with Stokes' theorem, and why formulas grow long in curvilinear coordinates are taken up again in later chapters.

Below, we work first in Cartesian coordinates. Use the $1$-form

$$
\omega = P\,dx + Q\,dy + R\,dz
$$

Readers who know vector analysis may read this as the field with components $(P,Q,R)$. A full systematic treatment of this correspondence is deferred to later chapters.

#### 6.5.1 Gradient $\mathrm{grad}\,f = df$

The exterior derivative $df$ of a $0$-form (scalar field) $f$ is a $1$-form:

$$
df = \frac{\partial f}{\partial x}\,dx
{}+ \frac{\partial f}{\partial y}\,dy
{}+ \frac{\partial f}{\partial z}\,dz
$$

In this book we call this the $1$-form representation of the gradient and write

$$
\mathrm{grad}\,f = df
$$

The operator $d$ raises the degree from $0 \to 1$. That is the form of the gradient needed in this chapter. The relation to the column-vector display $\nabla f$ of usual vector analysis is organized again in later chapters.

#### 6.5.2 Curl $\mathrm{curl}\,\omega = \ast\,d\,\omega$

For the $1$-form

$$
\omega = P\,dx + Q\,dy + R\,dz
$$

applying $d$ yields the $2$-form $d\omega$:

$$d\omega = (\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z})\,dy \wedge dz + (\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,dz \wedge dx + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dx \wedge dy$$

Applying $\ast$ returns the $2$-form to a $1$-form:

$$\ast(d\omega) = (\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z})\,dx + (\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x})\,dy + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\,dz$$

In this book we call this $1$-form the $1$-form representation of the curl and write

$$\mathrm{curl}\,\omega = \ast\,d\,\omega$$

The composition $\ast\,d$ has the degree transition

$$
1 \to 2 \to 1
$$

This structure of "rising once to a surface form, then returning to a line form" corresponds to the curl. The relation to what is written $\nabla\times\mathbf F$ in usual vector analysis is treated again in later chapters.

#### 6.5.3 Divergence $\mathrm{div}\,\omega = \ast\,d\,\ast\,\omega$

Apply $\ast$ first to the $1$-form $\omega$ to obtain a $2$-form. Apply $d$ to obtain a $3$-form. Apply $\ast$ once more to return to a $0$-form, namely a scalar field:

$$
\ast d\ast\omega
$$

Computing in Cartesian coordinates,

$$\ast(d(\ast\omega)) = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

In this book we call this $0$-form the divergence and write

$$\mathrm{div}\,\omega = \ast\,d\,\ast\,\omega$$

The composition $\ast\,d\,\ast$ has the degree transition

$$
1 \to 2 \to 3 \to 0
$$

The relation to what is written $\nabla\cdot\mathbf F$ in usual vector analysis is treated again in later chapters.

#### 6.5.4 The Shadow of $d^2 = 0$

Recall $d^2 = 0$ from Chapter 5. From this single fact, relations arise among the three operations.

First,

$$
\mathrm{curl}(\mathrm{grad}\,f)
=
\ast d(df)
=
\ast(d^2 f)
=
0
$$

Also,

$$
\mathrm{div}(\mathrm{curl}\,\omega)
=
\ast d\ast(\ast d\omega)
=
\ast d(d\omega)
=
\ast(d^2\omega)
=
0
$$

Here we stop at viewing these as identities on the side of forms. Readers who know vector analysis will see the correspondence with the usual identities. In this book, however, the meaning in the usual nabla notation is deferred to later chapters.

---
### §6.6 Toward Vector Analysis

In Chapter 5 we acquired the exterior derivative $d$; in this chapter, the metric $g$ and the Hodge star $\ast$. With this, the main tools needed to move from the world of forms toward vector analysis are in place.

What we confirmed in this chapter is that from combinations of $d$ and $\ast$, one can extract the three types called grad, curl, and div in three-dimensional vector analysis.

Let us tabulate the correspondences obtained here.

| Operation | Decomposition in this book | Degree transition | Number of uses of $\ast$ |
|---|---|---|---|
| $\mathrm{grad}$ | $d$ | $0 \to 1$ | 0 |
| $\mathrm{curl}$ | $\ast\,d$ | $1 \to 2 \to 1$ | 1 |
| $\mathrm{div}$ | $\ast\,d\,\ast$ | $1 \to 2 \to 3 \to 0$ | 2 |

By now, a substantial part of the structure behind nabla notation has come into view. However, this chapter has not yet formally developed the usual vector analysis.

Readers who know vector analysis may already see the usual $\nabla$ notation rising from here. But this book will not rush. The systematic organization in the usual nabla notation is deferred to later chapters.

In later chapters we will use the $d$, $g$, and $\ast$ obtained here to return to the notation of usual vector analysis. Stokes' theorem, Gauss' theorem, and why formulas grow long in curvilinear coordinates will all be reread from this toolkit.

> <strong>Note</strong> (by flipping just one sign in the metric) This chapter assumed a positive definite metric ($\mathbf{v}^T \mathbf{g} \,\mathbf{v} > 0$ for $\mathbf{v} \neq 0$). But on the four-dimensional spacetime stage of special relativity, an indefinite metric appears, such as $\mathbf{g} = \begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$, with only the time component's sign flipped. This book is fixed on three-dimensional Cartesian physical space, so we do not go further here; but the idea learned in this chapter of "inserting the matrix $\mathbf{g}$" extends directly to four-dimensional spacetime. When that becomes necessary, I hope the reader will return to this chapter.

---

> <strong>Checkpoint so far — Chapter 6 as a whole</strong>
> - The inner product is an operation taking the product-sum of components between vectors of the same kind (row×row, or column×column). It is a different operation from row×column computation.
> - In physical space the inner-product matrix is the identity $I$. In parameter space it is determined by the linear coefficients of coordinate transformation as $\mathbf{g}=J^T J$. That is, the metric $g$ is nothing other than the matrix that appears in the middle when one pulls back to physical space and takes the inner product.
> - $\mathbf{v}^T \mathbf{g}$ converts a column vector into a row vector; $\mathbf{g}^{-1}\omega^T$ returns a row vector to column-vector display. Without $g$, objects and measuring devices cannot convert into each other.
> - There are two ways to obtain a scalar: Route ① (row×column) and Route ② (inner product of like-kind vectors). The Hodge star $\ast$ is the correspondence linking the two.
> - $\ast$ returns, for a given form, the partner that combines with it to yield a positive volume form. The dictionary in physical space is $\ast dx = dy \wedge dz$, etc., and it satisfies $\ast\ast = \mathrm{id}$.
> - The Joule-heating and helicity examples show that Route ① and Route ② give the same result through $\ast$ and $\ast\ast = \mathrm{id}$.
> - In Chapter 6 we confirmed that the three types $\mathrm{grad}=d$, $\mathrm{curl}=\ast\,d$, $\mathrm{div}=\ast\,d\,\ast$ appear. The systematic organization in the usual nabla notation is deferred to later chapters.
> - From $d^2=0$, on the side of forms we get $\mathrm{curl}(\mathrm{grad}\,f)=0$ and $\mathrm{div}(\mathrm{curl}\,\omega)=0$. The meaning in usual vector analysis is treated again in later chapters.

---

## Appendix D: Array Representation of the Hodge Star

§6.3.2 gave the dictionary for $\ast$ in real space. This appendix checks how that dictionary looks as array operations. The Hodge star is not an abstract symbol; once a basis is chosen, it is a linear transformation that can be displayed as a concrete array. We first view the $1$-form $\leftrightarrow$ $2$-form correspondence through antisymmetric matrices, and finally view the $0$-form $\leftrightarrow$ $3$-form correspondence through a third-order array.

### D.1 $\ast_{1\to2}$ — placing three coefficients into an antisymmetric matrix

For the $1$-form

$$
\omega =
\begin{pmatrix}P & Q & R\end{pmatrix}
=
P\,dx + Q\,dy + R\,dz
$$

apply the dictionary from the main text,

$$
\ast dx = dy \wedge dz,\qquad
\ast dy = dz \wedge dx,\qquad
\ast dz = dx \wedge dy
$$

to obtain

$$
\ast\omega
=
P\,dy\wedge dz
+
Q\,dz\wedge dx
+
R\,dx\wedge dy
$$

In the antisymmetric matrix representation of Chapter 2, let the matrix representing $dy\wedge dz$ be

$$
E_1 =
\begin{pmatrix}
0 & 0 & 0 \\
0 & 0 & 1 \\
0 & -1 & 0
\end{pmatrix}
$$

Similarly, let the matrix representing $dz\wedge dx$ be

$$
E_2 =
\begin{pmatrix}
0 & 0 & -1 \\
0 & 0 & 0 \\
1 & 0 & 0
\end{pmatrix}
$$

and let the matrix representing $dx\wedge dy$ be

$$
E_3 =
\begin{pmatrix}
0 & 1 & 0 \\
-1 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}
$$

Therefore,

$$
\ast_{1\to2}
=
\begin{pmatrix}
E_1\\
E_2\\
E_3
\end{pmatrix}
$$

can be viewed as a "vertical vector of matrices." Multiplying the $1$-form $\omega=\begin{pmatrix}P&Q&R\end{pmatrix}$ on the left gives

$$
\omega\,\ast_{1\to2}
=
\begin{pmatrix}P&Q&R\end{pmatrix}
\begin{pmatrix}
E_1\\
E_2\\
E_3
\end{pmatrix}
=
P E_1+Q E_2+R E_3
$$

Hence

$$
\ast_{1\to2}(\omega)
=
\begin{pmatrix}
0 & R & -Q \\
-R & 0 & P \\
Q & -P & 0
\end{pmatrix}
$$

The three coefficients $P,Q,R$ of the $1$-form have been placed into the three independent components of the antisymmetric matrix of the $2$-form. This is the most visible form of $\ast_{1\to2}$.

> <strong>Note</strong> (relation to $\widehat{\epsilon}$ in Chapter 2) These $E_1,E_2,E_3$ are the same matrices written in Appendix A as $\varepsilon_{1,\cdot,\cdot},\varepsilon_{2,\cdot,\cdot},\varepsilon_{3,\cdot,\cdot}$. The essence of $\ast_{1\to2}$ is to place the first index of Einstein's epsilon $\varepsilon_{ijk}$ in the direction of the components of the $1$-form, and the remaining two indices in the directions of the $3\times3$ matrix. The same triple introduced in Chapter 2 as the volume-measuring device $\widehat{\epsilon}$ reappears here as the Hodge star.

### D.2 $\ast_{2\to1}$ — extracting coefficients by the Frobenius product

The reverse map $\ast_{2\to1}$ is the operation that extracts three independent components from an antisymmetric matrix. Looking at matrix entries alone, it suffices to read $A=M_{23}$, $B=M_{31}$, $C=M_{12}$. That is, to return from the antisymmetric matrix

$$
M=
\begin{pmatrix}
0 & C & -B \\
-C & 0 & A \\
B & -A & 0
\end{pmatrix}
$$

representing the $2$-form

$$
\eta
=
A\,dy\wedge dz
+
B\,dz\wedge dx
+
C\,dx\wedge dy
$$

to $A\,dx+B\,dy+C\,dz$, one need only read these three components. If we stop at this mere "reading," however, the transpose relation with $\ast_{1\to2}$ is hard to see. So we rewrite coefficient extraction itself as an inner product between matrices.

Define the inner product of $3\times3$ matrices $A,B$ by

$$
A\cdot B
=
\frac{1}{2}\operatorname{tr}(A^T B)
=
\frac{1}{2}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
A_{ij}B_{ij}
$$

> <strong>Note</strong> (trace) $\operatorname{tr}$ is the <strong>trace</strong> of a matrix (the sum of diagonal entries). It appeared when we treated the matrix representation of the exterior derivative in Appendix B. $\operatorname{tr}(A^T B)$ is the three-step operation "transpose $A$, multiply by $B$, and add the diagonal entries." Since the product $A\cdot B$ is equivalently $\frac{1}{2}\sum A_{ij}B_{ij}$, use the latter expression when you want to think in components.

This is the same notation as the inner product $\mathbf{v}_1 \cdot \mathbf{v}_2$ between column vectors in §6.2.3. Matrices, too, are "things of the same kind," and we multiply corresponding components and take the sum. Because we contract successively over the two indices $i$ and $j$, this is called the <strong>Frobenius product</strong> or <strong>consecutive contraction</strong>.

> <strong>Note</strong> (the factor $1/2$) Some conventions adopt $\operatorname{tr}(A^T B)$ (without $1/2$) as the Frobenius product. For antisymmetric matrices, however, that picks up both members of a pair such as $M_{23}$ and $M_{32}=-M_{23}$, and the inner product is doubled. In this book we build $1/2$ into the definition. Then the inner product of the $2$-form $M$ with itself, $M\cdot M=M_{23}^2+M_{31}^2+M_{12}^2$, agrees directly with the "squared unsigned area of the parallelogram" in §6.2.2.

> <strong>Note</strong> (the pull of abstraction) §6.2.3 touched on an axiomatic inner product, but once you actually work by hand like this, you can see why that brevity is attractive. For the inner product of column vectors we use $\mathbf{v}_1^T \mathbf{v}_2$; for the inner product of matrices we use $\frac{1}{2}\operatorname{tr}(A^T B)$—redefining the inner product from scratch every time the representation changes is, when you think about it, quite a burden. One notices the urge to lump these together and settle everything with one phrase: "an inner product is an operation satisfying certain axioms." Even so, this book does not abandon its policy of making representations explicit to the end. By this point, that is stubbornness.

The $E_1,E_2,E_3$ of D.1 are orthonormal with respect to this inner product. Indeed, each $E_k$ has only two nonzero components; for the same $E_k$ we get $\frac{1}{2}(1^2+(-1)^2)=1$, and for different $E_i,E_j$ the positions of the nonzero components do not overlap. Therefore,

$$
E_i\cdot E_j=\delta_{ij}
$$

Using this orthonormality, the reverse transformation $\ast_{2\to1}$ can be written as inner products with $E_1,E_2,E_3$. Let $M$ be an arbitrary $3\times3$ matrix; when it comes from a $2$-form, $M$ is an antisymmetric matrix.

$$
\ast_{2\to1}(M)
=
\begin{pmatrix}
E_1\cdot M & E_2\cdot M & E_3\cdot M
\end{pmatrix}
$$

Here $E_k\cdot M=\frac{1}{2}\operatorname{tr}(E_k^T M)$ is the Frobenius product defined above. In components,

$$
\begin{aligned}
E_1 \cdot M &= \frac{1}{2}(M_{23}-M_{32}) \\
E_2 \cdot M &= \frac{1}{2}(M_{31}-M_{13}) \\
E_3 \cdot M &= \frac{1}{2}(M_{12}-M_{21})
\end{aligned}
$$

If $M$ is an antisymmetric matrix, then $M_{32}=-M_{23}$, $M_{13}=-M_{31}$, $M_{21}=-M_{12}$, so

$$
\ast_{2\to1}(M)
=
\begin{pmatrix}
M_{23} & M_{31} & M_{12}
\end{pmatrix}
$$

Therefore, $\ast_{2\to1}$ is at once the operation that extracts independent components from an antisymmetric matrix and coefficient extraction by the Frobenius product with $E_k$.

Writing out all components, $\ast_{2\to1}$ is the following "horizontal vector of matrices":

$$
\ast_{2\to1} = \begin{pmatrix}
\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix} &
\begin{pmatrix} 0 & 0 & -1 \\ 0 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix} &
\begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
\end{pmatrix}
$$

In $\ast_{1\to2}$ we multiply by coefficients and add; in $\ast_{2\to1}$ we extract coefficients by inner product. Vertical and horizontal, weighted sum and inner-product extraction, correspond to each other.

### D.3 $\ast\ast=\mathrm{id}$ in the $1$-form and $2$-form case

Combining D.1 and D.2, $\ast\ast=\mathrm{id}$ for $1$-forms and $2$-forms appears as orthonormality of arrays.

For

$$
\omega=P\,dx+Q\,dy+R\,dz
$$

D.1 gives

$$
\ast_{1\to2}(\omega)=P E_1+Q E_2+R E_3
$$

Applying $\ast_{2\to1}$ to this,

$$
\begin{aligned}
\ast_{2\to1}(\ast_{1\to2}(\omega))
&=
\begin{pmatrix}
E_1\cdot (P E_1+Q E_2+R E_3) &
E_2\cdot (P E_1+Q E_2+R E_3) &
E_3\cdot (P E_1+Q E_2+R E_3)
\end{pmatrix} \\
&=
\begin{pmatrix}
P & Q & R
\end{pmatrix}
=
\omega
\end{aligned}
$$

In the last equality we used $E_i\cdot E_j=\delta_{ij}$. That is, the three coefficients placed into $E_1,E_2,E_3$ by $\ast_{1\to2}$ are recovered unchanged by $\ast_{2\to1}$ through inner products with the same $E_1,E_2,E_3$.

The reverse direction is the same. For the antisymmetric matrix

$$
M=P E_1+Q E_2+R E_3
$$

D.2 gives

$$
\ast_{2\to1}(M)
=
\begin{pmatrix}
E_1\cdot M & E_2\cdot M & E_3\cdot M
\end{pmatrix}
=
\begin{pmatrix}
P & Q & R
\end{pmatrix}
$$

and applying D.1's $\ast_{1\to2}$,

$$
\ast_{1\to2}(\ast_{2\to1}(M))
=
P E_1+Q E_2+R E_3
=
M
$$

Therefore, in the $1$-form and $2$-form case,

$$
\ast_{2\to1}(\ast_{1\to2}(\omega))=\omega,
\qquad
\ast_{1\to2}(\ast_{2\to1}(M))=M
$$

hold. $\ast_{1\to2}$ places three coefficients into $E_1,E_2,E_3$; $\ast_{2\to1}$ extracts coefficients by inner product with $E_1,E_2,E_3$. Using the normalized Frobenius product, the transpose relation between the two appears as this correspondence between placement and coefficient extraction.

### D.4 Array representation of $\ast_{0\to3}$ and $\ast_{3\to0}$

So far we have displayed $\ast_{1\to2}$ and $\ast_{2\to1}$ as transformations that move coefficient arrays. What remains is $\ast_{0\to3}$ and $\ast_{3\to0}$.

A $0$-form has a single coefficient. A $3$-form, viewed purely as an array, is a completely antisymmetric third-order array with three indices. Therefore, $\ast_{0\to3}$ is the transformation that spreads one component into $3\times3\times3$ components, and $\ast_{3\to0}$ is the transformation that extracts one component from $3\times3\times3$ components.

Here we bring $\varepsilon_{ijk}$, which also appeared in Chapter 2, to the fore and look at its form.

> <strong>Note</strong> (what $\varepsilon_{ijk}$ really is) $\varepsilon_{ijk}$ is the completely antisymmetric symbol that appeared in Chapter 2. If the indices $(i,j,k)$ are an even permutation of $(1,2,3)$, it is $+1$; if an odd permutation, $-1$; if the same index appears twice, $0$. In an orthonormal Cartesian basis, it can be read as the component of a completely antisymmetric tensor. In this book we use those components as the representation of the Hodge star.

First, apply $\ast_{0\to3}$ to the $0$-form $f$. The output is a $3$-form, so it can be written in components with three indices. Here we take the components of $\ast_{0\to3}$ itself to be

$$
(\ast_{0\to3})_{ijk}
=
\varepsilon_{ijk}
$$

Display this as three $3\times3$ matrices with $i$ fixed—that is, for each of $i=1,2,3$, arrange the $(j,k)$ components as a matrix:

$$
(\ast_{0\to3})_{1jk}
=
\begin{pmatrix}
0&0&0\\
0&0&1\\
0&-1&0
\end{pmatrix},
$$

$$
(\ast_{0\to3})_{2jk}
=
\begin{pmatrix}
0&0&-1\\
0&0&0\\
1&0&0
\end{pmatrix},
$$

$$
(\ast_{0\to3})_{3jk}
=
\begin{pmatrix}
0&1&0\\
-1&0&0\\
0&0&0
\end{pmatrix}.
$$

As you can see, these are exactly the antisymmetric matrices $E_1,E_2,E_3$ used in D.1. That is,

$$
(\ast_{0\to3})_{1jk}= (E_1)_{jk},
\qquad
(\ast_{0\to3})_{2jk}= (E_2)_{jk},
\qquad
(\ast_{0\to3})_{3jk}= (E_3)_{jk}
$$

Almost nothing new happens here. The antisymmetric matrices $E_1,E_2,E_3$ seen in D.1 are now simply arranged as three slices with $i=1,2,3$. In the $1$-form and $2$-form case we read three coefficients as the coefficients of three antisymmetric matrices. In the $0$-form and $3$-form case we build, from one coefficient, the completely antisymmetric third-order array obtained by stacking all three slices at once.

Indeed, acting on the $0$-form $f$,

$$
(\ast_{0\to3}f)_{ijk}
=
(\ast_{0\to3})_{ijk}f
=
\varepsilon_{ijk}f
$$

This is the operation of spreading the coefficient $f$ into a completely antisymmetric third-order array.

Next, consider the reverse map $\ast_{3\to0}$. This is the transformation that takes a third-order array and returns a single coefficient. Its components are

$$
(\ast_{3\to0})_{ijk}
=
\frac{1}{3!}\varepsilon_{ijk}
$$

Therefore, displayed again as three $3\times3$ matrices with $i$ fixed,

$$
(\ast_{3\to0})_{1jk}
=
\frac{1}{3!}
\begin{pmatrix}
0&0&0\\
0&0&1\\
0&-1&0
\end{pmatrix},
$$

$$
(\ast_{3\to0})_{2jk}
=
\frac{1}{3!}
\begin{pmatrix}
0&0&-1\\
0&0&0\\
1&0&0
\end{pmatrix},
$$

$$
(\ast_{3\to0})_{3jk}
=
\frac{1}{3!}
\begin{pmatrix}
0&1&0\\
-1&0&0\\
0&0&0
\end{pmatrix}.
$$

That is, $\ast_{3\to0}$ uses the same three antisymmetric matrices. The only difference is that the whole thing is multiplied by $1/3!$.

If we think of the indices $(i,j,k)$ lined up in a row as a single number, then $\ast_{0\to3}$ is a column vector that spreads one component into $27$ components, and $\ast_{3\to0}$ is a row vector that extracts one component from $27$ components. Apart from the normalization factor $1/3!$, the two are in a transpose relation.

Let a $3$-form be represented by its completely antisymmetric components $\eta_{ijk}$. Acting with $\ast_{3\to0}$ sums over all three indices:

$$
\ast_{3\to0}\eta
=
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
(\ast_{3\to0})_{ijk}\eta_{ijk}
$$

Therefore,

$$
\ast_{3\to0}\eta
=
\frac{1}{3!}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
\varepsilon_{ijk}\eta_{ijk}
$$

This is a triple contraction that extracts one coefficient from a completely antisymmetric third-order array.

The factor $1/3!$ plays the same role as the $1/2$ that appears in the Frobenius product of D.2. In an antisymmetric matrix, each independent component appears twice, so we multiply by $1/2$ to correct for the duplication. Here, each independent component of a completely antisymmetric third-order array appears $3!=6$ times, so we multiply by $1/3!$ to correct for the duplication.

Let us verify that applying $\ast$ twice returns the original. First, start from the $0$-form $f$:

$$
\ast_{3\to0}(\ast_{0\to3}f)
=
\frac{1}{3!}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
\varepsilon_{ijk}(\ast_{0\to3}f)_{ijk}
$$

Since $(\ast_{0\to3}f)_{ijk}=\varepsilon_{ijk}f$,

$$
\ast_{3\to0}(\ast_{0\to3}f)
=
\frac{1}{3!}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
\varepsilon_{ijk}\varepsilon_{ijk}f
$$

Only the $3!=6$ cases in which $(i,j,k)$ is a permutation of $(1,2,3)$ are nonzero; then $\varepsilon_{ijk}\varepsilon_{ijk}=1$, so

$$
\ast_{3\to0}(\ast_{0\to3}f)
=
\frac{1}{3!}(3!)f
=
f
$$

Let us also check the reverse direction. An arbitrary $3$-form has only one independent component in three dimensions. Therefore the completely antisymmetric components $\eta_{ijk}$ can be written using some coefficient $h$ as

$$
\eta_{ijk}
=
h\,\varepsilon_{ijk}
$$

Then

$$
\ast_{3\to0}\eta
=
\frac{1}{3!}
\sum_{i=1}^{3}
\sum_{j=1}^{3}
\sum_{k=1}^{3}
\varepsilon_{ijk}(h\varepsilon_{ijk})
=
h
$$

Therefore,

$$
(\ast_{0\to3}(\ast_{3\to0}\eta))_{ijk}
=
(\ast_{0\to3}h)_{ijk}
=
h\varepsilon_{ijk}
=
\eta_{ijk}
$$

Thus we have confirmed $\ast\ast=\mathrm{id}$ in the $0$-form and $3$-form case as well, in the array representation.

In the end, what we saw here is the same as in D.1–D.3. In $\ast_{1\to2}$ we distributed three coefficients among three antisymmetric matrices. In $\ast_{0\to3}$ we distributed one coefficient simultaneously among all three antisymmetric matrices. In $\ast_{2\to1}$ we extracted coefficients from an antisymmetric matrix; in $\ast_{3\to0}$ we extracted coefficients by triple contraction with the three antisymmetric matrices. The Hodge star, at every degree, is a linear transformation that can be displayed as a concrete array once a basis is chosen.

### D.5 Summary

> <strong>Checkpoint so far — Appendix D</strong>
> - $\ast_{1\to2}$ is the linear transformation that places three coefficients into the antisymmetric matrices $E_1,E_2,E_3$.
> - $\ast_{2\to1}$ is the linear transformation that extracts coefficients from an antisymmetric matrix, and can be written by the Frobenius product with $E_k$.
> - Using the Frobenius product $A\cdot B=\frac{1}{2}\operatorname{tr}(A^TB)$, we have $E_i\cdot E_j=\delta_{ij}$.
> - Therefore, in the $1$-form and $2$-form case, $\ast_{2\to1}(\ast_{1\to2}(\omega))=\omega$ and $\ast_{1\to2}(\ast_{2\to1}(M))=M$ hold.
> - $\ast_{0\to3}$ can be displayed as a third-order array obtained by stacking the three antisymmetric matrices $E_1,E_2,E_3$. In components, $(\ast_{0\to3})_{ijk}=\varepsilon_{ijk}$.
> - $\ast_{3\to0}$ can be displayed as the same array multiplied by the normalization factor $1/3!$. In components, $(\ast_{3\to0})_{ijk}=\frac{1}{3!}\varepsilon_{ijk}$.
> - The factors $1/2$ and $1/3!$ correct for duplication of antisymmetric components.
> - In the $0$-form/$3$-form case as well, $\ast_{3\to0}(\ast_{0\to3}f)=f$ and $\ast_{0\to3}(\ast_{3\to0}\eta)=\eta$ hold.
> - Therefore, the Hodge star $\ast$, for both $0\leftrightarrow3$ and $1\leftrightarrow2$, is a linear transformation that can be displayed as a concrete array once a basis is chosen.

# Chapter 7: Vector Analysis — Enter Nabla

# Chapter 7: Vector Analysis — Enter Nabla

### §7.0 Enter Nabla

The title of this book is *Unmasking Nabla*—yet up to this point we have never once defined nabla $\nabla$ head-on, at least officially. In Chapter 6 we got a preview of the shapes of grad, curl, and div by combining $d$ and $\ast$. In this chapter we rewrite the same objects in the standard notation of vector analysis.

What have we been doing instead? We have piled up the backstage tools: $dx$ as a row vector, $2$-forms as antisymmetric matrices, $d$ as the operation that raises degree—and so on. Some readers have surely been wondering, “When is $\nabla$ finally going to show up?”

I have been worrying about false advertising in the title for quite a while myself.

In this chapter we finally define $\nabla$. Then we unfold standard vector analysis—gradient, divergence, curl, the Laplacian, and the various identities—straight from the textbook, all at once. In the calculations in the main text, we set $d$, $\ast$, and $\wedge$ aside for now. This is the very vector analysis that many readers learned (probably while struggling) in their first or second year of university.

> <strong>Note</strong> (Why now) In Chapter 6 we previewed the shapes of grad, curl, and div using $d$ and $\ast$. In this chapter we deliberately unfold the same objects in standard vector-analysis notation, formula after formula. If, when you finish this chapter, you feel that there are too many formulas, that is fine. That discomfort will be the driving force for matching the two notations in the next chapter.

The tools used in this chapter are only those we have already assembled—column vectors, row vectors, matrices, inner products, the Jacobian matrix, and partial derivatives.


### §7.2 $\nabla$ and the Gradient

#### 7.2.1 Definition of $\nabla$

English textbooks usually call the symbol $\nabla$ <strong>del</strong>; it is also called <strong>nabla</strong>, the name common in Japanese texts. This book is about what div, grad, and curl do—not primarily about what to call the symbol. We define nabla $\nabla$ as a formal column vector whose components are partial-derivative operators:

$$\nabla = \begin{pmatrix}
\frac{\partial}{\partial x} \\[0.5em]
\frac{\partial}{\partial y} \\[0.5em]
\frac{\partial}{\partial z}
\end{pmatrix}$$

$\nabla$ is a “vector,” but its components are not numbers—they are <strong>differential operators</strong>. $\nabla$ does not ordinarily have a value as a vector quantity on its own; it returns a concrete field only when it acts on something.

#### 7.2.2 Gradient

What we obtain by letting $\nabla$ act on a scalar field $f(x,y,z)$ is called the <strong>gradient</strong>, written $\mathrm{grad}\,f$ or $\nabla f$:

$$\mathrm{grad}\,f = \nabla f = \begin{pmatrix}
\frac{\partial f}{\partial x} \\[0.5em]
\frac{\partial f}{\partial y} \\[0.5em]
\frac{\partial f}{\partial z}
\end{pmatrix}$$

Each component of the gradient is the rate of change of $f$ in the corresponding coordinate direction. Geometrically, $\nabla f$ is the vector field pointing in the direction of steepest increase of $f$.

> <strong>Note</strong> (Is the gradient a row vector or a column vector?) In §6.5 we wrote $\mathrm{grad}\,f = df$, and $df$ was a row vector of coefficients. In this chapter we treat $\nabla f$ as a column vector. Using the Euclidean metric introduced in Chapter 6, we read the $1$-form $df$ as the corresponding column vector and obtain $\nabla f$. In §6.5 we stood on the view that “the differential itself (the form) measures properties of space”; in this chapter we adopt the standard vector-analysis view that “at each point an arrow (a vector) stands.” The starting pictures differ, but if we aggregate by line integral we get the same scalar quantity. That agreement is no accident.

<strong>Example</strong>: the gradient of $f(x,y,z) = x^2 + y^2 + z^2$.

$$\nabla f = \begin{pmatrix} 2x \\ 2y \\ 2z \end{pmatrix}$$

This vector field points radially outward from the origin and grows larger as one moves away from the origin.

---

### §7.3 Divergence

For a vector field

$$
\mathbf{F}(x,y,z)
=
\begin{pmatrix}
F_x\\
F_y\\
F_z
\end{pmatrix}
$$

we call the operation $\nabla\cdot\mathbf{F}$ the <strong>divergence</strong>.

$$\mathrm{div}\,\mathbf{F} = \nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$$

Formally this is “the dot product of $\nabla$ and $\mathbf{F}$,” but since each component of $\nabla$ is a differential operator, the result is a scalar field.

> <strong>Note</strong> (connection to Chapter 6) In Chapter 6 we defined divergence on a $1$-form as $\mathrm{div}\,\omega = \ast\,d\,\ast\,\omega$. The $\mathrm{div}\,\mathbf{F}$ above is the same operation, written here in nabla notation for the vector field corresponding to that $1$-form.

Divergence can also be written in the language of matrices. Consider the Jacobian matrix $\mathbf{J}_\mathbf{F}$ of $\mathbf{F}$.

$$\mathbf{J}_\mathbf{F} = \begin{pmatrix}
\frac{\partial F_x}{\partial x} & \frac{\partial F_x}{\partial y} & \frac{\partial F_x}{\partial z} \\[0.3em]
\frac{\partial F_y}{\partial x} & \frac{\partial F_y}{\partial y} & \frac{\partial F_y}{\partial z} \\[0.3em]
\frac{\partial F_z}{\partial x} & \frac{\partial F_z}{\partial y} & \frac{\partial F_z}{\partial z}
\end{pmatrix}$$

The <strong>trace</strong> (sum of the diagonal entries) of this matrix agrees with the divergence.

$$\mathrm{div}\,\mathbf{F} = \operatorname{tr}(\mathbf{J}_\mathbf{F}) = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$$

Physically, $\mathrm{div}\,\mathbf{F}$ measures the strength of outflow at that point. If it is positive, there is outflow; if negative, inflow; if zero, there is neither outflow nor inflow at that point.

<strong>Example</strong>:

$$
\mathbf{F}
=
\begin{pmatrix}
x\\
y\\
z
\end{pmatrix}
$$

The divergence of this field is

$$\nabla \cdot \mathbf{F} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = 3$$

<strong>Example</strong>:

$$
\mathbf{F}
=
\begin{pmatrix}
-y\\
x\\
0
\end{pmatrix}
$$

The divergence of this field is

$$\nabla \cdot \mathbf{F} = \frac{\partial (-y)}{\partial x} + \frac{\partial x}{\partial y} + \frac{\partial 0}{\partial z} = 0 + 0 + 0 = 0$$

This field rotates, but there is no outflow or inflow.

---


### §7.4 Curl

For a vector field $\mathbf{F}$, the operation $\nabla\times\mathbf{F}$ is called the <strong>curl</strong>.

$$\mathrm{curl}\,\mathbf{F} = \nabla \times \mathbf{F} = \begin{pmatrix}
\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z} \\[0.5em]
\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x} \\[0.5em]
\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}
\end{pmatrix}$$

Using the cross-product matrix, we can also write

$$\mathrm{curl}\,\mathbf{F} = (\nabla \times)\,\mathbf{F} = \begin{pmatrix}
0 & -\frac{\partial}{\partial z} & \frac{\partial}{\partial y} \\[0.3em]
\frac{\partial}{\partial z} & 0 & -\frac{\partial}{\partial x} \\[0.3em]
-\frac{\partial}{\partial y} & \frac{\partial}{\partial x} & 0
\end{pmatrix}\begin{pmatrix}
F_x \\ F_y \\ F_z
\end{pmatrix}$$

> <strong>Note</strong> (connection to Chapter 6) Chapter 6 defined curl on a $1$-form as $\mathrm{curl}\,\omega = \ast\,d\,\omega$. The $\mathrm{curl}\,\mathbf{F}$ above is the same operation, written here in nabla notation for the corresponding vector field.

Physically, $\mathrm{curl}\,\mathbf{F}$ represents the strength and direction of the vortex at that point. It points along the axis of the vortex, and its magnitude corresponds to the strength of the vortex.

<strong>Example</strong>:

$$
\mathbf{F}
=
\begin{pmatrix}
-y\\
x\\
0
\end{pmatrix}
$$

The curl of this field is

$$\nabla \times \mathbf{F} = \begin{pmatrix}
\frac{\partial 0}{\partial y} - \frac{\partial x}{\partial z} \\[0.3em]
\frac{\partial (-y)}{\partial z} - \frac{\partial 0}{\partial x} \\[0.3em]
\frac{\partial x}{\partial x} - \frac{\partial (-y)}{\partial y}
\end{pmatrix} = \begin{pmatrix}
0 - 0 \\ 0 - 0 \\ 1 - (-1)
\end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 2 \end{pmatrix}$$

This field rotates uniformly about the $z$-axis, and the strength of the vortex is $2$.

<strong>Example</strong>:

$$
\mathbf{F}
=
\begin{pmatrix}
x\\
y\\
z
\end{pmatrix}
$$

The curl of this field is

$$\nabla \times \mathbf{F} = \begin{pmatrix}
\frac{\partial z}{\partial y} - \frac{\partial y}{\partial z} \\[0.3em]
\frac{\partial x}{\partial z} - \frac{\partial z}{\partial x} \\[0.3em]
\frac{\partial y}{\partial x} - \frac{\partial x}{\partial y}
\end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$

A radial field has no vortex—consistent with intuition.

> <strong>Checkpoint — §7.2–§7.4</strong>
> - $\nabla$ is the formal vector obtained by stacking $\partial_x,\partial_y,\partial_z$ vertically.
> - $\mathrm{grad}\,f = \nabla f$ (gradient): scalar field → vector field.
> - $\mathrm{div}\,\mathbf{F} = \nabla \cdot \mathbf{F}$ (divergence): vector field → scalar field. Equal to the trace of the Jacobian matrix.
> - $\mathrm{curl}\,\mathbf{F} = \nabla \times \mathbf{F}$ (curl): vector field → vector field. Can be written using the cross-product matrix.

---

### §7.5 The Laplacian

Applying the gradient (scalar → vector) and then the divergence (vector → scalar) in succession yields an operation from a scalar field to a scalar field. This is called the <strong>Laplacian</strong>.

$$\nabla^2 f = \mathrm{div}(\mathrm{grad}\,f) = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$

The notation $\nabla^2$ is shorthand for $\nabla \cdot \nabla$, and some authors write $\Delta f$ instead.

<strong>Example</strong>: The Laplacian of $f(x,y,z) = x^2 + y^2 + z^2$.

$$\nabla^2 f = \frac{\partial^2}{\partial x^2}(x^2) + \frac{\partial^2}{\partial y^2}(y^2) + \frac{\partial^2}{\partial z^2}(z^2) = 2 + 2 + 2 = 6$$

For a vector field $\mathbf{F}$ as well, applying the Laplacian to each component is called the <strong>vector Laplacian</strong>.

$$\nabla^2 \mathbf{F} = \begin{pmatrix} \nabla^2 F_x \\ \nabla^2 F_y \\ \nabla^2 F_z \end{pmatrix}$$

The Laplacian appears everywhere in physics. The heat equation, the wave equation, Poisson's equation—all are equations built around $\nabla^2$.

---


### §7.6 Identities

Among the three operations defined so far, two important identities hold. Both take the form "applying twice gives zero."

#### 7.6.1 $\mathrm{curl}(\mathrm{grad}\,f) = \mathbf{0}$

If we take a vector field from a gradient and then take its curl, we always get the zero vector.

$$\nabla \times (\nabla f) = \begin{pmatrix}
\frac{\partial}{\partial y}\frac{\partial f}{\partial z} - \frac{\partial}{\partial z}\frac{\partial f}{\partial y} \\[0.5em]
\frac{\partial}{\partial z}\frac{\partial f}{\partial x} - \frac{\partial}{\partial x}\frac{\partial f}{\partial z} \\[0.5em]
\frac{\partial}{\partial x}\frac{\partial f}{\partial y} - \frac{\partial}{\partial y}\frac{\partial f}{\partial x}
\end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$$

In each component, terms cancel by exchanging the order of partial derivatives $\frac{\partial^2 f}{\partial y\partial z} = \frac{\partial^2 f}{\partial z\partial y}$. This always holds if $f$ is smooth (twice continuously differentiable).

Physical meaning: "A gradient field has no vortex." Conservative gravitational and electrostatic fields fall into this category.

#### 7.6.2 $\mathrm{div}(\mathrm{curl}\,\mathbf{F}) = 0$

If we take a vector field from a curl and then take its divergence, we always get zero.

$$\nabla \cdot (\nabla \times \mathbf{F}) = \frac{\partial}{\partial x}\!\left(\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}\right) + \frac{\partial}{\partial y}\!\left(\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}\right) + \frac{\partial}{\partial z}\!\left(\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right)$$

When expanded, terms pair up and cancel by exchanging the order of partial derivatives, as in $\frac{\partial^2 F_z}{\partial x\partial y}$ and $-\frac{\partial^2 F_z}{\partial y\partial x}$, so the sum is $0$.

Physical meaning: "A curl field has no outflow or inflow." This is the identity reflected in Maxwell's equation $\nabla\cdot\mathbf B=0$, the mathematical expression of the absence of magnetic monopoles.

> <strong>Checkpoint — §7.5–§7.6</strong>
> - $\nabla^2 f = \mathrm{div}(\mathrm{grad}\,f)$ is the Laplacian of a scalar field. It describes heat conduction and waves.
> - $\mathrm{curl}(\mathrm{grad}\,f) = \mathbf{0}$: A gradient field has no vortex.
> - $\mathrm{div}(\mathrm{curl}\,\mathbf{F}) = 0$: A curl field has no outflow or inflow.
> - All follow from exchanging the order of partial derivatives $\partial_i\partial_j = \partial_j\partial_i$.

---


### §7.7 A Formula Collection for Nabla

For practical calculation, we collect product rules involving $\nabla$ and representative vector identities for smooth scalar and vector fields. Below, $f, g$ denote scalar fields and $\mathbf{F}, \mathbf{G}$ denote vector fields.

#### 7.7.1 Product rules

<strong>Gradient of a product</strong>:

$$\nabla(fg) = f\,\nabla g + g\,\nabla f$$

<strong>Divergence of a product</strong>:

$$\nabla \cdot (f\mathbf{F}) = (\nabla f) \cdot \mathbf{F} + f\,(\nabla \cdot \mathbf{F})$$

<strong>Curl of a product</strong>:

$$\nabla \times (f\mathbf{F}) = (\nabla f) \times \mathbf{F} + f\,(\nabla \times \mathbf{F})$$

<strong>Divergence of a cross product</strong>:

$$\nabla \cdot (\mathbf{F} \times \mathbf{G}) = (\nabla \times \mathbf{F}) \cdot \mathbf{G} - \mathbf{F} \cdot (\nabla \times \mathbf{G})$$

#### 7.7.2 Identities for double application

The curl of the gradient of a scalar field and the divergence of the curl of a vector field were derived in §7.6. We restate them here as part of the formula collection.

<strong>Curl of a gradient is zero</strong>:

$$\nabla \times (\nabla f) = \mathbf{0}$$

<strong>Divergence of a curl is zero</strong>:

$$\nabla \cdot (\nabla \times \mathbf{F}) = 0$$

<strong>Curl of a curl</strong>:

$$\nabla \times (\nabla \times \mathbf{F}) = \nabla(\nabla \cdot \mathbf{F}) - \nabla^2 \mathbf{F}$$

This is the formula that decomposes the Laplacian into divergence and curl. The derivation uses the BAC-CAB rule (§7.7.4).

<strong>Divergence of the gradient of a scalar field</strong> (= Laplacian):

$$\nabla \cdot (\nabla f) = \nabla^2 f$$

This is exactly the definition from §7.5.

#### 7.7.3 Scalar triple product

The scalar triple product of three column vectors $\mathbf{A}, \mathbf{B}, \mathbf{C}$ is defined as the dot product of $\mathbf{A}$ with $\mathbf{B}\times\mathbf{C}$.

$$\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C})$$

This value equals the signed volume of the parallelepiped spanned by $\mathbf{A}, \mathbf{B}, \mathbf{C}$. It is invariant under cyclic permutation, and swapping two vectors reverses the sign.

$$\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A}) = \mathbf{C} \cdot (\mathbf{A} \times \mathbf{B})$$

#### 7.7.4 Vector triple product (BAC-CAB rule)

$$\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B}(\mathbf{A} \cdot \mathbf{C}) - \mathbf{C}(\mathbf{A} \cdot \mathbf{B})$$

This appears when the cross product is used twice. Each term on the right is a vector scaled by a scalar, and the mnemonic is BAC-CAB.

> <strong>Note</strong> (why we listed the formulas) The formulas listed here are typical of the ones students are forced to memorize on university vector-analysis exams. One might ask: if we rewrite everything with $d$ and $\ast$, does the number of formulas shrink dramatically? Not necessarily. On the differential-forms side too, there are rules such as $d(f\omega) = df\wedge\omega + f d\omega$ in comparable quantity.
>
> The real problem of vector analysis is not the number of formulas. <strong>Everything looks like the same "bundle of three-component arrows."</strong> $\nabla f$, $\nabla \times \mathbf{F}$, and $\nabla^2\mathbf{F}$ all look on the screen like nothing but bundles of arrows. Yet $\nabla f$ is the gradient (the slope of a potential), $\nabla \times \mathbf{F}$ is the axis of a vortex—the geometric meaning of the arrows is entirely different. If you rely on drawing pictures and intuition, the distinction vanishes the moment a problem gets complicated. Differential forms prevent this confusion in principle by making the degree of the measuring instrument explicit: $0$-form, $1$-form, $2$-form, $3$-form. $d$ always raises the degree by $1$, and $\ast$ always reverses the degree—because type information rides on a few rules, you can tell what an expression is doing from its form alone, without looking at arrows. This is why we return to the language of forms from Chapter 8 onward.


> <strong>Note</strong> (just between us) Writing down the correspondences $\mathrm{grad}=d$, $\mathrm{curl}=\ast d$, $\mathrm{div}=\ast d\ast$ is, in fact, partly a compromise for dismantling vector analysis.
>
> In some introductory explanations of differential forms, what can be written neatly is often emphasized. But if you try seriously to translate vector analysis, $\ast$ keeps appearing and the appearance does not necessarily become simpler. For example, if we rewrite the vector triple product $\mathbf{A}\times(\mathbf{B}\times\mathbf{C})$ from §7.7.4 in this framework, nested $\ast$ appear as in $\ast(\alpha \wedge \ast(\beta \wedge \gamma))$, and it exposes a form more awkward than vector analysis itself.
>
> Even so, some introductory books emphasize beauty because the world before summoning the "strong constraint" called a metric—that is, the landscape woven only from $d$ and $\wedge$, without $\ast$—is so pure and beautiful. The fact that the skeleton of physical laws such as Maxwell's equations is fixed even before defining a metric (an inner product) is indeed striking.
>
> To head toward that "pure world of differential forms," we deliberately carry out once this awkward, $\ast$-covered translation work. That is the aim of this stage of the book. If you find these "vector analysis via differential forms" calculations dirty and unnatural, that reaction is correct. At that moment, you have already graduated from being a beginner in vector analysis.

---

### §7.8 Integral Theorems — Stokes, Gauss, and Green

The most important job of vector analysis is to connect differential operators (grad, div, curl) with integration. Below we state the three integral theorems in the language of $\nabla$.

#### 7.8.1 Stokes' Theorem

For a surface $S$ and its boundary, the closed curve $C = \partial S$,

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS$$

The left-hand side is the line integral (circulation) of $\mathbf{F}$ along the curve $C$; the right-hand side is the surface integral of the normal component of the curl on the surface $S$. It means that "circulation on the boundary equals the total vorticity inside." Here $\mathbf{n}$ is the unit normal vector to the surface, chosen in the right-hand-screw relation to the orientation of $C$.

> <strong>Note</strong> (Green's theorem) When $S$ is a region $D$ in the $xy$ plane and the components of $\mathbf{F}$ are $F_x=P,\;F_y=Q,\;F_z=0$, Stokes' theorem takes the following form, with the positive orientation on $\partial D$. This is called Green's theorem.
>
> $$\oint_{\partial D} (P\,dx + Q\,dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx\,dy$$

#### 7.8.2 Gauss' Theorem

For a solid $V$ and its boundary, the closed surface $S = \partial V$,

$$\oiint_S \mathbf{F} \cdot \mathbf{n}\,dS = \iiint_V (\nabla \cdot \mathbf{F})\,dV$$

The left-hand side is the outward flux of $\mathbf{F}$ through the closed surface $S$; the right-hand side is the volume integral of the divergence inside the solid $V$. It means that "the total flow through the boundary equals the total sources inside."

#### 7.8.3 Common Structure of the Integral Theorems

Placed side by side, Stokes' theorem and Gauss' theorem reveal a common pattern.

| Theorem | Integral on the boundary | Integral in the interior | Differential operator |
|---|---|---|---|
| Stokes | $\displaystyle\oint_C \mathbf{F}\cdot d\mathbf{r}$ | $\displaystyle\iint_S (\nabla\times\mathbf{F})\cdot\mathbf{n}\,dS$ | curl |
| Gauss | $\displaystyle\oiint_S \mathbf{F}\cdot\mathbf{n}\,dS$ | $\displaystyle\iiint_V (\nabla\cdot\mathbf{F})\,dV$ | div |

Each has the form "quantity measured on the boundary = sum of differential quantities in the interior." In this framework, §7.6's $\mathrm{div}(\mathrm{curl})=0$ can be read as "a curl field has no divergence, so nothing emerges from a closed surface that encloses it."

Yet one dissatisfaction remains. Because the vector-analysis language splits the same pattern across different operators such as curl and div, these formulas are usually <strong>memorized as separate theorems</strong>. Recall that in Chapter 5, a single formula $\int_{\partial M}\omega = \int_M d\omega$ unified all of these. In Chapter 8 we will organize the correspondence that rewrites the integral theorems of the $\nabla$ world into this single form.

> <strong>Checkpoint so far — §7.8</strong>
> - Stokes' theorem: $\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S (\nabla\times\mathbf{F})\cdot\mathbf{n}\,dS$
> - Gauss' theorem: $\oiint_S \mathbf{F}\cdot\mathbf{n}\,dS = \iiint_V (\nabla\cdot\mathbf{F})\,dV$
> - Green's theorem is the planar version of Stokes' theorem.
> - These integral theorems share the common structure "integral on the boundary = integral of a differential in the interior," but in the language of $\nabla$ they must be treated as separate theorems.

---


### §7.9 Toward Chapter 8 — Do Not Look at the Arrows; Look at the Measuring Devices

In Chapter 6 we saw that by combining the exterior derivative $d$ and the Hodge star $\ast$, three types appear: $\mathrm{grad}=d$, $\mathrm{curl}=\ast d$, and $\mathrm{div}=\ast d\ast$.

In this chapter we rewrote the same objects in the language of standard vector analysis. $\nabla f$, $\nabla\times\mathbf F$, and $\nabla\cdot\mathbf F$ are convenient, but on the screen they all look like arrows and scalars. Yet the geometric meaning each one carries is entirely different. And the more complex the problem becomes, the harder it is to distinguish them by looking at arrows alone.

In the next chapter we will align the $d$ and $\ast$ types obtained in Chapter 6 with the $\nabla$ notation introduced in this chapter. By reading $\nabla f$ as $df$, and for the $1$-form $\omega$ corresponding to $\mathbf F$, reading $\nabla\times\mathbf F$ as $\ast d\omega$ and $\nabla\cdot\mathbf F$ as $\ast d\ast\omega$, the formulas of standard vector analysis are organized as equations that carry the degree of measuring devices. Think in the algebra of measuring devices, not in pictures of arrows—that viewpoint will be connected to standard vector-analytic notation in the next chapter.

> <strong>Checkpoint so far — Chapter 7</strong>
> - We defined $\nabla$ as a formal vector with partial-derivative operators stacked vertically, and introduced gradient, divergence, curl, and the Laplacian.
> - $\mathrm{grad}\,f = \nabla f$, $\mathrm{div}\,\mathbf{F} = \nabla \cdot \mathbf{F} = \operatorname{tr}(\mathbf{J}_\mathbf{F})$, $\mathrm{curl}\,\mathbf{F} = \nabla \times \mathbf{F}$.
> - $\nabla^2 = \mathrm{div}\,\mathrm{grad}$, $\mathrm{curl}(\mathrm{grad}) = 0$, $\mathrm{div}(\mathrm{curl}) = 0$.
> - We confirmed the cross-product matrix as the antisymmetric-matrix representation connected to exterior products, and reviewed the BAC-CAB rule.
> - The difficulty of vector analysis lies not only in the number of formulas but in the fact that everything looks like the same arrow. Differential forms distinguish objects by the degree of measuring devices ($n$-forms). Chapter 8 will connect these two languages.

# Chapter 8: Two Languages — Differentiating Measuring Devices and Differentiating Fields

# Chapter 8: Two Languages — Differentiating Measuring Devices and Differentiating Fields

### §8.0 The Highlight of This Book

It has been a long road. In Chapter 1 we defined $dx$ as a row vector; in Chapter 2 we built area-measuring devices and volume-measuring devices; in Chapter 3 we rebuilt integration; in Chapter 5 we obtained the exterior derivative $d$; in Chapter 6 we acquired the metric $g$ and the Hodge star $\ast$; and in Chapter 7 we finally defined $\nabla$ head-on and unfolded vector analysis all at once.

From here on, there is no holding back. $d$, $\ast$, and $\nabla$—all the tools are in hand. We no longer need to warn, “for readers who already know vector analysis,” whenever we invoke the vocabulary of vector analysis. $\nabla$ became a proper resident of this book in Chapter 7.

This chapter is the <strong>highlight</strong> of the book. The central translation itself is surprisingly short. At the end, however, to move on to the practical chapter that follows, we will take a single look at how this dictionary behaves in curvilinear coordinates. The painstaking preparation from Chapters 1 through 7—matrices, wedge products, the exterior derivative, the metric, the Hodge star, and vector analysis—was all for that purpose. Because all these tools are now assembled, in this chapter we need only “translate,” and two worlds fit into one picture. We have acquired two languages—the differential of measuring devices ($d$) and the differential of fields ($\nabla$). These two do fundamentally different things. Yet when they are linked through integration, they give exactly the same results. We will now dig thoroughly into how that works.


### §8.2 Completing the Translation Dictionary

In Chapter 6 §6.5 we introduced the correspondences $\mathrm{grad}=d$, $\mathrm{curl}=\ast d$, and $\mathrm{div}=\ast d\ast$. Here we align this dictionary with the language of $\nabla$ and organize it in complete form. What we complete here is the translation dictionary used within three-dimensional Euclidean space and the matrix representation of this book.

In the dictionary below, the $1$-form corresponding to a vector field

$$
\mathbf{F}
=
\begin{pmatrix}
F_x\\
F_y\\
F_z
\end{pmatrix}
$$

is read using the metric $g$ as

$$
\omega=\mathbf{F}^T g
$$

In Cartesian coordinates $g=I$, so

$$
\omega
=
\begin{pmatrix}
F_x & F_y & F_z
\end{pmatrix}
=
F_x\,dx+F_y\,dy+F_z\,dz
$$

In orthogonal Cartesian coordinates the components look the same, but this does not mean they are the same object. A vector field is a column vector; a $1$-form is a row vector; and the correspondence between them involves the metric $g$.

#### 8.2.1 Gradient

$$
\mathrm{grad}\,f = \nabla f
\quad\longleftrightarrow\quad
df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz
$$

$\nabla f$ is a <strong>column vector</strong>; $df$ is a <strong>row vector</strong>. In Cartesian coordinates the components look the same, but the types differ. In the notation of Chapter 6, to read $df$ as the corresponding column vector we use $g^{-1}(df)^T$. In Cartesian coordinates $g=I$, so its components agree with the usual $\nabla f$.

#### 8.2.2 Curl

$$
\mathrm{curl}\,\mathbf{F} = \nabla \times \mathbf{F}
\quad\longleftrightarrow\quad
\ast d\omega
$$

$\nabla\times\mathbf{F}$ is a <strong>column vector</strong>; $d\omega$ is a <strong>$2$-form (antisymmetric matrix)</strong>; and $\ast d\omega$ is a <strong>$1$-form (row vector)</strong>. To compare it directly with the column-vector display of $\nabla\times\mathbf F$, we again read the $1$-form $\ast d\omega$ back through the metric as $g^{-1}(\ast d\omega)^T$. Curl is a two-stage operation: "raise the degree by the exterior derivative, then bring the degree back down with the Hodge star."

The $x$-component $\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}$ of $\nabla\times\mathbf{F}$ agrees with the coefficient of $dx$ in $\ast d\omega$. This is exactly the correspondence confirmed in Chapter 6.

#### 8.2.3 Divergence

$$
\mathrm{div}\,\mathbf{F} = \nabla \cdot \mathbf{F}
\quad\longleftrightarrow\quad
\ast d \ast \omega
$$

$\nabla\cdot\mathbf{F}$ is a <strong>scalar field</strong>; $\ast d\ast\omega$ is also a <strong>$0$-form (scalar field)</strong>. Divergence is a three-stage operation: "turn it into a $2$-form with the Hodge star, raise it to a $3$-form by the exterior derivative, then drop it back to a scalar with the Hodge star again."

#### 8.2.4 Summary Table of the Dictionary

| Operation | Vector analysis side | Differential forms (measuring device) side | To read back as a vector field |
|:---:|:---:|:---:|:---:|
| Gradient | $\mathrm{grad}\,f$ | $df$ | $g^{-1}(df)^T$ |
| Curl | $\mathrm{curl}\,\mathbf{F}$ | $\ast d\omega$ | $g^{-1}(\ast d\omega)^T$ |
| Divergence | $\mathrm{div}\,\mathbf{F}$ | $\ast d\ast\omega$ | as-is $0$-form |

The more times $\ast$ is used, the higher the "translation cost" between $\nabla$ notation and $d,\ast$ notation.
Here $\omega=\mathbf{F}^Tg$. For the gradient, $\ast$ appears zero times, but converting $df$ to the usual gradient vector requires the metric conversion $g^{-1}(df)^T$. For curl, $\ast$ appears once; for divergence, twice. This translation dictionary built from the metric $g$ and $\ast$ was the reason we felt in Chapter 7 §7.7 that "differential forms are messy."

> <strong>Checkpoint so far — §8.2</strong>
> - $\nabla f \leftrightarrow df$, $\nabla\times\mathbf{F} \leftrightarrow \ast d\omega$, $\nabla\cdot\mathbf{F} \leftrightarrow \ast d\ast\omega$.
> - Number of $\ast$ uses: gradient $0$, curl $1$, divergence $2$. This translation cost is the real source of the impression that "differential forms are messy."

---


### §8.3 Translating Stokes' Theorem

In Chapter 5 §5.6 we already derived Stokes' theorem in the form $\int_{\partial S}\omega = \int_S d\omega$. In Chapter 7 §7.8.1 we wrote the same theorem in the language of $\nabla$ as $\oint_C \mathbf{F}\cdot d\mathbf{r} = \iint_S (\nabla\times\mathbf{F})\cdot\mathbf{n}\,dS$. We now confirm that these two are the same thing, using the dictionary of §8.2.

#### 8.3.1 From $\nabla$ to $d$

Start with Stokes' theorem in $\nabla$ notation.

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS$$

The left-hand side $\oint_C \mathbf{F}\cdot d\mathbf{r}$ is the line integral of the vector field $\mathbf{F}$ along the curve $C$. If we let the $1$-form corresponding to $\mathbf{F}$ be $\omega = F_x\,dx + F_y\,dy + F_z\,dz$, then by the definition of Chapter 3 this equals $\int_C \omega$.

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \int_{\partial S} \omega$$

The right-hand side $\iint_S (\nabla\times\mathbf{F})\cdot\mathbf{n}\,dS$ is the surface integral of the normal component of the curl. Here we read a surface integral of the normal component of a vector field as the surface integral of the corresponding $2$-form. Using the dictionary $\nabla\times\mathbf{F} \leftrightarrow \ast d\omega$, $(\nabla\times\mathbf{F})\cdot\mathbf{n}\,dS$ corresponds to the surface integral of the $2$-form $\ast(\ast d\omega) = d\omega$ (the $\ast$'s cancel by $\ast\ast = \mathrm{id}$).

$$\iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n}\,dS = \int_S d\omega$$

Therefore,

$$\int_{\partial S} \omega = \int_S d\omega$$

This is exactly the formula obtained in Chapter 5 §5.6. Stokes' theorem in the world of $\nabla$, once translated through the dictionary into the language of $d$, becomes nothing but $\int_{\partial M}\omega = \int_M d\omega$.

#### 8.3.2 Round-Trip Translation — Either Direction Works

The reverse direction works too. Apply the dictionary in reverse to an expression written in the language of $d$, and we return to the language of $\nabla$. That this bidirectional translation is free is precisely the greatest achievement of introducing $\ast$ in Chapter 6.

> <strong>Note</strong> (Which language should you think in?) The short answer: it depends on the problem. When the boundary shape is simple and the field has high symmetry, $\nabla$ notation gives better visibility. On the other hand, when coordinates are distorted or you want to keep the "type" of the field clearly separated, $d,\ast$ notation has the advantage. What matters is being able to use both languages.

> <strong>Aside</strong> (My honest opinion) In the main text I wrote that "one should use the two languages as the problem demands." That is the public line for the reader. Personally, I think in the language of $d,\ast$ whenever I can. The reason is that $\nabla$ notation is convenient for calculation, but it collapses the type differences among gradient, curl, and divergence into the same arrows and scalars. The aim of this book is not to ban vector analysis, but to bring the type conversions that go on implicitly behind it out into the open.

---

### §8.4 Translating Gauss' Theorem

Gauss' theorem from Chapter 7 §7.8.2 can likewise be translated.

$$\oiint_{\partial V} \mathbf{F} \cdot \mathbf{n}\,dS = \iiint_V (\nabla \cdot \mathbf{F})\,dV$$

The surface integral on the left can be written as $\int_{\partial V} \ast\omega$ using the $1$-form $\omega$ corresponding to $\mathbf{F}$ ($\ast\omega$ is a $2$-form and is the object of the surface integral on a closed surface).

By the dictionary, the divergence itself corresponds to the $0$-form $\ast d\ast\omega$. To integrate it over $V$, we must read this scalar as the corresponding $3$-form. Applying $\ast$ once more gives $d\ast\omega$, so the volume integral is $\int_V d\ast\omega$.

In the end, Gauss' theorem is translated into the following form.

$$\int_{\partial V} \ast\omega = \int_V d\ast\omega$$

Setting $\eta = \ast\omega$ ($2$-form),

$$\int_{\partial V} \eta = \int_V d\eta$$

This is exactly the expression of Gauss' theorem obtained in Chapter 5 §5.7 written in the language of $d$. And this formula is already consolidated in §5.9.1 as the $k=2$ case of $\int_{\partial M}\omega = \int_M d\omega$.

#### 8.4.1 Three Theorems, One Formula

The three integral theorems arranged separately in Chapter 7—Green, Stokes, and Gauss—indeed had different faces in the language of $\nabla$. But translated into the language of $d$, all become the same formula, with only the value of $k$ differing in $\int_{\partial M}\omega = \int_M d\omega$.

| $k$ | $\partial M$ | $M$ | Theorem |
|---|---|---|---|
| $0$ | $B-A$ (two points) | curve | fundamental theorem of calculus |
| $1$ | closed curve | surface | Stokes (including Green) |
| $2$ | closed surface | solid | Gauss |

$k$ is all that differs. There is no longer any reason to memorize three theorems separately. Remember only $\int_{\partial M}\omega = \int_M d\omega$, and then apply it according to the dimension of $M$.

> <strong>Checkpoint so far — §8.3–§8.4</strong>
> - Stokes' theorem in $\nabla$ notation reduces to $\int_{\partial S}\omega = \int_S d\omega$ once the dictionary is applied.
> - Gauss' theorem in $\nabla$ notation reduces to $\int_{\partial V}\eta = \int_V d\eta$ once the dictionary is applied.
> - Both are merely the same $\int_{\partial M}\omega = \int_M d\omega$ with different $k$. The three theorems are different manifestations of one formula.

---


### §8.5 Why the Two Languages Agree

In Chapter 6 §6.3.1 we introduced two ways to obtain scalars. In §8.1 we contrasted them as the world of $d$ and the world of $\nabla$. Here we do not repeat that explanation. Building on the translations seen in §8.2–§8.4, we organize why the two languages give the same values upon integration.

#### 8.5.1 The Difference Between the Two Routes

As seen in §8.1, $d$ and $\nabla$ are not doing the same thing. $d$ raises the degree of measuring devices, moving among $0$-forms, $1$-forms, $2$-forms, and $3$-forms. On the other hand, $\nabla$ produces scalar fields or column-vector fields from the same formal differential operator.

That is, in the world of $d$, the degree of the measuring device changes, and in the world of $\nabla$ "what kind of field is produced" changes. This difference is the true nature of the problem seen in Chapter 7—that "everything looks like the same arrow."

#### 8.5.2 Why They Agree

Routes ① and ② are <strong>fundamentally different</strong> in what they do. One changes the measuring-device side; the other creates new fields. The operations differ, and so do the kinds of objects that appear.

Yet they agree upon integration. For example, when line-integrating the change of a scalar field $f$, whether we use $df$ (a row-vector measuring device) or $\nabla f$ (a column-vector arrow), the result in both cases is $f(B)-f(A)$.

$$\int_C df = \int_C \nabla f \cdot d\mathbf{r} = f(B) - f(A)$$

The middle equality uses the metric identification between $df$ and $\nabla f$ discussed in §8.2.

Why? Because the metric $g$ and $\ast$ connect the two. An "arrow" like $\nabla f$ and a "measuring device" like $df$ are different types. In Cartesian coordinates $g=I$, so they look like the same components, but in general they are paired via the row/column conversion induced by $g$. Passing through this conversion is what makes the corresponding integral quantities agree.

And because $\ast\ast = \mathrm{id}$, no information is lost no matter how many times we go back and forth through the conversion. This freedom of round-trip translation is precisely the power of being able to speak both languages.

> <strong>Remark</strong> (Choosing between the two routes — my position) I go back and forth between both routes according to the problem. In highly symmetric systems I use $\nabla$ for clarity; in systems where coordinates are distorted or field types are entangled, I translate into $d,\ast$ to check type consistency. There is no need to fixate on one or the other. What matters is keeping the translation dictionary in mind.

> <strong>Checkpoint so far — §8.5</strong>
>
> | | <strong>Language of $d$</strong> | <strong>Language of $\nabla$</strong> |
> |:---|:---|:---|
> | <strong>Operation</strong> | exterior derivative $d$ | nabla $\nabla$ |
> | <strong>Change</strong> | the degree of measuring devices changes | new fields arise from the same formal differential operator |
> | <strong>Result</strong> | measuring devices such as $1$-forms, $2$-forms, $3$-forms | scalar fields and column-vector fields |
>
> What supports agreement upon integration is the translation dictionary built from the metric $g$ and $\ast$. Round-trip translation is free thanks to $\ast\ast=\mathrm{id}$.

---

### §8.6 Curvilinear Coordinates and the Two Routes

From here on is the gateway to the practical part of Chapter 9. The full computational exercises come in the next chapter, but first we confirm once that the dictionary can be built mechanically even when it leaves Cartesian coordinates.

The dictionary of §8.2 assumed Cartesian coordinates $(x,y,z)$ with $\mathbf{g}=I$. In a general coordinate system the metric $g = J^T J$ is no longer the identity matrix, and the $\ast$ dictionary changes as well. Here we use cylindrical coordinates as an example to see how the dictionary changes, and then run through the difference between the two languages organized in §8.5. We first state the three-dimensional cylindrical dictionary, then restrict to the two-dimensional polar plane for the worked divergence example.

#### 8.6.1 The Dictionary Changes with the Metric

In Chapter 6 §6.1.3 we derived the metric for cylindrical coordinates.

$$\mathbf{g} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & r^2 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

How does this $\mathbf{g} \neq I$ affect the $\ast$ dictionary? In Cartesian coordinates we had $\ast(dx) = dy \wedge dz$. Taking the basis $1$-forms of cylindrical coordinates as $(dr, d\theta, dz)$, the $\ast$ dictionary changes as follows:

$$\begin{aligned}
\ast(dr) &= r\,d\theta \wedge dz \\
\ast(d\theta) &= \frac{1}{r}\,dz \wedge dr \\
\ast(dz) &= r\,dr \wedge d\theta
\end{aligned}$$

The coefficients $r$ and $1/r$ are determined from the diagonal components $1, r^2, 1$ of $\mathbf{g} = J^T J$. The $\ast$ dictionary carries location-dependent coefficients that reflect the metric at each point.

#### 8.6.2 Trying Out the Two Routes

That the dictionary changes means the difference between the two routes contrasted in §8.1 shows up in concrete calculations. Here we actually solve the same problem by both routes. The problem is "find the divergence at a point in the plane."

> <strong>Note</strong> (Thinking in two dimensions) Since Chapter 1, whenever we treated two-dimensional problems we stated $z=0$. By now, readers who have come this far probably no longer need such a disclaimer. Below we proceed using only the plane $(x,y)$ and its polar coordinates $(r,\theta)$.

<strong>Route ①—pull back the measuring device and let the form side carry the coordinate change.</strong>

Prepare parameter space $(r,\theta)$ and physical space $(x,y)$—two sheets of Cartesian coordinate paper. On the parameter-space sheet, an identical square grid is laid out everywhere. On this square grid we perform our measurements.

A vector field $\mathbf{F}$ with components $F_x,F_y$ lives in physical space. We <strong>pull back</strong> its measuring device $\omega = F_x\,dx + F_y\,dy$ onto the parameter-space sheet. Pullback is the operation of recasting a physical-space measuring device into the language of parameter space. It goes opposite to the map $\phi: (r,\theta) \to (x,y)$ that sends into physical space—bringing the measuring device back. Using $dx = \cos\theta\,dr - r\sin\theta\,d\theta$, $dy = \sin\theta\,dr + r\cos\theta\,d\theta$,

$$\tilde{\omega} = F_r\,dr + (r F_\theta)\,d\theta$$

is obtained.

> <strong>Note</strong> (Orthonormal components and form coefficients) In vector analysis, $\mathbf{F}$ is expressed by components $(F_r, F_\theta)$ with respect to unit arrows. But the natural basis of differential forms is the coordinate differentials $(dr, d\theta)$, and the tick spacing in the $d\theta$ direction differs by a factor of $r$ from place to place. Hereafter in this section, when we write $F_\theta$ we mean the component in the orthonormal direction used in vector analysis—not the coefficient on $d\theta$ itself. When we write $\tilde{\omega} = F_r\,dr + \tilde{F}_\theta\,d\theta$, the form coefficient $\tilde{F}_\theta$ is $r F_\theta$, which differs in both dimension and value from the vector-analysis component $F_\theta$. This difference is what produces the visual gap between the formulas of Route ① and Route ②.

From here on it is the mechanical computation of $\ast d\ast$. From the polar metric $\mathbf{g} = \begin{pmatrix} 1 & 0 \\ 0 & r^2 \end{pmatrix}$, the $\ast$ dictionary becomes $\ast(dr) = r\,d\theta$, $\ast(d\theta) = -\frac{1}{r}\,dr$ (the two-dimensional version of §8.6.1). $d$ simply picks up partial-derivative coefficients as they are; the metric factors are handled by $\ast$, not inserted into $d$ by hand.

$$\begin{aligned}
\ast\tilde{\omega} &= F_r \cdot r\,d\theta + (r F_\theta) \cdot \left(-\frac{1}{r}\,dr\right) = r F_r\,d\theta - F_\theta\,dr \\[0.3em]
d\ast\tilde{\omega} &= \left(\frac{\partial}{\partial r}(r F_r) + \frac{\partial F_\theta}{\partial \theta}\right) dr \wedge d\theta \\[0.3em]
\ast d\ast\tilde{\omega} &= \frac{1}{r}\frac{\partial}{\partial r}(r F_r) + \frac{1}{r}\frac{\partial F_\theta}{\partial \theta}
\end{aligned}$$

The $\frac{1}{r}$ appeared only in the single place $\ast(dr\wedge d\theta) = \frac{1}{r}$ at the end. The $r$ and $\frac{1}{r}$ in the middle cancel—the $r$ attached to the $d\theta$ coefficient and the $\frac{1}{r}$ in $\ast(d\theta)$. $\ast$ takes on all the metric information at once, and $d$ is responsible purely for partial differentiation—this division of labor is the greatest strength of Route ①.

In parameter space we can keep thinking of the measurement grid as uniform. Differences in conversion factors from place to place are woven in by the pullback, and $\ast$ sorts them out. Limit operations can be carried out all at once at the end.

<strong>Route ②—draw the physical infinitesimal piece and count flux directly.</strong>

This time use a single sheet of graph paper in physical space. On polar coordinates $(r,\theta)$, draw a small area element centered at the point $(r,\theta)$ directly. It is a small piece with width $\Delta r$ in the $r$ direction and $\Delta\theta$ in the $\theta$ direction. Here <strong>$\Delta r$ and $\Delta\theta$ must be infinitesimal</strong>—because of the angle, a finite $\Delta\theta$ would make the radial edges non-parallel, so the piece would not be a simple rectangle.

This small piece is part of a sector. The length of the inner edge in the $\theta$ direction is $r\Delta\theta$, the outer edge is $(r+\Delta r)\Delta\theta$, and the edges grow longer as $r$ grows larger. A vector field $\mathbf{F}$ with components $F_r,F_\theta$ passes through the four sides of this piece; we account for the flux through each side one by one.

$r$ direction: from the inner edge $-F_r(r,\theta) \cdot r\Delta\theta$ flows in, from the outer edge $+F_r(r+\Delta r,\theta) \cdot (r+\Delta r)\Delta\theta$ flows out. Dividing the difference by $\Delta r$ and then by the area $r\Delta r\Delta\theta$ and taking the limit yields $\frac{1}{r}\frac{\partial}{\partial r}(rF_r)$.

$\theta$ direction: from the $\theta$ side $-F_\theta(r,\theta) \cdot \Delta r$ flows in, from the $\theta+\Delta\theta$ side $+F_\theta(r,\theta+\Delta\theta) \cdot \Delta r$ flows out. Processing similarly yields $\frac{1}{r}\frac{\partial F_\theta}{\partial\theta}$.

$$\nabla \cdot \mathbf{F} = \frac{1}{r}\frac{\partial}{\partial r}(r F_r) + \frac{1}{r}\frac{\partial F_\theta}{\partial \theta}$$

Draw the small piece directly in physical space and count the flow through the walls—the picture is intuitive. But whenever the coordinate system changes, the shape of the small piece changes and we are forced into a different accounting each time. The $\frac{1}{r}$ in $\frac{1}{r}\frac{\partial}{\partial r}(rF_r)$ appears because we divide by the sector area $r\Delta r\Delta\theta$, but this term did not appear when we did the same calculation in Cartesian coordinates.

<strong>Neither is superior</strong>

Route ① measures on a uniform square grid; Route ② draws a sector piece and counts flow. What they do is completely different. Yet the answer is the same: $\frac{1}{r}\frac{\partial}{\partial r}(rF_r) + \frac{1}{r}\frac{\partial F_\theta}{\partial\theta}$. And this agreement is not limited to divergence. Gradient, curl, and Laplacian—all differential operators can be built by these two routes. For a simple coordinate change, Route ② may be faster, but when the coordinate system is distorted or the types of fields become intertwined, switch to Route ①.

#### 8.6.3 Divergence and Curl in Curvilinear Coordinates

Combining the dictionary of §8.6.1 with Route ① of §8.6.2, the formulas for divergence and curl in cylindrical coordinates can be derived mechanically. Here $F_r,F_\theta,F_z$ are the orthonormal components in cylindrical coordinates. We show only the results.

$$\nabla \cdot \mathbf{F} = \frac{1}{r}\frac{\partial}{\partial r}(r F_r) + \frac{1}{r}\frac{\partial F_\theta}{\partial \theta} + \frac{\partial F_z}{\partial z}$$

$$\nabla \times \mathbf{F} = \begin{pmatrix}
\frac{1}{r}\frac{\partial F_z}{\partial \theta} - \frac{\partial F_\theta}{\partial z} \\[0.3em]
\frac{\partial F_r}{\partial z} - \frac{\partial F_z}{\partial r} \\[0.3em]
\frac{1}{r}\frac{\partial}{\partial r}(r F_\theta) - \frac{1}{r}\frac{\partial F_r}{\partial \theta}
\end{pmatrix}$$

Memorizing these formulas is exhausting. But if we think in terms of the combination of $d$ and $\ast$ in $\ast d\ast\omega$, we can derive the $\ast$ dictionary on the spot from $g = J^T J$ and compute mechanically. In Chapter 9 we put this technique of "building the dictionary on the spot" into practice.

> <strong>Checkpoint so far — Chapter 8 as a whole</strong>
> - $d$ and $\nabla$ stand on fundamentally different worldviews, but they agree in integration. $d$ changes the degree of measuring devices; $\nabla$ builds scalar fields and column vector fields from the same formal differential operator.
> - Through the dictionary $\nabla f \leftrightarrow df$, $\nabla\times\mathbf{F} \leftrightarrow \ast d\omega$, $\nabla\cdot\mathbf{F} \leftrightarrow \ast d\ast\omega$, the two can be translated freely.
> - With the single formula $\int_{\partial M}\omega = \int_M d\omega$, we can unify the fundamental theorem of calculus, Stokes, and Gauss.
> - The $\ast$ dictionary depends on the metric $g = J^T J$; in curvilinear coordinates, coefficients such as $r$ and $1/r$ appear.
> - What matters is not clinging to one language but using the two languages as the problem demands. You already have the dictionary for that. In Chapter 9 we build this dictionary on the spot and apply it to real problems.

# Chapter 9: In Practice — Build the Dictionary and Solve Hard Problems

# Chapter 9: In Practice — Build the Dictionary and Solve Hard Problems

### §9.0 The Central Tools of This Book Are Now in Place

In Chapter 8 §8.0 we called that chapter the highlight of the book, and there we translated between the two languages, unified the integral theorems, and contrasted the two routes. The central tools of this book are now largely in place.

But it would be a waste to assemble all these tools and never use them. In this chapter we apply the dictionary built so far to actual problems and show how to solve hard problems in vector analysis mechanically. Theory is sufficient through Chapter 8—what follows is <strong>exercise</strong>.

The reader may simply watch the calculations below—or follow along by hand. Either way, what we show here is a demonstration of the fact that you need not memorize formulas; if you have the dictionary, everything can be derived.

> <strong>Note</strong> (for readers who have not studied vector analysis) Among the calculations below, every derivation of grad, div, and curl takes only a few lines. Substitute the dictionary into $d$, $\ast d$, or $\ast d\ast$ as appropriate, and expand the partial derivatives—that is all. That is why it looks easy. But if you try to derive the same results in the style of vector analysis, you are forced through pages of manipulation while manually attaching factors such as $\frac{1}{r}\frac{\partial}{\partial r}(r\,\cdot\,)$ and $\frac{1}{\rho^2\sin\theta}$ to the $\nabla$ formulas. It looks easy because $\ast$ automatically organizes measuring devices of different degrees. The Laplacian in §9.4 is admittedly tough, but even there all you do is consult the dictionary and expand partial derivatives—the method does not change. This difference is exactly the value of the "measuring device" framework that this book has built up from Chapter 1.


### §9.2 Cylindrical Coordinates $(r,\theta,z)$

#### 9.2.1 Deriving the Dictionary

The coordinate transformation to cylindrical coordinates is $x = r\cos\theta$, $y = r\sin\theta$, $z = z$.

> <strong>Note</strong> (Domain and singular points)
> Below we compute on the coordinate patch where $r > 0$. At $r = 0$, $\theta$ is not defined and cylindrical coordinates themselves become singular. Also, since $\theta$ is an angular coordinate with period $2\pi$, strictly speaking it should be treated as a local coordinate (for example $0 < \theta < 2\pi$). The formulas in this section are intended for use in regions that do not include this singular axis.

$$J = \begin{pmatrix}
\cos\theta & -r\sin\theta & 0 \\
\sin\theta & r\cos\theta & 0 \\
0 & 0 & 1
\end{pmatrix}, \qquad
\mathbf{g} = J^T J = \begin{pmatrix}
1 & 0 & 0 \\
0 & r^2 & 0 \\
0 & 0 & 1
\end{pmatrix}$$

From $\mathbf{g}$ we derive the $\ast$ dictionary. By the same principle as the $\ast$ dictionary in Cartesian coordinates seen in Chapter 6, the square roots of the diagonal components of $\mathbf{g}$ appear as coefficients in $\ast$.

$$\begin{aligned}
\ast(dr) &= r\,d\theta \wedge dz \\
\ast(d\theta) &= \frac{1}{r}\,dz \wedge dr \\
\ast(dz) &= r\,dr \wedge d\theta
\end{aligned}$$

Also $\ast(1) = r\,dr\wedge d\theta\wedge dz$, $\ast(dr\wedge d\theta\wedge dz) = 1/r$.

> <strong>Note</strong> (Four things to distinguish in cylindrical coordinates)
> To treat vector fields correctly as differential forms, let us distinguish the following four layers:
>
> | Name | Concrete example in cylindrical coordinates |
> | :--- | :--- |
> | <strong>Coordinate $1$-forms</strong> | $dr, d\theta, dz$ |
> | <strong>$1$-forms corresponding to unit-length ticks</strong> | $dr, r\,d\theta, dz$ |
> | <strong>Components used in vector analysis</strong> | $F_r, F_\theta, F_z$ |
> | <strong>Coefficients as $1$-forms</strong> | $F_r, rF_\theta, F_z$ |
>
> If we write the components in the unit-vector directions used in vector analysis as $F_r,F_\theta,F_z$, the corresponding $1$-form is $F_r dr + F_\theta (r d\theta) + F_z dz$—that is, the coefficients as $1$-forms are $F_r,rF_\theta,F_z$. Throughout this chapter, $F_\theta$ always refers to the "components used in vector analysis."

#### 9.2.2 Gradient

$\mathrm{grad}\,f = df$ does not use $\ast$. It simply places the partial-derivative coefficients on the basis $1$-forms.

$$df = \frac{\partial f}{\partial r}\,dr + \frac{\partial f}{\partial \theta}\,d\theta + \frac{\partial f}{\partial z}\,dz$$

In the notation of vector analysis (as a column vector),

$$
\nabla f
=
\begin{pmatrix}
\frac{\partial f}{\partial r}\\[0.4em]
\frac{1}{r}\frac{\partial f}{\partial \theta}\\[0.4em]
\frac{\partial f}{\partial z}
\end{pmatrix}
$$

The factor $\frac{1}{r}$ on the $\theta$ component appears because $\nabla f$ gives components with respect to an orthonormal basis. The coefficient of $d\theta$ in $df$, namely $\frac{\partial f}{\partial\theta}$, is the "rate of change per unit angle," whereas the $\mathbf{e}_\theta$ component of $\nabla f$ is the "rate of change per unit length." The conversion $\frac{1}{r}$ is needed because $d\theta$ corresponds to arc length $r\,d\theta$.

#### 9.2.3 Divergence

For a vector field $\mathbf{F}$ with orthonormal components $F_r,F_\theta,F_z$, the corresponding $1$-form is $\omega = F_r\,dr + rF_\theta\,d\theta + F_z\,dz$, following the convention that we always write the scale factors explicitly in the $1$-form coefficients.

> <strong>Note</strong> (About the tilde on $\tilde{\omega}$)
> In Chapter 8 §8.6.2, we used the notation $\tilde{\omega}$ to distinguish the orthonormal component $F_\theta$ from the coefficient as a $1$-form, $rF_\theta$. In this chapter we lighten the notation and write $\omega$ without a tilde below. However, $F_r,F_\theta,F_z$ always denote orthonormal vector components. The corresponding $1$-form is made explicit on each occasion by including the scale factors. In cylindrical coordinates,
> $$
> \omega = F_r\,dr + rF_\theta\,d\theta + F_z\,dz
> $$
> and in spherical coordinates,
> $$
> \omega = F_\rho\,d\rho + \rho F_\theta\,d\theta + \rho\sin\theta\,F_\phi\,d\phi
> $$
> Read with the convention that the coefficients as $1$-forms are made explicit through the scale factors appearing in the formulas—not inferred by the reader from context.

$$\begin{aligned}
\ast\omega &= F_r(r\,d\theta\wedge dz) + rF_\theta\!\left(\frac{1}{r}\,dz\wedge dr\right) + F_z(r\,dr\wedge d\theta) \\
&= rF_r\,d\theta\wedge dz + F_\theta\,dz\wedge dr + rF_z\,dr\wedge d\theta \\[0.3em]
d\ast\omega &= \left(\frac{\partial}{\partial r}(rF_r) + \frac{\partial F_\theta}{\partial\theta} + \frac{\partial}{\partial z}(rF_z)\right) dr\wedge d\theta\wedge dz \\[0.3em]
\ast d\ast\omega &= \frac{1}{r}\frac{\partial}{\partial r}(rF_r) + \frac{1}{r}\frac{\partial F_\theta}{\partial\theta} + \frac{\partial F_z}{\partial z}
\end{aligned}$$

This is the formula for divergence in cylindrical coordinates.

#### 9.2.4 Curl

Curl is $\mathrm{curl}\,\mathbf{F} \leftrightarrow \ast d\omega$.

$$d\omega = \left(\frac{\partial}{\partial r}(rF_\theta) - \frac{\partial F_r}{\partial\theta}\right) dr\wedge d\theta + \left(\frac{\partial F_z}{\partial\theta} - \frac{\partial}{\partial z}(rF_\theta)\right) d\theta\wedge dz + \left(\frac{\partial F_r}{\partial z} - \frac{\partial F_z}{\partial r}\right) dz\wedge dr$$

$$\ast d\omega = \frac{1}{r}\!\left(\frac{\partial F_z}{\partial\theta} - \frac{\partial}{\partial z}(rF_\theta)\right)\! dr + r\!\left(\frac{\partial F_r}{\partial z} - \frac{\partial F_z}{\partial r}\right)\! d\theta + \frac{1}{r}\!\left(\frac{\partial}{\partial r}(rF_\theta) - \frac{\partial F_r}{\partial\theta}\right)\! dz$$

Reading off the coefficients of $dr, d\theta, dz$ from the $1$-form and converting back to orthonormal components, the coefficient of $d\theta$ is divided by the scale factor $r$. In the end,

$$\nabla \times \mathbf{F} = \begin{pmatrix}
\frac{1}{r}\frac{\partial F_z}{\partial \theta} - \frac{\partial F_\theta}{\partial z} \\[0.3em]
\frac{\partial F_r}{\partial z} - \frac{\partial F_z}{\partial r} \\[0.3em]
\frac{1}{r}\frac{\partial}{\partial r}(r F_\theta) - \frac{1}{r}\frac{\partial F_r}{\partial \theta}
\end{pmatrix}$$

The structure in which $r$ appears both inside and outside $\frac{\partial}{\partial r}$ has exactly the same origin as the $\frac{1}{r}$ that appeared when we counted the area element of a sector in the previous chapter.

---

### §9.3 Spherical Coordinates $(\rho,\theta,\phi)$

#### 9.3.1 Deriving the Dictionary

The conversion to spherical coordinates is $x = \rho\sin\theta\cos\phi$, $y = \rho\sin\theta\sin\phi$, $z = \rho\cos\theta$ ($\theta$ is the angle from the $z$-axis, $\phi$ is the azimuthal angle in the $xy$ plane).

$$J = \begin{pmatrix}
\sin\theta\cos\phi & \rho\cos\theta\cos\phi & -\rho\sin\theta\sin\phi \\
\sin\theta\sin\phi & \rho\cos\theta\sin\phi & \rho\sin\theta\cos\phi \\
\cos\theta & -\rho\sin\theta & 0
\end{pmatrix},\qquad
\mathbf{g} = J^T J = \begin{pmatrix}
1 & 0 & 0 \\
0 & \rho^2 & 0 \\
0 & 0 & \rho^2\sin^2\theta
\end{pmatrix}$$

The scale factors $1, \rho, \rho\sin\theta$ derived from the diagonal metric components determine the coefficients in the $\ast$ dictionary.

$$\begin{aligned}
\ast(d\rho) &= \rho^2\sin\theta\; d\theta \wedge d\phi \\
\ast(d\theta) &= \sin\theta\; d\phi \wedge d\rho \\
\ast(d\phi) &= \frac{1}{\sin\theta}\; d\rho \wedge d\theta
\end{aligned}$$

> <strong>Note</strong> (Four things to distinguish in spherical coordinates)
>
> | Name | Concrete example in spherical coordinates |
> | :--- | :--- |
> | <strong>Coordinate $1$-forms</strong> | $d\rho, d\theta, d\phi$ |
> | <strong>$1$-forms for unit-length scales</strong> | $d\rho, \rho\,d\theta, \rho\sin\theta\,d\phi$ |
> | <strong>Components used in vector analysis</strong> | $F_\rho, F_\theta, F_\phi$ |
> | <strong>Coefficients as $1$-forms</strong> | $F_\rho, \rho F_\theta, \rho\sin\theta F_\phi$ |
>
> The $1$-form for orthonormal components $F_\rho,F_\theta,F_\phi$ is $\omega = F_\rho d\rho + \rho F_\theta d\theta + \rho\sin\theta F_\phi d\phi$.

Here we compute on the coordinate patch $\rho>0$ and $0<\theta<\pi$. At the origin $\rho=0$ and on the polar axis $\sin\theta=0$, spherical coordinates themselves become singular, and formulas containing $1/\rho$ or $1/\sin\theta$ cannot be used as written. For problems spanning singular points, use a different coordinate patch, or compute in a region excluding the singularities and then treat them via boundary conditions.

#### 9.3.2 Divergence

When converting a vector field $\mathbf{F}$ with orthonormal components $F_\rho,F_\theta,F_\phi$ to a $1$-form, the coefficient of $d\rho$ is $F_\rho$ ($\rho$ already carries length), the coefficient of $d\theta$ is $\rho F_\theta$, and the coefficient of $d\phi$ is $\rho\sin\theta\,F_\phi$ (corresponding respectively to arc lengths $\rho\,d\theta$, $\rho\sin\theta\,d\phi$).

$$\omega = F_\rho\,d\rho + \rho F_\theta\,d\theta + \rho\sin\theta\,F_\phi\,d\phi$$

Compute $\ast d\ast\omega$.

$$\ast\omega = \rho^2\sin\theta\,F_\rho\,d\theta\wedge d\phi + \rho\sin\theta\,F_\theta\,d\phi\wedge d\rho + \rho\,F_\phi\,d\rho\wedge d\theta$$

$$d\ast\omega = \left(\frac{\partial}{\partial\rho}(\rho^2\sin\theta\,F_\rho) + \frac{\partial}{\partial\theta}(\rho\sin\theta\,F_\theta) + \frac{\partial}{\partial\phi}(\rho\,F_\phi)\right) d\rho\wedge d\theta\wedge d\phi$$

From $\ast(d\rho\wedge d\theta\wedge d\phi) = 1/(\rho^2\sin\theta)$,

$$\nabla \cdot \mathbf{F} = \frac{1}{\rho^2}\frac{\partial}{\partial\rho}(\rho^2 F_\rho) + \frac{1}{\rho\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,F_\theta) + \frac{1}{\rho\sin\theta}\frac{\partial F_\phi}{\partial\phi}$$

#### 9.3.3 Curl

Similarly, from $\ast d\omega$,

$$\nabla \times \mathbf{F} = \begin{pmatrix}
\frac{1}{\rho\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,F_\phi) - \frac{1}{\rho\sin\theta}\frac{\partial F_\theta}{\partial\phi} \\[0.3em]
\frac{1}{\rho\sin\theta}\frac{\partial F_\rho}{\partial\phi} - \frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho F_\phi) \\[0.3em]
\frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho F_\theta) - \frac{1}{\rho}\frac{\partial F_\rho}{\partial\theta}
\end{pmatrix}$$

---

### §9.4 A Hard Problem in Calculus — The Vector Laplacian in Spherical Coordinates

The vector Laplacian $\nabla^2\mathbf{F} = \nabla(\nabla\cdot\mathbf{F}) - \nabla\times(\nabla\times\mathbf{F})$ is known as one of the longest formulas in the vector-analysis handbook. Here we show that every component falls out mechanically from the dictionary.

The strategy is simply to use the Chapter 8 dictionary as is.
- $\nabla(\nabla\cdot\mathbf{F}) \leftrightarrow d(\ast d\ast\omega)$
- $\nabla\times(\nabla\times\mathbf{F}) \leftrightarrow \ast d(\ast d\omega)$

Therefore, viewing the result as a $1$-form,

$$\nabla^2\mathbf{F} \leftrightarrow d\bigl(\ast d\ast\omega\bigr)-\ast d\bigl(\ast d\omega\bigr)$$

Starting from $\omega = F_\rho\,d\rho + \rho F_\theta\,d\theta + \rho\sin\theta\,F_\phi\,d\phi$ in spherical coordinates, we compute $d\ast d\ast\omega$ and $\ast d\ast d\omega$ separately and take their difference.

#### 9.4.1 The First Term — Gradient of the Divergence

From §9.3.2, the divergence is

$$\ast d\ast\omega = \frac{1}{\rho^2}\frac{\partial}{\partial\rho}(\rho^2 F_\rho) + \frac{1}{\rho\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,F_\theta) + \frac{1}{\rho\sin\theta}\frac{\partial F_\phi}{\partial\phi}$$

Denote this by $S$. Since $S$ is a scalar field, its gradient is $dS = \frac{\partial S}{\partial\rho}\,d\rho + \frac{\partial S}{\partial\theta}\,d\theta + \frac{\partial S}{\partial\phi}\,d\phi$. Converting to orthonormal components,

$$\nabla(\nabla\cdot\mathbf{F}) = \begin{pmatrix}
\frac{\partial S}{\partial\rho} \\[0.5em]
\frac{1}{\rho}\frac{\partial S}{\partial\theta} \\[0.5em]
\frac{1}{\rho\sin\theta}\frac{\partial S}{\partial\phi}
\end{pmatrix}$$

#### 9.4.2 The Second Term — Curl of the Curl

Write the curl from §9.3.3 as $C_\rho, C_\theta, C_\phi$.

$$\begin{aligned}
C_\rho &= \frac{1}{\rho\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,F_\phi) - \frac{1}{\rho\sin\theta}\frac{\partial F_\theta}{\partial\phi} \\[0.3em]
C_\theta &= \frac{1}{\rho\sin\theta}\frac{\partial F_\rho}{\partial\phi} - \frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho F_\phi) \\[0.3em]
C_\phi &= \frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho F_\theta) - \frac{1}{\rho}\frac{\partial F_\rho}{\partial\theta}
\end{aligned}$$

To apply $\nabla\times$ again to $\mathbf{C} = \nabla\times\mathbf{F}$, substitute $C_\rho, C_\theta, C_\phi$ into the formula of §9.3.3 in place of $F_\rho, F_\theta, F_\phi$.

$$\begin{aligned}
(\nabla\times(\nabla\times\mathbf{F}))_\rho &= \frac{1}{\rho\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,C_\phi) - \frac{1}{\rho\sin\theta}\frac{\partial C_\theta}{\partial\phi} \\[0.5em]
(\nabla\times(\nabla\times\mathbf{F}))_\theta &= \frac{1}{\rho\sin\theta}\frac{\partial C_\rho}{\partial\phi} - \frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho C_\phi) \\[0.5em]
(\nabla\times(\nabla\times\mathbf{F}))_\phi &= \frac{1}{\rho}\frac{\partial}{\partial\rho}(\rho C_\theta) - \frac{1}{\rho}\frac{\partial C_\rho}{\partial\theta}
\end{aligned}$$

#### 9.4.3 Take the Difference — The Vector Laplacian

Since $\nabla^2\mathbf{F} = \nabla(\nabla\cdot\mathbf{F}) - \nabla\times(\nabla\times\mathbf{F})$, each component is obtained by subtracting the second term from the first. Expand the $\rho$ component.

$$(\nabla^2\mathbf{F})_\rho = \frac{\partial S}{\partial\rho} - \frac{1}{\rho\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,C_\phi) + \frac{1}{\rho\sin\theta}\frac{\partial C_\theta}{\partial\phi}$$

Substituting the expressions for $S$ and $C_\theta, C_\phi$, expanding partial derivatives, and collecting terms yields the following. The expansion is long, so here we show only the result after substitution and like-term collection.

$$(\nabla^2\mathbf{F})_\rho = \nabla^2 F_\rho - \frac{2F_\rho}{\rho^2} - \frac{2}{\rho^2\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,F_\theta) - \frac{2}{\rho^2\sin\theta}\frac{\partial F_\phi}{\partial\phi}$$

Here $\nabla^2 F_\rho$ denotes the scalar Laplacian applied to the scalar component $F_\rho$:

$$\nabla^2 F_\rho = \frac{1}{\rho^2}\frac{\partial}{\partial\rho}\!\left(\rho^2\frac{\partial F_\rho}{\partial\rho}\right) + \frac{1}{\rho^2\sin\theta}\frac{\partial}{\partial\theta}\!\left(\sin\theta\frac{\partial F_\rho}{\partial\theta}\right) + \frac{1}{\rho^2\sin^2\theta}\frac{\partial^2 F_\rho}{\partial\phi^2}$$

Similarly, for the $\theta$ and $\phi$ components,

$$(\nabla^2\mathbf{F})_\theta = \nabla^2 F_\theta - \frac{F_\theta}{\rho^2\sin^2\theta} + \frac{2}{\rho^2}\frac{\partial F_\rho}{\partial\theta} - \frac{2\cos\theta}{\rho^2\sin^2\theta}\frac{\partial F_\phi}{\partial\phi}$$

$$(\nabla^2\mathbf{F})_\phi = \nabla^2 F_\phi - \frac{F_\phi}{\rho^2\sin^2\theta} + \frac{2}{\rho^2\sin\theta}\frac{\partial F_\rho}{\partial\phi} + \frac{2\cos\theta}{\rho^2\sin^2\theta}\frac{\partial F_\theta}{\partial\phi}$$

This completes the derivation of all components. Deriving from scratch in the usual vector-analysis style would easily exceed a page of computation, but via the dictionary each step is nothing more than partial differentiation and multiplication by coefficients. There is no need to memorize individual formulas by rote—given the single identity $d(\ast d\ast\omega)-\ast d(\ast d\omega)$ and the $\ast$ dictionary of §9.3, everything can be reconstructed on the spot.

---

### §9.5 A Hard Problem in Electromagnetism — Divergence of the Point-Charge Electric Field

Finally, one example from electromagnetism. It also serves as a bridge to Chapter 10.

> <strong>Note</strong> (For readers who have not studied electromagnetism) The terms "electric field" and "point charge" below need not be fully understood. Please read them simply as the calculation of "a vector field proportional to $\frac{1}{\rho^2}$." Chapter 10 does not dig deeply into electromagnetism itself either. It only shows that Maxwell's equations become terrifyingly concise when written in differential forms—and that we will actually write out in full what happens when one drops them all the way down to matrices, even though most textbooks stop at saying how beautiful they are.

When a point charge $q$ sits at the origin, the electric field is $\mathbf{E} = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\boldsymbol{\rho}}}{\rho^2}$ ($\hat{\boldsymbol{\rho}}$ is the radial unit vector). In vector analysis one shows $\nabla\cdot\mathbf{E} = 0$ (away from the origin) by plugging into the spherical divergence formula, but it is clearer to work directly with the $1$-form corresponding to $\mathbf{E}$.

The $\rho$ component of $\mathbf{E}$ is $E_\rho = \frac{k}{\rho^2}$ ($k = q/4\pi\varepsilon_0$); the $\theta$ and $\phi$ components are zero. The corresponding $1$-form is

$$\omega = \frac{k}{\rho^2}\,d\rho$$

Compute $d\ast\omega$. In spherical coordinates $\ast(d\rho) = \rho^2\sin\theta\,d\theta\wedge d\phi$ (§9.3.1), so

$$\ast\omega = \frac{k}{\rho^2} \cdot \rho^2\sin\theta\,d\theta\wedge d\phi = k\sin\theta\,d\theta\wedge d\phi$$

$$d\ast\omega = \frac{\partial}{\partial\rho}(k\sin\theta)\,d\rho\wedge d\theta\wedge d\phi + \frac{\partial}{\partial\theta}(k\sin\theta)\,d\theta\wedge d\theta\wedge d\phi + \cdots$$

The second term vanishes because $d\theta\wedge d\theta = 0$; the third term likewise. The first term has $\frac{\partial}{\partial\rho}(k\sin\theta) = 0$ (no dependence on $\rho$). Therefore

$$d\ast\omega = 0 \quad (\rho \neq 0)$$

So $\ast d\ast\omega = 0$, which corresponds to $\nabla\cdot\mathbf{E}=0$ away from the origin. The $\rho^2$ in $E_\rho$ cancels the $\rho^2$ in $\ast(d\rho)$, and the exterior derivative of the remaining $\sin\theta\,d\theta\wedge d\phi$ is zero—that alone shows zero divergence away from the origin.

> <strong>Note</strong> (What about the origin?) At $\rho = 0$, $\omega$ is not defined. To treat all of space including the origin, one must represent the point charge by distributions ($\delta$ functions) or in integral form rather than by ordinary divergence as a function. This book does not go there; we restrict ourselves to computation on the region excluding the origin. In Chapter 10, where charge density is treated, we write charge density as $\rho_{\mathrm e}$ so as not to confuse it with the radial coordinate $\rho$, and handle the form in which $\rho_{\mathrm e}/\varepsilon_0$ appears on the right-hand side.

---

### §9.6 The Dictionary Ends; the Journey Continues

In this chapter we used the dictionary built through Chapter 8 to derive vector-analysis formulas mechanically and to solve hard problems from calculus and electromagnetism. What matters is that every calculation required not "recalling a formula" but only "looking up the dictionary and tracing the procedure."

There is no longer any need to memorize the divergence and curl formulas for cylindrical or spherical coordinates by rote. Remember this single path: $J \to g = J^T J \to \ast$ dictionary $\to$ combinations of $d$ and $\ast$—and you can reconstruct the formulas for orthogonal curvilinear coordinates on the spot. The same principle holds for non-orthogonal coordinates, but note that the $\ast$ dictionary then acquires mixed terms from the off-diagonal metric, so the tables in this chapter with scale factors alone no longer suffice.

In Chapter 10 we apply this toolkit to Maxwell's equations.
The four fundamental equations of vector analysis collapse to two in differential-form language. Many textbooks stop here with "how beautiful," but we go further. We write Maxwell's equations in differential forms and actually carry out the full component expansion—showing what it looks like when done. Having worked through the calculations of this chapter, that translation should no longer be difficult.

> <strong>Checkpoint — Chapter 9 as a whole</strong>
> - Deriving formulas in orthogonal curvilinear coordinates proceeds by $J \to g = J^T J \to \ast$ dictionary $\to$ combinations of $d$ and $\ast$.
> - We derived the $\ast$ dictionary and the divergence and curl formulas in cylindrical and spherical coordinates.
> - Even hard problems such as the vector Laplacian $\nabla^2\mathbf{F}$ can be solved mechanically by combining the dictionary with identities.
> - Zero divergence of the point-charge electric field follows from the simple cancellation of $\ast(d\rho)$ with the $\rho^2$ in $E_\rho$.
> - Formulas need not be memorized by rote. Given the dictionary—and even that dictionary can be reconstructed on the spot—everything can be rebuilt when needed.

# Chapter 10: Maxwell's Equations — Beyond Beauty

# Chapter 10: Maxwell's Equations — Beyond Beauty

### §10.0 The Usual Caveat

Well, the end of this book is finally in sight. Apparently it is conventional for textbooks on the physical mathematics of differential forms to close by rewriting Maxwell's equations in differential forms. The author will follow this custom as well.

However, one caveat. This book is not an electromagnetism textbook. If you know electromagnetism you can enjoy the physical interpretation, but we will write so that even without that background you can follow the component calculations. Here, six functions $E_x, E_y, E_z, B_x, B_y, B_z$ appear; they fit into a certain antisymmetric matrix, and when $d$ and $\ast$ act on it, the famous formulas of vector analysis emerge—we ask you to view this flow purely as algebraic manipulation.

> <strong>Note</strong> (for readers who have not studied electromagnetism) All physical terminology in this chapter may be skipped. All you need is to see "what happens when you arrange six functions in a $4\times4$ matrix and apply $d$ and $\ast$." Even without knowledge of electromagnetism, readers who have made it this far should be able to enjoy the chapter by following the matrix components alone.

> <strong>Note</strong> (the role of this chapter) The core of this book is complete by Chapter 9. This chapter is, so to speak, a bonus, or nearly a digression. Do not take it too seriously; read it at your leisure.


### §10.2 The Electromagnetic Field $F$ and Fixing Sign Conventions

Before writing the electromagnetic field $F$ in explicit components, let us rigorously fix the sign conventions for spacetime used in this chapter. There are several traditions for sign choices, but this book adopts the following set.

- <strong>Coordinate order</strong>: $(x^0, x^1, x^2, x^3) = (t, x, y, z)$
- <strong>Time coordinate</strong>: $t = ct_{\text{SI}}$ (normalized to length dimension)
- <strong>Magnetic field</strong>: $\mathbf{B} = c\mathbf{B}_{\text{SI}}$ (quantity aligned in dimension with the electric field)
- <strong>Orientation (reference $4$-form)</strong>: $dt \wedge dx \wedge dy \wedge dz$
- <strong>Metric signature</strong>: $(-, +, +, +)$
- <strong>Matrix representation of $2$-forms</strong>: Following Chapter 2's convention, place the coefficients of basis $dx^\mu \wedge dx^\nu$ in the matrix $(\mu, \nu)$ components.

Under this convention, define the electromagnetic field $2$-form $F$ as follows.

$$
F = -E_x\,dt\wedge dx - E_y\,dt\wedge dy - E_z\,dt\wedge dz + B_x\,dy\wedge dz + B_y\,dz\wedge dx + B_z\,dx\wedge dy
$$

The minus signs on the electric-field terms (those containing $dt$) are an intentional choice to maintain consistency with Faraday's law $\mathrm{curl}\,\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}$ and the potential construction $F = -d\mathcal{A}$ described later.

In a $4\times4$ antisymmetric matrix, this becomes

$$F = \begin{pmatrix}
0 & -E_x & -E_y & -E_z \\
E_x & 0 & B_z & -B_y \\
E_y & -B_z & 0 & B_x \\
E_z & B_y & -B_x & 0
\end{pmatrix}$$

> <strong>Note</strong> (sign of electric-field terms and matrix)
> In this book's matrix convention, the coefficient $-E_x$ of $dt \wedge dx$ is placed in the matrix component $(t,x)$. Therefore $F_{tx}=-E_x,\;F_{xt}=E_x$. Many textbooks define $F_{t x}$ as positive $E_x$, but then one must either use $F = E_x dx \wedge dt + \dots$ (reversed order) or adjust the sign in the potential definition $F=d\mathcal{A}$. This book prioritizes $F=-d\mathcal{A}$ and the order $dt \wedge dx$, and adopts this sign.

---

### §10.3 The Minkowski Metric — From $\mathbb{R}^3$ to Four Dimensions

Throughout this book we have consistently worked on $\mathbb{R}^3$ with Cartesian coordinates $(x,y,z)$. However, to treat $F$ we need four-dimensional spacetime $(t,x,y,z)$ with time $t$ adjoined.

Fortunately, with the knowledge accumulated so far, the extension is easy. In Chapter 6 we derived $\mathbf{g} = J^T J$, and in Chapter 9 we practiced the procedure of building the $\ast$ dictionary from $\mathbf{g}$. We need only do the same in spacetime. The metric is as follows (the only new element is that the sign of the time component differs from that of the spatial components):

$$\mathbf{g} = \begin{pmatrix}
-1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

> <strong>Note</strong> (Departure from positive definiteness) The metrics in this book have always been positive definite ($\mathbf{v}^T\mathbf{g}\,\mathbf{v} > 0$ for $\mathbf{v}\neq\mathbf{0}$). The Minkowski metric is not positive definite and differs from the $\mathbf{g}=J^T J$ type of metric used until now. Here we inherit only the procedure of "building the $\ast$ dictionary from the metric matrix." This difference appears as sign changes in the $\ast$ dictionary, but the computational procedure itself does not change. This point will be foreshadowing when we look at manifolds and metrics in the next chapter.

> <strong>Note</strong> (Convention for the four-dimensional Hodge star)
> In this chapter we take the orientation (order of basis elements) to be $dt\wedge dx\wedge dy\wedge dz$ and the spacetime metric signature to be $(-,+,+,+)$. Under this convention we use the following $\ast F$ and $\ast\mathcal{J}$. When writing Maxwell's equations symbolically we still write $\ast$ as usual, but in component calculations we distinguish the Hodge star on four-dimensional spacetime as $\ast_4$ and the Hodge star on three-dimensional space as $\ast_3$. With different signatures or orientation conventions, note that several signs will flip.

---


### §10.4 Writing Out $dF=0$ in Full

Since $F$ is a $2$-form, $dF$ is a $3$-form. In the component calculations from here on, we write $d_4F$ to make explicit that the exterior derivative is on four-dimensional spacetime. A $3$-form in four dimensions has four independent components. Apply $d_4$ to the $F$ redefined in §10.2 (with the minus sign on the electric-field terms) and collect the coefficients on the same basis $3$-forms.

$$F = -E_x\,dt\wedge dx - E_y\,dt\wedge dy - E_z\,dt\wedge dz + B_x\,dy\wedge dz + B_y\,dz\wedge dx + B_z\,dx\wedge dy$$

Apply $d_4$ to each term. The electric-field terms become (note the sign changes):

$$\begin{aligned}
d_4\!\left(-E_x\,dt\wedge dx\right) &= -\frac{\partial E_x}{\partial y}\,dy\wedge dt\wedge dx - \frac{\partial E_x}{\partial z}\,dz\wedge dt\wedge dx \\
&= -\frac{\partial E_x}{\partial y}\,dt\wedge dx\wedge dy + \frac{\partial E_x}{\partial z}\,dt\wedge dz\wedge dx \\
d_4\!\left(-E_y\,dt\wedge dy\right) &= -\frac{\partial E_y}{\partial z}\,dt\wedge dy\wedge dz + \frac{\partial E_y}{\partial x}\,dt\wedge dx\wedge dy \\
d_4\!\left(-E_z\,dt\wedge dz\right) &= -\frac{\partial E_z}{\partial x}\,dt\wedge dz\wedge dx + \frac{\partial E_z}{\partial y}\,dt\wedge dy\wedge dz
\end{aligned}$$

The magnetic-field terms also include time derivatives and become:

$$\begin{aligned}
d_4(B_x\,dy\wedge dz) &= \frac{\partial B_x}{\partial t}\,dt\wedge dy\wedge dz + \frac{\partial B_x}{\partial x}\,dx\wedge dy\wedge dz \\
d_4(B_y\,dz\wedge dx) &= \frac{\partial B_y}{\partial t}\,dt\wedge dz\wedge dx + \frac{\partial B_y}{\partial y}\,dy\wedge dz\wedge dx \\
d_4(B_z\,dx\wedge dy) &= \frac{\partial B_z}{\partial t}\,dt\wedge dx\wedge dy + \frac{\partial B_z}{\partial z}\,dz\wedge dx\wedge dy
\end{aligned}$$

Summing all of these and organizing by basis $3$-form, for example the coefficient of $dt\wedge dy\wedge dz$ becomes:

$$
\left(\frac{\partial B_x}{\partial t} + \frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z}\right) dt\wedge dy\wedge dz = \left(\frac{\partial B_x}{\partial t} + (\mathrm{curl}\,\mathbf{E})_x\right) dt\wedge dy\wedge dz
$$

Setting each basis coefficient to zero, the component calculation of $d_4F=0$ is equivalent to the following four equations. Symbolically, we write this as $dF=0$.

$$d_4F = 0 \Longleftrightarrow \begin{cases}
\displaystyle \frac{\partial B_x}{\partial x} + \frac{\partial B_y}{\partial y} + \frac{\partial B_z}{\partial z} = 0 & (\mathrm{div}\,\mathbf{B} = 0) \\[1em]
\displaystyle (\mathrm{curl}\,\mathbf{E})_x = -\frac{\partial B_x}{\partial t} & \\[0.5em]
\displaystyle (\mathrm{curl}\,\mathbf{E})_y = -\frac{\partial B_y}{\partial t} & (\mathrm{curl}\,\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}) \\[0.5em]
\displaystyle (\mathrm{curl}\,\mathbf{E})_z = -\frac{\partial B_z}{\partial t} &
\end{cases}$$

The first line is Gauss's law for magnetism; the second through fourth lines are Faraday's law of electromagnetic induction. By placing minus signs on the electric-field terms, the familiar vector-analysis formulas with the correct signs are derived from the single differential-form equation $dF=0$ (computationally $d_4F=0$).


---


### §10.5 $\ast F$ and the Remaining Two Equations

Let us also write out in full the other equation $d(\ast F) = \mu_0(\ast\mathcal{J})$ by the same procedure as §10.4. Symbolically we write $\ast$, but in the component calculations from here on we make explicit the Hodge star on four-dimensional spacetime and write $d_4(\ast_4F)=\mu_0(\ast_4\mathcal{J})$.

First, compute $\ast_4F$ from the $F$ redefined in §10.2. Applying the four-dimensional Hodge star under the Minkowski metric signature $(-,+,+,+)$ and orientation $dt\wedge dx\wedge dy\wedge dz$ of §10.3, $\ast_4F$ becomes:

$$
\ast_4F = B_x\,dt\wedge dx + B_y\,dt\wedge dy + B_z\,dt\wedge dz + E_x\,dy\wedge dz + E_y\,dz\wedge dx + E_z\,dx\wedge dy
$$

In matrix form:

$$\ast_4F = \begin{pmatrix}
0 & B_x & B_y & B_z \\
-B_x & 0 & E_z & -E_y \\
-B_y & -E_z & 0 & E_x \\
-B_z & E_y & -E_x & 0
\end{pmatrix}$$

Because we started from an $F$ with reversed signs on the electric terms, after the $\ast_4$ action the magnetic terms become those involving $dt$, while the electric terms move to purely spatial terms ($2$-forms).

Next, expand $d_4(\ast_4F)$. Organizing by basis $3$-form, we obtain:

$$\begin{aligned}
d_4(\ast_4F) = &\left(\frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z}\right) dx\wedge dy\wedge dz \\
{+} &\left(\frac{\partial E_x}{\partial t} - \left(\frac{\partial B_z}{\partial y} - \frac{\partial B_y}{\partial z}\right)\right) dt\wedge dy\wedge dz \\
{+} &\left(\frac{\partial E_y}{\partial t} - \left(\frac{\partial B_x}{\partial z} - \frac{\partial B_z}{\partial x}\right)\right) dt\wedge dz\wedge dx \\
{+} &\left(\frac{\partial E_z}{\partial t} - \left(\frac{\partial B_y}{\partial x} - \frac{\partial B_x}{\partial y}\right)\right) dt\wedge dx\wedge dy
\end{aligned}$$

The right-hand side $\mu_0(\ast_4\mathcal{J})$ is a $3$-form containing the charge density $\rho_{\mathrm e}$ and the current density $\mathbf{J}$. Under the normalization of §10.1 it can be written as:

$$
\mu_0(\ast_4\mathcal{J}) = \frac{\rho_{\mathrm e}}{\varepsilon_0}\,dx\wedge dy\wedge dz - \mu_0 c J_x\,dt\wedge dy\wedge dz - \mu_0 c J_y\,dt\wedge dz\wedge dx - \mu_0 c J_z\,dt\wedge dx\wedge dy
$$

Here we have not yet used $\ast_3$. Comparing both sides directly as coefficients of the four-dimensional basis $3$-forms, from the coefficient of $dx\wedge dy\wedge dz$ we first obtain

$$
\frac{\partial E_x}{\partial x}+\frac{\partial E_y}{\partial y}+\frac{\partial E_z}{\partial z}=\frac{\rho_{\mathrm e}}{\varepsilon_0}
$$

This is Gauss's law $\mathrm{div}\,\mathbf E=\rho_{\mathrm e}/\varepsilon_0$. From the remaining three basis $3$-forms we obtain

$$
\begin{aligned}
\frac{\partial E_x}{\partial t}-\left(\frac{\partial B_z}{\partial y}-\frac{\partial B_y}{\partial z}\right)&=-\mu_0 cJ_x,\\
\frac{\partial E_y}{\partial t}-\left(\frac{\partial B_x}{\partial z}-\frac{\partial B_z}{\partial x}\right)&=-\mu_0 cJ_y,\\
\frac{\partial E_z}{\partial t}-\left(\frac{\partial B_y}{\partial x}-\frac{\partial B_x}{\partial y}\right)&=-\mu_0 cJ_z
\end{aligned}
$$

Rearranging,

$$
\mathrm{curl}\,\mathbf{B} = \mu_0 c \mathbf{J} + \frac{\partial \mathbf{E}}{\partial t}
$$

Thus far, from the four-dimensional equation $d_4(\ast_4F)=\mu_0(\ast_4\mathcal{J})$, the remaining two equations have emerged as components.

The same content can also be written in compressed form as spatial three-dimensional differential forms. The $\ast_4F$ we have just obtained can be written using the spatial metric correspondence at each instant of time as

$$
\ast_4F
=
dt\wedge(\mathbf B^Tg_3)+\ast_3(\mathbf E^Tg_3).
$$

Here, in Cartesian space $g_3=I$, so

$$
\mathbf B^Tg_3
=
B_x\,dx+B_y\,dy+B_z\,dz,
$$

and

$$
\ast_3(\mathbf E^Tg_3)
=
E_x\,dy\wedge dz+E_y\,dz\wedge dx+E_z\,dx\wedge dy.
$$

> <strong>Note</strong> (why we do not use $\flat$ notation) In differential geometry, the operation of turning a vector field into the corresponding $1$-form through the metric is often denoted by a musical symbol, for example $\mathbf B^\flat$. This book deliberately avoids that notation. Since we work throughout with row vectors, column vectors, and explicit metric matrices, we write the same operation as $\mathbf B^Tg_3$. No new operation is being introduced here; this is the same metric correspondence used in Chapter 8.

Using this decomposition, the four-dimensional calculation above can be read as

$$
d_4(\ast_4F)
=
dt\wedge\left(
\frac{\partial(\ast_3(\mathbf E^Tg_3))}{\partial t}
-
d_3(\mathbf B^Tg_3)
\right)
+
d_3(\ast_3(\mathbf E^Tg_3)).
$$

The right-hand side can also be written in spatial three-dimensional notation as

$$
\mu_0(\ast_4\mathcal J)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)-\mu_0 c\,dt\wedge J
$$

Here $J=J_x\,dy\wedge dz+J_y\,dz\wedge dx+J_z\,dx\wedge dy$ is the spatial current-density $2$-form. Here $\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)$ is the spatial $3$-form corresponding to the charge density. Therefore, comparing the parts that do and do not contain $dt$, we obtain

$$
d_3(\ast_3(\mathbf E^Tg_3))=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right),
\qquad
d_3(\mathbf B^Tg_3)=\mu_0 c\,J+\frac{\partial(\ast_3(\mathbf E^Tg_3))}{\partial t}
$$

Reading these forms back through the Chapter 8 spatial dictionary, these reduce to the earlier formulas for $\mathrm{div}\,\mathbf E$ and $\mathrm{curl}\,\mathbf B$. In this way it is fully confirmed that all four Maxwell equations are derived from the two differential-form equations with the correct signs and coefficients.

In other words, the four Maxwell equations are consolidated into the two differential-form equations

$$dF = 0, \qquad d(\ast F) = \mu_0(\ast\mathcal{J})$$

When actually expanding these two equations with matrices and partial derivatives, we use $d_4$ and $\ast_4$; when returning to the spatial three-dimensional dictionary, we use $d_3$ and $\ast_3$. The familiar vector-analysis formulas are reproduced by moving back and forth between these two levels. Behind the beauty lies genuinely gritty computation—and witnessing that is the achievement of this chapter.

> <strong>Note</strong> (Why only two equations?) A sharp reader may wonder: "So in the end there are only two? Can $dF=0$ and $d(\ast F)=\mu_0(\ast\mathcal{J})$ not be combined into a <strong>single line</strong>?" They can. In Chapter 12, using a complex vector that bundles $\mathbf{E}$ and $\mathbf{B}$ together and a Dirac operator built from Pauli matrices, Maxwell's equations will be unified in a single stroke. Look forward to it.

> <strong>Note</strong> (Why stop here?) Many textbooks close at the point where $dF=0$ has been shown, with "and thus Maxwell's equations are geometric." But this book's approach is different. Writing out every matrix component in full, using $d_4$ and $\ast_4$ in the calculations, and returning to $d_3$ and $\ast_3$ in the spatial dictionary to reproduce the vector-analysis formulas—the ability to make that round trip is precisely the destination of the "measuring device" framework built up from Chapter 1.

---

### §10.6 Constructing the Potential — Starting from $F=-d\mathcal{A}$

In §10.2, we defined the electromagnetic field $F$ as an assembly of $\mathbf{E}$ and $\mathbf{B}$.

But there is a deeper way to look at it.

$F$ can be built from a certain $1$-form by taking its exterior derivative.

Call that $1$-form $\mathcal{A}$. If we can set

$$
F=-d\mathcal{A},
$$

then

$$
dF
=
d(-d\mathcal{A})
=
-d(d\mathcal{A})
=
0
$$

holds.

In other words, the two equations we obtained in §10.4 by writing out every component,

$$
\mathrm{div}\,\mathbf{B}=0,
\qquad
\mathrm{curl}\,\mathbf{E}
=
-\frac{\partial\mathbf{B}}{\partial t}
$$

were already contained inside the identity of the exterior derivative

$$
dd=0.
$$

That is the heart of the potential representation.

In §10.4, we expanded $dF=0$ into the coefficients of four basis $3$-forms. But if we build $F$ as $-d\mathcal{A}$, those four conditions follow automatically in a single line.

So let us actually write down such an $\mathcal{A}$.

#### Setting up the four-potential

The four-potential $\mathcal{A}$ is a $1$-form. In electromagnetism, the scalar potential $\phi$ and the vector potential $\mathbf{A}$ come as a pair.

In this chapter, to satisfy both the $F$ of §10.2 and the standard formulas

$$
\mathbf{E}
=
-\nabla\phi
-
\frac{\partial\mathbf{A}}{\partial t},
\qquad
\mathbf{B}
=
\nabla\times\mathbf{A}
$$

at once, we adopt the following sign convention for the potential $1$-form:

$$
\mathcal{A}
=
\phi\,dt
-
A_x\,dx
-
A_y\,dy
-
A_z\,dz
$$

Here $\phi,A_x,A_y,A_z$ are all functions of $(t,x,y,z)$.

> <strong>Note</strong> (normalization of the potential)
> Read $\mathbf{A}$ here in the same normalized units used throughout this chapter. Just as the $\mathbf{B}$ of Chapter 10 is not the physical magnetic flux density but $c\mathbf{B}_{\mathrm{SI}}$, think of $\mathbf{A}$ as the normalized vector potential $c\mathbf{A}_{\mathrm{SI}}$ when needed. Under this convention, $\mathbf{B}=\nabla\times\mathbf{A}$ and $\mathbf{E}=-\nabla\phi-\partial\mathbf{A}/\partial t$ hold simultaneously.

From here we compute $d\mathcal{A}$, and finally set $F=-d\mathcal{A}$.

The point of this calculation is to confirm that the components of $F$ defined in §10.2 agree at the same time with the usual potential formulas.

#### Computing $d\mathcal{A}$ component by component

The computation of $d\mathcal{A}$ is exactly the procedure we have followed since Chapter 5. Apply $d$ to each of the four terms of $\mathcal{A}$.

$$
\begin{aligned}
d(\phi\,dt)
&=
\frac{\partial\phi}{\partial x}\,dx\wedge dt
+
\frac{\partial\phi}{\partial y}\,dy\wedge dt
+
\frac{\partial\phi}{\partial z}\,dz\wedge dt,
\\[0.5em]
d(-A_x\,dx)
&=
-\frac{\partial A_x}{\partial t}\,dt\wedge dx
-
\frac{\partial A_x}{\partial y}\,dy\wedge dx
-
\frac{\partial A_x}{\partial z}\,dz\wedge dx,
\\[0.5em]
d(-A_y\,dy)
&=
-\frac{\partial A_y}{\partial t}\,dt\wedge dy
-
\frac{\partial A_y}{\partial x}\,dx\wedge dy
-
\frac{\partial A_y}{\partial z}\,dz\wedge dy,
\\[0.5em]
d(-A_z\,dz)
&=
-\frac{\partial A_z}{\partial t}\,dt\wedge dz
-
\frac{\partial A_z}{\partial x}\,dx\wedge dz
-
\frac{\partial A_z}{\partial y}\,dy\wedge dz.
\end{aligned}
$$

The time derivative of $\phi$ vanishes because $dt\wedge dt=0$.

Likewise, the $x$ derivative of $A_x$, the $y$ derivative of $A_y$, and the $z$ derivative of $A_z$ each vanish by $dx\wedge dx=0$, $dy\wedge dy=0$, and $dz\wedge dz=0$.

Add these together and collect by basis $2$-form using the antisymmetry of the wedge product.

First, look at the coefficient of $dt\wedge dx$.

From $d(\phi\,dt)$ we get

$$
\frac{\partial\phi}{\partial x}\,dx\wedge dt
=
-\frac{\partial\phi}{\partial x}\,dt\wedge dx.
$$

From $d(-A_x\,dx)$ we also get

$$
-\frac{\partial A_x}{\partial t}\,dt\wedge dx.
$$

Therefore the $dt\wedge dx$ coefficient of $d\mathcal{A}$ is

$$
-\frac{\partial\phi}{\partial x}
-
\frac{\partial A_x}{\partial t}.
$$

Next, look at the coefficient of $dy\wedge dz$.

From $d(-A_y\,dy)$ we get

$$
-\frac{\partial A_y}{\partial z}\,dz\wedge dy
=
\frac{\partial A_y}{\partial z}\,dy\wedge dz.
$$

From $d(-A_z\,dz)$ we also get

$$
-\frac{\partial A_z}{\partial y}\,dy\wedge dz.
$$

Therefore the $dy\wedge dz$ coefficient of $d\mathcal{A}$ is

$$
-\frac{\partial A_z}{\partial y}
+
\frac{\partial A_y}{\partial z}.
$$

Collecting all six basis elements in the same way,

$$
\begin{aligned}
d\mathcal{A}
&=
\left(
-\frac{\partial\phi}{\partial x}
-
\frac{\partial A_x}{\partial t}
\right)
dt\wedge dx
\\[0.5em]
&\quad+
\left(
-\frac{\partial\phi}{\partial y}
-
\frac{\partial A_y}{\partial t}
\right)
dt\wedge dy
\\[0.5em]
&\quad+
\left(
-\frac{\partial\phi}{\partial z}
-
\frac{\partial A_z}{\partial t}
\right)
dt\wedge dz
\\[0.5em]
&\quad+
\left(
-\frac{\partial A_z}{\partial y}
+
\frac{\partial A_y}{\partial z}
\right)
dy\wedge dz
\\[0.5em]
&\quad+
\left(
-\frac{\partial A_x}{\partial z}
+
\frac{\partial A_z}{\partial x}
\right)
dz\wedge dx
\\[0.5em]
&\quad+
\left(
-\frac{\partial A_y}{\partial x}
+
\frac{\partial A_x}{\partial y}
\right)
dx\wedge dy.
\end{aligned}
$$
#### On the Signs

The $F$ defined in §10.2 was

$$
F
=
-E_x\,dt\wedge dx
-
E_y\,dt\wedge dy
-
E_z\,dt\wedge dz
+
B_x\,dy\wedge dz
+
B_y\,dz\wedge dx
+
B_z\,dx\wedge dy
$$

If we set $F=d\mathcal{A}$ here, comparing the $dt\wedge dx$ coefficients yields

$$
-E_x
=
-\frac{\partial\phi}{\partial x}
-
\frac{\partial A_x}{\partial t}
$$

so we obtain

$$
E_x
=
\frac{\partial\phi}{\partial x}
+
\frac{\partial A_x}{\partial t}
$$

This has the opposite sign from the standard

$$
E_x
=
-\frac{\partial\phi}{\partial x}
-
\frac{\partial A_x}{\partial t}
$$

Therefore in this chapter we set

$$
F=-d\mathcal{A}
$$

With this choice, the $dt\wedge dx$ coefficient becomes

$$
-E_x
=
\frac{\partial\phi}{\partial x}
+
\frac{\partial A_x}{\partial t}
$$

so we obtain

$$
E_x
=
-\frac{\partial\phi}{\partial x}
-
\frac{\partial A_x}{\partial t}
$$

Similarly, looking at the $dy\wedge dz$ coefficient, the $dy\wedge dz$ coefficient of $-d\mathcal{A}$ is

$$
\frac{\partial A_z}{\partial y}
-
\frac{\partial A_y}{\partial z}
$$

Therefore we obtain

$$
B_x
=
\frac{\partial A_z}{\partial y}
-
\frac{\partial A_y}{\partial z}
$$

Collecting all components,

$$
\mathbf{E}
=
-\nabla\phi
-
\frac{\partial\mathbf{A}}{\partial t},
\qquad
\mathbf{B}
=
\nabla\times\mathbf{A}.
$$

In other words, if we set

$$
\mathcal{A}
=
\phi\,dt
-
A_x\,dx
-
A_y\,dy
-
A_z\,dz,
\qquad
F=-d\mathcal{A}
$$

then the coefficient representation of $F$ in §10.2 and the standard potential formulas are reconciled at once.

> <strong>Note</strong> ($F$ and sign conventions for potentials)
> The definition $F=-d\mathcal{A}$ is adopted so that simultaneously: the $dt\wedge dx$ coefficient of $F$ in §10.2 is $-E_x$; and $\mathbf{E}=-\nabla\phi-\partial\mathbf{A}/\partial t$, $\mathbf{B}=\nabla\times\mathbf{A}$ hold. Other sign conventions exist, such as $F=+d\mathcal{A}$, $\mathcal{A}=-\phi\,dt+\cdots$, and so on.


#### $dd=0$ Proves $dF=0$

Now let us return to the opening discussion.

Since $F=-d\mathcal{A}$,

$$
dF
=
d(-d\mathcal{A})
=
-d(d\mathcal{A})
=
0.
$$

This is exactly the fundamental property of the exterior derivative seen in Chapter 5 §5.8:

$$
dd=0
$$

Therefore, the component expansions obtained in §10.4,

$$
\mathrm{div}\,\mathbf{B}=0,
\qquad
\mathrm{curl}\,\mathbf{E}
=
-\frac{\partial\mathbf{B}}{\partial t}
$$

follow automatically the moment we set $F=-d\mathcal{A}$.

What is happening here is not mere notational compression.

The $dd=0$ seen in Chapter 5 appears here as half of Maxwell's equations.

The moment $F$ is built as $-d\mathcal{A}$, $dF=0$ is no longer a law to be proved but an identity that follows automatically from the structure of the exterior derivative.

> <strong>Note</strong> ($\mathbf{B}$ and $\mathrm{div}\,\mathbf{B}=0$)
> In vector analysis too, it is known as a formula that if $\mathbf{B}$ can be written as the curl of something then $\mathrm{div}\,\mathbf{B}=0$. This is the familiar identity $\mathrm{div}\,\mathrm{curl}\equiv0$, the three-dimensional vector-analysis version of $dd=0$.

#### What Remains Is the Other Equation

$dF=0$ follows automatically from $F=-d\mathcal{A}$.

What about the other equation

$$
d(\ast F)
=
\mu_0(\ast\mathcal{J})
$$

Here we write it in symbolic notation to see the structure. In component calculations, read this as $d_4(\ast_4F)=\mu_0(\ast_4\mathcal{J})$. This one does not automatically become zero. Substituting $F=-d\mathcal{A}$,

$$
d(\ast(-d\mathcal{A}))
=
\mu_0(\ast\mathcal{J})
$$

that is,

$$
-d(\ast d\mathcal{A})
=
\mu_0(\ast\mathcal{J})
$$

This is the equation that the potential $\mathcal{A}$ satisfies.

> <strong>Note</strong> (gauge freedom) Transform as $\mathcal{A}'=\mathcal{A}+d\chi$ ($\chi$ is an arbitrary $0$-form). Then $F'=-d\mathcal{A}'=-d\mathcal{A}-d(d\chi)=-d\mathcal{A}=F$, so the physical electromagnetic field $F$ is invariant. This is a gauge transformation—another manifestation of $dd=0$. In electromagnetism, by adjusting the scalar potential $\phi$ and vector potential $\mathbf{A}$ together, one can choose a gauge convenient for calculation without changing $F$. Under the component convention $\mathcal{A}=\phi\,dt-A_i\,dx^i$, this means $\phi'=\phi+\partial_t\chi$ and $\mathbf{A}'=\mathbf{A}-\nabla\chi$; the sign difference from some physics texts comes from our choice of spatial signs in $\mathcal{A}$.

> <strong>Checkpoint so far — Chapter 10 as a whole</strong>
> - The electromagnetic field $F$ is a $4\times4$ antisymmetric matrix. Its six independent components accommodate $E_x,E_y,E_z,B_x,B_y,B_z$.
> - Symbolically we write $dF=0,\;d(\ast F)=\mu_0(\ast\mathcal{J})$. In component calculations, distinguish four-dimensional spacetime operators as $d_4,\ast_4$ and three-dimensional spatial operators as $d_3,\ast_3$.
> - Expanding $d_4F=0$ in components yields $\mathrm{div}\,\mathbf{B}=0$ and $\mathrm{curl}\,\mathbf{E}=-\partial\mathbf{B}/\partial t$.
> - Under this chapter's signature and orientation conventions, $\ast_4F$ appears to swap $E$ and $B$. The remaining two equations come from $d_4(\ast_4F)=\mu_0(\ast_4\mathcal{J})$.
> - <strong>Potential construction</strong>: From $\mathcal{A}=\phi\,dt-A_x\,dx-A_y\,dy-A_z\,dz$ we obtain $F=-d\mathcal{A}$. Then $dF=0$ holds automatically from $dd=0$. This means $\mathrm{div}\,\mathbf{B}=0$ and $\mathrm{curl}\,\mathbf{E}=-\partial\mathbf{B}/\partial t$ are contained in the structure of the exterior derivative.
> - The other equation $d(\ast F)=\mu_0(\ast\mathcal{J})$ becomes, upon substituting $F=-d\mathcal{A}$, an equation satisfied by the potential $\mathcal{A}$. In component calculations, read this as $d_4(\ast_4F)=\mu_0(\ast_4\mathcal{J})$.

---

## Appendix E: Slice-Matrix Representation of $d_4F$ and $d_4(\ast_4F)$ — Seeing Maxwell's Equations as $4\times4\times4$ Arrays

In §10.4 and §10.5 we rewrote the symbolic equations $dF=0,\;d(\ast F)=\mu_0(\ast\mathcal J)$ into the computational notation $d_4F,\;d_4(\ast_4F)$ and expanded them as coefficients of basis $3$-forms. In this appendix we visualize the same calculation as a <strong>bundle of $4\times4$ slice matrices</strong>—essentially a third-order $4\times4\times4$ tensor. It extends Appendix A and is the culmination of this book's practice of "putting everything into matrices."

### E.1 Basis $3$-forms and their slice matrices — all 16

The four basis $3$-forms in four dimensions are (compared with the ordering in §10.4, the signs and order of $\omega_2$ and $\omega_3$ differ, but the four forms themselves are the same):

$$
\omega_1 = dt\wedge dx\wedge dy,\qquad
\omega_2 = dt\wedge dx\wedge dz,\qquad
\omega_3 = dt\wedge dy\wedge dz,\qquad
\omega_4 = dx\wedge dy\wedge dz
$$

For each $\omega_i$, we define <strong>slice matrices</strong> $\mathbf{S}_{t}^{(\omega_i)}, \mathbf{S}_{x}^{(\omega_i)}, \mathbf{S}_{y}^{(\omega_i)}, \mathbf{S}_{z}^{(\omega_i)}$ in the coordinate directions $t,x,y,z$. A slice matrix is the $3$-form formed by the three remaining directions after omitting that coordinate direction, recast as a $4\times4$ antisymmetric matrix. Rows and columns are ordered $(t,x,y,z)$. Nonzero entries are $\pm1$. Four bases $\times$ four slices $=$ all $16$ matrices.

<strong>(1)</strong> Slices of $\omega_1 = dt\wedge dx\wedge dy$:

$$
\mathbf{S}_{t}^{(\omega_1)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&1&0\\[2pt]0&-1&0&0\\[2pt]0&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{x}^{(\omega_1)}=\begin{pmatrix}0&0&-1&0\\[2pt]0&0&0&0\\[2pt]1&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

$$
\mathbf{S}_{y}^{(\omega_1)}=\begin{pmatrix}0&1&0&0\\[2pt]-1&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{z}^{(\omega_1)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

<strong>(2)</strong> Slices of $\omega_2 = dt\wedge dx\wedge dz$:

$$
\mathbf{S}_{t}^{(\omega_2)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&0&0\\[2pt]0&-1&0&0\end{pmatrix},\qquad
\mathbf{S}_{x}^{(\omega_2)}=\begin{pmatrix}0&0&0&-1\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]1&0&0&0\end{pmatrix}
$$

$$
\mathbf{S}_{y}^{(\omega_2)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{z}^{(\omega_2)}=\begin{pmatrix}0&1&0&0\\[2pt]-1&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

<strong>(3)</strong> Slices of $\omega_3 = dt\wedge dy\wedge dz$:

$$
\mathbf{S}_{t}^{(\omega_3)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&-1&0\end{pmatrix},\qquad
\mathbf{S}_{x}^{(\omega_3)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

$$
\mathbf{S}_{y}^{(\omega_3)}=\begin{pmatrix}0&0&0&-1\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]1&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{z}^{(\omega_3)}=\begin{pmatrix}0&0&-1&0\\[2pt]0&0&0&0\\[2pt]1&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

<strong>(4)</strong> Slices of $\omega_4 = dx\wedge dy\wedge dz$:

$$
\mathbf{S}_{t}^{(\omega_4)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix},\qquad
\mathbf{S}_{x}^{(\omega_4)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&-1&0\end{pmatrix}
$$

$$
\mathbf{S}_{y}^{(\omega_4)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&-1\\[2pt]0&0&0&0\\[2pt]0&1&0&0\end{pmatrix},\qquad
\mathbf{S}_{z}^{(\omega_4)}=\begin{pmatrix}0&0&0&0\\[2pt]0&0&-1&0\\[2pt]0&1&0&0\\[2pt]0&0&0&0\end{pmatrix}
$$

Of the 16 matrices, $\mathbf{S}_{z}^{(\omega_1)}, \mathbf{S}_{y}^{(\omega_2)}, \mathbf{S}_{x}^{(\omega_3)}, \mathbf{S}_{t}^{(\omega_4)}$ are zero matrices. The remaining 12 each contain one $\pm1$ (and one antisymmetric partner). This is the substance of the $4\times4\times4$ tensor.

### E.2 Writing $dF$ with slice matrices

From the expansion in §10.4, the basis coefficients of $dF$ are given by

$$
\begin{aligned}
A_{txy} &= \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} + \frac{\partial B_z}{\partial t} = (\mathrm{curl}\,\mathbf{E})_z + \frac{\partial B_z}{\partial t}
\quad (\text{coefficient of } \omega_1 = dt\wedge dx\wedge dy) \\[6pt]
A_{txz} &= \frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z} - \frac{\partial B_y}{\partial t} = -(\mathrm{curl}\,\mathbf{E})_y - \frac{\partial B_y}{\partial t}
\quad (\text{coefficient of } \omega_2 = dt\wedge dx\wedge dz) \\[6pt]
A_{tyz} &= \frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z} + \frac{\partial B_x}{\partial t} = (\mathrm{curl}\,\mathbf{E})_x + \frac{\partial B_x}{\partial t}
\quad (\text{coefficient of } \omega_3 = dt\wedge dy\wedge dz) \\[6pt]
A_{xyz} &= \frac{\partial B_x}{\partial x} + \frac{\partial B_y}{\partial y} + \frac{\partial B_z}{\partial z} = \mathrm{div}\,\mathbf{B}
\quad (\text{coefficient of } \omega_4 = dx\wedge dy\wedge dz)
\end{aligned}
$$

Each slice of $dF$ is a linear combination of the four basis slice matrices with coefficients $A_{\cdots}$. For example, the $t$-slice $\mathbf{S}_{t}^{(dF)}$ collapses into a single $4\times4$ antisymmetric matrix with all 16 entries displayed explicitly:

$$
\mathbf{S}_{t}^{(dF)}
{=}
\left(\begin{array}{c|cccc}
 & t & x & y & z \\\hline
t & 0 & 0 & 0 & 0 \\[6pt]
x & 0 & 0 &
\displaystyle \frac{\partial E_y}{\partial x} - \frac{\partial E_x}{\partial y} + \frac{\partial B_z}{\partial t} &
\displaystyle \frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z} - \frac{\partial B_y}{\partial t} \\[14pt]
y & 0 &
\displaystyle \frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x} - \frac{\partial B_z}{\partial t} &
0 &
\displaystyle \frac{\partial E_z}{\partial y} - \frac{\partial E_y}{\partial z} + \frac{\partial B_x}{\partial t} \\[14pt]
z & 0 &
\displaystyle \frac{\partial E_x}{\partial z} - \frac{\partial E_z}{\partial x} + \frac{\partial B_y}{\partial t} &
\displaystyle \frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y} - \frac{\partial B_x}{\partial t} &
0
\end{array}\right)
$$

The $x,y,z$ slices $\mathbf{S}_{x}^{(dF)}, \mathbf{S}_{y}^{(dF)}, \mathbf{S}_{z}^{(dF)}$ are obtained similarly from four-term linear combinations. The whole of $dF$ is this bundle of four slice matrices.

### E.3 Extracting coefficients by the Frobenius product

The Frobenius product introduced in Appendix D extends directly to $4\times4$ matrices.

> <strong>Note</strong> (not the metric-induced inner product) The Frobenius product here is not the spacetime inner product induced by the Minkowski metric. It is a pairing on arrays for extracting coefficients from the antisymmetric matrix representation. We use it as a coefficient-extraction operation against basis slice matrices; $\frac{1}{2}\operatorname{tr}(A^T B)$ is the computational device for that purpose.

$$
A \cdot B = \frac{1}{2}\operatorname{tr}(A^T B) = \frac{1}{2}\sum_{i=1}^{4}\sum_{j=1}^{4} A_{ij}B_{ij}
$$

With this inner product, each coefficient can be <strong>extracted in one line</strong> from each slice. For example,

$$
A_{txy} = \mathbf{S}_{t}^{(\omega_1)} \cdot \mathbf{S}_{t}^{(dF)}
$$

The only nonzero entries of $\mathbf{S}_{t}^{(\omega_1)}$ are $(x,y)=+1$ and $(y,x)=-1$, so the Frobenius product gives $(1 \cdot S_{xy} + (-1) \cdot S_{yx})/2 = (S_{xy} - S_{yx})/2 = S_{xy}$ (because $\mathbf{S}_{t}^{(dF)}$ is antisymmetric, $S_{yx}=-S_{xy}$). The coefficient pops out immediately.

Similarly, <strong>every coefficient is obtained by the Frobenius product with the corresponding basis slice</strong>. This structure is completely analogous to Appendix D, where $\ast_{2\to1}(\mathbf{M}) = (E_1\!\cdot\!\mathbf{M},\;E_2\!\cdot\!\mathbf{M},\;E_3\!\cdot\!\mathbf{M})$ extracted the components of a $2$-form $\mathbf{M}$. Only the degree has risen from $1\to2$ to $2\to3$, and the inner-product partner has changed from a column vector to a bundle of $4\times4$ matrices.

### E.4 Reading $dF=0$ through the slices

$dF=0$ means that all four slice matrices are zero matrices:

$$
\mathbf{S}_{t}^{(dF)} = \mathbf{0},\quad
\mathbf{S}_{x}^{(dF)} = \mathbf{0},\quad
\mathbf{S}_{y}^{(dF)} = \mathbf{0},\quad
\mathbf{S}_{z}^{(dF)} = \mathbf{0}
$$

Reading the nonzero entries of the $t$-slice (above),
- from the $(x,y)$ entry $=0$: $(\mathrm{curl}\,\mathbf{E})_z + \partial B_z/\partial t = 0$
- from the $(x,z)$ entry $=0$: $-(\mathrm{curl}\,\mathbf{E})_y - \partial B_y/\partial t = 0$
- from the $(y,z)$ entry $=0$: $(\mathrm{curl}\,\mathbf{E})_x + \partial B_x/\partial t = 0$

These three are nothing but $\mathrm{curl}\,\mathbf{E} = -\partial\mathbf{B}/\partial t$. From the nonzero entries of the $z$-slice (arising from $\mathbf{S}_{z}^{(\omega_4)}$) we obtain $\mathrm{div}\,\mathbf{B} = 0$. The appearance is huge, but the content is merely the repetition of the four coefficient comparisons from §10.4.

### E.5 Slice representation of $d_4(\ast_4F) = \mu_0(\ast_4\mathcal{J})$

The source side has the same structure. $\ast_4F$ and $\ast_4\mathcal{J}$ were expanded in §10.5, and $d_4(\ast_4F)$ becomes slice matrices of the same type as $d_4F$—only the positions of the $\mathbf{E}$ and $\mathbf{B}$ coefficients are swapped.

Write the $\omega_1\sim\omega_4$ coefficients of $d_4(\ast_4F)$ as $B_{txy}, B_{txz}, B_{tyz}, B_{xyz}$.

$$
\begin{aligned}
B_{txy} &= \frac{\partial B_x}{\partial y} - \frac{\partial B_y}{\partial x} + \frac{\partial E_z}{\partial t}
\quad (\text{coefficient of } dt\wedge dx\wedge dy \text{ in §10.5}) \\[6pt]
B_{txz} &= \frac{\partial B_x}{\partial z} - \frac{\partial B_z}{\partial x} - \frac{\partial E_y}{\partial t} \\[6pt]
B_{tyz} &= \frac{\partial B_y}{\partial z} - \frac{\partial B_z}{\partial y} + \frac{\partial E_x}{\partial t} \\[6pt]
B_{xyz} &= \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z}
\quad (= \mathrm{div}\,\mathbf{E})
\end{aligned}
$$

Each slice of $d_4(\ast_4F)$ is likewise a linear combination of the basis slice matrices with the four coefficients $B_{\cdots}$, just as for $d_4F$. Writing the $t$-slice term by term:

$$
\begin{aligned}
\mathbf{S}_{t}^{(d_4(\ast_4F))}
&= \left(\frac{\partial B_x}{\partial y} - \frac{\partial B_y}{\partial x} + \frac{\partial E_z}{\partial t}\right)
\begin{pmatrix}0&0&0&0\\[2pt]0&0&1&0\\[2pt]0&-1&0&0\\[2pt]0&0&0&0\end{pmatrix} \\[10pt]
&\quad+ \left(\frac{\partial B_x}{\partial z} - \frac{\partial B_z}{\partial x} - \frac{\partial E_y}{\partial t}\right)
\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&0&0\\[2pt]0&-1&0&0\end{pmatrix} \\[10pt]
&\quad+ \left(\frac{\partial B_y}{\partial z} - \frac{\partial B_z}{\partial y} + \frac{\partial E_x}{\partial t}\right)
\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&1\\[2pt]0&0&-1&0\end{pmatrix}
{+} B_{xyz}
\begin{pmatrix}0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\\[2pt]0&0&0&0\end{pmatrix}
\end{aligned}
$$

Add corresponding entries into a single matrix. Compare with the $t$-slice of $d_4F$—$\mathbf{E}$ and $\mathbf{B}$ (and the cyclic permutations of indices) swap cleanly.

$$
\mathbf{S}_{t}^{(d_4(\ast_4F))}
{=}
\left(\begin{array}{c|cccc}
 & t & x & y & z \\\hline
t & 0 & 0 & 0 & 0 \\[6pt]
x & 0 & 0 &
\displaystyle\frac{\partial B_x}{\partial y} {-} \frac{\partial B_y}{\partial x} {+} \frac{\partial E_z}{\partial t} &
\displaystyle\frac{\partial B_x}{\partial z} {-} \frac{\partial B_z}{\partial x} {-} \frac{\partial E_y}{\partial t} \\[14pt]
y & 0 &
\displaystyle{-}\frac{\partial B_x}{\partial y} {+} \frac{\partial B_y}{\partial x} {-} \frac{\partial E_z}{\partial t} &
0 &
\displaystyle\frac{\partial B_y}{\partial z} {-} \frac{\partial B_z}{\partial y} {+} \frac{\partial E_x}{\partial t} \\[14pt]
z & 0 &
\displaystyle{-}\frac{\partial B_x}{\partial z} {+} \frac{\partial B_z}{\partial x} {+} \frac{\partial E_y}{\partial t} &
\displaystyle{-}\frac{\partial B_y}{\partial z} {+} \frac{\partial B_z}{\partial y} {-} \frac{\partial E_x}{\partial t} &
0
\end{array}\right)
$$

The right-hand side $\mu_0(\ast_4\mathcal{J})$ can also be written as the same linear combination of four slice matrices. Re-expanding $\ast_4\mathcal{J}$ in the basis order of this appendix (see §10.5), the coefficients of $\omega_1\!\sim\!\omega_4$ are, in order, $-\mu_0 c J_z,\; +\mu_0 c J_y,\; -\mu_0 c J_x,\; \rho_{\mathrm e}/\varepsilon_0$. That is,

$$
\mathbf{S}_{t}^{(d_4(\ast_4F))} = \mathbf{S}_{t}^{(\mu_0\ast_4\mathcal{J})},\quad
\mathbf{S}_{x}^{(d_4(\ast_4F))} = \mathbf{S}_{x}^{(\mu_0\ast_4\mathcal{J})},\quad
\mathbf{S}_{y}^{(d_4(\ast_4F))} = \mathbf{S}_{y}^{(\mu_0\ast_4\mathcal{J})},\quad
\mathbf{S}_{z}^{(d_4(\ast_4F))} = \mathbf{S}_{z}^{(\mu_0\ast_4\mathcal{J})}
$$

Reading the nonzero entries of the $t$-slice gives $-\mathrm{curl}\,\mathbf{B} + \partial\mathbf{E}/\partial t = -c\mu_0\mathbf{J}$, i.e. the components of $\mathrm{curl}\,\mathbf{B} = c\mu_0\mathbf{J} + \partial\mathbf{E}/\partial t$. From the $(x,y)$ entry of the $z$-slice we obtain $\mathrm{div}\,\mathbf{E} = \rho_{\mathrm e}/\varepsilon_0$.

---

Thus the full content of Maxwell's equations has been visualized as a bundle of $4\times4\times4$ slice matrices. What is written in each cell of this "giant array" is nothing but a combination of partial derivatives—and we have seen how the two algebraic operations of four-dimensional exterior differentiation $d_4$ and the Hodge star $\ast_4$ describe physical laws in the tidy grammar of matrices. That is the achievement of this appendix.

---

## Appendix F: The Four Equations of Chapter 5 and the Two Equations of Chapter 10

In the main text of Chapter 10, Maxwell's equations were written symbolically as two equations on four-dimensional spacetime:

$$
dF=0,
\qquad
d(\ast F)=\mu_0(\ast\mathcal{J})
$$

In component calculations, we read this as $d_4F=0,\;d_4(\ast_4F)=\mu_0(\ast_4\mathcal J)$.

However, in Chapter 5, rather than bundling everything at once into a $2$-form on four-dimensional spacetime, we worked with a viewpoint that treats the electric field, magnetic field, current, and charge at each instant as differential forms on space.

This appendix confirms that the "four equations on space" from Chapter 5 and the "two equations on spacetime" from the main text of Chapter 10 are simply the same Maxwell equations written in different splittings.

### F.1 $(E,B,J,\rho_{\mathrm e})$ on space

Consider space $(x,y,z)$ at each instant $t$.

Place the electric field as a $1$-form on space:

$$
E = E_x\,dx + E_y\,dy + E_z\,dz
$$

Place the magnetic field as a $2$-form on space:

$$
B = B_x\,dy\wedge dz + B_y\,dz\wedge dx + B_z\,dx\wedge dy
$$

The current density is also represented as a $2$-form, as a quantity that passes through space:

$$
J = J_x\,dy\wedge dz + J_y\,dz\wedge dx + J_z\,dx\wedge dy
$$

The charge density is written as a $3$-form on space:

$$
\rho_{\mathrm e}\,dx\wedge dy\wedge dz
$$

The $d$ and $\ast$ used here are the three-dimensional spatial $d$ and $\ast$. When we wish to distinguish them from the four-dimensional spacetime $d$ and $\ast$ used in the main text of Chapter 10, we write

$$
d_3,\quad \ast_3,
\qquad
d_4,\quad \ast_4
$$

### F.2 The four equations on space

In this notation, Maxwell's equations become the following four:

$$
d_3B=0
$$

$$
d_3E+\frac{\partial B}{\partial t}=0
$$

$$
d_3(\ast_3E)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)
$$

$$
d_3(\ast_3B)=\mu_0 c\,J+\frac{\partial(\ast_3E)}{\partial t}
$$

These are the four equations in differential-form style from Chapter 5.

Here the right-hand side has $\ast_3$ applied to read the scalar field $\rho_{\mathrm e}/\varepsilon_0$ as a $3$-form on space. In Cartesian coordinates,

$$
\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)=\frac{\rho_{\mathrm e}}{\varepsilon_0}\,dx\wedge dy\wedge dz
$$

In this book we do not place the vector-analytic $\mathrm{div}$ as a basic operation from the outset, but read it as the composite of $d$ and $\ast$:

$$
\mathrm{div}=\ast_3 d_3\ast_3
$$

Therefore, even for a scalar field such as charge density, on the right-hand side of an equation to be integrated we convert it to a $3$-form via $\ast_3$ before comparing. In particular, for the third equation we act with $\ast_3$ on both sides to read

$$
\ast_3d_3(\ast_3E)=\frac{\rho_{\mathrm e}}{\varepsilon_0}
$$

The left-hand side is what this book's dictionary calls $\mathrm{div}\,\mathbf E$.

Translating back to vector-analytic notation, these are respectively

$$
\mathrm{div}\,\mathbf B=0,
\qquad
\mathrm{curl}\,\mathbf E=-\frac{\partial\mathbf B}{\partial t},
$$

$$
\mathrm{div}\,\mathbf E=\frac{\rho_{\mathrm e}}{\varepsilon_0},
\qquad
\mathrm{curl}\,\mathbf B=\mu_0 c\,\mathbf J+\frac{\partial\mathbf E}{\partial t}
$$

Here $t$ and $\mathbf B$ are, as in the main text of Chapter 10, already normalized quantities with

$$
t=ct_{\mathrm{SI}},
\qquad
\mathbf B=c\mathbf B_{\mathrm{SI}}
$$

> <strong>Note</strong> (There is also a way to write without the metric) In this book we do not take the vector-analytic $\mathrm{div}$ as our starting basic operation, but read $\mathrm{div}=\ast d\ast$ to match the dictionary built up so far. Gauss's law is also written as $d_3(\ast_3E) = \ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)$ and then, when needed, read as $\mathrm{div}\,\mathbf E=\rho_{\mathrm e}/\varepsilon_0$. That is, we move back and forth among scalar fields, vector fields, and forms using the $\ast$ built from the metric. Maxwell's equations, however, also admit a standpoint that does not use the metric. In the view emphasized in Hehl–Obukhov's *Foundations of Classical Electrodynamics: Charge, Flux, and Metric*, one first separates two forms $F$ and $H$ and writes $dF=0, dH=J$. Here the Hodge star does not enter the equations themselves. The metric and properties of the medium enter later as a relation linking $H$ and $F$. This book does not go deep in that direction. The purpose is strictly to use the dictionary of $d$ and $\ast$ built up so far and see how the usual vector-analytic equations appear as components.

### F.3 Two equations emerge from $d_4F=0$

In the main text of Chapter 10, the electromagnetic field $F$ was defined by

$$
F=-E_x\,dt\wedge dx-E_y\,dt\wedge dy-E_z\,dt\wedge dz+B_x\,dy\wedge dz+B_y\,dz\wedge dx+B_z\,dx\wedge dy
$$

Using the spatial $E$ and $B$, this can be written as

$$
F=-dt\wedge E+B
$$

For a spatial form $\alpha(t)$,

$$
d_4\alpha = dt\wedge\frac{\partial\alpha}{\partial t}+d_3\alpha
$$

Therefore, computing

$$
d_4F=d_4(-dt\wedge E+B)
$$

we have

$$
d_4(-dt\wedge E)=dt\wedge d_3E
$$

and

$$
d_4B=dt\wedge\frac{\partial B}{\partial t}+d_3B
$$

Hence

$$
d_4F=dt\wedge\left(d_3E+\frac{\partial B}{\partial t}\right)+d_3B.
$$

Therefore,

$$
d_4F=0
$$

is the same as setting to zero separately the part that contains $dt$ and the part that does not, giving

$$
d_3E+\frac{\partial B}{\partial t}=0,
\qquad
d_3B=0
$$

In other words, the first equation of the main text of Chapter 10,

$$
d_4F=0
$$

splits in Chapter 5 style into the two equations

$$
d_3B=0,
\qquad
d_3E+\frac{\partial B}{\partial t}=0
$$

### F.4 The remaining two emerge from $d_4(\ast_4F)=\mu_0(\ast_4\mathcal J)$

Next we look at the source side.

Under the conventions of the main text of Chapter 10,

$$
\ast_4F= B_x\,dt\wedge dx+B_y\,dt\wedge dy+B_z\,dt\wedge dz+E_x\,dy\wedge dz+E_y\,dz\wedge dx+E_z\,dx\wedge dy.
$$

In spatial notation, this is

$$
\ast_4F=dt\wedge(\ast_3B)+\ast_3E
$$

Here $B$ is the spatial magnetic $2$-form defined in F.1, not the column-vector field $\mathbf{B}$. Thus $\ast_3B$ is a spatial $1$-form. Indeed,

$$
\ast_3B=B_x\,dx+B_y\,dy+B_z\,dz
$$

so

$$
dt\wedge(\ast_3B)=B_x\,dt\wedge dx+B_y\,dt\wedge dy+B_z\,dt\wedge dz
$$

Also,

$$
\ast_3E=E_x\,dy\wedge dz+E_y\,dz\wedge dx+E_z\,dx\wedge dy
$$

Apply $d_4$ to this.

First,

$$
d_4\bigl(dt\wedge(\ast_3B)\bigr)=-dt\wedge d_3(\ast_3B)
$$

On the other hand,

$$
d_4(\ast_3E)=dt\wedge\frac{\partial(\ast_3E)}{\partial t}+d_3(\ast_3E).
$$

Therefore,

$$
d_4(\ast_4F)=dt\wedge\left(\frac{\partial(\ast_3E)}{\partial t}-d_3(\ast_3B)\right)+d_3(\ast_3E).
$$

The right-hand side, under the conventions of the main text of Chapter 10, is

$$
\mu_0(\ast_4\mathcal J)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)-\mu_0 c\,dt\wedge J
$$

where

$$
J=J_x\,dy\wedge dz+J_y\,dz\wedge dx+J_z\,dx\wedge dy
$$

Therefore, comparing the part that does not contain $dt$,

$$
d_3(\ast_3E)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right).
$$

And comparing the part that contains $dt$,

$$
\frac{\partial(\ast_3E)}{\partial t}-d_3(\ast_3B)=-\mu_0 c\,J.
$$

Rearranging,

$$
d_3(\ast_3B)=\mu_0 c\,J+\frac{\partial(\ast_3E)}{\partial t}.
$$

Therefore, the second equation of the main text of Chapter 10,

$$
d_4(\ast_4F)=\mu_0(\ast_4\mathcal J)
$$

splits in Chapter 5 style into the two equations

$$
d_3(\ast_3E)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)
$$

and

$$
d_3(\ast_3B)=\mu_0 c\,J+\frac{\partial(\ast_3E)}{\partial t}
$$

### F.5 Summary

In the differential-form style of Chapter 5, Maxwell's equations appear as four equations on space:

$$
d_3B=0
$$

$$
d_3E+\frac{\partial B}{\partial t}=0
$$

$$
d_3(\ast_3E)=\ast_3\left(\frac{\rho_{\mathrm e}}{\varepsilon_0}\right)
$$

$$
d_3(\ast_3B)=\mu_0 c\,J+\frac{\partial(\ast_3E)}{\partial t}
$$

On the other hand, in the main text of Chapter 10, time is treated as one coordinate on the same footing as space, and the electric and magnetic fields are bundled into $F$:

$$
F=-dt\wedge E+B
$$

Then the four equations above consolidate into the two

$$
d_4F=0
$$

and

$$
d_4(\ast_4F)=\mu_0(\ast_4\mathcal J)
$$

In other words, the fact that four become two is not so much compressing the equations as reassembling what was viewed with space and time separated into a single spacetime $2$-form measuring device.

The four equations of Chapter 5 are the way of writing that looks at space and time separately.
The two equations of Chapter 10 are the way of writing that looks at a spacetime $2$-form.

Both are looking at the same Maxwell equations. What differs is what one treats as a single bundled measuring device.

# Chapter 11: Toward Curved Spaces — What Lies Beyond This Book

# Chapter 11: Toward Curved Spaces — What Lies Beyond This Book

### §11.0 The Position of This Chapter — A Guidepost for Readers Who Want to Look Further Ahead

The purpose of this book was to dismantle $\nabla$ into $d$ and $\ast$, and to rebuild the formulas of vector analysis in a transparent way. Chapters 8 and 9 achieved that purpose. Chapter 10 was an "extra," showing how concisely this framework describes Maxwell's equations.

This chapter goes further still—it is a **guidepost** for readers who finish this book and wonder, "How can these tools $d$ and $\ast$ be used in a wider world?" It does not aim to be a self-contained account. As a bridge to specialist texts, it offers only a sketch of what changes and what stays the same. And one more thing—in this chapter I will use, without stopping as carefully for the reader as before, the sorts of mathematical wording I have deliberately avoided until now, even without pausing to define every term. I want you to feel how vast the world still is.

> <strong>Note</strong> (pretense and sincerity)
> "A guidepost for readers who want to look further ahead" is, in a way, the official line.
> If I am honest, it is also my preemptive answer to knowledgeable readers who might think, "This person does not really understand abstract mathematics."
> At the same time, I am convinced that lining up rigorous abstract theory from the start would be too much for a beginner's hands.
> This chapter is a place where a compromise as a "step in understanding" mixes with respect for standard mathematics.

> <strong>Note</strong> (an easy chapter for me)
> In this chapter, I do not need to weigh metaphors carefully, or balance rigor and clarity, or allocate information density.
> I need not worry much about the reader's cognitive load here either.
> On top of that, the logical flow is clear, so it was very easy to write.
> —I express nothing but respect for Bourbaki-style logical solidity.

> <strong>Note</strong> (an unexpected consequence of this book)
> The direct purpose of this book was to rewrite vector analysis in matrix form and to rebuild it transparently through the dictionary of $d$ and $\ast$.
> Looking back, however, this book may in a secondary way have been doing tensor analysis, in the sense of "handling components directly."
> A weakness of tensor analysis is that in the course of calculation one tends to lose the geometric "type" intuition of $k$-forms.
> This book adopted matrix notation precisely to preserve that type—degree, antisymmetry, the distinction between row and column vectors—visually, while still enabling component calculation.
> In other words, this book may be called an intermediate approach for gaining both "the geometric intuition of differential forms" and "the computational power of tensor analysis."
> —though I must admit that, seen from either tradition, it has unavoidably halfway aspects.

### §11.1 Manifolds — Starting from $\mathbf{g}(x)$

In this book we introduced the metric $\mathbf{g}$ in Chapter 6, and in Chapter 9 we practiced building the dictionary for $\ast$ from $\mathbf{g}$. In Cartesian coordinates in Chapter 6, $\mathbf{g} = I$ was a constant matrix, but in cylindrical and spherical coordinates in Chapter 9, the components of $\mathbf{g}$ already depended on $r, \rho, \theta$. What happens, then, if we view this not as a matter of coordinate representation but as a metric $\mathbf{g}(p)$ assigned to each point of space itself?

The dictionary for $\ast$ is built from $\mathbf{g}$. If $\mathbf{g}$ changes from place to place, the dictionary for $\ast$ changes from place to place as well. The correspondence table $dx \mapsto \ast(dx) = \cdots\, dy \wedge dz$ comes to have different coefficients at each point in space.

This viewpoint—"at each point we have a metric $\mathbf{g}(p)$, and from that metric we build $\ast$ at each point"—is the first model for moving on to Riemannian manifolds. In flat $\mathbb{R}^3$, $\mathbf{g}$ was the identity matrix, so the dictionary for $\ast$ was utterly simple. In a general coordinate representation, $\mathbf{g}$ is no longer necessarily the identity matrix and appears as a function of position. Even so, the procedure for writing down the dictionary for $\ast$ from $\mathbf{g}$ is the same as what we did in Chapter 9—only now we must look up the dictionary anew at each point.

> <strong>Note</strong> (position dependence of the metric and curvature) That the metric components $g_{ij}(x)$ depend on position does not by itself mean that space is curved. If we write Euclidean space in curvilinear coordinates (polar, spherical, and so on), $g_{ij}(x)$ depends on position even in a flat space. Whether space is curved is judged not by the metric components themselves or by the appearance of Christoffel symbols $\Gamma^i_{jk}$ in a particular coordinate system, but by whether the curvature tensor $R^i{}_{mjk}$ constructed from them vanishes.

The mathematical framework that organizes this world of "handling coordinates and the metric point by point" is the **manifold**. A manifold itself is defined first as a smooth space that is locally indistinguishable from $\mathbb{R}^n$. On top of that, smoothly assigning to the tangent space at each point a nondegenerate symmetric bilinear form $g_p$ gives a **manifold with metric**; if $g_p$ is positive definite, we get a **Riemannian manifold**, and if the signature is Lorentzian, a **Lorentzian manifold**.

> <strong>Note</strong> (on the phrase "curved spacetime") In expositions of general relativity, one often hears that "spacetime curves." As a personal preference, I am not very fond of this wording. At any single point one can choose a local inertial frame, set the metric to the Minkowski metric at that point, and make the Christoffel symbols vanish, but curvature generally does not vanish, and a finite neighborhood does not become flat as a whole. Curvature appears precisely as the mismatch when gluing local inertial frames together beyond first order. In other words, a single picture of a "curved rubber sheet" is not enough; it is more accurate, I feel, to view the issue as "through the metric and the connection, the question becomes how to compare tangent spaces at different points." That said, I am being pedantic here, and it is probably more intuitive to think plainly that spacetime "is curved."

#### 11.1.1 Definition — Charts and an Atlas

An $n$-dimensional **topological manifold** $M$ is a Hausdorff, second-countable topological space such that for every point $p \in M$ there exists an open set $U \subset M$ containing $p$ and a homeomorphism $\varphi: U \to \varphi(U) \subset \mathbb{R}^n$. The pair $(U, \varphi)$ is called a **chart** (coordinate neighborhood). When we write $\varphi(p) = (x^1(p), \dots, x^n(p))$, the $x^i$ are called **local coordinates**.

When a family of charts $\{(U_\alpha, \varphi_\alpha)\}$ covers $M$ and for every pair of overlapping charts the **coordinate change**

$$\varphi_\beta \circ \varphi_\alpha^{-1}: \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$$

is $C^\infty$, we call this a **smooth atlas**, and $M$ becomes a **smooth manifold ($C^\infty$ manifold)**. That the coordinate changes are smooth—this single point is what makes calculus on manifolds possible.

The $\mathbb{R}^3$ that this book has used as its stage throughout is the most trivial example of a manifold: the whole space is covered by a single chart, the identity map $\mathrm{id}: \mathbb{R}^3 \to \mathbb{R}^3$.

As another well-known example, there is the $n$-dimensional sphere $S^n = \{x \in \mathbb{R}^{n+1} \mid \|x\| = 1\}$. $S^n$ cannot be covered by one chart, but an atlas can be built from two charts (stereographic projection) omitting the north and south poles. Spacetime in general relativity is formulated as a Lorentzian manifold—a 4-dimensional manifold whose metric signature is $(-,+,+,+)$.

#### 11.1.2 Tangent Spaces — Defining "Differentiation on Curved Space"

In $\mathbb{R}^n$ we could naively define a "vector" as an arrow extending from the origin. On a manifold we cannot do that. Try to draw an arrow on the surface of a sphere and the arrow sticks out of the surface.

There are two equivalent ways to construct tangent spaces.

<strong>Definition by equivalence classes of curves.</strong> For a smooth curve $\gamma: (-\varepsilon, \varepsilon) \to M$ through $p$ ($\gamma(0)=p$), choose one chart $(U, \varphi)$ and compute the velocity vector $(\varphi \circ \gamma)'(0)$ in $\mathbb{R}^n$. Even if we choose another chart $(V, \psi)$, we have $(\psi \circ \gamma)'(0) = D(\psi \circ \varphi^{-1})_{\varphi(p)} \cdot (\varphi \circ \gamma)'(0)$, transformed by the Jacobian matrix. Thus the relation "having the same velocity in one chart" is preserved under change of chart, and the resulting equivalence class is independent of the chart. This equivalence class $[\gamma]$ is the **tangent vector** at $p$.

<strong>Definition by directional derivatives (derivations).</strong> We define a tangent vector $v \in T_p M$ as a linear map that assigns to each smooth function $f$ in a neighborhood of $p$ a real number $v(f)$ and satisfies the Leibniz rule $v(fg) = v(f)\,g(p) + f(p)\,v(g)$. This definition is intrinsic and independent of charts, and it survives generalization to algebraic geometry and elsewhere. Given a chart $(U, \varphi)$ and local coordinates $x^i$,

$$\left.\frac{\partial}{\partial x^i}\right|_p (f) = \left.\frac{\partial (f \circ \varphi^{-1})}{\partial x^i}\right|_{\varphi(p)}$$

forms a basis of $T_p M$. We have $\dim T_p M = \dim M = n$.

When two vector fields $X, Y$ are given, their **Lie bracket** $[X, Y] = XY - YX$ is again a vector field. We have $[X,Y]^i = \sum_j (X^j \partial_j Y^i - Y^j \partial_j X^i)$; we did not treat it explicitly in this book, but it is the operation at the root of Frobenius's theorem (integrability of distributions) and Lie group theory.

The disjoint union of tangent spaces at all points is the **tangent bundle** $TM = \bigsqcup_{p \in M} T_p M$. $TM$ itself is a $2n$-dimensional manifold. A **vector field** $X$ on $M$ is nothing but a smooth assignment of a tangent vector $X_p \in T_p M$ to each point $p \in M$—a **section** of the tangent bundle, $X: M \to TM$.

Let us also touch on coordinate change and the transformation law for bases. When two charts $(U, x^i)$ and $(V, y^j)$ overlap, the basis of the tangent space transforms as

$$\frac{\partial}{\partial y^j} = \sum_i \frac{\partial x^i}{\partial y^j}\,\frac{\partial}{\partial x^i}$$

The transformation matrix $\partial x^i/\partial y^j$ is exactly the Jacobian matrix of coordinate change that appeared repeatedly in Chapter 4 of this book. The basis transforms by the Jacobian of the coordinate change, and the components of a tangent vector transform by the inverse matrix so that the vector itself is unchanged (contravariant vector). By contrast, the components of a 1-form transform by the Jacobian matrix itself (covariant vector). This distinction between "contravariant" and "covariant"—in this book visualized as vectors as "columns" and 1-forms as "rows"—is the starting point of tensor analysis in manifold theory.

#### 11.1.3 Differential Forms — The Cotangent Bundle and Tensor Fields

The dual space of the tangent space $T_p M$ is called the **cotangent space** $T_p^* M$. An element $\omega_p \in T_p^* M$ is a linear map $\omega_p: T_p M \to \mathbb{R}$ that eats tangent vectors and returns a real number—a **1-form**. Defining $dx$ in Chapter 1 as "the row vector that extracts the $x$ component from a displacement vector" was precisely an embodiment of this duality.

> <strong>Note</strong> (correspondence with the main text) This is a restatement of the promise in Chapter 1 that $dx = \begin{pmatrix}1&0&0\end{pmatrix}$, now as the component representation of the cotangent basis $dx^1|_p$ in standard Cartesian coordinates. In Chapter 1 we suppressed dependence on the point $p$, but in manifold theory we treat these as objects belonging to the cotangent space $T_p^* M$ at each point.

For local coordinates $x^i$, define $dx^i|_p \in T_p^* M$ by $dx^i|_p(\partial/\partial x^j|_p) = \delta^i_j$; then $\{dx^i|_p\}$ is the dual basis to $\{\partial/\partial x^i|_p\}$ of $T_p^* M$. Any 1-form $\omega$ can be expanded locally as $\omega = \sum_i \omega_i\,dx^i$.

Extending this $k$-fold gives **$k$-forms**. A $k$-form on a manifold is a section that smoothly assigns to each point $p$ an element of $\Lambda^k T_p^* M$. At each point it is an alternating multilinear map

$$\omega_p: \underbrace{T_p M \times \cdots \times T_p M}_{k\ \text{ copies}} \to \mathbb{R}$$

whose components vary smoothly in local coordinates. The wedge product $\wedge$ is defined as the operation that takes the signed sum over all permutations of the arguments of two forms. The wedge product introduced in Chapter 2 of this book as component calculation for antisymmetric matrices is reproduced naturally under this abstract definition.

<strong>Pullback</strong> is also generalized to maps between manifolds. For a smooth map $f: M \to N$, the pullback $f^*\omega$ of a $k$-form $\omega$ on $N$ is a $k$-form on $M$ defined by

$$(f^*\omega)_p(v_1, \dots, v_k) = \omega_{f(p)}(df_p(v_1), \dots, df_p(v_k))$$

Here $df_p: T_p M \to T_{f(p)} N$ is the differential (derivative map) of $f$. The pullback computed in Chapter 4 as the Jacobian of a coordinate change agrees, in local coordinates, with this general formula when $f$ is the coordinate change between charts.

The notation this book has used consistently—"$dx$ is a row vector"—is in the standard language of manifold theory nothing but the fact that the $dx^i$ are a basis of the cotangent space. When we write $\omega = \sum_i \omega_i\,dx^i$, the coefficients $\omega_i$ are in this book's language "the $i$th component of the row vector," and in manifold language "the component of the 1-form with respect to local coordinates." The calculation $\omega(v) = \sum_i \omega_i\,dx^i(v) = \sum_i \omega_i v^i$ corresponds completely to the matrix product of Chapter 1, $\begin{pmatrix}\omega_1&\omega_2&\omega_3\end{pmatrix}\begin{pmatrix}v^1\\v^2\\v^3\end{pmatrix}$.

This duality extends to higher-degree forms. Representing $k$-forms by matrices in Chapter 2 ($k=1$ as row vectors, $k=2$ as antisymmetric matrices, $k=3$ as antisymmetric third-order tensors) is nothing but the component representation of $k$-forms as alternating multilinear maps. When we handled $4\times4\times4$ slice matrices in Appendix E, we were already practicing component calculation for 3-forms on a manifold.

#### 11.1.4 Exterior Derivative $d$ — What Does Not Change on a Manifold

The exterior derivative $d$ is one of the few differential operators that can be defined on a manifold **without using the metric at all**. For a $k$-form $\omega$, $d\omega$ is a $(k+1)$-form, and its definition agrees completely with what we learned in Chapter 5 as a combination of partial derivatives and the wedge product.

The exterior derivative $d$ is a linear operator from $\Omega^k(M)$ to $\Omega^{k+1}(M)$; on functions it gives the ordinary total differential, it satisfies the graded Leibniz rule, and in local coordinates it is given by partial derivatives and the wedge product. For this operator, $d^2 = 0$ holds. The metric appears nowhere. Curved or flat, we can use the same computational rules for $d$ that we grew familiar with in this book.

This universality is the greatest weapon of differential forms, and it is also the reason **Stokes' theorem**

$$\int_M d\omega = \int_{\partial M} \omega$$

holds for an oriented $n$-dimensional manifold $M$ and an $(n-1)$-form satisfying appropriate smoothness and support conditions. What we met in Chapter 8 as the "unified Stokes theorem" was the special case of this general formula ($M \subset \mathbb{R}^3$, $n \le 3$).

#### 11.1.5 Metric and Hodge Star — What Changes Point by Point

Whereas $d$ is universal, $\ast$ is not. A **Riemannian metric** $g$ is a second-order covariant tensor field that smoothly assigns to each point $p \in M$ a positive definite inner product $g_p: T_p M \times T_p M \to \mathbb{R}$ on the tangent space. In local coordinates we can write

$$g = \sum_i\sum_j g_{ij}(x)\,dx^i \otimes dx^j$$

and $g_{ij}(x)$ are functions of position. In this book we have written the matrix whose entries are $g_{ij}$ as $\mathbf{g}$. In Cartesian coordinates on $\mathbb{R}^3$, $\mathbf{g}$ is the identity matrix; in Minkowski spacetime it is a constant diagonal matrix with entries $(-1,1,1,1)$; on a general manifold, $\mathbf{g}(x)$ differs from point to point.

On an oriented Riemannian manifold, the metric determines a **volume form** $\mathrm{vol}_g = \sqrt{\det g}\;dx^1 \wedge \cdots \wedge dx^n$ (for a pseudo-Riemannian metric, $\sqrt{|\det g|}$ appears according to convention), and using this we define the **Hodge star operator**

$$\ast: \Omega^k(M) \to \Omega^{n-k}(M)$$

The defining equation $\omega \wedge \ast\eta = \langle\omega,\eta\rangle_g\,\mathrm{vol}_g$ explicitly involves $g$. If $\mathbf{g}(x)$ is a function of position, the dictionary for $\ast$ differs point by point—we must repeat at each point the procedure of "building the $\mathbf{g} \to \ast$ dictionary" practiced in Chapter 9. Similar construction is possible for a pseudo-Riemannian metric, but one must watch sign conventions.

This asymmetry between $d$ and $\ast$—$d$ universal, $\ast$ metric-dependent—is precisely the structure toward which Burke's "metric deferral" ultimately points. In general relativity, the metric $g$ itself is determined dynamically as the solution of Einstein's equations. The electromagnetic field equations $dF = 0$, $d(\ast F) = \mu_0(\ast\mathcal{J})$ can be written in the same form even on curved spacetime if we use the Hodge star determined from the spacetime metric and an appropriate current form.

#### 11.1.6 Integration — Partitions of Unity and Orientability

Integration on manifolds likewise lies on the extension of the Riemann sums from this book. In $\mathbb{R}^n$ we could naively define the integral of an $n$-form $\omega = f\,dx^1 \wedge \cdots \wedge dx^n$ as $\int f\,dx^1 \cdots dx^n$. To integrate an $n$-form on a manifold we must compute local integrals chart by chart and glue them together. What makes this gluing possible is a **partition of unity**—a family of smooth functions associated with a covering family of charts that sum to 1.

Furthermore, for the integral of an $n$-form on a manifold not to depend on the choice of coordinates, the manifold must be **orientable**. Assuming throughout this book the right-handed system $(x,y,z)$ amounted to fixing an orientation on $\mathbb{R}^3$. On a non-orientable manifold such as the Möbius strip, a global volume form cannot be defined.

Once integration theory on manifolds is in place, under appropriate smoothness and support conditions, Stokes' theorem $\int_M d\omega = \int_{\partial M} \omega$ holds for an oriented $n$-dimensional manifold and an $(n-1)$-form on it. The unified Stokes theorem our journey reached was an application of this general framework to $n \le 3$.

#### 11.1.7 Connections and Curvature — In a Word

The additional structure needed to "parallel transport" vector fields on a manifold is a **connection**, or **covariant derivative** $\nabla$. Once a connection is given, the **curvature tensor** $R$ measuring the degree of bending is defined. In general relativity, the curvature obtained from the Levi-Civita connection (the unique connection compatible with the metric and torsion-free) describes the gravity of spacetime.

In the language of differential forms, curvature appears as a **curvature 2-form** $\Omega$, and structures such as the Bianchi identity $D\Omega = 0$ ($\Omega$ is closed under the exterior covariant derivative) arise. Beyond this point I leave matters to specialist texts such as Flanders and Burke.

#### 11.1.8 Correspondence with This Book

Let us collect in one table where the concepts of this book sit in manifold theory.

| This book | Manifold theory |
|------|---------|
| $dx$ is a row vector (Chapter 1) | $dx^i$ is a basis of the cotangent space $T_p^*M$ |
| $dx(v) = v_x$ (Chapter 1) | Dual pairing $\langle\omega, v\rangle$ of a 1-form and a tangent vector |
| Wedge product as antisymmetric matrix representation (Chapter 2) | Component representation of a $k$-form as an alternating multilinear map |
| Pullback = recalibrating the measuring device (Chapter 4) | Pullback $f^*\omega$ of a $k$-form under a smooth map |
| Partial derivatives + wedge product for $d$ (Chapter 5) | Exterior derivative $d$ (no metric needed on a manifold) |
| $\mathbf{g} = J^T J$ (Chapter 6) | A concrete example of a metric induced from coordinate change or embedding in Euclidean space |
| Dictionary for $\ast$ (Chapters 6, 9) | Hodge star $\ast: \Omega^k(M) \to \Omega^{n-k}(M)$ (metric-dependent) |
| Unified Stokes theorem (Chapter 8) | $\int_M d\omega = \int_{\partial M} \omega$ (general dimension) |
| $dF=0$, $d(\ast F)=\mu_0(\ast\mathcal{J})$ (Chapter 10) | On curved spacetime as well, the same form if we use the Hodge star from the spacetime metric and an appropriate current form |
| $4\times4\times4$ slices in Appendix E (Chapter 10) | Component calculation for a 3-form on a 4-dimensional manifold |


# Chapter 12: The True Nabla — Clifford, Pauli, Dirac, and Hamilton

# Chapter 12: The True Nabla — Clifford, Pauli, Dirac, and Hamilton

### §12.0 Combining Two Equations into One

In a note within Chapter 10, we actually wrote something like this—"Why two equations? Can we not combine $dF=0$ and $d(\ast F)=\mu_0(\ast\mathcal{J})$ into one?"

We can. And quite easily. Bring out the imaginary unit $i$, and they collapse into a single line of complex equations. In this chapter we first look at that "trick," and then move on to the more unified viewpoint beyond it—Pauli matrices and the Dirac operator.

> <strong>Note</strong> (the position of this chapter) This chapter is an advanced supplement and lies off the main line of the book. Chapter 9 completed the rewrite of vector analysis, and Chapter 10 finished the matrix expansion of Maxwell's equations. Here we do not intend to write a textbook of rigorous geometric algebra (Clifford algebra). The purpose is to see, as an entry point to calculation, how grad, curl, and div—which this book has dismantled—are integrated again into a single operator inside Pauli matrices and the Dirac operator.


### §12.2 Pauli Matrices — The Magic of Adding Different Degrees

There is, in fact, a "magic box." Tools that physicists discovered for quantum mechanics can be used directly as that box. The Pauli matrices. More precisely, what we look at here is the Clifford algebra of three-dimensional Euclidean space, represented by Pauli matrices. Not differential forms themselves, but each degree ($0$ through $3$) is matched (under this chapter's convention) to basis elements inside this algebra.

#### 12.2.1 Definition and Multiplication of Pauli Matrices

The Pauli matrices $\sigma_1, \sigma_2, \sigma_3$ are the following $2\times2$ matrices.

$$
\sigma_1 = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix},\quad
\sigma_2 = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix},\quad
\sigma_3 = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}
$$

Let us examine their multiplication rules. Individually, $\sigma_1^2 = \sigma_2^2 = \sigma_3^2 = I$ (the identity matrix), and for distinct indices **anticommutativity** holds: $\sigma_1\sigma_2 = -\sigma_2\sigma_1$. There are nine products in all.

$$
\begin{aligned}
\sigma_1\sigma_1 = I,\quad &\sigma_1\sigma_2 = i\sigma_3,\quad &\sigma_1\sigma_3 = -i\sigma_2 \\
\sigma_2\sigma_1 = -i\sigma_3,\quad &\sigma_2\sigma_2 = I,\quad &\sigma_2\sigma_3 = i\sigma_1 \\
\sigma_3\sigma_1 = i\sigma_2,\quad &\sigma_3\sigma_2 = -i\sigma_1,\quad &\sigma_3\sigma_3 = I
\end{aligned}
$$

Let us decompose these nine products into symmetric and antisymmetric parts—the same idea as when we introduced the wedge product $\wedge$ by antisymmetrization in Chapter 2.

For equal indices ($\sigma_1\sigma_1$, $\sigma_2\sigma_2$, $\sigma_3\sigma_3$), the symmetric part is $I$ and the antisymmetric part is $0$. For distinct indices, for example with $\sigma_1\sigma_2 = i\sigma_3$,

$$
\frac{1}{2}(\sigma_1\sigma_2 + \sigma_2\sigma_1) = \frac{i\sigma_3 + (-i\sigma_3)}{2} = 0,\qquad
\frac{1}{2}(\sigma_1\sigma_2 - \sigma_2\sigma_1) = \frac{i\sigma_3 - (-i\sigma_3)}{2} = i\sigma_3
$$

and similarly, products with distinct indices are purely antisymmetric. The symmetric part is $I$ only when the indices match; otherwise it is $0$—nothing other than the metric introduced in Chapter 6 (the identity matrix in Cartesian coordinates) appearing as the symmetric part of Pauli-matrix products. The antisymmetric part flips sign when indices are swapped—exactly the same structure as the wedge product in Chapter 2, $dx\wedge dy = -dy\wedge dx$.

Pauli-matrix products always decompose into "inner product (symmetric part) $+$ wedge product (antisymmetric part)." That single fact is the source of all the magic of Pauli matrices.

#### 12.2.2 Writing Vectors with Pauli Matrices

Let us represent a three-dimensional vector $\mathbf{v} = (v_1, v_2, v_3)$ with Pauli matrices.

$$V = v_1\sigma_1 + v_2\sigma_2 + v_3\sigma_3 = \mathbf{v}\!\cdot\!\bm{\sigma}$$

Compute the product of the Pauli matrices $V = \mathbf{v}\!\cdot\!\bm{\sigma}$, $W = \mathbf{w}\!\cdot\!\bm{\sigma}$ corresponding to two vectors $\mathbf{v}, \mathbf{w}$.

$$
\begin{aligned}
VW &= (v_1\sigma_1 + v_2\sigma_2 + v_3\sigma_3)(w_1\sigma_1 + w_2\sigma_2 + w_3\sigma_3) \\[4pt]
&= v_1w_1\sigma_1\sigma_1 + v_1w_2\sigma_1\sigma_2 + v_1w_3\sigma_1\sigma_3 \\
&\quad + v_2w_1\sigma_2\sigma_1 + v_2w_2\sigma_2\sigma_2 + v_2w_3\sigma_2\sigma_3 \\
&\quad + v_3w_1\sigma_3\sigma_1 + v_3w_2\sigma_3\sigma_2 + v_3w_3\sigma_3\sigma_3
\end{aligned}
$$

Apply the nine products to each term. Writing only the nonzero replacements,

$$
\sigma_1\sigma_1 = I,\quad \sigma_2\sigma_2 = I,\quad \sigma_3\sigma_3 = I,\quad
\sigma_1\sigma_2 = i\sigma_3,\quad \sigma_2\sigma_3 = i\sigma_1,\quad \sigma_3\sigma_1 = i\sigma_2
$$

and the nine obtained by reversing the indices: $\sigma_2\sigma_1 = -i\sigma_3$, $\sigma_3\sigma_2 = -i\sigma_1$, $\sigma_1\sigma_3 = -i\sigma_2$. Collect the coefficients of $I$ (symmetric part = inner product) and of $\sigma_1,\sigma_2,\sigma_3$ (antisymmetric part = wedge product).

$$
\begin{aligned}
\text{Coefficient of }I\text{ (inner product)} &: v_1w_1 + v_2w_2 + v_3w_3 \;=\; \mathbf{v}\!\cdot\!\mathbf{w} \\
\text{Coefficient of }\sigma_1\text{ ($\wedge$)} &: i\,(v_2w_3 - v_3w_2) \\
\text{Coefficient of }\sigma_2\text{ ($\wedge$)} &: i\,(v_3w_1 - v_1w_3) \\
\text{Coefficient of }\sigma_3\text{ ($\wedge$)} &: i\,(v_1w_2 - v_2w_1)
\end{aligned}
$$

Under the three-dimensional orientation convention used throughout this book, the expressions in parentheses for the coefficients of $\sigma_1,\sigma_2,\sigma_3$ are the same components that are read back as the cross product $\mathbf{v}\times\mathbf{w}$—equivalently, the components of the wedge product $\mathbf{v}\wedge\mathbf{w}$ defined in Chapter 2. Therefore

$$VW = (\mathbf{v}\!\cdot\!\mathbf{w})\,I \;+\; i\,(\mathbf{v}\times\mathbf{w})\!\cdot\!\bm{\sigma}$$

and the result takes the form inner product $+$ wedge product. Inner product and cross product **emerge simultaneously from a single product $VW$**.

That is the true nature of the "magic box." More precisely, what we are looking at is the Clifford algebra of three-dimensional Euclidean space, represented by Pauli matrices. Its product **at once** produces the inner product (a scalar corresponding to a $0$-form) and the cross product (a wedge product corresponding to a $2$-form). What in ordinary differential forms belonged to separate degrees coexists in this matrix representation as a single $2\times2$ matrix.

> <strong>Note</strong> (why $2\times2$?) Representing a vector by a $2\times2$ matrix may seem odd. But to express both inner and wedge products in one product requires at least a noncommutative algebra, and the minimal realization is $2\times2$ complex matrices. In this book's style, one may think of it as packing two objects of different degree—a $1$-form (row vector $1\times3$) and a $2$-form (antisymmetric $3\times3$ matrix)—into a single $2\times2$ matrix.

#### 12.2.3 Mixing in Scalars Too

We have now seen that vectors ($1$-forms) and wedge products ($2$-forms) appear together from a single calculation $VW$. Take one step further and mix scalars ($0$-forms) themselves into the same algebra.

The most general $2\times2$ matrix expressible as a linear combination of Pauli matrices has the form

$$\psi = \varphi\,I + A_1\sigma_1 + A_2\sigma_2 + A_3\sigma_3$$

Here $\varphi$ is a scalar ($0$-form) and $A_1,A_2,A_3$ are vector components ($1$-form). Furthermore, multiplying $\psi$ on the left by $\sigma_i$ brings in terms $i\sigma_k$ corresponding to $2$-forms. Under this chapter's convention, basis elements for degrees $0,1,2,3$ can all be matched inside this algebra.

> <strong>Note</strong> (what has become possible) In differential forms one can formally arrange forms of different degrees as a direct sum. But to treat inner product (contraction) and outer product (antisymmetrization) **simultaneously as one product**, the ordinary wedge product alone is not enough. In the Pauli-matrix algebra, they separate and coexist naturally inside a single product $VW$. That is the core of geometric algebra.

> <strong>Note</strong> (matching all degrees) Let us organize the degree correspondence under this chapter's convention. $I$ corresponds to $0$-forms (scalars), $\sigma_1,\sigma_2,\sigma_3$ to $1$-forms (vectors), $i\sigma_1,i\sigma_2,i\sigma_3$ to $2$-forms (bivectors), and $iI$ to $3$-forms (pseudoscalar). This is not identification with differential forms themselves, but a convention for matching basis elements of each degree inside the matrix representation of the three-dimensional Euclidean Clifford algebra. The most general element has the form $\psi = aI + \mathbf{v}\!\cdot\!\bm{\sigma} + i\,\mathbf{w}\!\cdot\!\bm{\sigma} + ibI$, containing all four degrees with complex coefficients.

> <strong>Note</strong> (quaternions—a magic box that already existed) In fact the idea of "mixing scalars and vectors into one number" is much older than Pauli matrices. Older than matrix algebra. The **quaternion** $q = a + bi + cj + dk$ discovered by Hamilton in 1843 is exactly that. Maxwell used quaternionic language in his formulation of electromagnetism. Later, Gibbs and Heaviside **separated** the scalar and vector parts from quaternions, and modern vector analysis (inner and cross products) was born. From this book's viewpoint, Pauli matrices also look like a tool for viewing, in the context of quantum mechanics, a structure once split into inner and outer products again as a single noncommutative product.

> <strong>Note</strong> (vector analysis in the age before matrices) When Gibbs and Heaviside organized vector analysis in the 1880s, matrix algebra was not yet common. Determinants existed, but the algebra of matrices itself—noncommutativity of products, eigenvalues, the unified understanding as linear transformations—was not yet the common working language of physicists. Gibbs invented his own notation, the **dyad** $\mathbf{a}\mathbf{b}$, to represent linear transformations; this corresponds to the modern matrix $\mathbf{a}\mathbf{b}^T$. From this book's viewpoint, vector analysis can be viewed as having differentiated from quaternionic unification into tools of inner product, outer product, and dyads. That this book, titled "Dismantling Nabla," decomposed $\nabla$ into $d$ and $\ast$ and in the final chapter shows re-unification via Pauli matrices also has the meaning of revisiting this history of separation and reunification from another angle.

> <strong>Note</strong> (when matrix algebra was not the standard language of physicists) Incidentally, that matrix algebra was not the standard language of physicists shows up clearly in matrix mechanics in 1925. Heisenberg himself did not initially know that his calculations were noncommutative matrix products; it was Born who read them as matrices.

---

### §12.3 The Dirac Operator and the "True Nabla"

#### 12.3.1 $\bm{\sigma}\!\cdot\!\nabla$ — A Unified Differential Operator

Combine Pauli matrices with nabla $\nabla = (\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z})$ and define the operator

$$D = \sigma_1\frac{\partial}{\partial x} + \sigma_2\frac{\partial}{\partial y} + \sigma_3\frac{\partial}{\partial z} = \bm{\sigma}\!\cdot\!\nabla$$

$D$ is a differential operator in the form of a $2\times2$ matrix. Apply it to a scalar field $\varphi$.

$$D\varphi = \sigma_1\frac{\partial\varphi}{\partial x} + \sigma_2\frac{\partial\varphi}{\partial y} + \sigma_3\frac{\partial\varphi}{\partial z} = (\nabla\varphi)\!\cdot\!\bm{\sigma}$$

This is $\mathrm{grad}\,\varphi$ written with Pauli matrices.

Next, write a vector field $\mathbf{A} = (A_1, A_2, A_3)$ as a Pauli matrix $A = \mathbf{A}\!\cdot\!\bm{\sigma}$ and apply $D$. Recall the product formula from §12.2.2.

$$
\begin{aligned}
D A &= (\sigma_1\tfrac{\partial}{\partial x} + \sigma_2\tfrac{\partial}{\partial y} + \sigma_3\tfrac{\partial}{\partial z})(A_1\sigma_1 + A_2\sigma_2 + A_3\sigma_3) \\[4pt]
&= \tfrac{\partial A_1}{\partial x}\,\sigma_1\sigma_1 + \tfrac{\partial A_2}{\partial x}\,\sigma_1\sigma_2 + \tfrac{\partial A_3}{\partial x}\,\sigma_1\sigma_3 \\
&\quad + \tfrac{\partial A_1}{\partial y}\,\sigma_2\sigma_1 + \tfrac{\partial A_2}{\partial y}\,\sigma_2\sigma_2 + \tfrac{\partial A_3}{\partial y}\,\sigma_2\sigma_3 \\
&\quad + \tfrac{\partial A_1}{\partial z}\,\sigma_3\sigma_1 + \tfrac{\partial A_2}{\partial z}\,\sigma_3\sigma_2 + \tfrac{\partial A_3}{\partial z}\,\sigma_3\sigma_3
\end{aligned}
$$

Apply the same replacements $\sigma_i\sigma_j$ as in §12.2.2 to the nine terms, and collect the coefficient of $I$ (inner product = divergence) and the coefficients of $\sigma_1,\sigma_2,\sigma_3$ (wedge product = curl).

$$
\begin{aligned}
\text{Coefficient of }I &: \frac{\partial A_1}{\partial x} + \frac{\partial A_2}{\partial y} + \frac{\partial A_3}{\partial z} = \mathrm{div}\,\mathbf{A} \\
\text{Coefficient of }\sigma_1\text{ ($\wedge$)} &: i\,\left(\frac{\partial A_3}{\partial y} - \frac{\partial A_2}{\partial z}\right) \\
\text{Coefficient of }\sigma_2\text{ ($\wedge$)} &: i\,\left(\frac{\partial A_1}{\partial z} - \frac{\partial A_3}{\partial x}\right) \\
\text{Coefficient of }\sigma_3\text{ ($\wedge$)} &: i\,\left(\frac{\partial A_2}{\partial x} - \frac{\partial A_1}{\partial y}\right)
\end{aligned}
$$

The expressions in parentheses for the coefficients of $\sigma_k$ are the components of $\mathrm{curl}\,\mathbf{A}$—equivalently, under the three-dimensional dictionary, the components of the $2$-form obtained by applying $d$ to the corresponding $1$-form. Therefore

$$D(\mathbf{A}\!\cdot\!\bm{\sigma}) = (\mathrm{div}\,\mathbf{A})\,I \;+\; i\,(\mathrm{curl}\,\mathbf{A})\!\cdot\!\bm{\sigma}$$

**A single operator $D$ simultaneously yields $\mathrm{grad}$ ($D\varphi$), $\mathrm{div}$ (the real part of $DA$), and $\mathrm{curl}$ (the imaginary part of $DA$).** This is none other than one endpoint of the journey on which we deepened our understanding by decomposing $\nabla$ into $d$ and $\ast$—**unification**.

> <strong>Note</strong> (in the language of $d$ and $\ast$) $D$ can also be expressed in this book's language. Up to sign conventions, $D$ can be understood as an operator combining $d$ (raising degree) and $\ast d\ast$ (lowering degree). The latter is called the **codifferential** $\delta$, defined by $\delta = \pm\ast d\ast$ (the sign depends on dimension and degree). Here we do not enter the exact signs; it is enough to keep in mind the structure $D \sim d + \delta$. $d$ raises degree and $\delta$ lowers it—the sum $D$ of these two binds grad, curl, and div into one operator.

#### 12.3.2 $D^2$ — The Laplacian

What happens if we apply $D$ twice?

$$D^2 = (\bm{\sigma}\!\cdot\!\nabla)(\bm{\sigma}\!\cdot\!\nabla) = (\sigma_1\frac{\partial}{\partial x} + \sigma_2\frac{\partial}{\partial y} + \sigma_3\frac{\partial}{\partial z})(\sigma_1\frac{\partial}{\partial x} + \sigma_2\frac{\partial}{\partial y} + \sigma_3\frac{\partial}{\partial z})$$

Expand into nine terms.

$$
\begin{aligned}
D^2 &= \sigma_1\sigma_1\,\frac{\partial^2}{\partial x^2} + \sigma_1\sigma_2\,\frac{\partial^2}{\partial x\partial y} + \sigma_1\sigma_3\,\frac{\partial^2}{\partial x\partial z} \\
&\quad + \sigma_2\sigma_1\,\frac{\partial^2}{\partial y\partial x} + \sigma_2\sigma_2\,\frac{\partial^2}{\partial y^2} + \sigma_2\sigma_3\,\frac{\partial^2}{\partial y\partial z} \\
&\quad + \sigma_3\sigma_1\,\frac{\partial^2}{\partial z\partial x} + \sigma_3\sigma_2\,\frac{\partial^2}{\partial z\partial y} + \sigma_3\sigma_3\,\frac{\partial^2}{\partial z^2}
\end{aligned}
$$

Terms containing the antisymmetric part of $\sigma_i\sigma_j$ (terms with $i\neq j$, such as $\sigma_1\sigma_2 = i\sigma_3$) cancel in pairs of opposite sign because of the commutativity of partial derivatives, $\frac{\partial^2}{\partial x\partial y} = \frac{\partial^2}{\partial y\partial x}$. For example, $\sigma_1\sigma_2\,\frac{\partial^2}{\partial x\partial y}$ and $\sigma_2\sigma_1\,\frac{\partial^2}{\partial y\partial x}$ sum to zero because $\sigma_2\sigma_1 = -\sigma_1\sigma_2$ and $\frac{\partial^2}{\partial y\partial x} = \frac{\partial^2}{\partial x\partial y}$. What remains are only the diagonal terms with $\sigma_i\sigma_i = I$.

$$D^2 = \left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}\right)I = \nabla^2 I$$

$D^2$ is the Laplacian itself. $D$ is the "square root" of the Laplacian. That fact—taking a square root of a differential operator—was the core insight when Dirac derived the equation for the electron in relativistic quantum mechanics.

#### 12.3.3 Unifying Maxwell — Revisited

In §12.1 we unified Maxwell's equations in four dimensions via $F + i\ast F$. With $D$, the same thing can be written using only three-dimensional language.

Bundle the electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$ into a single complex vector. This is called the **Riemann–Silberstein vector**.

$$\mathbf{F} = \mathbf{E} + i\mathbf{B}$$

In Pauli matrices, $F = \mathbf{E}\!\cdot\!\bm{\sigma} + i\,\mathbf{B}\!\cdot\!\bm{\sigma}$. $F$ is a purely complex Pauli vector with no scalar part. Apply the operator $D + \frac{\partial}{\partial t}$ including the time derivative.

$$(D + \frac{\partial}{\partial t})F = (\bm{\sigma}\!\cdot\!\nabla + \frac{\partial}{\partial t})(\mathbf{E}\!\cdot\!\bm{\sigma} + i\,\mathbf{B}\!\cdot\!\bm{\sigma})$$

Apply the formula for $D(\mathbf{A}\!\cdot\!\bm{\sigma})$ from §12.3.1 to both $\mathbf{E}$ and $\mathbf{B}$.

$$
\begin{aligned}
(D + \frac{\partial}{\partial t})F &= (\mathrm{div}\,\mathbf{E})\,I + i\,(\mathrm{curl}\,\mathbf{E})\!\cdot\!\bm{\sigma} + \frac{\partial}{\partial t}\mathbf{E}\!\cdot\!\bm{\sigma} \\
&\quad + i\,(\mathrm{div}\,\mathbf{B})\,I - (\mathrm{curl}\,\mathbf{B})\!\cdot\!\bm{\sigma} + i\,\frac{\partial}{\partial t}\mathbf{B}\!\cdot\!\bm{\sigma}
\end{aligned}
$$

Organize by real and imaginary parts, and by $I$ (scalar) and $\bm{\sigma}$ (vector) components.

$$
\begin{aligned}
\text{Real}\cdot I &: \mathrm{div}\,\mathbf{E} - 0 \\
\text{Real}\cdot\bm{\sigma} &: \frac{\partial}{\partial t}\mathbf{E} - \mathrm{curl}\,\mathbf{B} \\
\text{Imag}\cdot I &: 0 + \mathrm{div}\,\mathbf{B} \\
\text{Imag}\cdot\bm{\sigma} &: \mathrm{curl}\,\mathbf{E} + \frac{\partial}{\partial t}\mathbf{B}
\end{aligned}
$$

Setting these equal to zero yields all four vacuum Maxwell equations. When current $\mathbf{J}$ and charge $\rho_{\mathrm e}$ are present, under the same normalization as Chapter 10 the right-hand side can be set to $\rho_{\mathrm e}/\varepsilon_0 - \mu_0 c \mathbf{J}\!\cdot\!\bm{\sigma}$, and Maxwell's equations with sources collapse into one line.

$$(D + \frac{\partial}{\partial t})F = \frac{\rho_{\mathrm e}}{\varepsilon_0} - \mu_0 c \mathbf{J}\!\cdot\!\bm{\sigma}$$

> <strong>Note</strong> (normalization and signs in Chapter 12)
> Here $t, \mathbf{B}, \rho_{\mathrm e}, \mathbf{J}$ are normalized quantities as in Chapter 10 §10.1–10.5. The coefficients and signs of the source terms on the right-hand side are chosen to be consistent with the expansion of $d(\ast F) = \mu_0(\ast\mathcal{J})$ from Chapter 10.

The two equations $dF=0$ and $d(\ast F)=\mu_0(\ast\mathcal{J})$ have been unified into a single complex equation in front of $D$. Whereas the four-dimensional trick of §12.1 depended on a special dimension, here the unified operator $D$ itself achieves the unification.

#### 12.3.4 $\cancel{\partial} F = J$ — The Dirac Operator in Four-Dimensional Spacetime

In §12.3.3, $(D + \frac{\partial}{\partial t})F = \rho_{\mathrm e} + \mathbf{J}\!\cdot\!\bm{\sigma}$ still separates time and space. That is because it was built on the three-dimensional Pauli matrices $\sigma_1,\sigma_2,\sigma_3$. If we treat four-dimensional spacetime from the start, even this separation disappears.

Extending Pauli matrices to $4\times4$ gives the **gamma matrices** $\gamma^0,\gamma^1,\gamma^2,\gamma^3$. They satisfy anticommutativity $\gamma^\mu\gamma^\nu + \gamma^\nu\gamma^\mu = 2g^{\mu\nu}I$ ($g^{\mu\nu}$ is the Minkowski metric). The signs of the real coefficients in this equation depend on the chosen metric signature and index conventions. As in Chapter 10, this chapter adopts the convention with spacetime metric signature $(-,+,+,+)$. Using these gamma matrices, define the four-dimensional Dirac operator by

$$\cancel{\partial} = \gamma^0\frac{\partial}{\partial t} + \gamma^1\frac{\partial}{\partial x} + \gamma^2\frac{\partial}{\partial y} + \gamma^3\frac{\partial}{\partial z}$$

Identifying the electromagnetic field $F$ from Chapter 10 ($4\times4$ antisymmetric matrix) with an expansion in gamma-matrix wedge products $\gamma^\mu\!\wedge\!\gamma^\nu$, Maxwell's equations consolidate into the single line

$$\cancel{\partial} F = J$$

That is the standard geometric-algebra picture. $F$ is the electromagnetic field and $J$ is the four-current (expanded in $\gamma^\mu$). In vacuum, $\cancel{\partial} F = 0$.

> <strong>Note</strong> (on the product $\cancel{\partial} F$) The product here is not ordinary matrix multiplication but the geometric-algebra product generated by gamma matrices. The antisymmetric matrix $F$ from Chapter 10 is reinterpreted here as a $2$-vector expanded in $\gamma^\mu\!\wedge\!\gamma^\nu$. Details are left to textbooks on geometric algebra; it is enough to think that the four-dimensional version of $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$ (§12.2.1) holds here as well.

Both §12.1's $F + i\ast F$ and §12.3.3's $(D + \frac{\partial}{\partial t})F$ are absorbed into this single line. That is the farthest landscape on the journey that began with dismantling $\nabla$. The operator Dirac discovered in 1928 to derive the equation for the electron is the core of **geometric algebra**, which describes the geometry of spacetime and physical laws in one algebra; see Doran & Lasenby's *Geometric Algebra for Physicists* for details.

### §12.4 The Operator $\nabla$

Now let us return to the first question. What was $\nabla$?

In vector analysis, $\nabla$ was introduced as a formal vector of partial derivatives and was a mysterious symbol with three faces: grad, curl, and div. This book **dismantled** it into $d$ and $\ast$, thereby revealing what each operator truly is.

And now, tracing this in reverse, the scattered parts $d$ and $\ast$ are **unified** in geometric algebra as the three-dimensional Dirac operator $D = \bm{\sigma}\!\cdot\!\nabla$, and further its four-dimensional version, the Dirac operator $\cancel{\partial}$, gives the ultimate Maxwell equation $\cancel{\partial} F = J$.

By the way, in the context of geometric algebra this operator is not necessarily written $\cancel{\partial}$. Rather, this kind of vector differential operator is written

$$
\nabla
$$

# Afterword: How *Unmasking Div, Grad, and Curl* Was Born

# Afterword: How *Unmasking Div, Grad, and Curl* Was Born

To you, reader, who have finished this long journey—first, my heartfelt respect.

As you close this book, let me share a little of the backstage story of how this peculiar, somewhat forceful *Unmasking Div, Grad, and Curl* came to be.

It began with a bitter memory of my own. Like many students of physics, I nearly drowned in the quagmire of "vector analysis." Faced with $\mathrm{curl}$ and $\mathrm{div}$ in cylindrical or spherical coordinates, the question "why does it take this form?" was silenced by pressure to "just memorize the formulas." I had heard that differential forms could be the special remedy, but the axiomatic approach of mathematics books was too abstract for me then.

"Is there no slightly sneaky 'silver bullet' that would solve this indigestion in one shot?"—As I wondered, the first breakthrough came. This is personal: at the time I was quite absorbed in quantum mechanics and had grown accustomed to Dirac's bra–ket notation. The feeling of laying state vectors (column vectors) on their sides as dual vectors (row vectors) and computing naturally as matrix products—that sensation.

What mattered to me, however, was not that bra–ket notation was "convenient notation for inner products." Quite the opposite. A bra is originally a dual vector that eats a ket. The dual pairing in which a row vector eats a column vector and the inner product that compares two vectors via the metric are, in principle, different operations. Yet in the notation of physical mathematics they often appear with similar faces, and the distinction collapses before one notices. Dirac himself, in his justly famous book, writes that one "set[s] up a second set of vectors, which mathematicians call the dual vectors." Even so, in education a bra is often treated like "the left half of an inner-product symbol." I felt indignation about that at the time.

Around then I wondered: what if I applied this sensation directly to the classical $dx,dy,dz$ of three-dimensional Euclidean space? When I thought that, the first core of this book was fixed. Redefine the $dx$ at the tail of the integral sign as a "row vector (matrix) that extracts components from a displacement vector," and the abstract idea "function that eats vectors (1-form)" converts instantly into "matrix multiplication" that everyone knows. At least for me as a student, that became the decisive foothold for understanding vector analysis.

This is not an inner product. It is a measuring device that eats displacement vectors. Identification via the metric should come later. For my personal understanding, that was truly the silver bullet. Formulas of vector analysis could all be derived by hand from rules of matrix addition, subtraction, and multiplication.

But that alone was still not enough motive to start writing the book. The second breakthrough came from W. L. Burke's educational philosophy of "putting the metric later and later into the course."

Burke's intent was probably to show structures that hold before length, angle, and inner product are introduced, separated from structures that depend on the metric. The exterior derivative $d$, the wedge product, boundaries, and Stokes-type structure work to a large extent before the metric enters. In general relativity and vector analysis, putting the metric upfront from the start makes the exterior derivative, boundaries, conservation laws, coordinate changes, and metric-dependent conversion via the Hodge star look mixed together. Burke, I think, had a problem consciousness about that quite early.

Of course, this is my own reading. I do not think Burke himself wanted to "separate dual and inner product" the way I do. Still, on the point that introducing the metric in a hurry makes structures that should look separate collapse into one, I strongly sympathized with Burke's concern.

From Dirac I received the feeling "do not collapse dual into inner product." From Burke I received the feeling "if you introduce the metric in a hurry, you stop seeing structures that are visible without it." In my mind these two feelings linked up, and the book settled into the shape: place $dx$ as a measuring device, separate the pullback from the metric, and only then introduce the metric and Hodge star.

Especially important for me was showing that coordinate changes and the pullback can first be treated separately from talk of length and angle. Coordinate change is the demon gate of vector analysis. Pour unit vectors, scale factors, area elements, and the metric in all at once, and you lose sight of what comes from what. This book first treats the pullback as matrix calculation with the Jacobian, then introduces the metric and Hodge star. I decided to turn that order itself into "table-of-contents educational entertainment" that draws readers in.

From Chapter 1 through Chapter 5 we did not formally define the metric and pressed forward with naive intuition about length and area in real space $(x,y,z)$. From a more advanced standpoint one might want to say "area needs a metric," but in the early part of this book we fixed on $xyz$ Cartesian coordinates and deliberately used naive intuition about area and volume wherever the Pythagorean theorem holds. The metric $g = J^T J$ truly becomes necessary when generalizing to coordinate systems with distorted scales like parameter spaces—we derived that fact in a discovery-style way in Chapter 6 through matrix calculation.

Then came the opening of Chapter 6. Joking that "the author is getting bored too," we formally defined the inner product. At the same time we clarified the meaning of the metric $g = J^T J$ and positioned the Hodge star $\ast$ as a "type-conversion adapter linking differential forms and vector analysis." Through this discovery-based construction, the setup was to make readers accept the structure that "$df$ does not depend on the metric, but reading the usual gradient vector, curl, and divergence requires the metric and Hodge star."

Among these ideas, Burke's philosophy of "delaying the metric" and Flanders's physical applications of differential forms are both written in existing English literature. This book claims no mathematical novelty. Only the configuration—defining $dx$ as a matrix and pushing through the whole book with matrix calculation—seems, as far as I know, uncommon in the Western books I have seen. Perhaps those of us trained in East Asian entrance-exam culture are oddly accustomed to symbolic calculation—I joke—but in any case I merely organized something I wrote for myself. For the giants on whose shoulders this book stands, please see the references at the end.

This book is a "survival guide" written for my past self, who stumbled in vector analysis. Having cleared vector analysis and knowing powerful tools such as "dual," "exterior derivative," "pullback," "metric," and "Hodge star $\ast$," and knowing the limits of Cartesian coordinates, you have already opened the door to the next world.

What follows is an extra. Still, before you close the book, there is a conviction I want to state.

This book progressed by dropping differential forms—which look abstract—into matrix calculation as far as possible. Reading $dx$ as a row vector, treating the wedge product as calculation with antisymmetric matrices, and reading the Hodge star as a dictionary built from the metric matrix were all devices for that purpose.

Looking back, this was perhaps not merely my personal shortcut but an attempt to "misuse" algebraic training that science-track students who have gone through serious entrance-exam mathematics already possess at the entrance to university mathematics. Japanese competitive entrance exams, for better or worse, drill students in transforming expressions, substituting letters, tracking parameters, and organizing conditions. Not even calculus is an exception; substitution integrals and parametric representations are typically trained as almost purely algebraic symbol manipulation.

Such training is often excessive and can look like meaningless technique. Rather than lamenting that it is meaningless or an obstacle to abstraction, there is room to use it as an embodied, powerful weapon.

As an expression of that, this book asks readers for quite a lot of hand calculation—mostly not analytic work such as evaluating limits or studying convergence, but algebraic work: rearranging symbols, tracking components, multiplying matrices, expanding wedge products. That is not because I underestimate readers. I expect you can withstand this level of symbol manipulation—or perhaps I am flattering you a little.

University mathematics sometimes jumps to set-theoretic "definitions" too quickly. Abstract definitions have strength; there is still much to learn from Bourbaki-style structural organization. But there should also be a path where one first grasps abstract concepts as concrete operations using the algebraic body one already has. This book tried that path in a rather extreme form. The assertion $dx=(1\ 0\ 0)$ is its symbol.

This book's structure is certainly not the only correct one. It is probably awkward, forceful in places, and from a standard textbook looks like a detour. Even so, if through this book you felt abstract symbols as something you can move with your hands, the book has done its job.

As the author, I sincerely hope that *Unmasking Div, Grad, and Curl* will be a sturdy foothold on your journey in physics and mathematics—keeping the algebraic hands you already have and going higher and farther.

> <strong>Note</strong> (the third breakthrough)
> After Dirac's bra–ket notation and Burke's delay of the metric, this book has a third breakthrough: the arrival of generative AI, that is, LLMs.
>
> The real benefit LLMs brought was not teaching me correct answers. Rather, they gave me the freedom to externalize, compare, and discard the unorganized discomfort, draft explanations, objections, and rephrasings inside me as text again and again. Fragments that might have taken years to shape alone in a notebook could be lined up as drafts, broken apart, and rebuilt. In fact, the time for this book to reach its present form was only a few months. In that sense the LLM was a powerful sparring partner that made writing the book possible.
>
> Even so, this is not a heartwarming story that "thanks to the LLM it was easy to write." On the contrary, left alone an LLM quickly steers the conversation back to standard theory. $dx$ is a cotangent basis. The exterior derivative is the natural operation on a manifold. The Hodge star is fixed by the metric and orientation. Yes, all true. But what I wanted to write was a book that, before going to those correct explanations, traces with matrix calculation and the feel of finite cells why beginners are left behind there.
>
> So while writing I often had to tell the LLM, "Don't go to manifolds yet," "First write $dx=(1\ 0\ 0)$," "First count finite cells," "Don't put the metric in there yet." A strange job where I was supposedly using a convenient tool yet worried I might be writing nonsense myself.
>
> Generative AI produced many drafts and rephrasings. But every sentence that remains in this book was chosen, cut, corrected, and sometimes peeled away from explanations that were too standard by me. If the book has a strange stubbornness about not wanting to return immediately to standard theory, or superfluous meta remarks, that is my habit. And if mathematical errors remain, that too is my responsibility, not the LLM's.

# References (with Comments from the Author)

# References (with Comments from the Author)

This book's peculiar algebraic approach was built by combining the insights of the following pioneers.


<strong>2. David Bachman, *A Geometric Approach to Differential Forms*, Birkhäuser (2nd ed. 2011)</strong>

Comment: A geometric introduction to differential forms. A good book that explains differential forms not from axioms but from geometric intuition such as "measuring shadows." Much of this book's intuition that "$dx$ is a measuring device" comes from Bachman, but here computational closure is prioritized and that intuition is adopted by dropping it into matrix algebra.

---

<strong>3. Harley Flanders, *Differential Forms with Applications to the Physical Sciences*, Dover Publications (1989/1963)</strong>

Comment: A classic of physical-mathematical application. A bible-like masterpiece for applying differential forms to physics. The rigorous operational rules of the exterior derivative $d$ and Hodge star $\ast$ are condensed here. Because it starts from an axiomatic introduction, self-study is somewhat hard for beginners, but readers who finish this book should be able to wield its powerful calculations fully.

---

<strong>4. William L. Burke, *Applied Differential Geometry*, Cambridge University Press (1985)</strong>
<strong>William L. Burke, *Div, Grad, Curl are Dead* (Unfinished Manuscript)</strong>

Comment: The structural pillar of this book—the philosophy of "delaying the metric." The most important literature that fixed the skeleton of this book. Burke advocated the educational philosophy of "putting the metric later and later into the course." This philosophy, which made explicit how much can be said with the exterior derivative $d$ before introducing the metric, supports the book's structure up to the delayed introduction of the metric and Hodge star in Chapter 6.

---

<strong>5. Leonard Susskind & Art Friedman, *Quantum Mechanics: The Theoretical Minimum*, Basic Books (2014)</strong>

Comment: Intuition for matrix representation. The intuition of translating abstract $1$-forms (dual space) into the physicist's mother tongue—"lay column vectors on their sides as row vectors and take matrix products"—was strongly influenced by the operational feel of bra–ket notation in quantum mechanics.

---

<strong>6. Chris Doran & Anthony Lasenby, *Geometric Algebra for Physicists*, Cambridge University Press (2003)</strong>

Comment: One unification beyond this book. An entry to geometric algebra (Clifford algebra) for modern physics. One sees the landscape where "inner product" and "outer product," thoroughly separated in this book, are integrated from the start as a single noncommutative product. Readers who know the pain of separation can feel how powerfully liberating that unification is.

# Appendix: What This Book Did Not Discuss

# Appendix: What This Book Did Not Discuss

This appendix collects likely differences in convention, theoretical limits, or typical reader objections to the book's presentation.

This book is not an axiomatic development of differential forms on general manifolds. It is an educational book that reconstructs vector analysis in three-dimensional Cartesian space through matrix-represented differential forms. Therefore, the notation and order of exposition adopted here do not always match standard mathematics books. Those choices are, in principle, intentional; where needed, Chapter 11 shows connections to standard theory.

> <strong>Note</strong> (the honest version)
> The title of this section is the mild-sounding "What This Book Did Not Discuss," but that is the official line. To be honest, this is a collection of responses to typical criticisms thrown at the book without reading its scope.
>
> If I wrote that plainly, readers I genuinely want to support might get scared and run away. So on the surface I gave it a gentle name.

> <strong>Note</strong> ("I" am angry)
> When I was young, I published a series of SNS posts pointing in the same direction as this book and was harshly criticized by people who presented themselves as knowledgeable about mathematics, including people with institutional standing. Of course, the drafts of that time had many immature points. Even after ten years I still write in this vein—that was surely a post with "momentum." But what I received then was less criticism that read the definitions, checked the scope, and showed how to fix things, and more an attitude of judging an unfinished attempt from a professional position.
>
> That was perhaps a kind of inevitability produced by the engagement structure of SNS and crowd psychology. Publishing writing for free costs more than one imagines; I learned that firsthand.
>
> Even having understood that structure, I am still angry. An attitude that claims rigor while refusing to read what the other person defined and the scope in which they are speaking is, at least in my view, not a mathematical attitude.
>
> Even so, I decided to publish this book for free. In a sense it is also a private act of compensation. On top of that—sorry, this too is a bit of official rhetoric—to protect the readers this book is really for, or rather to protect my own self-respect, I have drawn preventive lines as carefully as I can.
>
> If a definition in this book looks different from a mathematician's textbook, I want you first to read the definition inside this book. Then please distinguish whether there is a real contradiction or whether someone has simply imported notation from a different context. After that, by all means criticize me harshly again. Having read the definitions, I want you to point out my mistakes.

> <strong>Note</strong> (as advanced "gatekeeping")
> As I read mathematics books, I have internalized, at least somewhat, the beauty and strength of abstract orders of definition. The result is that what this book does can suddenly look like nothing more than sophisticated gatekeeping.
>
> If I put that into words it looks like an excuse; if I stay silent it will be misunderstood. Worse, I half believe such criticism myself, so I cannot speak about it well.
>
> Even so, a shortcut is not necessarily bad. A shortcut does not replace a professional system, nor is it merely subordinate to one. It can be a powerful language for treating three-dimensional physical mathematics in the tangible words of matrix representation—at least a system of operations on concrete symbols.
>
> Once again, the first purpose of this book is my own act of compensation. Even so, if a reader takes home one language they can move with their hands, that is an unexpected bonus.

> <strong>Note</strong> (will the day come when I am not fooled?)
> They say one stands at thirty; when I actually reached that milestone, I was still getting angry at formulas rather than standing upright. I have started making dad jokes.


## II. On Methodological Choices and Limits of Application

- <strong>Einstein summation (tensor analysis) would allow the same calculations without bundles of matrices</strong>
  → True. This book explicitly writes out matrix components each time. That lets readers follow where each component comes from and where it acts, without being misled by black-box index manipulation. Readers who finish this book should be able to move fairly quickly to component calculation in tensor analysis by practicing upper/lower index rules and Einstein summation. Correspondence with index notation is shown in Chapter 11.

- <strong>Teaching Clifford algebra (geometric algebra) from the start would unify inner and outer products</strong>
  → This book deliberately chose the path of "separation." Chapters 1–5 build the outer product ($\wedge$), Chapter 6 builds the inner product (metric), and only then §6.3 introduces the Hodge star $\ast$ so readers can feel why unification becomes necessary. Unification via geometric algebra is introduced in Chapter 12.

- <strong>Because the book assumes a constant metric matrix $\mathbf{g}$, won't it break down when space is curved?</strong>
  → Chapter 6 starts from the metric $\mathbf{g}=I$ in $xyz$ physical space and shows that in parameter space $\mathbf{g}=J^T J$ becomes a function of position. Generalization to curved space (Riemannian manifolds) is signposted in Chapter 11. The expression $g=J^T J$ in this book is the most concrete example induced from coordinate changes or embeddings within Euclidean space.

- <strong>From the introduction of a positive-definite metric in Chapter 6 to its use with a pseudo-Riemannian metric in Chapter 10 is a logical jump</strong>
  → As noted in Chapter 10 §10.3, Chapter 10 keeps from Chapter 6 only the procedure "build the dictionary for $\ast$ from the metric matrix," giving up positive definiteness. The theoretical basis for generalizing from positive definite to pseudo-Riemannian is supplemented in Chapter 11.

- <strong>Spaces with torsion or manifolds with nonsymmetric connections are not considered</strong>
  → Outside the book's scope. The book treats three-dimensional Cartesian space (and parameter spaces); when connections are mentioned, they are implicitly symmetric, metric-compatible Levi-Civita connections. General connection theory is signposted in Chapter 11.

- <strong>There are algebraic limits to treating spinors and similar objects with differential forms alone</strong>
  → True. Differential forms are a framework for antisymmetric tensors; treating spinors (double-valued representations) naturally requires additional tools such as Clifford algebra and spin structure. This book does not enter that direction, but Chapter 12 gives signposts toward geometric algebra.

- <strong>Computing only with matrix components hides geometric properties of the underlying space (metric, etc.)</strong>
  → This book does not hide geometry; it constantly pairs atomic matrix operations with geometric intuition. For example, Chapter 6 §6.1 shows, while looking at matrix diagonal entries, that each component of the parameter-space metric $\mathbf{g}=J^T J$ directly expresses "stretching and shrinking of axis scales."

- <strong>When differential forms are represented as matrices, one cannot tell which basis the components refer to</strong>
  → We acknowledge this notational limitation. As in thermodynamics, where held variables are put in subscripts, we considered an original notation embedding the coordinate system or basis in the symbols, but did not adopt it in order not to widen the gap from general notation further. From Chapter 1 §1.1.6 and §1.4 onward, this book explicitly states in the main text which coordinate basis is being used. See Chapter 11 for correspondence with standard $dx^i$ notation.

- <strong>The exterior derivative $d$ and the covariant derivative $\nabla$ are different objects; won't the book's explanation of $d$ alone fail to treat differentiation on curved space?</strong>
  → True, and an intentional separation. The $d$ of this book is antisymmetric differentiation (the exterior derivative), a topological operation independent of the metric. The covariant derivative $\nabla$ is symmetric differentiation depending on the metric and becomes necessary on curved space. This separation ($d$ and $\nabla$) reflects the author's reading strongly influenced by Burke's "delay the metric"; it is treated in Chapters 6 and 11.

- <strong>In curvilinear coordinates (cylindrical, polar), it is unclear whether $dr$ and $d\theta$ can be treated as "row vectors" like $dx$ in Cartesian coordinates</strong>
  → Treated explicitly in Chapter 1 §1.4 and Chapter 4. The $dr,d\theta,dz$ of parameter space are, like $dx,dy,dz$ in Cartesian coordinates, row vectors (1-forms) within parameter space. The difference between them is absorbed by the pullback.

---

## III. On Physical Definitions and Pedagogical Choices

- <strong>Without intuitive diagrams (right-hand rule, etc.), the book is all algebra and no physical image forms</strong>
  → This book aims to form physical images through "matrix calculation" and "arrow vectors," not through "diagrams." For example, Chapter 2 §2.4 visualizes the internal structure of an area-measuring device as a matrix and shows antisymmetry of the wedge product appearing as "subtraction." That is the "image" in this book.

- <strong>Saying "vector analysis is wrong" misunderstands the history of physics</strong>
  → This book never says "vector analysis is wrong." Chapter 8 re-derives theorems of vector analysis (Gauss, Stokes, Green) as special cases of integral theorems for differential forms and shows that the two languages are equivalent (translatable). Chapter 12 algebraically nearly fully automates that translation.

- <strong>The content is already in existing mathematics books and is not the author's original research</strong>
  → True. This style has precedents in Burke and Flanders and is also seen in numerical computation. The author wrote the book simply because there seemed to be no Japanese book in this vein, without claiming novelty. For the giants on whose shoulders this book stands, see "References."

- <strong>The Hodge star $\ast$ depends on the metric and orientation of space; isn't it treated too much as mere "degree reversal"?</strong>
  → Chapter 6 §6.3 explicitly states that the definition of $\ast$ depends on the metric $\mathbf{g}$. In orthogonal Cartesian coordinates ($\mathbf{g}=I$) the dictionary becomes the concise $\ast(dx)=dy\wedge dz$, but Chapters 8 §8.6 and 9 show concretely that in orthogonal curvilinear coordinates the coefficients of $\ast$ become functions of position.

- <strong>In the differential-form presentation of Maxwell's equations, aren't unit normalization, sign conventions, and metric signature ambiguous?</strong>
  → Chapter 10 §10.1 explicitly normalizes dimensions with $w=ct$ and $\mathbf{B}'=c\mathbf{B}$, §10.3 defines the Minkowski metric signature, the note in §10.2 fixes the sign convention for $F_{\mu\nu}$, and §10.6 declares the convention $F=-d\mathcal{A}$. The note in §10.5 also remarks that normalization of $\mathcal{J}$ may differ in coefficient from standard relativistic notation.

- <strong>The row-matrix representation $dx = \begin{pmatrix}1&0&0\end{pmatrix}$ does not remain the same matrix after a coordinate change</strong>
  → Treated explicitly in Chapter 1 §1.4. In Cartesian coordinates, $dx = \begin{pmatrix}1&0&0\end{pmatrix}$ becomes $\begin{pmatrix}\cos\theta & -r\sin\theta & 0\end{pmatrix}$ in cylindrical scales. That is the concretization of the pullback; we show head-on, without hiding, how matrix entries change under coordinate transformations.

---

> <strong>Note</strong> (Easter egg)
> Once I harbored a borrowed admiration for the name "Bourbaki"—a presence that brought a great turn to mathematics. I thought there must be some sharp new language there, different from existing mathematics books.
>
> When I actually read it, what I found was, for me, rather the familiar face of "university mathematics textbooks." Of course, that does not mean Bourbaki was boring. Quite the opposite. The once-new axiomatic, structural style has settled deeply, not through Bourbaki alone, as part of the standard prose of modern mathematics. That is why it looks "ordinary" to readers today.
>
> And this book was written for readers who get lost in front of that "ordinary" face.

