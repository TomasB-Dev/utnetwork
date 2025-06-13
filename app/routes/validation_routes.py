from flask import render_template, url_for, request,  redirect, jsonify , session


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

