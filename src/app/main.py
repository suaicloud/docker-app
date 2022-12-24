from fastapi import FastAPI
from socket import gethostname

app = FastAPI()

host = gethostname()
@app.get("/")
def read_root():
    return {"name": host}