from fastapi import APIRouter
from controller import orderController
from models import OrderCreate

router = APIRouter()

@router.post("/", status_code=201)
async def create_order(order: OrderCreate):
    return await orderController.create_order(order)

@router.get("/{user_id}", status_code=200)
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    return await orderController.get_orders(user_id, limit, offset)
