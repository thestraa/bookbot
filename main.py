def main():
    book_path = "books/frankenstain.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document\n")
    num_chars = count_characters(text)
    print_chars = print_characters(num_chars)
    print("--- End report ---")
    
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

def sort_on(char_list):
    return char_list["count"]

def print_characters(num_chars):
    char_list = []
    for char in num_chars:
        if char.isalpha():
            count = num_chars[char]
            char_list.append({"character": char, "count": count})         
    char_list.sort(reverse=True, key=sort_on) 

    for dictionary in char_list:
        print(f"The '{dictionary["character"]}' character was found {dictionary["count"]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()