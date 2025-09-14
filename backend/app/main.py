# backend/app/main.py
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, subscription

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="SaaS Starter App")

app.include_router(auth.router)
app.include_router(subscription.router)

@app.get("/")
def root():
    return {"message": "Welcome to SaaS App!"}
