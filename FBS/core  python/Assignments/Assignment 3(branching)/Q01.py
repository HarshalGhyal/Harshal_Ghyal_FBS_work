#### Q1.Write a program to check if the given number is positive or negative.

#lets take input as a number first.
num=int(input("Enter your number:"))

# lets check whether its negative ,positive or zero:

if num>0:
    print(f'{num} is positive number')
elif num<0:
    print(f'{num} is negative number')
else:
    print("it is a zero!")    
