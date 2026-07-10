#### Q4.WAP to calculate area of triangle and rectangle.

#lets take input as base and height of triangle
base=float(input("Enter base of triangle:"))
height=float(input("Enter height of triangle:"))

#lets calculate area of triangle
area_triangle=0.5*base*height

#lets take input as length and width of rectangle
length=float(input("Enter length of rectangle:"))
width=float(input("Enter width of rectangle:"))

#lets calculate area of rectangle
area_rectangle=length*width

#lets display the output
print(f"Area of triangle: {area_triangle}")
print(f"Area of rectangle: {area_rectangle}")