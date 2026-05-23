# Appendix: What This Book Did Not Discuss

This appendix collects likely differences in convention, theoretical limits, or typical reader objections to the book's presentation.

This book is not an axiomatic development of differential forms on general manifolds. It is an educational book that reconstructs vector analysis in three-dimensional Cartesian space through matrix-represented differential forms. Therefore, the notation and order of exposition adopted here do not always match standard mathematics books. Those choices are, in principle, intentional; where needed, Chapter 11 shows connections to standard theory.

> <strong>Note</strong> (the honest version)
> The title of this section is the mild-sounding "What This Book Did Not Discuss," but that is the official line. To be honest, this is a collection of responses to typical criticisms thrown at the book without reading its scope.
>
> If I wrote that plainly, readers I genuinely want to support might get scared and run away. So on the surface I gave it a gentle name.

> <strong>Note</strong> ("I" am angry)
> When I was young, I published a series of SNS posts pointing in the same direction as this book and was harshly criticized by people who presented themselves as knowledgeable about mathematics, including people with institutional standing. Of course, the drafts of that time had many immature points. Even after ten years I still write in this vein——that was surely a post with "momentum." But what I received then was less criticism that read the definitions, checked the scope, and showed how to fix things, and more an attitude of judging an unfinished attempt from a professional position.
>
> That was perhaps a kind of inevitability produced by the engagement structure of SNS and crowd psychology. Publishing writing for free costs more than one imagines; I learned that firsthand.
>
> Even having understood that structure, I am still angry. An attitude that claims rigor while refusing to read what the other person defined and the scope in which they are speaking is, at least in my view, not a mathematical attitude.
>
> Even so, I decided to publish this book for free. In a sense it is also a private act of compensation. On top of that——sorry, this too is a bit of official rhetoric——to protect the readers this book is really for, or rather to protect my own self-respect, I have drawn preventive lines as carefully as I can.
>
> If a definition in this book looks different from a mathematician's textbook, I want you first to read the definition inside this book. Then please distinguish whether there is a real contradiction or whether someone has simply imported notation from a different context. After that, by all means criticize me harshly again. Having read the definitions, I want you to point out my mistakes.

> <strong>Note</strong> (as advanced "gatekeeping")
> As I read mathematics books, I have internalized, at least somewhat, the beauty and strength of abstract orders of definition. The result is that what this book does can suddenly look like nothing more than sophisticated gatekeeping.
>
> If I put that into words it looks like an excuse; if I stay silent it will be misunderstood. Worse, I half believe such criticism myself, so I cannot speak about it well.
>
> Even so, a shortcut is not necessarily bad. A shortcut does not replace a professional system, nor is it merely subordinate to one. It can be a powerful language for treating three-dimensional physical mathematics in the tangible words of matrix representation——at least a system of operations on concrete symbols.
>
> Once again, the first purpose of this book is my own act of compensation. Even so, if a reader takes home one language they can move with their hands, that is an unexpected bonus.

> <strong>Note</strong> (will the day come when I am not fooled?)
> They say one stands at thirty; when I actually reached that milestone, I was still getting angry at formulas rather than standing upright. I have started making dad jokes.

---

## I. On the Theoretical Framework and Rigor

- <strong>Introducing the exterior derivative $d$ without mathematical definitions of manifolds, atlases, tangent spaces, and so on is inaccurate</strong>
  → This book is not a textbook of differential forms on general manifolds; it is an introductory book for reaching vector analysis on three-dimensional Euclidean space. Chapter 11 gives signposts for moving to general manifolds.

- <strong>Contravariant and covariant vectors (dual spaces) should be distinguished clearly from the start</strong>
  → Chapter 1 §1.1.6 introduces the distinction between "column vectors (displacements)" and "row vectors (measuring devices)," which is a concrete representation of the dual-space idea. A more abstract formulation of dual spaces is connected in Chapter 6 and Chapter 11.

- <strong>Treating $dx$ as a row vector is not standard notation in mathematics books</strong>
  → An intentional choice. Defined in Chapter 1 §1.1 and used consistently throughout. The aim is to translate the abstract idea "1-form = function that eats vectors" into "matrix multiplication" that the reader already knows. Correspondence with standard differential-form notation is shown in Chapter 11.

- <strong>The exterior derivative $d$ should be defined generally from axioms (Leibniz rule, $d^2=0$)</strong>
  → This book does not start from axioms; in Chapter 5 §5.3 it discovery-style derives $d$ from the physical intuition of "mismatch when traversing an infinitesimal loop." $d^2=0$ is understood in Chapter 5 §8.8 as a consequence of symmetry of mixed partial derivatives. The axiomatic definition is supplemented in Chapter 11.

- <strong>A complete proof of Stokes' theorem on general $n$-dimensional manifolds is not given</strong>
  → This book derives the concrete cases in three-dimensional Euclidean space (Gauss, Stokes, Green) directly from the definition of integration (Chapters 5 and 8). Proof of Stokes' theorem in general dimension is outside the book's scope; Chapter 11 gives signposts only.

- <strong>The axiomatic approach via universal properties of exterior algebra is not used in defining the wedge product</strong>
  → In §2.4 this book builds the wedge product as antisymmetrization of the tensor product. That is the most concrete practice of the axiomatic approach, chosen so the reader can work by hand with matrix subtraction. Definition via universal properties is introduced in Chapter 11.

- <strong>The book relies too much on component representations even though geometric objects have no absolute coordinate representation</strong>
  → An intentional choice. The subject of this book is "how to use differential forms," not the philosophy of "differential forms as coordinate-independent geometric entities." Like standard vector-analysis textbooks, it adopts component representations as a practical computational tool. The coordinate-invariant viewpoint is connected in Chapter 11.

- <strong>Avoiding standard notation makes the book look like it claims a private school</strong>
  → The notation is chosen with top priority on "beginners can work by hand with matrix calculations." Why standard notation (index contraction, $\partial_\mu$, and so on) is deliberately avoided is explained in Chapter 11. This policy itself is widely seen in numerical computation and similar fields; the author does not especially claim anything new. There simply seemed to be no Japanese book in this style, so the author wrote one.

---

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
  → Outside the book's scope. The book treats three-dimensional Cartesian space (and parameter spaces); connections are implicitly always symmetric, metric-compatible Levi-Civita connections. General connection theory is signposted in Chapter 11.

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
> Once I harbored a borrowed admiration for the name "Bourbaki"——a presence that brought a great turn to mathematics. I thought there must be some sharp new language there, different from existing mathematics books.
>
> When I actually read it, what I found was, for me, rather the familiar face of "university mathematics textbooks." Of course, that does not mean Bourbaki was boring. Quite the opposite. The once-new axiomatic, structural style has settled deeply, not through Bourbaki alone, as part of the standard prose of modern mathematics. That is why it looks "ordinary" to readers today.
>
> And this book was written for readers who get lost in front of that "ordinary" face.
