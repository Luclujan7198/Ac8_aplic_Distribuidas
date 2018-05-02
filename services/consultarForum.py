from models.Forum import forum

def ConsultarPorId(id):
    forum = {}
    for Forum in Alunos:
        if Forum["forumId"] == id:
            break
        else:
            Forum = {}
    return Forum