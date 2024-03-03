def sort_hyphen_separated_sequence(sequence):
    sorted_words = sorted(sequence.split('-'))
    sorted_sequence = '-'.join(sorted_words)
    return sorted_sequence

def main():
    # Take input from the user for the hyphen-separated sequence
    sequence = input("Enter a hyphen-separated sequence of words: ")

    # Sort the sequence and print the result
    sorted_sequence = sort_hyphen_separated_sequence(sequence)
    print("Sorted sequence:", sorted_sequence)

if __name__ == "__main__":
    main()
