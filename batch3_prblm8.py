def is_armstrong(number):
    #convert the number to a string to count its digits
    num_str = str(number)
    #Get the number of digits
    num_digits = len(num_str)
    #calculate the sum of digits raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    #check if the sum is equal to the original number
    return armstrong_sum == number

number = int(input('Enter a number:'))

if is_armstrong(number):
    print(f"{number} is an Armstrong number..")

else:
    print(f"{number} is NOT Armstrong number..")


"""def is_armstrong(number):
    # Convert the number to a string
    num_str = str(number)
    # Get the number of digits
    num_digits = len(num_str)
    # Initialize the armstrong sum to 0
    armstrong_sum = 0
    
    # Calculate the armstrong sum
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    
    # Check if the armstrong sum is equal to the original number
    return armstrong_sum == number

# Test the function
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
"""
