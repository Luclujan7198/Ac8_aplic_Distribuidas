from models.Forum import forum
from services.consultarForum import ConsultarPorId

def registrarForum(forumId):
    forumAlterar = ConsultarPorId(forumId)

    if forumAlterar is None:
        return False
    else:
        forumAlterar["registro"] = True

        return forumAlterar
    