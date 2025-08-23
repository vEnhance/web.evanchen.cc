title: Contest Rules FAQs
header: Contest Rules FAQs
description: Some FAQs about math contests and my personal life.

---

[Return to FAQ Index.](faqs.html)

These are FAQs about the _rules_ of math contests
(e.g. MOP qualification, IMO criteria, and so on)
that I often get asked.
Please note: **this is not an official source in any way**;
it represents my best knowledge and may become out of date.
See the [official AMC website][amc] for authoritative answers.

If you are looking for training advice,
see [Contest FAQs](faq-contest.html).

### {{ faq("CR-1", "How is the USA IMO team determined?") }}

Starting in 2011 and as of 2019, the IMO selection procedure is as follows.

In the USA the main olympiad event is the USA(J)MO held in April each year.
Roughly 250 students qualify for the USAMO and 250 students qualify for the USA(J)MO
via scores on previous short-answer contests.
Then things get interesting:

- In USAMO of year $N-1$, about 60 students in grades 11 and below
  and the IMO team of that year are invited to the
  three-week Mathematical Olympiad Summer Program, abbreviated **MOP**.
- At the end of MOP, an exam called the **TSTST** (yes, I know) is given.
  The acronym stands for "Team Selection Test Selection Test".
  The top approximately 30 students are then selected
  for the year-round TST's for the IMO of year $N$.
- Two TST's are given in **December** and **January**, administered by schools.
  Each of the two exams is worth 21 points.
- Contestants participate in **RMM Day 1**, worth 21 points.
- Contestants participate in the **APMO**, which is weighted by 0.6;
  hence it is also worth 21 points (despite being a five-problem exam).
- Finally, the two days of **USAMO** of year $N$ serves as the final TST,
  worth 42 points.
- The sum of scores over these five tests (six days, maximum 126 points)
  determine that year's IMO team.

In particular, winning the USAMO is neither necessary nor sufficient
for qualifying for the American IMO team, since the IMO team is determined
by several different exams.

The IMO selection process takes an entire year.
(In particular, it is impossible to qualify for the IMO
without first having attended MOP the previous year.)
The IMO team is known shortly after the USAMO grading in May.

### {{ faq("CR-2", "How is the Taiwan IMO team determined?") }}

Here are the details for IMO 2014 (the year which I participated),
A series of tests/camps take place and at each step the number of contestants is reduced.
Interestingly, the Taiwan national olympiad was not present.

- The first test worth mentioning is the APMOC, an exam in the same format as the APMO.
- High scores on the APMOC are invited to another camp at which the APMO is given in March.
- The top 30 scores on the APMO are invited to the first TST camp in late March.
- The top 15 scores at the first TST camp are invited to the second TST camp two weeks later.
- The top 10 scores at the second TST camp are invited to the third TST camp two weeks later.
- The IMO team is decided by a weighted sum of the scores at the second and third TST camp plus an oral interview.

Each camp lasts roughly from Friday to Tuesday; the geography of Taiwan makes commuting convenient. Each TST camp features

- Three Team Selection Quizzes (formally "individual study"), which last 110 minutes with two olympiad problems
- A full mock IMO with six problems.

Thus, the IMO team is decided by $6 \cdot 2 = 12$ mock IMO problems and $2 \cdot 3 \cdot 2 = 12$ quiz problems.
The weighting is roughly so that a mock IMO problem is worth three quiz problems.
The selection process takes a few months.
The team is known shortly after the third camp, a couple of days into May.

For more details, see [my report on Taiwan IMO][taiwan].

A decade later, I was also sent an
[updated flowchart of the selection process for 2024](static/taiwan-select-2024.pdf).
This now includes a pathway to the EGMO.

### {{ faq("CR-3", "How is USAMO / IMO graded?") }}

Don't take my word for it:
try reading the [USAMO 2003 rubric][usa2003].

In general, for each problem the solution is graded according to the rubric:

- 7: Problem solved.
- 6: Tiny slip (and contestant could repair)
- 5: Small gap or mistake, but non-central
- 2: Lots of genuine progress
- 1: Significant non-trivial progress
- 0: "Busy work", special cases, lots of writing

The most important difference
is that USAMO grading is designed to reward complete solutions.
Basically, we split the solution into
either **top-down or bottom-up**:
meaning the score is "7-" (has all the main ideas)
or "0+" (missing at least one main idea).
The scores of 3 and 4 are absent for this reason
(typically used only for two-part problems or strange cases).
This means your total score is essentially equal to 7 times
the number of complete solutions plus or minus some pocket change.

