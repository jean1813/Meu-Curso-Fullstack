async function buscar(){
    let procura = await fetch("exe.json") // o fetch vai trazer o objeto resposta
    //console.log(procura)
    let lista = await procura.json() // o resultado da busca esta sendo convertido

    for( let x in lista){
        //alert(lista[x])
        //alert(x) //printar a posição de cada item

        let indice = parseInt(Math.random()* 4)
        //let g = Math.random()* 255
        //let b = Math.random()* 255
        
        document.body.innerHTML += `
            <h1 style="color:${cores[indice]}">
                
                ${lista[x]}
            </h1>
        ` 
    }
    
    //alert(lista[0]) //printar maça
    //alert(lista[1]) //printar banana
    //alert(lista[2]) //printar cereja
    //console.log(lista[1])
}

buscar()