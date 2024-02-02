/*
setTimeout(teste, 3000)

function teste(){
    alert("oi")
}
*/

/*
setInterval(teste, 2000)

function teste(){
    document.getElementById("demo").textContent = document.getElementById("demo").textContent + "Testando"
}
*/

/*
setInterval(acionar, 2000)

function acionar(){
    document.getElementById("demo").textContent += "Estuda"
}
*/

/*
setTimeout(acionar, 3000)  => // comando função // acionar uma função depois de um tempo determinado

function acionar(){
    alert("GRATIDÃO")
    alert("PRA QUEM NÃO SABE DE ONDE VEIO QUALQUER CAMINHO É LADO")
}
*/

setInterval(teste, 2000)  //=> // executar uma função a cada x tempo

function teste(){
 
   let elemento = document.getElementById("demo")
   elemento.textContent = elemento.textContent + "  Arthur e Enzo"
}   