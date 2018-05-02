from Models.Alunos import Alunos
from Services.ConsultarPorId import ConsultarPorId

def InativarAluno(Id):
    AlunoAlterar = ConsultarPorId(Id)

    if AlunoAlterar is None:
        return False
    else:
        AlunoAlterar["Ativo"] = False
        return True