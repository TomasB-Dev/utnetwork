from flask import Flask, render_template, url_for, request,  redirect
from app.registro import Registro
import time

app =  Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/terminos')
def terminos():
    return render_template('terminos.html')
@app.route('/app/registrar', methods=['POST'])
def registrar():
    username = request.form['name']
    key = request.form['password']
    mail = request.form['email']
    usuario = Registro(username, mail,key )
    usuario.hashear()
    usuario.registrar()
    time.sleep(1)#momentaneo, hablar con agus para ver que opina
    return redirect(url_for('index'))# aca agregar la confirmacion por el mail

if __name__ == "__main__":
    app.run(debug=True)