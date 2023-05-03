from app import  models, schemas
from typing import List
from fastapi import APIRouter,HTTPException,Depends
from fastapi.responses import JSONResponse
from app.db import SessionLocal
from sqlalchemy.orm import Session
from app.models.todo import Item
from app.schemas.todo import (
    ItemRead,ItemCreate,ItemUpdate
)
from app.db import get_db

router = APIRouter()


@router.post("/create/", response_model=ItemCreate)
async def create_item(item: ItemCreate,  db: Session = Depends(get_db)):
    db_item = Item(title=item.title, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return JSONResponse(content={"message": "Item created successfully"})



@router.get("/", response_model = List[ItemRead])
async def read_item(db: Session = Depends(get_db)):
    db_item = db.query(Item).all()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/edit/{item_id}", response_model = ItemUpdate)
async def update_item(item_id: int, item: ItemUpdate,  db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
    
    db_item.title = item.title
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    # return db_item
    return JSONResponse(content={"message": "Item edited successfully"})


@router.delete("/delete/{item_id}")
async def delete_item(item_id: int,  db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return JSONResponse(content={"message": "Item deleted successfully"})