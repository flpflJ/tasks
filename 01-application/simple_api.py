import socket
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def simple_get():
    hostname = socket.gethostname()
    addr = socket.gethostbyname(hostname)
    author_name = os.getenv('AUTHOR', 'UNKNOWN')
    return {
        "hostname": hostname,
        "addr": addr,
        "author_name": author_name
    }
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host="0.0.0.0")
