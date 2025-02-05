def main():
    book_path = "books/frankenstain.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)

def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def count_characters(text):
    character_count = {}
    lower_text = text.lower()
    for character in lower_text:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1 
    return character_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()