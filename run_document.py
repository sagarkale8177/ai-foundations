from document import Document
import logging

logger = logging.getLogger(__name__)

def main() -> None:
    try:
        doc = Document("input.txt")
        doc.load()
        doc.clean()

        total_words = doc.stats()
        print(f"Total words: {total_words}")

        doc.export_json("cleaned.json")

    except Exception:
        logger.exception("Program crashed")


if __name__ == "__main__":
    main()
