from flask import Flask, render_template, url_for, request,  redirect
from app.registro import Registro
from app.Loguear import Login
import time


app =  Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods=['GET'])
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
<<<<<<< HEAD
    usuario = Registro(username, mail,key )
    usuario.registrar()
    time.sleep(1)#momentaneo, hablar con agus para ver que opina 
    return redirect(url_for('index'))# aca agregar la confirmacion por el mail
=======
    usuario = Registro(username, mail, key)
    registro = usuario.registrar()
    time.sleep(1)  # momentaneo, hablar con agus para ver que opina
    # aca agregar la confirmacion por el mail
    if registro:
        return redirect(url_for('login'))
        
    else:
        return redirect(url_for('register'))
>>>>>>> be9189dab2338a10542da4ec6c21c6e5b474f76a

@app.route('/app/login', methods=['POST'])
def login():
    mail = request.form['email']
    key = request.form['password']
    usuario = Login(mail, key)
    usuario.loguear()
    time.sleep(1)
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)