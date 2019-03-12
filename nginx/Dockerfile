FROM nginx
RUN apt-get update -qq && apt-get -y install apache2-utils
ENV DJANGO_ROOT /var/www/projetoFinal
WORKDIR $DJANGO_ROOT
RUN mkdir -p log
COPY nginx/app.conf /tmp/docker_example.nginx
RUN envsubst '$DJANGO_ROOT' < /tmp/docker_example.nginx > /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD [ "nginx", "-g", "daemon off;" ]
