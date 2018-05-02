from models.Post import post

def ConsultarPostPorId(id):
    posts = {}
    for posts in post:
        if posts["PostId"] == id:
            break
        else:
            posts = {}
    return posts