# import os
# from dotenv import load_dotenv
# from motor.motor_asyncio import AsyncIOMotorClient

# # Load .env variables
# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")
# DB_NAME = os.getenv("DB_NAME")


# client = AsyncIOMotorClient(MONGO_URI)
# db = client[DB_NAME]
# products_collection = db["products"]
# orders_collection = db["orders"]


import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import certifi

# Load .env variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Use certifi for CA certs — solves TLS/SSL issues
client = AsyncIOMotorClient(MONGO_URI, tls=True, tlsCAFile=certifi.where())
db = client[DB_NAME]

products_collection = db["products"]
orders_collection = db["orders"]


