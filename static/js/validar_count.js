document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.getElementById('form-codigo');

    formulario.addEventListener('submit', function (e) {
        e.preventDefault();

        const datos = {
            c1: document.getElementById('1c').value,
            c2: document.getElementById('2c').value,
            c3: document.getElementById('3c').value,
            c4: document.getElementById('4c').value,
            c5: document.getElementById('5c').value,
            c6: document.getElementById('6c').value,
        };

        fetch('http://127.0.0.1:5000/validar-codigo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(datos),
        })
        .then(res => res.json())
        .then(respuesta => {
            const mensaje = document.getElementById('mensaje-respuesta');
            if (respuesta.correcto) {
                window.location.href = respuesta.redirect_url; /* diablo loco , reza reza */
            } else {
                mensaje.textContent = 'Codigo incorrecto';
                mensaje.style.color = 'red';
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});