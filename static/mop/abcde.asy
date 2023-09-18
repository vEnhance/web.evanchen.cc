unitsize(1.5cm);
picture g;
usepackage("mathrsfs");
usepackage("amssymb");

defaultpen(fontsize(24pt));
real k = 0.1 - 0.0707;

path rounded_square =
	(0,0.1)..(k,k)..(0.1,0)--
	(0.9,0)..(1-k,k)..(1,0.1)--
	(1,0.9)..(1-k,1-k)..(0.9,1)--
	(0.1,1)..(k,1-k)..(0,0.9)--
	cycle;

filldraw(g, shift(-0.5,-0.5) * scale(5.05)* rounded_square,
	 opacity(0.3)+paleyellow, black+2);
pen r1 = heavyred;
pen r2 = mediumred;
pen gr = deepgreen;
pen bl = heavyblue;
pen bk = black;
pen sp = orange + fontsize(32pt);
real r = 1.5;

label(g, "$\mathbb{A}$", (0,4), r1);
label(g, "$\mathbb{B}$", (1,4), r2);
label(g, "$\mathbb{C}$", (2,4), gr);
label(g, "$\mathbb{D}$", (3,4), bl);
label(g, "$\mathbb{E}$", (4,4), bk);

label(g, "$\mathbb{F}$", (0,3), bk);
label(g, "$\mathbb{G}$", (1,3), r1);
label(g, "$\mathbb{H}$", (2,3), r2);
label(g, "$\mathbb{I}$", (3,3), gr);
label(g, "$\mathbb{J}$", (4,3), bl);

label(g, "$\mathbb{K}$", (0,2), bl);
label(g, "$\mathbb{L}$", (1,2), bk);
label(g, scale(r)*"$\mathcal{M}$", (2,2), sp);
label(g, "$\mathbb{N}$", (3,2), r2);
label(g, scale(r)*"$\mathcal{O}$", (4,2), sp);

label(g, scale(r)*"$\mathcal{P}$", (0,1), sp);
label(g, "$\mathbb{Q}$", (1,1), bl);
label(g, "$\mathbb{R}$", (2,1), bk);
label(g, "$\mathbb{T}$", (3,1), r1);
label(g, "$\mathbb{U}$", (4,1), r2);

label(g, "$\mathbb{V}$", (0,0), r2);
label(g, "$\mathbb{W}$", (1,0), gr);
label(g, "$\mathbb{X}$", (2,0), bl);
label(g, "$\mathbb{Y}$", (3,0), bk);
label(g, "$\mathbb{Z}$", (4,0), r1);
add(rotate(7)*g);
label("\itshape\sffamily Math Olympiad Program", (1.8,-1),
	rgb(0.2,0.2,0.2)+fontsize(32pt));
