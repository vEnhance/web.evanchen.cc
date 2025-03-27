size(12cm);
for (int i=1; i<9; ++i) {
  draw((i,0)--(i,9), grey);
  draw((0,i)--(9,i), grey);
}

pen border = black + 2;

filldraw((0,9)--(9,9)--(9,0)--(8,0)--(8,8)--(0,8)--cycle,
  opacity(0.1)+red, border);
for (int i=0; i<8; ++i) {
  label("$L_8$", (i+0.5,8.5), red);
  label("$L_8$", (8.5,i+0.5), red);
}
label("$L_8$", (8.5,8.5), red);

filldraw((0,0)--(0,1)--(7,1)--(7,8)--(8,8)--(8,0)--(0,0)--cycle,
  opacity(0.1)+orange, border);
for (int i=0; i<7; ++i) {
  label("$L_7$", (i+0.5,0.5), brown);
  label("$L_7$", (7.5,i+1.5), brown);
}
label("$L_7$", (7.5,0.5), brown);

filldraw((0,8)--(0,1)--(7,1)--(7,2)--(1,2)--(1,8)--cycle,
  opacity(0.1)+yellow, border);
for (int i=0; i<6; ++i) {
  label("$L_6$", (i+1.5,1.5), black);
  label("$L_6$", (0.5,i+2.5), black);
}
label("$L_6$", (0.5,1.5), black);

filldraw((6,8)--(7,8)--(7,2)--(1,2)--(1,3)--(6,3)--cycle,
  opacity(0.1)+green, border);
for (int i=0; i<5; ++i) {
  label("$L_5$", (i+1.5,2.5), deepgreen);
  label("$L_5$", (6.5,i+3.5), deepgreen);
}
label("$L_5$", (6.5,2.5), deepgreen);

filldraw((1,7)--(1,8)--(6,8)--(6,3)--(5,3)--(5,7)--cycle,
  opacity(0.1)+cyan, border);
for (int i=0; i<4; ++i) {
  label("$L_4$", (i+1.5,7.5), black);
  label("$L_4$", (5.5,i+3.5), black);
}
label("$L_4$", (5.5,7.5), black);

filldraw((1,6)--(1,7)--(5,7)--(5,3)--(4,3)--(4,6)--cycle,
  opacity(0.1)+lightblue, border);
for (int i=0; i<3; ++i) {
  label("$L_3$", (i+1.5,6.5), blue);
  label("$L_3$", (4.5,i+3.5), blue);
}
label("$L_3$", (4.5,6.5), blue);

filldraw((1,6)--(1,3)--(4,3)--(4,4)--(2,4)--(2,6)--cycle,
  opacity(0.1)+purple, border);
for (int i=0; i<2; ++i) {
  label("$L_2$", (i+2.5,3.5), purple);
  label("$L_2$", (1.5,i+4.5), purple);
}
label("$L_2$", (1.5,3.5), purple);


filldraw((2,4)--(4,4)--(4,6)--(3,6)--(3,5)--(2,5)--cycle,
  opacity(0.1)+grey, border);
label("$L_1$", (3.5,5.5), black);
label("$L_1$", (2.5,4.5), black);
label("$L_1$", (3.5,4.5), black);


label("$
    \renewcommand{\arraystretch}{0.6}
    \begin{array}{cccccccc}
      L_8 & L_7 & L_6 & L_5 & L_4 & L_3 & L_2 & L_1 \\\\
      \mathsf{N} & \mathsf{S} & \mathsf{S} & \mathsf{S} &
      \mathsf{N} & \mathsf{N} & \mathsf{S} & \mathsf{S} \\\\
      \mathsf{E} & \mathsf{E} & \mathsf{W} & \mathsf{E} &
      \mathsf{E} & \mathsf{E} & \mathsf{W} & \mathsf{E} \\\\
    \end{array}
  $", (4.5,-0.5), dir(-90));
