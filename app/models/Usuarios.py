from app.models.Data_Base import DataBase
from dotenv import load_dotenv
import os
from app.utils.Error_Saver import save_error
import datetime
import mysql.connector

class Usuarios:
    def __init__(self):
        load_dotenv(dotenv_path='../.env')
        DB_NAME = os.getenv('DB_NAME')
        DB_KEY = os.getenv('DB_KEY')
        HOST = os.getenv('HOST')
        USER = os.getenv('USER')
        self.db_user = DataBase(HOST, USER, DB_KEY, DB_NAME)    

    def get_data_by_id(self, user_id):
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                "SELECT *  FROM usuarios WHERE id = %s", (user_id,)
            )
            
        
        
        
            self.db_user.cerrar()
            if resultado is not None:
                return resultado
            else:
                return None
        except Exception as e :
            save_error(e)
            return False
            
        
    def suggest_users(self, user_id):
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                "SELECT * FROM usuarios WHERE id != %s ORDER BY RAND() LIMIT 5", (user_id,)
            )
            self.db_user.cerrar()
            return resultado
        except Exception as e :
            save_error(e)
            return False
    
    def get_state_by_id(self,user_id):
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                "SELECT state FROM usuarios WHERE id = %s", (user_id)
            )
            
            state = resultado[0]['state']
            self.db_user.cerrar()
            return state
        except Exception as e :
            save_error(e)
            return False
    

    
    def seguir_usuario (self, user_id, follow_id):
        try:
            self.db_user.conectar()
            self.db_user.consulta(
                "INSERT INTO seguidores (id_user, id_follow) VALUES (%s, %s)", (user_id, follow_id)
            )
            self.db_user.cerrar()
            return True
        except Exception as e :
            save_error(e)
            return False
    
    def dejar_de_seguir_usuario(self, user_id, follow_id):
        try:
            self.db_user.conectar()
            self.db_user.consulta(
                "DELETE FROM seguidores WHERE id_user = %s AND id_follow = %s", (user_id, follow_id)
            )
            self.db_user.cerrar()
            return True
        except Exception as e :
            save_error(e)
            return False
    
    def obtener_seguidores(self, user_id):
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                "SELECT id_follow FROM seguidores WHERE id_user = %s", (user_id,)
            )
            self.db_user.cerrar()
            resultado_final = [row['id_follow'] for row in resultado]
            return resultado_final
        except Exception as e :
            save_error(e)
            return False
    
    def obtener_seguidos(self, user_id):
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                'SELECT id_user FROM seguidores WHERE id_follow = %s', (user_id,)
            )
            resultado_final = [row['id_user'] for row in resultado]
            self.db_user.cerrar()
            return resultado_final  
        except Exception as e :
            save_error(e)
            return False    
    
    #metodo traer publicaciones de amigos
    
    
