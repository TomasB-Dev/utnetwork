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