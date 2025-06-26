// const publicar = (e) => {
//     e.preventDefault();
//     const value = document.getElementById('input_publish').value;
//     if (value.trim() === '') {
//         alert('El campo de publicación no puede estar vacío.');
//         return;
//     }


  


//     fetch('http://127.0.0.1:5000/app/publicar', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify({ contenido: value }),
        

//     }).then(res => res.json())
//     .then(respuesta => {
//         if (respuesta.correcto) {
//             alert('Publicación exitosa');
//             console.log('Publicación exitosa:', respuesta);
//             document.getElementById('input_publish').value = ''; // Limpiar el campo de entrada
//         } else {
//             alert('Error al publicar: ' + respuesta.error);
//         }
//     })
// }

   



const form_update_text = document.getElementById('form_update_text');
const form_post_publication = document.getElementById('form_new_post');



const verifyPost = (e, id_input, id_error)=> {
    const value = document.getElementById(id_input).value;
    const error_message = document.getElementById(id_error);

    if(value.trim() ==='') {
        e.preventDefault();
        error_message.style.display='block';
        error_message.textContent='Debe agregar un texto'
    } else {
        error_message.style.display='none'
    }

}


form_update_text.addEventListener('submit', (e)=> verifyPost(e,'contenido', 'error_update_post'))
form_post_publication.addEventListener('submit', (e)=> verifyPost(e,'input_publish', 'error_new_post'))


const activateUpdate =(button)=> {
    const container = button.closest('.publish_card');
    
    
     if (!container) {
        console.error('No se encontró el contenedor .container_text');
        return;
    }

    const view = container.querySelector('.view_publication');
    const edit = container.querySelector('.edit_publication');


    view.style.display = 'none';
    edit.style.display = 'block'

}




const cancelUpdate =(button)=> {
    event.preventDefault?.();

    const container = button.closest('.publish_card');
    

    const view = container.querySelector('.view_publication');
    const edit = container.querySelector('.edit_publication');


    view.style.display = 'block';
    edit.style.display = 'none'

}