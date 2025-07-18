def main():
    print_report

def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def count_words(text):
    count = len(text.split())
    return count

def get_characters(text):
    alpha_characters = []
    characters = {}
    characters_dict= {}
    sorted_characters = {}
    for char in text:
        if char.isalpha():
            alpha_characters.append(char)
    for letters in alpha_characters:
        characters.setdefault(letters.lower(),0)
        characters[letters.lower()] += 1
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    characters_dict = [{"char": key, "num": value} for key, value in sorted_characters]
    return characters_dict

def print_report(count, characters_dict):
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------""")
    #print(characters)
    for item in characters_dict:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


#new_text = get_book_text("books/frankenstein.txt")
#word_count = count_words(new_text)
#characters = get_characters(new_text)
#count_words(new_text)
#get_characters(new_text)
main()