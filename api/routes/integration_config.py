from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config import settings

router = APIRouter()

integration_json = {
        "data": {
            "date": {
                "created_at": "2025-02-19",
                "updated_at": "2025-02-19"
            },
            "descriptions": {
                "app_name": "Task Prioritizer",
                "app_description": "Detects overdue tasks and notifies team members automatically.",
                "app_logo": "https://iili.io/dmHVsZG.png",
                "app_url": "http://ec2-51-21-132-194.eu-north-1.compute.amazonaws.com",
                "background_color": "#ffffff"
            },
            "integration_category": "Monitoring & Logging",
            "integration_type": "interval",
            "is_active": True,
            "output": [
                {"label": "slack_notifications", "value": True}
            ],
            "key_features": [
                "Automatically detects overdue tasks.",
                "Notifies assigned team members.",
                "Supports multiple notification channels.",
                "Configurable alert sensitivity."
            ],
            "permissions": {
                "task_manager": {
                    "always_online": True,
                    "display_name": "Task Overdue Monitor"
                }
            },
            "settings": [
                {"label": "task_source", "type": "text", "required": True, "default": "database"},
                {"label": "overdue_threshold", "type": "number", "required": True, "default": 24},
                {"label": "notification_method", "type": "dropdown", "required": True, "default": "email", "options": ["email", "slack", "webhook"]},
                {"label": "notify_roles", "type": "multi-checkbox", "required": True, "default": "Manager", "options": ["Super-Admin", "Admin", "Manager", "Developer"]}
            ],
            "target_url": settings.SLACK_WEBHOOK_URL,
            "tick_url": settings.TICK_URL,
        }
    }

@router.get("/integration-config")
async def get_integration_json():
    return JSONResponse(content=integration_json)