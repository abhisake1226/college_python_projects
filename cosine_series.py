import math

def cosine_series(x, n):
    result = 0
    for i in range(n):
        term = (-1) ** i * (x ** (2 * i)) / math.factorial(2 * i)
        result += term
    return result

# Input the value of x in degrees and the number of terms from the user
x = float(input("Enter the value of x in degrees: "))
n = int(input("Enter the number of terms: "))

# Convert degrees to radians
x = math.radians(x)

# Calculate the cosine series
cosine_result = cosine_series(x, n)

# Output the result
print(cosine_result)
