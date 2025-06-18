"""
CONTIENE LAS RUTAS DE CUANDO EL USUARIO YA ESTA LOGUEADO
"""
from flask import render_template, url_for, request,  redirect , session
from app.utils.Error_Saver import save_error

def logued_route(app, usuarios, publicaciones):
    @app.route('/home')
    def home():
        token = session.get('usuario')
        if session:
            id_user = token[0]['id']
            info_user = usuarios.get_data_by_id(id_user)
            user_state = usuarios.get_state_by_id(id_user)
            if user_state == True:
                publicacion = publicaciones.ver_publicaciones(id_user) #traigo las publicaciones
                return render_template('home.html', usuario=info_user[0],publicaciones=publicacion)
            else:
                return redirect(url_for('validation'))
        else:
            return render_template('error.html')
        
    @app.route('/app/publicar',methods=['POST'])
    def publicar():
        try:
            token = session.get('usuario')
            id_user = token[0]['id']
            contenido = request.form['contenido']
            publicaciones.publicar(id_user,contenido)
            return redirect(url_for('home'))
        except NameError as e:
            save_error(e)
            return render_template('error.html')