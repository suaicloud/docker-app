FROM alpine:latest

RUN apk update
RUN apk add --no-cache python3 py3-pip
RUN pip3 install fastapi "uvicorn[standart]"

CMD echo "Hello world"

WORKDIR /app
COPY ./app /app

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $APP_PORT"]
