function likeButton(){
    document.getElementById("Like").classList.toggle("blue");
}


function heartButton(){
    if( document.getElementById("Heart").style.color == "red"){
        document.getElementById ("Heart").style.color = "black"
        alert("Kitabi beyenmediniz");}
    else if (document.getElementById("Heart").style.color == "black"){
        document.getElementById("Heart").style.color = "red"
        alert("Kitabi Beyendiniz")

    }
}    


//  let kitab = document.createElement("p");
//     kitab.innerHTML = "  <li><span>X </span> Inkignito : (<span>12</span>Azn)</li>"
//     kitab.getElementsByTagName("span")[0].classList.add("text-danger");
//     kitab.getElementsByTagName("span")[0].classList.add("border-0");
//     kitab.getElementsByTagName("span")[0].setAttribute("onclick" , "deleteF(this);")
//     let addSebet = document.getElementById("Add_sebet")
//     let alert_say = document.getElementById("alert_word");
//     let cartt = document.getElementById("cart_dd")
   
 
 
//    let r = document.getElementById("q_1").textContent;
//    let z =  document.getElementById("q_2").textContent;
//    let result = parseFloat(r) + parseFloat (z);
//    console.log(result);
//    document.getElementById("result").innerText = result 
   







// let k_s = 2
// let a_s = 2
// function addCart(){
   

//     if (addSebet.style.backgroundColor == "gray"){
//         alert("Mehsul sebetden cixarildi");
//         addSebet.style.backgroundColor = "darkcyan";
//         addSebet.innerText = "Sebete elave et";
//         cartt.removeChild( cartt.firstElementChild);
//         document.getElementById("kitab_sayi").innerHTML = (k_s = k_s - 1);
//         alert_say.getElementsByTagName("span")[0].innerHTML = (a_s = a_s + 1);
//         alert_say.classList.remove("alert-danger");
//         alert_say.classList.add("alert-warning")



//         let f = kitab.getElementsByTagName("span")[1].textContent;
//         result = result - parseFloat(f)
//         document.getElementById("result").innerText = result

        
        





//     }

//     else{
//         alert("Mehsul sebete elave edildi")
//         addSebet.style.backgroundColor = "gray";
//         addSebet.innerText = "Sebetden cixar";
    
    
//         document.getElementById("cart_dd").prepend(kitab);
  

//         document.getElementById("kitab_sayi").innerHTML = (k_s = k_s + 1);
    
    
//         alert_say.getElementsByTagName("span")[0].innerHTML = (a_s = a_s - 1 );
//         alert_say.classList.remove("alert-warning");
//         alert_say.classList.add("alert-danger")

//         let f = kitab.getElementsByTagName("span")[1].textContent;
//         result = result + parseFloat(f)
//         document.getElementById("result").innerText = result
//         document.getElementById("kitab_sayi").style.display = "block"
   

//     }
    

// }


// function deleteF(element){
//     let parent_e = element.parentNode.parentNode;
//     console.log(element);
//     parent_e.parentNode.removeChild(parent_e);
//     document.getElementById("kitab_sayi").innerHTML = (k_s = k_s - 1);
//     let a = element.nextElementSibling.textContent;
//     result = result - a;
//     document.getElementById("result").innerText = result
//     console.log(kitab.getElementsByTagName("span")[0]);


//     if(kitab.getElementsByTagName("span")[0] == element){
//        addSebet.style.backgroundColor = "darkcyan";
//        addSebet.innerText = "Sebete elave et";
//        alert_say.getElementsByTagName("span")[0].innerHTML = (a_s = a_s + 1);
//         alert_say.classList.remove("alert-danger");
//         alert_say.classList.add("alert-warning")
//     }


//     if (k_s == 0){
//         document.getElementById("kitab_sayi").style.display = "none"
//     }



// }




let kitabList =[
    {
        "Sekil":"/static/images/312861_0d6fa_1538476516.jpg",
        "KitabAd":"Sefiller",
        'Ad':"Victor Hugo"
    },
    {
        "Sekil":"/static/images/Inkognito.png",
        "KitabAd":"Inkognito",
        "Ad":"David Eagleman"
    },
    {
        "Sekil":"/static/images/56586_6f66e_1619754763.jpg",
        'KitabAd':"1984",
        'Ad':"George Orwell"
    }
];



