import cse5; import olympiad;
size(8cm);
pathpen = black + linewidth(0.7); pointpen = black; pen s = fontsize(8);
pair B=(0,0),C=(5,0),A=(4,4); /* A.x > C.x/2 */
/* construction and drawing */
pair P=(A+B)/2,M=(B+C)/2,N=(A+C)/2,D=IP(A--M,P--P+5*(P-bisectorpoint(A,B))),E=IP(A--M,N--N+5*(bisectorpoint(A,C)-N)),F=IP(B--B+5*(D-B),C--C+5*(E-C)),O=circumcenter(A,B,C);
D(MP("A",A,(0,1),s)--MP("B",B,SW,s)--MP("C",C,SE,s)--A--MP("M",M,s));
D(C--D(MP("E",E,NW,s))--MP("N",N,(1,0),s));
D(D(MP("D",D,SE,s))--MP("P",P,W,s));
D(B--D(MP("F",F,s))); // D(O--A--F,linetype("4 4")+linewidth(0.7));
// D(MP("O'",circumcenter(A,P,N),NW,s));
D(circumcircle(A,P,N),linetype("4 4")+linewidth(0.7));
D(rightanglemark(A,P,D,3.5));D(rightanglemark(A,N,E,3.5));
D(circumcircle(A,B,C),linetype("1 4")+linewidth(0.7));
picture p = new picture;
// draw(p,circumcircle(B,O,C),linetype("1 4")+linewidth(0.7));
// clip(p,B+(-5,0)--B+(-5,A.y+2)--C+(5,A.y+2)--C+(5,0)--cycle); add(p);
