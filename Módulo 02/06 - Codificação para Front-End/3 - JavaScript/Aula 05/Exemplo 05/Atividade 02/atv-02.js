let numeros = [2,7,4,9,1]
//prompt("Digite um numero")

for (let x in numeros){
    //alert(numeros[x])

    if(numeros[x] % 2 == 0){
        alert("o numero " + numeros[x] + " é par.")
    }else{
        alert("o numero " + numeros[x] + " é impar.")
    }
}


