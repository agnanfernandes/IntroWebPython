from flask import Flask, render_template

app = Flask("Olá") #para utilizar os recursos do framework por essa variável

"""app.route: metodo que permite rotas para serem acessadas
    e passa o nome da rota que "/" é o diretório raiz, para outros diretorios,
    especificar nomes."""
@app.route("/alunos") 
def alunos():
    return render_template("hello.html")

    
