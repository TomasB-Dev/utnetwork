"""
CONTIENE LAS RUTAS DE VALIDACION DE LA CUENTA
"""
from flask import render_template, url_for, request,  redirect, jsonify , session
import random
import os
from app.models.Mail_Send import Send_Mail
import hashlib




def validation_route(app,usuarios,db_user):
    @app.route('/validar')
    def validation():

        if session:
                id = session.get('usuario')
                user_id = id[0]['id']
        
                state = usuarios.get_state_by_id(user_id)
                if state == True:
                    return redirect(url_for('home'))
                else:
                    return render_template('/temporales/confirm_mail.html')
        else:
            return render_template('error.html')
    @app.route('/validar-codigo', methods=['POST'])
    def validar_codigo():
        
        if session:
            #el id lo prodia traer de getid pero no creo que sea lo correcto, se puede dialogar, diablo loco
            id = session.get('usuario')
            user_id = id[0]['id']   
            state = usuarios.get_state_by_id(user_id)
            #chekea el estado de la cuenta, si la cuenta no es confirmada permite validar, no es realmente necesario pero es otra capa de seguridad ?
            if state == False :
                id_session = session['usuario']
                data = request.get_json()
                #obtengo la data de los inputs y los concateno
                codigo = data.get('c1', '') + data.get('c2', '') + data.get('c3', '') + \
                        data.get('c4', '') + data.get('c5', '') + data.get('c6', '') #el segundo parametro es lo que devuelve si esta vacio

                db_user.conectar()
                codigo_correcto  = db_user.consulta(
                    'SELECT confirmed FROM usuarios WHERE id = %s',(id_session[0]['id'])
                )
                db_user.cerrar()
                codigo = hashlib.sha256(codigo.encode()).hexdigest()
                #check si los codigos coinciden, si coinciden cambia el status y el usuario no podria ver mas validar.
                if codigo == codigo_correcto[0]['confirmed']:
                    db_user.conectar()
                    db_user.consulta(
                        "UPDATE usuarios SET state = %s WHERE id = %s",(True, id_session[0]['id'])
                    )
                    return jsonify({'correcto': True, 'redirect_url': url_for('home')}) #para redireccionar al home
                else:
                    return jsonify({'correcto': False})
            else:
                return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))


    @app.route('/reenviar-codigo')
    def reenviar_codigo(): #No se si queres que lo comente pero para mi lo sacas al toque: 👟
        if session: 
            id = session.get('usuario')
            user_id = id[0]['id']
            user_data = usuarios.get_data_by_id(user_id)
            
            codigo_nuevo = ''
            for i in range(6):
                codigo_nuevo += str(random.randrange(0,9,1))
            db_user.conectar()
            codigo_hash = hashlib.sha256(codigo_nuevo.encode()).hexdigest()
            db_user.consulta(
                "UPDATE usuarios SET confirmed = %s WHERE id = %s", (codigo_hash, user_id) 
            )
            db_user.cerrar()
            
            
            MAIL = os.getenv('MAIL')
            MAIL_KEY = os.getenv('MAIL_KEY')
            avisar = Send_Mail(MAIL, MAIL_KEY, user_data[0]['mail'])
            
            contenido = f"""
                <html>
                <body>
                    <p>Tu nuevo código de verificación es: <strong>{codigo_nuevo}</strong></p>
                </body>
                </html>
            """
            avisar.enviarMail('Reenvío de código de verificación', contenido)
            return jsonify({'reenviado': True})
        else:
            return jsonify({'reenviado': False, 'error': 'Sesión no encontrada'}) # esta parte manda un json con el alias digamos de reenviado para que se lo envie al js (validar_count) y validar si se envio correctamente 

