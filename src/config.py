from functools import lru_cache
from typing import Final, final

from pydantic_settings import BaseSettings, SettingsConfigDict


@lru_cache()
def get_config():
    """Get the configuration for the application. This is cached for performance."""
    return Config()


@final
class Config(BaseSettings):
    app_name: str = "sysdocs fastapi"

    model_config = SettingsConfigDict(env_file=".env")
