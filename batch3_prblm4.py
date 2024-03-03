def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

def find_anagrams(string, string_list):
    return list(filter(lambda x: is_anagram(string, x), string_list))

def main():
    # Take input from the user for the list of strings
    string_list = input("Enter a list of strings separated by spaces: ").split()
    # Take input from the user for the target string
    target_string = input("Enter the target string: ")

    # Find anagrams
    anagrams = find_anagrams(target_string, string_list)

    # Print the result
    print(f"Anagrams of '{target_string}' in the given list:")
    print(anagrams)

if __name__ == "__main__":
    main()
