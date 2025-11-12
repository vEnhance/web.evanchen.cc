# All you have to do is construct a parallelogram!

> i wrote this lecture as a teenager and now in my 30's people
> are still emailing me for solutions

## Problem 1

Reflect $M$ over $N$ to a point $P$, so $MP = 2MN$ by definition.
Then $AMCP$ is a parallelogram, but $AM = MB$, so $BMPC$ is also.

## Problem 2

Reflect $A$ over $M$ to $T$, so $ABTC$ is a parallelogram.
Then $ABT$ and $ABC$ have the same area,
but the side lengths of $ABT$ are all known.

## Problem 3 ([AIME 2011](https://aops.com/community/p2209660))

Build parallelogram $DPEF$.
Then $BP = BE + FD$, so you can get $BPC$.

## Problem 4

Build $T$ as in problem 2.
Then show that $ABT$ and $PAX$ are congruent by SAS congruence.

## Problem 5

Let $G$ be the centroid. Reflect $G$ over the midpoint of $BC$ to $P$.
Then $BGCP$ is a parallelogram, and $\triangle BGP$ has side lengths
$2/3 m_a$, $2/3 m_b$, $2/3 m_c$.

## Problem 6 ([USAMO 2003](https://aops.com/community/p336205))

See the [first official solution](https://web.evanchen.cc/upload/usamo-2003-rubric.pdf)
with the point $G$.

## Problem 7 ([NIMO 8.8](https://aops.com/community/p3228703))

Get rid of $B$ and $C$ first.
Set $\beta = \angle BAM$, $\gamma = \angle CAM$ and
note that $\sin \beta = \frac{5}{13}$ and $\sin \gamma = \frac{3}{5}$.
Compute $AM = 84$.

Now, let $A_1$ be the reflection of $A$ over $M$.
We can compute
$$[AST] = [AA_1T] = \frac{AM^2 \sin \beta \sin \gamma}{2 \sin \left( \beta + \gamma \right)} = 7^2 \cdot 288 \cdot \frac{\frac{5}{13} \cdot \frac{3}{5}}{\frac{5}{13} \cdot \frac{4}{5} + \frac{12}{13} \cdot \frac{3}{5}} = 7^2 \cdot 288 \cdot \frac{15}{56} = 3780.$$
In that case, the desired quantity is
$[ABC]-[AST] = 84 \cdot 7^2 - 3780 = \boxed{336}$.

## Problem 8

I don't remember anymore.
Please submit a pull request if you know.

## Problem 9 (Simson lines)

Let $X$, $Y$, $Z$ denote the feet form $P$ to $BC$, $CA$, $AB$.
The idea is that if line $PX$ meets the circumcicrle again at $K$,
and line $AH$ meets line $XYZ$ at $L$,
then $AKXL$ is a parallelogram.
Then $AHPK'$ is also a parallelogram, where $K'$ is the reflection
of $K$ across line $BC$.
Hence $LHXP$ is a parallelogram too.

See section 4.1 of my geometry textbook for details.

## Problem 10

See Jeck Lim's solution at [this link](https://aops.com/community/p3026737).

## Problem 11 ([ELMO 2012](https://aops.com/community/p2728469))

Let $R$ be the reflection of $P$ across the midpoint of $\overline{BC}$,
so $PBRC$ is a parallelogram.
The conditions $BD=CE$ and $\overline{PD} \parallel \overline{AE}$
imply that $R$ lies on $\overline{AE}$.
Then since $\overline{AP}$ and $\overline{AR}$ are isogonal,
isogonality lemma implies that $B$, $C$,
$\overline{BP} \cap \overline{AC}$ and $\overline{CP} \cap \overline{AB}$ are concyclic, done.
