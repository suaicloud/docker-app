from fastapi import FastAPI
import socket

host = socket.gethostname()
app = FastAPI()


@app.get("/")
def read_root():
    return {"host": host}