async function resolver(){
    let busca1 = await fetch("tarefas.json")//fazendo uma busca
    let lista = await busca1.json()//atribuindo o resultado da busca a variavel LISTA.

    for(let x in lista){
        document.body.innerHTML += `<h1> ${lista[x]} </h1>`
        //document.body.innerHTML = "<p> Olá Mundo </p>"
      
        
    }
}

resolver()