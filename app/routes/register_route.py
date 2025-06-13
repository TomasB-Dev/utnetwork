from flask import render_template, url_for, request,  redirect, session
from app.models.registro import Registro
import time

def register_route(app):
    @app.route('/register')
    def register():
        if session:
            return redirect(url_for('home'))
        else:
            return render_template('register.html')
        
    @app.route('/app/registrar', methods=['POST'])
    def registrar():
        if session:
            return redirect(url_for('home'))
        else:
            username = request.form['name']
            key = request.form['password']
            mail = request.form['email']
            usuario = Registro(username, mail, key)
            registro = usuario.registrar()
            time.sleep(1)  # espera 1 segundo para que se consiga ver el mensaje de registro correcto
            #si el registro es correcto redirecciona al login si no envia al template de error
            if registro == True:
                return redirect(url_for('login'))
            else:
                return render_template('error.html')