FROM alpine:latest

RUN apk update
RUN apk add --no-cache python3 py3-pip

CMD echo "Hello world"
RUN pip3 install fastapi uvicorn
COPY ./app/app
WORKDIR /app


ENV APP_PORT = 8009
CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}
