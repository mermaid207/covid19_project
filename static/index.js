var bars=document.querySelectorAll(".bar");
var total=Number(bars[0].getAttribute('value'));

var width=0;
for(var i of bars){
    width = Math.round(Number(i.getAttribute('value')/total)*100)+'%';
    i.style.width=width;
}

bars[0].style.background = "red";
bars[1].style.background = "pink";
bars[2].style.background = "yellow";
bars[3].style.background = "orange";