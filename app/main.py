# from distutils.log import debug
from urllib import request
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import Offline
# from passlib.hash import md5_crypt as md5
# from passlib.hash import sha256_crypt as sha256
# from passlib.hash import sha512_crypt as sha512

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'papelazo'
 
mysql = MySQL(app)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login(): 
    print("a")
    if request.method == "POST":
        print(request.form["username"])
        print(request.form["password"])
        return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/menu", methods=["GET", "POST"])
def menu():
    return render_template("menu.html")

@app.route("/404")
def NoEncontrado():
    return render_template("404.html")

@app.route("/tablero")
def offline():
    Offline.juego()
    return render_template("tablero.html")

def qery1():
    print(request)

if __name__ == "__main__":
    app.add_url_rule("/qery1", view_func=qery1)
    app.run(debug=True)

