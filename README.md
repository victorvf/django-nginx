# Dockerizando Django com Postgres e Nginx

Foi desenvolvida uma aplicação simples para Estacionamento, com ênfase no estudo de Docker para ambiente de Produção

> *Próxima atualização tera o Gunicorn*

### Versões:

- Docker 18.09.3
- Django 2.1.7:latest
- Postgres 11.2:latest
- Nginx 1.15.9:latest

### Passos:

para mais informações sobre os passos 1 a 6, acesse: [Docker](https://docs.docker.com/compose/django/) ou entre em contato comigo pelo [Twitter](https://twitter.com/victorfontenele)

*1. Criar os arquivos Dockerfile, requirements.txt, docker-compose.yml*

> touch Dockerfile

> touch requirements.txt

> touch docker-compose.yml

*2. Adicionar ao Dockerfile*

```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```

*3. Adicionar ao requirements.txt*

```
Django>=2.0,<3.0
psycopg2>=2.7,<3.0
psycopg2-binary
```

*4. Adicionar ao docker-compose.yml*

```
version: '3'
services:
  db:
    image: postgres
    restart: always
    volumes:
      - ./postgres:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: admin
  app:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - ./projetoFinal:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
  web:
    image: nginx
    build:
      context: .
      dockerfile: ./nginx/Dockerfile
    ports:
      - "80:80"
    depends_on:
      - app
```

*5. Criar o Projeto*

> sudo docker-compose run web django-admin startproject composeexample .

*6. Configurar o Settings*

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PASSWORD': 'admin',
        'PORT': 5432,
    }
}
```
