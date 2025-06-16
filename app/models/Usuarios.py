from app.models.Data_Base import DataBase
from dotenv import load_dotenv
import os
import datetime

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
        if resultado is not None:
            return resultado
        else:
            return None
        
    
    def get_state_by_id(self,user_id):
        self.db_user.conectar()
        resultado = self.db_user.consulta(
            "SELECT state FROM usuarios WHERE id = %s", (user_id)
        )
        
        state = resultado[0]['state']
        self.db_user.cerrar()
        return state
    

    def publicar(self, user_id, contenido):
        fecha = datetime.datetime.now()
        self.db_user.conectar()
        self.db_user.consulta(
            "INSERT INTO publicaciones (id_user,fecha,contenido) VALUES (%s,%s,%s)",(user_id,fecha,contenido)
        )
        self.db_user.cerrar()
    
    def ver_publicaciones(self,user_id):
        self.db_user.conectar()
        publicaciones = self.db_user.consulta(
            "SELECT * FROM publicaciones" #aca va filtrado por amigos pero no hicimos esa parte todavia
        )
        self.db_user.cerrar()
        return publicaciones
    #metodo traer publicaciones de amigos
    
    
