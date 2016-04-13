## O projeto

Esta é uma breve demostração de conhecimento de Python (API de Comunicação RESTful) com o prazo de conclusão de 4 noites.
(Eu fiz este projeto durante 4 noites, ou seja, após o horário de trabalho)

A idéia é fazer algo diferente (que não se encontra pronto na Internet), pois assim ficará claro que não se trata de plágio.

A demonstração será uma mescla de tecnologia nacional (integração com os Correios) e tecnologia internacional - integração com o Twitter (integração com a API RESTFull do Twitter).

A idéia básica é: 
1. O usuário informa um CEP
2. A partir do CEP eu vou buscar nos Correios a cidade referente ao CEP informado
3. Ao obter a cidade do CEP eu vou fazer uma busca no Twitter relacionada ao nome da cidade
4. As cidades serão todas gravadas em banco de dados
5. Os dados gravados em banco de dados vão gerar endpoints que serão consumidos pelo Frontend

Ao decorrer do projeto será adicionado mais funcionalidades para poder utilizar todos os verbos GET, POST, PUT e DELETE, bem como tratar e usar a maior quantidade de status http (200, 404, etc...)

O desenvolvimento será tanto em ambiente Linux quanto Windows.

## Descrição dos arquivos

* simple_twitter_rest_flask.py = Uma aplicação simples em Python que através de um CEP informado busca no Twitter posts sobre a cidade pertencente ao CEP.
Ao contrário do exemplo abaixo neste exemplo foi utilizado OAuth 1 com a biblioteca flask_oauthlib
Foi utilizado o Framework Flask e há tratamento de erros.

* simple_twitter_rest_no_framework.py = Uma simples demostração em Python de como se autentica no Twitter utilizando-se OAuth 2 e fazendo a requisição com urllib3 - a requisição foi feita ajustando-se o verbo, o header e o corpo da requisição.
*Como trata-se de uma simples demostração não foi realizado nenhum tratamento de erros neste arquivo em específico.*

## Detalhes de desenvolvimento

* Segunda noite: 12/04/2016
1. Foram aplicadas algumas melhorias no tratamento de erros
2. Adicionado conexão com o banco de dados MySql
3. Adicionado integração de busca de CEP utilizando-se o serviço https://viacep.com.br
4. O resultado das buscas são incluídos no banco de dados

* Primeira noite: 11/04/2016
1. Configuração do ambiente de desenvolvimento nas plataformas Windows e Linux
2. Criação de conta no GitHub para alocar o projeto
3. Criação de uma aplicação básica em Python para autenticar com o Twitter via API sem framework
4. Inicio do desenvolvimento da idéia do aplicativo utilizando-se Phyton e o framework Flask

## Instalação

Em breve...


