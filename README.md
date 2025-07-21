🛒 FastAPI E-Commerce Backend

A modern and minimal backend API for an e-commerce platform built using FastAPI, MongoDB, and Python. This project allows users to create and list products, place orders, and fetch order — all with proper validation and pagination support.

---

🚀 Features

- 📦 Add and list products with filtering by name and size
- 🧾 Place orders and calculate total prices
- 🔍 Get all orders for a specific user
- 📄 Auto-generated API docs via Swagger and ReDoc
- 🧪 Clean, modular, and scalable codebase

---

📁 Project Structure

├── controller/ 
│ ├── productController.py    # Business logic for products
│ └── orderController.py      # Business logic for orders
│
├── router/
│ ├── productRouter.py         # Product API endpoints
│ └── orderRouter.py           # Order API endpoints
│
├── database.py               # MongoDB connection and collections
├── models.py                 # Pydantic models for request validation
├── utils.py                  # Utility to generate random IDs
├── main.py                   # Entry point of the FastAPI app
├── .env                      # Environment variables (Mongo URI & DB name)
└── README.md               # Project documentation

--------

⚙️ Set-up Installations

1. Clone the Repository

git clone https://github.com/<your-username>/fastapi-ecommerce.git
cd fastapi-ecommerce

2. Create .env File

MONGO_URI=mongodb+srv://<username>:<password>@cluster-url/
DB_NAME=ecommerce

3. Install Dependencies

pip install fastapi uvicorn pymongo python-dotenv

Or use a requirements.txt:

fastapi
uvicorn
pymongo
python-dotenv
motor

4. Run the Server

uvicorn main:app --reload

-----

🧪 API Endpoints Overview

👕 Products

POST /products/ – Create a product

GET /products/ – List products with optional filters: name, size, limit, offset

📦 Orders

POST /orders/ – Create an order

GET /orders/{user_id} – List all orders for a user

---

📬 Contact
For any issues or queries, open an issue or 
email at singhal.shubhi.2002@gmail.com.
