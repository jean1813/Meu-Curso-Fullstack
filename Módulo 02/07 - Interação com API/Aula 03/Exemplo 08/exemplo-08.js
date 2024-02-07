/*function sos(){
document.getElementById("bomba").textContent = "Vamos"

}*/

async function sos(){
    let trocar = await fetch("btn.txt")
    console.log(trocar)
    let mesmoSinal = await trocar.text()
    console.log(mesmoSinal)
    alert(mesmoSinal)
}


