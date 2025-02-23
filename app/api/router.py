from fastapi import APIRouter, Response, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import httpx

from app.api.routes import jsonfile

api_router = APIRouter()

api_router.mount("/static", StaticFiles(directory="static"), name="static")

api_router.include_router(jsonfile.router, prefix="/integration.json", tags=["jsonD"])

mailchimp = Client()
mailchimp.set_config({
    "api_key": "c48af55456078f2e19cbf1ce309dee34-us14",
    "server": "us14"
})


class Payload(BaseModel):
    message: str
    settings: list[dict]

    class Config:
        extra = "allow"

async def processResult(message: str, settings: list[str]):

    """try:
        response =  await mailchimp.campaigns.list()
    except ApiClientError as err:
        return err"""
    
    """campaigns = [item["settings"]["title"] for item in response["campaigns"]]
    campaigns = "\n".join(campaigns)
    return campaigns"""
    return "great"

@api_router.post("/")
async def apipost(req: Request, res: Response):
    """result = await processResult(req.message, req.settings)"""

    data = {
        "event_name": "YOUR LISTS",
		"message":    "result",
		"status":     "success",
		"username":   "CHARLES"
    }
    print(req)
    print(req.headers)
    print(req.url)
    return RedirectResponse("https://goal.com", status_code=302)

@api_router.get("/")
async def apiHome():
    return "api home"
