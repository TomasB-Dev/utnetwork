import { BASE_URL } from "./base_url";

// codigo para verificar email
const validate_email =()=> {
    const input_value = document.getElementById('mail').value;
    const regex  = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const error_message = document.getElementById('error_email');
    
    const verify_email = regex.test(input_value);

    console.log(input_value)

    if(input_value.trim()=== '' || !verify_email) {
        error_message.style.display ='block';
        error_message.textContent='Error verifique el email';
        return false;
    } else {
        error_message.style.display='none';
        return true;
    }
    
}


const form_email = document.getElementById('form_email');


const validate_form_email =(e)=> {
    e.preventDefault();
    let verify_email= validate_email();

    if(verify_email) {
        form_email.submit();
    }
}


form_email.addEventListener('submit', validate_form_email);



// logica para verificar el codigo enviado


// const form_code = document.getElementById('form_code');


// const enviar_codigo = (e)=> {
//     e.preventDefault();

//     mail= document.getElementById('mail_used').value

//         let codigo = '';
//             for (let i = 1; i <= 6; i++) {
//                 codigo += document.getElementById(`${i}c`).value;
//             }

//     fetch(`${BASE_URL}/verificar_codigo_reestablecimiento`, {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({codigo})
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data, 'upa')
//         alert("codigo enviado", data)
//     })
// }



// form_code.addEventListener('submit', enviar_codigo)