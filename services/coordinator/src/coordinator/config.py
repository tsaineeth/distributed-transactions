from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class CoordinatorSettings(BaseSettings):
    """
    Application configuration.

    Values are loaded from environment variables and optionally from a .env file.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Service metadata
    service_name: str = Field(default="Coordinator Service")
    description: str = Field(default="Coordinator Service")
    version: str = Field(default="0.1.0")
    environment: str = Field(default="development")

    # Logging
    log_level: str = Field(default="INFO")

    # Server
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)


@lru_cache
def get_settings() -> CoordinatorSettings:
    """
    Return a cached Settings instance.
    """
    return CoordinatorSettings()
