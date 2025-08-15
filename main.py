
from stats import word_count
from stats import letter_count
from stats import sort_dictionary
import sys


def get_book_text (file_path):
    with open (file_path) as f:
        content = f.read()
    return content


def main ():
    main.py = sys.argv[0] 
    if len(sys.argv) <= 1 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    story = get_book_text(file_path)
    letters = letter_count(story)
    #print(letters)
    sorted_letters = sort_dictionary(letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + str(file_path))
    print("----------- Word Count ----------")
    print( "Found "+ str(word_count(story)) + " total words")
    print("--------- Character Count -------")
    for x in sorted_letters:
        print(x["char"] + ": " + str(x["num"]) )


main()

