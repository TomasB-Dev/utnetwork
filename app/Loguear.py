import hashlib
import secrets
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


        print(f"usuario: {self.key}, mail: {self.mail}")

    def __hashear(self):
        self.key = hashlib.sha256(self.key.encode()).hexdigest()

    def __generarToken(self):
        token = secrets.token_bytes(16)  
        token_hex = token.hex() 
        db_user.conectar()
        db_user.consulta(
            "UPDATE usuarios SET token = %s WHERE mail = %s",(token_hex,self.mail)
        )
        token2 = hashlib.sha256(token_hex.encode()).hexdigest()
        return  {"token": token2}
    
    def loguear(self):
        self.__hashear()
        db_user.conectar()
        resultados = db_user.consulta(
            "SELECT * FROM usuarios WHERE mail = %s AND contrasena = %s", (self.mail, self.key))
        db_user.cerrar()
        
        print("resultads", resultados)
        if len(resultados) > 0:
            token = self.__generarToken()
            return token
        else:
            return 0
