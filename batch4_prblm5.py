#question a diamond pattern printing
rows = int(input("Enter number of rows: "))

#loop to print the upper half of the pyramid
for i in range(1,rows+1):
    #loop to print spaces before astericks
    for j in range (1,rows-i+1):
        print(" ", end="")

    #loop to print astericks
    for k in range (0,i):
        print("*", end=" ")
    print()# move to new line


#loop to print the lower half of the pyramid
for i in range(rows-1,0,-1):
    #loop to print spaces before astericks
    for j in range (1,rows-i+1):
        print(" ", end="")

    #loop to print astericks
    for k in range (0,i):
        print("*", end=" ")
    
    print()# move to new line

#Write a Python program to check whether a number is prime
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        # Check divisibility by odd numbers starting from 3 up to the square root of the number
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

# Test the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
