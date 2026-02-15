import json
import re
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
    # remove emails
     self.text = re.sub(r"\S+@\S+", "", self.text)

    # remove phone numbers (10 digit)
     self.text = re.sub(r"\b\d{10}\b", "", self.text)

    # remove extra spaces
     self.text = re.sub(r"\s+", " ", self.text)

     self.text = self.text.strip().lower()

     logger.info("Text cleaned with regex")


    def stats(self) -> int:
        words = self.text.split()
        count = len(words)
        logger.info(f"Word count calculated: {count}")
        return count
    
    def export_json(self, output_path: str) -> None:
     data = {
        "file": self.path.name,
        "word_count": self.stats(),
        "cleaned_text": self.text
    }

     with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

     logger.info(f"JSON exported to {output_path}")

