const form = document.getElementById('form_new_password');




const verify_password=()=> {
    const input_value_new = document.getElementById('new_password').value;
    const input_value_confirm =document.getElementById('confirm_password').value;
    const error_message = document.getElementById('error_message');
    const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    if(input_value_new.trim() === '' || input_value_confirm.trim()==='') {
        error_message.textContent = 'Por favor, verifique que los campos no esten vacios';
        error_message.style.display = 'block';
        return false;
    } else if(regex.test(input_value_new.trim()) === false || regex.test(input_value_confirm.trim()) === false) {
        error_message.textContent = 'La contraseña debe tener al menos 8 caracteres, incluyendo letras y números';
        error_message.style.display = 'block';
        return false;
    } else if(input_value_new.trim() !== input_value_confirm.trim()) {
        error_message.textContent = 'Las contraseñas no coinciden';
        error_message.style.display = 'block';
        return false;
    } else {
        error_message.style.display = 'none';
        return true;
    }

}


const vefify_form = (e)=> {
    e.preventDefault()
    const is_true = verify_password();
    if(is_true) {
            form.submit();
        } else {
            return false;
        }
}


form.addEventListener('submit', vefify_form);
