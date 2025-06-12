from app.Data_Base import DataBase
from dotenv import load_dotenv
import os
DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
HOST = os.getenv('HOST')
USER = os.getenv('USER')


class Usuarios:
    def __init__(self):
        load_dotenv(dotenv_path='../.env')
        DB_NAME = os.getenv('DB_NAME')
        DB_KEY = os.getenv('DB_KEY')
        HOST = os.getenv('HOST')
        USER = os.getenv('USER')
        self.db_user = DataBase(HOST, USER, DB_KEY, DB_NAME)    

    def get_data_by_id(self, user_id):
        self.db_user.conectar()
        resultado = self.db_user.consulta(
            "SELECT *  FROM usuarios WHERE id = %s", (user_id,)
        )
        self.db_user.cerrar()
        return resultado
        
    
    def get_state_by_id(self,user_id):
        resultado = self.db_user.conectar(
            "SELECT s.state FROM usuarios s WHERE id = %s", (user_id)
        )
        self.db_user.cerrar()
        return resultado
    
