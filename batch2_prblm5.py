def longest_chain_of_zeros(lst):
    max_zeros = 0
    max_zeros_start = 0
    max_zeros_end = 0

    current_zeros = 0
    current_start = 0

    for i, num in enumerate(lst):
        if num == 0:
            current_zeros += 1
            if current_zeros == 1:
                current_start = i  # Start of a new chain of zeros
        else:
            if current_zeros > max_zeros:
                max_zeros = current_zeros
                max_zeros_start = current_start
                max_zeros_end = i - 1  # End of the current chain of zeros
            current_zeros = 0

    # Check if the last sequence of zeros is the longest
    if current_zeros > max_zeros:
        max_zeros = current_zeros
        max_zeros_start = current_start
        max_zeros_end = len(lst) - 1

    return max_zeros, max_zeros_start, max_zeros_end


def main():
    # Populate the list with integers (0 or 1)
    lst = [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]

    # Find the longest chain of zeros
    max_zeros, max_zeros_start, max_zeros_end = longest_chain_of_zeros(lst)

    # Print the result
    print(f"The longest run of zeros is {max_zeros}.")
    print(f"Span: {max_zeros_start} to {max_zeros_end}")


if __name__ == "__main__":
    main()
