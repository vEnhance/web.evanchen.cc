title: plz learn code
header: Speech on why coding is important
menu-position: 60

---

Are you scared by watching Evan's fingers repeatedly smashing
the wrong keys and things would somehow work anyway?
Have you tried using LaTeX and found that nothing made sense?
Are the lotus-eaters trying to convert you into the cult of Vim?
Have you just been overwhelmed by all the black magic that
Evan and his orz-ers seems to exercise like it's nothing?

(Or are you just here because of the $N = p^2+q^3$ question
on the OTIS application? Good, it's working.)

If so, these pages may be for you.

> You're much better off using code as your secret weapon in another profession.
> People who can code in the world of technology companies are a dime
> a dozen and get no respect. People who can code in biology, medicine,
> government, sociology, physics, history, and mathematics are respected and can
> do amazing things to advance those disciplines.
>
> --- [Zed A. Shaw](https://learnpythonthehardway.org/python3/advice.html)

This page will attempt to convince you to learn to code and how to get started.
For LaTeX stuff, see [FAQs on LaTeX](faq-latex.html).
For more advanced thoughts like why Vim or why Linux,
see [FAQs on Linux](faq-linux.html).

---

## Long speech

If you found my website, you are presumably someone
who likes learning and thinking.
If you are such a person, and you don't know how to code,
here is my advice for you: **sit down and learn it**.

Seriously, [learn to code](https://youtu.be/TYCxbFad36g?t=2070).
Learn. To. Code. Learn to code god-damn it!

[![Tiny Evan knows Python. You can too!][tiny]{width=90%}][tiny]
{class=text-center}

[tiny]: static/learnpython.jpg

I don't think everyone should be able to solve IOI problems[^ioi].
But I am adamant you should at least have a basic understanding
of how computers work, and be able to automate trivial tasks.
For example, you should be able to write a script that
batch renames the files `a1.out`, `a2.out`, ..., `a100.out`
to `output001.txt`, `output002.txt`, ..., `output100.txt`.
Or to [hack together a program](https://blog.evanchen.cc/2020/12/16/usemo-problem-development-behind-the-scenes/)
that reads the data from a Google form,
and sums the result into a table that you can send out.

[![Not made by hand][usemo]{width=90%}][usemo]
{class=text-center}

[usemo]: https://usamo.files.wordpress.com/2020/12/table.png

Unlike something like quadratic formula or differentiation,
most careers _directly_ benefit from some computer literacy[^think].
Programming is so efficient that, once you achieve a basic amount of literacy,
the extra productivity will rapidly repay the time invested in learning.
But making cumbersome tasks merely _faster_ is not the true reward;
the real payoff is changing _outright impossible_ into _straightforward_.

I think _every single job_ I've had since leaving high school used programming
in some way. Here are just a few examples:

- [arXiv:1708.01350](https://arxiv.org/abs/1708.01350) was one of the strongest
  papers I obtained from the Duluth REU.
  I got the result by writing a C++ program to work out several million cases
  and then using engineer's induction on the output.
  It took a whopping one afternoon.

- [OTIS](otis.html) was already using Python scripts by the time there were 10
  students. Today, there are more than 300 students,
  and the program runs on its own [dedicated Django server, OTIS-WEB][otisweb].
  It would simply not be possible to run OTIS without OTIS-WEB.

- Running [MOP](https://web.evanchen.cc/mop.html) involves a lot of Python
  scripts now for things like collating tests, printing score packets, etc.
  I think it would be unmanageable otherwise.

- Running [Mystery Hunt](https://en.wikipedia.org/wiki/MIT_Mystery_Hunt)
  requires extensive code not only to set up the hunt website,
  but even just to manage the problem-writing process,
  to say nothing of things like interactive puzzles.

  And then even individual puzzles can require code that the audience never
  sees. The logic puzzles in [Flooded Caves](https://puzzlefactory.place/puzzles/flooded-caves)
  used [grilops](https://github.com/obijywk/grilops) as a way to
  search for interesting configurations and verify uniqueness; while
  [Escape From Life](https://puzzles.mit.edu/2021/puzzle/escape-from-life/)
  involved overnight CPU computations to find configurations that produced
  the correct letters. The list goes on.

  Solving puzzles is, of course, greatly aided by code as well,
  and in some cases essentially required.

- The [Automatically Generated EGMO Solutions Treasury](https://web.evanchen.cc/textbooks/AGEST.pdf)
  is true to its name --- it's auto-compiled from
  [the problem database I wrote myself](https://github.com/venhance/von).
  The OTIS Excerpts, MOHS rating chart, and the various solutions files
  on this website's [problems page](https://web.evanchen.cc/problems.html),
  as well as the list of solved YouTube problems,
  were all produced using Python scripts as well.

- This website was generated by
  [Markdown and Python](https://github.com/vEnhance/web.evanchen.cc).

And so on.
To put it bluntly, not knowing how to code will severely cripple
the space of things you're able to work on.

## Getting started

- Read on about [files and folders](filesys.html).
- See [the learning path](techsupport.html)
  for advice about things like what language to work with.

[^ioi]:
    The IOI is an algorithmic contest,
    which means that part of the problem is first _finding_ an algorithm,
    and after that actually _implementing_ it in C++.
    I'm here to say that even the latter ability alone is valuable,
    even if you never learn graph theory or Dijkstra's algorithm.

[^think]:
    I, and several others, also suspect that knowing programming changes
    the way you think. But this is harder to measure or prove, so I only stated the
    weaker claim.

[otisweb]: https://github.com/vEnhance/otis-web
