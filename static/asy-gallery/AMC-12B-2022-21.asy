size(12cm);

void dc(pair x, pen p) {
pair y = intersectionpoints(circle((0,0),8),(0,0)--1000*x)[0];
filldraw(circle(x, abs(x-y)), opacity(0.1)+p, p);
filldraw(circle(conj(x), abs(x-y)), opacity(0.1)+p, p);
}

pair O1 = (0,0);
pair O2 = (5,0);
pair P1 = intersectionpoints(circle(O1,5),circle(O2,3+sqrt(3)))[0];
pair P2 = intersectionpoints(circle(O1,3),circle(O2,5+sqrt(3)))[0];
pair P3 = intersectionpoints(circle(O1,5),circle(O2,3-sqrt(3)))[0];
pair P4 = intersectionpoints(circle(O1,3),circle(O2,5-sqrt(3)))[0];

filldraw(circle(O1,8), opacity(0.1)+grey, black+1.8);

dc(P1,blue);
dc(P2,red);
dc(P3,darkgreen);
dc(P4,brown);

filldraw(circle(O1,2), opacity(0.4)+yellow, black+1.8);
filldraw(circle(O2,sqrt(3)), opacity(0.4)+yellow, black+1.8);

dot("$(0,0)$", (0,0), dir(-90));
dot("$(5,0)$", (5,0), dir(-90));