(Pocket change tends to also be pretty small,
though it depends a lot on who writes the rubric for each problem.
In particular, we don't give many sympathy points,
and demand real progress towards a solution to get partial credit,
not just vague ideas or lots of writing.)

One thing that is perhaps also surprising:
**rubrics often do NOT use standard addition**.
Meaning, we do not break the problem into bite-sized chunks
and award the sum of the chunks.
Here are a few examples of what I mean.

- Consider a problem that is two parts.
  In grader's internal jargon, an example rubric for that problem
  might colloquially be summarized as "2+2=7",
  meaning doing either half of the problem is worth 2 points,
  getting both halves is worth 7.
  The exact parameters depend on the problem and the captain.
  On both extremes, I have seen 3+5=7 and 1+1=7 rubrics as well.
- On a rubric, there might be three or four different
  starting observations that are worth 1 or 2 points.
  Often, a 0+ solution gets the maximum, rather than the sum,
  of these little partial bits: "1+1+1+2=2", say.
- If you forget to do some easy step (e.g. the base case of an induction),
  and the rubric penalizes a top-down solution by 1 point for this,
  it is not necessarily the case that the rubric
  would award 1 point for doing that step for a 0+ solution.

There is no style: a totally correct and complete solution receives 7 points.
However, it is still in your best interest to write a solution
clearly to minimize the chance the grader doesn't understand you.
Graders don't give points for things they can't comprehend ;)

If you want to see more examples of problem rubrics,
you should check out the reports of the [USEMO](usemo.html).
In particular, the first few USEMO years had rubrics
designed by veteran graders and released to the public,
so the standards for these rubrics is likely to be similar
to what you might encounter at USAMO.

### {{ faq("CR-4", "Can I get a regrade on USA(J)MO?") }}

No. It is a long-standing policy of AMC that decisions of the
USAMO graders are final and may not be appealed.

### {{ faq("CR-5", "What results may be cited without proof on USAMO or IMO?") }}

There are no hard criteria set in stone, but in general,
any well-known result which does not trivialize the problem is okay.
If you are still unsure, a good practice is to include a sketch of the proof
which only needs to be a few sentences long
(this is much better than gambling by omitting the proof altogether
because it only takes a few extra seconds).

See [English handout][english] for more discussion.

### {{ faq("CR-6", "How much detail should I include in a proof to avoid losing points?") }}

Enough to convince the grader that you understand the solution to the problem.

Whenever you say something like "it's easy to see X",
the grader has to ask themselves whether the student
actually understands why X is true, or doesn't know and is just "bluffing".
In particular, this is a math issue, not a style issue.

As a loose approximation, the official solutions file for
USAMO is about as terse as you can be.
See [English handout][english] for more discussion.

### {{ faq("CR-7", "What are the criteria for invitation to MOP?") }}

Before I say anything I want to say that the criteria for MOP invitations
are not especially well-defined.
Each year, the exact number and choice of students is determined
based on the exact scores for that year.

That being said, as of 2016 the criteria for MOP is _roughly_ as follows:

