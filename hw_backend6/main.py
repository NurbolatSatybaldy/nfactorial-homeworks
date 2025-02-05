from fastapi import FastAPI
from db import init_tables
from routers.auth_routes import router as auth_router
from routers.flowers_routes import router as flowers_router
from routers.cart_routes import router as cart_router

app = FastAPI()
init_tables()
app.include_router(auth_router)
app.include_router(flowers_router)
app.include_router(cart_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
