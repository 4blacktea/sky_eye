var pics = document.querySelectorAll('[id$="screen_pic]"]');
for(var i=0;i<pics.length;i++){
	    var host = document.domain;
	    if(pics[i].innerText!="screen_pic"){
		            pics[i].innerHTML="<img src= http://"+host+":8000/"+pics[i].innerText+"></img>"
		        }
};
var numofselect = document.getElementsByClassName("select").length;
for(var i=0;i<numofselect;i++){
        document.getElementsByClassName("select")[0].setAttribute("class","");console.log(i);
};
var ii = 0;
while(1){
	if(document.getElementsByName("where["+ii+"][op]").length==0)
	{
		break;
	}
	document.getElementsByName("where["+ii+"][op]")[0].innerHTML = document.getElementsByName("where["+ii+"][op]")[0].innerHTML+"<option>=</option><option>!=</option><option>LIKE</option><oprion>NOT LIKE</option><option>REGEXP</option>"
	ii=ii+1;

}


