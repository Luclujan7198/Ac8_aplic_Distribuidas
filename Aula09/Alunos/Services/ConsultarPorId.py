from Models.Alunos import Alunos

def ConsultarPorId(Id):
    Aluno = {}
    for Aluno in Alunos:
        if Aluno["Id"] == Id:
            break
        else:
            Aluno = {}
    return Aluno