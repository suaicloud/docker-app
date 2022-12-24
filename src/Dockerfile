FROM alpine:latest
ENV  APP_PORT 8004
RUN apk update
CMD echo "Hello world"
RUN apk add --no-cache python3 py3-pip
RUN pip3 install fastapi uvicorn
COPY app/main.py ./app/main.py
WORKDIR /app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $APP_PORT"]