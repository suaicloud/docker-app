FROM alpine:latest

ENV APP_PORT = 8016

RUN apk update

RUN apk add --no-cache python py3-pip

RUN pip3 install --no-cache-dir --upgrade fastapi uvicorn

COPY . ./
WDRKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port${APP_PORT}