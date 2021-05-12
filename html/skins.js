var pics = document.querySelectorAll('[id$="screen_pic]"]');
for(var i=0;i<pics.length;i++){
    pics[i].innerHTML="<img src="+pics[i].innerText+"></img>"

};
document.getElementsByName("where[0][op]")[0].innerHTML = document.getElementsByName("where[0][op]")[0].innerHTML+"<option>=</option>"
