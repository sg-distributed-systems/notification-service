from pydantic import BaseModel


class SendNotificationRequest(BaseModel):
    user_id: str


class SendNotificationResponse(BaseModel):
    status: str
