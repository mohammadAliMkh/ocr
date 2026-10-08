import logging
from pathlib import Path

import pytesseract
from PIL import Image

from app.config import Settings

log = logging.getLogger(__name__)


class VisionAnalyzer:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.tesseract_ok = False
        self.tesseract_version: str | None = None
        self.tesseract_langs: list[str] = []

    def load(self) -> None:
        if not self.settings.enable_tesseract:
            log.info("Tesseract is disabled")
            return

        try:
            if self.settings.tesseract_cmd:
                pytesseract.pytesseract.tesseract_cmd = self.settings.tesseract_cmd

            self.tesseract_version = str(pytesseract.get_tesseract_version())

            available = set(pytesseract.get_languages(config=""))

            chosen = [
                lang for lang in self.settings.tesseract_lang_list if lang in available
            ]

            missing = [
                lang
                for lang in self.settings.tesseract_lang_list
                if lang not in available
            ]

            if missing:
                log.warning(
                    "Requested Tesseract languages are not installed: %s",
                    ", ".join(missing),
                )

            if not chosen:
                raise RuntimeError("no requested Tesseract language is installed")

            self.tesseract_langs = chosen
            self.tesseract_ok = True

            log.info(
                "Tesseract loaded successfully, version: %s, languages: %s",
                self.tesseract_version,
                "+".join(chosen),
            )

        except Exception as exc:
            log.warning("Tesseract disabled: %s", exc)
            self.tesseract_ok = False

    def ocr_image(self, path: Path) -> str:
        if not self.tesseract_ok:
            return ""

        with Image.open(path) as img:
            text = pytesseract.image_to_string(
                img,
                lang="+".join(self.tesseract_langs),
            )

        return text.strip()
