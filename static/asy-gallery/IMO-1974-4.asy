size(13cm);
picture g;
for (int i=0; i<8; ++i) {
  for (int j=0; j<8; ++j) {
    if ((i+j)%2 == 0) {
      fill(g, shift(i,j)*unitsquare, rgb("cccccc"));
    }
  }
}

picture p1, p2, p3, p4;
add(p1, g);
add(p2, g);
add(p3, g);
add(p4, g);
label(p1, "$64 = 2 + 4 + 6 + 10 + 12 + 14 + 16$", (4,0), dir(-90));
label(p2, "$64 = 2 + 4 + 6 + 8 + 12 + 14 + 18$", (4,0), dir(-90));
label(p3, "$64 = 2 + 4 + 6 + 8 + 10 + 16 + 18$", (4,0), dir(-90));
label(p4, "$64 = 2 + 4 + 6 + 8 + 10 + 14 + 20$", (4,0), dir(-90));

pen r = heavyred+1.4+fontsize(16pt);
pen[] colors = {
  green, orange, yellow, blue, purple,
  lightred, cyan, darkcyan, olive, fuchsia
};
void draw_rect(picture p, int x1, int y1, int x2, int y2) {
  int a = abs((y2-y1)*(x2-x1));
  filldraw(p, box((x1,y1),(x2,y2)), opacity(0.2)+colors[a#2-1], r);
  label(p, "\textbf{" + (string) a + "}", ((x1+x2)/2, (y1+y2)/2), r);
}
draw_rect(p1, 0,6, 1,8);
draw_rect(p1, 1,6, 8,8);
draw_rect(p1, 0,4, 2,6);
draw_rect(p1, 2,4, 8,6);
draw_rect(p1, 0,2, 3,4);
draw_rect(p1, 3,2, 8,4);
draw_rect(p1, 0,0, 8,2);

draw_rect(p2, 0,6, 1,8);
draw_rect(p2, 1,6, 8,8);
draw_rect(p2, 0,4, 2,6);
draw_rect(p2, 2,4, 8,6);
draw_rect(p2, 0,1, 2,4);
draw_rect(p2, 2,1, 8,4);
draw_rect(p2, 0,0, 8,1);

draw_rect(p3, 0,6, 1,8);
draw_rect(p3, 1,6, 3,8);
draw_rect(p3, 3,6, 8,8);
draw_rect(p3, 0,4, 8,6);
draw_rect(p3, 0,1, 2,4);
draw_rect(p3, 2,1, 8,4);
draw_rect(p3, 0,0, 8,1);

draw_rect(p4, 0,6, 1,8);
draw_rect(p4, 1,6, 8,8);
draw_rect(p4, 2,1, 4,6);
draw_rect(p4, 0,4, 2,6);
draw_rect(p4, 0,1, 2,4);
draw_rect(p4, 4,1, 8,6);
draw_rect(p4, 0,0, 8,1);

pen border = black+1.5;
draw(p1, box((0,0), (8,8)), border);
draw(p2, box((0,0), (8,8)), border);
draw(p3, box((0,0), (8,8)), border);
draw(p4, box((0,0), (8,8)), border);

real w = 9.5;
add(shift(0,0)*p1);
add(shift(w,0)*p2);
add(shift(0,-w)*p3);
add(shift(w,-w)*p4);
