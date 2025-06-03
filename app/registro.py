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


    def __existe(self):
        """
        revisa si el mail ya fue registrado y devuelve true o false
        si el mail no esta registrado devuelve false, en caso contrario true

        """
        db_user.conectar()

        check_mail = []
        check_mail = db_user.consulta(
            f"SELECT mail FROM usuarios WHERE mail = '{self.mail}'"
        )
        db_user.cerrar()
        
        if len(check_mail) < 1:
            return False
        else:
            return True


    def registrar(self):
        """
        carga los datos  a la base de datos
        """
        existe = self.__existe()
        if existe:
            print('el mail ya esta registrado')
            return False
        else:
            self.__hashear()
            if self.key:
                try:
                    db_user.conectar()
                    db_user.consulta(
                        "INSERT INTO usuarios (nombre, mail,contrasena) VALUES (%s, %s,%s)", (self.nombre, self.mail, self.key))
                    db_user.cerrar()
                    # Manejar errores en caso de
                    print('Registro')
                    return True
                except Error as e:
                    print(f'El error es: {e}')
                    return False
            else:
                print('no registrado')
                return False

    def __str__(self):
        return f'nombre: {self.nombre} mail: {self.mail} key:{self.key}'
