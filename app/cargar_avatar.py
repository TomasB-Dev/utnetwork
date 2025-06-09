
#ARCHIVO TEMPORAL SOLO PARA PROBAR LO DE SUBIR LOS AVATARS A LA BASE DE DATOS
from Data_Base import DataBase
from dotenv import load_dotenv
import os
import base64
load_dotenv(dotenv_path='.env')
DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
#AVATAR A SUBIR
NOMBRE_IMAGEN = 'avatar_01.jpg'
ruta_imagen = f'static/images/avatars/{NOMBRE_IMAGEN}'
nombre_archivo = os.path.basename(ruta_imagen)
db_user = DataBase(HOST, USER, DB_KEY, DB_NAME)
with open(ruta_imagen, 'rb') as f:
    contenido = f.read()
    base64_str = base64.b64encode(contenido).decode('utf-8')

db_user.conectar()
db_user.consulta("INSERT INTO avatars (nombre,categoria,imagen) VALUES(%s,%s,%s)",(NOMBRE_IMAGEN,'Legado',base64_str))
db_user.cerrar()


# CREATE TABLE avatars(
# id_avatar INT AUTO_INCREMENT PRIMARY KEY,
# nombre VARCHAR(100) NOT NULL,
# categoria VARCHAR(100) NOT NULL,
# imagen LONGTEXT NOT NULL
# );