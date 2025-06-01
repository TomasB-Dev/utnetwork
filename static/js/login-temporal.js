const formulario = document.getElementById('login-form')
formulario.addEventListener('submit', function (e) {
    e.preventDefault()

    const email = document.getElementById('mail').value.trim()
    
    const mensaje = document.getElementById('login-msg')

    if (!validarmail(email)) {
        mensaje.style.color = 'red';
        mensaje.textContent = 'El correo es invalido.'
        return;
    }
    formulario.submit();
    console.log('lo tomo bien')
    
    // Este login es fake hasta que implementemos el backend y poder obtener los datos
    // de una DB real.
    
});

function validarmail(email) {
    const regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    return regex.test(email)
}
