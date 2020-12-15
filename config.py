def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"]=status
    response["mensagem"]=mensagem
    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    return response