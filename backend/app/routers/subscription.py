# backend/app/routers/subscription.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.subscription import Subscription
from app.services.stripe_service import create_stripe_customer, create_subscription
from app.schemas.subscription import SubscriptionResponse

router = APIRouter(prefix="/subscription", tags=["subscription"])

@router.post("/{user_id}", response_model=SubscriptionResponse)
def create_user_subscription(user_id: int, db: Session = Depends(get_db)):
    from app.models.user import User
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    customer_id = create_stripe_customer(user.email)
    subscription_id = create_subscription(customer_id, "price_your_price_id")
    sub = Subscription(user_id=user.id, stripe_customer_id=customer_id, stripe_subscription_id=subscription_id)
    db.add(sub)
    db.commit()
    db.refresh(sub)
    return sub
