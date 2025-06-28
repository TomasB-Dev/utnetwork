import mysql.connector
from mysql.connector import Error

class DataBase:
    def __init__(self, host, nombre, key, db, port):
        self.host = host
        self.port = port
        self.nombre = nombre
        self.key = key
        self.db = db
        self.conexion = None
        self.cursor = None

    def conectar(self):
        """
        crea una conexion a la db
        """
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.nombre,
                password=self.key,
                database=self.db
            )
            self.cursor = self.conexion.cursor(dictionary=True)

        except Error as e:
            print(f"error al conectar: {e}")
            self.conexion = None
            self.cursor = None

    def cerrar(self):
        """
        ciwrra la conexion y el cursor
        """
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            self.conexion = None

    def consulta(self, query, parametros=None, fetchone=False):
        """
        realiza consultas 
        """
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.nombre,
                password=self.key,
                database=self.db
            )
            cursor = conexion.cursor(dictionary=True)

            if parametros is not None and not isinstance(parametros, tuple):
                parametros = (parametros,)

            cursor.execute(query, parametros or ())

            if query.strip().lower().startswith("select"):
                resultado = cursor.fetchone() if fetchone else cursor.fetchall()
            else:
                conexion.commit()
                resultado = cursor.rowcount

            return resultado

        except Error as e:
            print(f"error en la consulta: {e}")
            return None
