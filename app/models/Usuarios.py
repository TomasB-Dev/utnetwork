from app.models.Data_Base import DataBase
from dotenv import load_dotenv
import os
from app.utils.Error_Saver import save_error


class Usuarios:
    def __init__(self):
        load_dotenv(dotenv_path='../.env')
        DB_NAME = os.getenv('DB_NAME')
        DB_KEY = os.getenv('DB_KEY')
        HOST = os.getenv('HOST')
        USER = os.getenv('USER')
        self.db_user = DataBase(HOST, USER, DB_KEY, DB_NAME)    

    def get_data_by_id(self, user_id):
        """
        Obtiene la data del user_id
        """
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
        """
        Recomienda 5 usuarios aletorios que el user_id no siga
        """
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                """
                SELECT u.*
                FROM usuarios u
                WHERE u.id != %s
                AND u.id NOT IN (
                    SELECT seguido_id FROM seguidores WHERE id_user = %s
                )
                ORDER BY RAND()
                LIMIT 5
            """, (user_id, user_id))#trae usuarios random que no seguis
                        
            self.db_user.cerrar()
            resultado = resultado or []
            return resultado
        except Exception as e :
            save_error(e)
            return False
    
    def get_state_by_id(self,user_id):
        """
        Obtiene el estado de la cuenta user_id (confirmada o no)
        """
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
        """
        El user_id sigue a follow_id
        """
        try:
            self.db_user.conectar()
            self.db_user.consulta(
                "INSERT INTO seguidores (id_user, seguido_id) VALUES (%s, %s)", (user_id, follow_id)
            )
            self.db_user.cerrar()
            return True
        except Exception as e:
            save_error(e)
            return False
    
    def dejar_de_seguir_usuario(self, user_id, follow_id):
        """
        Deja de seguir a el usuario follow_id
        """
        try:
            self.db_user.conectar()
            self.db_user.consulta(
                "DELETE FROM seguidores WHERE id_user = %s AND seguido_id = %s", (user_id, follow_id)
            )
            self.db_user.cerrar()
            return True
        except Exception as e :
            save_error(e)
            return False
    
    def obtener_seguidores(self, user_id):
        """
        Obtiene los usuarios que siguen a user_id
        """
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                "SELECT seguido_id FROM seguidores WHERE id_user = %s", (user_id,)
            )
            self.db_user.cerrar()
            resultado_final = [row['seguido_id'] for row in resultado]
            return resultado_final
        except Exception as e :
            save_error(e)
            return False
    
    def obtener_seguidos(self, user_id):
        """
        Obtiene los usuarios seguidos por el user_id
        """
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                'SELECT id_user FROM seguidores WHERE seguido_id = %s', (user_id,)
            )
            resultado_final = [row['id_user'] for row in resultado]
            self.db_user.cerrar()
            print(resultado_final)
            return resultado_final  
        except Exception as e :
            save_error(e)
            return False    
    
    def obtener_estadisticas(self,user_id):
        """
        Obtiene estadisticas del usuario en base a distintas consultas y las retorna
        """
        stats = {}
        try:
            self.db_user.conectar()
            cantidad_publi = self.db_user.consulta(
                "SELECT COUNT(id_publicacion) FROM publicaciones WHERE id_user = %s",(user_id)
            )
            cantidad_segui = self.db_user.consulta(
            'SELECT COUNT(id_user) FROM seguidores WHERE id_user = %s',(user_id)
            )
            cantidad_followers = self.db_user.consulta(
                'SELECT COUNT(seguido_id) FROM seguidores WHERE id_user = %s',(user_id)
            )
            self.db_user
            stats['cant_publi'] = cantidad_publi[0]['COUNT(id_publicacion)']
            stats['cant_seguidos'] = cantidad_segui[0]['COUNT(id_user)']
            stats['cant_seguidores'] = cantidad_followers[0]['COUNT(seguido_id)']
            return stats
        except Exception as e:
            save_error(e)

    def buscar_usuario(self,like):
        """
        Buscar usuarios atraves de un like en sql y retorna lo encontrado
        """
        self.db_user.conectar()
        busqueda = self.db_user.consulta(
            "SELECT id,nombre, avatar FROM usuarios WHERE nombre LIKE %s",
                ('%' + like + '%',)
        )
        self.db_user.cerrar()
        return busqueda

    #metodo traer publicaciones de amigos
    
    
