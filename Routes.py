from flask import jsonify, request
from Server import App, Response

@App.route("/forum", methods=["GET"])
def ListarForum():
    from services.getForums import listarForuns
    Dados = listarForuns()
    Response["Dados"] = {"Forum":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/forum", methods=["POST"])
def postForum():
    from services.postForum import postForum
    Dados = request.get_json()
    forumId = Dados["forumId"]
    criadorId = Dados["criadorId"]
    titulo = Dados["titulo"]
    descricao = Dados["descrição"]
    criacaoData = Dados["criacaoData"]
    ultimoPostDate = Dados["ultimoPostDate"]

    postForum(forumId,criadorId,titulo,descricao,criacaoData,ultimoPostDate)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/forum/<Id>", methods=["GET"])
def consultaForumPorId(Id):
    from services.consultarForum import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/forum/inactivate", methods=["POST"])
def inativarForum():
    from services.inativarForum import InativarForum
    Dados = request.get_json()

    forum = InativarForum(Dados["forumId"])

    Response["Dados"] = forum
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""

    return jsonify(Response)

@App.route("/forum/activate", methods=["POST"])
def ativarForum():
    from services.ativarForum import ativarForum
    Dados = request.get_json()

    forum = ativarForum(Dados["forumId"])

    Response["Dados"] = forum 
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    
    return jsonify(Response)

@App.route("/forum/register", methods=["POST"])
def registrarForum():
    from services.registrarForum import registrarForum

    Dados = request.get_json()

    forum = registrarForum(Dados["forumId"])

    Response["Dados"] = forum 
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""

    return jsonify(Response)


@App.route("/forum/unregister", methods=["POST"])
def removerRegistroForum():
    from services.removerRegistroForum import removerRegistroForum

    Dados = request.get_json()

    forum = removerRegistroForum(Dados["forumId"])

    Response["Dados"] = forum 
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""

    return jsonify(Response)


@App.route("/forum/<Id>/post", methods=["GET"])
def ListarPosts():
    from services.getPosts import listarPosts
    Dados = listarPosts()

    Response["Dados"] = {"Post":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""

    return jsonify(Response)


@App.route("/forum/post", methods=["POST"])
def cadastrarPost():
    from services.cadastrarPost import cadastrarPost
    Dados = request.get_json()
    PostId = Dados["PostId"]
    ForumId = Dados["ForumId"]
    OwnerId = Dados["OwnerId"]
    CreateDate = Dados["CreateDate"]
    Message = Dados["Message"]
    Visible = Dados["Visible"]

    cadastrarPost(PostId,ForumId,OwnerId,CreateDate,Message,Visible)

    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""

    return jsonify(Response)

@App.route("/forum/post/<Id>", methods=["GET"])
def consultaPostPorId(Id):
    from services.consultarPost import ConsultarPostPorId

    Dados = ConsultarPostPorId(Id)

    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""

    return jsonify(Response)
