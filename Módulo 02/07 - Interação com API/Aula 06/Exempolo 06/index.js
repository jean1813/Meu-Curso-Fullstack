async function buscas(){
    
    let procura = await fetch("lista-produtos.json")//objeto resposta
    let produtos = await procura.json()//lista do objeto resposta
    let divLista = document.getElementById("lista-card")//retorna a tag html div.
    //alert(procura)

    for(let produto of produtos){
        divLista.innerHTML += `
            <div class="card" data-id="${produto.id}">
                <h3>${produto.nome}</h3>
                <img src="${produto.img[0]} "width="200" height="200"/>
                <p>${produto.descricao}</p>
                <div class="valores">
                    <span class="valorCom">R$ ${produto.valorComDesconto.toFixed(2).replace(".", ",")}</span>
                    <span class="valorSem">R$ ${produto.valorSemDesconto.toFixed(2).replace(".",",")}</span>
                </div>
            </div>
        `
    }
    
    let divsCards = document.getElementsByClassName("card") 
    
    for(let card of divsCards){
     
        card.addEventListener("click", clicou)          
    }
    
}

function clicou(){
    //alert("Jean Dev do Senai") //=> quando clicar em cima de cada card,
    
    let elementoId = this.getAttribute("data-id")
    
    window.location.href = "detalhes.html?produto-id=" + elementoId
}

buscas()