- IMO team members (see [CR-1](#CR-1))
- The next _approximately_ 18 non-graduating USAMO students
- The next _approximately_ 12 USAMO students in 9th and 10th grades
- The top _approximately_ 12 students on USAJMO
- Some varying number of non-graduating female contestants from either USAMO or USAJMO
  (these students represent USA at the European Girls' Math Olympiad).
  The exact cutoffs for each contest are determined based on the scores for that year.

Young students in 8th grades and below receive invitations
if and only if the moon is full and the wind is blowing south-south-east.
All selection is done by ID number, without student names.

As a consequence of the procedure spelled out in [CR-1](#CR-1),
it is not possible for a student to attend MOP for the first time as
a graduating 12th grader.
This is because the IMO selection process begins at MOP of the previous year.

### {{ faq("CR-8", "What are the colors people keep referring to for MOP?") }}

At MOP, there are often four tracks of classes and tests.
The tracks are usually called Black, Blue, Green, Red
as a convenient shorthand, a tradition started around 2002.
Class assignments are based on USAMO score, Team Selection Test rank,
grade level, previous MOP attendance, RMM/EGMO score.
(This is a _completely separate process_ from the invitation list. The
invitations are _first_ sent according to [CR-7](#CR-7), and _then_ the class
assignments are done by me weeks later.)

_Nevertheless_, because these groups are kind-of-sort-of in bijection
with the first four bullets in [CR-7](#CR-7),
students will often colloquially refer to the cutoffs by color as well,
in an abuse of terminology that leads to endless confusion.
For example, in Internet slang, "blue cutoff" would mean the minimum score
for an 11th grader to be invited to MOP through USAMO,
even though such a student could be placed in any class group.[^blue11]

[^blue11]:
    Corollary: it is _absolutely untrue_ that an 11th grade student will not be
    placed in Red or Green. This happens _all the time_, and if you email me
    "bUt I tHoUgHt I wAs BlUe mOvE mE uP", I will laugh in your face.

Some students (not staff) even refer to the 5th cutoff
in [CR-7](#CR-7) as the "pink" cutoff,
despite there being no analogous class or testing group.
This imaginary color was coined by students around 2007,
not necessarily out of good will, and stuck around.
Students have told me they find "pink" offensive, so I avoid it.
But the name is so entrenched I think it will never die,
hence I decided to explain its history here.

Finally, I better explain that **color groups are not that important**.
Once the USA students arrive at MOP, they are all treated equally in team selection:
no matter their color group, past USAMO score, gender, or what-have-you.
The team selection is not based on a caste system.
As a matter of principle, any USA student attending MOP of year $N$
and still in high school could qualify for IMO of year $N+1$.

[abusenote]: https://en.wikipedia.org/wiki/Abuse_of_notation

### {{ faq("CR-9", "When are ties on the USA(J)MO broken?") }}

Between 2016 and 2019, ties are generally only broken for USAMO winners,
since exactly 12 winners are invited to the state dinner.
This did not occur in 2020 or 2021 (due to COVID).
Starting in 2022, the USAMO switched to a different medal system.

### {{ faq("CR-10", "How does coordination at IMO work?") }}

Relevant references:

- [General IMO regulations, section 7][regulation]
- [2002 IMO report by Tom Verhoeff][verhoeff]
- [IMO 2019/3 blog post by Michael Ng][michaelng]
- [Quora answer by Carlos Shine](https://qr.ae/pGvwWB)
- [Reddit post on IMO 2019/5](https://www.reddit.com/r/math/comments/cgwayt/how_coordination_went_for_imo_2019_problem_5)
- [IMO 2020 instructions (unusual virtual procedure)](https://imo2020.ru/Marking-and-Coordination.pdf)

Basically, the outline of the idea is:
before the exam, a marking scheme (rubric) is set for each problem,
to cover the typical cases of what progress will be worth what points.
Then, the _leaders_ of each country get to see the solutions
of their country's students, while there is a number
of _coordinators_ from the IMO host country for each problem.
Both the coordinators and the leaders read through these scripts in advance,
and then meet at an appointment where they discuss the scores.
There are a lot of scripts that are not in English,
in which case the leader is expected to do any necessary translation.

The idea is that the leaders try to make the best case
they can from their student's work (while of course still being honest),
while the coordinators for the problem try to maintain uniform fairness.

We sometimes say jokingly that it's an "organized fight"
(where leaders are defense attorneys and coordinators are prosecutors),
but in practice it's a lot friendlier than this.
I remember being a coordinator at the virtual IMO 2020 (problem 5),
and in quite a few cases I offered a higher score than the leader,
because I'd managed to decipher a part of the paper
that matched a rubric item.[^pattern]
On the other hand, it's not uncommon for leaders to spend a lot of effort
trying to see how partial solutions of their students could be completed,
particularly if the student's approach is novel or uncommon.

[^pattern]:
    It's quite a different experience having your country's six papers
    for each of six problems versus 100 papers of the same problem ---
    you start seeing the common patterns and similarities.

[regulation]: https://www.imo-official.org/documents/RegulationsIMO.pdf
[verhoeff]: https://www.win.tue.nl/~wstomv/publications/imo2002report.pdf
[imo2019reddit]: https://www.reddit.com/r/math/comments/cgwayt/how_coordination_went_for_imo_2019_problem_5/
[michaelng]: https://michaelng126.wordpress.com/2019/07/28/imo-2019-coordination-part-2/
[quora]: https://www.quora.com/How-are-IMO-solutions-graded

### {{ faq("CR-11", "What is ISL / IMO Shortlist?") }}

At every IMO, the jury is presented a list of about 30 problems,
and select six of them to comprise the IMO.[^longlist]
The list for each year is called the **IMO Shortlist**.

[^longlist]:
    The shortlist is in turn selected from all proposed problems,
    of which modern IMO's have a few hundred.
    These problems comprise the so-called "IMO longlist".
    The selection is nowadays much more competitive than back in early 2000s.
    In modern times, problems from the longlist that did not make the shortlist
    are returned to the authors for use in other math competitions.

The shortlist is typically divided into four categories
Algebra, Combinatorics, Geometry, Number Theory of about 6-8 problems each,
from IMO-easy to IMO-hard.
The problems are numbered A1, A2, ... in loosely ascending difficulty;
similarly the combinatorics problems are labeled C1, C2, ... and so on.
(This means you can refer to a problem being "C8 level"
in a way that is meaningful from year to year.)
All the posted shortlists for the past several years are indexed on
[AoPS](https://aops.com/community/c3223_imo_shortlist),
and recent shortlists are available in their entirety
on the [official IMO website](https://www.imo-official.org/problems.aspx).

An important property of the IMO shortlist
is that **problems which are shortlisted are confidential for one year**
if they do not appear on IMO.
For example, the IMO 2020 shortlist is confidential
until after IMO 2021 concludes.
The reason for this is that the IMO Shortlist is a valuable source
of good problems, so many countries will use shortlisted problems
either for training purposes, or in their team selection tests.
Thus, it is critical that the security of the shortlist is not compromised.
(So, if you see a shortlist problem posted on AoPS prematurely,
you should immediately report it.)

Shortlisted problems from previous years of the IMO
are extensively studied by top students,
to the point where IMO team members from countries like the USA
will often know from memory which problem
"[2011 G4](https://aops.com/community/p2739327)" refers to, etc.

### {{ faq("CR-12", "How does copyright for contest problems work?") }}

Here's my understanding of the situation, though this should be taken with a
freaking bucket of salt since I am not a lawyer.
Also, the following is based on my knowledge of US law,
and may not apply on an international basis.

At the risk of stating the obvious: if you are using problems and
solutions that are not by you, **please attribute generously**
to avoid plagiarism[^plagiarism].
That's polite no matter what the law says.
So the following is only about whether you can use a problem or solution at all:

- Copyright only protects the expression of an idea, not the idea itself.
  Therefore, if you are paranoid about copyright law then
  it's probably a good idea to at least change the wording of the problem.
  (How much constitutes "enough" is unclear.)
  [John Scholes did this for the old kalva site](https://prase.cz/kalva/).

- Even if you use a problem statement verbatim,
  there are certain limitations to copyright law that
  prevent blatant abuse from copyright holders.
  So if you quote a past USAMO problem on your public blog
  before presenting your own solution,
  you probably don't have to worry about getting sued for that.

  In the United States these are called
  ["fair use"](https://en.wikipedia.org/wiki/Fair_use); other nations have
  ["fair dealing"](https://en.wikipedia.org/wiki/Fair_dealing).
  These laws are deliberately vague in some ways,
  because they have to cover a lot of cases (hence lawyers exist).

- I would probably not try to copy entire solutions verbatim,
  either from AoPS or the official contest.
  If I see a solution from someone else that I like,
  I'll typically cite the original author of that solution,
  but then write up the solution from scratch myself.

And again, please attribute generously.
If you copy a bunch of contest problems, change the wording completely,
and then pass them off as your own work,
that might technically avoid copyright infringement,
but it's _definitely_ plagiarism
(not to mention, obviously terrible manners).

[^plagiarism]:
    Confusingly, at least according to
    [Cornell Law School](https://www.law.cornell.edu/wex/plagiarism),
    plagiarism is not "directly" illegal in the United States;
    instead, either another related law or contract is violated,
    or consequences instead come from a school/institution/etc.

### {{ faq("CR-13", "Are AIME I problems harder/easier than AIME II?") }}

There is no pattern.
The two drafts are called something like Lion/Tiger or Holmes/Watson or Heart/Soul
or whatever while being written, then randomly assigned to one of I and II.
So any trends that one exam has more difficult problems is purely noise.

Same is true for AMC A and B exams.

[amc]: https://www.maa.org/math-competitions
[usa2003]: upload/usamo-2003-rubric.pdf
[taiwan]: handouts/TaiwanTST/TaiwanTST.pdf
[english]: handouts/english/english.pdf
