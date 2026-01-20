"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import SendNotificationRequest, SendNotificationResponse
from .service import send_notification

router = APIRouter()


@router.post("/notifications/send", response_model=SendNotificationResponse, status_code=200)
def send_notification_route(req: SendNotificationRequest) -> SendNotificationResponse:
    result = send_notification(
        recipient_id=req.recipient_id,
        channel=req.channel,
        template_id=req.template_id,
        variables=req.variables,
    )
    return SendNotificationResponse(
        notification_id=result["notification_id"],
        status=result["status"],
        queued_at=result["queued_at"],
    )
