from stats import count_words

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")

main()