from pydantic import BaseModel
import sqlite3

# Pydantic model

from models import *

# Connect and create table (if not exists)
def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        """)
        conn.commit()

create_table()

def insert_item(item: Item):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item.name, item.price))
        item.id = cursor.lastrowid
        conn.commit()
        return item

def get_items():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price FROM items")
        rows = cursor.fetchall()
        return [Item(id=row[0], name=row[1], price=row[2]) for row in rows]

def delete_item(item_id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
        conn.commit()
        return {"detail": f"Item {item_id} deleted successfully"}

def update_item(item_id: int, item: Item):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE items SET name = ?, price = ? WHERE id = ?", (item.name, item.price, item_id))
        conn.commit()
        item.id = item_id
        return item