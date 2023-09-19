usepackage("amsmath");
usepackage("amssymb");
size(14cm);
picture body;
pen border = black+1.8;
path outline = (0,0)..(0.5,-0.1)..(0.9,0)..(0.9,0)..(1,0.7)
  ..(0.85,1.3)..(0.4,1.32)..(0.13,1.1)..(0.12,1.08)--(0.12,1.08)..(0.03,0.4)
  ..(0,0.1)--(-0.1,0.02)--(0,0)..cycle;
filldraw(body, (0.8,0.7)--(1.15,0.35)--(0.85,0.4)--cycle, rgb("#90a0b0"), border);
filldraw(body, outline, rgb("#90a0b0"), border);
filldraw(body, subpath(outline, 0.2, 6.6)
  --(0.25,0.9)..(0.25,0.7)--(0.44,0.52)--(0.27,0.45)
  ..(0.2,0.22)..(0.15,0.1)..cycle,
  rgb("#f4f4f4"), border);
filldraw(body, ellipse((0.32,-0.075), 0.12, 0.07), orange, border);
filldraw(body, ellipse((0.72,-0.07), 0.12, 0.07), orange, border);
draw(body, (0.51,1.07)..(0.59,1.09)..(0.66,1.07), black+2);
draw(body, (0.78,1.07)..(0.86,1.09)..(0.94,1.07), black+2);
filldraw(body, (0.7,0.98)--(0.89,0.92)--(0.68,0.89)--cycle, yellow, border);

picture crown;
filldraw(crown, (0,0)--(0.6,0)--(0.6,0.3)--(0.5,0.2)
  --(0.4,0.3)--(0.3,0.2)--(0.2,0.3)--(0.1,0.2)--(0,0.3)--cycle,
  yellow, border);

real r = 1.4;
add(shift(  0,0)*yscale(1.0)*body);
add(shift(1.4,0)*yscale(0.7)*xscale(0.8)*body);
add(shift(2.8,0)*yscale(1.3)*xscale(1.1)*body);
add(shift(4.6,0)*yscale(1.5)*xscale(1.2)*body);
add(shift(6.0,0)*yscale(0.85)*xscale(0.9)*body);
add(shift(7.2,0)*yscale(1.1)*body);

add(shift(0.25,1.25)*crown);
add(shift(3.2,1.6)*crown);
add(shift(5.1,1.9)*crown);

real y = -0.5;
label("$\boxed{3}$", (0.5,y), fontsize(19pt)+red);
label("$1$", (1.8,-0.5), fontsize(19pt)+blue);
label("$\boxed{5}$", (3.4,y), fontsize(19pt)+red);
label("$\boxed{6}$", (5.2,y), fontsize(19pt)+red);
label("$2$", (6.4,y), fontsize(19pt)+blue);
label("$4$", (7.7,y), fontsize(19pt)+blue);

pen boxborder = deepgreen+2;
draw((-0.3,-0.9)--(-0.3,2.3), boxborder);
draw((2.5,-0.9)--(2.5,2.3), boxborder);
draw((4.2,-0.9)--(4.2,2.3), boxborder);
draw((8.4,-0.9)--(8.4,2.3), boxborder);
label("$0$", (-0.3,-0.9), dir(-90), fontsize(17pt)+deepgreen);
label("$2$", (2.5,-0.9), dir(-90), fontsize(17pt)+deepgreen);
label("$3$", (4.2,-0.9), dir(-90), fontsize(17pt)+deepgreen);
label("$6$", (8.4,-0.9), dir(-90), fontsize(17pt)+deepgreen);
