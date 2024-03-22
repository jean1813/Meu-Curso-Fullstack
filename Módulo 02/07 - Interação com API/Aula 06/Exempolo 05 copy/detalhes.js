async function buscarDetalhes(){
    // Consumo do JSON
    let busca = await fetch("lista-produtos.json")
    let produtos = await busca.json()
    console.log(produtos)

    // Criou um objejto URLSearchParams e passou
    // a coleta dos parametros da URL nele.
    let parametros = new URLSearchParams(window.location.search)
    // Obteve do parametro "produto-id", o seu valor
    let parametroID = parametros.get("produto-id")

    let indiceProd
    for(let x in produtos){
        console.log("o valor de x é: " + x)
        console.log(`produtos[x].id é: ${produtos[x].id}`)
        console.log(`parametroID é: ${parametroID}`)
        console.log(`${produtos[x].id} == ${parametroID}`) 
        if(produtos[x].id == parametroID){
            //console.log("SIM")
            indiceProd = x   
        }
    }

    document.body.innerHTML = `
        <img src="${produtos[indiceProd].img}" width="250" height"250">
    `
    //alert("indiceProd= "  + indiceProd)
    //alert(parametroID)
    //alert(window.location.search) // => ?produto-id=1

}

buscarDetalhes()

