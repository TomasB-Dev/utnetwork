import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Send_Mail:


    def __init__(self,mail,key,destino):
        self.mail = mail
        self.key = key
        self.destinatario = destino


    def enviarMail(self,asunto,contenido):
        """
        Envia un mail al usuario en formato html
        """
        mensaje = MIMEMultipart("alternative")
        mensaje['From'] = self.mail
        mensaje['To'] = self.destinatario
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(contenido, 'html'))
        try:
            servidor = smtplib.SMTP('smtp.gmail.com', 587)
            servidor.starttls()  
            servidor.login(self.mail, self.key)
            servidor.send_message(mensaje)
            servidor.quit()
            return True
        except Exception as e:
            print(f'error al enviar el correo {e}')
            return False