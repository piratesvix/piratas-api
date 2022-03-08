<br>

## Piratas API

### Utilizar o Serviço de API localmente

  **API** (Application Programming Interface) é um conjunto de rotinas e padrões que facilitam a comunicação e troca de informações entre sistemas.

<br>
<br>

Crie um ambiente

```sh
py -3 -m venv venv
```

Ativar ambiente

```sh
venv \scripts\activate
```

Instalar depedências 

```sh
pip install -r requirements.txt
```

Adicionar variável de ambiente `FLASK_APP` e definir o nome do aplicativo associado ao arquivo do servidor Flask

```sh
export FLASK_APP=main
```

Executar servidor em Python utilizando Framework Flask

```sh
flask run
```
<br>
<br>

# Utilizando o Serviço da API em container Docker

Construa uma imagem docker executando o seguinte comando:

``sh
docker build -t <nome> <dockerfile>
``

Após a imagem estiver construída, nós iremos subir a imagem para um container e expor o serviço do **piratas-api** na porta 5000

``sh
docker run -d -p 5000:5000 <nome>
``

Agora acesse http://piratesvix; ou http://ip_do_container;  de seu navegador ou aplicativo de requisições.

<br>

## Como Se Interagir Com o Container

Primeiro inicie o container com:

```sh
docker start <id-container>
```

```sh
docker attach <id-container>
```

<br>
<br>

## Apagar Todos Containers, Imagens & Cache

```sh
docker system prune -a
```
<br>

# Construír Todo Projeto

Utilize o comando `docker-compose up -d` para construir os serviços que estão adicionados no arquivo **docker-compose.yml** do projeto

<br><br>

# Utilizando o Serviço do MongoDB em Container Docker

```sh
docker exec -it mongodb bash
```

<br>

1. Após entrar no container, efetue login da sua conta administrativa root do MongoDB

```sh
 mongo -u mongodbuser -p
```

<br>

1. Crie e use um Banco de Dados nomeado de `pirates-api` com o seguinte comando:

```sh
 mongodb> use pirates-api;
```

<br>

3. Adicionar um usuário administrativo para o **MongoDB**:

  ```sh
  db.createUser({user: 'root', pwd: '12345', roles: [{role: 'readWrite', db: 'piratas-api'}]})
  ```

<br>

1. Efetuar login de usuário autenticado no banco de dados:
  
  ```sh
  mongo -u root -p 12345 --authenticationDatabase pirates-api
  ```