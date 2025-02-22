from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from app.api.router import api_router

app = FastAPI(debug=settings.DEBUG,
               title=settings.APP_NAME,
               description=settings.APP_DESCRIPTION,
               version=settings.APP_VERSION)

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(api_router, prefix=settings.API_PREFIX, tags=["api"])

@app.get('/')
async def home():
    return {"home": "testing my first fastapi app"}