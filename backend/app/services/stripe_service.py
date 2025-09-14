# backend/app/services/stripe_service.py
import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_test_yourkey")

def create_stripe_customer(email: str):
    customer = stripe.Customer.create(email=email)
    return customer.id

def create_subscription(customer_id: str, price_id: str):
    subscription = stripe.Subscription.create(
        customer=customer_id,
        items=[{"price": price_id}],
        payment_behavior='default_incomplete',
        expand=["latest_invoice.payment_intent"],
    )
    return subscription.id
