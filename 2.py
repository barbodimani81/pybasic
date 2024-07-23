def count_words(text):
    word_counts = {}
    words = text.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def main():
    text = input("Enter text: ")
    word_counts = count_words(text)
    print("Word counts: ")
    for word, count in word_counts.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
