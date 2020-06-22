function FA(){
   
   
    var len=document.set_from.elements.length-1;  //length-1, потому что кнопка считается за элемент и мы ее отбрасываем.
      var mas=[];  // создаем массив к торый собственно и будем заполнять
      var paste=document.getElementById('paste'); 
      for(var i=0;i<len;i++){
       var val=document.set_from.elements[i].value;
         if (val!=0 && val!=undefined && val!=null){ // дабы не забивать массив не определенными значениями мы делаем проверку на передаваемое значение;
         mas.push(val);       // работаем с массивом как со стеком
       }
       
      }
     paste.innerHTML=mas; // ну и вывод массива
 }