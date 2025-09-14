# backend/app/schemas/subscription.py
from pydantic import BaseModel

class SubscriptionCreate(BaseModel):
    stripe_customer_id: str
    stripe_subscription_id: str

class SubscriptionResponse(BaseModel):
    id: int
    active: bool

    class Config:
        orm_mode = True
