from pathlib import Path


class Document:
    def __init__(self, path: str) -> None:
        self.path: Path = Path(path)
        self.text: str = ""

    def load(self) -> None:
        self.text = self.path.read_text(encoding="utf-8")

    def clean(self) -> None:
        self.text = self.text.strip().lower()

    def stats(self) -> int:
        words = self.text.split()
        return len(words)
