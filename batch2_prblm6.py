def is_positive_integer(val):
    """Check if the input is a positive integer."""
    if isinstance(val, int) and val > 0:
        return True
    else:
        return False

def number_of_factors(val):
    """Returns a list of factors of the input number."""
    if not is_positive_integer(val):
        print("Input must be a positive integer.")
        return []

    factors = []
    for i in range(1, val + 1):
        if val % i == 0:
            factors.append(i)
    return factors

def list_of_factors(val):
    """Returns the number of factors the input number has."""
    if not is_positive_integer(val):
        print("Input must be a positive integer.")
        return -1

    return len(number_of_factors(val))

# Example usage:
val = 12
print("Factors of", val, ":", number_of_factors(val))
print("Number of factors of", val, ":", list_of_factors(val))
