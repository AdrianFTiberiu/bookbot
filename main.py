def count_words(big_text):
    words = big_text.split()
    return len(words)

def count_letters(big_text):
    fmt_small_letters=big_text.lower()
    counter = {}
    for nr in range(0, 128):
        counter[chr(nr)] = 0
    for letter in fmt_small_letters:
        counter[letter] +=1
    return counter

def sort_on(dict):
    for letter in range(ord('a'), ord('z')+1):
        if chr(letter) in dict:
            return dict[chr(letter)]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document")
        print()
        letter_freq_dict = count_letters(file_contents)
        letter_freq_list = []
        for letter in range(ord('a'), ord('z')+1):
            single_dict = {chr(letter) : letter_freq_dict[chr(letter)]}
            letter_freq_list.append(single_dict)
        letter_freq_list.sort(reverse=True, key=sort_on)
        for dict in letter_freq_list:
            for key,value in dict.items():
                print(f"The '{key}' character was found {value} times")
        print("--- End report ---")

main()