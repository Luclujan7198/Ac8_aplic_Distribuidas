from flask import jsonify, request
from Server import App, Response

@App.route("/alunos", methods=["GET"])
def ListarAlunos():
    from Services.ListarAlunos import ListarAlunos
    Dados = ListarAlunos()
    Response["Dados"] = {"Alunos":Dados}
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/alunos/<Id>", methods=["GET"])
def ConsultarPorId(Id):
    from Services.ConsultarPorId import ConsultarPorId
    Dados = ConsultarPorId(Id)
    Response["Dados"] = Dados
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/alunos", methods=["POST"])
def CadastrarAluno():
    from Services.CadastrarAluno import CadastrarAluno
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    CadastrarAluno(Id, Nome)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/alunos", methods=["PUT"])
def AtualizarAluno():
    from Services.AtualizarAluno import AtualizarAluno
    
    Dados = request.get_json()
    Id = Dados["Id"]
    Nome = Dados["Nome"]
    Ativo = Dados["Ativo"]
    AtualizarAluno(Id, Nome, Ativo)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)

@App.route("/alunos/<Id>", methods=["DELETE"])
def InativarAluno(Id):
    from Services.InativarAluno import InativarAluno    
    InativarAluno(Id)
    
    Response["Dados"] = ""
    Response["Status"] = "Sucesso"
    Response["Mensagem"] = ""
    return jsonify(Response)