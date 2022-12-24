from fastapi import fastAPI
from socket import gethostname


app = FastAPI()

id = gethostname()

@app.get('/')
def read_root():
  return{'id': id}