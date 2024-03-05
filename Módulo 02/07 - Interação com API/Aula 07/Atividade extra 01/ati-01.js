async function brasil(){
    let jogo = await fetch("ati-01.json")
    let fut = await jogo.json()
    //console.log(fut)

    let aposta = document.getElementById("lista-card")

    for (let gol of fut) {
        aposta.innerHTML +=`
            <div class="card">
                <p>${gol.time}</p>
                <p>${gol.estado}</p>
                <p>${gol.estadio}</p>
                <img src="${gol.img}" width="200" height="200"> 
            </div>
        `
    }
    
}

brasil()
