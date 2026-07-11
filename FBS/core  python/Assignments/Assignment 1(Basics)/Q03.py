#### Q3.write a program to find quotient and reamainder of two numbers.

#first we gonna take two nubers from user let it  a and b
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))

#as we know for normal devision we use "/" in python and it gives us quotient and to get remainder we have '%' also k/a modulas division.

quotient=a//b
remainder=a%b

# lets display the outputs

print(f"the quotient and reaminder of {a} and {b} are quotient:{quotient} ,remainder:{remainder}")
