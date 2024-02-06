async function trazer(){
    let resposta = await fetch("futebol.txt")
    let convertido = await resposta.text()
    console.log(convertido)
    alert(convertido)
}

trazer()