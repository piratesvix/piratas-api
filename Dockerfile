# buscando imagem linux ubuntu versão 20.04
FROM python:3.6.8-alpine3.9
# Metadata indicating an image maintainer.
LABEL maintainer="William Agostini <willsantos96@gmail.com> @willsantos96"
LABEL maintainer="Aníbal Souza <annibalhsouza@gmail.com> @ahsouza"
# determinando diretório atual no container
WORKDIR /var/www/
# adicioanr variáveis de ambiente para o grupo e usuario
ENV GROUP_ID=1000 \
    USER_ID=1000
# fazendo cópia de todo conteúdo no diretório atual para o diretório atual do container
ADD . /var/www
# instalar pacotes pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# criar o usuário 'pirata' e atribuir ao grupo de acesso ao container
RUN addgroup -g $GROUP_ID piratesvix
RUN adduser -D -u $USER_ID -G piratesvix pirata -s /bin/sh

# usuário de acesso ao container
USER pirata

# expor aplicação na porta :5000
EXPOSE 5000
# iniciar servidor gunicorn com 4 workers por núcleo no servidor e escutar na porta 5000
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]