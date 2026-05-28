# Introduction: What Is $dx$? What Is Nabla?

### Prerequisites

You should be able to read this book if you are comfortable with the following basic material.

- <strong>Calculus</strong>: You should be able to differentiate and integrate one-variable functions. It is even better if substitution in integrals does not bother you.
- <strong>Linear algebra</strong>: You should not be allergic to multiplying matrices. You should also have an image of moving back and forth between “vectors as arrows” and “vectors as lists of numbers.”

You do not need to know determinants in advance. We will discover them along the way.

When I say that a high-school student could read this book, I do not mean that it will be effortless. But I wrote it so that, at least, the twenty-year-old version of myself could have read it through.

### What Is $dx$?

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

### What Is Nabla?

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

---

### Roadmap of This Book

This book has twelve chapters, divided into three large parts.

1. <strong>Part I: Differential Forms on $\mathbb{R}^3$ (Chapters 1–4)</strong>  
   We redefine $dx$ as a “matrix” and algebraically build the mechanism that measures area and volume, then reach integration and the pullback.
2. <strong>Part II: Vector Analysis (Chapters 5–9)</strong>  
   This is the core of the book. We treat the exterior derivative $d$, the metric and Hodge star $\ast$, vector analysis via nabla, translation between the two languages, and curvilinear coordinates in practice.
3. <strong>Part III: Development and Integration (Chapters 10–12)</strong>  
   We look at applications to electromagnetism, namely Maxwell’s equations, and then glance toward the worlds of manifolds and Geometric Algebra.
