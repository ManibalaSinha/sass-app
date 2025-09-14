from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    subscriptions = relationship("Subscription", back_populates="user")
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
