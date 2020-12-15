from flask import Flask, request
from controller import cria_usuario, lista_usuarios
from config import geraResponse

app = Flask("API")


## Configuração de rotas

@app.route("/cadastrar/usuario", methods=["POST"])
def cadastrar_usuario():
    body = request.get_json()
    if("nome" not in body):
        return{"status":400, "Error: ":"O parametro nome é obrigatorio"}
    usuario = cria_usuario(body["nome"], body["email"], body["senha"])
    return geraResponse(200, "Usuario criado", "user",usuario)

@app.route("/listar/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = lista_usuarios()
    return geraResponse(200, "Lista de usuario", "users",usuarios)


app.run()

