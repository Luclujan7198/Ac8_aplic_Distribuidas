from models.Forum import forum
from services.consultarForum import ConsultarPorId

def ativarForum(Id):
    forumAlterar = ConsultarPorId(Id)

    if forumAlterar is None:
        return False
    else:
        forumAlterar["Ativo"] = True
        return forumAlterar