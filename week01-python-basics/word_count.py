from pathlib import Path


def count_words(text):
    words = text.lower().split()
    result = {}
    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if not word:
            continue
        result[word] = result.get(word, 0) + 1
    return result


def main():
    file_path = Path(__file__).with_name("sample_text.txt")
    text = file_path.read_text(encoding="utf-8")
    counts = count_words(text)

    for word, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()

