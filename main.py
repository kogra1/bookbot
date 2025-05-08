from stats import word_count, char_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = book(book_path)
    words = word_count(text)
    chars = char_count(text)
    chars.pop(' ')
    chars.pop('\n')
    chars_sorted = {k: v for k, v in sorted(chars.items(), key=lambda item: item[1], reverse=True)}
    words = word_count(text)
    chars = char_count(text)
    print(f'--- Begin report of {book_path} ---')
    print(f'{words} words found in the document')
    
    for letter in chars_sorted:
        if not letter.isalpha():
            continue
        print(f'\'{letter}: {chars_sorted[letter]}\'')
    
    print(f'--- End report ---')
    sys.exit(0)


def book(book_path):
    with open(book_path) as f:
        text = f.read()
        return text
    
def sort_on(item):
    return item[""]

main()