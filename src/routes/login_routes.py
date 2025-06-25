"""
CONTIENE LAS RUTAS DE LOGIN DEL USUARIO
"""
from flask import render_template, url_for, request,  redirect, session
from src.models.Loguear import Login


def login_route(app):
    
    
    @app.route('/login')
    def login():
        if session:
            return redirect(url_for('home'))
        else:
            return render_template('login.html')


    @app.route('/app/Loguear', methods=['POST'])
    def log(): 
        key = request.form['password']
        mail = request.form['mail']
        user = Login(mail, key)
        check = user.loguear()
        if check == False:
            session.clear()   
            return render_template('login.html', incorrect_credential=True)
        elif check == '0':
            session['usuario'] = user.get_id()
            return redirect(url_for('validation'))
        else:
            session['usuario'] = user.get_id()
            return redirect(url_for('home'))
    

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))