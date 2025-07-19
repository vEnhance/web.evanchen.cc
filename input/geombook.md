title: EGMO book
menu-position: 71
header: Euclidean Geometry in Mathematical Olympiads (EGMO)
indent: 1
description: Synopsis and errata for EGMO geometry textbook for math olympiad students.

---

<span style="float:left;padding:10px;">
[![Book cover][cover]][ebook]
</span>

<span style="color:red; font-size: 120%;">
**You can get a hardcopy from [Amazon][amazon] or [the AMS][hardcopy].
You can also [buy a PDF][ebook].**
</span>

(ISBN-10: 0883858398 / ISBN-13: 978-0883858394)

_Euclidean Geometry in Mathematical Olympiads_ (often abbreviated _EGMO_,
despite an olympiad having the [same name][girls])
is a comprehensive problem-solving book in Euclidean geometry.
It was written for competitive students training for national
or international mathematical olympiads.
However, it has no prerequisites other than a good deal of courage:
any student with proof experience
should be able to follow the exposition.

The book has a selection of about 300 problems from around the world
and about 250 figures.
Some solutions are provided in [this solutions file][agest].

I wrote this textbook while
[serving time as a high school clerk][fillblank].
You can [read about the publication process][publishing].

## {{ hl("prereq", "Prerequisites and material") }}

There are essentially no geometry prerequisites;
EGMO is **entirely self-contained**.
(This was one of the design goals.)
The main limiting factor is instead the ability to **read proofs**.
As long as you can follow mathematical arguments,
then you should be able to follow the exposition
even if you don't know any geometrical theorems.
Here is a freely available subset of the book:

- [Table of contents][toc].
- [Chapters 1-3][googlebook] on Google Books preview.
- _Parody version of entire book_: check out
  [Undergraduate Math 011: a firsT yeaR coursE in geometrY](textbooks/tr011ey.pdf),
  made for April Fool's Day 2019.
- [Solutions to a lot of the problems][agest].

## {{ hl("translations", "Translations") }}

