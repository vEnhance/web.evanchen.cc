title: For coaches
header: Math olympiad coach's page
description: Pointers for math olympiad trainers
indent: 1
menu-position: 32

---

This page contains some pointers for coaches who are looking for advice
on how to help prepare their students for math olympiads,
particularly in countries new to the International Math Olympiad.

I would be extremely grateful for suggestions for more content to link here.
You can either email me suggestions directly,
or better yet, [submit a pull request](https://github.com/vEnhance/web.evanchen.cc/edit/main/input/coaches.md).

## {{ hl("general", "A few general truisms") }}

- Prioritize talent development over mere talent identification.
- Don't worry too much about initial results seeming slow.
  The best-case scenario for a coach is to have a system
  with exponentially growing returns,
  and exponential functions are _supposed_ to look flat near $t=0$.
  So if you can somehow ensure your growth curve maintains exponential _shape_,
  then all that remains is to be patient.
- Once your students pass the critical point where they understand
  what a proof is and can verify correctness of proofs independently,
  you should gradually shift from teaching specific lessons
  to [teaching them how to fish for themselves][fishquote].
  Strive to eventually become a guide rather than a lecturer.
  - In particular, as students get stronger, you may consider moving emphasis
    from specific techniques and theorems (induction, invariants, ...) to
    less formalizable [heuristics and understanding][hardsoft].
- It's important that your systems work _in practice_, not just in theory.
  For example: if you send monthly problem sets during the school year,
  and nobody does them, it's tempting to say,
  "well, the students didn't do the problems I sent, it's not my fault".
  And sure, maybe it isn't your fault, but that doesn't change the end result.
- Fellow MO coaches are always welcome to email me with questions or for advice.
  Specific inquiries are usually better than generic ones. Something like "can
  you look at this lesson plan and give suggestions" is both easier for me to
  answer (because it’s so concrete) and also more informative for you (because
  it's so targeted). In general the more concrete the better.

[fishquote]: https://en.wiktionary.org/wiki/give_a_man_a_fish_and_you_feed_him_for_a_day;_teach_a_man_to_fish_and_you_feed_him_for_a_lifetime
[hardsoft]: https://blog.evanchen.cc/2019/05/03/hard-and-soft-techniques/

## {{ hl("blog", "Top teaching posts from Evan's blog") }}

- [Running OTIS](https://blog.evanchen.cc/2023/11/03/things-ive-found-from-running-otis/)
- [Point-based problem sets](https://blog.evanchen.cc/2018/03/27/i-switched-to-point-based-problem-sets/)
- [Selecting topics and designing materials](https://blog.evanchen.cc/2017/04/08/on-designing-olympiad-training/)

## {{ hl("talks", "Talks and interviews with trainers") }}

- [Interview with Song Yong-jin (2017)](https://www.youtube.com/watch?v=TlGl7Vikf5Y),
  the longtime beloved team leader from South Korea.
- [Slides to Evan's EXCL talk](/handouts/EXCL-2023-11-04-slides/EXCL-2023-11-04-slides.pdf)
  as part of Global Talent Network initiatives (November 2023).

## {{ hl("lore", "International Math Olympiad lore") }}

- The United Kingdom keeps
  [team leader reports](https://bmos.ukmt.org.uk/home/imo.shtml) for the
  International Math Olympiad.
  Earlier reports contain a lot of interesting stories
  and anecdotes about the proceedings of the IMO.
  It's as close as you can get to seeing the IMO in action without being there.
- Tom Verhoeff has a particularly comprehensive
  [report for IMO 2002](https://www.win.tue.nl/~wstomv/publications/imo2002report.pdf)
  that shows a lot about how the IMO works.
- [Evan's FAQ CR-10 about IMO coordination](faq-rules.html#CR-10).

## {{ hl("write", "Thoughts on problem writing and test-setting") }}

- [Bruce Reznick on Putnam development](https://faculty.math.illinois.edu/~reznick/putnam.pdf)
- [USEMO test development process](https://blog.evanchen.cc/2020/12/16/usemo-problem-development-behind-the-scenes/)
  (we use a similar process for USAMO and USA TST too)
- [Evan's problem-writing thoughts](https://web.evanchen.cc/handouts/ProblemWrite/ProblemWrite.pdf)
- Anecdotes and stories about the writing of certain problems
  - [David Speyer on math.SE](https://math.stackexchange.com/a/203448)
  - [Izabella Laba on Putnam](https://ilaba.wordpress.com/2009/11/22/putnam/)

## {{ hl("misc", "Other resources") }}

- The "math circles" movement was developed as a model of math enrichment at all
  levels, originating in Eastern Europe before appearing in the United States.
  Some resources for organizers can be found at
  [mathcircles.org](https://mathcircles.org/organizers/).
- [Excellence in Coaching and Leadership (EXCL) Program](https://www.globtalent.org/excl)
  run by the Global Talent Network.

## {{ hl("syllabus", "Tips for learning the math olympiad syllabus") }}

For the most part, the [resources for the students](wherestart.html)
will work equally well for coaches looking for ideas for what to teach.
You can also see my [unofficial syllabus](/handouts/Syllabus/Syllabus.pdf)
which is a rough map of the topics that show up in math olympiads.

If you have a degree in math or related field
but not much competition-specific experience,
here are some specific pointers for things to watch for:

- You likely have good experience working with proofs, proof methods
  like induction, and quantifiers like $\forall$, $\exists$.[^usasux]
  That's good, and you'll want to lean on it.

  I'll mention that olympiad problems have two new "types" of imperatives:
  "find all" and "find the minimum/maximum".
  As I explain in [sections 2.3-2.4 of English](/handouts/english/english.pdf)
  and in [chapter 1 of the OTIS Excerpts](excerpts.html),
  these problems are always implicitly two-part problems.
  This may be obvious to math majors, but my experience is students
  new to proofs often don't notice this until it's pointed out.

- The combinatorics problems in olympiads are _tricky_,
  but they are mostly not going to use any theory you haven't seen before.
  At most, they may use terminology from graph theory in solutions,
  but only for cosmetic reasons or occasionally basic facts like
  "no odd cycles implies bipartite".
  You're rarely going to need something like four-color theorem or graph minors.

  So for the most part, you can jump right in to the combinatorics section.
  You might not necessarily be able to solve all the problems,
  but you should be able to understand most of the solutions,
  and improve your solving ability with practice.

- Number theory is a little more involved, but not by that much.
  If you're comfortable working in $\mathbb Z/n\mathbb Z$
  and $(\mathbb Z / n\mathbb Z)^\times$ (a group with order $\varphi(n)$),
  you should be mostly fine and can pick up any stray remaining lemmas as you go.

  Like with combinatorics, many of you can simply dive in headfirst without any
  other special preparation.

- However, unlike combinatorics and number theory,
  the geometry problems may often quote results that you will probably have
  never seen before unless you have specific contest training.
  At the IMO, even beginner contestants are expected to know by heart the
  definitions of the four main triangle centers
  (incenter, circumcenter, centroid, orthocenter)
  and their basic properties (for example, the orthocenter's reflections
  across the sides of the triangle lie on the circumcircle).

  [I wrote a textbook showing the necessary theory](geombook.html),
  and think it's worth at least studying the first three fundamental chapters
  (which I think are publicly available via Google Books preview)
  before trying your hand at any of the problems.

- In the last 10 to 20 years there is a style of problem called a
  _functional equation (FE)_ which has become quite popular
  (although I do not enjoy it).
  These will also look quite alien to you; they usually involve ad-hoc
  manipulation of fairly artificial expressions
  and don't really correspond to any part of mathematics.
  You might want to read a handout or two on these specifically.

- Especially when starting out, you won't need much calculus or analysis.

[^usasux]: Lucky for you, because most American high school students don't.
