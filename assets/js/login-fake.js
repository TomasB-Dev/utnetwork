document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const email = document.getElementById('mail').value.trim();
    const password = document.getElementById('key').value.trim();
    const mensaje = document.getElementById('login-msg');

    if (email && password) {
        mensaje.style.color = 'green';
        mensaje.textContent = 'Logeadp';
        
    
    } else {
        mensaje.style.color = 'red';
        mensaje.textContent = 'Completa todos los campos.';
    }
});