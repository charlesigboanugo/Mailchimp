from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from app.api.router import api_router

app = FastAPI(debug=settings.DEBUG,
               title=settings.APP_NAME,
               description=settings.APP_DESCRIPTION,
               version=settings.APP_VERSION)

app.add_middleware(CORSMiddleware, 
                   allow_origins=[
                       "https://telex.im",
                        "https://staging.telex.im",
                        "http://telextest.im",
                        "http://staging.telextest.im",
                        "https://ping.telex.im"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )

app.include_router(api_router, prefix=settings.API_PREFIX, tags=["api"])

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.head("/")
def appHead(response: Response):
    return "great"

@app.get('/')
async def home(request: Request):
    return {"home": "testing myy first fastapi app"}