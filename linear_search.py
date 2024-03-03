def linear_search(arr, target):
    """
    Perform linear search to find the target element in the array.

    Parameters:
        arr (list): The list in which to search for the target element.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return its index
    return -1  # Element not found

# Example usage:
arr = [3, 5, 2, 7, 9, 1]
target = 7
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
