import sys

from stats import get_word_count, get_char_counts, sort_char_counts


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def format_output(book_path, word_count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for count in char_counts:
        if count["char"].isalpha():
            print(f"{count["char"]}: {count["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_contents = get_book_text(f"./{sys.argv[1]}")

    word_count = get_word_count(book_contents)
    char_counts = sort_char_counts(get_char_counts(book_contents))

    format_output(sys.argv[1], word_count, char_counts)


main()
