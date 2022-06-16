from flask import Flask, render_template, request, redirect, url_fir, session
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)
app.config["MYSQL_HOST"] = "local_host"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = " "
app.config["MYSQL_DB"] = "app_citas"

@app.route("/")
def home():
    return render_template("menu_principal.html")

if __name__ == "__main__":
    app.run(debug = True)


