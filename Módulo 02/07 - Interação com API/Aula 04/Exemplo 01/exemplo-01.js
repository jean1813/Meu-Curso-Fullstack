async function mexer(){
    let resposta = await fetch("msg.txt")
    let convertido = await resposta.text()
    //console.log(convertido)
    //alert(convertido)

    //document.body.innerHTML = "<h1>" + convertido + "</h1>"

    //document.body.innerHTML = `<h1>${convertido}</h1>`

    /*document.body.innerHTML = `
        <h1>
            ${convertido}
        </h1>
        <p>
            como esta?
        </p>
    `*/

    let tnt = [2, 13, 19, 20]
    for (let x in tnt){  
        //alert(x) 
    }

    for (let x = 0; x <=2; x++) {
        
        //alert(x)

        document.body.innerHTML += `
            <h1>
                ${convertido}
            </h1>
            <p>
                ${tnt[x]}
            </p>
        `
    }
}

mexer() 


