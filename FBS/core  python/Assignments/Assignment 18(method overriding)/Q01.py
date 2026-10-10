### Q1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:
    
    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Destructor
    def __del__(self):
        print("Object destroyed")

    # Overload + operator
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    # Overload - operator
    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    # Display complex number
    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Creating objects
c1 = ComplexNumber(5, 3)
c2 = ComplexNumber(2, 4)

# # Addition
c3 = c1 + c2
print("Addition:", c3)

# Subtraction
c4 = c1 - c2
print("Subtraction:", c4)