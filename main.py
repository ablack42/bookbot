def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #w_count = get_num_words(text)
    char_count = get_char_count(text)
    print (char_count)   


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(doc):
    words = doc.split()
    count = len(words)
    return count

def get_char_count(doc):
    chars = {}
    for c in doc:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars 

main()