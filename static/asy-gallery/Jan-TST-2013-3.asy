size(11cm);
pair O = (0,0);
defaultpen(fontsize(7pt));

pair T(real x, real y, real z) {
return x * dir(90) + y * dir(210) + z * dir(330);
}

real M = 10.5;
transform t = shift(11,0)*rotate(-60);

pair[] yrs = { // lower left corner of yellow rhombi
// help
T(0, 5, 0),
T(0, 5, 1),
T(0, 5, 2),
T(0, 5, 3),
T(0, 2, 4),
T(1, 4, 0),
T(1, 4, 1),
T(1, 3, 2),
T(2, 4, 0),
T(2, 2, 1),
T(2, 1, 2),
T(3, 3, 0),
T(3, 1, 1),
T(3, 1, 2),
T(4, 2, 0),
T(4, 1, 1),
// argh
T(1, 0, 3),
T(1, 0, 4),
T(2, 0, 3),
T(2, 0, 4),
T(3, 0, 3),
T(3, 0, 4),
T(4, 0, 2),
T(4, 0, 3),
T(4, 0, 4),
};
path yellow_rhombus = O--dir(90)--dir(30)--dir(-30)--cycle;

for (int i=0; i<yrs.length; ++i) {
filldraw(shift(yrs[i])*yellow_rhombus, paleyellow, black);
filldraw(t*shift(yrs[i])*yellow_rhombus, paleyellow, black);
label("$0$", t*shift(yrs[i])*(0.5*dir(30)));
}

pair[] grs = { // upper corner of green rhombi
// help
T(0, 2, 4),
T(0, 3, 4),
T(0, 4, 4),
T(1, 4, 0),
T(1, 4, 1),
T(1, 4, 2),
T(1, 3, 2),
T(1, 4, 3),
T(1, 3, 3),
T(1, 2, 3),
T(1, 1, 3),
T(1, 0, 3),
T(1, 1, 4),
T(1, 0, 4),
T(2, 3, 1),
T(2, 2, 1),
T(2, 2, 2),
T(2, 1, 2),
T(3, 3, 0),
T(3, 1, 1),
T(4, 2, 0),
T(4, 0, 2),
T(5, 1, 0),
T(5, 0, 1),
T(5, 0, 0),
};
path green_rhombus = O--dir(210)--dir(270)--dir(330)--cycle;

for (int i=0; i<grs.length; ++i) {
filldraw(shift(grs[i])*green_rhombus, palegreen, black);
filldraw(t*shift(grs[i])*green_rhombus, palegreen, black);
label("$1$", shift(grs[i])*(0.5*dir(-90)));
}


pair[] brs = { // upper left corner of blue rhombi
T(5, 3, 0),
T(5, 4, 0),
T(5, 5, 0),
T(4, 4, 0),
T(4, 5, 0),
T(3, 5, 0),
T(2, 5, 0),
T(4, 1, 0),
T(3, 1, 0),
T(3, 2, 0),
T(2, 2, 0),
T(2, 3, 0),
T(0, 2, 0),
T(1, 0, 0),
T(4, 0, 1),
T(3, 0, 2),
T(2, 0, 2),
T(1, 0, 2),
T(0, 0, 1),
T(0, 1, 1),
T(0, 4, 3),
T(0, 3, 3),
T(0, 2, 3),
T(0, 1, 4),
T(0, 0, 4),
};
path blue_rhombus = O--dir(270)--dir(330)--dir(30)--cycle;
for (int i=0; i<brs.length; ++i) {
filldraw(shift(brs[i])*blue_rhombus, palecyan, black);
filldraw(t*shift(brs[i])*blue_rhombus, palecyan, black);
label("$0$", shift(brs[i])*(0.5*dir(-30)));
label("$1$", t*shift(brs[i])*(0.5*dir(-30)));
}

label("Row $1$", T(5, 0.2, 0), dir(160));
label("Row $2$", T(5, 1.2, 0), dir(160));
label("Row $3$", T(5, 2.2, 0), dir(160));
label("Row $4$", T(5, 3.2, 0), dir(160));
label("Row $5$", T(5, 4.2, 0), dir(160));

label("Row $1$", shift(M+0.5,0)*T(5, 0.2, 0), dir(160));
label("Row $2$", shift(M+0.5,0)*T(5, 1.2, 0), dir(160));
label("Row $3$", shift(M+0.5,0)*T(5, 2.2, 0), dir(160));
label("Row $4$", shift(M+0.5,0)*T(5, 3.2, 0), dir(160));
label("Row $5$", shift(M+0.5,0)*T(5, 4.2, 0), dir(160));

label(scale(2)*"$C$", T(0, 5, 5), dir(-90));
label(scale(2)*"$f(C)$", shift(M+0.5,0)*T(0, 5, 5), dir(-90));
path ar = shift(2,-0.5)*T(0,5,5)--shift(M-1.5,-0.5)*T(0,5,5);
draw(ar, EndArrow);
label("Rotate hexagon $60^{\circ}$", ar, dir(-90));
