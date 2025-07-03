def count_words(text):
    return len(text.split())

def count_characters(text):
    result_dict = {}
    for char in text:
        char = char.lower()
        if char in result_dict:
            result_dict[char] += 1
        else:
            result_dict[char] = 1
        
    return result_dict

def sort_on(items):
    return items["num"]

def sort_list_of_dictionaries(chars_dict):
    sorted_list = []
    for char in chars_dict:
        char_dict = {
            "char": char,
            "num": chars_dict[char]
        }
        sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list