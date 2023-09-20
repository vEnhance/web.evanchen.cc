defaultpen(fontsize(10pt));
usepackage("amsmath");
usepackage("amssymb");
settings.tex="latex";
settings.outformat="pdf";

import geometry;
pair foot(pair P, pair A, pair B) {
  return foot(triangle(A,B,P).VC);
}

size(12cm);

pair A = dir(120);
pair B = dir(210);
pair C = dir(330);
draw(A--B--C--cycle, red+1.3);
pair I = incenter(A, B, C);
pair D = foot(I, B, C);
pair E = foot(I, C, A);
pair F = foot(I, A, B);
pair P = foot(D, E, F);
pair Y = extension(B, P, A, C);
pair Z = extension(C, P, A, B);

draw(incircle(A, B, C), dashed+red);

filldraw(circumcircle(A, B, C), opacity(0.2)+lightcyan, blue);
filldraw(circumcircle(A, E, F), opacity(0.2)+paleblue, blue);
filldraw(circumcircle(A, Y, Z), opacity(0.2)+lightgreen, blue);

draw(B--Y, brown);
draw(C--Z, brown);
draw(D--E--F--cycle, red);
draw(D--P, red);
pair X = foot(A, P, I);

draw(I--X, orange);
pair K = foot(A, B, C);
draw(A--K, red);
pair Q = extension(P, I, A, K);

dot("$A$", A, dir(A));
dot("$B$", B, dir(B));
dot("$C$", C, dir(C));
dot("$I$", I, dir(-90));
dot("$D$", D, dir(D));
dot("$E$", E, dir(10));
dot("$F$", F, dir(190));
dot("$P$", P, dir(-90));
dot("$Y$", Y, dir(50));
dot("$Z$", Z, dir(200));
dot("$X$", X, dir(X));
dot("$Q$", Q, dir(45));
