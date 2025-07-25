"""
CONTIENE LAS RUTAS QUE NO SE NECESITA ESTAR LOGUEADO PARA VER
"""
from flask import render_template,redirect,url_for, session ,request, jsonify
from src.models.Mail_Send import Send_Mail
import random
import hashlib
import os


def nologued_view(app, usuarios):
    @app.route('/')
    def index():
        if session: 
            return redirect(url_for('home'))
        else:
            return render_template('index.html')
    
    @app.route('/terminos')
    def terminos():
        return render_template('terminos.html')
    
    
    @app.route("/recuperar_cuenta")
    def recuperar_contrasena():
        return render_template('/temporales/recovery_password.html')
        
        
    @app.route('/codigo_reestablecer' , methods=['POST'])
    def reestablecer_contra_codigo():

        user_email = request.form['mail'];
        code = ''
        for i in range(6):
            code += str(random.randrange(0,9,1))
            
            
        MAIL = os.getenv('MAIL')
        MAIL_KEY = os.getenv('MAIL_KEY')
        notify = Send_Mail(MAIL, MAIL_KEY, user_email)
        
        
        content = f"""
                <html>
                <body>
                    <p>Codigo para reestablecer contraseña: <strong>{code}</strong></p>
                </body>
                </html>
            """
        notify.enviarMail('Codigo para reestablecer contraseña', content)
        if user_email:
            session['user_email']= user_email
            session['code_email']= code
            
            return redirect(url_for("verificar_codigo_clave"))
            # return render_template('/temporales/recovery_password.html', code_email=code, user_email=user_email,message='se envio el codigo correctamente')
        else:
            return render_template('/temporales/recovery_password.html',messageError='se envio el codigo correctamente')
        
        
    @app.route('/verificar_codigo_clave')
    def verificar_codigo_clave():
        return render_template('/temporales/recovery_password_code.html')
        
        
    
    @app.route('/verificar_codigo_reestablecimiento', methods=['POST'])
    def verificar_codigo_reest():
        print('verificar_codigo_reest', request.get_json())
        data = request.get_json()
        user_email = session.get('user_email')
        code_email = session.get('code_email')

        print('user_email', user_email, 'code_email', code_email)
        
        if not data:
            return jsonify({'error': 'No se recibió JSON'}), 400


        codigo = data.get('codigo')
        print('codigo', codigo, 'code_email', code_email)
        if codigo == code_email:
            return jsonify({'success': True, 'redirect_url': url_for('cambiar_contrasena')}), 200
        else:
            return jsonify({'error': 'Codigo incorrecto'}), 400
    @app.route('/cambiar_contrasena')
    def cambiar_contrasena():
        user_email = session.get('user_email')
        if not user_email:
            return redirect(url_for('index'))
        
        return render_template('/temporales/recovery_password_new.html', user_email=user_email)
    
    @app.route('/cambiar_contrasena_reestablecimiento', methods=['POST'])
    def cambiar_contrasena_reest():
        new_password = request.form['new_password']
        user_email = session.get('user_email');

        print('new_password', new_password, 'user_email', user_email)
        new_password = hashlib.sha256(new_password.encode()).hexdigest()
        usuarios.reestablecer_contrasena(new_password, user_email)
        session.clear()
        return redirect(url_for('login'))


        