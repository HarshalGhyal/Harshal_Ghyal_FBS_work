#### Q7.Find the sum of three-digit number.

#lets take input as a three digit number
number=int(input("Enter your three digit number:"))

#lets take out one by one digit.

d1=number%10  #this will give us the last digit of the number.
a=number//10  #this will give us the first two digits of the number.

d2=a%10  #this will give us the second digit of the number.
d3=a//10  #this will give us the first digit of the number.

#lets calculate the sum of three digit number.
sum=d1+d2+d3

#lets display the output:
print(f"The sum of three digit number {number} is {sum}")
