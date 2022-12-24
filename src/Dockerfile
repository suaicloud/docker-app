FROM alpine:latest
ENV APP_PORT = 8003
RUN apk update
RUN apk add --no--cache python3 py3-pip
RUN pip3 install --no-cache-dir --upgrade fastapi uvicorn
COPY app/main.py ./app/main.py
WORKDIR /app
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $APP_PORT"] 
