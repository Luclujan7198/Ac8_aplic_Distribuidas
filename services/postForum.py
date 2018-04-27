from Models.Forum import Forum,forum

def postForum(forumId,criadorId,titulo,descricao,criacaoData,ultimoPostDate,ativo):
    Forum = Forum()
    Forum.forumId = forumId
    Forum.criadorId = criadorId
    Forum.titulo = titulo
    Forum.descricao = descricao
    Forum.criacaoData = criacaoData
    Forum.ultimoPostDate = ultimoPostDate
    Forum.ativo = ativo
    return Forum