def word_count(book):
    count = book.split()
    return len(count)

def letter_count(book):
    book = book.lower()
    letters = {'a':0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g':0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'p': 0, 'q': 0, 'r': 0, 's':0, 't':0, 'u':0, 'v':0, 'x':0, 'y':0, 'z':0}
    for letter in book:
        if letter in letters:
            letters[letter] +=1
    return letters

def sort_dictionary (my_dict):
    holder_list = []

    for key_value in my_dict.items():
        empty_dict = {}
        empty_dict["char"] = key_value[0]
        empty_dict["num"] = key_value[1]
        holder_list.append(empty_dict)

    def sort_on(items):
        return items["num"]
    

    holder_list.sort(reverse=True, key=sort_on)
    return holder_list



