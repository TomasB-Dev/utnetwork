from flask import Flask, render_template, url_for, request,  redirect, jsonify, session
from app.registro import Registro
from app.Loguear import Login
from app.datosUsuario import get_user_dataId
import time
import os
from app.Data_Base import DataBase
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
db_user = DataBase(HOST, USER, DB_KEY, DB_NAME)

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
    else:
        return render_template('error.html')


@app.route('/home')
def home():
    token = session.get('usuario')
    if token:
        print(token)
        user_data = get_user_dataId(token[0]['id'])

        db_user.conectar()
        resultado = db_user.consulta(
        "SELECT state FROM usuarios WHERE id = %s AND state  IS NOT NULL", (token[0]['id'])
        )
    
        db_user.cerrar()
        # statado = get_user_dataId(token[4]['state'])
        print(resultado)
        return render_template('home.html', usuario=user_data[0])
    else:
        return render_template('error.html')


@app.route('/validar')
def validation():
    if session:
        return render_template('/temporales/confirm_mail.html')
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


@app.errorhandler(404)
def page_error(error):
    return render_template('error.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
