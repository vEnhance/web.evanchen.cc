var howOften = 12; //number often in seconds to rotate
var current = 2; //start the counter at 0
var ns6 = document.getElementById&&!document.all; //detect netscape 6

// place your images, text, etc in the array elements here
var items = new Array();

items[0] = "http://farm7.staticflickr.com/6013/5987406587_99eb3f706e_z.jpg";
items[1] = "http://farm8.staticflickr.com/7116/7774553536_20086fa3c8.jpg";
items[2] = "http://www.math.ttu.edu/%7Ergelca/PL/mop_black_12.JPG"
items[3] = "http://www.math.ttu.edu/%7Ergelca/PL/mop_blue_12.JPG"
items[4] = "http://www.math.ttu.edu/%7Ergelca/PL/mop_green_12.JPG"
items[5] = "http://www.math.ttu.edu/~rgelca/PL/mop_red_12.JPG";
items[6] = "http://www.math.ttu.edu/~rgelca/PL/mop_grading_12_2.JPG";
items[7] = "http://www.math.ttu.edu/~rgelca/PL/rmm_2011.JPG";
items[8] = "http://www.math.ttu.edu/%7Ergelca/PL/mop_black_13.JPG";
items[9] = "http://www.math.ttu.edu/%7Ergelca/PL/mop_blue_13.JPG"
items[10]= "http://www.math.ttu.edu/%7Ergelca/PL/mop_red_131.JPG"
items[11]= "http://www.math.ttu.edu/%7Ergelca/PL/mop_red_133.JPG"

/*
function rotater() {
    document.getElementById("placeholder").innerHTML = "<img alt='Generic image' src='slider/" + items[current] + " height='300' width='500' border='0'>";
    current = (current==items.length-1) ? 0 : current + 1;
    setTimeout("rotater()",howOften*1000);
}
*/

function rotater() {
    if(document.layers) {
        document.placeholderlayer.document.write(items[current]);
        document.placeholderlayer.document.close();
    }
    if(ns6)document.getElementById("placeholderdiv").innerHTML="<img alt='Generic image' src='" + items[current] + "' height='400' border='0'>"; //;items[current]
        if(document.all)
            placeholderdiv.innerHTML=items[current];

    current = Math.floor(Math.random()*items.length);
    setTimeout("rotater()",howOften*1000);
}
window.onload=rotater;
