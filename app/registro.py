import hashlib
class Registro:
    def __init__(self,nombre,mail,key):
        self.nombre = nombre
        self.mail = mail
        self.key = key
    def __hashear(self):#podria incluir esta en registrar directamente pero prefiero manejarlo de manera separada
        """
        Hashea la contraseña
        """
        self.key  = hashlib.sha256(self.key.encode()).hexdigest() #se supone que flask viene con una funcion para hacer esto piola


    def registrar(self):
        """
        Carga los datos hasheados a la base de datos
        """
        self.__hashear()
        if self.key:
            print('Registrado')
        else:
            print('no registrado')
    def __str__(self):
        return f'nombre: {self.nombre} mail: {self.mail} key:{self.key}'
    
    