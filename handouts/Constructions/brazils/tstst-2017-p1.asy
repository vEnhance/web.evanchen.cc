size(6cm);
pair A = dir(110);
pair B = dir(210);
pair C = dir(330);
pair M = midpoint(A--B);
pair N = midpoint(A--C);
pair O = origin;
pair H = A+B+C;

draw(A--B--C--cycle, blue);
pair E = foot(B, A, C);
pair F = foot(C, A, B);
draw(B--E, lightblue);
draw(C--F, lightblue);
pair R = extension(E, F, B, C);
pair Q = -A+2*foot(O, A, R);

filldraw(unitcircle, opacity(0.1)+lightcyan, blue);
draw(A--R--E, heavygreen);
pair P = extension(M, N, A, A+dir(90)*A);
draw(A--P--N, red);
filldraw(circumcircle(A, M, N), opacity(0.1)+lightred, red);
filldraw(circumcircle(A, E, F), opacity(0.1)+lightgreen, heavygreen);

filldraw(circumcircle(M, N, E), opacity(0.1)+lightcyan, heavycyan);

dot("$A$", A, dir(A));
dot("$B$", B, dir(B));
dot("$C$", C, dir(C));
dot("$M$", M, dir(145));
dot("$N$", N, dir(20));
dot("$O$", O, dir(315));
dot("$H$", H, dir(H));
dot("$E$", E, dir(40));
dot("$F$", F, dir(F));
dot("$R$", R, dir(R));
dot("$Q$", Q, dir(Q));
dot("$P$", P, dir(P));

clip(box((-1.1,-1.1),(1.1,1.1)));
