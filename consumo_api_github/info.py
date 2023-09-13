import requests
import json

URL = 'https://api.github.com/users/nadiaaoliverr'
req = requests.get(URL)

if req.status_code == 200:
    dados_api = req.json()
    nome = dados_api['name']
    login = dados_api['login']
    descricao = dados_api['bio']
    
    print("Nome do usuário:", nome)
    print("Nome de usuário:", login)
    print("Descrição do perfil:", descricao)
    
if req.status_code == 404:
    print('Usuário não encontrado')
