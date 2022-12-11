FROM alpine:latest

ENV APP_PORT = "8007"

RUN apk update

RUN apk add --no-cache python3 py3-pip

RUN pip install --no-cache-dir --upgrade fastapi uvicorn

WORKDIR /code

COPY ./app /code/app

CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}