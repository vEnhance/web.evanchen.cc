import geometry;

// geometry draws circles with hundreds of nodes; 4 suffices and halves the SVG
nowarn("circlenodesnumberfactor");
circlenodesnumberfactor = 1;

pair foot(pair P, pair A, pair B) { return foot(triangle(A, B, P).VC); }
path CP(pair P, pair A) { return circle(P, abs(A-P)); }

size(255);  // 255pt = 340px
defaultpen(fontsize(9pt)+linewidth(0.65));
dotfactor = 4;  // keep dots small despite thicker default pen
pair A = dir(150);
pair B = dir(220);
pair C = dir(320);
pair I = incenter(A, B, C);
pair E = foot(I, C, A);
pair F = foot(I, A, B);
pair T = extension(E, F, B, C);
pair O = circumcenter(A, E, F);
pair S = extension(F, F+(O-F)*dir(-90), E, E+(O-E)*dir(90));
pair M = midpoint(B--C);
pair MB = midpoint(B--I);
pair MC = midpoint(C--I);

filldraw(A--B--C--cycle, opacity(0.1)+lightred, red+1.2);
draw(incircle(A, B, C), dotted+red);
filldraw(circumcircle(A, F, E), opacity(0.03)+green, dashed+mediumgreen);
draw(E--S--F, dashed+mediumgreen);
draw(B--I--C, orange);
draw(E--T--B);
filldraw(circumcircle(M, MB, MC), opacity(0.1)+lightblue, blue);
filldraw(CP(midpoint(S--T), S), opacity(0.1)+lightblue, blue);
draw(S--T, dashed+blue);

dot(M);
dot(MB);
dot(MC);
dot("$A$", A, dir(A));
dot("$B$", B, dir(-90));
dot("$C$", C, dir(-90));
dot("$I$", I, dir(150));
dot("$E$", E, dir(60));
dot("$F$", F, dir(F));
dot("$T$", T, dir(T));
dot("$S$", S, dir(S));
