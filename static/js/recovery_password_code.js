import { BASE_URL } from "./base_url.js";
const form_code = document.getElementById('form_code');

const enviar_codigo = (e)=> {
    e.preventDefault();


        let codigo = '';
            for (let i = 1; i <= 6; i++) {
                codigo += document.getElementById(`${i}c`).value;
            }

    fetch(`${BASE_URL}/verificar_codigo_reestablecimiento`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ codigo: codigo })  // 👈 También importante
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = data.redirect_url; // Redirige a la URL proporcionada por el servidor
        } else {
            alert('Código incorrecto. Inténtalo de nuevo.');
        }
    })
    
}



form_code.addEventListener('submit', enviar_codigo)