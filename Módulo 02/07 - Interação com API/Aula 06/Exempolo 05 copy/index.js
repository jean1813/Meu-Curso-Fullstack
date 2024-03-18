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
            <div class="card" data-id="${produto.id}">
                <h3>${produto.nome}</h3>
                <img src="${produto.img} "width="200" height="200"/>
                <p>${produto.descricao}</p>
                <div class="valores">
                    <span class="valorCom">R$ ${produto.valorComDesconto.toFixed(2).replace(".", ",")}</span>
                    <span class="valorSem">R$ ${produto.valorSemDesconto.toFixed(2).replace(".",",")}</span>
                </div>
            </div>
        `
    }

    let divsCards = document.getElementsByClassName("card")
    
}
buscas()

    //in = ao indice da lista(0,1,2...)
    //for(let produto in produtos){
       // divLista.innerHTML += `
            //<div class="card">

                //<h3>${produtos[produto].nome}</h3>
                //<img src="${produtos.[produto}" width="200" height="200"/>
               // <p>${produtos[produto].descricao}</p>
               // <p>${produto[produto].valorComDesconto}</p>
               // <p>${produto[produto].valorSemDesconto}</p>

            //</div>

        //`
    //}


