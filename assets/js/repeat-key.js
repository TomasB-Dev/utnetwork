const key1 = document.getElementById('password')
const key2 = document.getElementById('repassword')
const estado = document.getElementById('igual')

key2.addEventListener("input",check)
function check() {
    if( key2.value === key1.value){

        estado.textContent = "Las contraseñas coinciden."
        estado.style.color = "green"
    }
    else{
        estado.textContent ="Las contraseñas deben coincidir."
        estado.style.color= "red"
    }
}