let input = document.getElementById("input").value;
input = "0";


let row = document.getElementById("main")


document.getElementById("success").addEventListener("click" , function(){
    input = parseInt(input) + 1;
    document.getElementById("input").value = input;
    item = kitabList[Math.floor(Math.random()*kitabList.length)];
    console.log(item); 
    let sh = item['Sekil'];
    let ka = item['KitabAd'];
    let a = item['Ad']
  
    // console.log(sh);
    // console.log(ka);
    // console.log(a);


    let card = document.createElement("div")
    card.classList.add("col-4");
    card.classList.add("mb-5")  

    card.innerHTML = `
  
    <div class="card" style="width: 10rem;">
      <img src="" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title"></h5>
        <p class="card-text"></p>
        <a href="#" class="btn btn-primary">Etrafli</a>
      </div>
    </div>`




    let img = card.getElementsByTagName('img')[0];
    let h5 = card.getElementsByTagName('h5')[0];
    let p = card.getElementsByTagName('p')[0];
    
    img.setAttribute("src" , sh);
    h5.innerText = ka
    p.innerText = a
    
    console.log(h5.textContent);


    if(h5.textContent == '1984'){
        card.classList.add("Bilim");
    }
    else if (h5.textContent == "Sefiller"){
        card.classList.add("Roman")
    }
    else if (h5.textContent == "Inkognito"){
        card.classList.add("Psixo")
    }
    
  


   
    row.prepend(card);
  


   
    

})


document.getElementById("danger").addEventListener("click" , function(){
    if (input > 0)
    { input = parseInt(input) - 1;
        document.getElementById("input").value = input;
        
  
    row.removeChild(row.children[0])
    
    
    
    }

})






document.getElementById("btn").addEventListener("click", function(){


    if(this.innerText == "Bitir"){
        document.getElementById("sorgu").classList.remove("d-block");
        document.getElementById("sorgu").classList.add("d-none");
        this.classList.remove("btn-danger");
        this.innerText = "Basla"

    }
    else{
            document.getElementById("sorgu").classList.remove("d-none");
            document.getElementById("sorgu").classList.add("d-block");
            this.classList.add("btn-danger")
            this.innerText = "Bitir"
    
    }
   


})


document.getElementById("hesabla").addEventListener("click" , function(){
    let umumi = document.getElementById("umumi").value;
    let xususi = document.getElementById("xususi").value;
    let netice = parseInt(umumi) / parseInt(xususi);
    console.log(netice);
    if(isNaN(netice)){
        document.getElementById("alert").innerText = "Zehmet deilse duzgun reqem daxil edin"

    }
    else{ document.getElementById("alert").innerHTML = "Her gun en az <b> " + netice + " </b>sehife oxumalisiniz" }
   

})

















let b = document.getElementsByClassName("Bilim");
let r = document.getElementsByClassName("Roman");
let p = document.getElementsByClassName("Psixo");


document.getElementById("Hamisi").addEventListener("click",function(){
    for (i of b){
       
        i.classList.remove("d-none")
        i.classList.add("d-block")
    } 
    for (i of r){
       
        i.classList.remove("d-none")
        i.classList.add("d-block")
    } 
    for (i of p){
      
        i.classList.remove("d-none")
        i.classList.add("d-block")
    }          
    

})






document.getElementById("Psixo").addEventListener("click",function(){

    for (i of b){
     
        i.classList.remove("d-block")
        i.classList.add("d-none")

    }
    for (i of r){
        i.classList.remove("d-block")
        i.classList.add("d-none")

    }
    for (i of p){
        i.classList.remove("d-none")
        i.classList.add("d-block")

    }
    

})


document.getElementById("Roman").addEventListener("click",function(){
    
    for (i of b){
       
        i.classList.remove("d-block")
        i.classList.add("d-none")

    }
    for (i of r){
        i.classList.remove("d-none")
        i.classList.add("d-block")

    }
    for (i of p){
        i.classList.remove("d-block")
        i.classList.add("d-none")

    }




})



document.getElementById("Bilim").addEventListener("click",function(){
    for (i of b){
       
        i.classList.remove("d-none")
        i.classList.add("d-block")

    }
    for (i of r){
        i.classList.remove("d-block")
        i.classList.add("d-none")

    }
    for (i of p){
        i.classList.remove("d-block")
        i.classList.add("d-none")

    }




})




