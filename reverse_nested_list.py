def reverse_nested_list(nested_list):
    if isinstance(nested_list, list):
        return [reverse_nested_list(sublist) for sublist in reversed(nested_list)]
    else:
        return nested_list

# Example usage:
nested_list = [[1,2],[3,[4,5]], 6]
reversed_list = reverse_nested_list(nested_list)
print(reversed_list)
