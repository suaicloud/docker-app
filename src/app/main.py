from fastapi import FastAPI
from socket import gethostname

app = FastApi()

id = gethostname()

@app.get("/")
def read_root():
	return {"id": id}
