from fastapi import APIRouter
from datetime import datetime

from core.config import settings


router = APIRouter()

@router.get("/")
def getJson():
  currentDate = datetime.now()
  """jsonData = {
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
  jsonData = {
        "data": {
            "date": {
            "created_at": "2025-02-06",
            "updated_at": "2025-01-28"
            },
            "descriptions": {
            "app_name": "stackerX",
            "app_description": "good and great",
            "app_logo": "http://ec2-16-171-113-126.eu-north-1.compute.amazonaws.com/static/stackerx.png",
            "app_url": "http://ec2-16-171-113-126.eu-north-1.compute.amazonaws.com",
            "background_color": "#fff"
            },
            "is_active": True,
            "integration_type": "modifier",
            "integration_category": "Marketing Automation",
            "key_features": [
            "great easy"
            ],
            "author": "CHARLES",
            "settings": [
            {
                "label": "password",
                "type": "text",
                "required": True,
                "default": "password"
            },
            {
                "label": "name",
                "type": "text",
                "required": True,
                "default": "gabriel"
            },
            {
                "label": "second name",
                "type": "text",
                "required": True,
                "default": "james"
            }
            ],
            "target_url": "http://ec2-16-171-113-126.eu-north-1.compute.amazonaws.com/api/v1",
            "tick_url": "http://ec2-16-171-113-126.eu-north-1.compute.amazonaws.com/api/v1"
        }
    }"""
  jsonData = {
        "data": {
            "date": {
            "created_at": "2025-02-06",
            "updated_at": "2025-01-28"
            },
            "descriptions": {
            "app_name": "stackerX",
            "app_description": "good and great",
            "app_logo": "https://mailchimp-hqu1.onrender.com/static/stackerx.png",
            "app_url": "https://mailchimp-hqu1.onrender.com/",
            "background_color": "#fff"
            },
            "is_active": True,
            "integration_type": "modifier",
            "integration_category": "Marketing Automation",
            "key_features": [
            "great easy"
            ],
            "author": "CHARLES",
            "settings": [
            {
                "label": "password",
                "type": "text",
                "required": True,
                "default": "password"
            },
            {
                "label": "name",
                "type": "text",
                "required": True,
                "default": "gabriel"
            },
            {
                "label": "second name",
                "type": "text",
                "required": True,
                "default": "james"
            }
            ],
            "target_url": "https://mailchimp-hqu1.onrender.com/api/v1",
            "tick_url": "https://mailchimp-hqu1.onrender.com/api/v1"
        }
    }
  return jsonData
  