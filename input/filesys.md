title: Filesys concepts
header: File systems: Concepts for beginners
menu-position: 62
indent: 1

---

## {{ hl("intro", "Introduction (can be skipped)") }}

This explains at a high level the most basic types of objects[^0]
that any computer system will have.
It is meant to be a short briefing before you follow the instructions in the
[learning path](techsupport.html) page.

[^0]:
    To draw an analogy, imagine a friendly alien visiting Earth for first time.
    The tour guide might start by pointing out the big ball of fire in the sky
    and explain that it's the sun, where the Earth gets warmth and light.
    They might even go on to say the sun only works 12 hours per 24 hours,
    and each sun-revolution is called a day.
    Then they'll explain there are things called trees, and stuff called plants,
    some of which can be eaten for food, but which also provide critical oxygen.
    Of course, none of this is remotely enough data
    for the alien to settle in and live a life on Earth,
    but it sure is helpful as a start.

## {{ hl("topics", "Topics covered") }}

In the last 10 years, the ways users access files have changed dramatically.
For many students, even the concept of a "file" could be
challenging now, let alone an editor or compiler.

The goal for this post is to try and sort out some common conceptions.
It's attempting to write out what are some common confusions about different
_types_ of objects in computing world, and draw analogies to the real world.

Specifically, I want to talk about five kinds of things:

- Folders and files
- Editors
- Compilers / interpreter
- Terminal emulators
- Executing programs

## {{ hl("core", "Core concepts") }}

### {{ hl("folders", "Folders") }}

A **folder** is what it sounds like.
It hosts several items, each of which may be a file or a folder.
For analogy, **you can think of a folder as a huge building**,
so big that there are smaller rooms inside it (sub-folders).

Every folder is itself contained inside some folder.[^mac]
Well, except for a few top-level folders varying by system,
but you don't have to worry about ever interacting with that directly.

[^mac]: Apparently, Finder on OSX hides the home folder. Go figure.

**Folders are important because they help you organize files.**
Actually.
You should think of the "Downloads" or "Desktop" folder as
a physical desk.
It's fine to leave some papers on your desk if you are only going to need them
for a short while. What you should _not_ do is end up with 2 gigabytes of
unrelated stuff in your Downloads folder having no clue how to find anything.
That would be like throwing all your laundry in a
pile on the floor without even bothering to separate clean from dirty clothes.

### {{ hl("files", "Files") }}

A **file** is a piece of data; officially, a sequence of characters.
The characters are officially 0's and 1's,
but most often they're grouped into sets of eight bits called "bytes"
that map onto a set of printable characters
(01100001=97=A, 98=B, ...).
Files are stored in folders.

### {{ hl("plaintext", "Plain text files") }}

The simplest kind of file is a **text file** or **plain text file**,
in which the data simply spells out text.
For example if you had a file called `hello.txt`,
and its contents consisted of the 12 bytes "I am so cool",
that would be a plain text file.
Other examples:

- The source code for most programming languages is input in plain text format,
  such as in C++, Python, Go, Java, Lisp, etc. I actually can't think of a
  single example of a real programming language whose source codes are not in
  plain text format.
- LaTeX source files are in plain text too.
- This document being in Markdown is written in plain text format.
- HTML is considered plain text too. It may not be particularly _intuitive_
  plain text with `<div>` and `</span>` everywhere,
  but the encoding is at least human-comprehensible output.
- Most configuration files like `*.yaml`, `*.cfg`, `*.rc` are
  usually in plain text format.
- `*.txt` too I suppose :)

Files often have extensions like `*.py`, `*.tex`, `*.txt`. These are
meant to be hints for the operating system on what kind of file they are, but
they don't technically need to be there.[^win]

[^win]:
    For _Windows_ users, you should be aware
    Windows not only hides file extensions by default from you,
    but also tries to intimidate you when you do try to change extensions,
    e.g. "OMG changing the file extension might make the file unusable!!!"
    You can ignore this, because the file extension is just part of the file name
    that's customary (but not essential) in helping determine what kind of file is used.
    But it's better for learning to see the extensions, anyhow.

There are _counterexamples_, of course --- mainly for programs that use
their own encoding system, rather than standard A=97, B=98, ...

