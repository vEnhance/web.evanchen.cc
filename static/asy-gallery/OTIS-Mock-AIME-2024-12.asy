import roundedpath;
usepackage("amsmath");
unitsize(1.5cm);
pair[][] points;
path t = ((0,0) -- (1,0) -- (1/2, sqrt(3)/2) -- cycle);
for (int i = 0; i < 5; ++i) {
  points.push(new pair[]);
  for (int j = 0; j < 5 - i; ++j) {
    points[i].push((j + i/2, i * sqrt(3)/2));
  }
  for (int j = 0; j < 4 - i; ++j) {
    draw(shift((j + i/2, i * sqrt(3)/2)) * t, linewidth(12) + grey);
  }
}

void band(int[][] p, pen c) {
  int n = p.length;
  for (int i = 0; i < n; ++i) {
    pair A = points[p[i][0]][p[i][1]], B = points[p[(i + 1) % n][0]][p[(i + 1) % n][1]], C =  points[p[(i + 2) % n][0]][p[(i + 2) % n][1]];
    draw(roundedpath((A + B) / 2 -- B -- (B + C) / 2, 0.15), white + linewidth(8));
    draw(roundedpath((A * 2 + B) / 3 -- B -- (B + C * 2) / 3, 0.15), c + linewidth(4));
  }
}

band(new int[][]{{0, 0}, {0, 1}, {1, 1}, {1, 2}, {2, 1}, {2, 0}, {1, 0},
  {0, 1}, {0, 2}, {1, 1}, {1, 0}}, deepgreen);
band(new int[][]{{1, 1}, {2, 0}, {3, 0}, {2, 1}, {2, 2}, {1, 2}, {0, 2}, {0, 3},
  {0, 4}, {1, 3}, {2, 2}, {3, 1}, {2, 1}}, lightblue);
band(new int[][]{{3, 0}, {4, 0}, {3, 1}}, orange);
band(new int[][]{{0, 3}, {1, 2}, {1, 3}}, lightred);

real r1 = 0.4;
real r2 = 1.3;
pair O1 = points[2][1];
pair O2 = O1 + (5.2,0);

fill(circle(O2, r2), lightgrey);
draw((O2+r2*dir(240))--(O2+r2*dir(60)), white + linewidth(9));
draw((O2+r2*dir(240))--(O2+r2*dir(60)), lightblue + linewidth(5), Margins);
draw((O2+r2*dir(120))..(O2+0.1*r2*dir(60))..(O2+r2*dir(0)), white + linewidth(9));
draw((O2+r2*dir(120))..(O2+0.1*r2*dir(60))..(O2+r2*dir(0)), lightblue + linewidth(5), Margins);
draw((O2+r2*dir(180))..(O2+0.1*r2*dir(240))..(O2+r2*dir(300)), white + linewidth(9));
draw((O2+r2*dir(180))..(O2+0.1*r2*dir(240))..(O2+r2*dir(300)), deepgreen + linewidth(5), Margins);

draw(circle(O1, r1), red+4);
draw(circle(O2, r2), red+4);
draw((O1+r1*dir(90))--(O2+r2*dir(90)), red+2);
draw((O1-r1*dir(90))--(O2-r2*dir(90)), red+2);

label("Example placement of $\mathcal G_4$", (2,0), 4*dir(-90));
label(minipage("Pairing at the circled peg, \\ one of $\frac{1}{3!} \binom 62 \binom 42 = 15$ possible.",
  width=5.2cm),
  O2+r2*dir(-90), 4*dir(-90));
