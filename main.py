def main():
    with open('books/frankenstein.txt') as f:
      file_contents = f.read()

    # count_words_in_book(file_contents)
    # count_letters(file_contents)
    
    print_report(file_contents)
    
def count_words_in_book(book_text):
    word_counter = 0
    words = book_text.split()
    for word in words:
        word_counter += 1
    return word_counter

def count_letters(book_text):
    letters_hold = {}
    
    for letter in book_text:
        lower_letter = letter.lower()
        if lower_letter.isalpha() or lower_letter == ' ':
            if lower_letter not in letters_hold:
                letters_hold[lower_letter] = 1
            else:
                letters_hold[lower_letter] += 1
    return letters_hold
    # print(letters_hold)

def print_report(book_text):

    total_words = count_words_in_book(book_text)
    letters = count_letters(book_text)

    list_of_dicts = []

    for char, count in letters.items():
        new_dict = {"letter": char, "count": count}
        # print(f"char: {char} count: {count}")
        list_of_dicts.append(new_dict)
    # print(list_of_dicts)    
    list_of_dicts.sort(reverse=True, key=sort_on)
    print(list_of_dicts)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in document")

    for letter in list_of_dicts:
        print(f"The '{letter}' character was found  times")

def sort_on(dict):
    return dict["count"]

main()