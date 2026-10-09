import logging

import httpx

from app.config import Settings

log = logging.getLogger(__name__)


class VLMError(RuntimeError):
    pass


class VLMClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self._client: httpx.AsyncClient | None = None

    @property
    def client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.settings.vlm_base_url.rstrip("/"),
                timeout=self.settings.vlm_timeout_s,
                headers={"Authorization": (f"Bearer {self.settings.vlm_api_key}")},
            )

        return self._client

    async def aclose(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None
