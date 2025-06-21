const publicar = (e) => {
    e.preventDefault();
    const value = document.getElementById('input_publish').value;
    if (value.trim() === '') {
        alert('El campo de publicación no puede estar vacío.');
        return;
    }


  


    fetch('http://127.0.0.1:5000/app/publicar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ contenido: value }),
        

    }).then(res => res.json())
    .then(respuesta => {
        if (respuesta.correcto) {
            alert('Publicación exitosa');
            console.log('Publicación exitosa:', respuesta);
            document.getElementById('input_publish').value = ''; // Limpiar el campo de entrada
        } else {
            alert('Error al publicar: ' + respuesta.error);
        }
    })
}

   



const form_update_text = document.getElementById('form_update_text');


// form_update_text.addEventListener


const verify_form_update_post = (e)=> {
    const value = document.getElementById('contenido').value.trim();
    const error_update_post = document.getElementById('error_update_post')
    if(!value) {
        e.preventDefault();
        error_update_post.style.display='block';
        error_update_post.textContent='Debe agregar un texto'
    } else {
        error_update_post.style.display='none'
    }
}





form_update_text.addEventListener('submit', verify_form_update_post)

const activateUpdate =(button)=> {
    const container = button.closest('.publish_card');
    // const button_save_post = document.getElementById('button_save_post');

    // if (text == '') {
    //     button_save_post.disabled = true
    // }

    
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