"""
CONTIENE LAS RUTAS DE CUANDO EL USUARIO YA ESTA LOGUEADO
"""

from flask import render_template, url_for, request,  redirect , session

def logued_route(app,usuarios):
    @app.route('/home')
    def home():
        token = session.get('usuario')
        if session:
            id_user = token[0]['id']
            info_user = usuarios.get_data_by_id(id_user)
            user_state = usuarios.get_state_by_id(id_user)
            if user_state == True:
                return render_template('home.html', usuario=info_user[0])
            else:
                return redirect(url_for('validation'))
        else:
            return render_template('error.html')