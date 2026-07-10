#### Q7. write a program to find the roots of quadratic equation.
# import math
# qudratic eqn is written as ax^2+bx+c=0
# as per our root formula we have take 3 inputs. formula is -b+ or - under root b^2-4ac/2a

a=float(input("enter the value of a:"))

b=float(input("enter the value of b:"))

c=float(input("enter the value of c:"))

# lets calculate under root value first that is b^2-4ac

d=b**2-4*a*c

root1=(-b + d**0.5)/(2*a)
root2=(-b - d**0.5)/(2*a)

#lets display the output

print(f"so for our given quadratic equation two roots are {root1} and {root2}")