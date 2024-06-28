def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars = {}
    low_text = text.lower()
    for char in low_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    list_of_chars = []
    for char in count_chars(text):
        key = char
        value = count_chars(text)[char]
        if key.isalpha():
            dict1 = {"character":key, "num":value}
            list_of_chars.append(dict1)

    list_of_chars.sort(key=lambda x: x["num"], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_words(text)} words found in the document")
    print()

    for dict in list_of_chars:
        print(f"The '{dict["character"]}' character was found {dict["num"]} times")


main()
