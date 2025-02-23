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


import httpx

API_KEY = "3adbfbfa113236a5b990dd0f920972cd-us14"
SERVER_PREFIX = "us14"  # Adjust based on your Mailchimp account configuration

async def processResult(message: str, settings: list[str]):
    url = f"https://{SERVER_PREFIX}.api.mailchimp.com/3.0/campaigns"
    headers = {
        "Authorization": f"apikey {API_KEY}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        return response.json()
    """{"status": response.status_code, "data": response.json()}"""


"""mailchimp = Client()
mailchimp.set_config({
    "api_key": "31d331d9888fd4d2bee07fa090dcf5e4-us14",
    "server": "us14"
})"""


class Payload(BaseModel):
    message: str
    settings: list[dict]

    class Config:
        extra = "allow"

"""async def processResult(message: str, settings: list[str]):

    try:
        response =  await mailchimp.campaigns.list()
    except ApiClientError as err:
        return err.text
    campaigns = [item["settings"]["title"] for item in response["campaigns"]]
    campaigns = "\n".join(campaigns)
    return campaigns"""

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
