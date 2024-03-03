def count_occurrences(string):
    occurrences = {}

    for char in string:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1

    return occurrences

def print_occurrences(occurrences):
    for char, count in occurrences.items():
        print(f"'{char}' occurs {count} time(s)")

def main():
    string = input("Enter a string: ")
    occurrences = count_occurrences(string)
    print("Occurrences of characters in the string:")
    print_occurrences(occurrences)

if __name__ == "__main__":
    main()
