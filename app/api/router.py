from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

from app.api.routes import jsonfile
from app.api import dependency as dep
from core.config import settings


api_router = APIRouter()

api_router.mount("/static", StaticFiles(directory="static"), name="static")

api_router.include_router(jsonfile.router, prefix="/integration.json", tags=["jsonD"])


class Payload(BaseModel):
    message: str
    settings: list[dict]

    class Config:
        extra = "allow"

async def processResult(message: str, settings: list[str]):
    
    mailchimp = Client()
    
    MAILCHIMP_KEY = None
    for item in settings:
        if item["label"] == "Email":
            MAILCHIMP_KEY = item["default"]

    if MAILCHIMP_KEY is None:
            return "you need to add your mailchimp api key in the app settings"
    
    mailchimp.set_config({
    "api_key": MAILCHIMP_KEY,
    "server": "us14"
    })

    message = message.lstrip().lower()
    message.
    if message.startswith("get"):
        return dep.reply(message.,"get", mailchimp)
    elif message.startswith("add"):
         return dep.reply(message,"add", mailchimp)
    else:
         return dep.help()

@api_router.post("/")
async def apipost(req: Payload):
    result = await processResult(req.message, req.settings)

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
