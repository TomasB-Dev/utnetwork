document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault()

    const email = document.getElementById('mail').value.trim()
    const password = document.getElementById('key').value.trim()
    const mensaje = document.getElementById('login-msg')

    if (!validarmail(email)) {
        mensaje.style.color = 'red';
        mensaje.textContent = 'El correo es invalido.'
        return;
    }
    // Este login es fake hasta que implementemos el backend y poder obtener los datos
    // de una DB real.
    if (email == "mailfake@mail.com" && password == "123456") {
        
        mensaje.style.color = 'green'
        mensaje.textContent = 'Ingreso correctamente.'
    } else {
        mensaje.style.color = 'red'
        mensaje.textContent = 'Los datos son incorrectos, vuelve a intentarlo.'
    }
});

function validarmail(email) {
    const regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    return regex.test(email)
}
