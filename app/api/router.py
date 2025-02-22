from fastapi import APIRouter

from app.api.routes import jsonfile

api_router = APIRouter()

api_router.include_router(jsonfile.router, prefix="/json", tags=["jsonD"])

@api_router.get("/")
def apiHome():
    return "api home"

