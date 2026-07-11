#### Q6. write aa program to input two angles from user and calculate the third angle of triangle.

# lets take two angles as input from user

angle1=int(input("Enter the first angle of triangle:"))

angle2=int(input("Enter the second angle of triangle:"))

# so as we know whole triangle angle count is 180 degree so lets calculate remaining angle.

angle3=180-(angle1+angle2)

# lets display the output

print(f"the remaining third angle of triangle is {angle3}")

