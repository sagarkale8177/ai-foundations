import logging
from pathlib import Path

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

class Document:
    def __init__(self, path: str) -> None:
        self.path: Path = Path(path)
        self.text: str = ""
        logger.info(f"Document created for {self.path}")

    def load(self) -> None:
        try:
            self.text = self.path.read_text(encoding="utf-8")
            logger.info("File loaded successfully")
        except FileNotFoundError:
            logger.error("File not found")
            raise

    def clean(self) -> None:
        self.text = self.text.strip().lower()
        logger.info("Text cleaned")

    def stats(self) -> int:
        words = self.text.split()
        count = len(words)
        logger.info(f"Word count calculated: {count}")
        return count
