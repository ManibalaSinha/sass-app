from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User  # your SQLAlchemy User model

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Create a new user
def create_user(db: Session, name: str, email: str, password: str):
    hashed_pw = hash_password(password)
    user = User(name=name, email=email, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
