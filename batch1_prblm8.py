"""Write a Python program that defines a class Length, which models length in feet and inches. 
Include the following class methods : 
(a) A constructor that initializes length (default values will be 0). 
(b) SetLength () : To set value of feet and inches. 
(c) getLength () : To return feet-inches in a tuple. 
(d) A magic method to print length. 
(e) A magic method to add two lengths"""



class Length:
    def __init__(self, feet=0, inches=0):
        """Constructor to initialize length with default values."""
        self.feet = feet
        self.inches = inches

    def set_length(self, feet, inches):
        """Method to set value of feet and inches."""
        self.feet = feet
        self.inches = inches

    def get_length(self):
        """Method to return feet-inches in a tuple."""
        return self.feet, self.inches

    def __str__(self):
        """Magic method to print length."""
        return f"{self.feet} feet {self.inches} inches"

    def __add__(self, other):
        """Magic method to add two lengths."""
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches %= 12
        return Length(total_feet, total_inches)

# Example usage:
if __name__ == "__main__":
    # Create instances of Length class
    length1 = Length(5, 8)
    length2 = Length(3, 10)

    # Print length using __str__ method
    print("Length 1:", length1)
    print("Length 2:", length2)

    # Add two lengths using __add__ method
    total_length = length1 + length2
    print("Total length:", total_length)
