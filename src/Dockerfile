FROM alpine:latest

ENV APP_PORT = 8014

RUN apk update

CMD echo "Hello world"
RUN apk add --no-cache python3 py3-pip

RUN pip3 install --no-cache-dir --upgrade fastapi uvicorn


COPY . ./

WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}
