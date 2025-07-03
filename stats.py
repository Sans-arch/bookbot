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