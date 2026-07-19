#### Q4.WAP to print factorial of a number

# lets take input as number.
num=int(input("Enter number:"))

# let initalize var
fact=1

# lets iterate:
for i in range(num,0,-1):
    fact*=i
print(f'The factorial of {num} is {fact}')    