from flask import Flask, render_template, url_for, request,  redirect, jsonify, session
from app.registro import Registro
from app.Loguear import Login
from app.Usuarios import Usuarios
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

usuarios = Usuarios()




app = Flask(__name__)

FIRMA = os.getenv('FIRMA')  # firmar la cokiee
app.secret_key = FIRMA


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    if session:
        return redirect(url_for('home'))
    else:
        return render_template('login.html')


@app.route('/register')
def register():
    if session:
        return redirect(url_for('home'))
    else:
        return render_template('register.html')


@app.route('/terminos')
def terminos():
    return render_template('terminos.html')


@app.route('/validar-codigo', methods=['POST'])
def validar_codigo():
    
    if session:
        id = session.get('usuario')
        user_id = id[0]['id']   
        state = usuarios.get_state_by_id(user_id)
        #chekea el estado de la cuenta, si la cuenta no es confirmada permite validar no es realmente necesario pero es otra capa de seguridad ?
        if state == False :
            id_session = session['usuario']
            data = request.get_json()
            #obtengo la data de los inputs y los concateno
            codigo = data.get('c1', '') + data.get('c2', '') + data.get('c3', '') + \
                    data.get('c4', '') + data.get('c5', '') + data.get('c6', '') #el segundo parametro es lo que devuelve si esta vacio

            db_user.conectar()
            codigo_correcto  = db_user.consulta(
                'SELECT confirmed FROM usuarios WHERE id = %s',(id_session[0]['id'])
            )
            db_user.cerrar()
            #check si los codigos coinciden, si coinciden cambia el status y el usuario no podria ver mas validar.
            if codigo == codigo_correcto[0]['confirmed']:
                db_user.conectar()
                db_user.consulta(
                    "UPDATE usuarios SET state = %s WHERE id = %s",(True, id_session[0]['id'])
                )
                return jsonify({'correcto': True, 'redirect_url': url_for('home')}) #para redireccionar al home
            else:
                return jsonify({'correcto': False})
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

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


@app.route('/home')
def home():
    token = session.get('usuario')
    if session:
        id_user = token[0]['id']
        user_data = usuarios.get_data_by_id(id_user)
        state = user_data[0]['state']
        return render_template('home.html', usuario=user_data[0])
    else:
        return render_template('error.html')


@app.route('/validar')
def validation():

    if session:
            id = session.get('usuario')
            user_id = id[0]['id']
    
            state = usuarios.get_state_by_id(user_id)
            if state == True:
                return redirect(url_for('home'))
            else:
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
