#a) Python program to calculate GCD and LCM of two numbers:

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Test the functions
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd_result = gcd(num1, num2)
lcm_result = lcm(num1, num2)

print(f"GCD of {num1} and {num2} is:", gcd_result)
print(f"LCM of {num1} and {num2} is:", lcm_result)


#b) Python program to create a lambda function that adds 15 to a given number passed in as an argument:

add_15 = lambda x: x + 15

# Test the lambda function
number = int(input("Enter a number: "))
result = add_15(number)
print("Result after adding 15 to the number:", result)
