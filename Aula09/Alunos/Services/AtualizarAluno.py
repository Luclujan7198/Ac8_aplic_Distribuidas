from Models.Alunos import Alunos
from Services.ConsultarPorId import ConsultarPorId

def AtualizarAluno(Id, Nome, Ativo):
    AlunoAlterar = ConsultarPorId(Id)

    if AlunoAlterar is None:
        return False
    else:
        AlunoAlterar["Nome"] = Nome
        AlunoAlterar["Ativo"] = Ativo
        return True