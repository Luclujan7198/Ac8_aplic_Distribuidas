from models.Forum import forum
from services.consultarForum import ConsultarPorId

def removerRegistroForum(forumId):
    forumAlterar = ConsultarPorId(forumId)

    if forumAlterar is None:
        return False
    else:
        forumAlterar["registro"] = False

        return forumAlterar
    