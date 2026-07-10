#### Q12. Find the volume of sphere.

#lets take input as radius of sphere

import math

r=float(input("Enter the radius of sphere:"))

#lets calculate the volume using formula (4/3)*pi*r^3
volume=(4/3)*math.pi*(r**3)

print("The volume of the sphere is:", volume)