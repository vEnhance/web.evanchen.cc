/* File unicodetex not found. */

 /* Geogebra to Asymptote conversion, documentation at artofproblemsolving.com/Wiki, go to User:Azjps/geogebra */
import graph; size(12cm);
real labelscalefactor = 0.5; /* changes label-to-point distance */
pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); /* default pen style */
pen dotstyle = black; /* point style */
real xmin = -7.88, xmax = 12.42, ymin = -2.77, ymax = 12.95;  /* image dimensions */

 /* draw figures */
draw((-4,8)--(7,8));
draw((-4,8)--(0,5));
draw((0,5)--(7,8));
draw(circle((1.5,11.17), 6.35));
draw((xmin, -1.74*xmin + 1.05)--(xmax, -1.74*xmax + 1.05)); /* line */
draw((xmin, 1.74*xmin-4.16)--(xmax, 1.74*xmax-4.16)); /* line */
draw((-4,8)--(1.5,-1.55));
draw((7,8)--(1.5,-1.55));
draw((0,5)--(xmin, 0.43*xmin + 5)); /* ray */
draw((0,5)--(xmax, -0.75*xmax + 5)); /* ray */
draw(circle((1.5,2.82), 2.65));
draw((0,5)--(-1.14,3.03));
draw((0,5)--(2.64,0.43));
 /* dots and labels */
dot((0,5),dotstyle);
label("$A$", (0.1,5.14), NE * labelscalefactor);
dot((-4,8),dotstyle);
label("$P$", (-3.9,8.14), NE * labelscalefactor);
dot((7,8),dotstyle);
label("$Q$", (7.1,8.14), NE * labelscalefactor);
dot((1.5,11.17),dotstyle);
label("Center of APQ", (1.6,11.31), NE * labelscalefactor);
dot((1.5,-1.55),dotstyle);
label("$B$", (1.64,-1.61), NE * labelscalefactor);
dot((-1.14,3.03),dotstyle);
label("$X$", (-1.59,2.83), (0,0));
dot((2.64,0.43),dotstyle);
label("$Y$", (2.82,0.24), NE * labelscalefactor);
dot((3.18,2.62),dotstyle);
label("$R$", (3.26,2.76), NE * labelscalefactor);
dot((-3.65,3.44),dotstyle);
label("$S$", (-3.56,3.57), NE * labelscalefactor);
dot((-0.47,1.05),dotstyle);
label("$O$", (-0.95,0.68), (0,0));
clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle);
 /* end of picture */
