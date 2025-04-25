import sys
from stats import count_words, count_character, sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    path = book_path
    text = get_book_text(path)
    word_count = count_words(text)
    char_counts = count_character(text)
    sorted_chars = sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()