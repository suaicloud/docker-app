FROM alpine:latest

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR ./

COPY ./requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /requirements.txt
COPY ./app /app

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $APP_PORT"]
