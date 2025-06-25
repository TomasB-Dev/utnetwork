from flask import Flask, render_template
from app.models.Usuarios import Usuarios
import os
from app.models.Publicaciones import Publicaciones
from app.models.Data_Base import DataBase
from dotenv import load_dotenv
from app.routes.login_routes import login_route
from app.routes.register_route import register_route
from app.routes.validation_routes import validation_route
from app.routes.loged_routes import logued_route
from app.routes.nologed_routes import nologued_view

#load_dotenv(dotenv_path='../.env')
DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PORT = os.getenv('port')
db_user = DataBase(HOST, USER, DB_KEY, DB_NAME,PORT)
usuarios = Usuarios()
publicaciones =  Publicaciones()

app = Flask(__name__)

FIRMA = os.getenv('FIRMA')  # firmar la cokiee
app.secret_key = FIRMA

#modularizacion vista que no necesitan loguear
nologued_view(app)

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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
