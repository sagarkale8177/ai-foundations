from pathlib import Path

def read_text(path: str) -> str:
    file_path = Path(path)
    return file_path.read_text(encoding="utf-8")

def clean_text(text: str) -> str:
    return text.strip()

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def main() -> None:
    raw_text: str = read_text("input.txt")
    cleaned: str = clean_text(raw_text)
    total_words: int = count_words(cleaned)

    print(f"Total words: {total_words}")


if __name__ == "__main__":
    main()
