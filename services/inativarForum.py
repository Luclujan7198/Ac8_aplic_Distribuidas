from models.Forum import forum
from services.consultarForum import ConsultarPorId

def InativarForum(Id):
    forumAlterar = ConsultarPorId(Id)

    if forumAlterar is None:
        return False
    else:
        forumAlterar["Ativo"] = False
        return forumAlterar