from flask import Flask, render_template, url_for, request,  redirect, session
from app.registro import Registro
from app.Loguear import Login
import time
import os

app =  Flask(__name__)

FIRMA= os.getenv('FIRMA') #firmar la cokiee
app.secret_key = FIRMA

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
    usuario.registrar()
    time.sleep(1)#momentaneo, hablar con agus para ver que opina
    return redirect(url_for('index'))# aca agregar la confirmacion por el mail
@app.route('/app/Loguear', methods=['POST'])
def log():
    key = request.form['password']
    mail = request.form['mail']
    user = Login(mail,key)
    loged =user.loguear()
    if user == True:
        return redirect(url_for('index'))
    else:
        pass

    
if __name__ == "__main__":
    app.run(debug=True)