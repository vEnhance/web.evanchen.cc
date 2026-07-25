 /* Geogebra to Asymptote conversion, documentation at artofproblemsolving.com/Wiki, go to User:Azjps/geogebra */
import graph; size(12.47cm);
real labelscalefactor = 0.5; /* changes label-to-point distance */
pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); /* default pen style */
pen dotstyle = black; /* point style */
real xmin = -5.14, xmax = 7.34, ymin = -5.89, ymax = 5.45;  /* image dimensions */
pen zzttqq = rgb(0.6,0.2,0); pen qqwuqq = rgb(0,0.39,0);

draw((-1,4)--(-3,-2)--(5,-2)--cycle, zzttqq);
draw((-2.76,1.76)--(-2.52,2)--(-2.76,2.24)--(-3,2)--cycle, qqwuqq);
 /* draw figures */
draw((-1,4)--(-3,-2), zzttqq);
draw((-3,-2)--(5,-2), zzttqq);
draw((5,-2)--(-1,4), zzttqq);
draw(circle((1,0), 4.47));
draw((-2.45,-0.34)--(2.24,0.76));
draw(circle((-0.38,1.38), 2.69));
draw((-1,4)--(-3,2));
draw((xmin, -1*xmin-1)--(xmax, -1*xmax-1)); /* line */
 /* dots and labels */
dot((-1,4),dotstyle);
label("$A$", (-0.94,4.1), NE * labelscalefactor);
dot((-3,-2),dotstyle);
label("$B$", (-2.93,-1.9), NE * labelscalefactor);
dot((5,-2),dotstyle);
label("$C$", (5.07,-1.9), NE * labelscalefactor);
dot((-1,0),dotstyle);
label("$H$", (-0.94,0.09), NE * labelscalefactor);
dot((-2.45,-0.34),dotstyle);
label("$D$", (-2.38,-0.24), NE * labelscalefactor);
dot((2.24,0.76),dotstyle);
label("$E$", (2.3,0.87), NE * labelscalefactor);
dot((1,-2),dotstyle);
label("$M$", (1.06,-1.9), NE * labelscalefactor);
dot((-3,2),dotstyle);
label("$F$", (-3.24,1.93), NE * labelscalefactor);
label("$90^\circ$", (-2.77,1.93), NE * labelscalefactor,qqwuqq);
clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle);
 /* end of picture */
