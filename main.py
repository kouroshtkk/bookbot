import sys
from stats import *
def print_report(count: int,path: str,sorted_list:list[tuple[str,int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for (elem,size) in sorted_list:
        if elem.isalpha():
            print(f"{elem}: {size}")

    print("============= END ===============")

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    words_list = get_word_list(content)
    count = len(words_list)
    diction=get_dict(content)
    new_list = chars_dict_to_sorted_list(diction)
    print_report(count,path,new_list)

if __name__ == "__main__":
    main()