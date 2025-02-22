from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.api.routes import jsonfile

api_router = APIRouter()
api_router.mount("/static", StaticFiles(directory="static"), name="static")

api_router.include_router(jsonfile.router, prefix="/integration.json", tags=["jsonD"])

@api_router.get("/")
def apiHome():
    return "api home"

class Item(BaseModel):
    key: str
    value: str

    class Config:
        extra = "allow"

@api_router.post("/")
def apipost(req: Item):
    print(req)
    return {"status": "accepted"}
