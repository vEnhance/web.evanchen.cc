size(6cm);
pair A = dir(110);
pair B = dir(210);
pair C = dir(330);
draw(A--B--C--cycle, heavygreen);

pair H = orthocenter(A, B, C);
pair M = midpoint(B--C);
pair I = incenter(A, B, C);
pair W = foot(H, A, I);
pair D = extension(W, H, A, B);
pair E = extension(W, H, A, C);
draw(D--E, blue);

pair Y = foot(B, A, C);
pair Z = foot(C, A, B);
// draw(B--Y, dotted);
// draw(C--Z, dotted);

filldraw(unitcircle, opacity(0.1)+lightcyan, heavygreen);
filldraw(circumcircle(A, D, E), opacity(0.1)+lightcyan, blue);
pair X = (D*C-E*B)/(D+C-E-B);
// filldraw(circumcircle(A, Y, Z), opacity(0.1)+yellow, dashed+red);

pair Ap = -A;
// draw(Ap--X--A, lightblue);
draw(X--M, dotted);

dot("$A$", A, dir(A));
dot("$B$", B, dir(B));
dot("$C$", C, dir(C));
dot("$H$", H, dir(85));
dot("$M$", M, dir(-120));
dot("$D$", D, dir(D));
dot("$E$", E, dir(E));
dot("$X$", X, dir(X));
