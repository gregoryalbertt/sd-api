# Consulta de Despesas da Universidade Federal de Alagoas - Ufal

Para rodar o servidor, execute o comando: 
$ python manager.py runserver

O acesso a pagina da web é feita atraves do link: http://127.0.0.1:8000/despesas-view \\

A aplicaçao possui uma API que permite acessar os dados e adicionar comentários.
Para isso, utilize para acessar: \\

$ curl -X GET http://127.0.0.1:8000/Despesas/ \\

Para deletar um dado: \\

$ curl -X DELETE --header "Accept: application/json" http://127.0.0.1:8000/Despesas/{id}

Para postar:

$ curl -H 'Content-Type: application/json' \
-X POST http://127.0.0.1:8000/Despesas \
-d '{"comentario": "Insira seu comentario"}'

Para editar:

$ curl -H 'Content-Type: application/json' \
-X UPDATE http://127.0.0.1:8000/Despesas \
-d '{"comentario": "Edite seu comentario"}'

