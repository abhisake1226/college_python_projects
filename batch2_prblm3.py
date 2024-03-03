class PyConverter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()

    def kilometer(self):
        if self.unit == 'kilometers':
            return self.length
        elif self.unit == 'meters':
            return self.length / 1000
        elif self.unit == 'centimeters':
            return self.length / 100
        else:
            return "Invalid unit"

    def meter(self):
        if self.unit == 'kilometers':
            return self.length * 1000
        elif self.unit == 'meters':
            return self.length
        elif self.unit == 'centimeters':
            return self.length / 100
        else:
            return "Invalid unit"

    def centimeter(self):
        if self.unit == 'kilometers':
            return self.length * 100000
        elif self.unit == 'meters':
            return self.length * 100
        elif self.unit == 'centimeters':
            return self.length
        else:
            return "Invalid unit"


# Example usage:
ob = PyConverter(9, 'meters')
print("Length in centimeters:", ob.centimeter())  # Output: 900
