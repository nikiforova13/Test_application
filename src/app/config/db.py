from pydantic_settings import BaseSettings
from pydantic_settings.main import SettingsConfigDict
from app.config.base import get_updated_model_config, BASE_CONFIG

from pymantic import sparql


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        get_updated_model_config(
            BASE_CONFIG, SettingsConfigDict(env_prefix="BLAZEGRAPH_")
        )
    )
    HOST: str
    PORT: int
    USER: str | None = None
    PASSWORD: int | None = None
    DB_NAME: str

    @property
    def DATABASE_URL(self):
        return f"http://{self.HOST}:{self.PORT}/{self.DB_NAME}"


settings = DBSettings()
