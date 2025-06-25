from src.models.Data_Base import DataBase
from dotenv import load_dotenv
import datetime
import os
load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
PORT = os.getenv('PORT')
db_user = DataBase(HOST, USER, DB_KEY, DB_NAME,PORT)

def save_error(contenido):
    fecha = datetime.datetime.now()
    db_user.conectar()
    db_user.consulta(
        "INSERT INTO errores(fecha,contenido) VALUES (%s,%s)",(fecha,contenido)
    )
    db_user.cerrar()