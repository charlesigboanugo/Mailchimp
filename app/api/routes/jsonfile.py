from fastapi import APIRouter
from datetime import datetime

from core.config import settings


router = APIRouter()

@router.get("/")
def getJson():
  currentDate = datetime.now()
  jsonData = {
                "data": {
                    "date": {
                        "created_at": "2025-2-22",
                        "updated_at": f"{currentDate.year}-{currentDate.month}-{currentDate.day}"
                    },
                    "author": "Charles Igboanugo",
                    "descriptions": {
                        "app_description": settings.APP_DESCRIPTION,
                        "app_logo": "http://ec2-16-171-113-126.eu-north-1.compute.amazonaws.com/static/favicon.ico",
                        "app_name": settings.APP_NAME,
                        "app_url": settings.BASE_URL,
                        "background_color": "#A6CDE0"
                    },
                    "integration_category": "Marketing Automation",
                    "integration_type": "output",
                    "is_active": False,
                    "output": [
                        {
                            "label": "output_channel_1",
                            "value": True
                        },
                        {
                            "label": "output_channel_2",
                            "value": True
                        }
                    ],
                    "key_features": [
                        "Super Easy",
                        "Fast",
                        "Secure",
                        "Reliable"
                    ],
                    "permissions": {
                        "monitoring_user": {
                            "always_online": True,
                            "display_name": "Performance Monitor"
                        }
                    },
                    "settings": [
                        {
                            "label": "Name",
                            "type": "text",
                            "required": True,
                            "default": ""
                        },
                        {
                            "label": "Email",
                            "type": "text",
                            "required": True,
                            "default": ""
                        },
                    ],
                    "target_url": f'{settings.BASE_URL}{settings.API_PREFIX}'
                }
            }
  return jsonData
  