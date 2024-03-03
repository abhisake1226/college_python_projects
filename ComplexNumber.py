class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def multiply(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

# Example usage:
# Define two complex numbers
complex1 = ComplexNumber(2, 3)
complex2 = ComplexNumber(1, -1)

# Addition
result_addition = complex1.add(complex2)
print("Addition result:", result_addition)

# Multiplication
result_multiplication = complex1.multiply(complex2)
print("Multiplication result:", result_multiplication)

print(complex1)
print(complex2)
