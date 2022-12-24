From alpine:latest

ENV APP_PORT = 8003

RUN apk update

RUN apk add --no-cache python3 py3-pip

RUN pip3 install --no-cache-dir --upgrade fastapi uvicorn

COPY . ./

WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}