from fastapi import APIRouter
from datetime import datetime

from core.config import mysettings


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
                        "app_description": mysettings.APP_DESCRIPTION,
                        "app_logo": f"{mysettings.BASE_URL}/static/stackerx.png",
                        "app_name": mysettings.APP_NAME,
                        "app_url": mysettings.BASE_URL,
                        "background_color": "#A6CDE0"
                    },
                    "integration_category": "Marketing Automation",
                    "integration_type": "modifier",
                    "is_active": False,
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
                    "target_url": f'{mysettings.BASE_URL}{mysettings.API_PREFIX}'
                }
            }
  
  return jsonData
  