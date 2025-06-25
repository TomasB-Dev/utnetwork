import mysql.connector
from mysql.connector import Error



class DataBase:
    def __init__(self, host, nombre, key, db):
        self.host = host
        self.nombre = nombre
        self.key = key
        self.db = db
        self.conectar()

    def conectar(self):

        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.nombre,
                password=self.key,
                database=self.db
            )
            self.cursor = self.conexion.cursor(dictionary=True)

        except Error as e:
            print(f"Error al conectar: {e}")

    def cerrar(self):
        """
        cierdda la conexion con la base de datos
        """
        if self.cursor:
            self.cursor.close()
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()

    def consulta(self, query, parametros=None, fetchone=False):
        """
        realiza consultas a la base de datos
        """

        try:
            if parametros is not None and not isinstance(parametros, tuple):
                parametros = (parametros,) # esto es para verificar sea una tupla atte:los teni diabolicos
            self.cursor.execute(query, parametros or ())
            if query.strip().lower().startswith("select"):  # aca verifico si es un select
                return self.cursor.fetchall()
            else:
                self.conexion.commit()
                return self.cursor.rowcount
        except Error as e:
            print(f"error en la consulta: {e}")
            return None
