@@ -0,0 +1,7 @@
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"lastname":"Kokorina"}
