# Projeto de cosumo de API
Resumo:
Este projeto consiste em três partes distintas para interagir com a API pública do GitHub. Cada parte permite aos usuários realizar diferentes ações, como listar repositórios, obter informações básicas do perfil ou obter informações detalhadas do perfil de um usuário do GitHub.

Parte 1: Listagem de Repositórios do GitHub

Resumo:
Nesta parte do projeto, o script permite listar os repositórios de um usuário do GitHub.

Uso
1) Execute o script em um ambiente Python. Certifique-se de que você tenha a biblioteca requests e json instaladas em seu ambiente.

2) O script solicitará o nome de usuário do GitHub para o qual você deseja listar os repositórios. Digite o nome de usuário e pressione Enter.

3) O script fará uma solicitação à API do GitHub para obter os repositórios do usuário.

4) Se a solicitação for bem-sucedida (código de status 200), o script imprimirá os nomes dos repositórios na saída padrão.

5) Se a solicitação falhar (código de status diferente de 200), o script imprimirá o código de status da resposta.

   
Parte 2: Informações Básicas do Perfil do Usuário

Resumo:
Nesta parte do projeto, o script permite obter informações básicas do perfil de um usuário do GitHub.

Uso:
1) Execute o script em um ambiente Python. Certifique-se de que você tenha a biblioteca requests e json instaladas em seu ambiente.

2) O script solicitará o nome de usuário do GitHub para o qual você deseja obter informações do perfil. Digite o nome de usuário e pressione Enter.

3) O script fará uma solicitação à API do GitHub para obter informações básicas do perfil do usuário.

4) Se a solicitação for bem-sucedida (código de status 200), o script imprimirá o nome do usuário, nome de usuário do GitHub e a descrição do perfil na saída padrão.

5) Se a solicitação falhar (código de status diferente de 200), o script imprimirá o código de status da resposta.

Parte 3: Informações Detalhadas do Perfil do Usuário com Pretty Print

Resumo:
Nesta parte do projeto, o script permite obter informações detalhadas do perfil de um usuário do GitHub e as imprime com pretty print para formatação mais legível.

Uso:
1)Execute o script em um ambiente Python. Certifique-se de que você tenha as bibliotecas requests, json e pprint instaladas em seu ambiente.

2) O script solicitará o nome de usuário do GitHub para o qual você deseja obter informações do perfil. Digite o nome de usuário e pressione Enter.

3) O script fará uma solicitação à API do GitHub para obter todas as informações do perfil do usuário.

4) Se a solicitação for bem-sucedida (código de status 200), o script imprimirá todas as informações do perfil na saída padrão, formatadas de forma legível com a função pprint.

5) Se a solicitação falhar (código de status diferente de 200), o script imprimirá o código de status da resposta.

Dependências:
Certifique-se de que as seguintes bibliotecas Python estejam instaladas em seu ambiente para todas as partes do projeto:

.requests: Usado para fazer solicitações HTTP à API do GitHub.
.json: Usado para analisar a resposta da API em formato JSON.
.pprint: Usado para formatar a saída das informações do perfil de forma mais legível.

Limitações:
Este projeto depende da disponibilidade da API pública do GitHub.
Ele não lida com autenticação, portanto, está sujeito às limitações de acesso não autenticado à API.
