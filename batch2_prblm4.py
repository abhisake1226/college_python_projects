def words_ending_with_on(file_name):
    """Find and print all words ending with 'on'."""
    with open(file_name, 'r') as file:
        words = file.read().split()
        print("Words ending with 'on':")
        for word in words:
            if word.endswith('on'):
                print(word)


def words_with_second_and_third_letters_re(file_name):
    """Find and print all words whose second and third letters are 'r' and 'e'."""
    with open(file_name, 'r') as file:
        words = file.read().split()
        print("\nWords whose second and third letters are 'r' and 'e':")
        for word in words:
            if len(word) >= 3 and word[1] == 'r' and word[2] == 'e':
                print(word)


def words_with_no_vowels(file_name):
    """Find and print all words with no vowels."""
    vowels = 'aeiouAEIOU'
    with open(file_name, 'r') as file:
        words = file.read().split()
        print("\nWords with no vowels:")
        for word in words:
            if not any(char in vowels for char in word):
                print(word)


def main():
    file_name = 'data.txt'
    words_ending_with_on(file_name)
    words_with_second_and_third_letters_re(file_name)
    words_with_no_vowels(file_name)


if __name__ == "__main__":
    main()
