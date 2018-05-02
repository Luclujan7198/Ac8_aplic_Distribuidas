import requests as Req


Url = "http://localhost/forum"
Dados = Req.api.post(Url, json={"forumId":1, "criadorId":1,"titulo":"teste","descrição":"descricao","criacaoData":"11/04/2018","ultimoPostDate":"11/04/2018", "Ativo":True,"registro":""}).json()

print(Dados)