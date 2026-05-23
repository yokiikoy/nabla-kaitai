# Afterword: How *Unmasking Div, Grad, and Curl* Was Born

To you, reader, who have finished this long journey——first, my heartfelt respect.

As you close this book, let me share a little of the backstage story of how this peculiar, somewhat forceful *Unmasking Div, Grad, and Curl* came to be.

It began with a bitter memory of my own. Like many students of physics, I nearly drowned in the quagmire of "vector analysis." Faced with $\mathrm{curl}$ and $\mathrm{div}$ in cylindrical or spherical coordinates, the question "why does it take this form?" was silenced by pressure to "just memorize the formulas." I had heard that differential forms could be the special remedy, but the axiomatic approach of mathematics books was too abstract for me then.

"Is there no slightly sneaky 'silver bullet' that would solve this indigestion in one shot?"——As I wondered, the first breakthrough came. This is personal: at the time I was quite absorbed in quantum mechanics and had grown accustomed to Dirac's bra–ket notation. The feeling of laying state vectors (column vectors) on their sides as dual vectors (row vectors) and computing naturally as matrix products——that sensation.

What mattered to me, however, was not that bra–ket notation was "convenient notation for inner products." Quite the opposite. A bra is originally a dual vector that eats a ket. The dual pairing in which a row vector eats a column vector and the inner product that compares two vectors via the metric are, in principle, different operations. Yet in the notation of physical mathematics they often appear with similar faces, and the distinction collapses before one notices. Dirac himself, in his justly famous book, writes that one "set[s] up a second set of vectors, which mathematicians call the dual vectors." Even so, in education a bra is often treated like "the left half of an inner-product symbol." I felt indignation about that at the time.

Around then I wondered: what if I applied this sensation directly to the classical $dx,dy,dz$ of three-dimensional Euclidean space? When I thought that, the first core of this book was fixed. Redefine the $dx$ at the tail of the integral sign as a "row vector (matrix) that extracts components from a displacement vector," and the abstract idea "function that eats vectors (1-form)" converts instantly into "matrix multiplication" that everyone knows. At least for me as a student, that became the decisive foothold for understanding vector analysis.

This is not an inner product. It is a measuring device that eats displacement vectors. Identification via the metric should come later. For my personal understanding, that was truly the silver bullet. Formulas of vector analysis could all be derived by hand from rules of matrix addition, subtraction, and multiplication.

But that alone was still not enough motive to start writing the book. The second breakthrough came from W. L. Burke's educational philosophy of "putting the metric later and later into the course."

Burke's intent was probably to show structures that hold before length, angle, and inner product are introduced, separated from structures that depend on the metric. The exterior derivative $d$, the wedge product, boundaries, and Stokes-type structure work to a large extent before the metric enters. In general relativity and vector analysis, putting the metric upfront from the start makes the exterior derivative, boundaries, conservation laws, coordinate changes, and metric-dependent conversion via the Hodge star look mixed together. Burke, I think, had a problem consciousness about that quite early.

Of course, this is my own reading. I do not think Burke himself wanted to "separate dual and inner product" the way I do. Still, on the point that introducing the metric in a hurry makes structures that should look separate collapse into one, I strongly sympathized with Burke's concern.

From Dirac I received the feeling "do not collapse dual into inner product." From Burke I received the feeling "if you introduce the metric in a hurry, you stop seeing structures that are visible without it." In my mind these two feelings linked up, and the book settled into the shape: place $dx$ as a measuring device, separate the pullback from the metric, and only then introduce the metric and Hodge star.

Especially important for me was showing that coordinate changes and the pullback can first be treated separately from talk of length and angle. Coordinate change is the demon gate of vector analysis. Pour unit vectors, scale factors, area elements, and the metric in all at once, and you lose sight of what comes from what. This book first treats the pullback as matrix calculation with the Jacobian, then introduces the metric and Hodge star. I decided to turn that order itself into "table-of-contents educational entertainment" that draws readers in.

From Chapter 1 through Chapter 5 we did not formally define the metric and pressed forward with naive intuition about length and area in real space $(x,y,z)$. From a more advanced standpoint one might want to say "area needs a metric," but in the early part of this book we fixed on $xyz$ Cartesian coordinates and deliberately used naive intuition about area and volume wherever the Pythagorean theorem holds. The metric $g = J^T J$ truly becomes necessary when generalizing to coordinate systems with distorted scales like parameter spaces——we discovery-style derived that fact in Chapter 6 through matrix calculation.

Then came the opening of Chapter 6. Joking that "the author is getting bored too," we formally defined the inner product. At the same time we clarified the meaning of the metric $g = J^T J$ and positioned the Hodge star $\ast$ as a "type-conversion adapter linking differential forms and vector analysis." Through this discovery-based construction, the setup was to make readers accept the structure that "$df$ does not depend on the metric, but reading the usual gradient vector, curl, and divergence requires the metric and Hodge star."

Among these ideas, Burke's philosophy of "delaying the metric" and Flanders's physical applications of differential forms are both written in existing English literature. This book claims no mathematical novelty. Only the configuration——defining $dx$ as a matrix and pushing through the whole book with matrix calculation——seems, as far as I know, absent from Western books. Perhaps East Asian students are oddly trained in symbolic calculation——I joke——but in any case I merely organized something I wrote for myself. For the giants on whose shoulders this book stands, please see the references at the end.

This book is a "survival guide" written for my past self, who stumbled in vector analysis. Having cleared vector analysis and knowing powerful tools such as "dual," "exterior derivative," "pullback," "metric," and "Hodge star $\ast$," and knowing the limits of Cartesian coordinates, you have already opened the door to the next world.

What follows is an extra. Still, before you close the book, there is a conviction I want to state.

This book progressed by dropping differential forms——which look abstract——into matrix calculation as far as possible. Reading $dx$ as a row vector, treating the wedge product as calculation with antisymmetric matrices, and reading the Hodge star as a dictionary built from the metric matrix were all devices for that purpose.

Looking back, this was perhaps not merely my personal shortcut but an attempt to "misuse" algebraic training that science-track students who have seriously passed entrance-exam mathematics already possess at the entrance to university mathematics. Japanese competitive entrance exams, for better or worse, drill students in transforming expressions, substituting letters, tracking parameters, and organizing conditions. Not even calculus is an exception; substitution integrals and parametric representations are typically trained as almost purely algebraic symbol manipulation.

Such training is often excessive and can look like meaningless technique. Rather than lamenting that it is meaningless or an obstacle to abstraction, there is room to use it as an embodied, powerful weapon.

As an expression of that, this book asks readers for quite a lot of hand calculation——mostly not analytic work such as evaluating limits or studying convergence, but algebraic work: rearranging symbols, tracking components, multiplying matrices, expanding wedge products. That is not because I underestimate readers. I expect you can withstand this level of symbol manipulation——or perhaps I am flattering you a little.

University mathematics sometimes jumps to set-theoretic "definitions" too quickly. Abstract definitions have strength; there is still much to learn from Bourbaki-style structural organization. But there should also be a path where one first grasps abstract concepts as concrete operations using the algebraic body one already has. This book tried that path in a rather extreme form. The assertion $dx=(1\ 0\ 0)$ is its symbol.

This book's structure is certainly not the only correct one. It is probably awkward, forceful in places, and from a standard textbook looks like a detour. Even so, if through this book you felt abstract symbols as something you can move with your hands, the book has done its job.

As the author, I sincerely hope that *Unmasking Div, Grad, and Curl* will be a sturdy foothold on your journey in physics and mathematics——keeping the algebraic hands you already have and going higher and farther.

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
