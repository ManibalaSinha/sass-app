from sqlalchemy.orm import Session
from database import SessionLocal
from app.api.v1.auth import create_user

# Create a DB session
db: Session = SessionLocal()

# Example test user
name = "Test User"
email = "test@example.com"
password = "mypassword"

user = create_user(db, name, email, password)
print("User created:", user.id, user.name, user.email)

db.close()
