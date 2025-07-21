# controller/productcontroller.py
from utils import generate_id
from database import products_collection
from models import ProductCreate
from fastapi import HTTPException

async def create_product(product: ProductCreate):
    product_id = generate_id()
    product_dict = product.dict()
    product_dict["_id"] = product_id

    try:
        await products_collection.insert_one(product_dict)
    except Exception as e:
        print(f"Error inserting product: {e}")
        raise HTTPException(status_code=500, detail="Failed to insert product")

    return {"id": product_id}


async def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    query = {}

    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    if size:
        query["sizes"] = {
            "$elemMatch": {
                "size": {"$regex": f"^{size}$", "$options": "i"}
            }
        }

    try:
        cursor = products_collection.find(query).skip(offset).limit(limit)
        data = []
        async for product in cursor:
            data.append({
                "id": str(product["_id"]),
                "name": product["name"],
                "price": product["price"],
                "sizes": product.get("sizes", [])
            })

        return {
            "data": data,
            "page": {
                "next": offset + limit,
                "limit": len(data),
                "previous": max(0, offset - limit)
            }
        }
    except Exception as e:
        print(f"Error fetching products: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch products")
