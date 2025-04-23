const MODO_FINAL = localStorage.getItem('modo')
const modo = localStorage.getItem('modo');
const fondo = document.getElementById('body');
const btn = document.getElementById('swap-btn');
const txt = document.getElementsByClassName('txt');
/*
esto mantiene el modo atraves de paginas
claramente queda implimentar para el color y los textos queden bien
una de las soluciones que proponga es a todos los textos le pongan la clase txt y que los divs sean transparente asi solo 
cambia el color del body
el resto de cosas que cambia es el boton para la luna y el sol que lo pueden robar de login
*/
if (modo == 'claro'){
    btn.style.backgroundColor = '#282828';
        fondo.style.background = '#f8f8ff';   
        localStorage.setItem("modo", "claro"); 
        btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 12.79A9 9 0 0111.21 3a7 7 0 100 14A9 9 0 0021 12.79z" fill="currentColor"/></svg>';
        btn.style.color = 'white';
        for(const element of txt) {
            element.style.color = 'black';
        }
}else{
    btn.style.backgroundColor = 'white';
    btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" fill="currentColor"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
    btn.style.color = "#282828"
    fondo.style.background = '#282828';   
    for(const element of txt) { 
        element.style.color = 'white';
    }
}
/* Lo de arriba tiene un problema y es que queda 'pegado' el modo, una vez presionado no se puede cambiar si alguien lo fixea antes de que lo solucione avise <3 */



function changue_BG() {
    cant_textos = formulario.length;
    if (modo != 'claro') {
        btn.style.backgroundColor = '#282828';
        fondo.style.background = '#f8f8ff';   
        localStorage.setItem("modo", "claro"); 
        btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 12.79A9 9 0 0111.21 3a7 7 0 100 14A9 9 0 0021 12.79z" fill="currentColor"/></svg>';
        btn.style.color = 'white';
        for(const element of txt) {
            element.style.color = 'black';
        }
    }else{
        btn.style.backgroundColor = 'white';
        btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" fill="currentColor"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
        btn.style.color = "#282828"
        fondo.style.background = '#282828';   
        for(const element of txt) { 
            element.style.color = 'white';
        }
        localStorage.setItem("modo", "oscuro"); 
    }
}