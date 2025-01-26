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
    letters_hold = {}
    
    for letter in book_text:
        lower_letter = letter.lower()
        if lower_letter.isalpha() or lower_letter == ' ':
            if lower_letter not in letters_hold:
                letters_hold[lower_letter] = 1
            else:
                letters_hold[lower_letter] += 1

    print(letters_hold)
main()