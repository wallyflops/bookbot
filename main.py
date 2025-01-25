def main():
    with open('books/frankenstein.txt') as f:
      file_contents = f.read()

    count_words_in_book(file_contents)
    count_letters(file_contents)
    
def count_words_in_book(book_text):
    word_counter = 0
    words = book_text.split()
    for word in words:
        word_counter += 1
    
    print(word_counter)

def count_letters(book_text):
    letters = {}
    for letter in book_text:
        if letter not in letters:
            letters[letter] += 1
    
    print(letters)
main()