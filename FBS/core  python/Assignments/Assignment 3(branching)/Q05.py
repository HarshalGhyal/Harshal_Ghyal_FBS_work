#### Q5.Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

# Classification Rules:
# - Equilateral: All 3 angles are equal (exactly 60° each).
# - Isosceles: Exactly 2 angles are equal.
# - Scalene: All 3 angles are unique.

#lets take 3 input as 3 angles as a,b and c:

a=int(input("Enter angle 1:"))
b=int(input("Enter angle 2:"))
c=int(input("Enter angle 3:"))

# so valid triangle defination is sum of 3 angle of triangle is 180:
sum=a+b+c

# lets check:
if sum==180:
    if a==b and b==c :
        print("Its an equilateral triangle!")
    elif a!=b and b!=c and a!=c:
        print("its a scalene triangle!")
    else:
        print("its a isosceles triangle!")        


