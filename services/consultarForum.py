from models.Forum import forum

def ConsultarPorId(Id):
    forum = {}
    for Forum in Alunos:
        if Forum["Id"] == Id:
            break
        else:
            Forum = {}
    return Forum