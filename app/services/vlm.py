import logging

import httpx

from app.config import Settings
import base64
import io
from pathlib import Path

from PIL import Image, ImageOps

log = logging.getLogger(__name__)


class VLMError(RuntimeError):
    pass

def encode_image_data_url(path: Path) -> str:
    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=88)
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"

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

    
    async def chat(self, messages: list[dict], **extra) -> str:
        payload = {
            "model": self.settings.vlm_model,
            "messages": messages,
            "max_tokens": self.settings.vlm_max_tokens,
            "temperature": self.settings.vlm_temperature,
            **extra,
        }

        try:
            response = await self.client.post(
                "/chat/completions",
                json=payload,
            )
        except httpx.HTTPError as exc:
            raise VLMError(f"VLM unreachable: {exc}") from exc

        if response.status_code >= 400:
            raise VLMError(
                f"VLM HTTP {response.status_code}: {response.text[:300]}"
            )

        try:
            data = response.json()
            content = data["choices"][0]["message"]["content"]
        except (ValueError, KeyError, TypeError, IndexError) as exc:
            raise VLMError("Invalid VLM chat completion response") from exc

        return content or ""

