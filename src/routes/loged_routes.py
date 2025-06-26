"""
CONTIENE LAS RUTAS DE CUANDO EL USUARIO YA ESTA LOGUEADO
"""
from flask import render_template, url_for, request,  redirect , session,jsonify
from src.utils.Error_Saver import save_error
from src.utils.preguntas import preguntas_graciosas
import random
from flask_socketio import emit, join_room

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
                busqueda = usuarios.buscar_usuario(buscar,id_user)
                return render_template('search.html',usuario=info_user[0],busqueda=busqueda,seguidos=seguidos)
            else:
                return redirect(url_for('validation'))
        else:
            return redirect(url_for('login'))

    @app.route('/actualizar-descripcion', methods=['POST'])
    def actualizar_descripcion():
        id_usuario = request.form['id_usuario']
        nueva_descripcion = request.form['descripcion_contenido']
        usuarios.actualizar_descripcion(id_usuario, nueva_descripcion)
        return redirect(request.referrer)
    
    @app.route('/mis-mensajes')
    def mensajes():
        if session:
            token = session.get('usuario')
            id_user = token[0]['id']
            info_user = usuarios.get_data_by_id(id_user)
            seguidos = usuarios.obtener_informacion_seguidos(id_user)
            return render_template('mensajes.html',usuario=info_user[0],seguidos=seguidos)
        else:
            return redirect(url_for('login'))
    
    @app.route('/mensajes/<int:destinatario_id>')
    def obtener_mensajes(destinatario_id):
        if session:
            token = session.get('usuario')
            id_user = token[0]['id']

            # para obtener el historial de msj
            mensajes = db_user.consulta("""
                SELECT 
                    mensajes.id,
                    emisor.id AS emisor_id,
                    emisor.nombre AS emisor_nombre,
                    receptor.id AS receptor_id,
                    receptor.nombre AS receptor_nombre,
                    mensajes.contenido,
                    mensajes.fecha
                FROM mensajes
                JOIN usuarios AS emisor ON mensajes.emisor = emisor.id
                JOIN usuarios AS receptor ON mensajes.receptor = receptor.id
                WHERE 
                    (emisor.id = %s AND receptor.id = %s) OR 
                    (emisor.id = %s AND receptor.id = %s)
                ORDER BY mensajes.fecha ASC
            """, (id_user, destinatario_id, destinatario_id, id_user))
            print(mensajes)
            return jsonify(mensajes)
        else:
            return redirect(url_for('login'))

def socket_events(socketio, usuarios):
    
    @socketio.on('join')
    def handle_join(data):
        """
        se une a una sala ("conversacion")
        """
        id_user = data['id_user']
        join_room(f'user_{id_user}')
        emit('status', {'msg': f'Usuario {id_user} se unió a su sala.'}, room=f'user_{id_user}')

    @socketio.on('send_message')
    def handle_message(data):
        """
        envia los msj
        """
        sender_id = data['sender_id']
        recipient_id = data['recipient_id']
        message = data['message']
        usuarios.guardar_mensaje(sender_id, recipient_id, message)

        # es para el chat en tiempo real
        emit('receive_message', {
            'sender_id': sender_id,
            'message': message
        }, room=f'user_{recipient_id}')