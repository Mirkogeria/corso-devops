# OrderFlow - Order Service
from fastapi import FastAPI
import os

app = FastAPI(title="OrderFlow - Order Service")

orders = []

@app.get("/health")
def health():
    return {"status": "healthy", "service": os.getenv("SERVICE_NAME", "order-service")}

@app.get("/api/orders")
def list_orders():
    return {"orders": orders, "total": len(orders)}

@app.post("/api/orders", status_code=201)
def create_order(customer: str, product: str):
    order = {"id": len(orders) + 1, "customer": customer, "product": product, "status": "pending"}
    orders.append(order)
    return order

