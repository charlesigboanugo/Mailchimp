from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import httpx

from app.api.routes import jsonfile

api_router = APIRouter()
api_router.mount("/static", StaticFiles(directory="static"), name="static")

api_router.include_router(jsonfile.router, prefix="/integration.json", tags=["jsonD"])

@api_router.get("/")
def apiHome():
    return "api home"

class Item(BaseModel):

    class Config:
        extra = "allow"

@api_router.post("/")
async def apipost(req: Item):
    data = {
        "message": "your task was successful",
        "username": "Uptime Monitor",
        "event_name": "Uptime Check",
        "status": "success"
    }
    async with httpx.AsyncClient() as client:
        await client.post(f"https://ping.telex.im/v1/webhooks/{req.channel_id}", json=data)
    print(req)
    return {"status": "accepted"}
