from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config import settings

router = APIRouter()

integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-21",
      "updated_at": "2025-02-21"
    },
    "descriptions": {
      "app_name": "telex-uptime-monitor",
      "app_description": "Simple uptime integration",
      "app_logo": "https://iili.io/dmHVsZG.png",
      "app_url": "ec2-51-21-132-194.eu-north-1.compute.amazonaws.com",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "modifier",
    "integration_category": "Monitoring & Logging",
    "key_features": [
      "monitor apps",
      "send notifications"
    ],
    "author": "Malach Salama",
    "settings": [
      {
        "label": "Slack Channel",
        "type": "text",
        "required": True,
        "default": "#devops-alert"
      },
      {
        "label": "Event Type",
        "type": "dropdown",
        "required": True,
        "default": "ci_pipeline",
        "options": [
          "ci_pipeline",
          "cd_pipeline",
          "deployment",
          "error"
        ]
      },
      {
        "label": "Include Logs",
        "type": "checkbox",
        "required": True,
        "default": "true"
      },
      {
        "label": "Message Format",
        "type": "text",
        "required": True,
        "default": "Basic"
      },
      {
        "label": "Time Interval",
        "type": "dropdown",
        "required": True,
        "default": "Immediate",
        "options": [
          "Immediate",
          "Every 5 mins",
          "Hourly"
        ]
      }
    ],
    "target_url": settings.SLACK_WEBHOOK_URL,
    "tick_url": settings.TICK_URL,
  }
}

@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)