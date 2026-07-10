#### Q8.Write a program to swap two numbers using third variable.
 
#lets take two numbers as a input:
num1=int(input("enter your first number:"))

num2=int(input("enter your second number:"))

print(f'before swapping  numbers num1 was {num1} and num2 was {num2} ')

# lets swap two number using third variable as temp.
temp=num1

num1=num2

num2=temp

print(f'after swapping numbers now, num1 is {num1} and num2 is {num2}')


