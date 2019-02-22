document.open=time();
setInterval(time,1000);
function time(){
  var h=document.getElementById("t1");
  h.innerHTML=new Date().toLocaleTimeString().slice(0.5);
  
}


var bnt=document.getElementById("bttn");
bnt.addEventListener("click",Tasks)
function  Tasks(){
  var val=document.getElementById('input').value;
  var txt = document.createTextNode(val);
  var li=document.createElement('li');
  var checking=document.createElement("INPUT");
  checking.type="checkbox";
  checking.className="checkclass";
  li.append(checking);
  li.append(txt);
   
  if(val==="" || val===" "){
      alert('Please, write something');
  }
  else {
      document.getElementById('myList').append(li);
  }

  document.getElementById('input').value="";
  var btn=document.createElement("img");
  btn.src="rubbish.png";
  btn.style.width= 30;

//   var btn = document.createElement("INPUT");
  btn.className="close";
//   btn.value="delete";
//   btn.type="button";
  li.appendChild(btn);
  li.onclick=fnctnOnItem;
}
function fnctnOnItem(e){
    if(e.target.className==="close"){
        var div=e.target.parentNode;
        div.remove();
    }
    else if(e.target.className==="checkclass"){
        e.target.parentNode.classList.toggle('checked');
    }

}