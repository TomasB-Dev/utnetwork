"""
CONTIENE LAS RUTAS DE CUANDO EL USUARIO YA ESTA LOGUEADO
"""
from flask import render_template, url_for, request,  redirect , session
from app.utils.Error_Saver import save_error
from app.utils.preguntas import preguntas_graciosas
import random

def logued_route(app, usuarios, publicaciones,db_user):
    @app.route('/home')
    def home():
        
        token = session.get('usuario')
        if session:
            id_user = token[0]['id']
            info_user = usuarios.get_data_by_id(id_user)
            user_state = usuarios.get_state_by_id(id_user)
            users_suggested = usuarios.suggest_users(id_user)
            if user_state == True:
                usuarios.actualizar_conexion(id_user)
                page = int(request.args.get("page", 1)) 
                limit = 40
                offset = (page - 1) * limit
                pregunta = random.choice(preguntas_graciosas)
                publicacion = publicaciones.ver_publicaciones(id_user,limit,offset) #traigo las publicaciones
                return render_template('home.html', usuario=info_user[0],publicaciones=publicacion,pregunta=pregunta, usuarios_sugeridos=users_suggested,page=page)
            else:
                return redirect(url_for('validation'))
        else:
            return render_template('error.html')
        
    @app.route('/miperfil')
    def myprofile():
        token = session.get('usuario')
        if session:
            id_user = token[0]['id']
            info_user = usuarios.get_data_by_id(id_user)
            user_state = usuarios.get_state_by_id(id_user)
            if user_state == True:
                usuarios.actualizar_conexion(id_user)
                stats = usuarios.obtener_estadisticas(id_user)
                publica = publicaciones.solo_una_persona(id_user)
                return render_template('myprofile.html', usuario=info_user[0],stats=stats,publicaciones=publica)
            else:
                return redirect(url_for('validation'))
        else:
            return render_template('error.html')
        
    @app.route('/perfil',methods=['POST'])
    def profile():
        token = session.get('usuario')
        if session:
            id_user = token[0]['id']
            id_perfil = request.form['id_user']
            user_state = usuarios.get_state_by_id(id_user)
            if user_state == True:
                usuarios.actualizar_conexion(id_user)
                info_user = info_user = usuarios.get_data_by_id(id_user)
                info_perfil =  usuarios.get_data_by_id(id_perfil)
                stats = usuarios.obtener_estadisticas(id_perfil)
                publica = publicaciones.solo_una_persona(id_perfil)
                seguidos = usuarios.obtener_seguidores(id_user)
                return render_template('profile.html', usuario=info_user[0],stats=stats,publicaciones=publica,info_perfil=info_perfil[0],seguidos=seguidos)
            else:
                return redirect(url_for('validation'))
        else:
            return redirect(url_for('login'))

    @app.route('/app/publicar',methods=['POST'])
    def publicar():
        try:
            token = session.get('usuario')
            id_user = token[0]['id']
            contenido = request.form['input_publish']
            if contenido == '':
                return redirect(url_for('home'))
            else:
                usuarios.actualizar_conexion(id_user)
                publicaciones.publicar(id_user,contenido)
                return redirect(request.referrer)
        except Exception as e:
            save_error(e)
            return render_template('error.html')
        
    #INICIA SEGUIR
    @app.route('/app/seguir',methods=['POST'])

    def seguir():
        """
        Ruta para  seguir a un usuario
        """
        token = session.get('usuario')
        id_user = token[0]['id']
        id_seguido = request.form['id_seguido']
        usuarios.actualizar_conexion(id_user)
        seguimiento = usuarios.seguir_usuario(id_user,id_seguido)

        if seguimiento == True:
            return redirect(url_for('home'))
        else:
            return render_template('error.html')
        
    @app.route('/app/no-seguir',methods=['POST'])
    
    def unfollow():
        """
        Ruta para dejar de seguir a un usuario
        """
        token = session.get('usuario')
        id_user = token[0]['id']
        id_seguido = request.form['id_seguido']
        usuarios.actualizar_conexion(id_user)
        
        un_seguir = usuarios.dejar_de_seguir_usuario(id_user,id_seguido)
        if un_seguir == True:
            return redirect(url_for('home'))
        
    #INICIA PUBLICACIONES
    @app.route('/eliminar-publi',methods=['POST'])
    def eliminar_publi():
        id_publicacion = request.form['id_publi']
        publicaciones.eliminar_publicacion(id_publicacion)
        return redirect(request.referrer)
    
    
    
    
    @app.route('/actualizar-publi', methods=['POST'])
    def actualizar_publi():
        id_publicacion = request.form['id_publi']
        nuevo_contenido = request.form['contenido']
        print('nuevapublicacion', nuevo_contenido)
        publicaciones.actualizar_publicacion(id_publicacion, nuevo_contenido)
        return redirect(request.referrer)
    #INICIA BUSCAR
    @app.route('/buscar',methods=['POST'])
    def buscar():
        if session:
            token = session.get('usuario')
            id_user = token[0]['id']
            state = usuarios.get_state_by_id(id_user)
            if state == True:
                usuarios.actualizar_conexion(id_user)
                info_user = usuarios.get_data_by_id(id_user)
                seguidos = usuarios.obtener_seguidores(id_user)
                buscar = request.form['busqueda']
                busqueda = usuarios.buscar_usuario(buscar)
                return render_template('search.html',usuario=info_user[0],busqueda=busqueda,seguidos=seguidos)
            else:
                return redirect(url_for('validation'))
        else:
            return redirect(url_for('login'))

