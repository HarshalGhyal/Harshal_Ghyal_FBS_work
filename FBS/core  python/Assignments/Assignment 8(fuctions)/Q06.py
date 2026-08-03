#### Q6. Write a program to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8...n terms

def fibonacci(n):
    a=-1
    b=1
    for i in range(n):
        c=a+b
        if c!=0:
            print(c,end="  ")
        a=b
        b=c

n=int(input("Enter n:"))

fibonacci(n)