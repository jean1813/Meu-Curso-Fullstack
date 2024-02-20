async function fazer(){
    let busca1 = await fetch("executar.json")
    let lista = await busca1.json() 

    let busca2 = await fetch("cores.json")
    let cores = await busca2.json()
    
for(let x in lista){  
    
    document.body.innerHTML += `
        <h1 style ="color:${cores[x]}"> ${lista[x]} </h1>
    `        
}

}

fazer()