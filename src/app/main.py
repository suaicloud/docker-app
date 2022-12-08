from fastapi import FastAPI
import sys
import uvicorn

app = FastAPI()
server_id = None

def getargv(name):
    argv = sys.argv
    return argv[argv.index(f'--{name}') + 1]

@app.get("/")
def read_root():
    server_id = getargv("servid")
    return {
        "status": "success",
        "server_instance": f'#{server_id}'
    }

if __name__ == "__main__":
    port = getargv("port")
    uvicorn.run("main:app", host="0.0.0.0", port=port)