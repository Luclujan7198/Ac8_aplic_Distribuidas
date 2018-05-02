import requests as Req

Url = "http://localhost/alunos/add"
Dados = Req.api.post(Url, json={"Id":1, "Nome":"Vilson"}).json()

print(Dados)