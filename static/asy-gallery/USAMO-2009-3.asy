unitsize(1.5cm);

margin m = Margin(3,3);
arrowbar ar = EndArrow(TeXHead);
pen gamma = blue + 1;
draw( (0,0)--(1,0), gamma, ar, m);
draw( (1,0)--(2,0), gamma, ar, m);
draw( (2,0)--(3,0), gamma, ar, m);
draw( (3,0)--(3,-1), gamma, ar, m);
draw( (3,-1)--(4,-1), gamma, ar, m);
draw( (4,-1)--(4,0), gamma, ar, m);
draw( (4,0)--(4,1), gamma, ar, m);
draw( (4,1)--(4,2), gamma, ar, m);
draw( (4,2)--(3,2), gamma, ar, m);
draw( (3,2)--(3,3), gamma, ar, m);
draw( (3,3)--(4,3), gamma, ar, m);
draw( (4,3)--(4,4), gamma, ar, m);
draw( (4,4)--(3,4), gamma, ar, m);
draw( (3,4)--(2,4), gamma, ar, m);
draw( (2,4)--(1,4), gamma, ar, m);
draw( (1,4)--(1,3), gamma, ar, m);
draw( (1,3)--(0,3), gamma, ar, m);
draw( (0,3)--(0,2), gamma, ar, m);
draw( (0,2)--(0,1), gamma, ar, m);
draw( (0,1)--(0,0), gamma, ar, m);

fill( (0,0)--(3,0)--(3,-1)--(4,-1)--(4,2)--(3,2)
--(3,3)--(4,3)--(4,4)--(1,4)--(1,3)--(0,3)--cycle,
opacity(0.1) + lightcyan);
label("$s$", (0,0), 1.5*dir(225));
label("$a$", (3,2), 2*dir(45), red);
label("$b$", (1,0), 2*dir(225), red);
draw( (3,2)--(1,0), lightred);

real r = 0.07;
filldraw(CR( (3,-1), r), grey, black);
filldraw(CR( (0,0), r), grey, black);
filldraw(CR( (2,0), r), grey, black);
filldraw(CR( (4,0), r), grey, black);
filldraw(CR( (1,1), r), grey, black);
filldraw(CR( (3,1), r), grey, black);
filldraw(CR( (0,2), r), grey, black);
filldraw(CR( (2,2), r), grey, black);
filldraw(CR( (4,2), r), grey, black);
filldraw(CR( (1,3), r), grey, black);
filldraw(CR( (3,3), r), grey, black);
filldraw(CR( (2,4), r), grey, black);
filldraw(CR( (4,4), r), grey, black);

filldraw(CR( (4,-1), r), white, black);
filldraw(CR( (1,0), r), white, black);
filldraw(CR( (3,0), r), white, black);
filldraw(CR( (0,1), r), white, black);
filldraw(CR( (2,1), r), white, black);
filldraw(CR( (4,1), r), white, black);
filldraw(CR( (1,2), r), white, black);
filldraw(CR( (3,2), r), white, black);
filldraw(CR( (0,3), r), white, black);
filldraw(CR( (2,3), r), white, black);
filldraw(CR( (4,3), r), white, black);
filldraw(CR( (1,4), r), white, black);
filldraw(CR( (3,4), r), white, black);

real s = 3*r;
fill(CR( (0,0), s), opacity(0.2)+lightred );
fill(CR( (1,0), s), opacity(0.2)+lightred );
fill(CR( (1,1), s), opacity(0.2)+lightred );
fill(CR( (2,1), s), opacity(0.2)+lightred );
fill(CR( (2,2), s), opacity(0.2)+lightred );
fill(CR( (3,2), s), opacity(0.2)+lightred );

pen domino = heavygreen+1.2;
path vd = box( (-0.4, -0.4), (0.4, 1.4) );
path hd = rotate(-90)*vd;
draw(shift(0,0)*vd, domino);
draw(shift(1,1)*vd, domino);
draw(shift(2,2)*vd, domino);
draw(shift(1,0)*hd, domino);
draw(shift(2,1)*hd, domino);
draw(shift(3,2)*hd, domino);
