def main():
    book_path = "books/frankenstain.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words was found in the document.")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

main()