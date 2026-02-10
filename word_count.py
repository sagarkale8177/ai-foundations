from pathlib import Path

file_path = Path("input.txt")

text = file_path.read_text(encoding="utf-8")

words = text.split()

print(f"Total words: {len(words)}")
