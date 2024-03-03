#a) Python program to count Even and Odd numbers in a list

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Test the function
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_count, odd_count = count_even_odd(numbers)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)


#b) Python function to find the length of a given string:

def find_string_length(input_string):
    return len(input_string)

# Test the function
input_string = input("Enter a string: ")
length = find_string_length(input_string)
print("Length of the given string:", length)

