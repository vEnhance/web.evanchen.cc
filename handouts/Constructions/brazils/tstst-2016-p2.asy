size(6cm);
pair A = dir(110);
pair B = dir(210);
pair C = dir(330);
pair N = midpoint(B--C);
pair H = orthocenter(A, B, C);
pair M = midpoint(A--H);
pair O = circumcenter(A, B, C);
pair P = extension(O, M, A, B-C+A);
pair X = extension(P, N, A, H);
pair T = foot(M, P, N);
pair D = foot(A, B, C);
pair E = foot(B, C, A);
pair F = foot(C, A, B);
pair L = -A;
pair K = extension(H, N, A, P);

filldraw(A--B--C--cycle, opacity(0.1)+lightblue, blue);
// filldraw(B--L--C--cycle, opacity(0.1)+lightblue, blue);
draw(unitcircle, blue);
// draw(A--L, blue);

draw(A--D, heavygreen);
draw(B--E, heavygreen);
draw(C--F, heavygreen);
draw(E--F, heavygreen);
// draw(B--M--C, lightred);
// filldraw(circumcircle(M, B, C), opacity(0.05)+lightred, red);

filldraw(circumcircle(D, E, F), opacity(0.05)+lightred, red);
draw(O--P--N, heavycyan);

filldraw(circumcircle(A, E, F), opacity(0.1)+lightgreen, heavygreen);
pair Q = foot(H, A, N);
pair G = -A+2*foot(A, M, P);
draw(A--P--G, heavycyan);

pair R = extension(E, F, B, C);
/*
draw(R--F, heavygreen);
draw(R--B, blue);
draw(R--Q, heavygreen);
draw(A--R, heavygreen);
draw(A--N, blue);
draw(P--G, heavycyan);
draw(M--R, heavygreen);
filldraw(circumcircle(R, G, T), opacity(0.05)+lightred, red);
*/

dot("$A$", A, dir(A));
dot("$B$", B, dir(B));
dot("$C$", C, dir(C));
dot("$N$", N, dir(N));
dot("$H$", H, dir(H));
dot("$M$", M, dir(M));
dot("$O$", O, dir(225));
dot("$P$", P, dir(P));
// dot("$X$", X, dir(X));
// dot("$T$", T, dir(T));
dot("$D$", D, dir(D));
dot("$E$", E, dir(E));
dot("$F$", F, dir(F));
// dot("$L$", L, dir(L));
// dot("$K$", K, dir(K));
// dot("$Q$", Q, dir(Q));
dot("$G$", G, dir(G));
// dot("$R$", R, dir(R));
