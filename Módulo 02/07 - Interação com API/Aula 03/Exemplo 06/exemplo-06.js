async function refri(){
    let conteudo = await fetch("pepsi.txt")
    let liquido = await conteudo.text() 
    console.log(liquido)
    alert("BEBA COM MODERAÇÃO:  " +liquido)
}
refri()