

const verifyComment=(e)=> {
    e.preventDefault();
   const id_error = document.getElementById('error_descripcion');
   const value = document.getElementById('descripcion_contenido').value;

    if(value.trim() === '') {
        id_error.style.display= 'block'
        id_error.textContent='Debe ingresar contenido'
    } else  {
        id_error.style.display='none'
        update_description_form.submit()
    }


}



const update_description_form = document.getElementById('update_description')



update_description_form.addEventListener("submit", (e)=> verifyComment(e))