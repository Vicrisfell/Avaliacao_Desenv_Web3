import requests
import json
from pprint import pprint

URL = 'https://api.github.com/users/nadiaaoliverr'
req = requests.get(URL)

if req.status_code == 200:
    dados_api = req.json()
    pprint(dados_api)  # Isso imprimirá todas as informações do usuário

elif req.status_code == 404:
    print('Usuário não encontrado')
