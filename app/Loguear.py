import hashlib
from app.Data_Base import DataBase
from dotenv import load_dotenv
import os
import random
from app.Mail_Send import Send_Mail
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
    def confirmed_mail(self):
        """
        Si el mail no esta confirmado envia el mail

        """
        db_user.conectar()
        status = db_user.consulta(
            "SELECT status FROM usuarios WHERE mail = %s",(self.mail)
        )
        db_user.cerrar()
        if status == True:
            pass
        else:
            codigo = ''
            for i in range(6):
                codigo += str(random.randrange(0,9,1))
            db_user.conectar()
            db_user.consulta(
                "UPDATE usuarios SET confirmed = %s WHERE mail = %s",(codigo,self.mail)
            )
            db_user.cerrar()
            MAIL = os.getenv('MAIL')
            MAIL_KEY = os.getenv('MAIL_KEY')
            avisar = Send_Mail(MAIL, MAIL_KEY, self.mail)
            contenido = f"""
<html>
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; margin: 0;">
    <table width="100%" cellpadding="0" cellspacing="0" style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
        <tr>
            <td style="padding: 30px; text-align: center;">
                <h1 style="color: #2c3e50; margin-bottom: 10px;">Tu código de verificación 🔐</h1>
                <p style="color: #555555; font-size: 16px; line-height: 1.6;">
                    Utilizá el siguiente código para verificar tu cuenta en <strong>UTNetwork</strong>:
                </p>
                <p style="font-size: 32px; font-weight: bold; color: #0066cc; margin: 30px 0;">
                    {codigo}
                </p>
                <p style="color: #555555; font-size: 16px; line-height: 1.6;">
                    Este código es válido por tiempo limitado. Si no solicitaste este código, podés ignorar este mensaje.
                </p>
                <hr style="margin: 40px 0; border: none; border-top: 1px solid #eeeeee;">
                <p style="font-size: 13px; color: #999999;">
                    UTNetwork - Conectando la comunidad tecnológica.
                </p>
            </td>
        </tr>
    </table>
</body>
</html>
"""
            avisar.enviarMail('Bienvenido a UTNetwork', contenido)

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
            if resultados[0]['state'] == 1:
                return True
            else:
                self.confirmed_mail()
                return '0'  # retorno 0 para saber que no esta verificada
        else:
            return False
