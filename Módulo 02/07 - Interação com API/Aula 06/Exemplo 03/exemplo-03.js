async function people(){
    // cria uma variavel que recebe a resposta da busca pro "produtos.json"
    let busca = await fetch("produtos.json") 
    //converte o objeto resposta eu um arquivo legivel pelo JS
    let produtos = await busca.json() 
    
    let grupoDiv = document.getElementById("lista-card")

    for(let produto of produtos){
        grupoDiv.innerHTML +=`
        
           <div class = "card">

                <h3>${produto.nome}</h3>
                <p>${produto.marca}</p>
                <p>${produto.valor}</p>

           </div>
        `
    }   
}

people()
