from fastapi import FastAPI
from socket import gethostname

app = FastAPI()
print('app started')

@app.get("/")
def read_root():
    return {"host": gethostname()}