"""
CONTIENE LAS RUTAS QUE NO SE NECESITA ESTAR LOGUEADO PARA VER
"""
from flask import render_template

def nologued_view(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/terminos')
    def terminos():
        return render_template('terminos.html')