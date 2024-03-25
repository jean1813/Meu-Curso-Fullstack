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

    // Criou uma variável vazia
    let indiceProd
    // Usou o for para percorrer toda a lista de produtos do JSON 
    for(let x in produtos){
        console.log("o valor de x é: " + x)
        console.log(`produtos[x].id é: ${produtos[x].id}`)
        console.log(`parametroID é: ${parametroID}`)
        console.log(`${produtos[x].id} == ${parametroID}`) 
        if(produtos[x].id == parametroID){
            // Atribuiu à variável vazia, o valor de x, que contém
            // o indice do produto que corresponde ao ID da URL
            indiceProd = x   
        }
    }

    // Adiciona na TAG BODY do HTML, um código HTML concatenado
    // com valores do objeto produto encontrado
    document.body.innerHTML = `
        <div class="detalhes-corpo">
        <img src="${produtos[indiceProd].img}" width="250" height"250">
            <h3>${produtos[indiceProd].nome}</h3>
            <p>${produtos[indiceProd].descricao}</p>
            <span> O valor com desconto: R$ R$ ${produtos[indiceProd].valorComDesconto.toFixed(2).replace(".", ",") }</span>
            <span class="color"> O valor sem desconto: R$  ${produtos[indiceProd].valorSemDesconto.toFixed(2).replace(".", ",")}</span>
        </div>
        
    `
    //alert("indiceProd= "  + indiceProd)
    //alert(parametroID)
    //alert(window.location.search) // => ?produto-id=1

}

buscarDetalhes()

