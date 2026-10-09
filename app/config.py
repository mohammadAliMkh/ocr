from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "OCR Application"
    app_version: str = "0.1.0"
    data_dir: Path = Path("data")
    max_upload_mb: int = 512
    log_level: str = "INFO"
    cors_origins: str = "*"
    enable_tesseract: bool = True
    tesseract_langs: str = "eng"
    tesseract_min_conf: float = 40.0
    tesseract_cmd: str = ""
    vlm_base_url: str = "http://127.0.0.1:9000/v1"
    vlm_model: str = "mock-vlm"
    vlm_api_key: str = "EMPTY"
    vlm_timeout_s: float = 120.0
    vlm_max_tokens: int = 2048
    vlm_temperature: float = 0.2

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def upload_dir(self) -> Path:
        return self.data_dir / "uploads"

    @property
    def output_dir(self) -> Path:
        return self.data_dir / "outputs"

    @property
    def cors_origin_list(self) -> list[str]:
        return [
            origin.strip() for origin in self.cors_origins.split(",") if origin.strip()
        ]

    @property
    def tesseract_lang_list(self) -> list[str]:
        return [
            lang.strip() for lang in self.tesseract_langs.split("+") if lang.strip()
        ]

    def build(self) -> None:
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def public_snapshot(self) -> dict:
        return {
            "app_name": self.app_name,
            "app_version": self.app_version,
            "max_upload_mb": self.max_upload_mb,
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()
