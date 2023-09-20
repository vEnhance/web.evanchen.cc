size(6cm);
pair A = dir(110);
pair B = dir(210);
pair C = dir(330);
pair H = orthocenter(A, B, C);
pair D = foot(B, A, C);
pair E = foot(C, A, B);
pair F = foot(H, A, extension(D, E, B, C));

draw(A--B--C--cycle, orange);
filldraw(circumcircle(A, B, C), opacity(0.1)+orange, orange);
filldraw(circumcircle(D, E, F), opacity(0.1)+red, yellow);
draw(B--D, orange);
draw(C--E, orange);
draw(B--F--C, orange);
pair L = extension(A, H, B, C);
draw(A--L, orange);

/*
pair X = extension(A, H, -A, (B-C)-A);
draw(X--L, red+dashed);

pair T = extension(D, E, B, C);
draw(T--C, red);

draw(T--A, brown+dotted);
draw(T--D, brown+dotted);
*/

dot("$A$", A, dir(A));
dot("$B$", B, dir(B));
dot("$C$", C, dir(C));
dot("$H$", H, dir(315));
dot("$D$", D, dir(D));
dot("$E$", E, dir(E));
dot("$F$", F, dir(F));
dot("$L$", L, dir(L));
// dot("$X$", X, dir(X));
// dot("$T$", T, dir(T));
