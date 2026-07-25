import graph; size(7cm);
real labelscalefactor = 0.5; /* changes label-to-point distance */
pen dps = linewidth(0.7) + fontsize(10); defaultpen(dps); /* default pen style */
pen dotstyle = black; /* point style */
real xmin = -9.97, xmax = 22.26, ymin = -8.77, ymax = 12.88;  /* image dimensions */
pen zzttqq = rgb(0.6,0.2,0); pen wwwwww = rgb(0.4,0.4,0.4);

draw((9.92,3)--(-0.91,3)--(-0.91,-7.84)--(9.92,-7.84)--cycle, zzttqq);
draw((1,3)--(6,3)--(6,8)--(1,8)--cycle, zzttqq);
draw((2.64,12.28)--(-0.91,3)--(9.92,3)--cycle, wwwwww);
 /* draw figures */
draw((9.92,3)--(-0.91,3), zzttqq);
draw((-0.91,3)--(-0.91,-7.84), zzttqq);
draw((-0.91,-7.84)--(9.92,-7.84), zzttqq);
draw((9.92,-7.84)--(9.92,3), zzttqq);
draw((1,3)--(6,3), zzttqq);
draw((6,3)--(6,8), zzttqq);
draw((6,8)--(1,8), zzttqq);
draw((1,8)--(1,3), zzttqq);
draw((2.64,12.28)--(-0.91,3), wwwwww);
draw((-0.91,3)--(9.92,3), wwwwww);
draw((9.92,3)--(2.64,12.28), wwwwww);
draw((2.64,12.28)--(4.51,-2.42));
 /* dots and labels */
dot((1,3),dotstyle);
label("$M$", (1.2,3.28), NE * labelscalefactor);
dot((6,3),dotstyle);
label("$N$", (6.16,3.28), NE * labelscalefactor);
dot((-0.91,3),dotstyle);
label("$B$", (-0.75,3.28), NE * labelscalefactor);
dot((9.92,3),dotstyle);
label("$C$", (10.11,3.28), NE * labelscalefactor);
dot((-0.91,-7.84),dotstyle);
label("$M'$", (-0.75,-7.57), NE * labelscalefactor);
dot((9.92,-7.84),dotstyle);
label("$N'$", (10.11,-7.57), NE * labelscalefactor);
dot((6,8),dotstyle);
label("$L$", (6.16,8.29), NE * labelscalefactor);
dot((1,8),dotstyle);
label("$K$", (1.2,8.29), NE * labelscalefactor);
dot((2.64,12.28),dotstyle);
label("$A$", (2.83,12.33), NE * labelscalefactor);
dot((3.5,5.5),dotstyle);
label("$A_1$", (3.71,5.79), NE * labelscalefactor);
dot((4.51,-2.42),dotstyle);
label("$A_2$", (4.68,-2.14), NE * labelscalefactor);
clip((xmin,ymin)--(xmin,ymax)--(xmax,ymax)--(xmax,ymin)--cycle);
 /* end of picture */
