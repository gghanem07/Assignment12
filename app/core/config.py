# app/core/config.py
import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import Optional, List


class Settings(BaseSettings):
    # =========================
    # Database settings
    # =========================
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/fastapi_db"
    )

    TEST_DATABASE_URL: str = os.getenv(
        "TEST_DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/fastapi_test_db"
    )

    # =========================
    # JWT Settings
    # =========================
    JWT_SECRET_KEY: str = os.getenv(
        "JWT_SECRET_KEY",
        "your-super-secret-key-change-this-in-production"
    )

    JWT_REFRESH_SECRET_KEY: str = os.getenv(
        "JWT_REFRESH_SECRET_KEY",
        "your-refresh-secret-key-change-this-in-production"
    )

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    )

    REFRESH_TOKEN_EXPIRE_DAYS: int = int(
        os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7)
    )

    # =========================
    # Security
    # =========================
    BCRYPT_ROUNDS: int = int(os.getenv("BCRYPT_ROUNDS", 12))

    CORS_ORIGINS: List[str] = ["*"]

    # =========================
    # Redis (optional)
    # =========================
    REDIS_URL: Optional[str] = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379/0"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()


# Optional cached settings
@lru_cache()
def get_settings() -> Settings:
    return Settings()