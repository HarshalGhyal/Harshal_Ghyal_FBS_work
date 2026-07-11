#### Q11. Find the area and circumference of circle.

#lets take input as radius of circle

import math

r=float(input("Enter the radius of circle:"))

#lets calculate the area using formula pi*r^2
area=math.pi*(r**2)

#lets calculate the circumference using formula 2*pi*r
circumference=2*math.pi*r

print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference) 