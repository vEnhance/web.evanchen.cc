import olympiad;
import cse5;
pointpen = black;
pathpen = black;
pathfontpen = black;
anglepen = black;
anglefontpen = black;
pointfontsize = 9;
defaultpen(fontsize(9pt));
size(6cm); // set a reasonable default
usepackage("amsmath");
usepackage("amssymb");

defaultpen(fontsize(11pt));
pointfontsize=11;
void bigbox(string L) {
draw((-4,3)--(4,3)--(4,-3)--(-4,-3)--cycle );
label(L, (4,3), dir(-45));
}

pair opendot(pair P, pen p = defaultpen) {
dot(P, UnFill);
dot(P, p, Draw);
return P;
}

size(6cm);

real[] t = {-1,0,1,2};
xaxis(-2,3, graph.LeftTicks(Ticks=t), Arrows);
MP("\mathbb R", (2.5,0), dir(90));
path gt = (0,0.3)--(1,0.3);
draw(gt, blue, EndArrow);
label("$\tilde\gamma$", midpoint(gt), dir(90), blue);
add(shift( (0,3) ) * CC());

path darrow = (0,2.5)--(0,1.5);
MP("p", midpoint(darrow), dir(0));
draw(darrow, EndArrow);

real r = 1.2;
draw(scale(r)*unitcircle);
MP("S^1", r*dir(45), dir(45));
dot("$1$", r*dir(0), dir(0));
path g = dir(20)..dir(100)..dir(180)..dir(260)..dir(340);
draw(g, red, EndArrow);
label("$\gamma$", midpoint(g), -dir(midpoint(g)), red);

MP("p(0) = 1", (2.5,0.5));
MP("p(1) = 1", (2.5,0));
