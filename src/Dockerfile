RUN apk add --no-cache python3 py3-pip
RUN pip3 install fastapi uvicorn


WORKDIR /app

ENV APP_PORT=8001
CMD uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}