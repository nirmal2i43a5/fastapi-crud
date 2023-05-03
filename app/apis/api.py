from fastapi import APIRouter

from app.apis.routers import todo

api_router = APIRouter()

api_router.include_router(todo.router, prefix="/items", tags=["items"])