from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import HTMLResponse
import bl
from models import *

# Create FastAPI instance
app = FastAPI(title="Example API", description="A simple FastAPI with Swagger UI", version="1.0")


@app.get("/items/")
def get_all():
    result = bl.get_items()
    return {"result": result}

# Define a POST endpoint
@app.post("/items/")
def create_item(item: Item):
    bl.insert_item(item)
    return {"message": "item successfully added"}

@app.delete("/delete-item")
def read_root():
    return {"message": "item deleted"}

@app.put("/update-item")
def read_root():
    return {"message": "item updated"}

@app.get("/sum")
def sum_two_get(a: int, b: int):
    result = bl.sum_two(a, b)
    return {"sum": result}

class TwoNumbers(BaseModel):
    a: int
    b: int

@app.post("/sum-post")
def sum_two_post(two_numbers: TwoNumbers):
    result = bl.sum_two(two_numbers.a, two_numbers.b)
    return {"sum": result}

@app.get("/get-entities")
def get_entities(text: str):
    print(f"========= input get_entities: {text}")
    result = bl.get_entities(text)
    return {"entities": result}

@app.get("/get-person")
def get_person(text: str):
    print(f"========= input get_person: {text}")
    result = bl.get_person(text)
    return {"people": result}
