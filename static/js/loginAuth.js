// const formulario = document.getElementById('login-form')
// formulario.addEventListener('submit', function (e) {
//     e.preventDefault()

//     const email = document.getElementById('mail').value.trim()
    
//     const mensaje = document.getElementById('login-msg')

//     if (!validarmail(email)) {
//         mensaje.style.color = 'red';
//         mensaje.textContent = 'El correo es invalido.'
//         return;
//     }
//     formulario.submit();
    
    
//     // Este login es fake hasta que implementemos el backend y poder obtener los datos
//     // de una DB real.
    
// });

// function validarmail(email) {
//     const regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
//     return regex.test(email)
// }




const authForm= document.getElementById('login-form');


const validatePassword =()=> {
    const value = document.getElementById('password').value;
    const input = document.getElementById("password");
    const error_message = document.getElementById('error_password');
    const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    const verifyPassword= regex.test(value)

    if(!verifyPassword  ) {
        input.classList.add('error_input')
        error_message.textContent= 'Debe tener al menos 8 caracteres, una letra y un numero.';
        error_message.style.display = 'block';
        return false;
    } else {
        input.classList.remove('error_input');
        error_message.style.display='none';
            return true;

    }



}


const validateEmail=()=> {
    const value = document.getElementById('mail').value;
    const input = document.getElementById('mail')
    const error_message = document.getElementById("error_mail")
    const regex  = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const verifyEmail = regex.test(value);


    if(!verifyEmail) {
        input.classList.add('error_input')
        error_message.textContent= 'Error verifique que el correo sea correcto';
        error_message.style.display = 'block';
        return false;
    } else {
        input.classList.remove('error_input');
        error_message.style.display='none';
            return true;

    }



}







const validateForm =(e)=> {
    e.preventDefault();


    const responseEmail = validateEmail();
    const responsePassword = validatePassword();


    if(responseEmail && responsePassword){ 
        authForm.submit()
    } else {
        return;
    }


}



authForm.addEventListener('submit', validateForm);




