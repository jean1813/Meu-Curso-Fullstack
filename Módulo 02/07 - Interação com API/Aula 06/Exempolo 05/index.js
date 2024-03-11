// Função assíncrona para fazer o uso do Await
async function buscas(){
    // Await para a execução do programa aguardando
    // o resultado do comando fetch()
    let procura = await fetch("lista-produtos.json")
    let produtos = await procura.json()
    let divLista = document.getElementById("lista-card")
    //console.log(produtos)
    //alert(procura)

    for(let produto of produtos){
        divLista.innerHTML += `
            <div class="card">
                <h3>${produto.nome}</h3>
                <p>${produto.descricao}</p>
                <p> valor com desconto R$ ${produto.valorComDesconto}</p>
                <p> valor sem desconto R$ ${produto.valorSemDesconto}</p>
            </div>

        `
    }
}
buscas()

    //for(let produto in produtos){
       // divLista.innerHTML += `
            //<div class="card">

                //<h3>${produtos[produto].nome}</h3>
               // <p>${produtos[produto].descricao}</p>
               // <p>${produto[produto].valorComDesconto}</p>
               // <p>${produto[produto].valorSemDesconto}</p>

            //</div>

        //`
    //}


