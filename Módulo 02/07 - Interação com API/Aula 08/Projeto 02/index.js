// Função assíncrona para fazer o uso do Await
async function buscas(){
    // Await para(stop) a execução do programa aguardando
    // o resultado do comando fetch()
    let procura = await fetch("projeto.json")//objeto resposta
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
                <div class="lado">
                    <img class="img-card" src="${produto.img} "width="200" height="200"/>
                    <span class="ns-h6mex-e-23" dir="auto" x-score="1">-25%</span>
                </div>
                <p>${produto.descricao}</p>
                <div class="valores">
                    <span class="valorCom">R$ ${produto.valorComDesconto.toFixed(2).replace(".", ",")}</span>
                    <span class="valorSem">R$ ${produto.valorSemDesconto.toFixed(2).replace(".",",")}</span>
                    
                </div>
            </div>
        `
    }
    // Buscar por todos os elementos HTML que contém "card"
    // como valor do parâmetro "class".
    let divsCards = document.getElementsByClassName("card") 
    
    for(let card of divsCards){
     // Add em cada Div Card um evento que escuta quando o 
    // usuário clica nele, e chama uma função.
        card.addEventListener("click", clicou)          
    }
    
}
// É chamada essa função quando o usuário clicou 
// em card que contém o evento de Escuta.
function clicou(){
    //alert("Jean Dev do Senai") => quando clicar em cima de cada card,
    // Coleta o valor do atributo "data-id" do elemento
    // HTML que acionou o evento de Escuta.
    let elementoId = this.getAttribute("data-id")
    //alert(window.location.href) printa o endereço atual da pagina.
    //
    window.location.href = "detalhes.html?produto-id=" + elementoId
}

buscas()