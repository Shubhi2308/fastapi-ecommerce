# from fastapi import APIRouter, Query
# from controller import productController
# from models import ProductCreate

# router = APIRouter()

# @router.post("/", status_code=201)
# async def create_product(product: ProductCreate):
#     return await productController.create_product(product)

# @router.get("/", status_code=200)
# async def get_products(
#     name: str = Query(None),
#     size: str = Query(None),
#     limit: int = Query(10),
#     offset: int = Query(0)
# ):
#     return await productController.list_products(name=name, size=size, limit=limit, offset=offset)


# router/productRouter.py

from fastapi import APIRouter, Query
from models import ProductCreate
from controller import productController

router = APIRouter()

@router.post("/", status_code=201)
async def create_product(product: ProductCreate):
    return await productController.create_product(product)

@router.get("/", status_code=200)
async def get_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = Query(10),
    offset: int = Query(0)
):
    return await productController.list_products(name=name, size=size, limit=limit, offset=offset)

