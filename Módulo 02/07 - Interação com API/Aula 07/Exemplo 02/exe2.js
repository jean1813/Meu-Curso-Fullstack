async function friend(){
    let skol = await fetch("amigos.json")
    let puroMalte = await skol.json()
    console.log(puroMalte)

    let digita = document.getElementById("lista-card")

    for (let bebida of puroMalte) {
        digita.innerHTML +=`
            <div class="card">
                <h3>${bebida.nome}</h3>
                <p class="detalhe">${bebida.sobrenome}</p>
                <p class="detalhe">${bebida.apelido}</p>
                <p class="detalhe">${bebida.time}</p>
                <img src="${bebida.img}" width="150" height="150"> 
                <a href="https://www.pensador.com/melhores_amigos/">
            <button class="btn">CLIQUE AQUI</button>
        </a>
            </div>
        `
    }

}

friend()