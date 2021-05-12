var pics = document.querySelectorAll('[id$="screen_pic]"]');
for(var i=0;i<pics.length;i++){
    pics[i].innerHTML="<img src= http://23.254.225.15:8000/"+pics[i].innerText+"></img>"

};
var numofselect = document.getElementsByClassName("select").length;
for(var i=0;i<numofselect;i++){
    document.getElementsByClassName("select")[0].setAttribute("class","");console.log(i);
};
document.getElementsByName("where[0][op]")[0].innerHTML = document.getElementsByName("where[0][op]")[0].innerHTML+"<option>=</option>"
