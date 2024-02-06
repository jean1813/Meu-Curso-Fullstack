async function pesquisar(){
    let voltar = await fetch("exemplo.txt")
    let convertido = await voltar.text() 
    console.log(convertido)
    alert(convertido)
}
pesquisar()