# !/usr/bin/env python3
"""e3.py

A python framework example file.
Demonstrates FastAPI - a modern, fast (high-performance) web framework for
building APIs with Python 3.7+ based on standard Python type hints.

To run: uvicorn e3:app --reload
Install: pip install fastapi uvicorn
"""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

# Create the FastAPI application instance
app = FastAPI(
    title="My FastAPI Example",
    description="A simple API demonstrating FastAPI features",
    version="1.0.0"
)

# Pydantic model for request/response validation
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

# In-memory database (for demonstration)
items_db: dict[int, Item] = {}
item_id_counter = 1


# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint."""
    return {"message": "Welcome to FastAPI!", "docs": "/docs"}


# GET all items
@app.get("/items")
def get_items(skip: int = 0, limit: int = Query(default=10, le=100)):
    """Retrieve all items with pagination."""
    items_list = list(items_db.items())[skip:skip + limit]
    return {"items": [{"id": k, **v.model_dump()} for k, v in items_list]}


# GET single item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a single item by its ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items_db[item_id].model_dump()}


# POST create new item
@app.post("/items", status_code=201)
def create_item(item: Item):
    """Create a new item."""
    global item_id_counter
    items_db[item_id_counter] = item
    response = {"id": item_id_counter, **item.model_dump()}
    item_id_counter += 1
    return response


# PUT update existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return {"id": item_id, **item.model_dump()}


# DELETE an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item by its ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
