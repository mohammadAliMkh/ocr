import logging

import pytesseract

from app.config import Settings

log = logging.getLogger(__name__)


class VisionAnalyzer:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.tesseract_ok = False
        self.tesseract_version: str | None = None

    def load(self) -> None:
        if not self.settings.enable_tesseract:
            log.info("Tesseract is disabled")
            return

        try:
            if self.settings.tesseract_cmd:
                pytesseract.pytesseract.tesseract_cmd = self.settings.tesseract_cmd

            self.tesseract_version = str(pytesseract.get_tesseract_version())
            self.tesseract_ok = True

            log.info(
                "Tesseract loaded successfully, version: %s",
                self.tesseract_version,
            )

        except Exception as exc:
            log.warning("Tesseract disabled: %s", exc)
            self.tesseract_ok = False
