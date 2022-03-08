<br>

## Piratas API

### Executando o Serviço API

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

# Utilizando o Serviço de API em container Docker

Construa uma imagem docker executando o seguinte comando:

``sh
docker build -t <nome> <dockerfile>
``

Após a imagem estiver construída, nós iremos subir a imagem para um container e expor o serviço do **piratas-api** na porta 5000

``sh
docker run -d -p 5000:5000 <nome>
``

Agora acesse http://localhost:5000 de seu navegador ou aplicativo de requisições.

<br>


## Como se interagir com o container

Primeiro inicie o container com:

```sh
docker start <id-container>
```

```sh
docker attach <id-container>
```

<br>

## Apagar Todos Containers, Imagens & Cache

```sh
docker system prune -a
```

<br>

## Apagar Todos Containers, Imagens & Cache

```sh
docker system prune -a
```
<br>

# Utilizando Docker-Compose

Utilize o comando `docker-compose up -d` para construir os serviços que estão adicionados no arquivo **docker-compose.yml** do projeto
