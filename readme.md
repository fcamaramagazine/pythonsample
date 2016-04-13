## O projeto

Esta � uma breve demostra��o de conhecimento de Python (API de Comunica��o RESTful) com o prazo de conclus�o de 4 noites.
(Eu fiz este projeto durante 4 noites, ou seja, ap�s o hor�rio de trabalho)

A id�ia � fazer algo diferente (que n�o se encontra pronto na Internet), pois assim ficar� claro que n�o se trata de pl�gio.

A demonstra��o ser� uma mescla de tecnologia nacional (integra��o com os Correios) e tecnologia internacional - integra��o com o Twitter (integra��o com a API RESTFull do Twitter).

A id�ia b�sica �: 
1. O usu�rio informa um CEP
2. A partir do CEP eu vou buscar nos Correios a cidade referente ao CEP informado
3. Ao obter a cidade do CEP eu vou fazer uma busca no Twitter relacionada ao nome da cidade
4. As cidades ser�o todas gravadas em banco de dados
5. Os dados gravados em banco de dados v�o gerar endpoints que ser�o consumidos pelo Frontend

Ao decorrer do projeto ser� adicionado mais funcionalidades para poder utilizar todos os verbos GET, POST, PUT e DELETE, bem como tratar e usar a maior quantidade de status http (200, 404, etc...)

O desenvolvimento ser� tanto em ambiente Linux quanto Windows.

## Descri��o dos arquivos

* simple_twitter_rest_flask.py = Uma aplica��o simples em Python que atrav�s de um CEP informado busca no Twitter posts sobre a cidade pertencente ao CEP.
Ao contr�rio do exemplo abaixo neste exemplo foi utilizado OAuth 1 com a biblioteca flask_oauthlib
Foi utilizado o Framework Flask e h� tratamento de erros.

* simple_twitter_rest_no_framework.py = Uma simples demostra��o em Python de como se autentica no Twitter utilizando-se OAuth 2 e fazendo a requisi��o com urllib3 - a requisi��o foi feita ajustando-se o verbo, o header e o corpo da requisi��o.
*Como trata-se de uma simples demostra��o n�o foi realizado nenhum tratamento de erros neste arquivo em espec�fico.*

## Detalhes de desenvolvimento

* Segunda noite: 12/04/2016
1. Foram aplicadas algumas melhorias no tratamento de erros
2. Adicionado conex�o com o banco de dados MySql
3. Adicionado integra��o de busca de CEP utilizando-se o servi�o https://viacep.com.br
4. O resultado das buscas s�o inclu�dos no banco de dados

* Primeira noite: 11/04/2016
1. Configura��o do ambiente de desenvolvimento nas plataformas Windows e Linux
2. Cria��o de conta no GitHub para alocar o projeto
3. Cria��o de uma aplica��o b�sica em Python para autenticar com o Twitter via API sem framework
4. Inicio do desenvolvimento da id�ia do aplicativo utilizando-se Phyton e o framework Flask

## Instala��o

Em breve...


