FROM ubuntu:latest

ENV APP_PORT = 8001

RUN apt-get update  

RUN apt-get add --no-cache python3 py3-pip

RUN pip3 install fastapi uvicorn

COPY . ./
WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}
