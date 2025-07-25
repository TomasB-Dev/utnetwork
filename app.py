from flask import Flask, render_template
from src.models.Usuarios import Usuarios
import os
from src.models.Publicaciones import Publicaciones
from src.models.Data_Base import DataBase
from dotenv import load_dotenv
from src.routes.login_routes import login_route
from src.routes.register_route import register_route
from src.routes.validation_routes import validation_route
from src.routes.loged_routes import logued_route, socket_events
from src.routes.nologed_routes import nologued_view
from flask_socketio import SocketIO

load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PORT = os.getenv('PORT')

db_user = DataBase(HOST, USER, DB_KEY, DB_NAME,PORT)
usuarios = Usuarios()
publicaciones =  Publicaciones()

app = Flask(__name__)

FIRMA = os.getenv('FIRMA')  # firmar la cokiee
app.secret_key = FIRMA

socketio = SocketIO(app)

#modularizacion vista que no necesitan loguear
nologued_view(app, usuarios)

#modularizacion login
login_route(app)

#modularizacion register
register_route(app)

#modularizacion vaidations
validation_route(app,usuarios,db_user)

#modularizacion loged views
logued_route(app,usuarios, publicaciones,db_user)

#manejo de error 404
@app.errorhandler(404)
def page_error(error):
    return render_template('error.html'), 404


if __name__ == "__main__":
    socket_events(socketio, usuarios)
    socketio.run(app, debug=True)
