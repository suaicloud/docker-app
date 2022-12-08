FROM alpine:latest
RUN apk update

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"

COPY . ./
WORKDIR /app

ENV APP_PORT=8012
EXPOSE ${APP_PORT}
ENV SERVER_ID=1
CMD python main.py --port ${APP_PORT} --servid ${SERVER_ID}