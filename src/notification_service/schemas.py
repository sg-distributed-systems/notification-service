"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from datetime import datetime
from typing import Dict
from uuid import UUID

from pydantic import BaseModel, Field


class SendNotificationRequest(BaseModel):
    recipient_id: str
    channel: str
    template_id: str
    variables: Dict = Field(default_factory=dict)


class SendNotificationResponse(BaseModel):
    notification_id: UUID
    status: str
    queued_at: datetime
