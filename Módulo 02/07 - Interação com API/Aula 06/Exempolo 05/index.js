// Função assíncrona para fazer o uso do Await
async function buscas(){
    // Await para(stop) a execução do programa aguardando
    // o resultado do comando fetch()
    let procura = await fetch("lista-produtos.json")//objeto resposta
    let produtos = await procura.json()//lista do objeto resposta
    let divLista = document.getElementById("lista-card")//retorna a tag html div.
    //console.log(produtos)
    //alert(procura)

    // por que usar o for? => pra percorrer uma lista
    // Quantas linhas de comando tem dentro do for? => 1 linha(divLista.inneHTML)
    for(let produto of produtos){
        divLista.innerHTML += `
            <div class="card">
                <h3>${produto.nome}</h3>
                <p>${produto.descricao}</p>
                <div class="valores">
                    <span>R$ ${produto.valorComDesconto.toFixed(2)}</span>
                    <span>R$ ${produto.valorSemDesconto.toFixed(2)}</span>
                </div>
            </div>
        `
    }
}
buscas()

    //in = ao indice da lista(0,1,2...)
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


