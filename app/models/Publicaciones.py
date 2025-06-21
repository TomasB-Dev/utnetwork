from app.models.Data_Base import DataBase
from dotenv import load_dotenv
import os
import datetime



class Publicaciones:
    def __init__(self):
        load_dotenv(dotenv_path='../.env')
        DB_NAME = os.getenv('DB_NAME')
        DB_KEY = os.getenv('DB_KEY')
        HOST = os.getenv('HOST')
        USER = os.getenv('USER')
        self.db_user = DataBase(HOST, USER, DB_KEY, DB_NAME)    



    def actualizar_publicacion(self, publicacion_id,contenido_nuevo):
        fecha = datetime.datetime.now()
        self.db_user.conectar()
        resultado = self.db_user.consulta(
            """
            UPDATE publicaciones
            SET contenido = %s,
                fecha = %s
            WHERE id_publicacion = %s    

            """, (contenido_nuevo, fecha, publicacion_id)
        )
        self.db_user.cerrar()
        return resultado
        


    def publicar(self, user_id, contenido):
            fecha = datetime.datetime.now()
            self.db_user.conectar()
            resultado =self.db_user.consulta(
                "INSERT INTO publicaciones (id_user,fecha,contenido) VALUES (%s,%s,%s)",(user_id,fecha,contenido)
            )
            
            self.db_user.cerrar()
            return resultado
        
    def ver_publicaciones(self, user_id,limit=10, offset=0):
        self.db_user.conectar()
        
        publicaciones = self.db_user.consulta(
            """
            SELECT 
                usuarios.nombre, 
                usuarios.avatar, 
                publicaciones.fecha, 
                publicaciones.contenido,
                publicaciones.id_user,
                publicaciones.id_publicacion
            FROM publicaciones

            INNER JOIN usuarios ON publicaciones.id_user = usuarios.id
            WHERE publicaciones.id_user = %s
            OR publicaciones.id_user IN (
                    SELECT seguido_id 
                    FROM seguidores 
                    WHERE id_user = %s
            )
            ORDER BY publicaciones.fecha DESC
            LIMIT %s OFFSET %s
            """,
            (user_id, user_id,limit,offset) # consulta que trae la publicaciones de seguidos y las mias
        )
        self.db_user.cerrar()
        return publicaciones
    def solo_una_persona(self,id_user):
        self.db_user.conectar()
        publicaciones = self.db_user.consulta(
            'SELECT * FROM publicaciones WHERE id_user = %s',(id_user)
        )
        self.db_user.cerrar()
        return publicaciones
    #metodo traer publicaciones de amigos
    
    def eliminar_publicacion(self, publicacion_id):
        self.db_user.conectar()
        self.db_user.consulta(
            "DELETE FROM publicaciones WHERE id_publicacion = %s", (publicacion_id)
        )
        self.db_user.cerrar()
        return True
