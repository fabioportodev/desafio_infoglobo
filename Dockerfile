FROM python:3.7

# Define os argumentos
ARG PORT
ARG SECRET_KEY
ARG DEBUG
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

# Atualiza o apt-get
#RUN apt-get update && apt-get -y install python3-pip
#RUN ln /usr/bin/python3 /usr/bin/python && ln /usr/bin/pip3 /usr/bin/pip

# Variáveis de ambiente
ENV PORT=${PORT}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}

# Criar diretórios
RUN mkdir /app
RUN mkdir /app/base

# Selecionando o diretório de trabalho
WORKDIR /app

# Copiando requirements.txt
COPY requirements.txt /app/

#Atualizar o pip
RUN pip install --upgrade pip

# Instalar os pacotes listados no requirements.txt apenas se forem originados do site informado
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Cria um usuario
RUN useradd python

# Copiar o conteúdo do diretório atual para o conteiner em /app
COPY --chown=python . /app

# Muda o usuário
USER python

#Porta de exposição
EXPOSE ${PORT}

# Executar o arquivo principal do projeto quando o conteiner for iniciado
CMD python manage.py runserver 0.0.0.0:${PORT}





