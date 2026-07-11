#### Q2. write a program to calculate area of rectangle based on length and breadth.

# To calculate area of rectangle we have get length and breadth of a rectangle from user. and also length should greater than breadth

length_of_rectangle=float(input("Enter the length of a rectangle:"))

breadth_of_rectangle=float(input("Enter the breadth of a rectangle:"))

#so the formula for area of rectangle is length*breadth.

Area_of_rectangle=length_of_rectangle*breadth_of_rectangle

#lets display the results

print(f"Area of given measurments rectangle is {Area_of_rectangle} sq.m")