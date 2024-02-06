async function marketing(){
    let voltar = await fetch("propaga.txt")
    let disseminar = await voltar.text() 
    console.log(disseminar)
    alert(disseminar)
}
marketing()