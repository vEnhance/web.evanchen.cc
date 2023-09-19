picture turkey;
pen turkeyborder = black+1.2;
pair[] A = new pair[11];
for (int i=0; i<=10; ++i) {
A[i] = 5*dir(360*i/11);
}

picture leg;
pen turkeyleg = rgb("cc3300") + 1.2;
filldraw(turkey, scale(0.7)*unitcircle, rgb("cc0000"), turkeyborder);
draw(leg, (0.5*dir(-70))--(1.6*dir(-70)), turkeyleg);
draw(leg, (1.3*dir(-70))--(1.3*dir(-70)+0.3*dir(-95)), turkeyleg);
draw(leg, (1.3*dir(-70))--(1.3*dir(-70)+0.3*dir(-50)), turkeyleg);
add(turkey, leg);
add(turkey, reflect(dir(-90), dir(90))*leg);
filldraw(turkey, (1,0)--(-1,0)..(0,-1)..cycle, rgb("604020"), turkeyborder); // body of turkey
draw(turkey, (0.1,-0.4)..(-0.2,-0.35)..(-0.6,-0.2), turkeyborder); // part of wing
draw(turkey, (0.1,-0.8)..(-0.2,-0.7)..(-0.6,-0.2), turkeyborder); // part of wing
filldraw(turkey, (1.2,0.3)--(1.2,0)--(1.7,0.15)--cycle, yellow, turkeyborder); // beak of turkey
filldraw(turkey, circle((0.7,0.3), 0.6), rgb("e67300"), turkeyborder); // turkey head
fill(turkey, ellipse((1.05,0.45), 0.08, 0.12), black);
fill(turkey, ellipse((1.07,0.49), 0.02, 0.03), white);
draw(turkey, (1.6,0.5)--(1.8,0.7)..(2.0,0.75)..(2.4,1.2)..(1.8,1.5)..(1.2,1.2)..(1.6,0.7)--cycle );
label(turkey, scale(0.7)*"\textsf{gobble}", (1.8,1.1), fontsize(9pt));
add(shift(1.4*A[0])*rotate(-90)*turkey);
add(shift(1.4*A[4])*rotate(40)*turkey);

size(9cm);
draw(scale(5)*unitcircle, grey);
dotfactor *= 2;
draw(A[0]--A[4], blue);
draw(A[4]--A[8], lightblue+dashed);
draw(arc(origin, A[0], A[1]), deepgreen+1.8, EndArrow(TeXHead), Margin(0,4));
draw(arc(origin, A[4], A[5]), deepgreen+1.8, EndArrow(TeXHead), Margin(0,4));
draw(arc(origin, A[8], A[9]), deepgreen+1.8, EndArrow(TeXHead), Margin(0,4));
draw(A[10]--A[1], red, EndArrow(TeXHead), Margins);
draw(A[3]--A[5], red, EndArrow(TeXHead), Margins);
label(rotate(90)*"bigger than", A[10]--A[1], dir(180), red);

for (int i=0; i<=10; ++i) {
dot(A[i]);
}
