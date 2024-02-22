async function pessoa(){
    let self = await fetch("pessoa.json") // o fetch gera o objeto resposta
    
    let party = await self.json() 
    console.log(pessoa)

    for(let x in party){
        document.body.innerHTML +=`
        <h1 style="color:blue"> Meu nome é  ${party[0].nome} </h1>
        <p> Meu sobrenome é  ${party[0].sobrenome} </p>
        <p> Minha idade é  ${party[0].idade} </p>
        <p> Minha etnia é  ${party[0].etnia} </p>
        <p> O nome da minha mãe é  ${party[0].mae} </p>
        <p>-----------------------------------------------------</p>
    `
    }

    
}
pessoa()