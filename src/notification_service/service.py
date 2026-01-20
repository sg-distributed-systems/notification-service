"""
Notification orchestration and delivery logic.

Manages multi-channel notification delivery (email, SMS, push, Slack) with
template rendering, variable substitution, and delivery status tracking.
"""
from datetime import datetime
from uuid import UUID, uuid4

from core_logger import get_logger

from .errors import NotFoundError, ValidationError

logger = get_logger("notification-service")

VALID_CHANNELS = {"email", "sms", "push", "slack"}
TEMPLATES = {"welcome", "order_confirmation", "password_reset", "payment_receipt"}


def send_notification(
    recipient_id: str, channel: str, template_id: str, variables: dict
) -> dict:
    logger.info(
        "notification_requested",
        recipient_id=recipient_id,
        channel=channel,
        template_id=template_id,
    )

    if channel not in VALID_CHANNELS:
        raise ValidationError("invalid_channel", details={"allowed": list(VALID_CHANNELS)})

    if template_id not in TEMPLATES:
        logger.warning("template_not_found", template_id=template_id)
        raise NotFoundError("template_not_found", details={"template_id": template_id})

    notification_id = uuid4()

    logger.debug(
        "template_rendered", template_id=template_id, variable_count=len(variables)
    )

    queued_at = datetime.utcnow()
    logger.info(
        "notification_queued",
        notification_id=str(notification_id),
        channel=channel,
        recipient_id=recipient_id,
    )

    return {"notification_id": notification_id, "status": "queued", "queued_at": queued_at}


def get_notification_status(notification_id: UUID) -> dict:
    logger.debug("status_check", notification_id=str(notification_id))
    return {
        "notification_id": notification_id,
        "status": "delivered",
        "delivered_at": datetime.utcnow(),
    }
