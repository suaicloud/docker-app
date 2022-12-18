FROM ubuntu:latest

ENV APP_PORT=8022

RUN apt-get update

RUN apt-get install -y python3 pip

RUN pip install fastapi uvicorn

COPY .  ./
WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port $APP_PORT
