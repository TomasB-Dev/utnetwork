
const authForm= document.getElementById('form');




const validateTerm =()=> {
    const error_message = document.getElementById('error_term')
    const value = document.getElementById('check')

    if(!value.checked) {
        error_message.style.display = 'block'
        error_message.textContent= 'Debes aceptar los terminos y condiciones.'


        return false
    } else {
        error_message.style.display = 'none'
        value.classList.remove('error_input')
        return true

    }



}


const validateName = ()=> {
    const error_message = document.getElementById('error_name');
    const value = document.getElementById('name').value.trim();
    const input = document.getElementById('name');
    const regex = /^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\-_!@#$%^&*()\[\]{}.,<>?:;"'=+|\\/~]+$/;

    let verify = regex.test(value);


    if(value.length <3 || !verify) {
        error_message.textContent= 'Debe tener al menos 3 caracteres.'
        error_message.style.display = 'block'
        input.classList.add('error_input')
        return false
    } else {
        error_message.style.display = 'none'
        input.classList.remove('error_input')
        return true;
    }
}


const validateEmail = ()=> {
    const error_message = document.getElementById("error_email");
    const value = document.getElementById('email').value.trim();
    const input = document.getElementById('email');
    const regex  = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    let verify = regex.test(value);


    if(!verify) {
        error_message.style.display = 'block'
        error_message.textContent= 'El correo no es valido.'
        input.classList.add('error_input')
        return false
    } else {
        error_message.style.display = 'none'
        input.classList.remove('error_input')
        return true;
    }


}



const validatePassword = ()=> {
    const error_message = document.getElementById('error_password');
    const value = document.getElementById('password').value.trim();
    const input = document.getElementById('password');
    const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    let verify = regex.test(value);
    if(value.length < 8 || !verify) {
        error_message.textContent= 'Debe tener al menos 8 caracteres, una letra y un numero.'
        error_message.style.display = 'block'
        input.classList.add('error_input')
        return false;
    } else {
        error_message.style.display = 'none'
        input.classList.remove('error_input')
        return true;
    }


}



const validateConfirmPassword = ()=> {
    const error_message = document.getElementById('error_confirm_password');
    const value = document.getElementById('confirm_password').value.trim();
    const input = document.getElementById('confirm_password');
    const password = document.getElementById('password').value.trim();

    if(value !== password) {
        error_message.style.display = 'block'

        error_message.textContent= 'Las contraseñas deben coincidir.'
        input.classList.add('error_input')
        return false
    } else {
        error_message.style.display = 'none'
        input.classList.remove('error_input')
            return true;

    }


}

const successMessage = ()=> {
    const message = document.getElementById('success_message');
    message.style.display = 'block';
    message.textContent = 'Usted se registró con exito.';
    

}



const validateForm = (e)=> {
    e.preventDefault();
    const term = validateTerm();
    const name = validateName();
    const email = validateEmail();
    const password = validatePassword();
    const confirm_password = validateConfirmPassword();
    
    if(term && name && email && password && confirm_password){
        successMessage();
        authForm.submit();
    
    } else {

        return 
    }
    
}



authForm.addEventListener('submit', validateForm);
