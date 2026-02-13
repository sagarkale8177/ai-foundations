from document import Document


def main() -> None:
    doc = Document("input.txt")
    doc.load()
    doc.clean()

    total_words = doc.stats()
    print(f"Total words: {total_words}")


if __name__ == "__main__":
    main()
