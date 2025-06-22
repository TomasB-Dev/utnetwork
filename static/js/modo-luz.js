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
const page_calling = document.location.pathname.split("/").pop() /* muchachos esta la usamos para saber que archivo html esta calleando el script */
switch (page_calling) {
    case 'login.html':
        if (modo == 'claro'){
            btn.style.backgroundColor = '#282828';
                fondo.style.background = '#f8f8ff';   
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
        break;
    case 'register.html':
        if (modo == 'claro'){
            btn.style.backgroundColor = '#282828';
                fondo.style.background = '#f8f8ff';   
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
        break;
    case 'index.html':
        if (modo == 'claro'){
                btn.style.backgroundColor = '#282828';
                fondo.style.background = '#f8f8ff'; 
                btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 12.79A9 9 0 0111.21 3a7 7 0 100 14A9 9 0 0021 12.79z" fill="currentColor"/></svg>';
                btn.style.color = 'white';
                fondo.style.color = "black"
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
    case 'home.html':
        if (modo == 'claro'){
            btn.style.backgroundColor = '#282828';
                fondo.style.background = '#f8f8ff'; 
                btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 12.79A9 9 0 0111.21 3a7 7 0 100 14A9 9 0 0021 12.79z" fill="currentColor"/></svg>';
                btn.style.color = 'white';
                fondo.style.color = "black"
                for(const element of txt) { 
            
                    element.style.color = 'black';
                }
        }else{
            btn.style.backgroundColor = 'white';
            btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" fill="currentColor"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
            btn.style.color = "#282828"
            fondo.style.background = '##212121';
            for(const element of txt) {
                element.style.color = 'white';
            }
            
        }
        
    default:
        break;
}


function changue_BG() {
    /* lo tuve que traer localmente para que funcionara el cambio cada vez que se ejecutaba la funcion, en caso de no hacerlo no cambiaba el valor de modo*/
    let modo_local = localStorage.getItem('modo');
    if (modo_local != 'claro') {
        try {
            btn.style.backgroundColor = '#282828';
            fondo.style.background = '#f8f8ff';   
            localStorage.setItem("modo", "claro"); 
            btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 12.79A9 9 0 0111.21 3a7 7 0 100 14A9 9 0 0021 12.79z" fill="currentColor"/></svg>';
            btn.style.color = 'white';
            for(const element of txt) {
                element.style.color = 'black';
            }
            } catch (error) {
                console.log(error)
            }       
    }else{
        try {
            btn.style.backgroundColor = 'white';
            btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" fill="currentColor"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
            btn.style.color = "#212121"
            fondo.style.background = '#212121';   
            localStorage.setItem("modo", "oscuro");
            for(const element of txt) { 
            
                element.style.color = 'white';
            }
        } catch (error) {
            console.log(error)
        }
        
    }
}
