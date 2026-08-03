#### Q1.Write a program to calculate area of rectangle.

# with passing parameter and with not returning value:
def Area_Rectangle(length,breadth):

    print ("Area of rectangle:",length*breadth)
Area_Rectangle(10,7) 

# without passing parameter and with not returning value:
def area_rectangle():
    length=float(input("Enter length of rectangle:"))
    breadth=float(input("Enter breadth of rectangle:"))

    area=length*breadth
    print(f"area of rectangle for given length:{length} and breadth:{breadth} is {area}")

area_rectangle()









