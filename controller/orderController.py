# controller/orderController.py

from database import db
from utils import generate_id
from database import orders_collection, products_collection
from models import OrderCreate
from fastapi import HTTPException

async def create_order(order: OrderCreate):
    order_id = generate_id()
    items = order.items
    total = 0.0
    validated_items = []

    for item in items:
        product = await products_collection.find_one({"_id": item.productId})
        if not product:
            raise HTTPException(status_code=404, detail=f"Product ID {item.productId} not found")

        validated_items.append({
            "productId": item.productId,
            "qty": item.qty
        })

        total += product["price"] * item.qty

    order_doc = {
        "_id": order_id,
        "userId": order.userId,
        "items": validated_items,
        "total": round(total, 2)
    }

    try:
        await orders_collection.insert_one(order_doc)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to create order")

    return {"id": order_id}


async def get_orders(user_id: str, limit: int, offset: int):
    try:
        cursor = orders_collection.find({"userId": user_id}).skip(offset).limit(limit)
        data = []

        async for order in cursor:
            order_items = []
            for item in order["items"]:
                product = await products_collection.find_one({"_id": item["productId"]})
                if product:
                    order_items.append({
                        "productDetails": {
                            "name": product["name"],
                            "id": product["_id"]
                        },
                        "qty": item["qty"]
                    })

            data.append({
                "id": order["_id"],
                "items": order_items,
                "total": order["total"]
            })

        return {
            "data": data,
            "page": {
                "next": offset + limit,
                "limit": limit,
                "previous":  offset - limit
            }
        }
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to fetch orders")
