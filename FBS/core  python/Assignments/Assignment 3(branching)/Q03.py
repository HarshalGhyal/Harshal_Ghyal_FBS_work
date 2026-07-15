#### Q3.Write a program to input angles of a triangle and check whether triangle is valid or not.

#lets take 3 input as 3 angles as a,b and c:

a=int(input("Enter angle 1:"))
b=int(input("Enter angle 2:"))
c=int(input("Enter angle 3:"))

# so valid triangle defination is sum of 3 angle of triangle is 180 degrees:
sum=a+b+c
# lets check.

if sum==180:
    print("its a valid triangle!")
else:
    print("its not a valid triangle!")    
