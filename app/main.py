# from distutils.log import debug
from urllib import request
from flask import Flask, render_template
# from passlib.hash import md5_crypt as md5
# from passlib.hash import sha256_crypt as sha256
# from passlib.hash import sha512_crypt as sha512

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def index(): 
    # data = {
    #     "titulo": "Papelazo",
    #     "subtitulo": "Juego",
    #     "arreglo": ["Datos", "Piedra", "Papel", "Tijera"]
    # }
    return render_template("login.html")

@app.route("/acceso")
def acceso():
    return render_template("layout.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/menu", methods=["GET", "POST"])
def menu():
    return render_template("prueba.html")

def qery1():
    print(request)

if __name__ == "__main__":
    app.add_url_rule("/qery1", view_func=qery1)
    app.run(debug=True)

