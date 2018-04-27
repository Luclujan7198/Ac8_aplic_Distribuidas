class Forum():
    forumId = None
    cridorId = None
    titulo = None
    descricao = None
    criacaoData = None
    ultimoPostDate = None
    ativo = None


def transformarJson(forum):
    forumResposta = []
    forumRepsosta.append(forum.forumId)
    forumRepsosta.append(forum.cridorId)
    forumRepsosta.append(forum.titulo)
    forumRepsosta.append(forum.descricao)
    forumRepsosta.append(forum.criacaoData)
    forumRepsosta.append(forum.ultimoPostDate)
    forumRepsosta.append(forum.ativo)