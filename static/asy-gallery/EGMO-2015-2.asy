size(10cm);
pen[] colors = {olive, deepmagenta, heavycyan, heavygreen};

fill((0,0)--(2,0)--(2,4)--(4,4)--(4,8)--(0,8)--cycle, cyan+opacity(0.2));
fill((2,0)--(6,0)--(6,2)--(4,2)--(4,4)--(2,4)--cycle, green+opacity(0.2));
fill(box((4,4),(6,8)), purple+opacity(0.2));
fill((4,2)--(6,2)--(6,0)--(8,0)--(8,8)--(6,8)--(6,4)--(4,4)--cycle, yellow+opacity(0.2));

for (int i=1; i<=4; ++i) {
draw((0,2*i-1)--(8,2*i-1), lightgrey+1);
draw((2*i-1,0)--(2*i-1,8), lightgrey+1);
}
for (int i=0; i<=4; ++i) {
draw((0,2*i)--(8,2*i), grey+1.5+linetype("3 2"));
draw((2*i,0)--(2*i,8), grey+1.5+linetype("3 2"));
}

path red_path = (0,0)--(2,0)--(2,4)--(6,4)--(6,8)--(8,8);
path blue_path = (0,8)--(4,8)--(4,2)--(6,2)--(6,0)--(8,0);
draw(red_path, lightred+7);
draw(red_path, heavyred+3);
draw(blue_path, lightcyan+7);
draw(blue_path, blue+3);

real eps = 0.22;
path dom = (eps,1-eps)--(1-eps,1-eps)--(1-eps,eps-1)--(eps,eps-1)--cycle;
void draw_domino(real x, real y, int n) {
filldraw(
shift(2*x-1,2*y-1)*rotate(90*n)*dom,
colors[n]+opacity(0.7),
black+1.3
);
}

draw_domino(4,4,0); draw_domino(4,3,0); draw_domino(4,2,0); draw_domino(4,1,0); draw_domino(3,2,0);
draw_domino(3,3,1); draw_domino(3,4,1);
draw_domino(1,1,2); draw_domino(1,2,2); draw_domino(1,3,2); draw_domino(1,4,2); draw_domino(2,3,2); draw_domino(2,4,2);
draw_domino(2,2,3); draw_domino(2,1,3); draw_domino(3,1,3);
