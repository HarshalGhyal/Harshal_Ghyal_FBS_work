#### Q2.Write a program to calculate area of circle.
from math import pi
# with passing parameter and with returning value:
def area_circle(radius):
    area=pi*(radius**2)

    print(f'Area of circle for given radius:{radius} is {area}')

area_circle(3)

# without passing parameter and with returning value:
def Area_circle():
    radius=float(input("Enter radius of circle:"))
    Area=pi*(radius**2)
    
    print(f'Area of circle for given radius:{radius} is {Area}')
   
    
Area_circle()

