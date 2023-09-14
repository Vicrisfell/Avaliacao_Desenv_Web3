import requests
import json
from pprint import pprint
nome = input("Escreva seu usuario: ")
URL = f'https://api.github.com/users/{nome}'
req = requests.get(URL)

if req.status_code == 200:
    dados_api = req.json()
    pprint(dados_api)  # Isso imprimirá todas as informações do usuário

elif req.status_code == 404:
    print('Usuário não encontrado')
