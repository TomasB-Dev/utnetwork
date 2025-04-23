function changue_BG() {
    let modo = localStorage.getItem('modo');
    let fondo = document.getElementById('body');
    let btn = document.getElementById('swap-btn');
    let txt = document.getElementsByClassName('txt');
    cant_textos = formulario.length
    if (modo != 'oscuro') {
        btn.style.backgroundColor = '#282828';
        fondo.style.background = 'white';   
        localStorage.setItem("modo", "oscuro"); 
        btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M21 12.79A9 9 0 0111.21 3a7 7 0 100 14A9 9 0 0021 12.79z" fill="currentColor"/></svg>';
        btn.style.color = 'white'

        for (let i = 0; i <cant_textos; i++) {
            txt[i].style.color = 'red';
            
        }
    }else{
        btn.style.backgroundColor = 'white';
        btn.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" fill="currentColor"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>';
        btn.style.color = "#282828"
        fondo.style.background = '#282828';   
        for (let i = 0; i <cant_textos; i++) {
            txt[i].style.color = 'blue';
            
        }
        localStorage.setItem("modo", "claro"); 
    }


}