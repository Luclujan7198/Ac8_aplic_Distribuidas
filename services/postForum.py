from Models.Forum import Forum,forum

def postForum(forumId,criadorId,titulo,descricao,criacaoData,ultimoPostDate):
    Forum.append({"forumId":forumId, "criadorId":criadorId,"titulo":titulo,"descrição":descricao,"criacaoData":criacaoData,"ultimoPostDate":ultimoPostDate, "Ativo":True})
    return Forum