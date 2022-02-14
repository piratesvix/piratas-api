# buscando imagem linux ubuntu versão 20.04
FROM ubuntu:20.04
# Metadata indicating an image maintainer.
LABEL maintainer="William Agostini <willsantos96@gmail.com> @willsantos96"
LABEL maintainer="Aníbal Henrique <annibalhsouza@gmail.com> @ahsouza"
# atualizando pacotes do sistema e instalando modulos python 3
RUN apt update && apt install -y python3 python3-dev python3-pip

# determinando diretório atual no container
WORKDIR /var/www/piratas-api
# fazendo cópia de todo conteúdo no diretório atual para o diretório atual do container
COPY . .

# instalar pacotes pip
RUN pip3 install --no-cache-dir -r requirements.txt

# executar comando para subir servidor flask
ENTRYPOINT flask run

# expor aplicação na porta :5000
EXPOSE 5000