FROM ubuntu:latest
LABEL author="Vladislav Polshchikov" version="1.0"
ENV  APP_PORT="8021"
RUN apt-get update 
RUN   apt-get install -y python3 
RUN    apt-get -y install python3-pip
RUN    pip3 install fastapi 
RUN    pip3 install "uvicorn[standard]" 

WORKDIR /home
COPY ./app home/app
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $APP_PORT"]