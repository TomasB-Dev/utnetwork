


const form = document.getElementById('form');


const validate_nombre = ()=> {
    const input = document.getElementById('nombre_usuario');
    const error_name = document.getElementById('error_name');
    const regex = /^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\-_!@#$%^&*()\[\]{}.,<>?:;"'=+|\\/~]+$/;
    const value = input.value
    const verify_value = regex.test(value);


    if(!verify_value || value.trim() === ''){
        error_name.style.display ='block'
        error_name.textContent='error, vuelva a verificar';
        input.classList.add('input_error');
        return false;
    } else {
        error_name.style.display='none';
        input.classList.remove('input_error');
        return true;
    
    };

}


const validate_email = ()=> {
    const input = document.getElementById('mail');
    const error_name = document.getElementById('error_mail');
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const value = input.value
    const verify_value = regex.test(value);


    if(!verify_value || value.trim() === ''){
        error_name.style.display ='block'
        error_name.textContent='error, vuelva a verificar';
        input.classList.add('input_error');
        return false;
    } else {
        error_name.style.display='none';
        input.classList.remove('input_error');
        return true;
    
    };
}


const validate_password = ()=> {
    const input = document.getElementById('key');
    const error_name = document.getElementById('error_key');
    const regex = /^$|^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    const value = input.value
    const verify_value = regex.test(value);


    if(!verify_value){
        error_name.style.display ='block'
        error_name.textContent='error, vuelva a verificar';
        input.classList.add('input_error');
        return false;
    } else {
        error_name.style.display='none';
        input.classList.remove('input_error');
        return true;
    
    };
}


const validateForm =(e)=> {
    e.preventDefault();

    const nombre = validate_nombre();
    const email = validate_email();
    const password= validate_password();

    if(!nombre || !email || !password) {
        return false;
    }


    form.submit();
    
}



form.addEventListener('submit', validateForm)




