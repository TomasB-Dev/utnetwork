document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault()

    const email = document.getElementById('mail').value.trim()
    const password = document.getElementById('key').value.trim()
    const mensaje = document.getElementById('login-msg')

    if (!validarmail(email)) {
        mensaje.style.color = 'red';
        mensaje.textContent = 'correo invalido.'
        return;
    }

    if (email == "mailfake@mail.com" && password == "123456") {
        mensaje.style.color = 'green'
        mensaje.textContent = 'Logeado'
    } else {
        mensaje.style.color = 'red'
        mensaje.textContent = 'datos incorrectos, vuelve a intentarlo.'
    }
});

function validarmail(email) {
    const regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    return regex.test(email)
}
