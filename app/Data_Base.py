import mysql.connector
from mysql.connector import Error


class DataBase:
    def __init__(self, host, nombre, key, db):
        self.host = host
        self.nombre = nombre
        self.key = key
        self.db = db

    def conectar(self):
        """
        establece la conexion con la base de datos
        """
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.nombre,
                password=self.key,
                database=self.db
            )
            self.cursor = self.conexion.cursor(dictionary=True)
        except Error as e:
            print(f"error al conectar: {e}")

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
            self.cursor.execute(query, parametros or ())
            if query.strip().lower().startswith("select"):  # aca verifico si es un select
                return self.cursor.fetchall()
            else:
                self.conexion.commit()
                return self.cursor.rowcount
        except Error as e:
            print(f"error en la consulta: {e}")
            return None
