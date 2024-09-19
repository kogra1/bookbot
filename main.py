from collections import Counter
def main():
    book_path = 'books/frankenstein.txt'
    text = book(book_path)
    words = word_count(text)
    chars = char_count(text)
    chars.pop(' ')
    chars.pop('\n')
    chars_sorted = {k: v for k, v in sorted(chars.items(), key=lambda item: item[1], reverse=True)}
    # (reverse=True)
    # , key=sort_on)
    print(f'--- Begin report of {book_path} ---')
    print(f'The book has {words} words')
    
    for letter in chars_sorted:
        if not letter.isalpha():
            continue
        print(f'the \'{letter}\' character was found {chars_sorted[letter]} times')
    
    print(f'--- End report ---')


def book(book_path):
    with open(book_path) as f:
        text = f.read()
        return text
    
def sort_on(item):
    return item[""]
    
def char_count(text):
    text = text.lower()
    char_count = Counter(text)
    char_count = dict(char_count)
    return char_count


def word_count(text):
    return len(text.split())

main()