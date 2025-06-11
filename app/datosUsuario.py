from app.Data_Base import DataBase
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='../.env')
DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
db_user = DataBase(HOST, USER, DB_KEY, DB_NAME)


def get_user_dataId(userId):
    db_user.conectar()
    resultado = db_user.consulta(
        "SELECT * FROM usuarios WHERE id = %s", (userId)
    )
    
    db_user.cerrar()
    print(resultado)
    return resultado

