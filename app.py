from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask no Docker</title>
    </head>
    <body style="font-family: Arial; text-align: center; background-color: #e8f0fe;">
        <h1>Bem-vindo ao Flask no Docker!</h1>
        <p>Aplicação desenvolvida por Leonardo.</p>

        <a href="/sobre">Sobre</a> |
        <a href="/contato">Contato</a>
    </body>
    </html>
    """


@app.route("/sobre")
def sobre():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sobre o Projeto</title>
    </head>
    <body style="font-family: Arial; text-align: center; background-color: #dff6e4;">
        <h1>Sobre o Projeto</h1>

        <p>
            Este projeto foi desenvolvido para o trabalho de RASI,
            utilizando Python, Flask e Docker.
        </p>

        <a href="/">Página inicial</a> |
        <a href="/contato">Contato</a>
    </body>
    </html>
    """


@app.route("/contato")
def contato():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Contato</title>
    </head>
    <body style="font-family: Arial; text-align: center; background-color: #eeeeee;">
        <div style="
            background-color: white;
            width: 60%;
            margin: 50px auto;
            padding: 30px;
            border-radius: 10px;
        ">
            <h1>Contato</h1>

            <p>Aluno: Leonardo Freitas de Faria</p>
            <p>Curso: Técnico em Informática</p>
            <p>Disciplina: Redes e Administração de Sistemas</p>

            <a href="/">Página inicial</a> |
            <a href="/sobre">Sobre</a>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)