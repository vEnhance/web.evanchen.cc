size(11cm);
picture duck;
pen duckborder = black+1.2;

picture leg;
draw(leg, (0.5*dir(-70))--(1.6*dir(-70)), duckborder);
draw(leg, (1.3*dir(-70))--(1.3*dir(-70)+0.3*dir(-95)), duckborder);
draw(leg, (1.3*dir(-70))--(1.3*dir(-70)+0.3*dir(-50)), duckborder);
add(duck, leg);
add(duck, reflect(dir(-90), dir(90))*leg);
filldraw(duck, (1,0)--(-1,0)..(0,-1)..cycle, rgb("a67b5b"), duckborder); // body of duck
draw(duck, (0.1,-0.4)..(-0.2,-0.35)..(-0.6,-0.2), duckborder); // part of wing
draw(duck, (0.1,-0.8)..(-0.2,-0.7)..(-0.6,-0.2), duckborder); // part of wing
filldraw(duck, (1.2,0.3)--(1.2,0)--(1.7,0.15)--cycle, yellow, duckborder); // beak of duck
filldraw(duck, circle((0.7,0.3), 0.6), rgb("b9d3a4"), duckborder); // duck head
fill(duck, ellipse((1.05,0.45), 0.08, 0.12), black);
fill(duck, ellipse((1.07,0.49), 0.02, 0.03), white);
draw(duck, (1.6,0.5)--(1.8,0.7)..(2.0,0.75)..(2.4,1.2)..(1.8,1.5)..(1.2,1.2)..(1.6,0.7)--cycle );
label(duck, "\textsf{quack}", (1.8,1.1), fontsize(9pt));

draw(scale(4)*unitcircle, blue+2);
pen labelpen = red + fontsize(16pt);

add(rotate(-10)*shift(5*dir(90))*duck);
add(rotate(10)*shift(5*dir(90))*duck);
label("Rocks", 3*dir(90), labelpen);

add(rotate(100)*shift(5*dir(90))*duck);
add(rotate(120)*shift(5*dir(90))*duck);
add(rotate(140)*shift(5*dir(90))*duck);
label("Papers", 3*dir(210), labelpen);

add(rotate(200)*shift(5*dir(90))*duck);
add(rotate(220)*shift(5*dir(90))*duck);
add(rotate(240)*shift(5*dir(90))*duck);
add(rotate(260)*shift(5*dir(90))*duck);
label("Scissors", 3*dir(330), labelpen);
