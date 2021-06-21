var pics = document.querySelectorAll('[id$="screen_pic]"]');
for(var i=0;i<pics.length;i++){
    var host = document.domain;
    pics[i].innerHTML="<img src= http://"+host+":8000/"+pics[i].innerText+"></img>"

};
var numofselect = document.getElementsByClassName("select").length;
for(var i=0;i<numofselect;i++){
    document.getElementsByClassName("select")[0].setAttribute("class","");console.log(i);
};
document.getElementsByName("where[0][op]")[0].innerHTML = document.getElementsByName("where[0][op]")[0].innerHTML+"<option>=</option>"
