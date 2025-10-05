import sys
from stats import get_word_count, get_char_count, get_sorted_list


def get_book_text(filepath):

    contents = None
    
    with open(filepath, 'r', encoding="utf-8") as f:

        contents = f.read()

    return contents


def is_valid_arguments(arguments):
    if len(arguments) < 2:
        return False
    return True


def main():

    usage_message = "Usage: python3 main.py <path_to_book>"
    arguments = sys.argv

    if not is_valid_arguments(arguments):
        print(usage_message)
        sys.exit(1)

    book_file_path = sys.argv[1]
    book_text = get_book_text(book_file_path)
    word_count = get_word_count(book_text)
    character_count = get_char_count(book_text)
    sorted_char_count_list = get_sorted_list(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")

    for item in sorted_char_count_list:
        character: str = item["char"]
        count: int = item["num"]

        if not character.isalpha():
            continue

        print(f"{character}: {count}")

    print("============= END ===============")


main()


