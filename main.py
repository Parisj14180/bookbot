def get_book_text(books):
    with open(books) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)

main()