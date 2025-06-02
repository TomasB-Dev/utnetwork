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


class Registro:
    def __init__(self, nombre, mail, key):
        self.nombre = nombre
        self.mail = mail
        self.key = key

    def __hashear(self):  # podria incluir esta en registrar directamente pero prefiero manejarlo de manera separada
        """
        Hashea la contraseña
        """
        self.key = hashlib.sha256(self.key.encode()).hexdigest(
        )  # se supone que flask viene con una funcion para hacer esto piola

    def registrar(self):
        """
        carga los datos hasheados a la base de datos
        """
        self.__hashear()
        if self.key:
            print('Registrado')
            db_user.conectar()
            db_user.consulta(
                "INSERT INTO usuarios (nombre, mail,contrasena) VALUES (%s, %s,%s)", (self.nombre, self.mail, self.key))
            db_user.cerrar()
        else:
            print('no registrado')

    def __str__(self):
        return f'nombre: {self.nombre} mail: {self.mail} key:{self.key}'
