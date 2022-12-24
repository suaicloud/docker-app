FROM alpine:latest

ENV APP_PORT=8015

RUN apk update

RUN apk add --ni-cache-dir --upgrade fastapi uvicorn


Copy ../
WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port ${APP_Port}