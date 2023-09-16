# Projeto de cosumo de API
## Resumo:
Este projeto consiste em três partes distintas para interagir com a API pública do GitHub. Cada parte permite aos usuários realizar diferentes ações, como listar repositórios, obter informações básicas do perfil ou obter informações detalhadas do perfil de um usuário do GitHub.

## Parte 1: Listagem de Repositórios do GitHub

## Resumo:
Nesta parte do projeto, o script permite listar os repositórios de um usuário do GitHub.

## Uso
- Execute o script em um ambiente Python. Certifique-se de que você tenha a biblioteca requests e json instaladas em seu ambiente.

- O script solicitará o nome de usuário do GitHub para o qual você deseja listar os repositórios. Digite o nome de usuário e pressione Enter.

- O script fará uma solicitação à API do GitHub para obter os repositórios do usuário.

- Se a solicitação for bem-sucedida (código de status 200), o script imprimirá os nomes dos repositórios na saída padrão.

- Se a solicitação falhar (código de status diferente de 200), o script imprimirá o código de status da resposta.

   
## Parte 2: Informações Básicas do Perfil do Usuário

## Resumo:
Nesta parte do projeto, o script permite obter informações básicas do perfil de um usuário do GitHub.

## Uso:
- Execute o script em um ambiente Python. Certifique-se de que você tenha a biblioteca requests e json instaladas em seu ambiente.

- O script solicitará o nome de usuário do GitHub para o qual você deseja obter informações do perfil. Digite o nome de usuário e pressione Enter.

- O script fará uma solicitação à API do GitHub para obter informações básicas do perfil do usuário.

- Se a solicitação for bem-sucedida (código de status 200), o script imprimirá o nome do usuário, nome de usuário do GitHub e a descrição do perfil na saída padrão.

- Se a solicitação falhar (código de status diferente de 200), o script imprimirá o código de status da resposta.

## Parte 3: Informações Detalhadas do Perfil do Usuário com Pretty Print

## Resumo:
Nesta parte do projeto, o script permite obter informações detalhadas do perfil de um usuário do GitHub e as imprime com pretty print para formatação mais legível.

## Uso:
- Execute o script em um ambiente Python. Certifique-se de que você tenha as bibliotecas requests, json e pprint instaladas em seu ambiente.

- O script solicitará o nome de usuário do GitHub para o qual você deseja obter informações do perfil. Digite o nome de usuário e pressione Enter.

- O script fará uma solicitação à API do GitHub para obter todas as informações do perfil do usuário.

- Se a solicitação for bem-sucedida (código de status 200), o script imprimirá todas as informações do perfil na saída padrão, formatadas de forma legível com a função pprint.

- Se a solicitação falhar (código de status diferente de 200), o script imprimirá o código de status da resposta.

## Dependências:
Certifique-se de que as seguintes bibliotecas Python estejam instaladas em seu ambiente para todas as partes do projeto:

.requests: Usado para fazer solicitações HTTP à API do GitHub.
.json: Usado para analisar a resposta da API em formato JSON.
.pprint: Usado para formatar a saída das informações do perfil de forma mais legível.

## Limitações:
Este projeto depende da disponibilidade da API pública do GitHub.
Ele não lida com autenticação, portanto, está sujeito às limitações de acesso não autenticado à API.

## Como ativar no seu pc
Como Ativar o Ambiente Virtual
- python -m venv P1-DW3
- cd P1-DW3
- cd Scripts
- activate.bat
## como extrair informação do github
acessa o link https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository 
## Comando usado para execução correta do Sistema
- pip install -r requirements.txt
- pip install requests
