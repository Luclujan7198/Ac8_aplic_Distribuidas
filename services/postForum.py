from models.Forum import forum

def postForum(forumId,criadorId,titulo,descricao,criacaoData,ultimoPostDate):
    forum.append({"forumId":forumId, "criadorId":criadorId,"titulo":titulo,"descrição":descricao,"criacaoData":criacaoData,"ultimoPostDate":ultimoPostDate, "Ativo":True,"registro":""})
    return forum