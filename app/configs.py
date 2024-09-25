from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", frozen=True)

    ROOT_PATH: str = Field(default=str(Path(__file__).parent.parent.absolute()))
    APP_PATH: str = Field(default=str(Path(__file__).parent.absolute()))

    BREWERIES_API_URL: str
    POSTGRES_URI: SecretStr


settings = Settings()
