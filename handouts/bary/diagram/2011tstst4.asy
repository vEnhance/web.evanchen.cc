/* Geogebra to Asymptote conversion, documentation at artofproblemsolving.com/Wiki, go to User:Azjps/geogebra */
import graph; size(12cm);
real labelscalefactor = 0.5; /* changes label-to-point distance */
pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); /* default pen style */
pen dotstyle = black; /* point style */
real xmin = -7.67, xmax = 6.69, ymin = -7.5, ymax = 7.01;  /* image dimensions */
pen zzttqq = rgb(0.6,0.2,0);

draw((-1,4)--(-3,-2)--(5,-2)--cycle, zzttqq);
 /* draw figures */
draw((-1,4)--(-3,-2), zzttqq);
draw((-3,-2)--(5,-2), zzttqq);
draw((5,-2)--(-1,4), zzttqq);
draw(circle((1,0), 4.47));
draw((-2,1)--(3,-4));
draw((2,1)--(-3.4,-0.8));
draw((3,-4)--(-7,1));
draw((-7,1)--(2,1));
draw((-7,1)--(-1,4));
 /* dots and labels */
dot((-1,4),dotstyle);
label("$A$", (-0.87,4.17), NE * labelscalefactor);
dot((-3,-2),dotstyle);
label("$B$", (-2.87,-1.82), NE * labelscalefactor);
dot((5,-2),dotstyle);
label("$C$", (5.12,-1.82), NE * labelscalefactor);
dot((-1,0),dotstyle);
label("$H$", (-0.87,0.18), NE * labelscalefactor);
dot((1,0),dotstyle);
label("$O$", (1.13,0.18), NE * labelscalefactor);
dot((-2,1),dotstyle);
label("$M$", (-1.87,1.18), NE * labelscalefactor);
dot((2,1),dotstyle);
label("$N$", (2.12,1.18), NE * labelscalefactor);
dot((3,-4),dotstyle);
label("$P$", (3.12,-3.81), NE * labelscalefactor);
dot((-3.4,-0.8),dotstyle);
label("$Q$", (-3.29,-0.61), NE * labelscalefactor);
dot((-7,1),dotstyle);
label("$R$", (-6.89,1.18), NE * labelscalefactor);
clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle);
 /* end of picture */
