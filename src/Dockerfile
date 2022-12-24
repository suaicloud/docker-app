FROM alpine:latest
ENV APP_PORT 8016
RUN apk update
RUN apk add --no-cache python3 py3-pip
RUN pip3 install fastapi uvicorn
COPY ./app /app
WORKDIR /app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $APP_PORT"]