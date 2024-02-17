from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.debug = True

app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "petDB"

mysql = MySQL(app)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT pet_name FROM petInfo WHERE username = % s', (username))
    rv = cursor.fetchall()
    
    return render_template("register.html", msg=rv)


