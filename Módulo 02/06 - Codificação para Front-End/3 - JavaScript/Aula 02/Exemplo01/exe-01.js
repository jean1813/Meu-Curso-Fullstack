function verificar(){
    let elemento = document.getElementById("titulo")

    if(elemento.textContent.toLowerCase().includes("p")){
        alert("Tem a letra o")
    }else{
        alert("Não tem a letra o")
    }
}
    