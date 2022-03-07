ARG VERSION_ALPINE=latest
FROM alpine:${VERSION_ALPINE}

# Metadata criador da imagem.
LABEL MAINTAINER="Aníbal Souza <annibalhsouza@gmail.com>"
# atualizar e instalar nginx
RUN apk --update add nginx && \
    ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log && \
    mkdir /etc/nginx/sites-enabled/ && \
    mkdir -p /run/nginx && \
    rm -rf /etc/nginx/conf.d/default.conf && \
    rm -rf /var/cache/apk/*

COPY conf.d/app.conf /etc/nginx/conf.d/app.conf

# expor aplicação em porta segura 443
EXPOSE 80 443
CMD ["nginx", "-g", "daemon off;"]