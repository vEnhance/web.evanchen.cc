title: Linux FAQs
header: Linux FAQs
description: Some FAQs about Linux and the like.

---

[Return to FAQ Index.](faqs.html)

These are FAQs about software I use.
You might also see [LaTeX FAQs](faq-latex.html).

### {{ faq("X-1", "If I don't know anything, where do I start?") }}

Check the [plz learn code](techsupport.html) page.

### {{ faq("X-2", "What programming language should I learn first?") }}

I recommend [Python](http://openbookproject.net/thinkcs/python/english3e/index.html)
but plenty of other languages are OK too.
Prospective competitive programmers (IOI, etc.) should learn C++.

I personally anti-recommend PHP and JavaScript because I think weakly typed
languages are not good for learning.
(I have no stance on duck typing vs static typing though.)
HTML and CSS are _not_ programming languages, they are markup languages.

### {{ faq("X-3a", "Why do you use Linux?") }}

If I had to summarize this in one word, it would be "control".

I insist my computers are fully transparent and configurable.
I want to be able to see every dial and knob and turn them as I please.
In exchange, this means investing time to learn how my computer works,
doing my own homework (aka search engine) whenever issues arise,
and writing my own tools when no existing software fits my needs.
This process is time-consuming but
[I enjoy it](https://xkcd.com/974/) so I am happy with this cost.

Also, [Linux package management is amazing](https://itsfoss.com/package-manager/).
If one day I hear about a program called Geogebra,
I can install it by typing `sudo pacman -S geogebra` into my command line
(here `pacman` is the Arch Linux package manager).
That's _it_. You do not even need to open a web browser.

### {{ faq("X-3b", "Should I try Linux?") }}

- If you're not willing to use search engines to do your own homework
  when you don't know something, then no.
- If you're just learning how to code, then maybe.
  Some people think it's too overwhelming to learn both at the same time,
  others think that Windows is so bad for programming that
  it's actually easier to switch to a beginner-friendly Linux
  and deal with both at the same time. Up to you.
- If you want to do serious programming (say, building a nontrivial website,
  or doing intensive calculations that require special libraries),
  you should consider switching more strongly. The truth is that the
  [majority of programmers use Linux](https://www.reddit.com/r/linux/comments/vytkf),
  and hence languages, development tools, libraries and so on
  tend to be Linux-targeted.
  The situation for Windows and OSX has gotten better over time,
  but practically speaking I don't think setting up a development environment
  is ever going to be easier on a commercial OS than on Linux.
- If you're curious, then yes, try it out. It's free.
  If you don't like it after trying it, switch back.
  Just be aware there's a bit of learning curve depending on which
  distribution you pick up.

### {{ faq("X-4a", "Why do you use Arch Linux?") }}

I've only used Ubuntu and Arch Linux.
I switched from Ubuntu to Arch Linux because Arch

- was faster;
- was more lightweight (basically nothing installed by default);
- was more transparent;
- has significantly more up-to-date package repositories;
- has a [do-it-yourself philosophy](https://wiki.archlinux.org/title/Arch_Linux#Principles).

To me Ubuntu is sort of the midpoint of Windows and Arch Linux.
It's a _bona fide_ Linux system, but there are a lot of pre-installed parts
and a lot of things that are hidden behind graphical interfaces.

### {{ faq("X-4b", "Should I switch to Arch Linux?") }}

Only if you really like doing homework ;)

Note well: if you are new to Linux, installing Arch will be a trial by fire.
This is not necessarily a bad thing; it might actually be better this way if
your goal is to learn about systems, because by the end of the process, you will
know way more than you started with. Just be aware of it and probably block out
a week or two.

### {{ faq("X-4c", "Which Linux distribution should I use?") }}

I've only tried two distributions, so I have no comment here, sorry.
Search the web.

### {{ faq("X-5", "Why are you so obsessed with the terminal?") }}

I think the analogy in my head is like, when you use a terminal, you are kind of
"talking to the computer directly", rather than going through some user interface.
It's sort of like, once you know LaTeX, you wouldn't want to go back to the
mouse-based equation editor, because it's faster to just type `\frac12x^2+3`
than to click on the fraction button, then type 1 and 2, then press the exponent
button, and so on. Using the command line is like that but one level higher ---
it controls all the files and applications.

Here's an example of one way being able to talk directly helps.
Terminal commands have something called _standard input_ and _standard output_.
So, programs can read in text from a stream (or file, etc.),
and they will print the output to terminal by default.
Meaning you can compose the programs together with
[pipes](https://en.wikipedia.org/wiki/Pipeline_%28Unix%29),
feeding the output of one program to the output of another.

For example, suppose you have a program `foo` that downloads the list
of participants on a contest sorted by score.
I want to find all the participants with surname Chen,
sort them alphabetically, and then put the result on my clipboard.
Roughly, this is `foo | grep Chen | sort | xsel --clipboard`.

Of course, without a terminal you _could_ also run a graphical program,
open Google sheets, copy the results in, use the filter menu,
then sort it, and finally Ctrl-C the result. But why be so roundabout?
You know what you want, just say it.

Pushing this example ever further,
if you find yourself doing this exact sequence several times,
you can write `alias meow="foo | grep Chen | sort | xsel --clipboard"`.
Then in the future you can just type `meow` and have this done in four keystrokes.

The fact that all terminal programs read and write
in a uniform way is exactly what makes this possible.
Programmers like this simplicity and elegance.
They like it so much that software made for sophisticated users
often doesn't bother to provide a graphical interface.
This is the same reason why command line flags or
configuration files tend to be text-based on Linux:
this means they can be manipulated in any editor,
[transferred from one computer to another via Git](https://github.com/vEnhance/dotfiles),
and so on.

Also, Fish autocomplete is life-changing 🐟 ❤️ 🔥
(zsh is good too I hear.)

### {{ faq("X-6a", "Why (Neo)Vim?") }}

Pretty similar to reasons I use Linux.

- It is extremely customizable, both by
  [text](https://github.com/vEnhance/dotfiles/blob/main/vimrc),
  and by a gazillion plugins (also via text)
  for IDE-like features and autocomplete and so on.
  (On the scale of Vim users, I lean feature-heavy over lightweight;
  I use both ALE and CoC.)
- Any Linux computer will have it.
- It's fast.
- It is programmable. If you want to, say,
  toggle the case of the first character of the next 100 lines,
  you type `qa~j^q99@a`. You don't need any external program.
- Most importantly, it is a [modal editor](https://en.wikipedia.org/wiki/Vi#Interface).

The last item is the most important one for me,
and also the one that will be most foreign to newcomers.
Modal editing which means that there are different _modes_
for entering text versus navigating the document that you constantly switch between.
So when you are typing new text, Vim behaves much like a standard editor,
with every keystroke adding one character.
But when you are _editing_ or _moving_,
instead _every keystroke is a command_ (no ctrl needed).
Here's a picture of what my cheat sheet looks like:
[taken from vi-emu](https://boredzo.org/vi_tutorial/vi_tutorial-Dvorak-Color.pdf)
(Dvorak keys):

![Power overwhelming.](static/vim-dvorak.png)

That means that if when you want to do a specific thing like
"go to line 100" or "go to the end of this paragraph",
you can _type what you want_ (`100G` or `}` respectively in this example).
The entire keyboard lets you navigate: basically every single key
becomes a navigation tool like "go to end of line", "delete line",
"copy line", "append to end of line", and so on.
[More comprehensive.](https://stackoverflow.com/a/1220118)

The main downside to Vim is that there is a learning curve.
I paid that price long ago 😉

### {{ faq("X-6b", "Emacs?") }}

¯\\\_(ツ)\_/¯

### {{ faq("X-6c", "Editor recommendations for beginners?") }}

Reproducing [from the learning path](techsupport.html#editors):

For beginners, there are a _ton_ of "basic" text editors that
support syntax highlighting and some basic quality-of-life features,
and are simple to use.
Some of the popular ones include

- [FeatherPad](https://en.wikipedia.org/wiki/FeatherPad);
- [Geany](https://en.wikipedia.org/wiki/Geany);
- [gedit](https://en.wikipedia.org/wiki/Gedit);
- [Notepad++](https://notepad-plus-plus.org/) (only Windows);
- [Sublime](https://www.sublimetext.com/).

[Visual Studio Code](https://en.wikipedia.org/wiki/Visual_Studio_Code)
(abbreviated VS Code) is also extremely popular,
although it's a bit more sophisticated than the beginner ones above.
