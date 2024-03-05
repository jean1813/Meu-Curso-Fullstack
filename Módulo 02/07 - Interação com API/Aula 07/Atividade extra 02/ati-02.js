async function marcas(){
    let mer = await fetch("ati-02.json")
    let bol = await mer.json()
    console.log(bol)

    let digita = document.getElementById("lista-card")

    for (let gol of bol) {
        digita.innerHTML +=`
            <div class="card">
                <p>${gol.marca}</p>
                <p>${gol.modelo}</p>
                <p>${gol.produto}</p>
                <p>${gol.acessorio}</p>
                <img src="${gol.img}" width="150" height="150"> 
            </div>
        `
    }

}

marcas()