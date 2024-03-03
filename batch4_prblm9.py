'''a) Python program to reverse the order of words in a given string:'''

def reverse_words(string):
    words = string.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

# Test the function
input_str = input("Enter a string: ")
output_str = reverse_words(input_str)
print("Reversed string:", output_str)

'''b) Python program to get the number of occurrences of a specified element in an array:'''

def count_occurrences(arr, element):
    count = 0
    for item in arr:
        if item == element:
            count += 1
    return count

# Test the function
arr = list(map(int, input("Enter array elements separated by space: ").split()))
element = int(input("Enter the element to count occurrences: "))
occurrences = count_occurrences(arr, element)
print("Number of occurrences of", element, "in the array:", occurrences)
