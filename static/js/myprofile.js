

const add_description_form = document.getElementById('add_description');
const add_description_button = document.getElementById('button_description_add');

const verifyComment=(e)=> {
    e.preventDefault();
   const id_error = document.getElementById('error_descripcion');
   const value = document.getElementById('descripcion_contenido').value;

    if(value.trim() === '') {
        id_error.style.display= 'block'
        id_error.textContent='Debe ingresar contenido'
    } else  {

        if(value.trim().length > 100 ) {
            id_error.style.display= 'block';
            id_error.textContent = 'Pasaste el limite de caracteres'
        } else  {
            id_error.style.display='none'
            add_description_form.submit()
        }
       
    }
}


add_description_button.addEventListener('submit', (e)=> verifyComment(e))



const btn_edit_description = document.getElementById('button_edit_description')

const edit_description = ()=> {
    const description = document.getElementById('description_container');
    const container_edit_description = document.getElementById("container_update_desc");


    description.classList.add('hidden');
    container_edit_description.classList.remove('hidden');
    

}
btn_edit_description.addEventListener("click", edit_description)













// const update_description_form = document.getElementById('update_description')



// update_description_form.addEventListener("submit", (e)=> verifyComment(e))