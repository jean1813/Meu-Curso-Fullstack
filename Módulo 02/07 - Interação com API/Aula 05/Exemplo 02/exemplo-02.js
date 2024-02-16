async function olx(){
    let busca = await fetch("carros.json") 
    console.log()
    
    let convertido = await busca.json() 

    //for( let x in convertido ){
        alert(convertido[1].modelo)
        
    //} 
}

olx()
