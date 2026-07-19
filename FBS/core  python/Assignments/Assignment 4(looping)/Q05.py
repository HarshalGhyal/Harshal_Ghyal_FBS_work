#### Q5.WAP to print Fibonacci series upto n.

# lets take n as input.
n=int(input("How many fibonacci numbers you want:"))

#lets iniatialize var a and b.
a=-1
b=1 # why a is -1 and b is 1 because 1st fibonnaci number is 0.

# lets iterate:
for i in range(n):
    c=a+b
    print(c)
    a=b
    b=c
