/* File unicodetex not found. */

 /* Geogebra to Asymptote conversion, documentation at artofproblemsolving.com/Wiki, go to User:Azjps/geogebra */
import graph; size(11.02cm);
real labelscalefactor = 0.5; /* changes label-to-point distance */
pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); /* default pen style */
pen dotstyle = black; /* point style */
real xmin = -5.26, xmax = 5.76, ymin = 0.92, ymax = 9.82;  /* image dimensions */
pen zzttqq = rgb(0.6,0.2,0);

draw((-2,9)--(-4,2)--(5,2)--cycle, zzttqq);
 /* draw figures */
draw((-2,9)--(-4,2), zzttqq);
draw((-4,2)--(5,2), zzttqq);
draw((5,2)--(-2,9), zzttqq);
draw(circle((-0.81,4.41), 2.41));
draw((-2,9)--(1.81,2));
draw((-4,2)--(2.11,4.89));
 /* dots and labels */
dot((-2,9),dotstyle);
label("$A$", (-1.92,9.12), NE * labelscalefactor);
dot((-4,2),dotstyle);
label("$B$", (-3.92,2.12), NE * labelscalefactor);
dot((5,2),dotstyle);
label("$C$", (5.08,2.12), NE * labelscalefactor);
dot((-0.81,4.41),dotstyle);
label("$I$", (-0.72,4.52), NE * labelscalefactor);
dot((-0.81,2),dotstyle);
label("$D_1$", (-0.72,2.12), NE * labelscalefactor);
dot((0.89,6.11),dotstyle);
label("$E_1$", (0.98,6.22), NE * labelscalefactor);
dot((1.81,2),dotstyle);
label("$D_2$", (1.88,2.12), NE * labelscalefactor);
dot((2.11,4.89),dotstyle);
label("$E_2$", (2.18,5.02), NE * labelscalefactor);
dot((-0.81,6.81),dotstyle);
label("$Q$", (-0.72,6.94), NE * labelscalefactor);
dot((0.62,4.19),dotstyle);
label("$P$", (0.7,4.3), NE * labelscalefactor);
clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle);
 /* end of picture */
