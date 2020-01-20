FROM python:3.7

# Atualiza o apt-get
RUN apt-get update
RUN apt-get -y install python3-pip
RUN ln /usr/bin/python3 /usr/bin/python
RUN ln /usr/bin/pip3 /usr/bin/pip

# Variáveis de ambiente
ENV PORT=${PORT}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG=False

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
EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]





