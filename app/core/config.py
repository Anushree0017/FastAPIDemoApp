from pydantic_settings import BaseSettings
import os

import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Info
    PROJECT_NAME: str = "FASTAPI-DEMO"
    APP_NAME: str = "FASTAPI DEMO APP"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 4000

    # PostgreSQL
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    # RabbitMQ
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str

    # Redis
    REDIS_URL: str

    # Constructed URLs
    DATABASE_URL: str
    CELERY_BROKER_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"   # prevents validation errors

settings = Settings()
