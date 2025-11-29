from stats import get_num_words, get_char_count, sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = get_num_words(book)
    char_count = get_char_count(book)
    sorted = sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if(item["char"].isalpha()):
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")    
    

main()
