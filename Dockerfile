FROM python:3.10


RUN apt-get update && apt-get install -y pkg-config
COPY requirements.txt /temp/requirements.txt

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
WORKDIR /app/src

