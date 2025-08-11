from stats import *
import sys

def get_book_text(filepath):
    """
    Reads the content of a book from a file and returns it as a string.
    
    :param filepath: Path to the book file.
    :return: Content of the book as a string.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError("The specified file does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")

def print_pretty_report(filepath, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    try:
        book_text = get_book_text(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    num_words = count_words(book_text)
    num_chars = count_chars(book_text)
    sorted_dict = sort_dictionary(num_chars)

    print_pretty_report(filepath, num_words, sorted_dict)


if __name__ == "__main__":
    main()