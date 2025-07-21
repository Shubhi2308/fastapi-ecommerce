from fastapi import FastAPI
from router import productRouter, orderRouter

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to E-Commerce API"}

app.include_router(productRouter.router, prefix="/products", tags=["Products"])
app.include_router(orderRouter.router, prefix="/orders", tags=["Orders"])
