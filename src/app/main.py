from fastapi import FastAPI
import socket

app = FastAPI()

host = socket.gethostname()

@app.get("/")
def read_root():
    return {"Host Name": host}