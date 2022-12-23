from fastapi import FastApi
app = FastApi()
@app.get("/")
def read_root():
	return{"Hello": "World"}