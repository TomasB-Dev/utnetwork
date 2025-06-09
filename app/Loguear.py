import hashlib
from app.Data_Base import DataBase
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='../.env')
DB_NAME = os.getenv('DB_NAME')
DB_KEY = os.getenv('DB_KEY')
HOST = os.getenv('HOST')
USER = os.getenv('USER')
db_user = DataBase(HOST, USER, DB_KEY, DB_NAME)


class Login:
    def __init__(self, mail, key):
        self.mail = mail
        self.key = key

    def __hashear(self):
        """
        Hashea la contraseña
        """
        self.key = hashlib.sha256(self.key.encode()).hexdigest()

    def get_id(self):
        """
        Retorna el id del usuario
        """
        db_user.conectar()
        resultados = db_user.consulta(
            "SELECT id FROM usuarios WHERE mail = %s AND contrasena = %s", (self.mail, self.key))
        db_user.cerrar()
        return resultados

    def loguear(self):
        """
        Loguea el usuario, hashea la contraseña y luego compara el mail y la contraseña.
        cuando el mail y la contraseña matchean revisa el estado de la cuenta
        si es 1 significa que la cuenta esta confirmada y devuelve True, si no esta confirmada
        devuelve '0'.en caso de que no matchee devuelve False
        """
        self.__hashear()
        db_user.conectar()
        resultados = db_user.consulta(
            "SELECT * FROM usuarios WHERE mail = %s AND contrasena = %s", (self.mail, self.key))
        db_user.cerrar()
        if len(resultados) > 0:
            print('entro primer if')
            print(resultados[0]['state'])
            if resultados[0]['state'] == 1:
                return True
            else:
                return '0'  # retorno 0 para saber que no esta verificada
        else:
            return False
