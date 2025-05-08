from collections import Counter
def char_count(text):
    text = text.lower()
    char_count = Counter(text)
    char_count = dict(char_count)
    return char_count


def word_count(text):
    return len(text.split())