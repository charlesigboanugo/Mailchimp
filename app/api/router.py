from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from mailchimp_marketing import Client
import httpx

from app.api.routes import jsonfile

api_router = APIRouter()

api_router.mount("/static", StaticFiles(directory="static"), name="static")

api_router.include_router(jsonfile.router, prefix="/integration.json", tags=["jsonD"])

mailchimp = Client()
mailchimp.set_config({
    "api_key": "775b33ecefa3a4ec4ec02eef303223c6-us14",
    "server": "us14"
})


class Payload(BaseModel):
    message: str
    settings: list[dict]

    class Config:
        extra = "allow"

def processResult(message: str, settings: list[str]):
    response = mailchimp.campaigns.list()
    campaigns = [item["settings"]["title"] for item in response["campaigns"]]
    campaigns = "\n".join(campaigns)
    return campaigns

@api_router.post("/")
async def apipost(req: Payload):
    result = processResult(req.message, req.settings)

    data = {
        "event_name": "YOUR LISTS",
		"message":    result,
		"status":     "success",
		"username":   "CHARLES"
    }
    print(req)
    return data

@api_router.get("/")
async def apiHome():
    return "api home"
