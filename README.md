# Luizalabs Employee Manager Application 

Desenvolvimento de uma web app 'fictícia' em Python & Django Rest Framework que simulará uma aplicação que gerenciará as informações do funcionários através de uma API que permita integrá-la a outros sistemas. 
A aplicação precisa ter: 

* Um painel Admin feito em Django para que possa gerenciar os dados dos empregados;
* E uma API que permita: listar, adicionar e remover os empregados (somente o Admin);

Essa versão é a v.1 do projeto. Sendo assim, uma app básica que irá receber os verbos do HTTP.

## Exemplo das URI's de Requisição (Request):

```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/

```

E o resultado do JSon (Response) deverá ser (exemplo):

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

- Python ~  3.8.10;
- Pip ~ 20.0.2;
- VirtualEnv ~ ?;
- Conceito RestFul;
- Django Rest Framework ~ 3.13.1;
- Django ~ 4.1.0;
- Conceito Web & HTTP Protocol;
- IDE: Visual Code;
- Navicat Premium (para fácil manipulação da base de dados - SQLite);
- PostMan (para testar as API's criadas);
- TDD (Test Driven Development - não solicitado no desafio porém tentei fazer....);

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
  - Video explicando como instalar Python 3.8 [AQUI](https://www.youtube.com/watch?v=UI2OKHxLWfg)

2) Criar um ambiente virtual usando o virtualenv do python:

Na pasta do projeto, digite: 

```
 python -m venv venvapi
```

3) Inicializar o ambiente virtual.

```
 source venvapi/bin/activate
```

4) Instalar os requisitos do projeto da seguinte maneira:
  
```
 pip -r requirements.txt
```


## Executando os testes na Aplicação:

Para executar os testes criados na aplicação, você deverá ir até a pasta da app onde está contido o arquivo 'manage.py' e 
digitar o seguinte comando abaixo:

```
 python manage.py test
```


## Resultados dos Requests via REST:

### 1) Método: GET (Selecionar Todos: http://localhost:8000/employee/ )

Antes.... execute o comando, na pasta raiz do projeto: 'api' o cmd:

```
 python manage.py runserver
```

Depois Abre a página em 

```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

E vejam a lista de todos os funcionários cadastrados abaixo: 

![image](https://user-images.githubusercontent.com/276077/150683618-e506ec0f-5281-4764-bc7f-a51179139308.png)

Request no Postman: 

![image](https://user-images.githubusercontent.com/276077/150683697-68c3dcfa-f65b-411e-878e-764d5b94c0d7.png)


### 2) Método: POST (Criar Novo: http://localhost:8000/employee/ )

Na mesma página, insira um novo cadastro nos campos abaixo e clique no botão POST. E vejam o resultado abaixo:

![image](https://user-images.githubusercontent.com/276077/150683793-d92ccb0f-e8b0-40b3-8240-e1fc40374122.png)

Agora cliquem no botão GET e vejam o resultado. Aparecerá o novo empregado na lista:

![image](https://user-images.githubusercontent.com/276077/150683824-9416d3ee-c5f6-4af1-bae9-64b5acd995a6.png)

### 3) Método: GET (By Id) (Selecionar Por Id: http://localhost:8000/employee/:employee_id/ )

Bom, agora vamos regastar um determinado funcionário através do id. E vejam o resultado abaixo:

![image](https://user-images.githubusercontent.com/276077/150683848-42f4cf3d-d42b-4fcf-a571-e1bcb2daa043.png)

### 4) Método: PUT (Atualizar Por Id: http://localhost:8000/employee/:employee_id/ )

Assim como o método acima, vamos atualizar (alterar) o cadastro e depois cliquem no botão PUT e vejam o resultado abaixo:
Note que o 'department' foi mudado para 'mobile'. 

![image](https://user-images.githubusercontent.com/276077/150684101-56ddb6f2-cf53-4d27-b8b2-f1b0ea8f44cd.png)

Os dados foram alterados com sucesso! :D

### 5) Método: DELETE (Excluir Por Id: http://localhost:8000/employee/:employee_id/ )

E enfim, o último método. Vamos excluir esse funcionário.... :( :( :( e Vejam o resultado abaixo:

![image](https://user-images.githubusercontent.com/276077/150684227-95e78c96-3fa6-431c-bad1-80bba8d06976.png)

O Funcionário foi devidademente excluído e ao listar via GET observem que o funcionário(a) não consta mais na lista:

![image](https://user-images.githubusercontent.com/276077/150684253-702a33bb-f925-4f31-b3ec-2bb30c276ab7.png)

## Observações Finais:

* Nunca tinha programado na minha vida em Python & Django. Porém, não senti dificuldade em aprender a linguagem uma vez que é uma linguagem de fácil interpretação e muito intuitiva. Me lembrou um pouco, por exemplo: Node.Js. Uma vez que há a necessidade de baixar pacotes via pip (no Node.Js é via npm) e como já programo em Node.Js ficou fácil a manipulação.

* E outro ponto que curti demais é o DRF (Django Rest Framework). A questão, por exemplo, do 'makemigrations' e 'migrate' para atualizar o modelo para a BD, me lembrou muito os comandos do Entity Framework.
Curti tanto programar em Python & Django que irei escrever um tutorial sobre a linguagem e o framework. :D :D

* O único ponto negativo para mim foi a dificuldade em instalar os programar uma vez que o meu S.O é o Windows. Porém, como eu já programei em CentOs (RED HAT) então.... acredito que é questão de costume.

* Procurei ler a documentação do Django e ver alguns cursos de Python para entender um pouco a sintaxe da linguagem.
A questão do TDD.... se vocês executarem o teste... infelizmente vai executar com erros.... eu tentei e tentei ver onde eu falhei.. mas.. infelizmente, não consegui encontrar o erro.... (mas, como não foi solicitado acredito que seja um plus eu ter tentado!! :D )


* Bom... espero que tenham gostado. Vou fazer a versão dessa app em Node. E caso vocês queiram ver... bastam clicar [AQUI](https://github.com/glaucia86/employee-manager-app-node-v1)

## Atualizações 2022

* Os requisitos/códigos foram atualizados para rodar com uma versão mais recente de python e django. 

* Os testes foram atualizados e estão funcinonando. 

* O Readme foi atualizado para exibir as imagens do request e atualizar o passo a passo da instalação dos requisitos do projeto. 
