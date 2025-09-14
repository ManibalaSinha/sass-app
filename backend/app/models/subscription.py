# backend/app/models/subscription.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    stripe_customer_id = Column(String, nullable=False)
    stripe_subscription_id = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    user = relationship("User", backref="subscription")
