from flask import Flask, render_template, url_for, request,  redirect, jsonify, session
from app.models.Usuarios import Usuarios
import os
from app.models.Data_Base import DataBase
from dotenv import load_dotenv
from app.routes.login_routes import login_route
from app.routes.register_route import register_route
from app.routes.validation_routes import validation_route

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
#modularizacion login
login_route(app)
#modularizacion register
register_route(app)
#modularizacion vaidations
validation_route(app,usuarios,db_user)


@app.route('/terminos')
def terminos():
    return render_template('terminos.html')


@app.route('/home')
def home():
    token = session.get('usuario')
    if session:
        id_user = token[0]['id']
        info_user = usuarios.get_data_by_id(id_user)
        user_state = usuarios.get_state_by_id(id_user)
        if user_state == True:
            return render_template('home.html', usuario=info_user[0])
        else:
            return redirect(url_for('validation'))
    else:
        return render_template('error.html')


@app.errorhandler(404)
def page_error(error):
    return render_template('error.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
