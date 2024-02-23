async function pessoa(){
    let self = await fetch("pessoa.json") // o fetch gera o objeto resposta
    
    let party = await self.json() 
    console.log(pessoa)

    for(let x in party){
        document.body.innerHTML +=`
        <h1 style="color:blue"> Meu nome é  ${party[x].nome} </h1>
        <p> Meu sobrenome é  ${party[x].sobrenome} </p>
        <p> Minha idade é  ${party[x].idade} anos </p>
        <p> Minha etnia é  ${party[x].etnia} </p>
        <p> O nome da minha mãe é  ${party[x].mae} </p>
        <p style= "color:red">-----------------------------------------------------</p>
        <p style="border:0.5px solid #000"></p>
        <p style="background-color:green; height:5px"></p>
        
        
    `
    }

    
}
pessoa()