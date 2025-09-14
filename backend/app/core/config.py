from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "SaaS App API"
    API_V1_STR: str = "/api/v1"

    # Security
    SECRET_KEY: str = Field(default="change-me", description="JWT secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24h
    ALGORITHM: str = "HS256"

    # Database
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "saas"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"

    # Stripe (optional now)
    STRIPE_SECRET_KEY: Optional[str] = None
    STRIPE_WEBHOOK_SECRET: Optional[str] = None

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()

