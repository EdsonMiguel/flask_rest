from sql import select

def cria_usuario(nome, email, senha):
    return{"id":1, "nome":nome}


def lista_usuarios():
    usuarios = select("nome, email", "usuarios")
    return usuarios

def busca_usuario():
    usuario ={}
    return usuario

def deleta_usuario(id):
    return id


def altera_usuario(id, nome, email, senha):
    novo_usuario = {}
    return novo_usuario
