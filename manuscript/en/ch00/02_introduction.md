# Introduction: What Is $dx$? What Is Nabla?

## Prerequisites

You should be able to read this book comfortably if you are familiar with the following basic material.

- <strong>Calculus</strong>: You should be able to do calculus of one-variable functions. It is even better if substitution in integrals does not bother you.
- <strong>Linear algebra</strong>: You should not be allergic to multiplying matrices. You should also have an image of moving back and forth between “vectors as arrows” and “vectors as lists of numbers.”

You do not need to know determinants in advance. We will discover them together along the way.

If I say that even a high-school student can read this book, that student will have to work. But I wrote it with the intention that, at least, the twenty-year-old version of myself could have read it through.

## What Is $dx$?

At the end of an integral sign, there is always a $dx$. In high-school mathematics, it is treated something like a mark saying “integrate with respect to $x$.”
Also, although we are taught that $\frac{dy}{dx}$ is not a fraction, we are in practice allowed to perform substitutions as if it were one.

In first-year university calculus, $dx$ appears as part of the total differential. But in many cases, I think, we do not go very deeply into what it actually is.

Furthermore, especially in specialized courses in physics and engineering, entities such as infinitesimals $dx$ and $\delta x$ are manipulated as if this were the most natural thing in the world.

In my own experience, when I was a first-year master’s student, I asked a friend in mathematics what $dx$ was. I remember receiving an explanation that sounded both understandable and not understandable: “$dx$ is a linear functional on the tangent vector space, or an element of the cotangent space.”

So, in the end, what is $dx$? Unless we are already in an advanced specialized course, do we have no choice but either to avoid the question or to understand it as an infinitesimal?

Of course, from a more advanced mathematical point of view, my graduate-school friend’s explanation was overwhelmingly correct, and it is better if one can understand it that way. But it is hard.

So this book asks what it would really take to lead a high-school student to that understanding. For that purpose, we use as our foothold the matrix algebra that, at least in my case, had already been drilled into me in high school.

That is, in this book we first read $dx$ as “a measuring device that extracts the $x$-component from a displacement vector.” In matrix representation, symbolically,

$$
dx=\begin{pmatrix}1&0&0\end{pmatrix}
$$

What we want to know is what the $dx$ dangling from the tail of the integral sign is actually doing. In this book, we first make that operation visible.

$dx$ eats a displacement and returns its $x$-component. $dx\wedge dy$ measures the oriented area spanned by two displacements. $dx\wedge dy\wedge dz$ measures the oriented volume spanned by three displacements.

Instead of immediately placing abstract terminology between the $dx$ of high-school mathematics and the $dx$ of differential forms, we first place matrices and measuring devices there. That is the starting point of this book.

## What Is Nabla?

There is another symbol this book wants to take up: $\nabla$.

In English, the symbol $\nabla$ is called **del**, and also **nabla**. In Japanese textbooks, it is often called *nabla*. This book is not really about the name of the symbol. It is about what div, grad, and curl are actually doing.

When studying vector analysis, there may come a point when the whole system suddenly begins to look like a collection of formulas. At least that was my experience. Cartesian coordinates may be fine, but once cylindrical or spherical coordinates enter the stage, $r$ and $\sin\theta$ appear, and one has to memorize coefficients whose origin is not clear.

For example, in two dimensions, one encounters

$$
\frac{\partial F_y}{\partial x}-\frac{\partial F_x}{\partial y}
\qquad=\qquad
\frac{1}{r}\frac{\partial (r F_\theta)}{\partial r}-\frac{1}{r}\frac{\partial F_r}{\partial \theta}
$$

The left-hand side is written in Cartesian coordinates, and the right-hand side is the same thing written in polar coordinates. It is not especially easy to feel satisfied, with a midterm tomorrow, about why this deserves to be called “curl.”

Of course, this point is explained in supplementary books on mathematical physics and in careful recent books as well. But as far as I know, books in Japanese that build this up heuristically within the structure of a textbook are still rare.

Now, this book does not begin with nabla. Since we are going to think about the matrix representation of $dx$, we use it.

From $dx$, we then rethink what area is and what volume is. After that, we move on to integration, changes of variables, the exterior derivative, and the Hodge star. Only then do we finally return to nabla.

It will not help you in time for tomorrow’s midterm. But perhaps it will make it in time for the final.

---

## Roadmap of This Book

This book has twelve chapters, divided into three large parts.

1. <strong>Part I: Differential Forms on $\mathbb{R}^3$ (Chapters 1–5)</strong>  
   We redefine $dx$ as a “matrix” and algebraically build the mechanism that measures area and volume. We obtain two powerful tools: the exterior derivative $d$ and the Hodge star $\ast$.
2. <strong>Part II: Vector Analysis (Chapters 6–9)</strong>  
   This is the core of the book. We dismantle grad, curl, and div in vector analysis, and we take on Stokes’ theorem and curvilinear coordinates.
3. <strong>Part III: Development and Integration (Chapters 10–12)</strong>  
   We look at applications to electromagnetism, namely Maxwell’s equations, and then glance toward the worlds of manifolds and Geometric Algebra.
