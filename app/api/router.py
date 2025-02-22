from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles

from app.api.routes import jsonfile

api_router = APIRouter()
api_router.mount("/static", StaticFiles(directory="static"), name="static")

api_router.include_router(jsonfile.router, prefix="/json", tags=["jsonD"])

@api_router.get("/")
def apiHome():
    return "api home"

