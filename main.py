from stats import count_words, count_characters, sort_list_of_dictionaries

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_list = sort_list_of_dictionaries(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
main()