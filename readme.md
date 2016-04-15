## O projeto

Esta é uma breve demostração de conhecimento de Python (API de Comunicação RESTful) com o prazo de conclusão de 4 noites.
(Eu vou fazer este projeto durante 4 noites, ou seja, após o horário de trabalho)

*A idéia é fazer algo diferente (que não se encontra pronto na Internet), pois assim ficará claro que não se trata de plágio.*

A demonstração será uma mescla de tecnologia nacional (integração com a busca de CEP dos Correios) e tecnologia internacional - integração com o Twitter (integração com a API RESTFul do Twitter).

A idéia básica é:
1. O usuário informa um CEP
2. A partir do CEP eu vou buscar via API a cidade referente ao CEP informado
3. Ao obter a cidade do CEP eu vou fazer uma busca no Twitter relacionada ao nome da cidade
4. As cidades referentes aos CEPs buscados serão todas gravadas em banco de dados
5. Os dados gravados em banco de dados vão gerar endpoints que serão consumidos pelo Frontend
6. O Frontend busca via API e lista todas as cidades buscadas no Twitter, bem como informa o verbo utilizado na requisição (GET, PUT, etc...)

Eu utilizo sistemas operacionais diferentes em casa e no trabalho, portanto o projeto será feito tanto em Windows quanto em Linux.
- Linux - Vim/Sublime
- Windows 10 - Visual Studio 2015

Razões pelo qual eu optei pelo Python v2.7.11:
- Apesar do Python 3 ter sido lançado em 2008 o Python 2 ainda é a versão mais utilizada acordo com varias pesquisas publicadas na Internet
- Este projeto é muito simples e não há nenhuma vantagem significativa em utilizar a versão 3

Razões pelo qual eu optei pelo MicroFramework Flask:
- A ajuda de um Framework é bem vinda quando o projeto deve ser entregue muito rapido
- A curva de aprendizado do Framework Flask é curta
- Estava vetado no escopo do projeto o uso do Framework Django

## Descrição dos arquivos

- *simple_twitter_rest_flask.py* = Uma aplicação simples em Python que através de um CEP informado busca no Twitter posts sobre a cidade pertencente ao CEP. Gera também um endpoint (API) que busca as informações previamente gravadas no banco de dados MySql e informa todas as cidades que foram buscadas no Twitter. Foi utilizado OAuth 1 com a biblioteca flask_oauthlib para a comunicação com o Twitter, bem como o Framework Flask. Está implementado tratamento de erros e log.

- *frontend_flask.py* = Consome a API gerada pelo arquivo *simple_twitter_rest_flask.py* via server-side utilizando os verbos GET, PUT e DELETE. O html gerado informa a resposta e os verbos utilizados. Está implementado tratamento de erros e log.

- *simple_twitter_rest_no_framework.py* = Uma simples demostração em Python de como se autentica no Twitter utilizando-se OAuth 2 e fazendo a requisição com urllib3 - a requisição foi feita ajustando-se o verbo, o header e o corpo da requisição. 
*Como trata-se de uma simples demostração não foi realizado nenhum tratamento de erros neste arquivo em específico.*

## Detalhes de desenvolvimento

**Quarta noite: 14/04/2016 para 15/04/2016**
1. API configurada para responder aos verbos ['GET', 'POST', 'PUT', 'DELETE']
2. Feito Frontend desacoplado em Python (Flask) com tratamento de erros
3. Configurado API para responder na porta 8086
4. Feito o a proposta EXTRA (logs) = os arquivos de log ficam na raiz com a extensão .log
5. Conclusão desta documentação 
6. Entrega do projeto

**Terceira noite: 13/04/2016 para 14/04/2016**
1. Feito tratamento da variável de CEP utilizando-se expressão regular
2. Feito um simples endpoint de API em /API que responde as cidades que foram procuradas baseando-se nos dados inseridos no MySql
3. Juntado o script que gera a tabela do MySql no repositório
4. Modificado a porta http da aplicação para 8085

**Segunda noite: 12/04/2016 para 13/04/2016**
1. Foram aplicadas algumas melhorias no tratamento de erros
2. Adicionado conexão com o banco de dados MySql
3. O resultado das buscas são incluídos no banco de dados
4. Adicionado integração de busca de CEP utilizando-se o serviço (https://viacep.com.br)
5. Primeiro envio ao repositório (https://github.com/fcamaramagazine/pythonsample)

**Primeira noite: 11/04/2016 para 12/04/2016**
1. Configuração do ambiente de desenvolvimento nas plataformas Windows e Linux
2. Criação de conta no GitHub para alocar o projeto
3. Criação de uma aplicação básica em Python para autenticar com o Twitter via API sem framework
4. Inicio do desenvolvimento da idéia do aplicativo utilizando-se Phyton e o framework Flask

## Instalação 

Considerando que você já possua o MySql instalado crie o banco de dados de acordo com o script contido em *mysql_tables.sql*
*Você deve também modificar as informações de conexão do banco de dados no arquivo simple_twitter_rest_flask.py apontando para o seu banco de dados*

Como rodar a aplicação no Ubuntu 14.04 (considerando que você possua a instalação server default)

```
$ sudo apt-get install python-virtualenv
$ mkdir fcamaramagazine
$ cd fcamaramagazine
$ virtualenv venv
$ . venv/bin/activate
$ pip install Flask
$ sudo apt-get install git
$ git clone https://github.com/fcamaramagazine/pythonsample.git
$ cd pythonsample/
$ pip install urllib3
$ pip install requests
$ pip install flask-oauthlib
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install python-dev
$ pip install flask-mysqldb
```

Para executar a aplicação:
```
$ python simple_twitter_rest_no_framework.py
$ python simple_twitter_rest_flask.py
$ python frontend_flask.py
```

Observação:
- O arquivo python simple_twitter_rest_no_framework.py é apenas um scrit e irá rodar no próprio terminal
- O arquivo python simple_twitter_rest_no_framework.py irá responder na porta 8085
- O arquivo python frontend_flask.py irá responder na porta 8086
