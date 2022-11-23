from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "1234"

app = Flask("Olá") #para utilizar os recursos do framework por essa variável

app.config.from_object(__name__)

def conectar():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_first_request():
    g.bd = conectar()

@app.teardown_request
def teardown_request(exception):
    g.bd.close()

@app.route("/") 
def alunos():
    nomeUsuario = ["Danilo", "Caio", "Guilherme", None, "Cassio"]
    return render_template("hello.html", nome=nomeUsuario)

 