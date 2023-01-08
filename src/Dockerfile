FROM alpine:latest

ARG APP_PORT=8007
ENV  APP_PORT="${APP_PORT}"

RUN apk update
RUN apk add --no-cache python3 py3-pip
RUN pip3 install fastapi uvicorn

COPY src/main.py ./app/main.py

WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}