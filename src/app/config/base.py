from pydantic_settings.main import SettingsConfigDict
from pathlib import Path

APP_GLOBAL_PATH = Path(__file__).parent.parent.parent.absolute()


BASE_CONFIG: SettingsConfigDict = SettingsConfigDict(
    env_file=APP_GLOBAL_PATH.joinpath(".env"),
    env_file_encoding="utf-8",
)


def get_updated_model_config(orig: SettingsConfigDict, update: SettingsConfigDict):
    copy = orig.copy()
    for k, v in update.items():
        copy[k] = v

    return copy
