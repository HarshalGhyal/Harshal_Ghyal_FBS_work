#### Q4.Write a program to input all sides of a triangle and check whether triangle is valid or not.

# lets take three sides of triangle as a input as a,b and c:

a=float(input("Enter side 1:"))
b=float(input("Enter side 2:"))
c=float(input("Enter side 3:"))

# as we know sides should follow this rule to make a valid triangle: a+b>c and a+c>b and b+c>a
#lets check:

if a+b>c and a+c>b and b+c>a:
    print(f'Given sides a:{a} , b:{b}, c:{c} makes valid triangle!')
else:
    print("given sides not makes a valid triangle!") 

      