- **Chinese** translation at
  [abebooks](https://www.abebooks.com/Euclidean-Geometry-Mathematical-OlympiadChinese-Edition-MEI/31089552348/bd)
  and [amazon](https://www.amazon.com/Euclidean-Geometry-Mathematical-Olympiad-Chinese/dp/7560395880).<br />
  ISBN-10: 7560395880 / ISBN-13: 978-7560395883.
- **Japanese** translation at
  [nippyo.co.jp](https://www.nippyo.co.jp/shop/book/8967.html)
  and [amazon.co.jp](https://www.amazon.co.jp/dp/4535789789).<br />
  ISBN-10: 4535789789 / ISBN-13: 978-4535789784.

Contact `reprint-permission [at] ams.org` if you are interested in
a proposal for a translation into a different language.
I have preemptively granted blanket author-approval to the AMS
to move forward with any translation proposals (on 22 April 2023 17:19 UTC).

## {{ hl("errata", "Errata (aka selected solutions to Problem 11.0)") }}

The errata list is now embarrassingly extensive. You can see:

- [List of mistakes in PDF format](/textbooks/geombook-errata.pdf)
- [List of mistakes in TeX format](https://github.com/vEnhance/egmo-book-errata)
- [Instructions for submitting errata](https://github.com/vEnhance/egmo-book-errata#submitting-more-errata)

Most mistakes are harmless, but a few of the mistakes are significant.
Here are the important ones:

- On **page 4**, the proof of Theorem 1.3 is incomplete
  because it assumes that the point $O$ lies inside the triangle $ABC$.
- On **page 12**, Theorem 1.22, the four points could also be collinear.
- On **page 76**, Theorem 5.1 is missing a factor of $\frac12$.
- On **page 92**, Problem 5.23, when defining $G$, line $HE$ should intersect
  $\Gamma_1$, not $\Gamma_2$.
- On **page 107**, the proof of part (a) of the theorem
  has several issues, and is probably best to just ignore.
  Figure 6.6B is also broken.
  (The result is still true, and the proof of part (b) is correct.)
- On **page 146**, Problem 7.52, change $\angle PCB$ to $\angle PBC$.
- On **page 159**, in Lemma 8.16,
  change "fixes $B$ and $C$" to "swaps $B$ and $C$".
- On **page 184**, in Theorem 9.33, uniqueness is not true for (b) or (c).
  The last sentence is also wrong as written. The correct sentence is:
  if the _circumcircle_ of a cyclic quadrilateral is preserved,
  then so is the cross ratio of the cyclic quadrilateral.
- On **page 235**, hint 556 doesn't make sense.
  I don't remember what I meant to write.
- On **page 243**, Solution 1.50 is incomplete;
  one also needs to check $A$, $P$, $W$ are collinear.
  Thus, add the remark $\measuredangle NPA = \measuredangle NMA = \measuredangle NMC = \measuredangle NBC = \measuredangle NBW = \measuredangle NPW$.
  (Radical axis also works.)
- On **page 268**, Solution 7.44 is completely broken; it's solving a different
  problem. See the above file for a fixed solution.
- On **page 274**, Solution 8.37 is wrong, it assumes $AB$ passes through the center of $\omega\_2$.

## {{ hl("solutions", "On solutions to problems") }}

I included solutions to about a quarter of the
practice problems in the back of the textbook
(it was impossible to include more for space reasons).
If you are stuck on a problem for which no solution is provided,
here are some possible places to look:

1. Each problem in the text has one or more hints,
   the intention is that the union of all the hints
   should form an outline of the complete solution
   (even if the details are omitted).

2. The [Automatically Generated EGMO Solutions Treasury][agest]
   contains updated solutions to a significant number of the sourced problems.
   (However, I compiled the solutions by problem,
   so they don't necessarily "match" the chapter the problem appears in.)

3. There is a [user-created forum][userforum]
   which has a link to discussion for every problem.

4. I included sources for as many of the problems as possible,
   so looking up the corresponding thread on
   [Art of Problem-Solving's Contest Index][contests]
   will generally yield a solution to any sourced problem.
   (The search function can work too, but is usually less helpful.)

5. If all of the above fail, try posting on the AoPS forums directly.

[userforum]: https://artofproblemsolving.com/community/c618937h1605831_egmo_problem_discussions_links
[agest]: textbooks/AGEST.pdf

## {{ hl("resources", "More resources") }}

Of course there are other good geometry textbooks too.
A few that I recommend are:

- [A Beautiful Journey Through Olympiad Geometry][stefan] by Stefan Lozanovski,
  which is free (though I encourage you to donate to the author if you can).
  This book ramps up more slowly than mine,
  so I would also recommend it to beginners.
- [Lemmas in Olympiad Geometry][log]
- [UKMT Plane Euclidean Geometry][ukmt], but consider starting from Chapter 3
- [106][106], [107][107], and [110][110] Geometry Problems

See also [advice from Geoff Smith on geometry](https://web.archive.org/web/20250124103026/https://people.bath.ac.uk/masgcs/geo.pdf).

[106]: https://www.awesomemath.org/product/106-geometry-problems-from-amsp/
[107]: https://www.awesomemath.org/product/107-geometry-problems-from-amy/
[110]: https://bookstore.ams.org/xyz-14/
[log]: https://www.awesomemath.org/product/lemmas-in-olympiad-geometry/
[stefan]: https://www.olympiadgeometry.com/
[ukmt]: https://shop.ukmt.org.uk/ukmt-books/plane-euclidean-geometry
[ebook]: https://bookstore.ams.org/prb-27/
[cover]: /static/egmo-cover.jpg
[googlebook]: https://books.google.com/books?id=47UaDAAAQBAJ&lpg=PP1&pg=PP1#v=onepage&q&f=false
[amazon]: https://www.amazon.com/Euclidean-Geometry-Mathematical-Olympiads-Problem/dp/1470466201
[hardcopy]: https://bookstore.ams.org/prb-27/
[girls]: https://www.egmo.org/
[contests]: https://artofproblemsolving.com/community/c13_contests
[fillblank]: https://blog.evanchen.cc/2016/05/27/fill-in-the-blank/
[publishing]: https://blog.evanchen.cc/2016/11/11/notes-on-publishing-my-textbook/
[toc]: https://www.maa.org/sites/default/files/pdf/pubs/books/EGMO_TOC.pdf
