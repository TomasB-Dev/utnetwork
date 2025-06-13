from flask import render_template, url_for

def nologued_view(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/terminos')
    def terminos():
        return render_template('terminos.html')