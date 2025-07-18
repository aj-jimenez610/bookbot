import sys

def main():
    if len(sys.argv) < 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
    else:
        filepath = sys.argv[1]
        book = get_book_text(filepath)
        word_count = count_words(book)
        characters = get_characters(book)
        print_report(filepath,word_count, characters)
    
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_words(text):
    count = len(text.split())
    return count

def get_characters(text):
    characters = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            characters[char] = characters.get(char, 0) + 1
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)
    characters_dict = [{"char": key, "num": value} for key, value in sorted_characters]
    return characters_dict


def print_report(filepath, word_count, characters):
    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    #print(characters)
    for item in characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()