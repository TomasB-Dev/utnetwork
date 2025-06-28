from src.models.Data_Base import DataBase
from dotenv import load_dotenv
import os
from src.utils.Error_Saver import save_error
from datetime import datetime

class Usuarios:
    def __init__(self):
        load_dotenv()
        DB_NAME = os.getenv('DB_NAME')
        DB_KEY = os.getenv('DB_KEY')
        HOST = os.getenv('HOST')
        USER = os.getenv('USER')
        PORT = os.getenv('PORT')

        self.db_user = DataBase(HOST, USER, DB_KEY, DB_NAME,PORT)    


    def eliminar_descripcion(self, user_id):
        try:
            self.db_user.conectar()
            self.db_user.consulta(
                """
                UPDATE usuarios
                SET descripcion = ''
                WHERE id = %s;
                
                
                """, (user_id)
                
            )
            self.db_user.cerrar()
        except Exception as e :
            save_error(e)
            return False
        # end try

    def actualizar_descripcion(self, user_id, nueva_descripcion):
        try:
            self.db_user.conectar()
            resutado = self.db_user.consulta(
                """
                UPDATE usuarios
                SET descripcion = %s
                
                WHERE id = %s
                
                """, (nueva_descripcion, user_id)
            )
            self.db_user.cerrar()
            return resutado
        except Exception as e:
            save_error(e)
            return False

    def get_data_by_id(self, user_id):
        """
        Obtiene la data del user_id
        """
        try:
            self.db_user.conectar()
            resultado = self.db_user.consulta(
                "SELECT id, nombre, mail,state,avatar,confirmed,descripcion  FROM usuarios WHERE id = %s", (user_id,)
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
    def actualizar_conexion(self,user_id):
        """
        Actuliza la ultima conexion
        """
        actual = datetime.now()
        self.db_user.conectar()
        self.db_user.consulta(
            "UPDATE usuarios SET ultima_conexion = %s WHERE id = %s",(actual,user_id)
        )
        self.db_user.cerrar()


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
    def obtener_informacion_seguidos(self,user_id):
        """
        obtiene informacion de los seguidos
        """
        self.db_user.conectar()
        informacion = self.db_user.consulta (
            """
            SELECT usuarios.id, usuarios.nombre, usuarios.avatar
            FROM usuarios
            INNER JOIN seguidores ON usuarios.id = seguidores.seguido_id
            WHERE seguidores.id_user = %s;
            """,(user_id)
        )
        self.db_user.cerrar()
        return informacion
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
                'SELECT COUNT(seguido_id) FROM seguidores WHERE seguido_id = %s',(user_id)
            )
            self.db_user
            ultima_conexion = self.db_user.consulta(
                "SELECT ultima_conexion FROM usuarios WHERE id = %s",(user_id)
            )
            self.db_user.cerrar()
            dia_actual = datetime.now()
            diferencia = dia_actual - ultima_conexion[0]['ultima_conexion']
            dias = diferencia.days
            horas= diferencia.total_seconds() / 3600
            minutos = diferencia.total_seconds() / 60
            segundos =  diferencia.total_seconds()
            stats['cant_publi'] = cantidad_publi[0]['COUNT(id_publicacion)']
            stats['cant_seguidos'] = cantidad_segui[0]['COUNT(id_user)']
            stats['cant_seguidores'] = cantidad_followers[0]['COUNT(seguido_id)']
            stats['ultima_conexion_dias'] = round(dias)
            stats['ultima_conexion_horas'] = round(horas)
            stats['ultima_conexion_minutos'] = round(minutos)
            stats['ultima_conexion_segundos'] = round(segundos)
            return stats
        except Exception as e:
            save_error(e)

    def buscar_usuario(self,like,user_id):  
        """
        Buscar usuarios atraves de un like en sql y retorna lo encontrado
        """
        self.db_user.conectar()
        busqueda = self.db_user.consulta(
            "SELECT id,nombre, avatar FROM usuarios WHERE nombre LIKE %s AND id !=%s",
                ('%' + like + '%',user_id)
        )
        self.db_user.cerrar()
        return busqueda
    
    def guardar_mensaje(self,sender_id, recipient_id, message):
        """
        GUARDA LOS MENSAJES EN LA BASE DE DATOS
        """
        self.db_user.conectar()
        self.db_user.consulta("INSERT INTO mensajes (emisor,receptor,contenido) VALUES(%s,%s,%s)",(sender_id,recipient_id,message)
        )
        self.db_user.cerrar()
    #metodo traer publicaciones de amigos
    
    
