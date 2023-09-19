unitsize(0.75cm);

for (int i=0; i<=8; ++i) {
if ((i!=0) && (i!=4) && (i!=8)) {
draw( (0,i)--(8,i), grey );
draw( (i,0)--(i,8), grey );
}
else {
draw( (0,i)--(8,i), black+1 );
draw( (i,0)--(i,8), black+1 );
}
}


filldraw( box((2.1,4.1),(5.9,7.9)), opacity(0.2)+palered, red+1 );
filldraw( box((1.1,2.1),(4.9,5.9)), opacity(0.2)+lightgreen, blue+1 );
fill(box((0,4),(4,8)), opacity(0.1)+lightcyan);
label("$A$", (3.5,8), dir(90), red);
label("$B$", (2.5,2), dir(-90), blue);

label("$2$", (0.5,7.5));
label("$1$", (1.5,7.5));
label("$2$", (2.5,7.5));
label("$1$", (3.5,7.5));
label("$1$", (0.5,6.5));
label("$5$", (1.5,6.5), red);
label("$1$", (2.5,6.5));
label("$3$", (3.5,6.5));
label("$2$", (0.5,5.5));
label("$1$", (1.5,5.5));
label("$2$", (2.5,5.5));
label("$1$", (3.5,5.5));
label("$1$", (0.5,4.5));
label("$3$", (1.5,4.5));
label("$1$", (2.5,4.5));
label("$4$", (3.5,4.5));
label("$6$", (5.5,6.5), blue);
