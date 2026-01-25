# !/usr/bin/env python3
"""e4.py

Another example module in the e4 framework. A python framework example file.
Demonstrates FastAPI - a modern, fast (high-performance) web framework for
building APIs with Python 3.7+ based on standard Python type hints.

"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize the FastAPI app
app = FastAPI(
    title="E4 API Example",
    description="A simple FastAPI demonstration",
    version="1.0.0"
)

# Pydantic model for request/response validation
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int = 1

# In-memory storage for demo purposes
items_db: dict[int, Item] = {}
item_counter = 0

# Root endpoint
@app.get("/")
def read_root():
    """Welcome endpoint."""
    return {"message": "Welcome to the E4 FastAPI Example!"}

# GET all items
@app.get("/items")
def get_items():
    """Retrieve all items."""
    return {"items": items_db}

# GET single item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a specific item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item": items_db[item_id]}

# POST create new item
@app.post("/items")
def create_item(item: Item):
    """Create a new item."""
    global item_counter
    item_counter += 1
    items_db[item_counter] = item
    return {"item_id": item_counter, "item": item}

# PUT update existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return {"item_id": item_id, "item": item}

# DELETE an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items_db.pop(item_id)
    return {"message": "Item deleted", "item": deleted_item}


if __name__ == "__main__":
    import uvicorn
    # Run the server: uvicorn e4:app --reload
    uvicorn.run(app, host="127.0.0.1", port=8000)
