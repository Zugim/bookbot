def get_word_count(book_contents):
    word_count = len(book_contents.split())

    return word_count


def get_char_counts(book_contents):
    char_counts = {}

    for char in book_contents:
        char_lowercase = char.lower()

        if char_lowercase in char_counts:
            char_counts[char_lowercase] += 1
            continue

        char_counts[char_lowercase] = 1

    return char_counts


def sort_char_counts(char_counts):
    count_dicts = []

    for count in char_counts:
        count_dicts.append({
            "char": count,
            "num": char_counts[count]
        })

    count_dicts.sort(reverse=True, key=lambda count_dict: count_dict["num"])

    return count_dicts
