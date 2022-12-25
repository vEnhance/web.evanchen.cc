title: LaTeX FAQs
header: LaTeX FAQs
description: Some FAQs about LaTeX

---

[Return to FAQ Index.](faqs.html)

These are FAQs about LaTeX.

Before anything else, I need to define some terms.
You can think of LaTeX workflow as having three components:

1. A **text editor** that you type your content into,
   like gedit, Sublime, Vim, or Emacs.
   (See [tech briefing](filesys.html#editors) for details.)
2. A **LaTeX compiler** (aka **LaTeX distribution**)
   that converts the source into a PDF.
   See question [L-10](#L-10) for recommendations.
3. A **PDF viewer**, the same one you use for normally viewing PDF's.
   See question [L-12](#L-12) for recommendations.

What you need to know right now is that **these three components are disjoint**.
Some text editors may let you invoke a compiler directly,
and others may be designed specifically for LaTeX editing,
but it is a mistake to confuse the editor with the compiler.
Any text editor will work with any compiler will work with any PDF viewer.

### {{ faq("L-1", "I don't know anything. Where do I start?") }}

[Read Wikibooks](https://en.wikibooks.org/wiki/LaTeX), it's really comprehensive.
Also, [this tutorial is good too](https://www.latex-tutorial.com/tutorials/).

See also the [example file](https://web.evanchen.cc/handouts/TeXSample/TeXSample.tex).

### {{ faq("L-2a", "What about online suites like Overleaf?") }}

I think it's better long-term to install LaTeX on your computer.
I realize that people want something that "just works" with no additional effort.
But for frequent usage, there are downsides:

- You do not have much control over the editor or viewer.
- You do not have control over package versions, or custom packages
  (besides manually making a copy of a package each time you need it).
- It's slower, because you need to do repeated round-trips to an external server
  for compilation and viewing.
- If you use Asymptote, any errors are silently discarded.

More bluntly, just install LaTeX, you only have to do it once.

Overleaf certainly has its uses; most notably, its strength is _collaboration_.
For example, sometimes I have to work with colleagues that are too incompetent
to learn how to use [Git](https://en.wikipedia.org/wiki/Git).
In that case, it's easier for me to throw an Overleaf at them
(and then use the underlying Git myself).
Or, sometimes I am stuck on some library computer,
making it impossible to install my own software. That does happen.

But I think it's not good for learning though, see the next question.

### {{ faq("L-2b", "How do I get X to work on Overleaf?") }}

First install LaTeX properly, then if it still doesn't work write to me again.
(Usually this fixes the issue because it forces the asker to actually
[do their homework](http://catb.org/~esr/faqs/smart-questions.html#intro). 😉)

### {{ faq("L-3", "Your documents are pretty, can I use your formatting?") }}

Yes, it's contained in the style file
[evan.sty](https://github.com/vEnhance/dotfiles/blob/main/texmf/tex/latex/evan/evan.sty).
Attribution is required in source versions only,
and not mandated in PDF output (though still appreciated).
Check the license that appears.

You should either copy-paste the 600-ish lines of code into a text file,
or else click "Raw" and save the file.

### {{ faq("L-4", "How do I use a custom style file like evan.sty?") }}

[Check Google.](https://www.google.com/search?q=where+to+put+latex+custom+package)
Or [see Wikibooks](https://en.wikibooks.org/wiki/LaTeX/Creating_Packages#Creating_your_own_package).
The source itself looks something like:

```latex
\documentclass[11pt]{article}
\usepackage{evan}
\begin{document}
\title{Example of a Title}
\maketitle
\end{document}
```

### {{ faq("L-5", "How do I get the colored boxes and section headers with evan.sty?") }}

Pass the `sexy` option to the package
(see source code for more detailed breakdown of options).
Colored sections will then happen automatically if you are using `scrartcl`
(rather than `article` or `report`).
For the theorem environments in colored boxes, use the provided theorem environments.
See examples in [FAQ L-9](#L-9).

### {{ faq("L-6", "What package did you use to typeset your CV?") }}

I use [moderncv](https://ctan.org/pkg/moderncv?lang=en).
You can [download the TeX source of my CV](static/CV-example-source-2020.tex)
(with slight modifications for simplicity; this link is not updated).

### {{ faq("L-7", "How do you get the LaTeX to auto-compile?") }}

Use [`latexmk`](https://personal.psu.edu/~jcc8/software/latexmk/)
with the `-pvc` flag,
and a PDF viewer that does not "lock" the PDF file from being written
(Adobe reader does not work).

To fit `latexmk` into the framework we described,
it is a "wrapper script" that calls the compiler for you.

### {{ faq("L-8", "What do you use to typeset geometry diagrams?") }}

I use [Asymptote](https://asymptote.sourceforge.io/doc/index.html#SEC_Contents).
It integrates well with LaTeX;
for example, here is a document that compiles to a picture of a circle.

```latex
\documentclass{article}
\usepackage{asymptote}
\begin{document}
\begin{asy}
size(6cm);
draw(unitcircle);
\end{asy}
\end{document}
```

However, the setup to make this functional requires some work ---
there is both a separate _installation_ process for Asymptote,
and then a separate _compilation_ process to actually render the figures.

First, one needs to install the Asymptote program itself
(this is a separate program from LaTeX).
Check the [installation instructions][asy-install].

[asy-install]: https://asymptote.sourceforge.io/doc/Installation.html

Once you have Asymptote installed, to integrate it with LaTeX,
the compilation workflow requires three steps.

1. Run PDFLaTeX on, say, `example.tex`.
   This creates `example-N.asy` for the N'th diagram.
2. You need to then run the Asymptote binary on `example-N.asy` to generate `example-N.pdf`.
3. The diagram `example-N.pdf` then gets incorporated when you run PDFLaTeX again.

In principle, you can run this three-step process by hand each time
you change the diagrams of your figure.
This is annoying though, so if you use `latexmk` you can automate this process
by putting the provided
[subroutine](https://raw.githubusercontent.com/vectorgraphics/asymptote/HEAD/doc/latexmkrc)
into the `latexmkrc` configuration file.
See the [LaTeX usage page](https://asymptote.sourceforge.io/doc/LaTeX-usage.html)
for instructions on how to do this.

If you use a web-based compiler like Overleaf,
then things may not work so well since you do not have control
over the compilation process.
As mentioned in [L-2](#L-2a), my recommended solution is to
not use web-based compilers.

CJ Quines wrote a really nice
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

to get [this figure](https://github.com/cjquines/tsqx),
which makes it much easier to use.

### {{ faq("L-9", "Can I see some example source code?") }}

Yes, go to [Olympiad page](olympiad.html)
and to download TeX source.
(The geometry handouts will have diagrams.)
You can also look at [Napkin source code](https://github.com/vEnhance/napkin/).

### {{ faq("L-10", "Which LaTeX distribution do you recommend?") }}

- Windows: [MikTeX](https://miktex.org/)
- Mac: [MacTeX](https://www.tug.org/mactex/)
- Linux: [TeX Live](https://en.wikipedia.org/wiki/TeX_Live),
  almost certainly available from your package manager
  (e.g. `pacman -S texlive-core` or `apt install texlive`)

### {{ faq("L-11", "Which text editor do you use/recommend?") }}

I use [NeoVim](https://neovim.io/) with
[LaTeX Suite](http://vim-latex.sourceforge.net/index.php?subject=manual&title=Manual#user-manual).
But that is a pretty advanced setup, so if you are a beginner,
it may be overwhelming to learn Vim and LaTeX at the same time.

For now, you may prefer to stick with whatever text editor you are used to.
(Note that the editor does not need to be specific to LaTeX,
[any source code editor will work](https://en.wikipedia.org/wiki/Source-code_editor).)

If you _don't_ have a source code editor yet
because you ignored my advice to [learn how to code](techspeech.html),
then see the [FAQ X-6c](faq-linux.html#X-6c)
for some suggestions.

### {{ faq("L-12", "Which PDF viewer do you use?") }}

I use [Zathura](https://pwmt.org/projects/zathura/).

[Evince](https://en.wikipedia.org/wiki/Evince) and
[Skim](<https://en.wikipedia.org/wiki/Skim_(software)>) are also good.

### {{ faq("L-13", "How did you get randomized hint order in your geometry textbook?") }}

It's a bit of a hack, but here is [demo code](static/random-hints.tex)
corresponding to the version used in my geometry book.

Dennis Chen wrote a more sophisticated version `scrambledenvs`,
[available on GitHub as chennisden/scrambledenvs](https://github.com/chennisden/scrambledenvs).
If you have TeX Live 2021, you can just run `tlmgr install scrambledenvs`.
Otherwise, follow the installation instructions at
[this GitHub gist](https://gist.github.com/chennisden/84c2224b10f0b177e4726db0bec45381).

### {{ faq("L-14", "How do you live-TeX your notes so quickly?") }}

The main contributing factors are:

- My typing speed is quite high, at around 650 characters per minute.
- NeoVim (see [L-11](#L-11)) is fast.
- Several additional custom keyboard shortcuts specifically for TeX,
  see the vim folder in [my dotfiles](https://github.com/vEnhance/dotfiles).
- I have `conceal` enabled in Vim, so I can read my source code more easily.
- I use latexmk to auto-compile ([L-8](#L-8)).

I have been using Vim and LaTeX since I was a teenager,
so I am quite proficient with both.

### {{ faq("L-15", "How did you integrate your problem database with LaTeX?") }}

I [wrote my own database software in Python](https://github.com/vEnhance/von).

### {{ faq("L-16", "What's the best way to learn new things in LaTeX?") }}

Two things:

- Read the source code of other people;
- Search on Google and [tex.SE](https://tex.stackexchange.com/).

### {{ faq("L-17", "How can I look up a symbol?") }}

Use [Detexify](https://detexify.kirelabs.org/classify.html).

### {{ faq("L-18", "How can I have space between my paragraphs?") }}

You can use `\setlength{\parskip}{1ex plus 0.5ex minus 0.2ex}`.
You can also add `\setlength{\parindent}{0pt}` to suppress indents.

But don't do this, it looks terrible.
Indents are a better way of separating paragraphs.

### {{ faq("L-19", "What do you use for slideshows (e.g. on Twitch stream)?") }}

[Beamer](http://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf).

### {{ faq("L-20", "How do you get LaTeX on WordPress blog?") }}

I used to use [this Python2 script](https://lucatrevisan.wordpress.com/latex-to-wordpress/);
later I updated it to
[Python3](https://github.com/vEnhance/dotfiles/blob/main/py-scripts/latex2wp.py).
Not that elegant, but works.

### {{ faq("L-21", "My code doesn't work / I want to do X, what should I do?") }}

Prepare a [minimal working example](http://tug.ctan.org/info/dickimaw/dickimaw-minexample.pdf)
and ask on [tex.SE](https://tex.stackexchange.com/).

### {{ faq("L-22", r"Why do you anti-recommend \dfrac or \displaystyle?") }}

If your expression is so complicated that it isn't legible without using
`\dfrac` or `\displaystyle`, then it should probably be displayed.

### {{ faq("L-23", r"Any common mistakes?") }}

[Thought you'd never ask][petpeeve].

[petpeeve]: https://web.evanchen.cc/handouts/LaTeXPetPeeve/LaTeXPetPeeve.pdf
