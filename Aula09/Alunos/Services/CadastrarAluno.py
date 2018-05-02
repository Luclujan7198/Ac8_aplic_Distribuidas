from Models.Alunos import Alunos

def CadastrarAluno(Id, Nome):
    Alunos.append({"Id":Id, "Nome":Nome, "Ativo":True})
    return