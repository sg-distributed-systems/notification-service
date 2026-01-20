"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .main import send_notification
from .schemas import SendNotificationRequest, SendNotificationResponse

router = APIRouter()


@router.post("/notifications/send", response_model=SendNotificationResponse)
def send_notification_route(req: SendNotificationRequest) -> SendNotificationResponse:
    send_notification(req.user_id)
    return SendNotificationResponse(status="ok")