- Microsoft Word is one example, those documents use their own encoding that
  doesn't make sense to the uninformed, so only Word can really edit it.
  (It's sort of like, you live in an English-speaking country,
  but Microsoft Word will only read/write documents in Ishkashimi language,
  thus forcing you to keep using Microsoft Word.)
- PDF also uses its own compressed format.
- And of course, `*.tar.gz` or `*.zip` archive files use a different
  encoding to achieve compression that isn't possible with plain text.

But bottom line: **you can think of a file like a piece of paper.**
Which brings us to...

### {{ hl("editors", "Editors") }}

An **editor** is any program that manipulates the contents of a text file.
In other words, an **editor is like a pencil/eraser/pen**:
given a piece of paper, you can append, alter, or delete contents.

Because the most common file is a plain text file,
the most common editor is a **text editor**.
That's an editor that understand plain text files,
and can manipulate them in natural ways.
The beauty of this is the following principle,
which you must understand.

> **Important Principle: ANY text editor can edit ANY plain text file**.

For example, I am a die-hard user of
[Vim](<https://en.wikipedia.org/wiki/Vim_(text_editor)>).
(But I don't recommend Vim for beginners unless you like trial by fire.)
Others swear by [VS Code](https://en.wikipedia.org/wiki/Visual_Studio_Code),
and still others by [Emacs](https://en.wikipedia.org/wiki/Emacs).
There are simpler beginner editors too;
some are listed in [the learning path](techsupport.html#editors).

But the thing you need to understand is that choosing an editor does NOT
rely on what _kind_ of file you are editing, as long as it's plain text.
If you love Vim like me, you can use Vim for Python, for LaTeX, for C++, for
Markdown, whatever you like. You do not need a different editor per file type.

### {{ hl("compile", "Compilers and interpreters") }}

Compilers and interpreters are programs that take files as input and do something with them.
Maybe they make a copy in a different form, or execute some commands, or so on.

**You can think of a compiler or interpreter as a person
who accepts instructions in writing.**

For example, consider Monty Python, your friendly Python interpreter.
Suppose you give Monty a piece of paper called `beer.py` as follows:

```python
n = 100
while n >= 0:
  print(f"{n} bottles of beer on the wall, {n} bottles of beer!")
  print(f"Take it down, pass it around, {n-1} bottles of beer on the wall")
  n -= 1
```

Monty will read these instructions, and happily begin singing
one of the most obnoxious car songs of all time.

As another example, Leslie LaTeX is a friendly LaTeX interpreter.
You write a file called `nt.tex` as follows:

```latex
\documentclass[12pt]{scrartcl}
\title{A number theory problem}
\author{Evan Chen}
\date{November 16, 2021}

\begin{document}
\maketitle
Let $\theta$ be a real number such that
$\cos(20\theta)$ and $\cos(21\theta)$
are rational numbers.
Is $\cos(\theta)$ necessarily rational?
\end{document}
```

If you give this to Leslie, she'll look through for a bit
and then produce a beautifully typeset PDF file for you
that you can give to torment your math teacher. Wonderful!

The thing I need to hammer home now is that:

> **Important Principle: the compiler or interpreter
> neither knows nor cares what editor was used.**

It's none of the interpreter's business how you prepare your documents. You can
write in pencil, or fountain pen, or crayon, or sharpie, or art brush, and the
interpreter is only there to read the instructions and fulfill their job.

## {{ hl("invoke", "Invoking the tools") }}

### {{ hl("cmd", "The Command Line") }}

A **terminal** is a text-based interface for issuing commands to a
computer.[^1] As a trivial example, if you have a file called `gossip.txt`,
you can run `vim gossip.txt` to read the latest hot tea, in Vim.

[^1]:
    Some terminology confusion these days as "terminal", "terminal emulator",
    "shell", etc. are all interchangeable.
    See [unix.SE](https://unix.stackexchange.com/a/254366)

For simplicity, we're going to use **Bash** as the name of the commander,
though others exist.[^2] In general, Linux prompts may look different depending
on what terminal emulator or shell you use, but it should be easily accessible.
Windows may be more complicated.[^3]

[^2]:
    Allegiances: I use `xfce4-terminal` as the wrapper around my terminal, and
    I use `fish` for the shell instead of the more standard `bash`.

[^3]:
    That's because the shell is deliberately hidden
    from the user, leaving lots of confusion between things like Git Bash versus
    Powershell vs Windows Subsystem Linux versus MinGW or whatever.

You can think of **Bash as a commanding officer**.
It is able to run all other programs.
However, Bash has to travel from folder to folder.
At any point, Bash is stationed at a certain folder,
which is called its **current directory**.
Bash can travel to different directories using the `cd` command,
which you can [read about literally anywhere][redhat].
(Pro-tip: the faster you learn tab-completion, the better.)

Moreover, bash can then issue commands like `vim gossip.txt`.
But there are some catches.

1. First, Bash looks around for a file called `gossip.txt`
   in the folder that Bash happens to be in.
   If it sees `gossip.txt` in the current folder.
   If it's there, it picks up that piece of paper.
2. Then, Bash looks for a command called `vim`.
   There is a Vim editor on the system so Bash radios Vim to come
   over and read the `gossip.txt` document.
3. Vim does its thing.

The argument can be a filename in the current directory,
or a path to one.
So for example, `vim secretbox/gossip.tex` does the same thing
as `cd secretbox/` plus `vim gossip.tex`.

The orders and space arguments matters.
The first word is almost always a verb,
and everything that comes after it is an argument.
This could be the name of a file as in our example,
or it could be some other flag or parameter
This is one reason we avoid spaces in filenames,
because it mucks all these commands up, requiring quotes.

## {{ hl("exec", "Execution") }}

### {{ hl("progfile", "Programs are secretly executable files") }}

(Skip this entire section if you are learning this for the first time.)

Small surprise: editors like Vim or compilers like LaTeX
are all _technically_ actually files too,
even though we don't typically think of them that way.
For one thing, they are meant to be executed rather than edited.
Hence, they usually don't happen to have plain text encoding,
because they're meant to be read by machines, not you
(and in particular they are not meant to be editable).
In other words, they're written in "machine code", run by your system.

Vim isn't the only program.
Even most basic commands used in regular terminal sessions,
like `cd` (change directory), `pwd` (print working directory),
`rm` (deletes a file), etc. are actually all executable files.
As is `firefox`, which launches a Firefox process.

How can you tell these apart?
This is a bit out of scope, but on Linux,
every file has a set of [permission bits](https://en.wikipedia.org/wiki/File-system_permissions#Permissions),
and all you need to know the third bit indicates the file is _executable_.

So if someone types `vim gossip.txt`, that means `vim` is the "verb",
(the executable file being run), so Bash will give `vim` all the arguments
(in this case `gossip.txt`) and let Vim do its thing.

In which case you might ask: how does Bash know where to find `vim`,
if it's also a file but not in the current directory?
The way it works is that computers have a variable called `$PATH`
that specifies a list of directories.
Bash will look around every folder listed in `$PATH`
for an executable file which matches the same name; it takes the first one.
On Linux, the `$PATH` variable is managed well,
and unless you have something extra you need you can leave it alone.
If you're on Windows, HAHAHAHA GOOD LUCK.

To summarize: some files are executables,
and every incantation should start with the name of an executable.
The executables could live in a faraway system directory,
but Bash is smart enough to look for them in `$PATH`.

### {{ hl("manyprog", "Hence there are lots of programs") }}

Earlier, I talked about compilers and interpreters
as programs that read a piece of paper and do some action.
But programs are really versatile.

Once executed, programs can actually do more than one thing.
For example, they can read or write from _multiple_ files, not just one.
Or they can find the files themselves.
Or they may not need files as input: `firefox` is a program that,
when executed, launches a web browser.

There are also a lot of _suite-like_ programs for a specific kind of file.
You can think of this as a Swiss army knife.
If you are writing LaTeX,
you might have a program like TeXWorks which is both a text editor
(lets you edit `main.tex`) but also has a button that
invokes the LaTeX compiler (like a play button).

Using such suites is fine especially as a beginner.
Just be aware that the suite is hiding from you that two unrelated process,
the editing and the compiling, are happening.
This will help you when/if you need to debug an issue.

## {{ hl("next", "Where next?") }}

If you're ready to start playing with code,
[check out the tech support page](techsupport.html).

Thanks to the following individuals for suggestions and corrections:

- Ankan Bhattacharya
- David Altizio
- Luke Robitaille

I also acknowledge that some oversimplifications were made here.

[redhat]: https://www.redhat.com/sysadmin/navigating-filesystem-linux-terminal
