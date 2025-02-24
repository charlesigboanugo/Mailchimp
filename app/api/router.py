import asyncio
import re
from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from mailchimp_marketing import Client

from app.api.routes import jsonfile
from app.api import dependency as dep
from core.config import mysettings


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
        if item["label"] == "api key":
            MAILCHIMP_KEY = item["default"]
    if MAILCHIMP_KEY is None:
            return "you need to add your mailchimp api key in the app settings"
    mailchimp.set_config({
    "api_key": MAILCHIMP_KEY,
    "server": "us14"
    })
    message = re.sub(r'</?p>', '', message)
    message = message.lstrip().lower()
    if message.startswith("get"):
        message = " ".join(message[3:].split())
        result = await dep.reply(message, 0, mailchimp)
        return result
    elif message.startswith("add"):
        message = " ".join(message[3:].split())
        result = await dep.reply(message, 1, mailchimp)
        return result
    else:
         result = await dep.help(help_type="full")
         return result

@api_router.post("/")
async def apipost(req: Payload):
    result = await processResult(req.message, req.settings)

    data = {
        "event_name": "YOUR LISTS",
		"message":     "<h1 style='font-size: 25px;color: purple;'>Response<h1>\n" + f"<p style='border-left: solid green 7px; padding: 20px; background-color: #090909; color: white;'>{result}<p>",
		"status":     "success",
		"username":   "CHARLES"
    }
    print(req)
    return data
   
@api_router.get("/")
async def apiHome():
    return "api home"
