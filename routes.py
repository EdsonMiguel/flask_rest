from flask import Flask, request

from main import cria_usuario

app = Flask("API")


@app.route("/teste",methods=["GET"])
def olaMundo():
    return{"Ola":"Seu zé"}


@app.route("/cadastrar/usuario", methods=["POST"])
def cadastrar_usuario():
    body = request.get_json()

    if("nome" not in body):
        return{"status":400, "Error: ":"O parametro nome é obrigatorio"}


    usuario = cria_usuario(body["nome"], body["email"], body["senha"])


    return geraResponse(200, "Usuario criado", "user",usuario)


def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"]=status
    response["mensagem"]=mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response


app.run()

#gente@cotabox.com.br