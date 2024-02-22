async function concessionaria(){
    let resultado = await fetch("carros.json") // o fetch gera o objeto resposta
    
    let carros = await resultado.json() //a variavel carros esta recebendo conversão do objeto resposta!
    console.log(carros)
    //alert("A marca é " +carros.marca+ ", o modelo é " +carros.modelo+ ", e o ano é " +carros.ano+ ", e a cor é " +carros.cor)
    //A marca é x, o modelo é x, o ano é x e a cor é x
           
    //alert(carro.marca)

    //alert(carros[2].modelo)
    //carros = [0,1,2]
    document.body.innerHTML +=`
        <h1 style="color:blue"> A marca do carro é  ${carros[1].marca} </h1>
        <p> O modelo do carro é  ${carros[1].modelo} </p>
        <p> O ano do carro é  ${carros[1].ano} </p>
        <p> A cor do carro é  ${carros[1].cor} </p>
    `
    //document.body.innerHTML +=`
   // <p> A modelo do carro é " ${carros[0].modelo} </p>
    //`
   // document.body.innerHTML +=`
    //<p> O ano do carro é " ${carros[0].ano} </p>
    //`
    //document.body.innerHTML +=`
    //<p> A cor do carro é " ${carros[0].cor} </p>
    //`
    
    //for( let x in carros){
        //alert(carros[0].modelo)
    //}
    
}
concessionaria()
