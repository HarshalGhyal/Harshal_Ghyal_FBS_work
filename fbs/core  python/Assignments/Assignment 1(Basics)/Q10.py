#### Q10.Write a program to calculate area of an equilateral triangle.

# In equolateral triangle all sides are equal so we can take any side as input and calculate area using formula (sqrt(3)/4)*a^2

#lets take input as side of triangle

import math

a=float(input("Enter the side of an equilateral triangle:"))

#lets calculate the area using formula (sqrt(3)/4)*a^2

area=(math.sqrt(3)/4)*(a**2)

print("The area of the equilateral triangle is:", area)