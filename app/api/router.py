from fastapi import APIRouter, Response, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import httpx

from app.api.routes import jsonfile
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
        if item["key"] == "Email":
            MAILCHIMP_KEY = item["default"]

    if MAILCHIMP_KEY is None:
            return "you need to add your mailchimp api key in the app settings"
    
    mailchimp.set_config({
    "api_key": MAILCHIMP_KEY,
    "server": "us14"
    })

    try:
        response =  mailchimp.campaigns.list()
    except ApiClientError as err:
        return err.text
    campaigns = [item["settings"]["title"] for item in response["campaigns"]]
    campaigns = "\n".join(campaigns)
    return campaigns

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
