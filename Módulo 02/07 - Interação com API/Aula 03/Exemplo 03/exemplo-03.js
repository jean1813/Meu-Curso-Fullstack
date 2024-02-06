async function procurar(){
    let resposta = await fetch("mensagem.txt")
    let convertido = await resposta.text() 
    console.log("o texto: "+convertido)
    alert("o texto foi convertido para: " + convertido)
}
procurar()