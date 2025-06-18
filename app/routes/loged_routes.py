"""
CONTIENE LAS RUTAS DE CUANDO EL USUARIO YA ESTA LOGUEADO
"""
from flask import render_template, url_for, request,  redirect , session
from app.utils.Error_Saver import save_error
from app.utils.preguntas import preguntas_graciosas
import random

def logued_route(app, usuarios, publicaciones):
    @app.route('/home')
    def home():
        token = session.get('usuario')
        if session:
            id_user = token[0]['id']
            info_user = usuarios.get_data_by_id(id_user)
            user_state = usuarios.get_state_by_id(id_user)
            users_suggested = usuarios.suggest_users(id_user)
            if user_state == True:
                
                pregunta = random.choice(preguntas_graciosas)
                publicacion = publicaciones.ver_publicaciones(id_user) #traigo las publicaciones
                print(publicacion, 'publicacion')
                return render_template('home.html', usuario=info_user[0],publicaciones=publicacion,pregunta=pregunta, usuarios_sugeridos=users_suggested)
            else:
                return redirect(url_for('validation'))
        else:
            return render_template('error.html')
        
    @app.route('/app/publicar',methods=['POST'])
    def publicar():
        try:
            token = session.get('usuario')
            id_user = token[0]['id']
            contenido = request.form['input_publish']
            if contenido == '':
                return redirect(url_for('home'))
            else:
                publicaciones.publicar(id_user,contenido)
                return redirect(url_for('home'))
        except NameError as e:
            save_error(e)
            return render_template('error.html')
    @app.route('/app/seguir',methods=['POST'])

    def seguir():
        token = session.get('usuario')
        id_user = token[0]['id']
        id_seguido = request.form['id_seguido']
        seguimiento = usuarios.seguir_usuario(id_user,id_seguido)
        if seguimiento == True:
            return redirect(url_for('home'))
        else:
            return render_template('error.html')
        
    @app.route('/app/no-seguir',methods=['POST'])
    
    def unfollow():
        token = session.get('usuario')
        id_user = token[0]['id']
        id_seguido = request.form['id_seguido']
        un_seguir = usuarios.dejar_de_seguir(id_user,id_seguido)
        if un_seguir == True:
            return redirect(url_for('home'))
    
