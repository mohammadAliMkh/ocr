import logging
from pathlib import Path

import pytesseract
from PIL import Image
from pytesseract import Output

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
                    "Tesseract are not installed: %s",
                    ", ".join(missing),
                )

            if not chosen:
                raise RuntimeError("no requested Tesseract language is installed")

            self.tesseract_langs = chosen
            self.tesseract_ok = True

            log.info(
                "Tesseract started v%s | lang:%s",
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

    def ocr_lines(self, path: Path) -> tuple[str, list[dict]]:
        if not self.tesseract_ok:
            return "", []

        with Image.open(path) as img:
            data = pytesseract.image_to_data(
                img,
                lang="+".join(self.tesseract_langs),
                output_type=Output.DICT,
            )

        lines: dict[tuple[int, int, int], list[tuple[str, float]]] = {}

        for i in range(len(data["text"])):
            word = data["text"][i].strip()
            conf = float(data["conf"][i])

            if not word or conf < self.settings.tesseract_min_conf:
                continue

            key = (
                int(data["block_num"][i]),
                int(data["par_num"][i]),
                int(data["line_num"][i]),
            )

            lines.setdefault(key, []).append((word, conf))

        result: list[dict] = []

        for words in lines.values():
            line_text = " ".join(word for word, _ in words)

            confidence = sum(conf for _, conf in words) / len(words) / 100

            result.append(
                {
                    "text": line_text,
                    "confidence": confidence,
                }
            )

        text = "\n".join(item["text"] for item in result)

        return text, result
