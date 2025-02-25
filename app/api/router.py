from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.api.routes import jsonfile
from app.api import dependency as dep


api_router = APIRouter()

api_router.mount("/static", StaticFiles(directory="static"), name="static")

api_router.include_router(jsonfile.router, prefix="/integration.json", tags=["jsonD"])


class Payload(BaseModel):
    message: str
    settings: list[dict]

@api_router.post("/")
async def apipost(req: Payload):
    result = await dep.processResult(req.message, req.settings)
    result = dep.inHtml(result)
    
    data = {
        "event_name": "YOUR LISTS",
		"message":     result,
		"status":     "success",
		"username":   "CHARLES"
    }
    print(req)
    return data
   
@api_router.get("/")
async def apiHome():
    return "api home"
