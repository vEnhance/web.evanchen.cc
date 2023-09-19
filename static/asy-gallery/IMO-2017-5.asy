size(10cm);
int[] ys = {7,11,2,5,0,10,9,0,12,1,6,8,4,3};
real r = 0.2;

fill(box((-1, 8.5),(4,4.5)), opacity(0.3)+lightred);
fill(box((-1,12.5),(7,8.5)), opacity(0.3)+lightcyan);
fill(box((-1, 4.5),(14,0.5)), opacity(0.3)+lightgreen);
fill(box((4, 8.5),(14,4.5)), opacity(0.3)+grey);
fill(box((7,12.5),(14,8.5)), opacity(0.3)+grey);

draw( (-1,4.5)--(14,4.5) );
draw( (-1,8.5)--(14,8.5) );

pair P(int x) {
return (x,ys[x]);
}

pair O;
int y;
pen c;
for (int x=0; x<=13; ++x) {
y = ys[x];
if (y==0) continue;
O = (x, y);
if ((y==7) || (y==5)) c = red;
else if ((y==10) || (y==9)) c = blue;
else if ((y==1) || (y==4)) c = heavygreen;
else c = grey;
filldraw(circle(O, r), c, black+1);
label("$"+(string)y+"$", O+(r,0), 0.5*dir(0), c);
}

pen border = black+2;
pen dash = dotted+1;
draw( (4,12.5)--(4,0.5), dash );
draw( (7,12.5)--(7,0.5), dash );

path bracket(real x0, real x1) {
return (x0,0.7)--(x0,0.5)--(x1,0.5)--(x1,0.7);
}
draw(bracket(-0.8,3.8), border);
draw(bracket(4.2,6.8), border);
draw(bracket(7.2,13.8), border);
