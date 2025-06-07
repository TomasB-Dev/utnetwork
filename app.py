from flask import Flask, render_template, url_for, request,  redirect, jsonify,session
from app.registro import Registro
from app.Loguear import Login
import time
import os

app = Flask(__name__)

FIRMA = os.getenv('FIRMA')  # firmar la cokiee
app.secret_key = FIRMA


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/terminos')
def terminos():
    return render_template('terminos.html')


@app.route('/app/registrar', methods=['POST'])
def registrar():

    
    username = request.form['name']
    key = request.form['password']
    mail = request.form['email']
    usuario = Registro(username, mail, key)
    registro = usuario.registrar()
    time.sleep(1)  # momentaneo, hablar con agus para ver que opina
    # aca agregar la confirmacion por el mail
    if registro == True:
        return redirect(url_for('login'))

@app.route('/home')
def home():
    token = session.get('usuario')
    if session:
        return render_template('home.html', token=token)
    else:
        return render_template('error.html')
    

    

@app.route('/app/Loguear', methods=['POST'])
def log():
    key = request.form['password']
    mail = request.form['mail']
    user = Login(mail, key)
    check = user.loguear()
    if check == False:
        session.clear()
        return redirect(url_for('login'))
    else:
        session['usuario'] = user.get_id()
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
    