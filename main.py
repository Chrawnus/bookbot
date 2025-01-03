def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for key in num_chars_dict:
        sorted_list.append({"name": key, "num": num_chars_dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(words, chars_dict, path):
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()

    for item in sorted_list:
        char = item["name"]
        num = item["num"]
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {num} times")

    print("--- End report ---")

    
def character_count(text):
    num_char_dict = {}
    for c in text:
        lower_c = c.lower()
        if not lower_c in num_char_dict:
            num_char_dict[lower_c] = 1
        else:
            num_char_dict[lower_c] += 1 
    return num_char_dict

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = character_count(text)
    print_report(num_words, chars_dict, book_path)
    
main()