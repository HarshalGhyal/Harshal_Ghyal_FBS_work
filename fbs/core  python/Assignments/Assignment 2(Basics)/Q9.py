#### Q9.Write a program to swap two numbers without using third variable.

#lets take two numbers as a input:
num1=int(input("enter your first number:"))

num2=int(input("enter your second number:"))

print(f'before swapping  numbers num1 was {num1} and num2 was {num2} ')

#lets swap them without third variable.

num1,num2=num2,num1

print(f'before swapping  numbers num1 is {num1} and num2 is {num2} ')
