async function saude(){
    let bemEstar = await fetch("corrida.txt")
    let saudeMental = await bemEstar.text()
    console.log(saudeMental)
    alert(saudeMental)
}
saude()