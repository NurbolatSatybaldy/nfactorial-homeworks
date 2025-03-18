from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/{path:path}")
async def handle_get(path: str, request: Request):
    return JSONResponse({
        "method": request.method,
        "path": path,
        "headers": dict(request.headers)
    })

@app.post("/{path:path}")
async def handle_post(path: str, request: Request):
    body = await request.body()
    return JSONResponse({
        "method": request.method,
        "path": path,
        "headers": dict(request.headers),
        "body": body.decode('utf-8')
    })

@app.put("/{path:path}")
async def handle_put(path: str, request: Request):
    body = await request.body()
    return JSONResponse({
        "method": request.method,
        "path": path,
        "headers": dict(request.headers),
        "body": body.decode('utf-8')
    })

@app.delete("/{path:path}")
async def handle_delete(path: str, request: Request):
    return JSONResponse({
        "method": request.method,
        "path": path,
        "headers": dict(request.headers)
    })
