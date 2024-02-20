async function resolver(){
    let busca1 = await fetch("tarefas.json")//fazendo uma busca
    let lista = await busca1.json()//atribuindo o resultado da busca a variável LISTA.

    let busca2 = await fetch("cores.json")
    let cores = await busca2.json()
    //alert(cores)


   /* for(let x in lista){
        document.body.innerHTML += `<h1> ${lista[x]} </h1>`    
    }*/


for(let x of lista){  // of recebe o conteúdo do item
                     //  in recebe o o número do item
    //alert(x)
    let corAleatoria = parseInt(Math.random()*7)
    
    document.body.innerHTML += `
        <h1 style ="color:${cores[corAleatoria]}"> ${[x]} </h1>
    `        
}

}

resolver()