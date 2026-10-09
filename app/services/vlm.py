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

    async def check_ready(self) -> tuple[bool, str]:
        try:
            response = await self.client.get(
                "/models",
                timeout=5.0,
            )
        except httpx.HTTPError as exc:
            return False, f"VLM unreachable: {exc}"

        if response.status_code >= 400:
            return False, f"VLM HTTP {response.status_code}"

        try:
            data = response.json()
            ids = [item["id"] for item in data["data"]]
        except (ValueError, KeyError, TypeError):
            return False, "Invalid VLM models response"

        model = self.settings.vlm_model

        if model not in ids:
            return False, f"model {model} not served; available: {ids}"

        return True, "ready"
