# Luizalabs Employee Manager Application 

Desenvolvimento de uma web app 'fictícia' em Python & Django que simulará uma aplicação que gerenciará as informações do funcionários através de uma API que permita integrá-la a outros sistemas. 
A aplicação irá ter: 

* Um painel Admin feito em Django para que possa gerenciar os dados dos empregados;
* E uma API que permita: listar, adicionar e remover os empregados (somente o Admin);

Essa versão é a v.1 do projeto. Sendo assim, uma app básica que irá receber os verbos do HTTP.

## Exemplo das URI's de Requisição (Request):

```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/

```

E o resultado do JSon (Response) deverá (exemplo):

```
[
  {
    "name": "Arnaldo Pereira",
    "email": "arnaldo@luizalabs.com",
    "department": "Architecture"
    },
    {
      "name": "Renato Pedigoni",
      "email": "renato@luizalabs.com",
      "department": "E-commerce"
    },
    {
      "name": "Thiago Catoto",
      "email": "catoto@luizalabs.com",
      "department": "Mobile"
    }
]

```

## Recursos Utilizados no Desenvolvimento da Aplicação:

- Python ~ 3.5.0;
- Pip ~ 9.0.1;
- VirtualEnv ~ 15.1.0;
- Conceito RestFul;
- Django Rest Framework ~ 3.5.4;
- Django ~ 1.8.3;
- Conceito Web & HTTP Protocol;
- IDE: Visual Code;
- Navicat Premium;
- PostMan (para testar as API's criadas);
- TDD (Test Driven Development);

## Acompanhamento do Desenvolvimento dos BackLogs do Projeto:

Caso queira saber o acompanhamento do desenvolvimento de cada backlog do projeto que está sendo
desenvolvido, basta clicar [Aqui](https://trello.com/b/p7vkH4Bs/desafio-luizalabs-employee-manager-application)

## Padrão das Rotas Criadas: 

Procurando seguir o padrão e design das API's, segue abaixo as URI's das rotas a serem desenvolvidas:

 ROTA                      |     HTTP(Verbo)   |      Descrição        | 
-------------------------  | ----------------- | --------------------- | 
/employee                  |       GET         | Selecionar Todos      | 
/employee                  |       POST        | Criar                 | 
/employee/:employee_id     |       GET         | Selecionar Por Id     | 
/employee/:employee_id/    |       PUT         | Atualizar Por Id      |    
/employee/:employee_id/    |       DELETE      | Excluir Por Id        |


## Padrão da Arquitetura do Projeto:

Como estaremos desenvolvendo usando o framework do Python - **Django** - trabalharemos com a seguinte definição de Arquitetura: MTV

- **M**: Model
- **T**: Template
- **V**: View

## Executando a Aplicação:

Para que o projeto execute de maneira satisfatória, há a necessidade de instalar os programas abaixo:

1) Instalar: Python [AQUI](https://www.python.org/downloads/)
  - Video explicando como instalar Python 3.5 [AQUI](https://www.youtube.com/watch?v=YdNiifNwt_M)

2) Instalar Django de maneira global da seguinte maneira:
  
Deverá abrir o seu cmd e digitar o seguinte comando abaixo:

```
> python -m pip install django 

```

3) Instalar o VirtualEnv de maneira global da seguinte maneira:

Deverá abrir o seu cmd e digitar o seguinte comando abaixo:

```
> python -m pip instal virtualenv

```

4) Instalar o Django Rest Framework:

Deverá abrir o seu cmd e digitar o seguinte comando abaixo:

```
> python -m pip instal djangorestframework

```

Bom, depois que tudo estiver instalado, vamos averiguar se todo o ambiente já está preparado. Para isso, basta digitar o seguinte comando abaixo:

```
> python -m pip freeze

```

Se ao digitar o comando e apresentar: Django, Pyscopg2 e Virtualenv com as suas versões é porque estão devidamente instalados no computador.

```
C:\>python -m pip freeze
Django==1.10.5
psycopg2==2.6.2
virtualenv==15.1.0
djangorestframework==3.5.4

```

## Executando os testes na Aplicação:

Para executar os testes criados na aplicação, você deverá ir até a pasta da app onde está contido o arquivo 'manage.py' e 
digitar o seguinte comando abaixo:

```
> python manage.py test

```

(Documentação em desenvolvimento....)