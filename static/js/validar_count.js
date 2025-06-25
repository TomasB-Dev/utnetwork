// document.addEventListener('DOMContentLoaded', function () {
//     const formulario = document.getElementById('form-codigo');

//     formulario.addEventListener('submit', function (e) {
//         e.preventDefault();

//         const datos = {
//             c1: document.getElementById('1c').value,
//             c2: document.getElementById('2c').value,
//             c3: document.getElementById('3c').value,
//             c4: document.getElementById('4c').value,
//             c5: document.getElementById('5c').value,
//             c6: document.getElementById('6c').value,
//         };

//         fetch('http://127.0.0.1:5000/validar-codigo', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify(datos),
//         })
//         .then(res => res.json())
//         .then(respuesta => {
//             const mensaje = document.getElementById('mensaje-respuesta');
//             if (respuesta.correcto) {
//                 window.location.href = respuesta.redirect_url; /* diablo loco , reza reza */
//             } else {
//                 mensaje.textContent = 'Codigo incorrecto';
//                 mensaje.style.color = 'red';
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//         });
//     });
// });


function enviarCodigo(e) {
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
            console.log(respuesta);
            if (respuesta.correcto) {
                window.location.href = respuesta.redirect_url; /* diablo loco , reza reza */
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}



function reenviarCodigo(e) {
    e.preventDefault()

    const btn = document.getElementById('btn_re_send')
    btn.classList.remove('btn_re_send_code')
    btn.classList.add('btn_disabled')
    btn.disabled= true;

    fetch('http://127.0.0.1:5000/reenviar-codigo')
    .then(response => response.json())
    .then(data => {
        if(data.reenviado) {
            Toastify({
                text: "El codigo fue reenviado correctamente",
                className: "info",
                style: {
                    background: "#00628D",
                }
                }).showToast();
        } else {
            Toastify({
                text: "Error al reenviar el codigo",
                className: "info",
                style: {
                    background: "red",
                }
                }).showToast();
        }
    })


    setTimeout(()=> {
        
        btn.classList.remove('btn_disabled')
        btn.classList.add('btn_re_send_code')
        btn.disabled=false;
    }, 10000)

  

}



function pegarCodigo() {
    navigator.clipboard.readText().then(text => {
        const inputs = document.querySelectorAll('.code');
        const character = text.trim().slice(0, inputs.length).split('');

        character.forEach((char, index)=> {
            inputs[index].value = char;

        })
    }).catch(err => {
        alert("error al acceder al portapapeles");
        console.error(err);
    })
}