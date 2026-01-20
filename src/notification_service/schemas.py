"""
Pydantic models for API request and response validation.

Defines data transfer objects used for request parsing and response
serialization in the API layer.
"""
from pydantic import BaseModel


class SendNotificationRequest(BaseModel):
    user_id: str


class SendNotificationResponse(BaseModel):
    status: str
