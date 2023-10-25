title: Asy guide
header: Asymptote Guide
description: Notes on how to set up Asymptote with LaTeX.
menu-position: 68
indent: 1

---

This was originally [LaTeX FAQ L-8](faq-latex.html#L-8),
but it became so long that I decided it deserved its own page.

# Video screencast

<iframe width="448" height="252" src="https://www.youtube-nocookie.com/embed/fhe7atsYLuw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Gallery

Here are some examples of pictures you can make with Asymptote.
You can [view the source code on GitHub][asy-gallery].

[asy-gallery]: https://github.com/vEnhance/web.evanchen.cc/tree/main/static/asy-gallery

<div class="photo-gallery">
{{ clickable_asy_image("321avoid") }}
{{ clickable_asy_image("AMC-12B-2022-21") }}
{{ clickable_asy_image("EGMO-2015-2") }}
{{ clickable_asy_image("IMO-2017-5") }}
{{ clickable_asy_image("Jan-TST-2013-3") }}
{{ clickable_asy_image("Mexico-2020-3") }}
{{ clickable_asy_image("Napkin-cproj2") }}
{{ clickable_asy_image("open-cover") }}
{{ clickable_asy_image("ST-Napkin-Extn") }}
{{ clickable_asy_image("TSTST-2020-1") }}
{{ clickable_asy_image("USAMO-2009-3") }}
{{ clickable_asy_image("USAMO-2017-5") }}
</div>

---

# Prerequisites

First, if you haven't already, make sure you know everything in
the [File systems beginner page](https://web.evanchen.cc/filesys.html).
If you don't understand how files work, this page will not make much sense.

You should have a working local LaTeX installation working,
as described in [LaTeX FAQ](faq-latex.html).
(Overleaf is _not_ sufficient for this tutorial;
see [FAQ L-2](faq-latex.html#L-2a) for why.)

You can verify you have LaTeX installed by typing

`pdflatex --version`

into a command line; this should give an output like

```text
pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Arch Linux)
kpathsea version 6.3.5
Copyright 2023 Han The Thanh (pdfTeX) et al.
(and so on...)
```

You should also have Asymptote installed.
Check the [installation instructions on the Asymptote website][asy-install].
If that's working, you should be able to type

`asy --version`

into a command line and obtain a version number.
(If you're using Windows with MikTeX, this might pull a really
old version of `asy` that's bundled into MikTeX,
which has been [known to cause issues][miktex-asy-bug].
You may have to instead type the long string
`"C:/Program Files/Asymptote/asy.exe"` instead of `asy` in what follows.)

[asy-install]: https://asymptote.sourceforge.io/doc/Installation.html
[miktex-asy-bug]: https://tex.stackexchange.com/q/666218/76888

---

# The main workflow

Once you have Asymptote installed, to integrate it with LaTeX,
the compilation workflow requires three steps.

1. Run PDFLaTeX on, say, `meow.tex`.
   This creates `meow-N.asy` for the N'th diagram.
2. You need to then run the Asymptote binary on `meow-N.asy` to generate `meow-N.pdf`.
3. The diagram `meow-N.pdf` then gets incorporated when you run PDFLaTeX again.

This is shown in detail in the video at the top of the page.
Here's the sample file if you want to copy and try it yourself.

```tex
\documentclass[11pt]{article}
\usepackage{asymptote}
\begin{document}
\title{Meow}
\author{Twitch Solves ISL}
\maketitle
\begin{center}
\begin{asy}
  size(6cm);
  draw(unitcircle);
  draw( (0.3,0.3)--(0.3,0.4) );
  draw( (-0.3,0.3)--(-0.3,0.4) );
  draw( (0.6,-0.2)..(0,-0.4)..(-0.6,-0.2) );
\end{asy}
\end{center}
\end{document}
```

To reiterate, the 3 commands you should be running
(after `cd`-ing to the directory with these files, of course) are:

```sh
pdflatex meow
asy meow-1.asy
pdflatex meow
```

---

# Automating the workflow with latexmk

In principle, you can run this three-step process by hand each time
you change the diagrams on your page. But this is super annoying.

Fortunately, there's a program called `latexmk` which,
among many other nice LaTeX features, can help run this entire process for you.
I didn't show this setup in the video because it's OS-dependent[^lost]
but here are some hints about how you might do this.

[^lost]: It may be a lost cause on Windows, for example.

Of course, you should first install `latexmk`.
Matthias Geier has installation instructions on [mg.readthedocs.io][mg].
As before, you can verify it's installed by seeing if `latexmk --version`
produces a sensible output:

```text
Latexmk, John Collins, 7 Jan. 2023. Version 4.79
```

Now, as explained on [mg.readthedocs.io][mg] above about "crazy stuff",
`latexmk` has a configuration file called `latexmkrc` that lets you define subroutines.
The Asymptote authors, recognizing the power of `latexmk`, wrote such a
[subroutine](https://raw.githubusercontent.com/vectorgraphics/asymptote/HEAD/doc/latexmkrc)
for automatically compiling only changed Asymptote diagrams.
If you copy-paste these lines into latexmk's configuration file,
it should automatically do the right thing.
See the [LaTeX usage page](https://asymptote.sourceforge.io/doc/LaTeX-usage.html)
for further instructions on how to do this.

[mg]: https://mg.readthedocs.io/latexmk.html

---

# Advanced stuff

## Olympiad geometry macros

If you're using Asymptote to typeset diagrams,
chances are you'd appreciate having commands like `circumcircle`.

Back in 2007, the Art of Problem-Solving community had this issue,
and they actually wrote their own packages called
`olympiad.asy` and `cse5.asy` with definitions for these commands.
However, this is probably _not_ the solution you want to use[^links],
because it means you have to rely on some nonstandard packages written by
some math olympiad enthusiasts that you'd have to copy back and forth between
every computer you use. It would be a major nuisance, to say the least.

[^links]:
    If you really want, though, you can download a copy of these two packages
    from [my dotfiles](https://github.com/vEnhance/dotfiles/tree/main/asy).
    I have these because a bunch of legacy code sometimes uses them.

Instead, Asymptote has a built-in module called `geometry` already,
that does almost everything you would want in practice.
You could read
[the geometry manual](https://web.archive.org/web/20180417141555if_/http://www.piprime.fr:80/files/res/geometry_en.pdf)
for instructions on how to use it,
or the page
[on the Asymptote website](https://asymptote.sourceforge.io/doc/geometry.html),
but you could probably also just copy Evan's code as a template
and that might be easier than reading the fairly long manual.
Read on to the next section to see how to do this.

## Using asydef for geometry and other purposes

In practice, there are some setup commands I want to have automatically done for
every Asymptote picture that I draw.
For example, I like to `import geometry;` and then define a
few extra commands that I often use, like `foot`.
I also like to make sure `amsmath` and `amssymb` are active,
and set a reasonable default size for the picture, etc.

If you happen to be using my LaTeX template `evan.sty`,
as described in [LaTeX FAQ L-3](faq-latex.html#L-3) and
[LaTeX FAQ L-4](faq-latex.html#L-4),
then in fact all of my Asymptote shortcuts are already done for you.
Just `\usepackage{evan}` and you should be good to go.

Otherwise, the way to do this is to stick an `asydef` environment
right after `\usepackage{asymptote}` but before `\begin{document}`,
containing whatever extra definitions you want to use everywhere.
You can copy the one from
[evan.sty on GitHub](https://github.com/vEnhance/dotfiles/blob/main/texmf/tex/latex/evan/evan.sty)
if you like; look for the lines `\begin{asydef}` and `\end{asydef}` and copy
everything in between into your preamble. This is shown in the video.

## Exporting from GeoGebra

GeoGebra Classic 5 supports exporting GeoGebra figures to Asymptote code
directly that you can include in your file.

However, the source code generated by this is in my opinion not easy to read.
I ended up writing my own [Python script][ggb-clean]
to make the source code output a little more presentable;
you can pipe the copied Asymptote code to standard input to this program.

As an example, you can watch me export a diagram for IMO 2023/2 at
[1:08:20 of this video](https://youtu.be/Alz2OWHH7QY?si=ERpn8N2to5t01W9A&t=4100)
from [my Twitch stream](videos.html).

[ggb-clean]: https://github.com/vEnhance/dotfiles/blob/main/py-scripts/export-ggb-clean-asy.py

## Bonus: Using CJ Quine's TSQX

If you really pay attention to Evan's stream,
you might notice that Evan often generates olympiad geometry diagrams
by writing what looks like pseudocode that magically transpiles to Asymptote.
(One example is
[5:55 of this video](https://youtu.be/wMdc6hUhhaA?si=jMwl5qUx_baomfXp),
where a diagram from GeoGebra on the left half of the screen
is redrawn manually on the right half of the screen for better quality.)

The way this is done is that CJ Quines and I wrote a
[Asymptote preprocessor](https://github.com/cjquines/tsqx)
where you can write something like

```text
~triangle A B C
D ;= foot A B C
E := midpoint A--B
F' N = (rotate -30 E)(extension A (foot A B C) C E)

circumcircle A B C / 0.2 lightgray /
A--B--C--cycle
A--D
B--F' / dashed blue
```

to get [this figure](https://github.com/cjquines/tsqx)!
It's a Python script, so this will only be useful to you if you know
how to run a Python script.

## Help

If you need help, in my [public Discord](discord.html), there's a channel
called `#latex-asy-help-!mwe` that you might drop by.[^otisdiscord]
Remember to provide [minimal examples](https://texfaq.org/FAQ-minxampl).

[^otisdiscord]: For [OTIS](otis.html) students, the OTIS Discord has an analogous channel called `#latex-asy-linux-git-etc`.

Emails to me may or may not work.
